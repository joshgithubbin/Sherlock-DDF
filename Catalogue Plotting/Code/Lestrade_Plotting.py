#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:41:31 2025

@author: joshuaweston
"""

import matplotlib.pyplot as plt
import numpy as np
import math

def plot_host(method, metric, a1, b1, theta_deg1, ra1, dec1, 
              a2, b2, theta_deg2, ra2_host, dec2_host, 
              ra_sn, dec_sn, min_val, min_val_2,
              min_z, min_zt, min_z_2, min_zt_2, cat1, cat2, 
              orig_ra=None, orig_dec=None, name=None,fp=None, match=None, 
              blend=None, spike=None, trueflag=None, 
              truera=None, truedec=None, truea=None, trueb=None, truepa=None, overwrite=None):
    """
    Plot two ellipses (galaxies), their axes, and the supernova position on the sky.
    If `trueflag` is set, the true host galaxy is also plotted in green.
    """

    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import os
    
    def plot_ellipse_and_axes(a, b, theta_deg, ra_center, dec_center, label, color, alpha=1.0,linestyle='--'):
        """
        Helper function to plot an ellipse and its major/minor axes.
        """
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
        delta_ra = (ra_center - ra_sn) * 3600
        delta_dec = (dec_center - dec_sn) * 3600
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

        return delta_ra, delta_dec

    # Start plotting
    plt.figure(figsize=(8, 8))

    # Plot first host
    delta_ra1, delta_dec1 = plot_ellipse_and_axes(a1, b1, theta_deg1, ra1, dec1, "Host 1", "black")

    # Plot second host
    delta_ra2, delta_dec2 = plot_ellipse_and_axes(a2, b2, theta_deg2, ra2_host, dec2_host, "Host 2", "black", alpha=0.3)

    # Mark the supernova position
    plt.scatter([0], [0], color="red", label="Supernova", zorder=5)

    # Draw lines to hosts
    plt.plot([0, delta_ra1], [0, delta_dec1], color="black", linestyle="-", label="SN to Host 1")
    plt.plot([0, delta_ra2], [0, delta_dec2], color="black", alpha=0.3, linestyle="--", label="SN to Host 2")

    if trueflag and truera is not None and truedec is not None:
        # Plot the true host
        delta_ra_true, delta_dec_true = plot_ellipse_and_axes(truea, trueb, truepa, truera, truedec, "True Host", "green",alpha=0.3,linestyle='-')

        # Draw a line to the true host
        plt.plot([0, delta_ra_true], [0, delta_dec_true], color="green", linestyle="--", label="SN to True Host")

    # Additional text and indicators
    if orig_ra is not None and orig_dec is not None:
        delta_rao = (orig_ra - ra_sn) * 3600
        delta_deco = (orig_dec - dec_sn) * 3600
        plt.plot([0, delta_rao], [0, delta_deco], color="green", linestyle="--", label="SN to Host 2")

        if match == 'YES':
            text = 'Consistent Match' + (' (Overwritten)' if overwrite == 1 else '')
            plt.text(0.02, 0.05, text, ha='left', va='top', transform=plt.gca().transAxes,
                     bbox=dict(facecolor='palegreen', edgecolor='black', boxstyle='round,pad=0.3'))
        else:
            plt.text(0.02, 0.05, 'Inconsistent Match', ha='left', va='top', transform=plt.gca().transAxes,
                     bbox=dict(facecolor='lightcoral', edgecolor='black', boxstyle='round,pad=0.3'))

    if blend == 1:
        plt.text(0.02, 0.1, 'Blended Host', ha='left', va='top', transform=plt.gca().transAxes,
                 bbox=dict(facecolor='gold', edgecolor='black', boxstyle='round,pad=0.3'))
    elif spike == 1:
        plt.text(0.02, 0.1, 'Potential Diffraction Spikes', ha='left', va='top', transform=plt.gca().transAxes,
                 bbox=dict(facecolor='gold', edgecolor='black', boxstyle='round,pad=0.3'))

    if trueflag == 'NO':
        plt.text(0.78, 0.05, 'True Host Missing', ha='left', va='top', transform=plt.gca().transAxes,
                 bbox=dict(facecolor='gold', edgecolor='black', boxstyle='round,pad=0.3'))

    if min_zt == 'both NaN':
        z_desc_1 = ', No known z'
        z_desc_2 = ''
    elif min_zt_2 is None or min_zt_2 == 'both NaN':
        z_desc_1 = f', {min_zt} = {min_z:.2f}'
        z_desc_2 = ', No z given'
    else:
        z_desc_1 = f', {min_zt} = {min_z:.2f}'
        z_desc_2 = f', {min_zt_2} = {min_z_2:.2f}'

    desc = f"Associated with Minimum {metric} = {min_val:.4f}{z_desc_1}, from {cat1}"
    if not math.isnan(min_val_2):
        desc += f"\nSecond Lowest {metric} = {min_val_2:.4f}{z_desc_2}, from {cat1}"

    plt.text(0.02, 0.98, desc, ha='left', va='top', transform=plt.gca().transAxes,
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    # Set plot properties
    plt.xlabel('ΔRA (")')
    plt.ylabel('ΔDec (")')
    plt.gca().invert_xaxis()
    plt.title(f"{method} Separation {ra_sn}, {dec_sn}")
    plt.axis("equal")

    if name and fp:
        # Determine subfolder based on match status
        if match == 'YES':
            subfolder = "Consistent"
        elif match == 'NO':
            subfolder = "Inconsistent"
        else:
            subfolder = ""

        # Construct full path: fp/method/subfolder/
        save_path = os.path.join(fp, method, subfolder)
        os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists

        # Save the plot
        plt.savefig(os.path.join(save_path, f"{name}.png"), dpi=400)


    plt.show()

def feature_plotting(df, method, fp=False):
    
    import os

    def histplot(df, column, label, scale='linear', fp=False):
        df_yes = df[df[f'{method} MATCH'] == 'YES']
        plt.hist(df_yes[column], bins=30, alpha=0.5, label=f'{method} MATCH = YES', color='green')

        df_no = df[df[f'{method} MATCH'] == 'NO']
        df_no[column] = df_no[column].replace([np.inf, -np.inf], np.nan).dropna()
        plt.hist(df_no[column], bins=30, alpha=0.5, label=f'{method} MATCH = NO', color='red')

        plt.title('')
        plt.xlabel(label)
        plt.ylabel('Frequency')
        plt.legend()
        plt.yscale(scale)
        plt.grid(True)

        if fp:


            save_path = os.path.join(fp, f'{method}/Feature Distributions/')
            os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists
            
            save_fp = os.path.join(save_path, f'{column}.png')
            plt.savefig(save_fp, dpi=400)

        plt.show()

    histplot(df, 'Matches', 'Candidates within 0.1 deg', scale='log', fp=fp)
    histplot(df, f'Min {method}', f'Minimum {method}', scale='log', fp=fp)
    histplot(df, f'Min {method} 2', f'2nd Minimum {method}', scale='log', fp=fp)

    if method == 'DLR':
        histplot(df, f'{method} HC', 'Host Confusion Parameter', scale='log', fp=fp)

    histplot(df, f'{method} S', f'Angular Separation from Best Host', scale='log', fp=fp)
    histplot(df, f'{method} S 2', f'Angular Separation from 2nd Best Host', scale='log', fp=fp)
    histplot(df, f'{method} S_12', f'Angular Separation between Hosts', scale='log', fp=fp)
    histplot(df, f'd{method}', f'{method} Difference', scale='log', fp=fp)
    histplot(df, f'r{method}', f'{method} Ratio', scale='log', fp=fp)
    histplot(df, f'{method}_12', f'{method} (1st to 2nd Host)', scale='log', fp=fp)
    histplot(df, f'{method}_21', f'{method} (2nd to 1st Host)', scale='log', fp=fp)