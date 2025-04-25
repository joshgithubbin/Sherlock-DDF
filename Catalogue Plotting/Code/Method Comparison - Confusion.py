#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:07:15 2025

@author: joshuaweston
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

df = pd.read_csv('XMM-LSS_Sample_Final.csv')

df['DLR target'] = (df['DLR MATCH'] == 'YES').astype(int)
df['A-Value target'] = (df['AMAJOR MATCH'] == 'YES').astype(int)

cm = confusion_matrix(df['DLR target'], df['A-Value target'])

fig, ax = plt.subplots(figsize=(6, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
disp.plot(cmap='Reds', ax=ax)

ax.set_xlabel('A-Value Target', fontsize=12)
ax.set_ylabel('DLR Target', fontsize=12)

plt.title('DLR vs A-Value (All cases)')
plt.show()


df = df[df.truematch_exist != 'NO']

df['DLR target'] = (df['DLR MATCH'] == 'YES').astype(int)
df['A-Value target'] = (df['AMAJOR MATCH'] == 'YES').astype(int)

cm = confusion_matrix(df['DLR target'], df['A-Value target'])

fig, ax = plt.subplots(figsize=(6, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
disp.plot(cmap='Blues', ax=ax)

ax.set_xlabel('A-Value Target', fontsize=12)
ax.set_ylabel('DLR Target', fontsize=12)

plt.title('DLR vs A-Value (Complete Cases)')
plt.show()

df = df[df.Blended != 'Y']

df['DLR target'] = (df['DLR MATCH'] == 'YES').astype(int)
df['A-Value target'] = (df['AMAJOR MATCH'] == 'YES').astype(int)

cm = confusion_matrix(df['DLR target'], df['A-Value target'])

fig, ax = plt.subplots(figsize=(6, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
disp.plot(cmap='Greens', ax=ax)

ax.set_xlabel('A-Value Target', fontsize=12)
ax.set_ylabel('DLR Target', fontsize=12)

plt.title('DLR vs A-Value (Complete non-blended cases)')
plt.show()

df = df[(df['DLR Spikeflag'] != 1)&(df['A-Value Spikeflag'] != 1)]

df['DLR target'] = (df['DLR MATCH'] == 'YES').astype(int)
df['A-Value target'] = (df['AMAJOR MATCH'] == 'YES').astype(int)

cm = confusion_matrix(df['DLR target'], df['A-Value target'])

fig, ax = plt.subplots(figsize=(6, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
disp.plot(cmap='Purples', ax=ax)


ax.set_xlabel('A-Value Target', fontsize=12)
ax.set_ylabel('DLR Target', fontsize=12)

plt.title('DLR vs A-Value (Complete non-blended cases, probable spikes removed)')
plt.show()

df = df[df['Spike'].isna()]

# Create the target columns
df['DLR target'] = (df['DLR MATCH'] == 'YES').astype(int)
df['A-Value target'] = (df['AMAJOR MATCH'] == 'YES').astype(int)

# Compute confusion matrix
cm = confusion_matrix(df['DLR target'], df['A-Value target'])

# Plot confusion matrix
fig, ax = plt.subplots(figsize=(6, 6))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No Match', 'Match'])
disp.plot(cmap='Purples', ax=ax)

ax.set_xlabel('A-Value Target', fontsize=12)
ax.set_ylabel('DLR Target', fontsize=12)

plt.title('DLR vs A-Value (Complete non-blended cases, spikes removed)')
plt.show()