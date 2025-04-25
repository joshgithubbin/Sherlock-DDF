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
    
    "Hatfield-XMM": {
        "ZPH":"zphHBbest",
    },

    "XMM-SERVS": {
        "ZSP":"zsp", 
        "ZPH":"zph",
        "u":"umag1C",
        "g":"gmag1H",
        "r":"rmag1C",
        "i":"imag1C",
        "z":"zmag1C",
        "y":"ymag1H",
        },

    "SWIRE-REVISED": {
        "ZSP":"zsp", 
        "u":"umag2", 
        "g":"gmag2", 
        "r":"rmag2", 
        "i":"imag2", 
    },

    "VIRMOS": {
        "A":"Ai", 
        "B":"Bi", 
        "PA":"PAi",
        
        "axis_scale": 0.205/3600.

    },

    "HERSCHEL": {

    },

    "S-CANDELS": {

    },

    "MIGHTEE": {
        "A":"MajAxis", 
        "B":"MinAxis", 
        "PA":"PA",
    },

    "VIMOS": {
        "ZSP":"zsp", 
        "u":"umag", 
        "g":"gmag", 
        "r":"rmag", 
        "i":"imag", 
        "z":"zmag",
    },

    "HSC-SSP": {
        "ZPH":"z",
        "i":"imag", 
    },

    "XMM-LSS": {
    }
    
    }

import Lestrade_Catalogues as lcat

xmm = lcat.gen_cat(XMM_LSS, 'XMM-LSS')
    