"""
Created on Mon Jul  1 14:53:55 2024

@author: joshuaweston

Functions to load the catalogue table and subsequently load/import data.

"""

from ast import literal_eval
from os.path import exists
from pyvo import registry
import pandas as pd
import os
import warnings
from itertools import combinations
from collections import defaultdict
from fieldplot import *
from DDFs import *
from searchcat import *
from redshift_plotting_WIP import *

import gc
import warnings

warnings.filterwarnings(
    "ignore",
    message=".*W02: .* is not a valid datatype according to the VOSI spec.*",
)


def load_catalogue_table(path="Catalogue_List.csv"):
    """
    Loads the catalogue summary table.

    Parameters
    ----------
    path : STRING, optional
        Filepath of the summary table. The default is "Catalogue_List.csv" in the current directory.

    Returns
    -------
    filtered_cdf_use : PANDAS DATAFRAME
        Pandas dataframe with the correctly formatted table.

    """
    
    #import catalogue summary table
    full_cdf = pd.read_csv(path)
    
    # #filter out unused catalogues
    full_cdf_use = full_cdf[full_cdf['RA Column'].notna()].copy()
    
    
    #shared columns
    full_cdf_use['shared_columns'] = full_cdf_use['shared_columns'].apply(
        lambda x: [col.strip() for col in x.split(',')] if isinstance(x, str) else []
    )
    # group known RA/Dec column pairs
    def group_ra_dec(columns):
        ra_dec_pairs = [
            ('RAJ2000', 'DEJ2000'),
            ('RAdeg', 'DEdeg'),
            ('RA', 'DEC'),
            # add more pairs as needed
        ]
        cols = columns.copy()
        for ra, dec in ra_dec_pairs:
            if ra in cols and dec in cols:
                cols.remove(ra)
                cols.remove(dec)
                cols.append([ra, dec])  # insert grouped pair at the start (or change position if needed)
        return cols
    
    full_cdf_use['shared_columns'] = full_cdf_use['shared_columns'].apply(group_ra_dec)

    #redshifts
    full_cdf_use['spec_z'] = full_cdf_use['spec_z'].apply(
        lambda x: [col.strip() for col in x.split(',')] if isinstance(x, str) else []
    )
    
    full_cdf_use['photo_z'] = full_cdf_use['photo_z'].apply(
        lambda x: [col.strip() for col in x.split(',')] if isinstance(x, str) else []
    )
    
    full_cdf_use['qual_z'] = full_cdf_use['qual_z'].apply(
        lambda x: [col.strip() for col in x.split(',')] if isinstance(x, str) else []
    )
    
    full_cdf_use['other_z'] = full_cdf_use['other_z'].apply(
        lambda x: [col.strip() for col in x.split(',')] if isinstance(x, str) else []
    )
    
    #type flags
    full_cdf_use['Type_Flag'] = full_cdf_use['Type_Flag'].apply(
        lambda x: [col.strip() for col in x.split(',')] if isinstance(x, str) else []
    )
    
    return full_cdf_use



def import_vizier(ID,table_no,index,directory='Catalogues/',save=True):
    """

    Parameters
    ----------
    ID : STRING
        Vizier catalogue ID.
    table_no : INT
        Table in the Vizier catalogue.
    directory : STRING, optional
        Folder path in which to save/import catalogue. The default is 'Catalogues/'.
    save : BOOLEAN, optional
        Option to save catalogue after downloading. The default is True.

    Returns
    -------
    df : TYPE
        DESCRIPTION.

    """
    
    catalogue_ivoid = f"ivo://CDS.VizieR/{ID}"   
        
    # each resource in the VO has an identifier, called ivoid. For vizier catalogs,
    # the VO ids can be constructed like this:
    # the actual query to the registry

    try:
        
        voresource = registry.search(ivoid=catalogue_ivoid)[0]
            
        tables = voresource.get_tables()
                
        tables_names = list(tables.keys())    
        # get the numbered table of the catalogue
        
        table_name = tables_names[table_no]
        
    except:
        
        print(f'Unable to find table {table_no} in {catalogue_ivoid}. Check the ID and table number are correct.')
        
        return
    
    filename = table_name.replace('/','-') +'.csv'   
    df_fname = filename
    
    if not os.path.exists(directory+ID.replace('/','-')):
        os.makedirs(directory+ID.replace('/','-'))
    
    filename = directory+ID.replace('/','-')+'/'+filename
    
    
    
    print(f"\nSearching for catalogue {filename}.")
        
    if exists(filename):
        
        print("Data found in folder. Importing . . .")
        
        df = pd.read_csv(filename)
    
    else:
        
        print("No file found. Collecting data . . .")
        
        # execute a synchronous ADQL query
        tap_service = voresource.get_service("tap")
        
        offset = 0
        chunk_size=100000
        df_list=[]
        last_index= 0
        
        if index != "None":
            
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
            "Saving data . . ."
            df.to_csv(filename) 
        
    return df, df_fname

