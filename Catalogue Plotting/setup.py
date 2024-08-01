#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:16:10 2024

@author: joshuaweston
"""
import os
from os.path import exists
import pandas as pd
from Code.DDFs import *

if not exists("Catalogues"):
    os.mkdir("Catalogues")
    os.mkdir("Catalogues/SubCatalogues")
    
if not exists("Plots"):
    os.mkdir("Plots")

    ddfs = load_ddfs(path='DDF_Coordinates.csv')[0]
    
    for i in ddfs:
        os.mkdir(f'Plots/{i}')

