#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 10:33:11 2025

@author: joshuaweston
"""


def field(cat,catname,fp=None):
    """
    Plot all five (or just one) field.
    """
    import sys
    sys.path.insert(1, '/Users/joshuaweston/Desktop/Live/lestrade/')

    from browser import fields, search
    import matplotlib.pyplot as plt
    import numpy as np

    # Load field definitions
    ddfs, ddfs_pd = fields.load_ddfs(
        path="/Users/joshuaweston/Desktop/Live/lestrade/tools/fields/fields.csv"
    )

    # First pass — find global max count for consistent color scale
    global_max = 0
    for i in ddfs:
        subset = search.search(
            ddfs[i]['RAdeg'],
            ddfs[i]['DECdeg'],
            ddfs[i]['Diameter'] * 1.2,
            cat,
            'RA',
            'DEC'
        )
        if not subset.empty:
            counts, _, _ = np.histogram2d(
                subset['RA'], subset['DEC'],
                bins=100
            )
            global_max = max(global_max, counts.max())

    # Generate subplots
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(10, 8.5), constrained_layout=True)

    axes = axes.ravel()

    hist_img = None  # will store one mappable for colorbar

    for plot_idx, i in enumerate(ddfs):
        subset = search.search(
            ddfs[i]['RAdeg'],
            ddfs[i]['DECdeg'],
            ddfs[i]['Diameter'] * 1.2,
            cat,
            'RA',
            'DEC'
        )

        rac = ddfs[i]['RAdeg']
        decc = ddfs[i]['DECdeg']
        diameter = ddfs[i]['Diameter']

        ax = axes[plot_idx]
        ax.set_xlabel('Right Ascension (degrees)')
        ax.set_ylabel('Declination (degrees)')
        ax.set_title(i, fontsize=16, fontweight='bold')
        ax.set_aspect('equal')
        

        if not subset.empty:
            h = ax.hist2d(
                subset['RA'], subset['DEC'],
                bins=100,
                cmap='plasma',
                cmin=1,
                vmin=0,
                vmax=global_max
            )
            
            count = subset[subset['RA'].notna() & subset['DEC'].notna()].shape[0]
            
            hist_img = h[3]  # store QuadMesh for colorbar
            ddf_fill = None
            circle = plt.Circle((rac, decc), diameter / 2, color='black',fill=False)
            
            ax.text(0.95, 0.05, f"N = {count}",transform=ax.transAxes, ha='right',va='bottom',                  
                bbox={'facecolor':'white', 'alpha':0.5, 'pad':5})

            
        else:
            circle = plt.Circle((rac, decc), diameter / 2, edgecolor='black', facecolor='darkgrey')
            ax.text(rac,decc,"No Data",fontsize=16,ha='center',va='center_baseline',color='whitesmoke')
        
        
        ax.add_artist(circle)

        ax.set_xlim(rac - diameter / 1.8, rac + diameter / 1.8)
        ax.set_ylim(decc - diameter / 1.8, decc + diameter / 1.8)

    # Add ONE shared colorbar
    if hist_img is not None:
        
        fig.colorbar(hist_img, ax=axes, label='Counts',orientation="horizontal",shrink=0.7)
        
    else:
        # Create dummy mappable with same cmap and norm as your hist2d
        import matplotlib as mpl
        
        cmap = mpl.cm.Greys
        norm = mpl.colors.Normalize(vmin=0, vmax=global_max)  # same scale as your heatmaps
        
        dummy_mappable = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
        dummy_mappable.set_array([])  # no data
        
        # Add the colorbar, no label
        fig.colorbar(dummy_mappable, ax=axes, orientation='horizontal', shrink=0.7, label='')
        
    fig.suptitle(f'Coverage for {catname}', fontsize=30, fontweight='bold', y=0.98)
    fig.set_constrained_layout_pads(hspace=0.00001, wspace=0.1)
    
    if fp:
        
        import os
        os.makedirs(fp, exist_ok=True)
        plt.savefig(f"{fp}/coverage.png",dpi=800)
    
    
    plt.show()
    
def plot_z(cat,catname,z,fp=None):
    
    import sys
    sys.path.insert(1, '/Users/joshuaweston/Desktop/Live/lestrade/')

    from browser import fields, search
    import matplotlib.pyplot as plt
    import numpy as np

    # Load field definitions
    ddfs, ddfs_pd = fields.load_ddfs(
        path="/Users/joshuaweston/Desktop/Live/lestrade/tools/fields/fields.csv"
    )

    # Generate subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 10))
    
    axes = axes.ravel()
    
    for plot_idx, i in enumerate(ddfs):
        
        subset = search.search(
            ddfs[i]['RAdeg'],
            ddfs[i]['DECdeg'],
            ddfs[i]['Diameter'] * 1.2,
            cat,
            'RA',
            'DEC'
        )
        subset = subset.dropna(subset=[z])
        subset = subset[(subset[z] >= 0) & (subset[z] < 12)] #optimistic upper limit :)
        
        ax = axes[plot_idx]
        ax.set_title(i, fontsize=16, fontweight='bold')
        
        if not subset.empty:
            
            import math
            
            step = 0.05
            upper = math.ceil(np.nanmax(subset[z]) / step) * step
            
            ax.set_xlabel(z)
            ax.set_ylabel('Counts')
            
            ax.hist(
                subset[z],
                bins=np.arange(0,7.5,0.05).tolist(),
                color=ddfs[i]['Colour'],
                edgecolor='black',
                alpha=0.7
            )
            
            count = subset[subset[z].notna()].shape[0]
            ax.text(0.95, 0.05, f"N {z}= {count}",transform=ax.transAxes, ha='right',va='bottom',                  
                bbox={'facecolor':'white', 'alpha':0.5, 'pad':5})

            
            
        else:
            
            ax.set_facecolor('darkgrey')
            ax.text(0.5,0.5,"No Data",fontsize=16,ha='center',va='center_baseline',color='whitesmoke')
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            
            
    fig.suptitle(f'{z} for {catname}', fontsize=30, fontweight='bold', y=0.98)
    fig.subplots_adjust(top=0.9, hspace=0.4,wspace=0.4)
    
    if fp:
        
        import os
        os.makedirs(fp, exist_ok=True)
        plt.savefig(f"{fp}/{z}.png",dpi=800)
    
    
    plt.show()
            
            
def plot_morph(cat,catname,fp=None):
    
    import sys
    sys.path.insert(1, '/Users/joshuaweston/Desktop/Live/lestrade/')

    from browser import fields, search
    import matplotlib.pyplot as plt
    import numpy as np

    # Load field definitions
    ddfs, ddfs_pd = fields.load_ddfs(
        path="/Users/joshuaweston/Desktop/Live/lestrade/tools/fields/fields.csv"
    )

    # Generate subplots
    fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 10))
    
    axes = axes.ravel()
    
    for plot_idx, i in enumerate(ddfs):
        
        subset = search.search(
            ddfs[i]['RAdeg'],
            ddfs[i]['DECdeg'],
            ddfs[i]['Diameter'] * 1.2,
            cat,
            'RA',
            'DEC'
        )
        subset = subset.dropna(subset=['A'])
        
        ax = axes[plot_idx]
        ax.set_title(i, fontsize=16, fontweight='bold')
        
        if not subset.empty:
            
            import math
            
            subset['e'] = 1 - (subset['B']/subset['A'])
            
            ax.set_xlabel('Semi-major Axis Length')
            ax.set_ylabel('Ellipticity')
            
            ax.scatter(subset['A'],subset['e'],s=5,c=ddfs[i]['Colour'],edgecolors='black',linewidths=0.1)
            ax.set_xscale('log')
            
            count = len(subset['A'])
            
            ax.text(0.95, 0.05, f"N morph= {count}",transform=ax.transAxes, ha='right',va='bottom',                  
                bbox={'facecolor':'white', 'alpha':0.5, 'pad':5})
            
        else:
            
            ax.set_facecolor('darkgrey')
            ax.text(0.5,0.5,"No Data",fontsize=16,ha='center',va='center_baseline',color='whitesmoke')
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xticklabels([])
            ax.set_yticklabels([])
            
            
    fig.suptitle(f'Morphological Summary for {catname}', fontsize=30, fontweight='bold', y=0.98)
    fig.subplots_adjust(top=0.9, hspace=0.4,wspace=0.4)
    
    if fp:
        
        import os
        os.makedirs(fp, exist_ok=True)
        plt.savefig(f"{fp}/morphology.png",dpi=800)
    
    
    plt.show()            
    

def col_discrete(col, unique_ratio_threshold=0.05, max_unique_discrete=20):

    if pd.api.types.is_numeric_dtype(col):
        
        unique_count = col.nunique(dropna=True)
        total_count = len(col)
        unique_ratio = unique_count / total_count
        
        if unique_count <= max_unique_discrete or unique_ratio <= unique_ratio_threshold:
            
            return True
        
        else:
        
            return False
    else:
        return True  # Non-numeric assumed discrete
    
    

            
    
