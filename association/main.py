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
             check=False, #compare to true hosts in sample
             
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
                                                                                           
                                              Version 0.5.1            
                                                                                                    
                                              
                                                                                                    
    """
    
    print(art)

    import lestrade
    import os
    import pandas as pd
    
    #determine output folder
    fp_a = f'{os.path.dirname(lestrade.__file__)}/output/'

    fp_b = f'{os.path.splitext(os.path.basename(sample))[0]}/{field}'
    
    fp_c = f'{os.path.splitext(os.path.basename(sample))[0]}_{field}'
    
    output_file = f"{fp_a}{fp_b}/base/{fp_c}"
    
    # Ensure the directory exists
    os.makedirs(f"{fp_a}{fp_b}/base/", exist_ok=True)
    
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
        
        field_cat['GalID'] = range(1, len(field_cat) + 1)
        
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

        
        module = importlib.import_module(association_method)
        
        subset_output = apply_method(subset, field_cat, module, metric,r,ms,n)
        
        subset_output.to_csv(f'{output_file}.csv',index=False)
        
        
        #then we do the annotation

        if annotate:
            
            from lestrade.association.annotate import annotate_matches
            
            annotation_folder = f"{fp_a}{fp_b}/config"
            
            output_file = f"{fp_a}{fp_b}/annotated/{fp_c}_annotated.csv"   
            
            # Ensure the directory exists
            os.makedirs(annotation_folder, exist_ok=True)
            
            os.makedirs(f"{fp_a}{fp_b}/annotated/", exist_ok=True)
            
            files = ['blended', 'ds']
            
            for fname in files:
                
                file_path = os.path.join(annotation_folder, f"{fname}.csv")
                
                if not os.path.exists(file_path):
                    # Create empty dataframe and save it
                    df = pd.DataFrame(columns=['GalID'])
                    df.to_csv(file_path, index=False)
                else:
                    # Read existing dataframe
                    df = pd.read_csv(file_path)
                    
                    #now go through and identify catalogue items to annotate
                    #for each item in subset_output, if host id exists in catalogue, flag
                    annotate_matches(subset_output,df,fname)                    

                #save
                subset_output.to_csv(output_file,index=False)
        
        field_cat.to_csv(f"{fp_a}{fp_b}/catalogue.csv",index=False) 
        
        if check:
            
            #check if the true host exists in the catalogue
            
            
            #if so, check whether the true host is consistent with the method-identified host
            pass

    return subset_output




