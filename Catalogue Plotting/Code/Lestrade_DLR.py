#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 14:55:16 2025

@author: joshuaweston
"""

import math
import pandas as pd
import numpy as np
from Imports import *
from searchcat import *
from DDFs import *
from tqdm import tqdm
from astropy.coordinates import SkyCoord
from astropy import units as u
import time

def DLR(a,b,theta,da,db):
    
    numerator = a*b
    
    epsilon = theta


    theta = math.atan2(db,da)
    
    if np.sign(a) == np.sign(b):
        
        theta= abs(theta)
    
    else:
        
        theta= -abs(theta)
    
    phi = theta - epsilon
    
    
    d_sin = a*math.sin(theta)
    d_cos = b*math.cos(theta)
    
    denominator = math.sqrt((d_sin**2) + (d_cos**2))
    
    if denominator == 0:
        return float('inf')
    
    return numerator / denominator

def ang_sep(ra1,dec1,ra2,dec2):
    
    x = math.cos(dec1) * math.sin(dec2) - math.sin(dec1) * math.cos(dec2) * math.cos(ra2 - ra1)
    
    y = math.cos(dec2) * math.sin(ra2 - ra1);
    
    z = math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra2 - ra1)
    
    d = math.degrees(math.atan2(math.sqrt(x*x + y*y),z))*3600
    
    return d

def d_dlr(a,b,theta,ra1,dec1,ra2,dec2):
    
    ra1 = math.radians(ra1)
    dec1 = math.radians(dec1)
    ra2 = math.radians(ra2)
    dec2 = math.radians(dec2)
    theta = math.radians(theta)
    
    a=a*3600
    b=b*3600
        
    a_s = ang_sep(ra1,dec1,ra2,dec2)
    
    da = ra1 - ra2
    db = dec1 - dec2
    
    D = DLR(a,b,theta,da,db)
    
    return a_s/D

def dlr_multiwrap(df, columns):
    """
    Function to calculate DLR values for multiple rows based on input columns.
    
    Arguments:
    - df: DataFrame containing the necessary columns.
    - columns: List of columns in the form ['a', 'b', 'theta', 'ra1', 'dec1', 'ra2', 'dec2'].
    
    Returns:
    - A list of calculated DLR values.
    """
    dlr = []
    
    for index, row in df.iterrows():
        # Extract values from the row based on the column list
        a = row[columns[0]]
        b = row[columns[1]]
        theta = row[columns[2]]
        ra1 = row[columns[3]]
        dec1 = row[columns[4]]
        ra2 = row[columns[5]]
        dec2 = row[columns[6]]
        
        # Append the calculated DLR value to the list
        dlr.append(d_dlr(a, b, theta, ra1, dec1, ra2, dec2))
    
    return dlr

def compute_HC(D, epsilon=1e-5):
    
    """
    Compute the Host Confusion (HC) parameter for a given SN.
    
    Parameters:
        D (numpy array): Array of galaxy separations, sorted from lowest to highest.
        epsilon (float): Small constant to avoid division by zero.
    
    Returns:
        float: HC value
    """
    
    D = D.to_numpy()  # Convert pandas Series to numpy array
    D = np.array(D)  # Ensure it's a NumPy array
    D = D[~np.isnan(D)]  # Remove NaNs properly
    N = len(D)  # Number of galaxies

    if N == 1:
        return -99  # Defined case when there's only one galaxy
    
    D1, D2 = D[0], D[1]  # Closest and second closest galaxy separations

    # First fraction
    first_term = (D1**2 / (D2 + epsilon)) / (D2 - D1 + epsilon)
    
    # Double summation over galaxy pairs
    i_indices = np.arange(N - 1)  # Indices from 0 to N-2
    j_indices = np.arange(1, N)   # Indices from 1 to N-1
    
    D_i = D[i_indices]  # First N-1 galaxies
    D_j = D[j_indices]  # Second N-1 galaxies
    
    # Now D_i and D_j should have the same length (N-1)
    denominator = (i_indices + 1)**2 * (D_j - D_i + epsilon)
    sum_term = np.sum(D_i / (D_j + epsilon) / denominator)
    
    # Final HC calculation
    HC = np.log10(first_term * sum_term)
    
    return HC

def check_matches_dlr(df):
    """
    Checks if the HOSTGAL point (RA, DEC) falls within the ellipse defined by the DLR Host parameters.
    Adds a 'MATCH' column with 'YES' or 'NO'.
    
    Parameters:
        df (pd.DataFrame): DataFrame containing HOSTGAL_RA, HOSTGAL_DEC, DLR Host RA, DLR Host Dec, 
                           DLR Host a, DLR Host b, and DLR Host pa.
    """
    # Function to check if a point lies inside an ellipse
    def is_inside_ellipse(ra_host, dec_host, ra_dlr, dec_dlr, a, b, pa):
        # Convert position angle to radians
        theta = np.radians(pa)
        
        # Shift the point to ellipse's center
        delta_ra = ra_host - ra_dlr
        delta_dec = dec_host - dec_dlr
        
        # Rotate the coordinates to align with the ellipse's axes
        x_prime = delta_ra * np.cos(theta) + delta_dec * np.sin(theta)
        y_prime = -delta_ra * np.sin(theta) + delta_dec * np.cos(theta)
        
        # Check the ellipse equation
        return (x_prime**2 / a**2) + (y_prime**2 / b**2) <= 1
    
    # Apply the function to each row in the DataFrame
    df['DLR MATCH'] = df.apply(
        lambda row: 'YES' if is_inside_ellipse(
            row['HOSTGAL_RA'], row['HOSTGAL_DEC'],
            row['DLR Host RA'], row['DLR Host Dec'],
            row['DLR Host a'], row['DLR Host b'],
            row['DLR Host pa']
        ) else 'NO',
        axis=1
    )
    
    return df

def check_true_exists(df, field):
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
    
    def is_inside_ellipse(ra, dec, ra0, dec0, A, B, theta):
        """Check if a point (ra, dec) is inside an ellipse centered at (ra0, dec0)"""
        theta = np.radians(theta)

        # Shift coordinates
        x = ra - ra0
        y = dec - dec0

        # Rotate coordinates
        x_prime = x * np.cos(theta) + y * np.sin(theta)
        y_prime = -x * np.sin(theta) + y * np.cos(theta)

        # Ellipse equation
        return (x_prime ** 2) / (A ** 2) + (y_prime ** 2) / (B ** 2) <= 1

    # Initialize new columns
    df["truematch_exist"] = "NO"
    df["truematch RA"] = np.nan
    df["truematch Dec"] = np.nan
    df["truematch A"] = np.nan
    df["truematch B"] = np.nan
    df["truematch THETA"] = np.nan

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Processing Rows"):
        ra, dec = row["HOSTGAL_RA"], row["HOSTGAL_DEC"]
        
        # Search for sources in the field catalog near the host position
        field_subset = search_catalogue(field, 'RA', 'DEC', ra, dec, 0.1)

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

def DLR_Apply(transients,df,radius=0.1,truelabels=False):
    
    test_set = transients

    host_dlr1 = []
    host_ra1 = []
    host_dec1 = []
    host_z1 =[]
    host_zt =[]
    host_a1 =[]
    host_b1=[]
    host_pa1=[]
    host_cat1=[]
    host_HC = []
    
    host_U1 =[]
    host_G1 =[]
    host_R1=[]
    host_I1=[]
    host_Z1=[]
    host_Y1=[]

    host_dlr2 = []
    host_ra2 = []
    host_dec2 = []
    host_z2 =[]
    host_zt2 =[]
    host_a2=[]
    host_b2=[]
    host_pa2=[]
    host_cat2=[]
    
    host_U2 =[]
    host_G2 =[]
    host_R2=[]
    host_I2=[]
    host_Z2=[]
    host_Y2=[]
    
    matches=[]

    for index,row in tqdm(test_set.iterrows(), total=len(test_set), desc="Creating DLR Associations"):
        
        #identify nearby hosts from which to calculate dlr values
        
        dlr_subset = search_catalogue(df,'RA','DEC',row['RA'],row['DEC'],radius)
        
        matches.append(len(dlr_subset))

        
        dlr_values = []
        dlr_hosts = []
        dlr_ra=[]
        dlr_dec=[]
        host_z=[]
        host_z_type=[]
        host_a=[]
        host_b=[]
        host_pa=[]
        host_ref=[]
        
        host_mu=[]
        host_mg=[]
        host_mr=[]
        host_mi=[]
        host_mz=[]
        host_my=[]
        
        
        #SN coordinates
        ra2=row['RA']
        dec2=row['DEC']
        
        for i, j in dlr_subset.iterrows():
            
            a = j['A']
            b = j['B']
            theta = j['THETA']
            
            ra1=j['RA']
            dec1=j['DEC']
            
            zsp1=j['ZSP']
            zph1=j['ZPH']
            
            cat=j['CATALOGUE'] 
            
            U=j['u']
            G=j['g']
            R=j['r']
            I=j['i']
            Z=j['z']
            Y=j['y']
            
            dlr_values.append(d_dlr(a,b,theta,ra1,dec1,ra2,dec2))
            dlr_ra.append(ra1)
            dlr_dec.append(dec1)
            host_a.append(a)
            host_b.append(b)
            host_pa.append(theta)
            host_ref.append(cat)
            
            host_mu.append(U)
            host_mg.append(G)
            host_mr.append(R)
            host_mi.append(I)
            host_mz.append(Z)
            host_my.append(Y)
            
            # Assign host z based on the conditions
            if not np.isnan(zsp1):
                host_z.append(zsp1)
                host_z_type.append('zsp')
            elif not np.isnan(zph1):
                host_z.append(zph1)
                host_z_type.append('zph')
            else:
                host_z.append(-1)
                host_z_type.append('both NaN')
                
        new_df = pd.DataFrame({
        'dlr value': dlr_values,
        'host RA': dlr_ra,
        'host DEC': dlr_dec,
        'host z': host_z,
        'host z type': host_z_type,
        'host a':host_a,
        'host b':host_b,
        'host pa':host_pa,
        'host ref':host_ref,
        'host um':host_mu,
        'host gm':host_mg,
        'host rm':host_mr,
        'host im':host_mi,
        'host zm':host_mz,
        'host ym':host_my
        })
    
        if new_df.empty:
            # Append None (or placeholders) to all lists since no match was found
            host_dlr1.append(None)
            host_ra1.append(None)
            host_dec1.append(None)
            host_z1.append(None)
            host_zt.append(None)
            host_a1.append(None)
            host_b1.append(None)
            host_pa1.append(None)
            host_cat1.append(None)
            
            host_U1.append(None)
            host_G1.append(None)
            host_R1.append(None)
            host_I1.append(None)
            host_Z1.append(None)
            host_Y1.append(None)
        
            host_dlr2.append(None)
            host_ra2.append(None)
            host_dec2.append(None)
            host_z2.append(None)
            host_zt2.append(None)
            host_a2.append(None)
            host_b2.append(None)
            host_pa2.append(None)
            host_cat2.append(None)
            
            host_U2.append(None)
            host_G2.append(None)
            host_R2.append(None)
            host_I2.append(None)
            host_Z2.append(None)
            host_Y2.append(None)
        
            host_HC.append(-99)  # Assigning a default HC value
        
            continue
        # Sort the DataFrame by 'dlr value' in ascending order
        new_df = new_df.sort_values(by='dlr value', ascending=True)        
    
        HC = -99
        
        host_dlr1.append(new_df.iloc[0]['dlr value'])
        host_ra1.append(new_df.iloc[0]['host RA'])
        host_dec1.append(new_df.iloc[0]['host DEC'])
        host_z1.append(new_df.iloc[0]['host z'])
        host_zt.append(new_df.iloc[0]['host z type'])
        host_a1.append(new_df.iloc[0]['host a'])
        host_b1.append(new_df.iloc[0]['host b'])
        host_pa1.append(new_df.iloc[0]['host pa'])
        host_cat1.append(new_df.iloc[0]['host ref'])
        
        host_U1.append(new_df.iloc[0]['host um'])
        host_G1.append(new_df.iloc[0]['host gm'])
        host_R1.append(new_df.iloc[0]['host rm'])
        host_I1.append(new_df.iloc[0]['host im'])
        host_Z1.append(new_df.iloc[0]['host zm'])
        host_Y1.append(new_df.iloc[0]['host ym'])

        if len(new_df) >= 2:  # Ensure there are at least two entries
            i = 0
            while i < len(new_df) - 1:  # Prevent IndexError
                # Calculate the separation between the best and current candidate
                best_coord = SkyCoord(ra=new_df.iloc[0]['host RA'] * u.deg, 
                                      dec=new_df.iloc[0]['host DEC'] * u.deg)
                current_coord = SkyCoord(ra=new_df.iloc[1 + i]['host RA'] * u.deg, 
                                         dec=new_df.iloc[1 + i]['host DEC'] * u.deg)
                
                separation = best_coord.separation(current_coord).arcsec  # Separation in arcseconds
                
                # Threshold for minimum separation (e.g., 0.8 arcseconds)
                r_arcsec = 0.8
                
                if separation > r_arcsec:
                    
                    HC = compute_HC(pd.concat([pd.Series([new_df['dlr value'].iloc[0]]), new_df['dlr value'].iloc[1+i:]]).sort_values(ascending=True))

                    # Append the candidate if it's far enough
                    host_dlr2.append(new_df.iloc[1 + i]['dlr value'])
                    host_ra2.append(new_df.iloc[1 + i]['host RA'])
                    host_dec2.append(new_df.iloc[1 + i]['host DEC'])
                    host_z2.append(new_df.iloc[1 + i]['host z'])
                    host_zt2.append(new_df.iloc[1 + i]['host z type'])
                    host_a2.append(new_df.iloc[1 + i]['host a'])
                    host_b2.append(new_df.iloc[1 + i]['host b'])
                    host_pa2.append(new_df.iloc[1 + i]['host pa'])
                    host_cat2.append(new_df.iloc[1 + i]['host ref'])
                    
                    host_U2.append(new_df.iloc[1+i]['host um'])
                    host_G2.append(new_df.iloc[1+i]['host gm'])
                    host_R2.append(new_df.iloc[1+i]['host rm'])
                    host_I2.append(new_df.iloc[1+i]['host im'])
                    host_Z2.append(new_df.iloc[1+i]['host zm'])
                    host_Y2.append(new_df.iloc[1+i]['host ym'])
                    break  # Exit the loop since a valid candidate was found
                else:
                    i += 1  # Move to the next candidate
            
            # If no valid candidate is found, append None
            if i >= len(new_df) - 1:
                host_dlr2.append(None)
                host_ra2.append(None)
                host_dec2.append(None)
                host_z2.append(None)
                host_zt2.append(None)
                host_a2.append(None)
                host_b2.append(None)
                host_pa2.append(None)
                host_cat2.append(None)
                
                host_U2.append(None)
                host_G2.append(None)
                host_R2.append(None)
                host_I2.append(None)
                host_Z2.append(None)
                host_Y2.append(None)        
        else:
            # If there are fewer than two entries, append None for all values
            host_dlr2.append(None)
            host_ra2.append(None)
            host_dec2.append(None)
            host_z2.append(None)
            host_zt2.append(None)
            host_a2.append(None)
            host_b2.append(None)
            host_pa2.append(None)
            host_cat2.append(None)

            host_U2.append(None)
            host_G2.append(None)
            host_R2.append(None)
            host_I2.append(None)
            host_Z2.append(None)
            host_Y2.append(None)   
    
        host_HC.append(HC)
        
    test_set['Min DLR'] = host_dlr1
    test_set['DLR Host RA'] = host_ra1
    test_set['DLR Host Dec'] = host_dec1
    test_set['DLR Host z'] = host_z1
    test_set['DLR Host z Type'] = host_zt
    test_set['DLR Host a'] = host_a1
    test_set['DLR Host b'] = host_b1
    test_set['DLR Host pa'] = host_pa1
    test_set['DLR Cat 1'] = host_cat1
    test_set['DLR HC'] = host_HC
    
    test_set['DLR u 1'] = host_U1
    test_set['DLR g 1'] = host_G1
    test_set['DLR r 1'] = host_R1
    test_set['DLR i 1'] = host_I1
    test_set['DLR z 1'] = host_Z1
    test_set['DLR y 1'] = host_Y1

    test_set['Min DLR 2'] = host_dlr2
    test_set['DLR Host RA 2'] = host_ra2
    test_set['DLR Host Dec 2'] = host_dec2
    test_set['DLR Host z 2'] = host_z2
    test_set['DLR Host z Type 2'] = host_zt2
    test_set['DLR Host a 2'] = host_a2
    test_set['DLR Host b 2'] = host_b2
    test_set['DLR Host pa 2'] = host_pa2
    test_set['DLR Cat 2'] = host_cat2
    
    test_set['DLR u 2'] = host_U2
    test_set['DLR g 2'] = host_G2
    test_set['DLR r 2'] = host_R2
    test_set['DLR i 2'] = host_I2
    test_set['DLR z 2'] = host_Z2
    test_set['DLR y 2'] = host_Y2

    test_set['dRA 1'] = (test_set['DLR Host RA'] - test_set['HOSTGAL_RA'])*3600
    test_set['dDec 1'] = (test_set['DLR Host Dec'] - test_set['HOSTGAL_DEC'])*3600
    test_set['dz 1'] = test_set['DLR Host z'] - test_set['REDSHIFT_FINAL']


    test_set['dRA 2'] = (test_set['DLR Host RA 2'] - test_set['HOSTGAL_RA'])*3600
    test_set['dDec 2'] = (test_set['DLR Host Dec 2'] - test_set['HOSTGAL_DEC'])*3600
    test_set['dz 2'] = test_set['DLR Host z 2'] - test_set['REDSHIFT_FINAL']
    
    # Define the column set for DLR calculation (1-2)
    columns_12 = ['DLR Host a', 'DLR Host b', 'DLR Host pa', 'DLR Host RA', 'DLR Host Dec', 'DLR Host RA 2', 'DLR Host Dec 2']

    test_set['DLR_12'] = dlr_multiwrap(test_set, columns_12)

    # Define the column set for DLR calculation (2-1)
    columns_12 = ['DLR Host a 2', 'DLR Host b 2', 'DLR Host pa 2', 'DLR Host RA 2', 'DLR Host Dec 2', 'DLR Host RA', 'DLR Host Dec']

    # Calculate DLR for each row
    test_set['DLR_21'] = dlr_multiwrap(test_set, columns_12)
    
    test_set['Matches'] = matches
    
    if truelabels:    
    
        test_set = check_matches_dlr(test_set)
    
        test_set = check_true_exists(test_set, df)
    
    return test_set