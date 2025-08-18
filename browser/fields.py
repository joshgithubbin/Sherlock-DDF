"""
Created on Tue Jul  2 10:02:17 2024

@author: joshuaweston
"""

def load_ddfs(path='DDF_Coordinates.csv'):
    
    import pandas as pd
    from ast import literal_eval
    from astropy.coordinates import Angle
    
    DDFs = pd.read_csv(path)
    
    DDFs['RA-Centre'] = DDFs['RA-Centre'].apply(lambda x: literal_eval(x) if pd.notna(x) else x)
    DDFs['DEC-Centre'] = DDFs['DEC-Centre'].apply(lambda x: literal_eval(x) if pd.notna(x) else x)
    
    
 
    DDFs['RAdeg'] = DDFs['RA-Centre'].apply(lambda x:  Angle(f"{x[0]}h{x[1]}m{x[2]}s").degree)
    DDFs['DECdeg'] = DDFs['DEC-Centre'].apply(lambda x:  Angle(f"{x[0]}d{x[1]}m{x[2]}s",unit='deg').degree)
    
    ddf_dict = DDFs.set_index('Name').T.to_dict()
    
    
    return ddf_dict,DDFs