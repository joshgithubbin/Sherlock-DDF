"""
Created on Mon Jul  1 09:37:24 2024

@author: joshuaweston

Pulls catalogue data from a list and creates datasets for DDF plotting and summarising.

INPUT:
    -Catalogue_List.csv
    
OUTPUT:    

"""

import pandas as pd
from Imports import *
from DDFs import *
from searchcat import *
from fieldplot import *
from redshift_plotting import *
from plot_type import *
from pathlib import Path
import gc
import warnings

warnings.filterwarnings(
    "ignore",
    message=".*W02: .* is not a valid datatype according to the VOSI spec.*",
)

ddfs,ddfs_pd = load_ddfs(path='../DDF_Coordinates.csv')

cdf = load_catalogue_table(path='../Catalogue_List.csv')

for index, row in cdf.iterrows():
    
    if isinstance(row['Key'],str):
        
        df,df_name,df_ID = import_and_merge(row,row['Key'],directory='../Catalogues/'),row['Name'],row['ID']

    else:
        #return table name, ID as well
        df,df_name,df_ID = import_catalogue(row,directory='../Catalogues/'),row['Name'],row['ID']
    
    print(df.columns)
    print("Searching catalogue:")
    #loop through for each ddf
    for i in ddfs:
        
        z_ddf=[]
        z_ddf_labels=[]
        
        filename = f'../Catalogues/SubCatalogues/{df_name}_{i}.csv'
        
        if exists(filename):
            
            print(f"Catalogue subset for {i} already exists. Importing . . .")
            
            subset = pd.read_csv(filename)

        else:
            
            subset = search_catalogue(df,row['RA Column'],row['DEC Column'],ddfs[i]['RAdeg'],ddfs[i]['DECdeg'],ddfs[i]['Diameter']*1.2)

            #save subset
            if subset.empty == False:
            
                print(f"Items found in {i}. Saving subset . . .")
            
                subset.to_csv(filename)
            
                print(f"Subset saved to csv under Catalogues/SubCatalogues/{df_name}_{i}.csv. \n")

        if subset.empty == False:
            
            Path(f"../Plots/{i}/{df_name}").mkdir(parents=True, exist_ok=True)
            
            fieldplot(i, df_name,
                      ddfs[i]['RAdeg'],ddfs[i]['DECdeg'],subset[row['RA Column']],subset[row['DEC Column']],
                      color=ddfs[i]['Colour'],size=row['Marker size'],
                      savefig=400,directory='../Plots')
                        
            if row['Best Z'] == row['Best Z']:
                                
                #z_ddf.append(subset[row['Best Z']])
                #z_ddf_labels.append(df_name)
                

                #plot best z
                plot_zhist(i,subset[row['Best Z']],labels=df_name,savefig=400,savename=f'{df_name}/{i}_{df_name}')
                plot_zhist_stacked(i,subset,row['Z'],savefig=400,savename=f'{df_name}/{i}_{df_name}')
                plot_pairwise_comparisons(i,subset,row['Z'],savefig=400,savename=f'{df_name}/{i}_{df_name}')
            
                if not isinstance(row['Quality_Flags'],float):
                    
                    plot_redshift_quality_histogram(i, subset, row['Z'], row['Quality_Flags'],savefig=400,savename=f'{df_name}/{i}_{df_name}')
            
            if not isinstance(row['Type_Flag'],(float,type(None))):
                

                plot_type(i,subset,row['Type_Flag'],savefig=400,savename=f'{df_name}/{i}_{df_name}')
                
        # Cleanup: Delete subset dataframe and force garbage collection
        del subset
        gc.collect()
    
    # Cleanup: Delete main dataframe and force garbage collection
    del df
    gc.collect()
            
                
    
            

