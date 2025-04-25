#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:35:59 2024

@author: joshuaweston
"""

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.legend_handler import HandlerPathCollection
import matplotlib.animation as animation
import numpy as np

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


def fieldplot_anim(field, label, centre_ra, centre_dec, ra, dec, color='marine', size=0.1, savefig=False, directory=""):
    # Create the figure and axis
    fig, ax = ddf(field, centre_ra, centre_dec)  # Assuming ddf creates a pre-configured plot
    
    # Placeholder for the scatter plot (initially empty)
    scatter = ax.scatter([], [], s=size, color=color, label=label)
    
    # Add legend with a fixed marker size
    legend_marker_size = 30
    ax.legend(
        loc='upper right',
        handler_map={scatter: HandlerPathCollection(marker_pad=0, numpoints=1, sizes=[legend_marker_size])}
    )
    
    # Add additional figure text for displaying the number of points
    text = fig.text(0.5, 0.05, '', ha='center', fontname="Times New Roman", fontsize=12)
    
    # Function to update the scatter plot
    def update_scatter(i):
        # Update data for the first `i` points
        current_ra = ra[:i]
        current_dec = dec[:i]
        
        # Update scatter plot data
        scatter.set_offsets(np.c_[current_ra, current_dec])
        
        # Update the text below the plot with the current number of points
        text.set_text(f'n = {len(current_ra)}')
        
    # Create the animation
    anim = animation.FuncAnimation(
        fig,
        update_scatter,
        frames=np.arange(0, len(ra), 1000),  # Update every 10,000 points
        interval=100,  # Adjust interval to control the speed (500ms between frames)
        repeat=False
    )
    
    # Save the animation if requested
    if savefig:
        fn = f'{directory}/{field}/{label}/{field}-{label}_animation.gif'
        anim.save(fn, writer='ffmpeg', dpi=300)
    
    # Show the animation
    plt.show()
    
    return


def fieldplot(field,label,centre_ra,centre_dec,ra,dec,color='marine',size=0.1,savefig=False,fn="",directory=""):

    fig,ax = ddf(field,centre_ra,centre_dec)

    scatter=ax.scatter(ra, dec, s=size,color=color,label=label)  
    
    legend_marker_size = 30  # Adjust this multiplier as needed
    ax.legend(loc='upper right',handler_map={scatter: HandlerPathCollection(marker_pad=0, numpoints=1, sizes=[legend_marker_size])})
    
    plt.subplots_adjust(bottom=0.2)
    
    plt.figtext(0.5, 0.05, f'n = {len(ra)}', ha='center',fontname="Times New Roman", fontsize=12) 

    if savefig:
        
        fn = f'{directory}'
        
        plt.savefig(fn,dpi=savefig)

    plt.show()
    
    return
