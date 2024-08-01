#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 11:32:16 2024

@author: joshuaweston

Do conesearch for objects in diameter.

"""

from math import radians, cos, sin, asin, sqrt
import numpy as np

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

def search_catalogue(catalogue, ra_label, dec_label, rac, dec, diameter):
    # Calculate radius from diameter
    radius = diameter / 2.0
    
    # Calculate angular separation for each object in the catalogue
    catalogue['separation_{ddf}'] = haversine(catalogue[ra_label], catalogue[dec_label], rac, dec)
    
    # Convert radius from degrees to radians
    radius_rad = np.radians(radius)
    
    # Find objects within the specified radius
    within_radius = catalogue['separation_{ddf}'] <= radius_rad
    
    # Return the filtered catalogue
    return catalogue[within_radius]

