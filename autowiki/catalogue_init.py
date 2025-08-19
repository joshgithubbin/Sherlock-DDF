#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 09:43:27 2025

@author: joshuaweston
"""


def gen_ls_cat(rac,dec,d,cats):
    
    #rac - centre of ddf
    #dec - centre of ddf
    #d - diameter of ddfs
    #cats - list of cds bibcodes
    import sys
    sys.path.insert(1, '/Users/joshuaweston/Desktop/Live/lestrade/')

    from browser import fields, search
    from download import catalogue
    import pandas as pd
    
    df = None
    
    for i in cats:
        
        #download catalogue
        df_j = catalogue(i[0])        
        
        df_j.get_combined_catalogue()
        
        df_j = df_j._catalogue_concat

        
        # Apply axis scale if A and B are present
        df_j['A'] *= i[1]

        df_j['B'] *= i[1]
        
        df_j['catalogue'] = i[0]
        
        #combine with others
        if df is not None:
            
            #crop catalogue
            df_i = search.search(rac,dec,d,df_j,'RA','DEC')
            
            #combine
            df = pd.concat([df, df_i],ignore_index=True)
            
        else:
            
            #crop catalogue
            df_i = search.search(rac,dec,d,df_j,'RA','DEC')
            
            #initialize
            df = df_i

    cols = ['RA','DEC','ZSP','ZPH','A','B','THETA','q_ZSP','e_ZSP','q_ZPH','e_ZPH','Classes','catalogue']
    
    return df[cols]


XMM_LSS = [["J/ApJS/235/36",1],
           ["J/A+A/616/A55",1]]

ECDFS = [["II/253A",1.0/3600.]]
    
import sys
sys.path.insert(1, '/Users/joshuaweston/Desktop/Live/lestrade/')
from browser import fields, search
ddfs, ddfs_pd = fields.load_ddfs(
        path="/Users/joshuaweston/Desktop/Live/lestrade/tools/fields/fields.csv"
    )

rac = ddfs['XMM-LSS']['RAdeg']
dec = ddfs['XMM-LSS']['DECdeg']
d = ddfs['XMM-LSS']['Diameter']

df = gen_ls_cat(rac,dec,d,XMM_LSS)
