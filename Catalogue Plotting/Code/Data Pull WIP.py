#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 09:30:58 2025

@author: joshuaweston
"""

df = load_catalogue_table("../Updated_Catalogue_List.csv")
ddfs,ddfs_pd = load_ddfs(path='../DDF_Coordinates.csv')


for index, row in df.iterrows():
    
    directory = f"../Catalogues/{row['ID'].replace('/','-')}"
    print(directory)

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
        combined_path = os.path.join(directory, f"{row['ID'].replace('/','-')}_cm.csv")
        combined_df.to_csv(combined_path, index=False)
        print(f"Combined catalogue saved to {combined_path}")
    else:
        print(f"No relevant columns found for {row['ID']}")
        
    print("Searching catalogue:")
    #loop through for each ddf
    for i in ddfs:
        
        z_ddf=[]
        z_ddf_labels=[]
        
        subdr = f"../Catalogues/{row['ID'].replace('/','-')}/Subcatalogues/"
        os.makedirs(subdr, exist_ok=True) 
        os.makedirs(f"{subdr}/{i}/Plots", exist_ok=True) 

        
        filename = f"{subdr}/{{row['ID'].replace('/','-')}_{i}.csv"
        
        if exists(filename):
            
            print(f"Catalogue subset for {i} already exists. Importing . . .")
            
            subset = pd.read_csv(filename)

        else:
            
            subset = search_catalogue(combined_df,'RAJ2000','DEJ2000',ddfs[i]['RAdeg'],ddfs[i]['DECdeg'],ddfs[i]['Diameter']*1.2)

            #save subset
            if subset.empty == False:
            
                print(f"Items found in {i}. Saving subset . . .")
            
                subset.to_csv(filename)
            
                print(f"Subset saved to csv under Catalogues/SubCatalogues/{df_name}_{i}.csv. \n")

        if subset.empty == False:
                        
            fieldplot(i, df_name,
                      ddfs[i]['RAdeg'],ddfs[i]['DECdeg'],subset[row['RA Column']],subset[row['DEC Column']],
                      color=ddfs[i]['Colour'],size=row['Marker size'])