#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

LESTRADE 

BROWSER

SEARCH.PY

v0.2.1

Functions for searching for objects within given radius of a set of coordinates.

@author: joshuaweston

"""

def search(rac, dec, diameter,
           catalogue = None, ra_label = None, dec_label = None):
    """
    
    Searches for catalogued objects within angular distance of a given RA and DEC.

    Parameters
    ----------
    rac : FLOAT
        Centre of search (Degrees).
        
    dec : FLOAT
        Centre of search (Degrees).
        
    diameter : FLOAT
        Diameter of search (Degrees).
        
    catalogue : PANDAS DATAFRAME, optional
        PD Dataframe of catalogue from which to conduct search. The default is None; in this case, the SDSSDR16 TAP Service is used.
        
    ra_label : STRING, optional
        PD Dataframe's RA Label. The default is None.
        
    dec_label : TYPE, optional
        PD Dataframe's DEC Label. The default is None.

    Returns
    -------
    PANDAS DATAFRAME
        Search results. 
        
        Columns: 'objname', 'RA', 'DEC', 'ZSP', 'ZPH', 'A', 'B', 'THETA', 'CATALOGUE', 'u', 'g', 'r', 'i', 'z', 'y'.

    """   
    
    
    import numpy as np
    import pandas as pd
    
    def haversine(ra_1, dec_1, ra_2, dec_2):
    
        # convert decimal degrees to radians 
        ra_1= np.radians(ra_1)
        dec_1 = np.radians(dec_1)
        ra_2 = np.radians(ra_2)
        dec_2 = np.radians(dec_2)
        
        # haversine formula 
        ra_d = ra_2 - ra_1 
        dec_d = dec_2 - dec_1 
        
        a = np.sin(dec_d/2)**2 + np.cos(dec_1) * np.cos(dec_2) * np.sin(ra_d/2)**2
    
        c = 2 * np.arcsin(np.sqrt(a)) 
    
        return c


    if not catalogue.empty:
        
        try:
            # Calculate radius from diameter
            radius = diameter / 2.0
            
            # Calculate angular separation for each object in the catalogue
            catalogue['separation_{ddf}'] = haversine(catalogue[ra_label], catalogue[dec_label], rac, dec)
            
            # Convert radius from degrees to radians
            radius_rad = np.radians(radius)
            
            # Find objects within the specified radius
            within_radius = catalogue['separation_{ddf}'] <= radius_rad
            
            return catalogue[within_radius]
        
        except Exception as e:
            
            print(f"Encountered error: {e} \nCheck catalogue and corresponding ra and dec labels exist.")
            
            print(f"Reverting to all-sky matching in SDSS.")
        
    # Revert to all-sky searching if no catalogue provided.
    
    import pyvo
    
    
    try:
        service = pyvo.dal.TAPService("https://dc.g-vo.org/tap")
    
        query = f"""
        SELECT TOP 500
          obj_id AS objname,
          ra,
          dec,
          spec_z AS zsp,
          photoz_z AS zph,
          dev_rads[2] AS rcirc,
          dev_abs[2]  AS q,
          dev_phi[2] AS phi,
          photo_flags
        FROM sdssdr16.main
        WHERE 1 = CONTAINS(
            POINT('ICRS', ra, dec),
            CIRCLE('ICRS', {ra}, {dec}, {radius_deg})
        )
        AND class = 3
        """
    
        result = service.run_sync(query)
        df = result.to_table().to_pandas()
        
        is_blended = df['photo_flags'] & (1 << 3) != 0
        is_nodeblend = df['photo_flags'] & (1 << 6) != 0
        
        df = df[~(is_blended & is_nodeblend)]
        
        exclude_bits = [8,26]
        bitmask = 0
        for bit in exclude_bits:
            bitmask |= (1 << bit)
        
        # Example: df is your returned DataFrame
        mask = (df['photo_flags'] & bitmask) == 0
        df = df[mask]
    
        if df.empty:
            pass
    
        df = df.dropna(subset=['rcirc', 'q'])
    
        # Clip q to avoid divide-by-zero or invalid sqrt
        df['q'] = np.clip(df['q'], 0.001, 1.0)
    
        # Compute A, B, THETA
        df['A'] = df['rcirc'] / np.sqrt(df['q'])
        df['B'] = df['A'] * df['q']
        df['THETA'] = (90.0 - df['phi']) % 180.0  # convert from SDSS to PA
    
        # Drop unused columns
        df = df.rename(columns={'ra': 'RA', 'dec': 'DEC', 'zsp': 'ZSP', 'zph': 'ZPH'})
    
        # Convert A and B from arcsec to degrees
        df['A'] /= 3600.
        df['B'] /= 3600.
    
        # Pad with empty bands
        for band in ['u', 'g', 'r', 'i', 'z', 'y']:
            df[band] = None
            
        df['u'] = df['rcirc']
        df['g'] = df['q']
        df['r'] = df['photo_flags']
    
        df['CATALOGUE'] = df['objname']
    
        cols = ['objname', 'RA', 'DEC', 'ZSP', 'ZPH', 'A', 'B', 'THETA', 'CATALOGUE'] + ['u', 'g', 'r', 'i', 'z', 'y']
        return df[cols]
    
    except Exception:
        
        pass   

    # fallback if all tries
    cols = ['objname', 'RA', 'DEC', 'redshift', 'ZSP', 'ZPH', 'A', 'B', 'THETA', 'CATALOGUE'] + ['u', 'g', 'r', 'i', 'z', 'y']
    return pd.DataFrame(columns=cols)

    
    
    
    
    
    