def analyse_shared_columns(shared_columns, df_info):
    summary = []

    for col in shared_columns:
        matched_tables = []

        for fname, info in df_info.items():
            cols = info['columns']

            if isinstance(col, list):
                # Check both RA/DEC names and their common aliases
                if all(c in cols for c in col) or \
                   (col == ['RAdeg', 'DEdeg'] and 'RAJ2000' in cols and 'DEJ2000' in cols):
                    matched_tables.append(fname)
            else:
                if col in cols:
                    matched_tables.append(fname)

        summary.append({
            'shared_column': col,
            'count': len(matched_tables),
            'tables': matched_tables
        })

    return pd.DataFrame(summary)


df = load_catalogue_table("../Updated_Catalogue_List.csv")
ddfs,ddfs_pd = load_ddfs(path='../DDF_Coordinates.csv')


for index, row in df.iterrows():
    
    directory = f"../Catalogues/{row['ID'].replace('/','-')}"
    print(directory)

    combined_df = None
    subset = None

    if exists(os.path.join(directory, f"{row['ID'].replace('/','-')}_cm.csv")):
        
        print("Combined data found in folder. Importing...")
        
        combined_df = pd.read_csv(os.path.join(directory, f"{row['ID'].replace('/','-')}_cm.csv"))
        
    else:

        print("combined data not found")        

        df_info = {}
    
        for i in range(0, int(row['Total Tables.'])):
            result = import_vizier(row['ID'], i, 'recno', directory='../Catalogues/')
        
            if result is None:
                print(f"Table {i} not found or failed to load for {row['ID']}. Skipping.")
                continue
        
            df_table, df_fname = result
        
            df_info[df_fname] = {
                'length': len(df_table),
                'columns': df_table.columns.tolist()
            }
        
        
        ra_columns = ['RA', 'RAdeg', 'RAJ2000']
        dec_columns = ['DEC', 'DEdeg', 'DEJ2000']
        
        zsp_col = row['Best ZSP']
        zph_col = row['Best ZPH']
        
        q_zsp_col = f"q_{row['Best ZSP']}"
        q_zph_col = f"q_{row['Best ZPH']}"
        
        collected_rows = []
        
        for fname in df_info:
            filepath = os.path.join(directory, fname)
            try:
                df_table = pd.read_csv(filepath)
            except Exception as e:
                print(f"Failed to read {filepath}: {e}")
                continue
        
            available_ra = next((col for col in ra_columns if col in df_table.columns), None)
            available_dec = next((col for col in dec_columns if col in df_table.columns), None)
        
            selected_cols = [c for c in [available_ra, available_dec, zsp_col, zph_col,q_zsp_col, q_zph_col] if c in df_table.columns]
            
            if selected_cols:
                subset = df_table[selected_cols].copy()
                
                subset['source_table'] = fname  # optional for traceability
                collected_rows.append(subset)
        
        if collected_rows:
            combined_df = pd.concat(collected_rows, ignore_index=True)
            
            combined_df.rename(columns={zsp_col: "zspec", zph_col: "zphot"},inplace=True)
            
            
            combined_path = os.path.join(directory, f"{row['ID'].replace('/','-')}_cm.csv")
            
            combined_df.to_csv(combined_path, index=False)
            
            print(f"Combined catalogue saved to {combined_path}")
        else:
            print(f"No relevant columns found for {row['ID']}")
        
    print("Searching catalogue:")
    #loop through for each ddf
    if combined_df is not None and 'RAJ2000' in combined_df.columns and 'DEJ2000' in combined_df.columns:
        
        
        
        for i in ddfs:
            
            z_ddf=[]
            z_ddf_labels=[]
            
            subdr = f"../Catalogues/{row['ID'].replace('/','-')}/Subcatalogues/"
            os.makedirs(subdr, exist_ok=True) 
            os.makedirs(f"{subdr}/{i}/Plots", exist_ok=True) 
    
            
            filename = f"{subdr}/{row['ID'].replace('/','-')}_{i}.csv"
            
            if exists(filename):
                
                print(f"Catalogue subset for {i} already exists. Importing . . .")
                
                subset = pd.read_csv(filename)
    
            else:
                
                subset = search_catalogue(combined_df,'RAJ2000','DEJ2000',ddfs[i]['RAdeg'],ddfs[i]['DECdeg'],ddfs[i]['Diameter']*1.2)
    
                #save subset
                if subset.empty == False:
                
                    print(f"Items found in {i}. Saving subset . . .")
                
                    subset.to_csv(filename)
                
                    print(f"Subset saved to csv.")
    
            if subset.empty == False:
                fieldplot(i, row['ID'],ddfs[i]['RAdeg'],ddfs[i]['DECdeg'],
                          subset['RAJ2000'],subset['DEJ2000'],
                              color=ddfs[i]['Colour'],size=0.1,
                              savefig=400,directory=f"{subdr}/{i}/Plots/fieldcover.png")
                
                if 'zspec' in combined_df.columns:
                    
                    plot_zhist(i,subset['zspec'],labels=row['ID'],savefig=400,savename=f"{subdr}/{i}/Plots/zspec.png")
                    
                if 'zphot' in combined_df.columns:
                        
                    plot_zhist(i,subset['zphot'],labels=row['ID'],savefig=400,savename=f"{subdr}/{i}/Plots/zspec.png")
                
    del subset, combined_df
                
    gc.collect()