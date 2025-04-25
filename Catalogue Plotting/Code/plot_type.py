#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 13:59:34 2024

@author: joshuaweston
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import itertools

def plot_type(field, df, z, savefig=False, savename="field", subfolder=False, log_threshold=100):
    
    # Temporarily set the style to ggplot
    plt.style.use('ggplot')

    # Extract ggplot colors
    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Revert to the original style
    plt.style.use('default')
    
    # Number of groups (each unique value in the z list)
    categories = [df[col].value_counts() for col in z]  # Count values for each category in z
    unique_vals = [list(c.index) for c in categories]   # Get the unique values for each z
    
    # Create an index based on the number of unique categories in z[0] (for positioning the bars)
    indices = np.arange(len(unique_vals[0]))  # Assuming the first z group defines the categories

    bar_width = 0.2  # Width of each bar
    opacity = 0.7

    # Start creating the grouped bar chart
    fig, ax = plt.subplots()

    # Collect all the counts to determine min and max for log scale decision
    all_counts = list(itertools.chain.from_iterable([cat.values for cat in categories]))
    
    if not all_counts:
        return
    
    max_count = max(all_counts)
    min_count = min(all_counts)


    # Check if the difference between max and min counts exceeds the threshold
    if max_count / min_count > log_threshold:
        
        ax.set_yscale('log')  # Set y-axis to logarithmic if the condition is met

    for i, cat_counts in enumerate(categories):
        ax.bar(indices + i * bar_width, cat_counts.values, bar_width, label=z[i], alpha=opacity)
    
    # Set the properties of the chart
    ax.set_xlabel('Categories')
    ax.set_ylabel('Frequency')
    ax.set_title(f'{field} Category Counts', fontweight='bold')
    ax.set_xticks(indices + bar_width * (len(z) - 1) / 2)  # Adjust the ticks to the middle of grouped bars
    ax.set_xticklabels(unique_vals[0])  # Assuming the first z group defines the categories
    ax.legend()

    if subfolder:
        field = f'{field}/{subfolder}'
        
    # Save the figure if required
    if savefig:
        fn = f"../Plots/{field}/{savename}_classes.png"
        plt.savefig(fn, dpi=savefig)

    plt.show()
    
    # Revert to the original style
    plt.style.use('default')
    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']