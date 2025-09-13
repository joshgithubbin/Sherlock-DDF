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

import pandas as pd

def annotate_matches(transient_matches, annotations, label):
    matched_columns = [
        col for col in transient_matches.columns 
        if "GalID" in col and "Label" not in col
    ]
    
    for col in matched_columns:
        label_col = f"{col} Label"
        
        # Ensure label column exists and is string-typed
        if label_col not in transient_matches.columns:
            transient_matches[label_col] = ""
        else:
            transient_matches[label_col] = transient_matches[label_col].fillna("").astype(str)
        
        # Mask where GalID is in the annotations
        mask = transient_matches[col].isin(annotations["GalID"])
        
        def add_label(x):
            if not x or pd.isna(x):
                return label
            parts = [p for p in str(x).split(",") if p]
            if label not in parts:
                parts.append(label)
            return ",".join(parts)
        
        transient_matches.loc[mask, label_col] = (
            transient_matches.loc[mask, label_col].apply(add_label)
        )
    
    return transient_matches

