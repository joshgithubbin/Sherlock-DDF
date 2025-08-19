#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 12:18:44 2025

@author: joshuaweston
"""

def lestrade(sample,field,catalogues, #list of transients, deep drilling field, catalogues for matching
             metric, #method of association
             overwrite=True, #overwrite relevant columns
             annotate=True, #check for annotations
             
             r=15,
             ms=0.8,
             n=2
             ):
    
    art = r"""
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                   &&&                                                                              
                   &&&                                                    &&&                       
                   &&&                        &&                          &&&                       
                   &&&        &&&&&&  &&&&&&&&&&&&&&&& &&&  &&&&&    &&&&&&&&  &&&&&&&              
                   &&&      &&&   && &&&&    &&&   &&&&    &   &&&  &&&   &&& &&&   &&&             
                   &&&      &&&&&&&&& &&&&   &&&   &&&       &&&&& &&&    &&& &&&&&&&&&             
                   &&&      &&&         &&&& &&&   &&&    &&&  &&& &&&    &&& &&&                   
                  &&&&&&&&&&&&&&&  & &&  &&& &&&& &&&&    &&&  &&&  &&&&  &&& &&&&&  &              
                  &&&&&&&&&   &&&&&& &&&&&&   &&&&&&&&     &&&&&&&   &&&&&&&&   &&&&&&                                  
                                                                                           
                                              Version 0.4.1            
                                                                                                    
                                              
                                                                                                    
    """
    
    print(art)

    import lestrade
    import os
    import pandas as pd
    
    #determine output folder
    fp_a = f'{os.path.dirname(lestrade.__file__)}/output/'

    fp_b = f'{os.path.splitext(os.path.basename(sample))[0]}/{field}'
    
    fp_c = f'{os.path.splitext(os.path.basename(sample))[0]}_{field}'
    
    output_file = f"{fp_a}{fp_b}/{fp_c}"
    
    if annotate:
        
        output_file +='_annotated.csv'     
        
    else:   
        
        output_file +='.csv'
        
    
    # Ensure the directory exists
    os.makedirs(fp_a+fp_b, exist_ok=True)
    
    #check for overwrite
    if os.path.exists(output_file) and not overwrite:
        
        df_final = pd.read_csv(output_file)
        
    else:
        
        
        if os.path.exists(output_file):
            
            
            transients = pd.read_csv(output_file)
            
        else:
            
            transients = pd.read_csv(sample)
        
        #build the catalogue
        import lestrade.association.catalogue_init as l_cinit
        from lestrade.browser import fields,search
                
        ddfs, ddfs_pd = fields.load_ddfs(
                path=os.path.dirname(lestrade.__file__)+'/tools/fields/fields.csv'
            )

        rac = ddfs[field]['RAdeg']
        dec = ddfs[field]['DECdeg']
        d = ddfs[field]['Diameter']*1.2
        
        field_cat = l_cinit.gen_ls_cat(rac,dec,d,catalogues)
        
        
        #constrain the sample
        subset = search.search(
            ddfs[field]['RAdeg'],
            ddfs[field]['DECdeg'],
            ddfs[field]['Diameter'] * 1.2,
            transients,
            'RA',
            'DEC'
        )
        
        #now we need to apply the relevant method to the subset
        
        from lestrade.association.base_assoc import apply_method
        
        association_method = f'lestrade.association.methods.{metric}'
        
        import importlib

        # Correct import of the module:
        
        module = importlib.import_module(association_method)
        
        # Pass the module, not the function
        subset_output = apply_method(subset, field_cat, module, metric,r,ms,n)
        
        
        #then we do the annotation
        if annotate:
            pass

        #save
        subset_output.to_csv(output_file) 
                

    return subset_output




