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


def features(df):
    
    #dlr 1-2
    df['DLR 1-2'] = df.apply(
                lambda df: d_dlr(
                    float(df['DLR Host 1 A']), float(df['DLR Host 1 B']), float(df['DLR Host 1 PA']),
                    float(df['DLR Host 1 RA']), float(df['DLR Host 1 DEC']),
                    float(df['DLR Host 2 RA']), float(df['DLR Host 2 DEC'])
                ),
                axis=1
                    )
    
    #dlr 2-1
    df['DLR 2-1'] = df.apply(
                lambda df: d_dlr(
                    float(df['DLR Host 2 A']), float(df['DLR Host 2 B']), float(df['DLR Host 2 PA']),
                    float(df['DLR Host 2 RA']), float(df['DLR Host 2 DEC']),
                    float(df['DLR Host 1 RA']), float(df['DLR Host 1 DEC'])
                ),
                axis=1
                    )
    
    return df



