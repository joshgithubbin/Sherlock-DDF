#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 18:08:22 2025

@author: joshuaweston
"""

from astropy.coordinates import SkyCoord
from astropy import units as u

import math
import math
import pandas as pd
import numpy as np
from Imports import *
from searchcat import *
from DDFs import *
from tqdm import tqdm


def ASearch_Calc(ra_sn, dec_sn, ra_host, dec_host, a):
    """
    Calculates the normalized distance from a supernova (SN) to a single host galaxy.

    Parameters:
    - ra_sn (float): Right Ascension of the SN in degrees.
    - dec_sn (float): Declination of the SN in degrees.
    - ra_host (float): Right Ascension of the host galaxy in degrees.
    - dec_host (float): Declination of the host galaxy in degrees.
    - a (float): Semimajor axis of the galaxy in degrees.

    Returns:
    - float: Distance between SN and host galaxy center, normalized by 'a'.
    """
    
    # Convert coordinates to SkyCoord objects
    sn_coord = SkyCoord(ra=ra_sn * u.deg, dec=dec_sn * u.deg, frame='icrs')
    host_coord = SkyCoord(ra=ra_host * u.deg, dec=dec_host * u.deg, frame='icrs')

    # Calculate angular separation in degrees
    separation = sn_coord.separation(host_coord).deg
    
    # Normalize by semimajor axis
    return separation / a if a > 0 else float('inf')  # Avoid division by zero

def av_multiwrap(df, columns):
    """
    Function to calculate A-values for multiple rows based on input columns.
    
    Arguments:
    - df: DataFrame containing the necessary columns.
    - columns: List of columns in the form ['a', 'ra1', 'dec1', 'ra2', 'dec2'].
    
    Returns:
    - A list of calculated DLR values.
    """
    av = []
    
    for index, row in df.iterrows():
        # Extract values from the row based on the column list
        a = row[columns[0]]
        ra1 = row[columns[1]]
        dec1 = row[columns[2]]
        ra2 = row[columns[3]]
        dec2 = row[columns[4]]
        
        # Append the calculated DLR value to the list
        av.append(ASearch_Calc(ra2, dec2, ra1, dec1, a))
    
    return av

def check_matches_amajor(df):
    """
    Checks if the HOSTGAL point (RA, DEC) falls within the ellipse defined by the Consearch Host parameters.
    Adds a 'A-MATCH' column with 'YES' or 'NO'.
    
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
    df['A-Value MATCH'] = df.apply(
        lambda row: 'YES' if is_inside_ellipse(
            row['HOSTGAL_RA'], row['HOSTGAL_DEC'],
            row['A-Value Host RA'], row['A-Value Host Dec'],
            row['A-Value Host a'], row['A-Value Host b'],
            row['A-Value Host pa']
        ) else 'NO',
        axis=1
    )
    return df

def check_true_exists(df,field):
    """
    Checks if the true host galaxy exists in the catalogues used.

    Parameters
    ----------
    df : PANDAS DATAFRAME
        Transient data being used.
    field : PANDAS DATAFRAME
        Field catalogue being used.

    Returns
    -------
    None.

    """
    def is_inside_ellipse(ra, dec, ra0, dec0, A, B, theta):
        """Check if a point (ra, dec) is inside an ellipse centered at (ra0, dec0)"""
        # Convert theta to radians
        theta = np.radians(theta)

        # Shift coordinates
        x = ra - ra0
        y = dec - dec0

        # Rotate coordinates
        x_prime = x * np.cos(theta) + y * np.sin(theta)
        y_prime = -x * np.sin(theta) + y * np.cos(theta)

        # Ellipse equation
        return (x_prime ** 2) / (A ** 2) + (y_prime ** 2) / (B ** 2) <= 1

    for index, row in tqdm(df.iterrows(), total=len(df), desc="Processing Rows"):
        ra, dec = row["HOSTGAL_RA"], row["HOSTGAL_DEC"]
        
        field_subset = search_catalogue(field,'RA','DEC',row['HOSTGAL_RA'],row['HOSTGAL_DEC'],0.1)
        
        matches = []
        
        for _, sh_row in field_subset.iterrows():
            if is_inside_ellipse(ra, dec, sh_row["RA"], sh_row["DEC"], sh_row["A"], sh_row["B"], sh_row["THETA"]):
                matches.append(sh_row["RA"])  # Just to count matches
        
        if len(matches) == 1:
            df.at[index, "truematch_exist"] = "YES"
        elif len(matches) > 1:
            df.at[index, "truematch_exist"] = "CONFUSION"
        else:
            df.at[index,'truematch_exist'] = 'NO'
            
    return df['truematch_exist']


