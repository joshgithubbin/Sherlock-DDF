#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 15:12:10 2025

@author: joshuaweston
"""

def apply_method(transients, catalogue, method, metric, radius=15, ms=0.8,n=2):     # number of candidates to return

    from tqdm import tqdm
    from lestrade.browser import search
    import pandas as pd
    
    pd.options.mode.chained_assignment = None

    for index, row in tqdm(transients.iterrows(), total=len(transients), desc=f"Creating {metric} Associations . . . "):
    #for index, row in transients.iterrows():
        # identify nearby hosts from which to calculate dlr values
        transient_host_candidates = search.search(
            row['RA'],
            row['DEC'],
            radius * 2. * (1./3600.),
            catalogue,
            'RA',
            'DEC'
        )
        

        method_pipe = method.pipe 
        
        transient_host_candidates  = method_pipe(transient_host_candidates, row)


        # sort from best (lowest) to worst
        transient_host_candidates = transient_host_candidates.sort_values(
            by=f'{metric}', ascending=True
        ).reset_index(drop=True)
        
        transient_host_candidates['Ncand'] = len(transient_host_candidates)
        
        # initialize Drop column
        transient_host_candidates['Drop'] = False

        # remove duplicates among neighbouring rows
        for i in range(len(transient_host_candidates) - 1):
            
            
            from astropy.coordinates import SkyCoord
            from astropy import units as u
            
            
            ra1, dec1 = transient_host_candidates.iloc[i][['RA', 'DEC']]
            ra2, dec2 = transient_host_candidates.iloc[i+1][['RA', 'DEC']]

            best_coord = SkyCoord(ra=ra1 * u.deg, 
                                          dec= dec1 * u.deg)
            current_coord = SkyCoord(ra=ra2 * u.deg, 
                                             dec= dec2 * u.deg)
                    
            s = best_coord.separation(current_coord).arcsec  # Separation in arcseconds
            
            if s < ms:
                transient_host_candidates.loc[transient_host_candidates.index[i+1], 'Drop'] = True

        transient_host_candidates = transient_host_candidates[~transient_host_candidates['Drop']]
        
        if len(transient_host_candidates) > 1:
            transients.loc[index,f'{metric} Host Confusion'] = compute_HC(transient_host_candidates[f'{metric}'])

        # attach top n hosts

        for i in range(min(n, len(transient_host_candidates))):
            
            cand = transient_host_candidates.iloc[i]
            
            transients.loc[index,f'Ncand'] = cand[f'Ncand']
            
            transients.loc[index,f'{metric} Host {i+1} GalID'] = cand['GalID']

            transients.loc[index, f'{metric} Host {i+1} RA']  = cand['RA']
            transients.loc[index, f'{metric} Host {i+1} DEC'] = cand['DEC']
            transients.loc[index, f'{metric} Host {i+1} A']   = cand['A']
            transients.loc[index, f'{metric} Host {i+1} B']   = cand['B']
            transients.loc[index, f'{metric} Host {i+1} PA']  = cand['THETA']
            
            transients.loc[index, f'{metric} Host {i+1} {metric}'] = cand[f'{metric}']
            
            transients.loc[index, f'{metric} Host {i+1} S'] = base_ang_sep(cand['RA'],cand['DEC'],transients.loc[index,'RA'],transients.loc[index,'DEC'])

            if pd.notna(cand['ZSP']):
                transients.loc[index, f'{metric} Host {i+1} z']      = cand['ZSP']
                transients.loc[index, f'{metric} Host {i+1} z type'] = 'ZSP'
            elif pd.notna(cand['ZPH']):
                transients.loc[index, f'{metric} Host {i+1} z']      = cand['ZPH']
                transients.loc[index, f'{metric} Host {i+1} z type'] = 'ZPH'
            else:
                transients.loc[index, f'{metric} Host {i+1} z']      = None
                transients.loc[index, f'{metric} Host {i+1} z type'] = None

    return transients


def base_ang_sep(ra1,dec1,ra2,dec2):
    
    import math
    
    ra1, dec1, ra2, dec2 = map(math.radians, [ra1, dec1, ra2, dec2])
    
    x = math.cos(dec1) * math.sin(dec2) - math.sin(dec1) * math.cos(dec2) * math.cos(ra2 - ra1)
    
    y = math.cos(dec2) * math.sin(ra2 - ra1);
    
    z = math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra2 - ra1)
    
    d = math.degrees(math.atan2(math.sqrt(x*x + y*y),z))*3600
    
    return d


def compute_HC(D, epsilon=1e-5):
    
    """
    Compute the Host Confusion (HC) parameter for a given SN.
    
    Parameters:
        D (numpy array): Array of galaxy separations, sorted from lowest to highest.
        epsilon (float): Small constant to avoid division by zero.
    
    Returns:
        float: HC value
    """
    
    import numpy as np
    
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