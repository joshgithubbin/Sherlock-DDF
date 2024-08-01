#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:08:47 2024

@author: joshuaweston
"""
import matplotlib.pyplot as plt
import pandas as pd

def plot_zhist(field,z,labels="",savefig=False,savename="field"):
   
    plt.hist(z, label=labels, bins=20, edgecolor='black', alpha=0.7)
    
    plt.legend()
    plt.title(f'{field} Redshifts',fontweight='bold')
    plt.xlabel('Redshift')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    
    if savefig:
        
        fn = f"../Plots/{field}/{savename}_histogram.png"
        
        plt.savefig(fn,dpi=savefig)

    plt.show()