def AV_Apply(transients,df,radius=0.1,truelabels=False):
    
    
    test_set = transients
    
    host_av1 = []
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

    host_av2 = []
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
    
    matches = []

    for index,row in tqdm(test_set.iterrows(), total=len(test_set), desc="Creating AV Associations"):
        
        #identify nearby hosts from which to calculate dlr values
        
        a_subset = search_catalogue(df,'RA','DEC',row['RA'],row['DEC'],radius)
        
        matches.append(len(a_subset))
        
        a_values = []
        a_hosts = []
        a_ra=[]
        a_dec=[]
        host_z=[]
        host_z_type=[]
        host_a=[]
        host_b=[]
        host_pa=[]
        host_ref=[]

        host_um=[]
        host_gm=[]
        host_rm=[]
        host_im=[]
        host_zm=[]
        host_ym=[]
        
        #SN coordinates
        ra2=row['RA']
        dec2=row['DEC']
        
        for i, j in a_subset.iterrows():
            
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
            #this takes SO long. what's going on here?
            #a_values.append(ASearch_Calc(ra2,dec2,ra1,dec1,a))
            
            ra1r = math.radians(ra1)
            dec1r = math.radians(dec1)
            ra2r = math.radians(ra2)
            dec2r = math.radians(dec2)
            thetar = math.radians(theta)
            
            ar=a*3600
            br=b*3600
            
            x = math.cos(dec1r) * math.sin(dec2r) - math.sin(dec1r) * math.cos(dec2r) * math.cos(ra2r - ra1r)
            
            y = math.cos(dec2r) * math.sin(ra2r - ra1r);
            
            z = math.sin(dec1r) * math.sin(dec2r) + math.cos(dec1r) * math.cos(dec2r) * math.cos(ra2r - ra1r)
            
            d = math.degrees(math.atan2(math.sqrt(x*x + y*y),z))
            
            if a == 0:
                a_values.append(float('inf'))
            else:
                a_values.append(d/a)
            
            a_ra.append(ra1)
            a_dec.append(dec1)
            host_a.append(a)
            host_b.append(b)
            host_pa.append(theta)
            host_ref.append(cat)
            
            host_um.append(U)
            host_gm.append(G)
            host_rm.append(R)
            host_im.append(I)
            host_zm.append(Z)
            host_ym.append(Y)
            
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
        'a-value': a_values,
        'host RA': a_ra,
        'host DEC': a_dec,
        'host z': host_z,
        'host z type': host_z_type,
        'host a':host_a,
        'host b':host_b,
        'host pa':host_pa,
        'host ref':host_ref,
        'host um':host_um,
        'host gm':host_gm,
        'host rm':host_rm,
        'host im':host_im,
        'host zm':host_zm,
        'host ym':host_ym
        })
    
        if new_df.empty:
            # Append None (or placeholders) to all lists since no match was found
            host_av1.append(None)
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
        
            host_av2.append(None)
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
        
        
            continue
        
        # Sort the DataFrame by 'dlr value' in ascending order
        new_df = new_df.sort_values(by='a-value', ascending=True)
        
        HC = -99
        
        host_av1.append(new_df.iloc[0]['a-value'])
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

                    # Append the candidate if it's far enough
                    host_av2.append(new_df.iloc[1 + i]['a-value'])
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
                host_av2.append(None)
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
            host_av2.append(None)
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

        #host_HC.append(HC)
            
    test_set['Min A-Value'] = host_av1
    test_set['A-Value Host RA'] = host_ra1
    test_set['A-Value Host Dec'] = host_dec1
    test_set['A-Value Host z'] = host_z1
    test_set['A-Value Host z Type'] = host_zt
    test_set['A-Value Host a'] = host_a1
    test_set['A-Value Host b'] = host_b1
    test_set['A-Value Host pa'] = host_pa1
    test_set['A-Value Cat 1'] = host_cat1    
    
    test_set['A-Value u 1'] = host_U1
    test_set['A-Value g 1'] = host_G1
    test_set['A-Value r 1'] = host_R1
    test_set['A-Value i 1'] = host_I1
    test_set['A-Value z 1'] = host_Z1
    test_set['A-Value y 1'] = host_Y1

    test_set['Min A-Value 2'] = host_av2
    test_set['A-Value Host RA 2'] = host_ra2
    test_set['A-Value Host Dec 2'] = host_dec2
    test_set['A-Value Host z 2'] = host_z2
    test_set['A-Value Host z Type 2'] = host_zt2
    test_set['A-Value Host a 2'] = host_a2
    test_set['A-Value Host b 2'] = host_b2
    test_set['A-Value Host pa 2'] = host_pa2
    test_set['A-Value Cat 2'] = host_cat2
    
    test_set['A-Value u 2'] = host_U2
    test_set['A-Value g 2'] = host_G2
    test_set['A-Value r 2'] = host_R2
    test_set['A-Value i 2'] = host_I2
    test_set['A-Value z 2'] = host_Z2
    test_set['A-Value y 2'] = host_Y2

    test_set['A-Value dRA 1'] = (test_set['A-Value Host RA'] - test_set['HOSTGAL_RA'])*3600
    test_set['A-Value dDec 1'] = (test_set['A-Value Host Dec'] - test_set['HOSTGAL_DEC'])*3600
    test_set['A-Value dz 1'] = test_set['A-Value Host z'] - test_set['REDSHIFT_FINAL']


    test_set['A-Value dRA 2'] = (test_set['A-Value Host RA 2'] - test_set['HOSTGAL_RA'])*3600
    test_set['A-Value dDec 2'] = (test_set['A-Value Host Dec 2'] - test_set['HOSTGAL_DEC'])*3600
    test_set['A-Value dz 2'] = test_set['A-Value Host z 2'] - test_set['REDSHIFT_FINAL']

    # Define the column set for A-Value calculation (1-2)
    columns_12 = ['A-Value Host a','A-Value Host RA', 'A-Value Host Dec', 'A-Value Host RA 2', 'A-Value Host Dec 2']

    test_set['A-Value_12'] = av_multiwrap(test_set, columns_12)

    # Define the column set for A-Value calculation (2-1)
    columns_12 = ['A-Value Host a 2','A-Value Host RA 2', 'A-Value Host Dec 2', 'A-Value Host RA', 'A-Value Host Dec']

    # Calculate DLR for each row
    test_set['A-Value_21'] = av_multiwrap(test_set, columns_12)
    
    test_set['Matches'] = matches

    if truelabels:    
    
        test_set = check_matches_amajor(test_set)
    
        test_set['truematch_exist'] = check_true_exists(test_set, df)
        
    return test_set
