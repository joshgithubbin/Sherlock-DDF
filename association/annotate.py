#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:49:14 2025

@author: joshuaweston
"""

def annotate_matches_old(transient_matches, annotations, label):
    
    matched_columns = [
    col for col in transient_matches.columns 
    if "GalID" in col and "Label" not in col
    ]
    
    for col in matched_columns:
        transient_matches[f'{col} Label'] = ''
        
        transient_matches[f'{col} Label'] += transient_matches[col].isin(
            annotations['GalID']
        ).map({True: label, False: ''})
    
    return transient_matches

def overwrite_matches(transient_matches, annotations, metric):
    
    match_col = f"{metric} MATCH"
    overwritten_col = f"{metric} Overwritten"
    # Initialize column with "NO"
    transient_matches[overwritten_col] = "NO"

    # Update where SNID is in annotations
    mask = transient_matches["SNID"].isin(annotations["SNID"])
    transient_matches.loc[mask, match_col] = "YES"
    transient_matches.loc[mask, overwritten_col] = "YES"

    return transient_matches

import numpy as np

def annotate_matches(transient_matches, annotations, label):
    matched_columns = [
        col for col in transient_matches.columns 
        if "GalID" in col and "Label" not in col
    ]
    
    for col in matched_columns:
        label_col = f"{col} Label"
        
        # If label column doesn't exist yet, initialize with empty string
        if label_col not in transient_matches.columns:
            transient_matches[label_col] = ""
        
        # Create mask for matches
        mask = transient_matches[col].isin(annotations["GalID"])
        
        # Append label only if it's not already present
        transient_matches.loc[mask, label_col] = transient_matches.loc[mask, label_col].apply(
            lambda x: f"{x},{label}" if label not in x.split(",") else x
        ).str.strip(",")
    
    return transient_matches
