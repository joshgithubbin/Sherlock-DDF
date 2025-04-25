#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 13:22:16 2025

@author: joshuaweston
"""

import Lestrade_Catalogues as lcat
import Lestrade_gen_sample as lgs
import Lestrade_DLR as ldlr
import Lestrade_AV as lav
import Lestrade_Overwrite_Matches as lom
import Lestrade_Confusion as lcon

import pandas as pd
import os

from Lestrade_Plotting import *


def apply_searches(df, field, check=False, methods=['DLR', 'AV']):
    
    test_set_1, test_set_2 = None, None

    if 'DLR' in methods:
        test_set_1 = ldlr.DLR_Apply(df, field, radius=0.1, truelabels=check)
        
        #ratios and angular separation
        
        df['dDLR'] = df['Min DLR'] - df['Min DLR 2']

        df['rDLR'] = df['Min DLR'] / df['Min DLR 2']

        df['DLR S'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['RA']), 
            math.radians(row['DEC']), 
            math.radians(row['DLR Host RA']), 
            math.radians(row['DLR Host Dec'])
        ), axis=1)

        df['DLR S 2'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['RA']), 
            math.radians(row['DEC']), 
            math.radians(row['DLR Host RA 2']), 
            math.radians(row['DLR Host Dec 2'])
        ), axis=1)

        df['DLR S_12'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['DLR Host RA']), 
            math.radians(row['DLR Host Dec']), 
            math.radians(row['DLR Host RA 2']), 
            math.radians(row['DLR Host Dec 2'])
        ), axis=1)

        df['DLR S_21'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['DLR Host RA 2']), 
            math.radians(row['DLR Host Dec 2']), 
            math.radians(row['DLR Host RA']), 
            math.radians(row['DLR Host Dec'])
        ), axis=1)


    if 'AV' in methods:
        test_set_2 = lav.AV_Apply(df, field, radius=0.1, truelabels=check)
        
        #ratios and angular separation
        df['dA-Value'] = df['Min A-Value'] - df['Min A-Value 2']

        df['rA-Value'] = df['Min A-Value'] / df['Min A-Value 2']

        df['A-Value S'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['RA']), 
            math.radians(row['DEC']), 
            math.radians(row['A-Value Host RA']), 
            math.radians(row['A-Value Host Dec'])
        ), axis=1)

        df['A-Value S 2'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['RA']), 
            math.radians(row['DEC']), 
            math.radians(row['A-Value Host RA 2']), 
            math.radians(row['A-Value Host Dec 2'])
        ), axis=1)

        df['A-Value S_12'] = df.apply(lambda row: ldlr.ang_sep(
            math.radians(row['A-Value Host RA']), 
            math.radians(row['A-Value Host Dec']), 
            math.radians(row['A-Value Host RA 2']), 
            math.radians(row['A-Value Host Dec 2'])
        ), axis=1)

    # If both methods are used, merge the results
    if test_set_1 is not None and test_set_2 is not None:
        cols_to_merge = [col for col in test_set_2.columns if col not in test_set_1.columns]
        test_set = pd.merge(test_set_1, test_set_2[["SNID"] + cols_to_merge], on="SNID")
    else:
        # Return whichever dataset was created
        test_set = test_set_1 if test_set_1 is not None else test_set_2

    return test_set

def plot_association(df,method,metric,fp='Default/'):
    
    
    #blend=['Blended'],spike=row[f'{method} Spike'],overwrite=row['Overwritten']
    
    for index, row in df.iterrows():
        
        plot_host(
            method=method,metric=metric,a1=row[f"{method} Host a"], b1=row[f'{method} Host b'], theta_deg1=row[f'{method} Host pa'], 
            ra1=row[f'{method} Host RA'], dec1=row[f'{method} Host Dec'],
            a2=row[f'{method} Host a 2'], b2=row[f'{method} Host b 2'], theta_deg2=row[f'{method} Host pa 2'], 
            ra2_host=row[f'{method} Host RA 2'], dec2_host=row[f'{method} Host Dec 2'],
            ra_sn=row['RA'], dec_sn=row['DEC'],
            min_val=row[f'Min {method}'], min_val_2=row[f'Min {method} 2'],
            min_z =row[f'{method} Host z'],min_zt=row[f'{method} Host z Type'],
            min_z_2 = row[f'{method} Host z 2'], min_zt_2=row[f'{method} Host z Type 2'],
            orig_ra = row[f'HOSTGAL_RA'],orig_dec=row[f'HOSTGAL_DEC'],name=row['SNID'], fp=fp,
            cat1=row[f'{method} Cat 1'], cat2=row[f'{method} Cat 2'], match=row[f'{method} MATCH'], 
            trueflag = row['truematch_exist'], truera=row['truematch RA'],truedec=row['truematch Dec'],
            truea=row['truematch A'],trueb=row['truematch B'],truepa=row['truematch THETA']
        )

#save as json
XMM_LSS = {
    "SPLASH-SXDF": {
        "ZSP": "zspec", 
        "ZPH": "zphot",
        "A": "amaj", 
        "B": "bmin", 
        "PA": "PA",
        "u": "umagC", 
        "g": "gmagC", 
        "r": "rmagC", 
        "i": "imagC", 
        "z": "zmagC",
    },
    
    "CFHQSIR": {
        "A": "AaxisY", 
        "B": "BaxisY", 
        "PA": "thetaY",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag", 
        "y": "ymag",
    },
    
}



ECDFS = {
    
    "ACS-GC": {
        "ZPH": "zph",
        "ZSP": "zsp",
        "A": "a1", 
        "B": "b1", 
        "PA": "PA1",
        "u": "umag", 
        "g": "gmag", 
        "r": "rmag", 
        "i": "imag", 
        "z": "zmag",
        
        "axis_scale": 0.03/3600.
    },
    
    "Chandra-Multi": {
        "ZPH": "MCz",
        "A": "MajAxis", 
        "B": "MinAxis", 
        "PA": "PA",
        "u": "usMAG", 
        "g": "gsMAG", 
        "r": "rsMAG",
        
        "axis_scale": 1.0/3600.
    },
    
    "GOODS-S-CANDELS": {
        "A": "a(H)", 
        "B": "b(H)", 
        "PA": "PA",
        
        "axis_scale": 0.06/3600
    }}

def lestrade(field, field_str, df_fp, save=True, overwrite=False, annotate=False, check=False, plot=False, compare=False,feature_analysis=False):

    # Determine output file path
    annotated = "annotated_" if annotate else ""
    output_dir = f'../Output/{df_fp}/{field_str}'
    output_file = f'{output_dir}/{df_fp}_{annotated}output.csv'

    # Ensure the directory exists
    os.makedirs(output_dir, exist_ok=True)

    # If the file exists and overwrite is False, import it
    if os.path.exists(output_file) and not overwrite:
        print(f"File {output_file} already exists. Importing...")
        df_final = pd.read_csv(output_file)
    else:
        
        # Generate dataframes
        xmm = lcat.gen_cat(field, field_str)

        test_Set = lgs.gen_sample(filepath=f'../Output/{df_fp}/{df_fp}.csv', field=field_str,
                                   DDF_path='../DDF_Coordinates.csv', catlist='../Catalogue_List.csv')

        df_final = apply_searches(test_Set, xmm, check=check)

    # Annotate
    if annotate:
        config_dir = f'{output_dir}/config'
        os.makedirs(config_dir, exist_ok=True)
        
        df_final = lom.update_dataframe_overwrite(df_final, f'{config_dir}/{df_fp}_overwrite.txt')
        df_final = lom.update_dataframe_blended(df_final, f'{config_dir}/{df_fp}_blended.txt')
        df_final = lom.update_dataframe_spikes(df_final,
                                               DLR1=f'{config_dir}/{df_fp}_sdlr1.txt',
                                               DLR2=f'{config_dir}/{df_fp}_sdlr2.txt',
                                               AV1=f'{config_dir}/{df_fp}_sav1.txt',
                                               AV2=f'{config_dir}/{df_fp}_sav2.txt')

    # Save if required
    if save:
        df_final.to_csv(output_file, index=False)

    # Plot
    if plot:
        plot_dir = f'{output_dir}/Plots'
        os.makedirs(plot_dir, exist_ok=True)

        plot_association(df_final, 'DLR', "$d_{{DLR}}$", fp=plot_dir)
        plot_association(df_final, 'A-Value', 'AV', fp=plot_dir)

    if compare:
        lcon.lcon(df_final,remove_notruematch=False,remove_blended=False,remove_spikes=False)
        
        lcon.lcon(df_final,remove_notruematch=True,remove_blended=False,remove_spikes=False)
        
        lcon.lcon(df_final,remove_notruematch=True,remove_blended=True,remove_spikes=False)
        
        lcon.lcon(df_final,remove_notruematch=True,remove_blended=True,remove_spikes=True)

    # Feature analysis
    if feature_analysis:
        plot_dir = f'{output_dir}/Plots'
        os.makedirs(plot_dir, exist_ok=True)
        feature_plotting(df_final, 'DLR', fp=plot_dir)
        feature_plotting(df_final, 'A-Value', fp=plot_dir)

    return df_final

# Call function
df = lestrade(XMM_LSS,'XMM-LSS','DES5yr',annotate=True,compare=True,feature_analysis=True)
#df = lestrade(ECDFS,'ECDFS','DES5yr',save=True,overwrite=True,check=True,annotate=False,plot=True,feature_analysis=True)
#diffraction spike analysis

