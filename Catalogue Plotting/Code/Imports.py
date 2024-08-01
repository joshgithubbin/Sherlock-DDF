"""
Created on Mon Jul  1 14:53:55 2024

@author: joshuaweston

Functions to load the catalogue table and subsequently load/import data.

"""

from ast import literal_eval
from os.path import exists
from pyvo import registry
import pandas as pd

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
    
    #filter out unused catalogues
    filtered_cdf = full_cdf[full_cdf["Use"] == "Yes"]
    
    #Analysis Columns
    filtered_cdf_use = filtered_cdf[["Name","Source","ID","Table No.","Index","RA Column","DEC Column","Z","Best Z","Marker size"]]
    
    #strip strings and convert table numbers to integers
    filtered_cdf_use = filtered_cdf_use.applymap(lambda x: x.strip() if isinstance(x, str) else x)
    filtered_cdf_use['Table No.']=filtered_cdf_use['Table No.'].astype(int)
    
    try:
        filtered_cdf_use['Z'] = filtered_cdf_use['Z'].apply(lambda x: literal_eval(x) if pd.notna(x) else x)
        
    except ValueError:
        
        print("Value Error. Make sure redshift column values are correctly inputted.")
    
    return filtered_cdf_use[0:]

def import_catalogue(row,directory):
    
    source = row['Source']
    
    if source not in ['Vizier']:
        
        print(f'Cannot import catalogue {row.Name}.Catalogues from {source} are not compatible with this code. Skipping . . .')
        
        return    
    
    ID = row['ID']
    table_no = row['Table No.']
    index = row['Index']
    
    ra_label = row['RA Column']
    dec_label = row['DEC Column']
    Z = row['Best Z']
    Z_alt = row['Z']
    
    if source == 'Vizier':
        
        df=import_vizier(ID, table_no,index,directory)
    
    return df

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
   
    filename = table_name.replace('/','-') +'.csv'   
    
    filename = directory+filename
    
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
        
        df = pd.concat(df_list,ignore_index=True)
        
        if save==True:
            "Saving data . . ."
            df.to_csv(filename) 
        
    return df