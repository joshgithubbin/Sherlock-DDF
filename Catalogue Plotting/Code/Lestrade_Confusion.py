#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 15:17:05 2025

@author: joshuaweston
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def lcon(df,remove_notruematch=False,remove_blended=False,remove_spikes=False):
    
    subtitle = ''
    
    cmap = 'Reds'
    if remove_notruematch:
    
        df = df[df.truematch_exist != 'NO']
        
        subtitle = 'Complete'
        
        cmap = 'Blues'
    
        if remove_blended:
            
            df = df[df.Blended != 1]
        
            subtitle += ', Non-Blended'
    
            cmap = 'Greens'
    
            if remove_spikes:
                
                df = df[(df['DLR Spike'] == 0) & (df['A-Value Spike'] == 0)]
                
                subtitle += ', No-Spike'

                cmap = 'Oranges'

    if subtitle == '':
        
        subtitle = 'All'

    df['DLR target'] = (df['DLR MATCH'] == 'YES').astype(int)
    df['A-Value target'] = (df['A-Value MATCH'] == 'YES').astype(int)
    
    
    cm = confusion_matrix(df['DLR target'], df['A-Value target'])
    
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
    disp.plot(cmap=cmap, ax=ax, colorbar=False)
    
    ax.set_xlabel('A-Value Target', fontsize=12)
    ax.set_ylabel('DLR Target', fontsize=12)
    
    plt.title(f'DLR vs A-Value ({subtitle} Cases)')
    plt.show()
    
    return