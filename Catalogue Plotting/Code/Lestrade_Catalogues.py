
import math
import os
import pandas as pd
import numpy as np
from DDFs import *
from searchcat import *
from Imports import *

def add_bobby(cdf, Name, RA='RAJ2000', DEC='DEJ2000', ZSP=None, ZPH=None, A=None, B=None, PA=None,
              u=None, g=None, r=None, i=None, z=None, y=None, axis_scale=1.0):

    # Filter the catalogue DataFrame for the specified Name
    filtered_cdf = cdf[cdf['Name'] == Name]

    if filtered_cdf.empty:
        raise ValueError(f"No catalogue entry found for Name: {Name}")

    row = filtered_cdf.iloc[0]

    # Import the corresponding catalogue
    df = import_catalogue(row, directory='../Catalogues/')

    # Explicitly define all target columns
    target_columns = ['RA', 'DEC', 'ZSP', 'ZPH', 'A', 'B', 'THETA', 'u', 'g', 'r', 'i', 'z', 'y']

    # Map provided column names to target column names
    columns_mapping = {
        RA: 'RA',
        DEC: 'DEC',
        ZSP: 'ZSP',
        ZPH: 'ZPH',
        A: 'A',
        B: 'B',
        PA: 'THETA',
        u: 'u',
        g: 'g',
        r: 'r',
        i: 'i',
        z: 'z',
        y: 'y'
    }

    # Remove None keys from the mapping
    filtered_mapping = {k: v for k, v in columns_mapping.items() if k is not None}

    # Select and rename columns based on the mapping
    sdf = df[list(filtered_mapping.keys())].rename(columns=filtered_mapping)

    # Apply axis scale if A and B are present
    if 'A' in sdf.columns:
        sdf['A'] *= axis_scale
    if 'B' in sdf.columns:
        sdf['B'] *= axis_scale

    # Add missing columns with NaN values
    for column in target_columns:
        if column not in sdf.columns:
            print(f"Adding missing column: {column}")
            sdf[column] = np.nan

    # Add the CATALOGUE column with the Name
    sdf['CATALOGUE'] = Name

    return sdf

def gen_cat(region_dict, region_name, catalogue_path='../Catalogue_List.csv', ddf_path='../DDF_Coordinates.csv', 
            save_folder="../Lestrade Catalogues/", overwrite=False):

    # Ensure the save folder exists
    os.makedirs(save_folder, exist_ok=True)

    # Define the save path
    save_path = os.path.join(save_folder, f"{region_name}.csv")

    # If the file exists and overwrite is False, load the existing file
    if not overwrite and os.path.exists(save_path):
        print(f"Loading existing catalogue: {save_path}")
        return pd.read_csv(save_path)

    # Load the necessary data
    ddfs, ddfs_pd = load_ddfs(path=ddf_path)
    cdf = load_catalogue_table(path=catalogue_path)

    # Process each catalogue in the region dictionary
    df_list = []
    for name, params in region_dict.items():
        # Extract axis_scale, defaulting to 1.0 if not provided
        axis_scale = params.pop("axis_scale", 1.0)
        df_list.append(add_bobby(cdf, name, **params, axis_scale=axis_scale))

    # Concatenate all component dataframes
    combined_df = pd.concat(df_list, ignore_index=True)

    # Search catalogue and filter results
    combined_df = search_catalogue(combined_df, 'RA', 'DEC', ddfs[region_name]['RAdeg'], 
                                   ddfs[region_name]['DECdeg'], ddfs[region_name]['Diameter'] * 1.2)
    # Save the combined catalogue
    combined_df.to_csv(save_path, index=False)
    print(f"Combined catalogue saved to: {save_path}")

    return combined_df




XMM_LSS = {
    "SPLASH-SXDF": {
        "ZSP": "zspec", 
        "ZPH": "zphot",
        "A": "amaj", 
        "B": "bmin", 
        "PA": "PA",
        "u": "umagC", 
        "g": "gmagC", 
        "r": "rmagC", 
        "i": "imagC", 
        "z": "zmagC",
    },
    
    "CFHQSIR": {
        "A": "AaxisY", 
        "B": "BaxisY", 
        "PA": "thetaY",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag", 
        "y": "ymag",
    },
    
}

COSMOS = {
    "COSMOS2020-CLASSIC": {
        "ZPH": "EZzphot",
        "A": "ACSAWorld", 
        "B": "ACSBWorld", 
        "PA": "ACSthetaWorld",
        "u": "CFHTumag", 
        "g": "HSCgmag", 
        "r": "HSCrmag", 
        "i": "HSCimag", 
        "z": "HSCzmag",
        "y": "HSCymag"
    },
    
    "ACS-GC": {
        "ZPH": "zph",
        "ZSP": "zsp",
        "A": "a1", 
        "B": "b1", 
        "PA": "PA1",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag"
    }
}

ECDFS = {
    
    "Chandra-Multi": {
        "ZPH": "MCz",
        "A": "MajAxis", 
        "B": "MinAxis", 
        "PA": "PA",
        "u": "usMAG", 
        "g": "gsMAG", 
        "r": "rsMAG"
    },
    
}