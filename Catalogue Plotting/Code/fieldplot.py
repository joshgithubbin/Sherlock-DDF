#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:35:59 2024

@author: joshuaweston
"""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.legend_handler import HandlerPathCollection

def ddf(field,rac,decc,diameter=3.6):
    
    fig, ax = plt.subplots()
    
    circle = plt.Circle((rac, decc), diameter/2, color='black', fill=False)

    ax.add_artist(circle)

    ax.set_xlim(rac - diameter/1.8, rac + diameter/1.8)
    ax.set_ylim(decc - diameter/1.8, decc + diameter/1.8)

    ax.set_xlabel('Right Ascension (degrees)')
    ax.set_ylabel('Declination (degrees)')  
    
    ax.set_title(field, fontname="Times New Roman",fontsize=16,fontweight='bold')
        
    ax.set_aspect('equal')    

    return fig,ax


def fieldplot(field,label,centre_ra,centre_dec,ra,dec,color='marine',size=0.1,savefig=False,directory=""):

    fig,ax = ddf(field,centre_ra,centre_dec)

    scatter=ax.scatter(ra, dec, s=size,color=color,label=label)  
    
    legend_marker_size = 30  # Adjust this multiplier as needed
    ax.legend(loc='upper right',handler_map={scatter: HandlerPathCollection(marker_pad=0, numpoints=1, sizes=[legend_marker_size])})
    
    plt.subplots_adjust(bottom=0.2)
    
    plt.figtext(0.5, 0.05, f'n = {len(ra)}', ha='center',fontname="Times New Roman", fontsize=12)
    
    if savefig:
        
        fn = f'{directory}/{field}/{field}-{label}.png'
        
        plt.savefig(fn,dpi=savefig)

    plt.show()
    
    return
