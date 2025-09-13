#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 18:08:22 2025

@author: joshuaweston
"""


def av_calc(ra_sn, dec_sn, ra_host, dec_host, a):
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
    from astropy.coordinates import SkyCoord
    from astropy import units as u
    
    # Convert coordinates to SkyCoord objects
    sn_coord = SkyCoord(ra=ra_sn * u.deg, dec=dec_sn * u.deg, frame='icrs')
    host_coord = SkyCoord(ra=ra_host * u.deg, dec=dec_host * u.deg, frame='icrs')

    # Calculate angular separation in degrees
    separation = sn_coord.separation(host_coord).deg
    
    # Normalize by semimajor axis
    return separation / a if a > 0 else float('inf')  # Avoid division by zero


def pipe(transient_host_candidates, row):
    # compute AV
    transient_host_candidates['AV'] = transient_host_candidates.apply(
        lambda r_: av_calc(
            float(row['RA']), float(row['DEC']),
            float(r_['RA']), float(r_['DEC']), float(r_['A'])
        ),
        axis=1
    )
    
    return transient_host_candidates

def features(df):
    
    #dlr 1-2
    df['AV 1-2'] = df.apply(
                lambda df: av_calc(
                    float(df['AV Host 2 RA']), float(df['AV Host 2 DEC']),
                    float(df['AV Host 1 RA']), float(df['AV Host 1 DEC']), float(df['AV Host 1 A'])
                ),
                axis=1
                    )
    
    #dlr 2-1
    df['AV 2-1'] = df.apply(
                lambda df: av_calc(
                    float(df['AV Host 1 RA']), float(df['AV Host 1 DEC']),
                    float(df['AV Host 2 RA']), float(df['AV Host 2 DEC']), float(df['AV Host 2 A'])
                ),
                axis=1
                    )
    
    return df