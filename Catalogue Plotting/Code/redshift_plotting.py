#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:08:47 2024

@author: joshuaweston
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import itertools
import matplotlib.animation as animation

def plot_zhist(field,z,labels="",savefig=False,savename="field"):
   
    plt.hist(z, label=labels, bins=np.arange(0,7.5,0.05).tolist(), edgecolor='black', alpha=0.7)
    
    plt.legend()
    plt.title(f'{field} Redshifts',fontweight='bold')
    plt.xlabel('Redshift')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    
    if savefig:
        
        fn = f"../Plots/{field}/{savename}_histogram.png"
        
        plt.savefig(fn,dpi=savefig)

    plt.show()

def plot_zhist_stacked_static(field, df, z, savefig=False, savename="field"):
    import matplotlib.pyplot as plt
    import numpy as np
    
    # Prepare the data for the histogram
    data = [df[col].dropna() for col in z]  # Ensure NaN values are excluded
    
    # Compute the total counts for each category
    counts = [len(col_data) for col_data in data]
    
    # Update the labels to include total counts
    labels = [f"{col} (n={count})" for col, count in zip(z, counts)]
    
    # Create the stacked histogram
    plt.hist(data, bins=np.arange(0, 7.5, 0.05).tolist(), edgecolor='black', alpha=0.7, label=labels, stacked=True)
    
    # Add title, labels, and legend
    plt.title(f'{field} Redshifts', fontweight='bold')
    plt.xlabel('Redshift')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    
    # Save the figure if savefig is True
    if savefig:
        fn = f"../Plots/{field}/{savename}_stacked_histogram.png"
        plt.savefig(fn, dpi=savefig)

    # Show the plot
    plt.show()
    
def plot_zhist_stacked(field, df, z, savefig=False, savename="field"):
    # Prepare the data for the histogram
    data = [df[col].dropna() for col in z]  # Ensure NaN values are excluded
    counts = [len(col_data) for col_data in data]  # Total counts per column
    labels = [f"{col} (n={count})" for col, count in zip(z, counts)]
    
    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Set the bins for the histogram
    bins = np.arange(0, 7.5, 0.05).tolist()
    
    # Initialize the stacked histogram plot with empty data
    hist_data = [np.zeros_like(bins[:-1]) for _ in z]
    
    # Function to update the plot
    def update_hist(i):
        # Update the data for the first i rows
        updated_data = [df[col].dropna().iloc[:i] for col in z]
        
        # Reset the histogram counts
        for idx, col_data in enumerate(updated_data):
            hist_data[idx] = np.histogram(col_data, bins=bins)[0]
        
        # Clear previous data in the plot
        ax.clear()
        
        # Plot the updated stacked histogram
        ax.hist(updated_data, bins=bins, edgecolor='black', alpha=0.7, label=labels, stacked=True)
        
        # Title, labels, and legend
        ax.set_title(f'{field} Redshifts', fontweight='bold')
        ax.set_xlabel('Redshift')
        ax.set_ylabel('Frequency')
        ax.legend(loc='upper right')
        
    # Create the animation
    anim = animation.FuncAnimation(fig, update_hist, frames=np.arange(0, len(df), 1000), interval=100, repeat=False)
    
    # Save the animation if savefig is True
    if savefig:
        fn = f"../Plots/{field}/{savename}_stacked_histogram_animation.gif"
        anim.save(fn, writer='ffmpeg', dpi=300)
    
    # Show the animation
    plt.show()

    
