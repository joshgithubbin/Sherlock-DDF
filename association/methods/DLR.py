#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 15:22:00 2025

@author: joshuaweston
"""

def DLR(a,b,theta,da,db):
    
    import math
    import numpy as np
    
    
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
    
    import math
    
    x = math.cos(dec1) * math.sin(dec2) - math.sin(dec1) * math.cos(dec2) * math.cos(ra2 - ra1)
    
    y = math.cos(dec2) * math.sin(ra2 - ra1);
    
    z = math.sin(dec1) * math.sin(dec2) + math.cos(dec1) * math.cos(dec2) * math.cos(ra2 - ra1)
    
    d = math.degrees(math.atan2(math.sqrt(x*x + y*y),z))*3600
    
    return d

def d_dlr(a,b,theta,ra1,dec1,ra2,dec2):
    
    import math
    
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



def pipe(transient_host_candidates,row):
    
        # compute DLR
        transient_host_candidates['DLR'] = transient_host_candidates.apply(
                    lambda r_: d_dlr(
                        float(r_['A']), float(r_['B']), float(r_['THETA']),
                        float(r_['RA']), float(r_['DEC']),
                        float(row['RA']), float(row['DEC'])
                    ),
                    axis=1
                        )
        
        return transient_host_candidates



def apply_dlr(transients, catalogue,
              radius=15, # radius in arcseconds
              ms=0.8,    # minimum separation for hosts to be distinct, in arcseconds
              n=2):     # number of candidates to return

    from tqdm import tqdm
    from lestrade.browser import search
    import pandas as pd
    
    pd.options.mode.chained_assignment = None

    for index, row in tqdm(transients.iterrows(), total=len(transients), desc="Creating DLR Associations . . . "):
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

        
        # compute DLR
        transient_host_candidates['DLR'] = transient_host_candidates.apply(
                    lambda r_: d_dlr(
                        float(r_['A']), float(r_['B']), float(r_['THETA']),
                        float(r_['RA']), float(r_['DEC']),
                        float(row['RA']), float(row['DEC'])
                    ),
                    axis=1
                        )



        # sort from best (lowest) to worst
        transient_host_candidates = transient_host_candidates.sort_values(
            by='DLR', ascending=True
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
            #s = ang_sep(ra1, dec1, ra2, dec2)
            
            if s < ms:
                transient_host_candidates.loc[transient_host_candidates.index[i+1], 'Drop'] = True

        transient_host_candidates = transient_host_candidates[~transient_host_candidates['Drop']]

        # attach top n hosts

        for i in range(min(n, len(transient_host_candidates))):
            
            cand = transient_host_candidates.iloc[i]

            transients.loc[index, f'DLR Host {i+1} RA']  = cand['RA']
            transients.loc[index, f'DLR Host {i+1} DEC'] = cand['DEC']
            transients.loc[index, f'DLR Host {i+1} A']   = cand['A']
            transients.loc[index, f'DLR Host {i+1} B']   = cand['B']
            transients.loc[index, f'DLR Host {i+1} PA']  = cand['THETA']
            
            transients.loc[index, f'DLR Host {i+1} DLR'] = cand['DLR']

            if pd.notna(cand['ZSP']):
                transients.loc[index, f'DLR Host {i+1} z']      = cand['ZSP']
                transients.loc[index, f'DLR Host {i+1} z type'] = 'ZSP'
            elif pd.notna(cand['ZPH']):
                transients.loc[index, f'DLR Host {i+1} z']      = cand['ZPH']
                transients.loc[index, f'DLR Host {i+1} z type'] = 'ZPH'
            else:
                transients.loc[index, f'DLR Host {i+1} z']      = None
                transients.loc[index, f'DLR Host {i+1} z type'] = None

    return transients

