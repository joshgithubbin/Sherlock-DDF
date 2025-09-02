#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 09:46:30 2025

@author: joshuaweston
"""

class aide:
    
    def __init__(self,row):
        
        import numpy as np
        import matplotlib.pyplot as plt
        import math
        import os
        
        self._row = row
        
        self._ra_sn = self._row['RA']
        self._dec_sn = self._row['DEC']
        self._name = self._row['SNID']
        
        plt.figure(figsize=(8, 8))
        
        # Mark the supernova position
        plt.scatter([0], [0], color="red", label="Supernova", zorder=5)
        
        # Set plot properties
        plt.xlabel('ΔRA (")',fontsize=20)
        plt.ylabel('ΔDec (")',fontsize=20)
        plt.tick_params(axis='both', which='major', labelsize=16)
        
        plt.gca().invert_xaxis()
        plt.title(f"{self._ra_sn}, {self._dec_sn}",fontsize=20)
        plt.axis("equal")
        
    def save(self,fp):
        
        import matplotlib.pyplot as plt
        import os
        
        plt.savefig(os.path.join(fp, f"{self._name}.png"), dpi=400)
        
        plt.close()
        
    def desc(self, metric, n):
                
        import matplotlib.pyplot as plt
        
        zt = self._row[f'{metric} Host {n} z type'] 
        z = self._row[f'{metric} Host {n} z'] 
        
        if zt is not None:
            
            z_desc = f', {zt} = {z:.2f}'
            
        else:
            
            z_desc = f', No z given'

        min_val = self._row[f'{metric} Host {n} {metric}']
        
        
        txt = f"Associated with Minimum {metric} = {min_val:.4f}{z_desc}"
        
        plt.text(0.02, 0.98, txt, ha='left', va='top', transform=plt.gca().transAxes, fontsize=16,
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
        
    def match_flag(self, match, overwrite,truehost):
        
        import matplotlib.pyplot as plt
        
        if match == 'YES':
            text = 'Consistent Match' + (' (Overwritten)' if overwrite == 'YES' else '')
            plt.text(0.02, 0.05, text, ha='left', va='top', transform=plt.gca().transAxes,
                     bbox=dict(facecolor='palegreen', edgecolor='black', boxstyle='round,pad=0.3'))
        else:
            plt.text(0.02, 0.05, 'Inconsistent Match', ha='left', va='top', transform=plt.gca().transAxes,
                     bbox=dict(facecolor='lightcoral', edgecolor='black', boxstyle='round,pad=0.3'))
            
        if truehost == 'NO':
            plt.text(0.78, 0.05, 'True Host Missing', ha='left', va='top', transform=plt.gca().transAxes,
                     bbox=dict(facecolor='gold', edgecolor='black', boxstyle='round,pad=0.3'))
            
    def annotation_flags(self,labels):
        
        import matplotlib.pyplot as plt
        
        if "blended" in str(labels).lower():
            plt.text(
                0.02, 0.1, "Blended Host",
                ha="left", va="top", transform=plt.gca().transAxes,
                bbox=dict(facecolor="gold", edgecolor="black", boxstyle="round,pad=0.3")
            )
            
        if "ds" in str(labels).lower():
            plt.text(
                0.02, 0.1, "Potential Diffraction Spike",
                ha="left", va="top", transform=plt.gca().transAxes,
                bbox=dict(facecolor="gold", edgecolor="black", boxstyle="round,pad=0.3")
            )



    def plot_galaxy(self,metric,n,color,alpha=1.0,linestyle='--'):
        
        import math
        import numpy as np
        import matplotlib.pyplot as plt
        
        if metric == 'True':
            
            a = self._row[f'truematch A']
            b = self._row[f'truematch B']
            theta_deg = self._row[f'truematch THETA']
            
            ra_gal = self._row[f'truematch RA']
            dec_gal = self._row[f'truematch Dec']
            
        else:
        
            a = self._row[f'{metric} Host {n} A']
            b = self._row[f'{metric} Host {n} B']
            theta_deg = self._row[f'{metric} Host {n} PA']
            
            ra_gal = self._row[f'{metric} Host {n} RA']
            dec_gal = self._row[f'{metric} Host {n} DEC']
        
        # Convert theta to radians
        theta = math.radians(theta_deg)
        
        # Convert semi-major and semi-minor axes from degrees to arcseconds
        a_arcsec = a * 3600
        b_arcsec = b * 3600

        # Create an ellipse in parametric form
        t = np.linspace(0, 2 * np.pi, 500)
        ellipse_x = a_arcsec * np.cos(t)
        ellipse_y = b_arcsec * np.sin(t)

        # Rotation matrix
        R = np.array([[np.cos(theta), -np.sin(theta)], 
                      [np.sin(theta), np.cos(theta)]])
        
        # Rotate the ellipse
        rotated_ellipse = R @ np.array([ellipse_x, ellipse_y])
        
        # Shift ellipse to galaxy center relative to the supernova
        delta_ra = (ra_gal - self._ra_sn) * 3600
        delta_dec = (dec_gal - self._dec_sn) * 3600
        ellipse_x_shifted = rotated_ellipse[0] + delta_ra
        ellipse_y_shifted = rotated_ellipse[1] + delta_dec

        # Plot the ellipse
        plt.plot(ellipse_x_shifted, ellipse_y_shifted, linestyle=linestyle, color=color, alpha=alpha)

        # Semi-major and semi-minor axes
        major_axis = np.array([[-a_arcsec, a_arcsec], [0, 0]])
        minor_axis = np.array([[0, 0], [-b_arcsec, b_arcsec]])

        # Rotate and shift the axes
        rotated_major = R @ major_axis
        rotated_minor = R @ minor_axis
        major_x_shifted = rotated_major[0] + delta_ra
        major_y_shifted = rotated_major[1] + delta_dec
        minor_x_shifted = rotated_minor[0] + delta_ra
        minor_y_shifted = rotated_minor[1] + delta_dec

        # Plot the axes
        plt.plot(major_x_shifted, major_y_shifted, color=color, linestyle=":", alpha=alpha)
        plt.plot(minor_x_shifted, minor_y_shifted, color=color, linestyle=":", alpha=alpha)

        # Mark the galaxy center
        plt.scatter([delta_ra], [delta_dec], color=color, zorder=5)
        
        plt.plot([0, delta_ra], [0, delta_dec], color="black", linestyle="--", label=f"SN to {metric} Host {n}")
        
        

def plot_method(transients,metric,n,fp,annotate=False,plot_true_host=False):
    
    from tqdm import tqdm
    import os
    
    if not plot_true_host:
    
        for index,row in tqdm(transients.iterrows(),total=len(transients),desc=f"\tPlotting {metric} Associations . . . "):
            
            plot = aide(row)
            
            for i in range(1,n+1):
                
                ls = '-' if i == 1 else '--'
                
                plot.plot_galaxy(metric,i,color='black',linestyle=ls)
            
            plot.desc(metric,1)
            
            if annotate:
                
                plot.annotation_flags(row[f'{metric} Host 1 GalID Label'])
            
            plot.save(fp)
            
    else:
        
        fps = [['consistent','YES'],['inconsistent','NO']]
        
        for label, value in fps:
            
            subset = transients[transients[f'{metric} MATCH'] == value]
            
            fp1 = f'{fp}{label}/'
            os.makedirs(fp1, exist_ok=True)

            for index,row in tqdm(subset.iterrows(),total=len(subset),desc=f"\tPlotting {label} {metric} Associations . . . "):
                
                plot = aide(row)
                
                for i in range(1,n+1):
                    
                    ls = '-' if i == 1 else '--'
                    
                    plot.plot_galaxy(metric,i,color='black',linestyle=ls)
                    
                plot.plot_galaxy('True',i,color='green',linestyle='-')
                
                plot.desc(metric,1)
                
                plot.match_flag(row[f'{metric} MATCH'],row[f'{metric} Overwritten'],row['truematch_exist'])
                
                if annotate:
                    
                    plot.annotation_flags(row[f'{metric} Host 1 GalID Label'])               
                
                plot.save(fp1)
    
    return