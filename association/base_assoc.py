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

        # attach top n hosts

        for i in range(min(n, len(transient_host_candidates))):
            
            cand = transient_host_candidates.iloc[i]

            transients.loc[index, f'{metric} Host {i+1} RA']  = cand['RA']
            transients.loc[index, f'{metric} Host {i+1} DEC'] = cand['DEC']
            transients.loc[index, f'{metric} Host {i+1} A']   = cand['A']
            transients.loc[index, f'{metric} Host {i+1} B']   = cand['B']
            transients.loc[index, f'{metric} Host {i+1} PA']  = cand['THETA']
            
            transients.loc[index, f'{metric} Host {i+1} {metric}'] = cand[f'{metric}']

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