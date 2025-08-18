#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

LESTRADE AUTOWIKI

build.py

v0.2.1

Function for building wiki from multiple catalogues and assembling the sidebar.

@author: joshuaweston

"""


def build_wiki(fp="../pages/ids.csv"):
    
    import csv
    
    from page import autowiki
    
    with open(fp, newline='') as f:
        reader = csv.reader(f)
        data = [row[0] for row in reader]
    
    data = list(dict.fromkeys(data))    
    
    #now for each doi, build a wiki page
    
    ct = [] #cleaned doi for url generation
    
    for doi in data:

        page = autowiki(doi)
        page.save()
        
        ct.append([page._doi_tidy,page._lrank,page._title])
        
    #build home
    
    hp = autowiki()
    hp.set_homepage()
    hp.save()
    
    #build footer
    
    ft = autowiki()
    ft.set_footer()
    ft.save()
    
    #build sidebar
    
    from page import sidebar
    
    sb = sidebar(ct)
    sb.save()
    
    return


def build_catalogues(fp="../pages/ids.csv"):
    
    import csv
    
    from download import catalogue
    
    with open(fp, newline='') as f:
        reader = csv.reader(f)
        data = [row[0] for row in reader]
    
    data = list(dict.fromkeys(data))    
    
    for doi in data:
        
        try:
    
            dataset = catalogue(doi)
            dataset.get_combined_catalogue()
            
            from plot import field
            field(dataset._catalogue_concat, doi,fp=f"../pages/{dataset._doi_tidy}/im/")
            from plot import plot_z
            plot_z(dataset._catalogue_concat,doi,'ZPH',fp=f"../pages/{dataset._doi_tidy}/im/")
            plot_z(dataset._catalogue_concat,doi,'ZSP',fp=f"../pages/{dataset._doi_tidy}/im/")
            from plot import plot_morph
            plot_morph(dataset._catalogue_concat,doi,fp=f"../pages/{dataset._doi_tidy}/im/")
            
        except Exception as e:
            
            print(e)
            continue
    
    return

