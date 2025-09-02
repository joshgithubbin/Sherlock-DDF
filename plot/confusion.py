#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  2 17:07:38 2025

@author: joshuaweston
"""

def compare_methods(df,method1, method2,fp,cmap='Blues',subtitle=None):

    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    import os
    
    df[f'{method1} target'] = (df[f'{method1} MATCH'] == 'YES').astype(int)
    df[f'{method2} target'] = (df[f'{method2} MATCH'] == 'YES').astype(int)
    
    cm = confusion_matrix(df[f'{method1} target'], df[f'{method2} target'])
    
    fig, ax = plt.subplots(figsize=(6, 6))
    
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
    disp.plot(cmap=cmap, ax=ax, colorbar=False)
    
    ax.set_xlabel(f'{method2} Target', fontsize=18)
    ax.set_ylabel(f'{method1} Target', fontsize=18)
    
    title = f'{method1} vs {method2}'
    
    if subtitle:
        
        title += f' {subtitle}'
    
    plt.title(title,fontsize=24)
    
    for text in disp.text_.ravel():
        text.set_fontsize(28)
        
    plt.savefig(fp, dpi=400)
    plt.close()