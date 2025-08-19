#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  7 11:22:20 2025

@author: joshuaweston
"""

from ast import literal_eval
from os.path import exists
from pyvo import registry
import pandas as pd
import os
import gc
import warnings
from itertools import combinations
from collections import defaultdict


class catalogue:
     
    def __init__(self,doi,fp='lestrade/catalogues/'):
        
        import re
        import os
        import lestrade
        
        self._doi = doi
        self._doi_tidy = re.sub(r'[<>:"/\\|?*]', '_', self._doi).strip()
        #self._directory = fp
        
        self._directory = os.path.dirname(lestrade.__file__)+'/catalogues/'
        
        #need to get autowiki instance
        
        #best zsp, best zph, associated quality flags, morphology, type flags
    
        from lestrade.autowiki.page import autowiki
        
        summary = autowiki(doi=self._doi)
        
        self._zsp = summary._best_zsp
        
        self._q_zsp = summary._q_zsp
        self._e_zsp = summary._e_zsp
        
        
        self._zph = summary._best_zph
        
        self._q_zph = summary._q_zph
        self._e_zph = summary._e_zph
        
        self._a = summary._a_best
        
        self._b = summary._b_best
        
        self._pa = summary._pa_best
        
        self._types = summary._type_labels
        
        
    def get_combined_catalogue(self):
        
        
        if os.path.exists(f"{self._directory}{self._doi_tidy}/{self._doi_tidy}_cm.csv"):
                
            combined_df = pd.read_csv(f"{self._directory}{self._doi_tidy}/{self._doi_tidy}_cm.csv")
            
            self._catalogue_concat = combined_df
            
        else:
            
            import gc
            import warnings

            warnings.simplefilter(action="ignore", category=pd.errors.DtypeWarning)
            warnings.simplefilter("ignore", category=FutureWarning)

            #download every table and extract columns where necessary: ra, dec, zsp, zph, a, b, pa, type flags
            
            catalogue_ivoid = f"ivo://CDS.VizieR/{self._doi}"
            
            voresource = registry.search(ivoid=catalogue_ivoid)[0]
                
            tables = voresource.get_tables()
                    
            no_tables = len(tables)
            
            
            self._catalogue_concat = None
            
            for i in range(0,no_tables):
                
                self.download_table(i,save=True) #create df_latest
            
                if self._catalogue_concat is not None:
                    
                    self._catalogue_concat = pd.concat([self._catalogue_concat, self._df_latest],ignore_index=True)
                    
                else:
                    
                    cols = ['RA','DEC','ZSP','ZPH','A','B','THETA','q_ZSP','e_ZSP','q_ZPH','e_ZPH','Classes']
                    
                    self._catalogue_concat = pd.DataFrame(columns=cols)
                    
                    self._catalogue_concat = pd.concat([self._catalogue_concat, self._df_latest],ignore_index=True)
            
            
            
            #save combined data
            
            
            self._catalogue_concat.to_csv(f'{self._directory}{self._doi_tidy}/{self._doi_tidy}_cm.csv')
            
            
    def download_table(self,table_no,save=False):
        
        catalogue_ivoid = f"ivo://CDS.VizieR/{self._doi}"   
        
        try:
            
            voresource = registry.search(ivoid=catalogue_ivoid)[0]
                
            tables = voresource.get_tables()
                    
            tables_names = list(tables.keys())    
            # get the numbered table of the catalogue
            
            table_name = tables_names[table_no]
            
        except:
            
            print(f'Unable to find table {table_no} in {catalogue_ivoid}. Check the ID and table number are correct.')
            
            return
        
        filename = self._doi_tidy
        

        if not os.path.exists(f'{self._directory}{filename}/'):
            os.makedirs(f'{self._directory}{filename}/')
        
        
        #searching for table data
        if exists(f'{self._directory}{filename}/{os.path.basename(table_name)}.csv'):
            
            df = pd.read_csv(f'{self._directory}{filename}/{os.path.basename(table_name)}.csv')
            
        else:
            
            #download the table
            tap_service = voresource.get_service("tap")
            
            offset = 0
            chunk_size=100000
            df_list=[]
            last_index= 0
            index_candidates = ['recno', 'seq', 'Seq']

            for candidate in index_candidates:
                try:
                    
                    # Try to run a tiny test query using this candidate index
                    test_query = f"""
                    SELECT TOP 1 {candidate}
                    FROM "{table_name}"
                    ORDER BY {candidate}
                    """
                    test_result = voresource.get_service("tap").run_sync(test_query)
                    _ = test_result.to_table().to_pandas()  # Will raise if column doesn't exist
            
                    index = candidate  # Success!
                    print(f"Using index column: {index}")
                    break  # Exit loop once one works
            
                except Exception as e:
                    print(f"Failed with index '{candidate}': {e}")
            
            else:
                # This runs if no break occurred (i.e. all candidates failed)
                index = None
                
                
            offset = 0
            chunk_size=100000
            df_list=[]
            last_index= 0    
                
            if index:
                
                
                try:
                
                    while True:
                    
                        print(f"Pulling rows {offset} - {offset+chunk_size}")
                        
                            
                        query = f"""
                        SELECT TOP {chunk_size} * 
                        FROM "{table_name}"
                        WHERE {index} > {last_index}
                        ORDER BY {index}
                        """
                            
                        tap_records = voresource.get_service("tap").run_sync(
                            query,
                            )
                            
                    
                        chunk_df = tap_records.to_table().to_pandas()
                        df_list.append(chunk_df)
                        offset+= chunk_size
                        
                        last_index = chunk_df[index].max()
                        
                        if len(chunk_df) < chunk_size:
                            break
                    
                except:
                        
                     query = f"""
                     SELECT * 
                     FROM "{table_name}"
                     """
                            
                     tap_records = voresource.get_service("tap").run_sync(
                         query,
                         )
                        
                     chunk_df = tap_records.to_table().to_pandas()
                        
                     df_list.append(chunk_df)
                     
            else:
                
                query = f"""
                SELECT * 
                FROM "{table_name}"
                """
                    
                tap_records = voresource.get_service("tap").run_sync(
                    query,
                    )
                
                chunk_df = tap_records.to_table().to_pandas()
                
                df_list.append(chunk_df)
            
            df = pd.concat(df_list,ignore_index=True)
            
            if save==True:

                df.to_csv(f'{self._directory}{filename}/{os.path.basename(table_name)}.csv') 
                
                
            
                
        cols = ['RA','DEC','ZSP','ZPH','A','B','THETA','q_ZSP','e_ZSP','q_ZPH','e_ZPH','Classes']
        
        df.rename(columns={'RAJ2000':'RA',
                           'DEJ2000':'DEC',
                           self._zsp:'ZSP',
                           self._zph:'ZPH',
                           
                           self._e_zsp:'e_ZSP',
                           self._q_zsp:'q_ZSP',
                           
                           self._e_zph:'e_ZPH',
                           self._q_zph:'q_ZPH',
                           
                           self._a:'A',
                           self._b:'B',
                           self._pa:'THETA',
                           }, inplace=True)   
        self._df_latest = df.reindex(columns=cols, fill_value=None)


        
        
    

        
        
        
        