def plot_pairwise_comparisons(field,df, z,savefig=False,subfolder=False,savename="field"):
    n = len(z)
    
    # Temporarily set the style to ggplot
    plt.style.use('ggplot')

    # Extract ggplot colors
    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Revert to the original style
    plt.style.use('default')
    
    if n < 2:
        print("Not enough columns to plot pairwise comparisons.")
        return
    
    # Handle the case where len(z) == 2 separately
    if n == 2:
        fig, axes = plt.subplots(1, 1, figsize=(5, 5))
       # color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
        color_idx = 0
        
        color = color_cycle[color_idx % len(color_cycle)]
        axes.scatter(df[z[0]], df[z[1]], alpha=0.2, color=color)
        axes.set_xlabel(z[0],fontsize=18)
        axes.set_ylabel(z[1],fontsize=18)
        
    else:
        fig, axes = plt.subplots(n-1, n-1, figsize=(5 * (n-1), 5 * (n-1)))
        #color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
        color_idx = 0
        
        for i in range(1, n):
            for j in range(i):
                color = color_cycle[color_idx % len(color_cycle)]
                axes[i-1, j].scatter(df[z[j]], df[z[i]], alpha=0.2, color=color)
                axes[i-1, j].set_xlabel(z[j],fontsize=18)
                axes[i-1, j].set_ylabel(z[i],fontsize=18)
                color_idx += 1

        # Hide any empty subplots
        for i in range(n-1):
            for j in range(i+1, n-1):
                axes[i, j].set_visible(False)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.suptitle(f'{field} Redshifts',fontweight='bold',fontsize=10*n,x=0.55,y=1.05)
    
    if savefig:
        
        fn = f"../Plots/{field}/{savename}_redshifts.png"
        
        plt.savefig(fn,dpi=savefig)
        
    plt.show()
    
    # Revert to the original style
    plt.style.use('default')
    color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
    
def plot_redshift_quality_histogram(field, df, z, Q, savefig=False,savename="field"):
    """
    Plots histograms of redshift values from 'z' columns, grouped by corresponding quality flag values in 'Q'.
    If the quality flag is a float, it bins the values into 5 classes and then creates the histogram.

    Parameters:
    field (str): Title of the field.
    df (pd.DataFrame): DataFrame containing the redshift and quality flag columns.
    z (list): List of redshift column names.
    Q (list): List of corresponding quality flag column names ("" if no flag).
    savefig (bool): Whether to save the figure or not.
    savename (str): Filename for saving the figure.
    """
    
    for i, z_col in enumerate(z):
        # Check if there's a corresponding quality flag
        q_col = Q[i]
        
        if q_col == "":
            print(f"No quality flag for {z_col}, skipping...")
            continue
        
        if q_col not in df.columns or z_col not in df.columns:
            print(f"Column {q_col} or {z_col} does not exist in DataFrame, skipping...")
            continue
        
        # Get redshift and quality flag values
        redshift_vals = df[z_col]
        quality_vals = df[q_col]
        
        # Drop NaN values from both columns
        mask = ~redshift_vals.isna() & ~quality_vals.isna()
        redshift_vals = redshift_vals[mask]
        quality_vals = quality_vals[mask]

        plt.figure(figsize=(8, 6))
        
        # Check if quality flag is float or integer type
        if pd.api.types.is_float_dtype(quality_vals):
            # Bin the float values into 5 equal-width intervals
            num_bins = 5
            bins = np.linspace(quality_vals.min(), quality_vals.max(), num_bins + 1)
            binned_quality_vals = pd.cut(quality_vals, bins=bins, labels=[f'{round(b, 2)}-{round(bins[i+1], 2)}' for i, b in enumerate(bins[:-1])])

            # Plot the histogram for each bin
            for bin_label in binned_quality_vals.unique():
                plt.hist(redshift_vals[binned_quality_vals == bin_label], bins=np.arange(0, 7.5, 0.05), 
                         alpha=0.6, label=f'Quality {bin_label}', edgecolor='black')
            
            plt.title(f'Redshift vs Binned Quality Flag ({z_col})', fontweight='bold')
            plt.xlabel('Redshift')
            plt.ylabel('Frequency')
            plt.legend(loc='upper right')
        
        else:
            # Histogram plot for discrete quality flag
            unique_qualities = quality_vals.unique()
            for quality in unique_qualities:
                plt.hist(redshift_vals[quality_vals == quality], bins=np.arange(0, 7.5, 0.05), 
                         alpha=0.6, label=f'Quality {int(quality)}', edgecolor='black')
            
            plt.title(f'Redshift vs Quality Flag ({z_col})', fontweight='bold')
            plt.xlabel('Redshift')
            plt.ylabel('Frequency')
            plt.legend(loc='upper right')
        
        # Save figure if needed
        if savefig:
            fn = f"../Plots/{field}/{savename}_{z_col}_quality_plot.png"
            plt.savefig(fn, dpi=savefig)
        
        plt.show()
