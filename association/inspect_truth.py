#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 14:42:10 2025

@author: joshuaweston
"""

def is_inside_ellipse(ra, dec, ra0, dec0, A, B, theta):
    """Check if a point (ra, dec) is inside an ellipse centered at (ra0, dec0)"""
    import numpy as np
    theta = np.radians(theta)

    # Shift coordinates
    x = ra - ra0
    y = dec - dec0

    # Rotate coordinates
    x_prime = x * np.cos(theta) + y * np.sin(theta)
    y_prime = -x * np.sin(theta) + y * np.cos(theta)

    # Ellipse equation
    return (x_prime ** 2) / (A ** 2) + (y_prime ** 2) / (B ** 2) <= 1


def does_true_exist(df, field, r):
    """
    Checks if the true host galaxy exists in the catalogues used.

    Parameters
    ----------
    df : pd.DataFrame
        Transient data being used.
    field : pd.DataFrame
        Field catalogue being used.

    Returns
    -------
    pd.DataFrame
        DataFrame with new columns indicating if a match was found and the properties of the matched object.
    """
    
    import numpy as np
    import pandas as pd
    from tqdm import tqdm
    from lestrade.browser import search
    from lestrade.association.inspect_truth import is_inside_ellipse

    # Initialize new columns
    df["truematch_exist"] = "NO"
    df["truematch RA"] = np.nan
    df["truematch Dec"] = np.nan
    df["truematch A"] = np.nan
    df["truematch B"] = np.nan
    df["truematch THETA"] = np.nan

    for index, row in tqdm(df.iterrows(), total=len(df), desc="\tProcessing Rows"):
        
        
        ra, dec = row["HOSTGAL_RA"], row["HOSTGAL_DEC"]
        
        # Search for sources in the field catalog near the host position
        field_subset = search.search(ra, dec, r, field, 'RA', 'DEC')


        matches = []
        
        for _, sh_row in field_subset.iterrows():
            if is_inside_ellipse(ra, dec, sh_row["RA"], sh_row["DEC"], sh_row["A"], sh_row["B"], sh_row["THETA"]):
                matches.append(sh_row)

        if len(matches) >= 1:
            match = matches[0]  # Store only the first match
            df.at[index, "truematch_exist"] = "YES" if len(matches) == 1 else "CONFUSION"
            df.at[index, "truematch RA"] = match["RA"] 
            df.at[index, "truematch Dec"] = match["DEC"]
            df.at[index, "truematch A"] = match["A"]
            df.at[index, "truematch B"] = match["B"]
            df.at[index, "truematch THETA"] = match["THETA"]

    return df

def is_match_consistent(df,metric):
    """
    Checks if the HOSTGAL point (RA, DEC) falls within the ellipse defined by the identified host parameters.
    Adds a 'MATCH' column with 'YES' or 'NO'.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing HOSTGAL_RA, HOSTGAL_DEC, Method Host RA, Method Host Dec, 
                           Method Host a, Method Host b, and Method Host pa.
    """
    
    from lestrade.association.inspect_truth import is_inside_ellipse
    
    # Apply the function to each row in the DataFrame
    df[f'{metric} MATCH'] = df.apply(
        lambda row: 'YES' if is_inside_ellipse(
            row['HOSTGAL_RA'], row['HOSTGAL_DEC'],
            row[f'{metric} Host 1 RA'], row[f'{metric} Host 1 DEC'],
            row[f'{metric} Host 1 A'], row[f'{metric} Host 1 B'],
            row[f'{metric} Host 1 PA']
        ) else 'NO',
        axis=1
    )
    
    return df