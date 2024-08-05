#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:08:47 2024

@author: joshuaweston
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_zhist(field,z,labels="",savefig=False,savename="field"):
   
    plt.hist(z, label=labels, bins=np.arange(0,7.5,0.05).tolist(), edgecolor='black', alpha=0.7)
    
    plt.legend()
    plt.title(f'{field} Redshifts',fontweight='bold')
    plt.xlabel('Redshift')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    
    if savefig:
        
        fn = f"../Plots/{field}/{savename}_histogram.png"
        
        plt.savefig(fn,dpi=savefig)

    plt.show()
