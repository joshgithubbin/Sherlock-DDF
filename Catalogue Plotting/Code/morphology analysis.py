#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 09:39:16 2025

@author: joshuaweston
"""

import Lestrade_Catalogues as lcat
import Lestrade_gen_sample as lgs
import Lestrade_DLR as ldlr
import Lestrade_AV as lav
import Lestrade_Overwrite_Matches as lom

import pandas as pd
import os

from Lestrade_Plotting import *

ECDFS = {
    
    "ACS-GC": {
        "ZPH": "zph",
        "ZSP": "zsp",
        "A": "a1", 
        "B": "b1", 
        "PA": "PA1",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag"
    },
    
    "Chandra-Multi": {
        "ZPH": "MCz",
        "A": "MajAxis", 
        "B": "MinAxis", 
        "PA": "PA",
        "u": "usMAG", 
        "g": "gsMAG", 
        "r": "rsMAG"
    },
    
    "GOOD-S-CANDELS": {
        "A": "a(H)", 
        "B": "b(H)", 
        "PA": "PA"
    }}

XMM_LSS = {
    "SPLASH-SXDF": {
        "ZSP": "zspec", 
        "ZPH": "zphot",
        "A": "amaj", 
        "B": "bmin", 
        "PA": "PA",
        "u": "umagC", 
        "g": "gmagC", 
        "r": "rmagC", 
        "i": "imagC", 
        "z": "zmagC"
    },
    
    "CFHQSIR": {
        "A": "AaxisY", 
        "B": "BaxisY", 
        "PA": "thetaY",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag", 
        "y": "ymag"
    },
    
}

COSMOS = {
    "COSMOS2020-CLASSIC": {
        "ZPH": "EZzphot",
        "A": "ACSAWorld", 
        "B": "ACSBWorld", 
        "PA": "ACSthetaWorld",
        "u": "CFHTumag", 
        "g": "HSCgmag", 
        "r": "HSCrmag", 
        "i": "HSCimag", 
        "z": "HSCzmag",
        "y": "HSCymag"
    },
    
    "ACS-GC": {
        "ZPH": "zph",
        "ZSP": "zsp",
        "A": "a1", 
        "B": "b1", 
        "PA": "PA1",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag",
        
        "axis_scale": 0.03/3600.
    }
}

ECDFS_2 = {
    
    "ACS-GC": {
        "ZPH": "zph",
        "ZSP": "zsp",
        "A": "a1", 
        "B": "b1", 
        "PA": "PA1",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag",
        
        "axis_scale": 0.03/3600.
    },
    
    "Chandra-Multi": {
        "ZPH": "MCz",
        "A": "MajAxis", 
        "B": "MinAxis", 
        "PA": "PA",
        "u": "usMAG", 
        "g": "gsMAG", 
        "r": "rsMAG",
        
        "axis_scale": 1.0/3600.
    },
    
    "GOODS-S-CANDELS": {
        "A": "a(H)", 
        "B": "b(H)", 
        "PA": "PA",
        
        "axis_scale": 0.06/3600
    }}


def plot_histogram2(field,field_str,scale='linear'):
    
    df = lcat.gen_cat(field,field_str)
    
    df_filtered = df.loc[(df['A']!=0)]
    
    #df_filtered = df[(df['A'] >= 0) & (df['A'] < 100)]  # Keep A values within range
    categories = df_filtered['CATALOGUE'].unique()  # Unique categories
    colors = plt.cm.tab10(np.linspace(0, 1, len(categories)))  # Distinct colors

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))  # Create two side-by-side plots

    # Histogram of A
    for cat, color in zip(categories, colors):
        subset = df_filtered[df_filtered['CATALOGUE'] == cat]['A']
        axes[0].hist(subset, bins=30, alpha=0.6, label=str(cat), color=color, edgecolor='black')

    axes[0].set_xlabel('A')
    axes[0].set_ylabel('Count')
    axes[0].set_yscale('log')  # Log scale for better visualization
    axes[0].legend(title='Category')

    # Scatter plot of Ellipticity vs A
    df_filtered['Ellipticity'] = 1 - (df_filtered['B'] / df_filtered['A'])
    
    for cat, color in zip(categories, colors):
        subset = df_filtered[df_filtered['CATALOGUE'] == cat]
        axes[1].scatter(subset['A'], subset['Ellipticity'], alpha=0.5, color=color, label=str(cat), s=10)

    axes[1].set_xlabel('A')
    axes[1].set_ylabel('Ellipticity (1 - B/A)')
    axes[1].set_title('Ellipticity vs A')
    axes[1].legend(title='Category')
    
    
    axes[1].set_xscale(scale)


    plt.tight_layout()  # Adjust layout
    plt.show()


# Call the function
plot_histogram2(XMM_LSS,'XMM-LSS')
plot_histogram2(XMM_LSS,'XMM-LSS',scale='log')

#plot_histogram2(ECDFS,'ECDFS')
#plot_histogram2(ECDFS,'ECDFS',scale='log')

plot_histogram2(COSMOS,'COSMOS')
plot_histogram2(COSMOS,'COSMOS',scale='log')

plot_histogram2(ECDFS_2,'ECDFS')
plot_histogram2(ECDFS_2,'ECDFS',scale='log')