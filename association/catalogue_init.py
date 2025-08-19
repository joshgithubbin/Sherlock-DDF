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

    from lestrade.browser import fields, search
    from lestrade.autowiki.download import catalogue
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


