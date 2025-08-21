#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:49:14 2025

@author: joshuaweston
"""

def annotate_matches(transient_matches, annotations, label):
    
    matched_columns = [col for col in transient_matches.columns if 'GalID' in col]
    
    for col in matched_columns:
        
        transient_matches[f'{col} Label'] = ''
        
        transient_matches[f'{col} Label'] += transient_matches[col].isin(
            annotations['GalID']
        ).map({True: label, False: ''})
    
    return transient_matches
