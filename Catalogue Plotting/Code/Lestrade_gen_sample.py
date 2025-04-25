#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 14:23:07 2025

@author: joshuaweston
"""
import pandas as pd
from searchcat import *
from Imports import *
from DDFs import *

def gen_sample(filepath,field,
               DDF_path='../DDF_Coordinates.csv',catlist='../Catalogue_List.csv',
               finalpath=None):
    
    #load sample from path provided
    
    if finalpath:
        
        subset_df = pd.read_csv(finalpath)
        
        return subset_df
    
    ddfs,ddfs_pd = load_ddfs(path=DDF_path)
    
    cdf = load_catalogue_table(path=catlist)
    
    df = pd.read_csv(filepath)
    
    subset_df = search_catalogue(df,'RA','DEC',ddfs[field]['RAdeg'],ddfs[field]['DECdeg'],ddfs[field]['Diameter']*1.2)
    
    if finalpath:
        
        subset_df.to_csv(finalpath)
    
    return subset_df
    
    
    