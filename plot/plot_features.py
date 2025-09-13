#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  3 13:13:23 2025

@author: joshuaweston
"""

def plot_features(subset_output, metric, fp, consistency_split):

    # Exclusion keywords
    exclude = [" A", " B", " PA", " RA", " DEC", "MATCH", "GalID", "Label", " z", "Overwritten"]

    # Select columns that start with the metric and do not contain any exclude keyword
    features = [
        col for col in subset_output.columns
        if col.startswith(metric) and not any(ex in col for ex in exclude)
    ]
    
    
    #now plot histogram!
    
    for feature in features:
        
        histplot(subset_output,feature,metric,consistency_split,filepath=fp)
            
    
    return 

def histplot(df, column, method, consistency_split=False, scale='log',filepath=''):
    
    import matplotlib.pyplot as plt
    import numpy as np
        
    if consistency_split:
        
        df_yes = df[df[f'{method} MATCH'] == 'YES']
        df_no = df[df[f'{method} MATCH'] == 'NO']
        df_no[column] = df_no[column].replace([np.inf, -np.inf], np.nan).dropna()
        df_yes[column] = df_yes[column].replace([np.inf, -np.inf], np.nan).dropna()

        plt.hist(df_yes[column], bins=30, alpha=0.5, label=f'{method} MATCH = YES', color='green')
        plt.hist(df_no[column], bins=30, alpha=0.5, label=f'{method} MATCH = NO', color='red')
        
        figname = f'{column}_split.png'
        
    else:
        
        plt.hist(df[column], bins=30, alpha=0.5, label=f'{method} MATCH = YES', color='blue')
        
        figname = f'{column}.png'

    plt.title('')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.legend()
    plt.yscale(scale)
    plt.grid(True)
    
    plt.savefig(f'{filepath}{figname}',dpi=400)
    
    plt.close()
