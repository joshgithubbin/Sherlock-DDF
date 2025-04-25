#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 15:01:28 2025

@author: joshuaweston
"""

import pandas as pd
import numpy as np

def update_dataframe_overwrite(df, file_path):
    """
    Updates the DataFrame: where df['SNID'] matches an item in the provided file,
    set df['DLR MATCH'] and df['AMAJOR MATCH'] to 'YES'.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    file_path (str): Path to the text file containing SNID values.

    Returns:
    pd.DataFrame: The updated DataFrame.
    """
    # Read the SNID values from the file
    with open(file_path, 'r') as file:
        snid_list = [int(line.strip().strip(',')) for line in file if line.strip()]  # Remove commas & empty lines

    # Convert to NumPy array (optional, but keeps behavior similar to before)
    snid_list = np.array(snid_list, dtype=np.int64)

    # Apply the update logic
    mask = df['SNID'].isin(snid_list)
    df.loc[mask, ['DLR MATCH', 'AMAJOR MATCH']] = 'YES'

    # Add 'Overwritten' column: 1 where SNID matches, 0 otherwise
    df['Overwritten'] = 0
    df.loc[mask, 'Overwritten'] = 1

    return df

def update_dataframe_blended(df, file_path):
    """
    Updates the DataFrame: where df['SNID'] matches an item in the provided file,
    set df['Blended'] to 1, otherwise 0.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    file_path (str): Path to the text file containing SNID values.

    Returns:
    pd.DataFrame: The updated DataFrame.
    """
    # Read the SNID values from the file
    with open(file_path, 'r') as file:
        snid_list = [int(line.strip().strip(',')) for line in file if line.strip()]  # Remove commas & empty lines

    # Convert to NumPy array
    snid_list = np.array(snid_list, dtype=np.int64)

    # Create 'Blended' column: 1 where SNID matches, 0 otherwise
    df['Blended'] = df['SNID'].isin(snid_list).astype(int)

    return df

def update_dataframe_spikes(df, DLR1, DLR2, AV1, AV2):
    """
    Updates the DataFrame by creating new spike columns based on matches in the provided files.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    DLR1 (str): Path to the text file containing SNID values for 'DLR Spike 1'.
    DLR2 (str): Path to the text file containing SNID values for 'DLR Spike 2'.
    AV1 (str): Path to the text file containing SNID values for 'AV Spike 1'.
    AV2 (str): Path to the text file containing SNID values for 'AV Spike 2'.

    Returns:
    pd.DataFrame: The updated DataFrame.
    """

    def load_snid_list(file_path):
        """Reads SNID values from a text file, ignoring empty lines and commas."""
        with open(file_path, 'r') as file:
            return set(int(line.strip().strip(',')) for line in file if line.strip())

    # Load SNID lists from files
    snid_dlr1 = load_snid_list(DLR1)
    snid_dlr2 = load_snid_list(DLR2)
    snid_av1 = load_snid_list(AV1)
    snid_av2 = load_snid_list(AV2)

    # Create new columns based on SNID membership in each list
    df['DLR Spike 1'] = df['SNID'].isin(snid_dlr1).astype(int)
    df['DLR Spike 2'] = df['SNID'].isin(snid_dlr2).astype(int)
    df['AV Spike 1'] = df['SNID'].isin(snid_av1).astype(int)
    df['AV Spike 2'] = df['SNID'].isin(snid_av2).astype(int)

    # Create combined columns for 'DLR Spike' and 'AV Spike'
    df['DLR Spike'] = ((df['DLR Spike 1'] == 1) | (df['DLR Spike 2'] == 1)).astype(int)
    df['A-Value Spike'] = ((df['AV Spike 1'] == 1) | (df['AV Spike 2'] == 1)).astype(int)

    return df