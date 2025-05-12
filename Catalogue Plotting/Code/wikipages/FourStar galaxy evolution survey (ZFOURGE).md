**Authors:** Spitler L.R., Quadri R.F., Labbe I., Glazebrook K.,, Persson S.E., Papovich C., Tran K.-V., Brammer G.B., Cowley M., Tomczak A.,, Nanayakkara T., Alcorn L., Allen R., Broussard A., van Dokkum P.,, Forrest B., van Houdt J., Kacprzak G.G., Kawinwanichakij L., Kelson D.D.,, Lee J., McCarthy P.J., Mehrtens N., Monson A., Murphy D., Rees G.,, Tilvi V., Whitaker K.E., <Astrophys. J., 830, 51-51 (2016)>, =2016ApJ...830...51S (SIMBAD/NED BibCode)

## Summary: FourStar galaxy evolution survey (ZFOURGE) 

The FourStar galaxy evolution survey (ZFOURGE) is a 45 night legacy program with the FourStar near-infrared camera on Magellan and one of the most sensitive surveys to date. ZFOURGE covers a total of 400arcmin^2^ in cosmic fields CDFS, COSMOS and UDS, overlapping the CANDELS fields.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/XMM-LSS/Plots/fieldcover.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/ECDFS/Plots/fieldcover.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zspec:** [0.06/6.2]?=-99 Spectroscopic redshift 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/XMM-LSS/Plots/zspec.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/ECDFS/Plots/zspec.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/COSMOS/Plots/zspec.png)
## Photometric Redshift 
 
**zpk:**  
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/XMM-LSS/Plots/zphot.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/ECDFS/Plots/zphot.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-830-51/Subcatalogues/COSMOS/Plots/zphot.png)
## Catalogue Schema

<details>
<summary>zf_cdfs.dat</summary>

| Bytes     | Format             | Units     | Label     | Explanations                               |
|:----------|:-------------------|:----------|:----------|:-------------------------------------------|
| 1- 5      | I5                 | ---       | Seq       | [1/30911] Running sequence number (id)     |
| 7- 14     | F8.3               | pix       | xpos      | Pixel X coordinates (scale:0.15"/pixel)    |
| 16- 23    | F8.3               | pix       | ypos      | Pixel Y coordinates (scale:0.15"/pixel)    |
| 25- 34    | F10.7              | deg       | RAdeg     | [52.9/53.3] Right ascension (J2000) (ra)   |
| 36- 46    | F11.7              | deg       | DEdeg     | [-28/-27.6] Declination (J2000) (dec)      |
| 48- 49    | I2                 | ---       | SE        | [0/19] Source Extractor flag               |
| 51- 57    | F7.1               | pix2      | isoArea   | [0/14799] Isophotal area above Source      |
| 59- 71    | F13.8              | 0.3631uJy | FKsap     | [0.02/9250.5]?=-99 (convolved) Ks-band     |
| 73- 84    | F12.8              | 0.3631uJy | e_FKsap   | [/0.3]?=-99 FKsap uncertainty (eap_Ksall)  |
| 86- 94    | F9.7               | ---       | apcorr    | [0.9/1.8] Aperture correction applied to   |
| 96- 105   | F10.7              | 0.3631uJy | KsR       | [0.4/84.3] Ratio between FKsap and FKsall  |
| 107- 119  | F13.8              | 0.3631uJy | FKsapD    | [0.06/8042]?=-99 Aperture flux measured    |
| 121- 132  | F12.8              | 0.3631uJy | e_FKsapD  | [0.02/0.2]?=-99 FKsapD uncertainty         |
| 134- 141  | F8.6               | ---       | apcorrD   | [1.7/1.8] Aperture correction applied to   |
| 143- 156  | F14.7              | 0.3631uJy | FKsD      | [0.1/14270]?=-99 Total (aperture           |
| 158- 169  | F12.8              | 0.3631uJy | e_FKsD    | [/0.3]?=-99 FKsD uncertainty               |
| 171- 184  | F14.8              | 0.3631uJy | FKsauto   | [0.05/22445] Ks-band flux within a         |
| 186- 191  | F6.3               | pix       | R50       | [0.7/36.1] Radius enclosing 50% of the     |
| 193- 198  | F6.3               | pix       | amaj      | [0.5/53.2] Major axis of a Kron-like       |
| 200- 205  | F6.3               | pix       | bmin      | [0.2/16.2] Minor axis of a Kron-like       |
| 207- 212  | F6.3               | ---       | Rad       | [0/68] Radius of a circularized Kron-like  |
| 214- 236  | F23.17             | 0.3631uJy | FKsall    | [0.1/23034]?=-99 Total (aperture           |
| 238- 259  | F22.18             | 0.3631uJy | e_FKsall  | [0.04/11]?=-99 FKsall uncertainty          |
| 261- 264  | F4.2               | ---       | w_FKsall  | [0/3.4] Weight corresponding to FKsall,    |
| 266- 288  | E23.20             | 0.3631uJy | FB        | [-0.4/728]?=-99 Aperture flux in HST/ACS   |
| 290- 312  | F23.18             | 0.3631uJy | e_FB      | [0/0.7]?=-99 FB uncertainty (e_B)          |
| 314- 317  | F4.2               | ---       | w_FB      | [0/3] Weight corresponding to FB, median   |
| 319- 341  | E23.20             | 0.3631uJy | FI        | [-0.4/3082]?=-99 Aperture flux in HST/ACS  |
| 343- 365  | F23.18             | 0.3631uJy | e_FI      | [0/1.3]?=-99 FI uncertainty (e_I)          |
| 367- 370  | F4.2               | ---       | w_FI      | [0/2.3] Weight corresponding to FI, median |
| 372- 394  | E23.20             | 0.3631uJy | FR        | [-0.5/5588]?=-99 Aperture flux in          |
| 396- 419  | F24.19             | 0.3631uJy | e_FR      | [0/279.4]?=-99 FR uncertainty (e_R)        |
| 421- 424  | F4.2               | ---       | w_FR      | [0/2.4] Weight corresponding to FR, median |
| 426- 448  | E23.20             | 0.3631uJy | FU        | [-1/1869]?=-99 Aperture flux in VLT/VIMOS  |
| 450- 472  | F23.19             | 0.3631uJy | e_FU      | [0/0.7]?=-99 FU uncertainty (e_U)          |
| 474- 477  | F4.2               | ---       | w_FU      | [0/2] Weight corresponding to FU, median   |
| 479- 501  | E23.20             | 0.3631uJy | FV        | [-0.4/1606]?=-99 Aperture flux in HST/ACS  |
| 503- 525  | F23.18             | 0.3631uJy | e_FV      | [0/0.7]?=-99 FV uncertainty (e_V)          |
| 527- 530  | F4.2               | ---       | w_FV      | [0/2.4] Weight corresponding to FV, median |
| 532- 554  | E23.20             | 0.3631uJy | FZ        | [-0.5/5701]?=-99 Aperture flux in HST/ACS  |
| 556- 578  | F23.18             | 0.3631uJy | e_FZ      | [0/1.6]?=-99 FZ uncertainty (e_Z)          |
| 580- 583  | F4.2               | ---       | w_FZ      | [0/2.5] Weight corresponding to FZ, median |
| 585- 612  | F28.20             | 0.3631uJy | FHs       | [-8.1/30415]?=-99 Aperture flux in         |
| 614- 635  | F22.17             | 0.3631uJy | e_FHs     | [0/15]?=-99 FHs uncertainty (e_Hs)         |
| 637- 640  | F4.2               | ---       | w_FHs     | [0/1.2] Weight corresponding to FHs,       |
| 642- 667  | F26.20             | 0.3631uJy | FHl       | [-7.1/27164]?=-99 Aperture flux in         |
| 669- 690  | F22.17             | 0.3631uJy | e_FHl     | [0/9]?=-99 FHl uncertainty (e_Hl)          |
| 692- 695  | F4.2               | ---       | w_FHl     | [0/1.2] Weight corresponding to FHl,       |
| 697- 718  | E22.20             | 0.3631uJy | FJ1       | [-2.7/19499]?=-99 Aperture flux in         |
| 720- 742  | F23.18             | 0.3631uJy | e_FJ1     | [0/5.1]?=-99 FJ1 uncertainty (e_J1)        |
| 744- 747  | F4.2               | ---       | w_FJ1     | [0/1.2] Weight corresponding to FJ1,       |
| 749- 770  | E22.20             | 0.3631uJy | FJ2       | [-6.5/16467]?=-99 Aperture flux in         |
| 772- 794  | F23.18             | 0.3631uJy | e_FJ2     | [0/9.1]?=-99 FJ2 uncertainty (e_J2)        |
| 796- 799  | F4.2               | ---       | w_FJ2     | [0/1.2] Weight corresponding to FJ2,       |
| 801- 822  | E22.19             | 0.3631uJy | FJ3       | [-3.5/25854]?=-99 Aperture flux in         |
| 824- 846  | F23.18             | 0.3631uJy | e_FJ3     | [0/9.5]?=-99 FJ3 uncertainty (e_J3)        |
| 848- 851  | F4.2               | ---       | w_FJ3     | [0/1.2] Weight corresponding to FJ3,       |
| 853- 874  | E22.20             | 0.3631uJy | FKs       | [-13.8/19204]?=-99 Aperture flux in        |
| 876- 897  | F22.17             | 0.3631uJy | e_FKs     | [0/8]?=-99 Uncertainty in FKs (e_Ks)       |
| 899- 902  | F4.2               | ---       | w_FKs     | [0/1.2] Weight corresponding to FKs,       |
| 904- 930  | F27.18             | 0.3631uJy | FKsHI     | [-64690/15404205]?=-99 Aperture flux in    |
| 932- 954  | F23.18             | 0.3631uJy | e_FKsHI   | [0/7.6]?=-99 FKsHI uncertainty (e_KsHI)    |
| 956- 960  | F5.2               | ---       | w_FKsHI   | [0/34.2] Weight corresponding to FKsHI,    |
| 962- 974  | E13.10             | 0.3631uJy | NB118     | [-7.7/17204]?=-99 Aperture flux in         |
| 118       | band,              | corrected | to        | total                                      |
| 976- 988  | F13.8              | 0.3631uJy | e_NB118   | [0/5.6]?=-99 NB118 uncertainty (e_NB118)   |
| 990- 993  | F4.2               | ---       | w_NB118   | [0/1.2] Weight corresponding to NB118,     |
| 995-1007  | E13.10             | 0.3631uJy | NB209     | [-18/17226]?=-99 Aperture flux in FourStar |
| 209       | band,              | corrected | to        | total                                      |
| 1009-1020 | F12.7              | 0.3631uJy | e_NB209   | [0/29]?=-99 NB209 uncertainty (e_NB209)    |
| 1022-1025 | F4.2               | ---       | w_NB209   | [0/1.2] Weight corresponding to NB209,     |
| 1027-1052 | F26.20             | 0.3631uJy | F098M     | [-0.2/27975]?=-99 Aperture flux in         |
| 3         | F098M              | filter,   | corrected | to total                                   |
| 1054-1076 | F23.18             | 0.3631uJy | e_F098M   | [0/1.2]?=-99 F098M uncertainty (e_F098M)   |
| 1078-1081 | F4.2               | ---       | w_F098M   | [0/1.7] Weight corresponding to F098M,     |
| 1083-1104 | E22.19             | 0.3631uJy | F105W     | [-0.7/35575]?=-99 Aperture flux in         |
| 3         | F105W              | band,     | corrected | to total                                   |
| 1106-1129 | F24.19             | 0.3631uJy | e_F105W   | [0/2.3]?=-99 F105W uncertainty (e_F105W)   |
| 1131-1135 | F5.2               | ---       | w_F105W   | [0/37] Weight corresponding to F105W,      |
| 1137-1158 | E22.20             | 0.3631uJy | F125W     | [-0.8/36252]?=-99 Aperture flux in         |
| 3         | F125W              | band,     | corrected | to total                                   |
| 1160-1183 | F24.19             | 0.3631uJy | e_F125W   | [0/1.5]?=-99 F125W uncertainty (e_F125W)   |
| 1185-1189 | F5.2               | ---       | w_F125W   | [0/21.6] Weight corresponding to F125W,    |
| 1191-1216 | F26.20             | 0.3631uJy | F140W     | [-2.4/43986]?=-99 Aperture flux in         |
| 3         | F140W              | band,     | corrected | to total                                   |
| 1218-1240 | F23.18             | 0.3631uJy | e_F140W   | [0/2.7]?=-99 F140W uncertainty (e_F140W)   |
| 1242-1245 | F4.2               | ---       | w_F140W   | [0/6.5] Weight corresponding to F140W,     |
| 1247-1261 | F15.9              | 0.3631uJy | F160W     | [-3.3/46862]?=-99 Aperture flux in         |
| 3         | F160W              | band,     | corrected | to total                                   |
| 1263-1275 | F13.8              | 0.3631uJy | e_F160W   | [0/1.9]?=-99 F160W uncertainty (e_F160W)   |
| 1277-1281 | F5.2               | ---       | w_F160W   | [0/33.4] Weight corresponding to F160W,    |
| 1283-1305 | E23.20             | 0.3631uJy | F814W     | [-0.5/14629]?=-99 Aperture flux in HST/ACS |
| 1307-1329 | F23.18             | 0.3631uJy | e_F814W   | [0/1.5]?=-99 F814W uncertainty (e_F814W)   |
| 1331-1334 | F4.2               | ---       | w_F814W   | [0/5.4] Weight corresponding to F814W,     |
| 1336-1358 | E23.20             | 0.3631uJy | IA484     | [-0.8/4503]?=-99 Aperture flux in          |
| 1360-1382 | F23.18             | 0.3631uJy | e_IA484   | [0/2.1]?=-99 IA484 uncertainty (e_IA484)   |
| 1384-1387 | F4.2               | ---       | w_IA484   | [0/1] Weight corresponding to IA484,       |
| 1389-1411 | E23.20             | 0.3631uJy | IA527     | [-19.6/5550]?=-99 Aperture flux in         |
| 1413-1435 | F23.18             | 0.3631uJy | e_IA527   | [0/2.2]?=-99 IA527 uncertainty (e_IA527)   |
| 1437-1440 | F4.2               | ---       | w_IA527   | [0/1] Weight corresponding to IA527,       |
| 1442-1467 | F26.20             | 0.3631uJy | IA574     | [-209/12437] Aperture flux in              |
| 1469-1491 | F23.18             | 0.3631uJy | e_IA574   | [0/5.4]?=-99 IA574 uncertainty (e_IA574)   |
| 1493-1496 | F4.2               | ---       | w_IA574   | [0/1] Weight corresponding to IA574,       |
| 1498-1520 | E23.20             | 0.3631uJy | IA598     | [-0.4/5362]?=-99 Aperture flux in          |
| 1522-1544 | F23.18             | 0.3631uJy | e_IA598   | [0/2.1]?=-99 IA598 uncertainty (e_IA598)   |
| 1546-1549 | F4.2               | ---       | w_IA598   | [0/1] Weight corresponding to IA598,       |
| 1551-1573 | E23.20             | 0.3631uJy | IA624     | [-0.6/5229]?=-99 Aperture flux in          |
| 1575-1597 | F23.18             | 0.3631uJy | e_IA624   | [0/2.4]?=-99 IA624 uncertainty (e_IA624)   |
| 1599-1602 | F4.2               | ---       | w_IA624   | [0/1] Weight corresponding to IA624,       |
| 1604-1626 | E23.20             | 0.3631uJy | IA651     | [-0.4/4338]?=-99 Aperture flux in          |
| 1628-1650 | F23.18             | 0.3631uJy | e_IA651   | [0/1.9]?=-99 IA651 uncertainty (e_IA651)   |
| 1652-1655 | F4.2               | ---       | w_IA651   | [0/1] Weight corresponding to IA651,       |
| 1657-1679 | E23.20             | 0.3631uJy | IA679     | [-2.1/3650]?=-99 Aperture flux in          |
| 1681-1703 | F23.18             | 0.3631uJy | e_IA679   | [0/2.4]?=-99 IA679 uncertainty (e_IA679)   |
| 1705-1708 | F4.2               | ---       | w_IA679   | [0/1] Weight corresponding to IA679,       |
| 1710-1732 | E23.20             | 0.3631uJy | IA738     | [-0.7/5147]?=-99 Aperture flux in          |
| 1734-1756 | F23.18             | 0.3631uJy | e_IA738   | [0/2.6]?=-99 IA638 uncertainty (e_IA638)   |
| 1758-1761 | F4.2               | ---       | w_IA738   | [0/1] Weight corresponding to IA738,       |
| 1763-1785 | E23.20             | 0.3631uJy | IA767     | [-2.3/6004]?=-99 Aperture flux in          |
| 767       | band,              | corrected | to        | total (f_IA767) (1)                        |
| 1787-1809 | F23.18             | 0.3631uJy | e_IA767   | [0/6.5]?=-99 IA767 uncertainty (e_IA767)   |
| 1811-1814 | F4.2               | ---       | w_IA767   | [0/1] Weight corresponding to IA767,       |
| 1816-1838 | E23.20             | 0.3631uJy | IA797     | [-3.4/5522]?=-99 Aperture flux in          |
| 797       | band,              | corrected | to        | total (f_IA797) (1)                        |
| 1840-1862 | F23.18             | 0.3631uJy | e_IA797   | [0/7.4]?=-99 IA797 uncertainty (e_IA797)   |
| 1864-1867 | F4.2               | ---       | w_IA797   | [0/1] Weight corresponding to IA797,       |
| 1869-1891 | E23.20             | 0.3631uJy | IA856     | [-4.2/7129]?=-99 Aperture flux in          |
| 856       | band,              | corrected | to        | total (f_IA856) (1)                        |
| 1893-1914 | F22.17             | 0.3631uJy | e_IA856   | [0/10]?=-99 IA856 uncertainty (e_IA856)    |
| 1916-1919 | F4.2               | ---       | w_IA856   | [0/1] Weight corresponding to IA856,       |
| 1921-1943 | E23.20             | 0.3631uJy | FVWFI     | [-0.6/13011]?=-99 Aperture flux in WFI     |
| 1945-1967 | F23.18             | 0.3631uJy | e_FVWFI   | [0/1.8]?=-99 FVWFI uncertainty (e_WFI_V)   |
| 1969-1972 | F4.2               | ---       | w_FVWFI   | [0/1.2] Weight corresponding to FVWFI,     |
| 1974-1996 | E23.20             | 0.3631uJy | FRcWFI    | [-0.5/12926]?=-99 Aperture flux in WFI     |
| 1998-2020 | F23.18             | 0.3631uJy | e_FRcWFI  | [0/1.7]?=-99 FRcWFI uncertainty (e_WFI_Rc) |
| 2022-2025 | F4.2               | ---       | w_FRcWFI  | [0/1.2] Weight corresponding to FRcWFI,    |
| 2027-2049 | E23.20             | 0.3631uJy | FU38      | [-6/11722]?=-99 Aperture flux in WFI U38   |
| 2051-2073 | F23.18             | 0.3631uJy | e_FU38    | [0/6]?=-99 FU38 uncertainty (e_WFI_U38)    |
| 2075-2078 | F4.2               | ---       | w_FU38    | [0/1.41] Weight corresponding to FU38,     |
| 2080-2106 | F27.20             | 0.3631uJy | FKT       | [-1.3/26277]?=-99 Aperture flux in TENIS   |
| 2108-2129 | F22.17             | 0.3631uJy | e_FKT     | [0/11.4]?=-99 FKT uncertainty (e_tenisK)   |
| 2131-2134 | F4.2               | ---       | w_FKT     | [0/1.3] Weight corresponding to FKT,       |
| 2136-2161 | F26.20             | 0.3631uJy | F3.6      | [-247/27619]?=-99 Aperture flux in         |
| 2163-2185 | F23.18             | 0.3631uJy | e_F3.6    | [-8/18.5]?=-99 F3.6 uncertainty            |
| 2187-2193 | F7.2               | ---       | w_F3.6    | [0/2.8]?=-99 Weight corresponding to F3.6, |
| 2195-2217 | E23.20             | 0.3631uJy | F4.5      | [-4627/27090]?=-99 Aperture flux in        |
| 2219-2242 | F24.18             | 0.3631uJy | e_F4.5    | [-4626.5/12.5]?=-99 F4.5 uncertainty       |
| 2244-2250 | F7.2               | ---       | w_F4.5    | [0/3]?=-99 Weight corresponding to F4.5,   |
| 2252-2273 | E22.20             | 0.3631uJy | F5.8      | [-6249/48340]?=-99 Aperture flux in        |
| 2275-2307 | F33.17             | 0.3631uJy | e_F5.8    | [-4441/]?=-99 F5.8 uncertainty (e_IRAC_58) |
| 2309-2315 | F7.2               | ---       | w_F5.8    | [0/2.3]?=-99 Weight corresponding to F5.8, |
| 2317-2339 | E23.20             | 0.3631uJy | F8.0      | [-1811/27616]?=-99 Aperture flux in        |
| 2341-2363 | F23.17             | 0.3631uJy | e_F8.0    | [-3756/30311]?=-99 F8.0 uncertainty        |
| 2365-2371 | F7.2               | ---       | w_F8.0    | [0/2.2]?=-99 Weight corresponding to F8.0, |
| 2373-2376 | F4.2               | ---       | wminOpt   | [0/1] Minimum weight of groundbased        |
| 2378-2381 | F4.2               | ---       | wmin1     | [0/5.4] Minimum weight of HST optical      |
| 2383-2386 | F4.2               | ---       | wminFS    | [0/5.4] Minimum weight of FourStar filters |
| 2388-2391 | F4.2               | ---       | wminNIR   | [0/3.4] Minimum weight of J, H & K filters |
| 2393-2396 | F4.2               | ---       | wmin2     | [0/1.3] Minimum weight of HST NIR filters  |
| 2398-2406 | F9.2               | ---       | wminIR    | [0/166680] Minimum weight of Spitzer/IRAC  |
| 2408-2411 | F4.2               | ---       | wmin      | [0/3.4] Minimum weight of all filters      |
| 2413      | I1                 | ---       | Star      | [0/1] 1=source is likely a star (G1)       |
| 2415      | I1                 | ---       | Nghb      | [0/1] 1=near a bright star (nearstar) (G2) |
| 2417      | I1                 | ---       | Use       | [0/1] 1=source selected (use)              |
| 2419-2430 | F12.6              | ---       | SNR       | [1/99198] Signal-to-noise                  |
| 2432      | A1                 | ---       | Use2      | [0/1] 1=source selected (use_nosnr) (2)    |
| 2434-2441 | F8.4               | ---       | zspec     | [0/5.8]?=-99 Spectroscopic redshift        |
| 4318      | 0.73               | 22.097    | -0.029    | -0.032                                     |
| 7693      | 0.73               | 22.151    | 0.019     | -0.014                                     |
| 6443      | 0.65               | 27.321    | -0.148    | -0.020                                     |
| 3749      | 0.81               | 25.932    | -0.181    | -0.037                                     |
| 5919      | 0.73               | 22.968    | -0.010    | -0.022                                     |
| 9036      | 0.73               | 21.378    | 0.041     | -0.011                                     |
| 5544      | 0.60               | 26.618    | -0.031    | -0.004                                     |
| 7020      | 0.50               | 26.588    | -0.051    | -0.004                                     |
| 0540      | 0.59               | 26.270    | -0.041    | -0.009                                     |
| 1448      | 0.62               | 26.558    | -0.043    | -0.006                                     |
| 2802      | 0.56               | 26.521    | -0.067    | -0.006                                     |
| 1538      | 0.46               | 26.851    | -0.083    | -0.003                                     |
| 118       | 1.1909             | 0.47      | 24.668    | 0.000    -0.006                            |
| 209       | 2.0990             | 0.45      | 24.786    | 0.000    -0.003                            |
| 9867      | 0.26               | 25.670    | 0.011     | -0.008                                     |
| 0545      | 0.24               | 26.259    | -0.002    | -0.007                                     |
| 2471      | 0.26               | 26.229    | 0.004     | -0.005                                     |
| 3924      | 0.27               | 26.421    | -0.027    | -0.004                                     |
| 5396      | 0.27               | 25.942    | -0.000    | -0.004                                     |
| 8057      | 0.22               | 25.931    | -0.004    | -0.011                                     |
| 484       | 0.4847             | 0.81      | 25.463    | -0.013    -0.024                           |
| 527       | 0.5259             | 0.87      | 25.639    | -0.059    -0.022                           |
| 574       | 0.5763             | 1.01      | 25.543    | -0.148    -0.019                           |
| 598       | 0.6007             | 0.69      | 25.962    | -0.040    -0.018                           |
| 624       | 0.6231             | 0.67      | 25.887    | 0.014    -0.017                            |
| 651       | 0.6498             | 0.67      | 26.072    | -0.062    -0.016                           |
| 679       | 0.6782             | 0.86      | 26.105    | -0.080    -0.015                           |
| 738       | 0.7359             | 0.83      | 26.003    | -0.003    -0.013                           |
| 767       | 0.7680             | 0.77      | 26.000    | -0.028    -0.012                           |
| 797       | 0.7966             | 0.74      | 25.986    | -0.022    -0.012                           |
| 856       | 0.8565             | 0.74      | 25.713    | -0.007    -0.010                           |
| 5376      | 0.96               | 23.999    | -0.076    | -0.021                                     |
| 6494      | 0.84               | 24.597    | -0.038    | -0.016                                     |
| 38        | 0.3686             | 0.98      | 21.587    | -0.291    -0.032                           |
| 1574      | 0.86               | 24.130    | 0.233     | -0.002                                     |
| 1748      | 0.45               | 31.419    | 0.022     | -0.003                                     |
| 36        | 3.5569             | 1.50      | 20.054    | -0.016     0.000                           |
| 45        | 4.5020             | 1.50      | 20.075    | 0.005     0.000                            |
| 58        | 5.7450             | 1.90      | 20.626    | 0.023     0.000                            |
| 80        | 7.9158             | 2.00      | 21.803    | 0.022     0.000                            |
| 11        | Subaru/Suprime-Cam | optical   | medium    | bands                                      |

**Note**: (convolved) aperture flux in filter [] within a 1.2" diameter
          circular aperture, corrected to total (Fap[]=F[]/KsR)
          CDFS passband parameters as in table 2:
       
        Filter   lam_C_    FWHM    Zeropoint    Offset   Galactic
                 (um)    (arcsec)  (AB mag)             extinction
                                     (G6)     (AB mag)   (AB mag)
       
        B        0.4318    0.73     22.097     -0.029    -0.032
        I        0.7693    0.73     22.151      0.019    -0.014
        R        0.6443    0.65     27.321     -0.148    -0.020
        U        0.3749    0.81     25.932     -0.181    -0.037
        V        0.5919    0.73     22.968     -0.010    -0.022
        Z        0.9036    0.73     21.378      0.041    -0.011
        H_s_     1.5544    0.60     26.618     -0.031    -0.004
        H_l_     1.7020    0.50     26.588     -0.051    -0.004
        J_1_     1.0540    0.59     26.270     -0.041    -0.009
        J_2_     1.1448    0.62     26.558     -0.043    -0.006
        J_3_     1.2802    0.56     26.521     -0.067    -0.006
        Ks       2.1538    0.46     26.851     -0.083    -0.003
        118      1.1909    0.47     24.668      0.000    -0.006
        209      2.0990    0.45     24.786      0.000    -0.003
        F098M    0.9867    0.26     25.670      0.011    -0.008
        F105W    1.0545    0.24     26.259     -0.002    -0.007
        F125W    1.2471    0.26     26.229      0.004    -0.005
        F140W    1.3924    0.27     26.421     -0.027    -0.004
        F160W    1.5396    0.27     25.942     -0.000    -0.004
        F814W    0.8057    0.22     25.931     -0.004    -0.011
        IA484    0.4847    0.81     25.463     -0.013    -0.024
        IA527    0.5259    0.87     25.639     -0.059    -0.022
        IA574    0.5763    1.01     25.543     -0.148    -0.019
        IA598    0.6007    0.69     25.962     -0.040    -0.018
        IA624    0.6231    0.67     25.887      0.014    -0.017
        IA651    0.6498    0.67     26.072     -0.062    -0.016
        IA679    0.6782    0.86     26.105     -0.080    -0.015
        IA738    0.7359    0.83     26.003     -0.003    -0.013
        IA767    0.7680    0.77     26.000     -0.028    -0.012
        IA797    0.7966    0.74     25.986     -0.022    -0.012
        IA856    0.8565    0.74     25.713     -0.007    -0.010
        WFI_V    0.5376    0.96     23.999     -0.076    -0.021
        WFI_Rc   0.6494    0.84     24.597     -0.038    -0.016
        WFI_U38  0.3686    0.98     21.587     -0.291    -0.032
        tenisK   2.1574    0.86     24.130      0.233    -0.002
        KsHI     2.1748    0.45     31.419      0.022    -0.003
        IRAC_36  3.5569    1.50     20.054     -0.016     0.000
        IRAC_45  4.5020    1.50     20.075      0.005     0.000
        IRAC_58  5.7450    1.90     20.626      0.023     0.000
        IRAC_80  7.9158    2.00     21.803      0.022     0.000
       
       The CDFS UV-to-optical filters include VLT/VIMOS/U, R-imaging
       (Nonino+ 2009ApJS..183..244N), HST/Advanced Camera for Surveys (ACS)/B,
       V, I, Z-imaging (Giavalisco+ 2004, II/261; Wuyts+ 2008, J/ApJ/682/985),
       ESO/MPG/WFI/U38, V, Rc-imaging (Erben+ 2005AN....326..432E;
       Hildebrandt+ 2006A&A...452.1121H), HST/WFC3/F098M, F105W, F125W, F140W,
       F160W and HST/ACSF606W, F814W-imaging (Grogin+ 2011ApJS..197...35G;
       Koekemoer+ 2011ApJS..197...36K; Windhorst+ 2011ApJS..193...27W;
       Brammer+ 2012ApJS..200...13B), 11 Subaru/Suprime-Cam optical medium bands
       (Cardamone+ 2010, J/ApJS/189/270) with seeing <1.1" (from a set of 18,
       including seeing >1.1" images) and CFHT/WIRCAM/K-band imaging
       (Hsieh+ 2012ApJS..203...23H).
       KsHI comes from a combined VLT/HAWKI and Magellan/FOURSTAR image.
Note (2): Same meaning as column "Use" (see Note (G3)) but without the
           snr>=5 criterion.

</details>

<details>
<summary>cdfszout.dat</summary>

| Bytes   | Format   | Units   | Label    | Explanations                                                                   |
|:--------|:---------|:--------|:---------|:-------------------------------------------------------------------------------|
| 1- 5    | I5       | ---     | Seq      | [1/30911] Running sequence number                                              |
| 7- 16   | F10.6    | ---     | zspec    | [0/6.2]?=-99 Spectroscopic redshift                                            |
| 18- 24  | F7.3     | ---     | za       | [0.005/10]?=-99 Photometric redshift derived                                   |
| 26- 32  | F7.3     | ---     | zml      | [0.005/10]?=-99 Weighted redshift derived                                      |
| 34- 45  | E12.7    | ---     | Chia     | [/3683]?=-99 Minimum {chi}^2^ derived without                                  |
| 47- 53  | F7.3     | ---     | zp       | [0.005/10]?=-99 Best-fit redshift after                                        |
| 55- 66  | E12.7    | ---     | Chip     | [/1e+08]?=-99 Minimum {chi}^2^ after applying                                  |
| 68- 74  | F7.3     | ---     | zm2      | [0.005/10]?=-99 Weighted redshift after                                        |
| 76- 82  | F7.3     | ---     | odds     | [0/1]?=-99 Parameter indicating presence of                                    |
| 1       | if       | no      | minimum) | 84- 90  F7.3  ---    l68    [0.005/9.9]?=-99 1 sigma lower confidence interval |
| 92- 98  | F7.3     | ---     | u68      | [0.01/10]?=-99 1 sigma upper confidence interval                               |
| 100-106 | F7.3     | ---     | l95      | [0.005/9.8]?=-99 2 sigma lower confidence interval                             |
| 108-114 | F7.3     | ---     | u95      | [0.01/10]?=-99 2 sigma upper confidence interval                               |
| 116-122 | F7.3     | ---     | l99      | [0.005/9.8]?=-99 3 sigma lower confidence interval                             |
| 124-130 | F7.3     | ---     | u99      | [0.01/10]?=-99 3 sigma upper confidence interval                               |
| 132-134 | I3       | ---     | nfilt    | [3/39]?=-99 Number of filters used in the fit                                  |
| 136-147 | E12.6    | ---     | Qual     | ? z quality parameter                                                          |
| 149-156 | F8.4     | ---     | zpk      | [/9.9]? Default derived photometric redshift                                   |
| 158-164 | F7.3     | ---     | pkProb   | [0/1]?=-99 Peak probability                                                    |
| 166-173 | F8.4     | ---     | zmc      | [0.005/10]?=-99 Randomly drawn redshift value                                  |
</details>

<details>
<summary>*zsp.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                             |
|:--------|:---------|:--------|:--------|:-----------------------------------------|
| 1- 5    | I5       | ---     | Seq     | [1/30911] Running sequence number        |
| 7- 14   | F8.4     | ---     | zsp     | [0/6.2]?=-99 Redshift spectroscopic (G5) |
</details>

<details>
<summary>cdfsfout.dat</summary>

| Bytes   | Format   | Units     | Label   | Explanations                                 |
|:--------|:---------|:----------|:--------|:---------------------------------------------|
| 1- 5    | I5       | ---       | Seq     | [1/30911] Running sequence number            |
| 7- 13   | F7.4     | ---       | z       | [0.01/9.9]? z_peak (or z_spec if available)  |
| 15- 19  | F5.2     | [yr-1]    | ltau    | [7/11]? Log of timescale {tau}               |
| 21- 27  | F7.4     | [-]       | Metal   | [0.02]? Metallicity (fixed to 0.020)         |
| 29- 33  | F5.2     | [yr]      | lage    | [7.5/10.1]? Log of age                       |
| 35- 39  | F5.2     | mag       | Av      | [0/4]? Dust reddening                        |
| 41- 46  | F6.2     | [Msun]    | lmass   | [2.5/14.4]? Log of mass                      |
| 48- 53  | F6.2     | [Msun/yr] | lsfr    | [-37.1/4.6]? Log of star formation rate      |
| 55- 60  | F6.2     | [yr-1]    | lssfr   | [-42.3/-7.4]? Log of specific star formation |
| 62- 66  | F5.2     | ---       | la2t    | [-3.5/3.1]? log(age/tau)                     |
| 68- 75  | E8.3     | ---       | chi2    | [0.01/386]? minimum {chi}^2^                 |
</details>

<details>
<summary>*sfr.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                 |
|:--------|:---------|:--------|:--------|:---------------------------------------------|
| 1- 5    | I5       | ---     | Seq     | [1/30911] Running sequence number            |
| 7- 13   | F7.4     | ---     | zPk     | [0.01/9.9]?=-1 Redshift peak                 |
| 15- 25  | E11.5    | mJy     | F24     | [-0.4/9.1]?=-99 Spitzer/MIPS 24um total flux |
| 27- 37  | E11.5    | mJy     | e_F24   | [/2]?=-99 F24 uncertainty                    |
| 39- 50  | E12.6    | Lsun    | LIR     | ?=-99 Total integrated IR luminosity         |
| 52- 62  | E11.6    | Lsun    | L2800   | [0.001/]?=-99 2800{AA} UV luminosity (1)     |
| 64- 73  | E10.4    | Msun/yr | SFR     | [-4287/50740]?=-99 UV-IR star formation rate |
| 75- 84  | E10.4    | Msun/yr | e_SFR   | ?=-99 Lower uncertainty on SFR               |
| 86- 95  | E10.4    | Msun/yr | E_SFR   | ?=-99 Upper uncertainty on SFR               |

**Note**: Rest-frame flux at 2800{AA} was computed using EAZY and a tophat
          filter of 200{AA} width (filter 274 in
          calibrations/FILTER_RES_DR34.latest).

</details>

<details>
<summary>*3dhst.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                      |
|:--------|:---------|:--------|:--------|:--------------------------------------------------|
| 1- 5    | I5       | ---     | Seq     | [1/30911] Running sequence number                 |
| 7- 11   | I5       | ---     | Name    | [1/50506]?=-99 3D-HST ID of nearest neighbour (1) |
| 13- 15  | I3       | ---     | Use     | [0/1]?=-99 3D-HST use flag (0=DON'T USE)          |
| 17- 19  | I3       | ---     | N       | [1/4]?=-99 Number of 3D-HST sources within        |

**Note**: 3D-HST sources were matched to ZFOURGE to within r<0.7".
          Only the ID of the nearest neighbour is displayed.
          3D-HST data is available at http://3dhst.research.yale.edu/;
          see also Skelton+, 2014, J/ApJS/214/24

</details>

<details>
<summary>*agn.dat</summary>

| Bytes   | Format          | Units                             | Label            | Explanations                                                       |
|:--------|:----------------|:----------------------------------|:-----------------|:-------------------------------------------------------------------|
| 1- 5    | I5              | ---                               | Seq              | [1/30911] Running sequence number                                  |
| 7       | I1              | ---                               | irAGN            | [0/1] Infrared AGN? (1=positive detection,                         |
| 9- 10   | I2              | ---                               | radAGN           | [0/1]?=-1 Radio AGN? (1=positive detection,                        |
| 12- 13  | I2              | ---                               | xAGN             | [0/1]?=-1 X-ray AGN? (1=positive detection,                        |
| 0       | z>1.8:          | [8.0]-[24]>2.9x([4.5]-[8.0])+2.8, | [8.0]-[24]>0.5   | Note (2): Radio AGN are selected using the Rees et al. (2015)      |
| 0       | The             | minimum                           | root-mean-square | (RMS) sensitivity for the 1.4GHz data in                           |
| 10      | and             | 100uJy/beam,                      | respectively.    | Note (3): X-ray AGN are selected using the Szokoly et al. (2004)   |
| 2       | L_x_>=1e42erg/s | &                                 | HR<=-0.2         | The on-axis limiting X-ray flux in the soft and hard bands for the |
| 18      | and             | 5.5e-17erg/cm^2^/s,               | 1.9e-16          | and 7.3e-16erg/cm^2^/s, and 6.0e-16 and 3.0e-15erg/cm^2^/s,        |

**Note**: Infrared AGN are selected using the colour-colour classifications of
          Messias et al. (2012):
          z<1.8: Ks-[4.5]>0, [4.5]-[8.0]>0
          z>1.8: [8.0]-[24]>2.9x([4.5]-[8.0])+2.8, [8.0]-[24]>0.5
Note (2): Radio AGN are selected using the Rees et al. (2015)
          Radio AGN activity index:
          SFR_Radio_/SFR_IR+UV_>3.0
          The minimum root-mean-square (RMS) sensitivity for the 1.4GHz data in
          CDFS, COSMOS and UDS fields are 6, 10 and 100uJy/beam, respectively.
Note (3): X-ray AGN are selected using the Szokoly et al. (2004)
          classification:
          L_x_>=1e41erg/s & HR>-0.2
          L_x_>=1e42erg/s & HR<=-0.2
          The on-axis limiting X-ray flux in the soft and hard bands for the
          CDFS, COSMOS and UDS fields are 9.1e-18 and 5.5e-17erg/cm^2^/s,
          1.9e-16 and 7.3e-16erg/cm^2^/s, and 6.0e-16 and 3.0e-15erg/cm^2^/s,
          respectively.

</details>

<details>
<summary>*rest.dat</summary>

| Bytes   | Format    | Units         | Label   | Explanations                                               |
|:--------|:----------|:--------------|:--------|:-----------------------------------------------------------|
| 1- 5    | I5        | ---           | Seq     | [1/30911] Running sequence number                          |
| 7- 18   | E12.6     | uJy           | Fu      | [-36/82505] Computed flux in the rest frame                |
| 20- 30  | E11.6     | uJy           | e_Fu    | [0/1046]? Fu uncertainty (1)                               |
| 32- 43  | E12.6     | uJy           | Fg      | [-36/162538] Computed flux in the rest frame               |
| 45- 55  | E11.6     | uJy           | e_Fg    | [0/1799] Fg uncertainty (1)                                |
| 57- 68  | E12.6     | uJy           | Fr      | [-36/16490] Computed flux in the rest frame                |
| 70- 80  | E11.6     | uJy           | e_Fr    | [0/2773]? Fr uncertainty (1)                               |
| 82- 93  | E12.6     | uJy           | Fi      | [-36/19332] Computed flux in the rest frame                |
| 95-105  | E11.6     | uJy           | e_Fi    | [0/]? Fi uncertainty (1)                                   |
| 107-118 | E12.6     | uJy           | Fz      | [-36/26394] Computed flux in the rest frame                |
| 120-130 | E11.6     | uJy           | e_Fz    | [0/492]? Fz uncertainty (1)                                |
| 132-143 | E12.6     | uJy           | FU      | [-36/83749] Computed flux in the rest frame                |
| 145-155 | E11.6     | uJy           | e_FU    | [0/1110]? FU uncertainty (1)                               |
| 157-168 | E12.6     | uJy           | FB      | [-36/81872] Computed flux in the rest frame                |
| 170-180 | E11.6     | uJy           | e_FB    | [0/]? FB uncertainty (1)                                   |
| 182-193 | E12.6     | uJy           | FV      | [-36/136753] Computed flux in the rest frame               |
| 195-205 | E11.6     | uJy           | e_FV    | [0/512]? FV uncertainty (1)                                |
| 207-218 | E12.6     | uJy           | FJ      | [-36/38317] Computed flux in the rest frame                |
| 220-230 | E11.6     | uJy           | e_FJ    | [0/477]? FJ uncertainty (1)                                |
| 232-243 | E12.6     | uJy           | FH      | [-36/26626] Computed flux in the rest frame                |
| 245-255 | E11.6     | uJy           | e_FH    | [0/170]? FH uncertainty (1)                                |
| 257-268 | E12.6     | uJy           | FK      | [-36/21396] Computed flux in the rest frame                |
| 270-280 | E11.6     | uJy           | e_FK    | [0/]? FK uncertainty (1)                                   |
| 282-293 | E12.6     | uJy           | Fuv13   | [-36/59450] Computed flux in the rest frame                |
| 295-305 | E11.6     | uJy           | e_Fuv13 | [0/]? Fuv13 uncertainty (1)                                |
| 307-318 | E12.6     | uJy           | Fuv15   | [-36/61064] Computed flux in the rest frame                |
| 320-330 | E11.6     | uJy           | e_Fuv15 | [0/624]? Fuv15 uncertainty (1)                             |
| 332-343 | E12.6     | uJy           | Fuv19   | [-36/55309] Computed flux in the rest frame                |
| 345-355 | E11.6     | uJy           | e_Fuv19 | [0/550]? Fuv19 uncertainty (1)                             |
| 357-368 | E12.6     | uJy           | Fuv22   | [-36/49546] Computed flux in the rest frame                |
| 370-380 | E11.6     | uJy           | e_Fuv22 | [0/522]? Fuv22 uncertainty (1)                             |
| 382-393 | E12.6     | uJy           | Fuv28   | [-36/44349] Computed flux in the rest frame                |
| 395-405 | E11.6     | uJy           | e_Fuv28 | [0/]? Fuv28 uncertainty (1)                                |
| 29      | *3*10**18 | /lambda_c**2, | where   | lambda_c is the central wavelength of the filter bandpass. |

**Note**: These catalogs are in units of uJy.
          To convert back to catalog fluxes
          (AB flux densities with zeropoint 25), divide by 10**((23.9-25)/2.5).
          To convert to solar luminosities:
          1. Convert to ergs/cm^2^/s/{AA} --
             flux density [uJy] *10**-29 *3*10**18 /lambda_c**2,
             where lambda_c is the central wavelength of the filter bandpass.
          2. Convert from flux density to flux -- multiply by lambda_c

</details>

<details>
<summary>*rad.dat</summary>

| Bytes   | Format   | Units    | Label     | Explanations                           |
|:--------|:---------|:---------|:----------|:---------------------------------------|
| 1- 5    | I5       | ---      | Seq       | [1/30911] Running sequence number      |
| 7- 13   | F7.1     | uJy/beam | F1.4GHz   | [0/53640]?=-99 Peak or integrated      |
| 15- 19  | F5.1     | uJy/beam | e_F1.4GHz | [6/147]?=-99 F1.4GHz uncertainty       |
| 21- 27  | E7.3     | W/Hz     | L1.4GHz   | ?=-99 Rest-frame 1.4GHz luminosity (2) |

**Note**: For M13, F1.4GHz includes a combination of peak and integrated fluxes,
          with the final value chosen based on the author's recommendation.
          For the other fields, the integrated flux is used.
Note (2): The rest-frame radio luminosity is calculated using:
          L1.4GHz=(4*pi*ld**2)*F1.4GHz*(1+z_peak)**({alpha}-2)
          where ld is the luminosity distance (cm) and {alpha} is the radio
          spectral index (fixed to {alpha}=-0.3).

</details>

<details>
<summary>*vdw.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                                 |
|:--------|:---------|:--------|:----------|:-------------------------------------------------------------|
| 1- 5    | I5       | ---     | Seq       | [1/30911] Running sequence number                            |
| 7- 11   | F5.2     | ---     | wmin      | [0/33.4] wmin>0 for HST coverage                             |
| 13- 19  | F7.2     | arcsec  | Sep       | [0/0.7]?=-999 Separation of the ZFOURGE object               |
| 14      | (1)      | 21      | A1        | ---   f_Sep      Number of matches flag (0=single match) (2) |
| 23- 27  | I5       | ---     | [SWM2014] | [/50506]?=-999 Number in vdW14 (3)                           |
| 29- 39  | F11.6    | deg     | RAdeg     | ?=-999 vdW14 right ascension (J2000)                         |
| 41- 51  | F11.6    | deg     | DEdeg     | ?=-999 vdW14 declination (J2000)                             |
| 53- 59  | F7.2     | arcsec  | Reff      | [0.02/24]?=-999 vdW14 effective radius                       |
| 61- 69  | F9.2     | arcsec  | e_Reff    | [0/348635]?=-999 Reff uncertainty                            |
| 71- 77  | F7.2     | ---     | n         | [0.2/8]?=-999 vdW14 sersic index                             |
| 79- 86  | F8.2     | ---     | e_n       | [0/50193]?=-999 n uncertainty                                |
| 88- 94  | F7.2     | ---     | q         | [0/1]?=-999 vdW14 axis ratio                                 |
| 96-103  | F8.2     | ---     | e_q       | [0/25330]?=-999 q uncertainty                                |
| 105-111 | F7.2     | mag     | mag       | [9/30]?=-999 vdW14 HST/WFC3 F160W AB magnitude               |
| 113-120 | F8.2     | mag     | e_mag     | [0/59353]?=-999 mag uncertainty                              |
| 122-128 | F7.2     | deg     | PA        | [-90/90]?=-999 vdW14 position angle                          |
| 130-139 | F10.2    | deg     | e_PA      | ?=-999 PA uncertainty                                        |
| 141-150 | F10.2    | ---     | S/N       | ?=-999 vdW14 object S/N                                      |
| 152-155 | I4       | ---     | Fit       | [/3]?=-999 vdW14 goodness of fit flag                        |
| 0       | =        | single  | matches,  | 1 = multiple matches,                                        |
| 2       | =        | no      | matches   | Note (3): Objects are <[SWM2014] GOODS-S NNNNN> or           |

**Note**: Sources from X_F160W_galfit_v4.0.cat (vdW14) were matched to ZFOURGE
          to within r<0.7". If an object has multiple or no matches,
          the 'Sep' column has a value of -999.
Note (2): Flags the number of van der Wel+ 2014ApJ...788...28V catalog matches
          to a single ZFOURGE object as follows:
      0 = single matches,
      1 = multiple matches,
      2 = no matches
Note (3): Objects are <[SWM2014] GOODS-S NNNNN> or
          <[SWM2014] COSMOS NNNNN> or <[SWM2014] UDS NNNNN> in Simbad.

</details>

<details>
<summary>cdfsx.dat</summary>

| Bytes   | Format   | Units    | Label   | Explanations                                   |
|:--------|:---------|:---------|:--------|:-----------------------------------------------|
| 1- 5    | I5       | ---      | Seq     | [1/30911] Running sequence number              |
| 7- 14   | E8.2     | 10-3W/m2 | Fx      | ?=-99 Full band X-ray flux in erg/cm^2^/s (1)  |
| 16- 23  | E8.3     | 10-7W    | Lx      | ?=-99 Rest-frame X-ray luminosity in erg/s (2) |
| 25- 30  | F6.2     | ---      | HR      | [-0.9/0.9]?=-99 Hardness ratio (3)             |
| 4       | For      | sources  | from    | X11, the intrinsic flux is derived from counts |
| 09      | and      | U08      | it      | is derived from                                |
| 09      | and      | U08      | to      | align with                                     |
| 11      | by       | assuming | a       | power-law model with                           |
| 4       | (i.e.    | E09      | and     | U08 fluxes are multiplied                      |
| 2-8     | or       | 2-10keV) | and     | soft (0.5-2keV) bands, respectively.           |

**Note**: In the absence of a full-band flux value, Fx is calculated
          considering a counts-to-flux conversion factor with
          photon index {Gamma}=1.4
          For sources from X11, the intrinsic flux is derived from counts
          in the 0.5-8keV full band, while from E09 and U08 it is derived from
          the sum of the counts in the relevant bands over 0.5-10keV.
          Flux values were adjusted for sources from E09 and U08 to align with
          the full bandpass values of X11 by assuming a power-law model with
          photon index {Gamma}=1.4 (i.e. E09 and U08 fluxes are multiplied
          by a factor of 0.95).
Note (2): The rest-frame X-ray luminosity is calculated using:
          Lx=(4*pi*ld**2)*f_x*(1+z_peak)**({Gamma}-2)
          where ld is the luminosity distance (cm) and {Gamma} is the photon
          index (fixed to {Gamma}=1.4).
Note (3): The hardness ratio (HR) is calculated using: HR = (H-S)/(H+S)
          where H and S are the count rates in the hard (2-8 or 2-10keV) and
          soft (0.5-2keV) bands, respectively.

</details>

<details>
<summary>cdfs_her.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                 |
|:--------|:---------|:--------|:--------|:---------------------------------------------|
| 1- 5    | I5       | ---     | Seq     | [1/30911] Running sequence number            |
| 7- 13   | F7.4     | ---     | z       | [0.01/9.7]?=-1 Photometric redshift          |
| 15- 25  | E11.5    | mJy     | F24     | [-0.3/8.1]?=-99 Spitzer/MIPS 24um total flux |
| 27- 37  | E11.5    | mJy     | e_F24   | [0/0.3]?=-99 F24 uncertainty                 |
| 39- 49  | E11.5    | mJy     | F100    | [-8.1/196.1]?=-99 Herschel/PACS 100um flux   |
| 51- 61  | E11.5    | mJy     | e_F100  | [0/1.2]?=-99 F100 uncertainty                |
| 63- 73  | E11.5    | mJy     | F160    | [-7.2/224.8]?=-99 Herschel/PACS 160um flux   |
| 75- 85  | E11.5    | mJy     | e_F160  | [0/3.6]?=-99 F160 uncertainty                |
| 87- 98  | E12.6    | Lsun    | LIR     | ?=-99 Total integrated IR luminosity         |
| 100-110 | E11.6    | Lsun    | LUV     | ?=-99 Total UV luminosity                    |
| 112-122 | E11.5    | ---     | SFR     | Star formation rate (equation 6) (1)         |

**Note**: We use the conversion from Bell+ (2005ApJ...625...23B) to calculate
          SFRs from our data, scaled to a Chabrier (2003PASP..115..763C) IMF
          Equation (6):
          SFR[M_{sun}_/yr]=1.09x10^-10^(L_IR_+2.2L_UV_).

</details>

<details>
<summary>zf_cosmos.dat</summary>

| Bytes     | Format             | Units     | Label            | Explanations                                         |
|:----------|:-------------------|:----------|:-----------------|:-----------------------------------------------------|
| 1- 5      | I5                 | ---       | Seq              | [1/20786] Running sequence number (id)               |
| 7- 14     | F8.3               | pix       | xpos             | Pixel X coordinates (scale:0.15"/pixel)              |
| 16- 23    | F8.3               | pix       | ypos             | Pixel Y coordinates (scale:0.15"/pixel)              |
| 25- 35    | F11.7              | deg       | RAdeg            | Right ascension (J2000)                              |
| 37- 45    | F9.7               | deg       | DEdeg            | Declination (J2000)                                  |
| 47- 48    | I2                 | ---       | SE               | [0/19] Source Extractor flag                         |
| 50- 56    | F7.1               | pix2      | IsoArea          | [1/26678] Isophotal area above Source                |
| 58- 71    | F14.8              | 0.3631uJy | FKsap            | [0.07/12352]?=-99 (convolved) Ks-band                |
| 73- 84    | F12.8              | 0.3631uJy | e_FKsap          | [0.07/0.3]?=-99 FKsap uncertainty                    |
| 86- 94    | F9.7               | ---       | apcorr           | [0.9/1.7] Aperture correction applied to             |
| 96- 106   | F11.7              | ---       | KsR              | [0.5/309] Ratio between FKsap and                    |
| 108- 120  | F13.7              | 0.3631uJy | FKsapD           | [0.1/10933]?=-99 Aperture flux measured              |
| 122- 133  | F12.8              | 0.3631uJy | e_FKsapD         | [0.06/0.3]?=-99 FKsapD uncertainty                   |
| 135- 142  | F8.6               | ---       | apcorrD          | [1.6/1.7] Aperture correction applied to             |
| 144- 156  | F13.7              | 0.3631uJy | FKsD             | [0.2/18001]?=-99 Total (aperture                     |
| 158- 168  | F11.7              | 0.3631uJy | e_FKsD           | [0.1/0.4]?=-99 FKsD uncertainty                      |
| 170- 182  | F13.7              | 0.3631uJy | FKsauto          | [0.06/47726] Ks-band flux within a                   |
| 184- 190  | F7.3               | pix       | R50              | [0.7/139] Radius enclosing 50% of the                |
| 192- 198  | F7.3               | pix       | amaj             | [0.5/231] Major axis of a Kron-like                  |
| 200- 205  | F6.3               | pix       | bmin             | [0.2/19.5] Minor axis of a Kron-like                 |
| 207- 212  | F6.3               | ---       | Rad              | [0/76.5] Radius of a circularized                    |
| 214- 226  | F13.7              | 0.3631uJy | FKsall           | [0.2/48199]?=-99 Total (aperture                     |
| 228- 238  | F11.7              | 0.3631uJy | e_FKsall         | [0.1/9.1]?=-99 FKsall uncertainty                    |
| 240- 243  | F4.2               | ---       | w_FKsall         | [0/1.4] Weight corresponding to FKsall,              |
| 245- 267  | E23.20             | 0.3631uJy | FB               | [-106.3/1687] Aperture flux in                       |
| 269- 288  | F20.18             | 0.3631uJy | e_FB             | [0.006/3.5] FB uncertainty (e_B)                     |
| 290- 292  | F3.1               | ---       | w_FB             | [1] Weight corresponding to FB, median               |
| 294- 316  | E23.20             | 0.3631uJy | Fg               | [-8/3738] Aperture flux in CFHT g-band,              |
| 318- 337  | F20.18             | 0.3631uJy | e_Fg             | [0.008/4.7] Fg uncertainty (e_G)                     |
| 339- 341  | F3.1               | ---       | w_Fg             | [1] Weight corresponding to Fg, median               |
| 343- 364  | E22.19             | 0.3631uJy | Fi               | [-13.4/7044] Aperture flux in CFHT                   |
| 366- 385  | F20.18             | 0.3631uJy | e_Fi             | [0.009/5.5] Fi uncertainty (e_I)                     |
| 387- 389  | F3.1               | ---       | w_Fi             | [1] Weight corresponding to Fi, median               |
| 391- 413  | E23.20             | 0.3631uJy | IA427            | [-134.1/7821] Aperture flux in                       |
| 427       | band,              | corrected | to               | total (f_IA427) (1)                                  |
| 415- 435  | F21.18             | 0.3631uJy | e_IA427          | [0.02/13] IA427 uncertainty (e_IA427)                |
| 437- 439  | F3.1               | ---       | w_IA427          | [1] Weight corresponding to FI, median               |
| 441- 462  | E22.20             | 0.3631uJy | IA484            | [-134/4489] Aperture flux in                         |
| 484       | band,              | corrected | to               | total (f_IA484) (1)                                  |
| 464- 484  | F21.18             | 0.3631uJy | e_IA484          | [0.02/12] IA484 uncertainty (e_IA484)                |
| 486- 488  | F3.1               | ---       | w_IA484          | [1] Weight corresponding to IA484,                   |
| 490- 512  | E23.20             | 0.3631uJy | IA505            | [-521/5478] Aperture flux in                         |
| 505       | band,              | corrected | to               | total (f_IA505) (1)                                  |
| 514- 534  | F21.18             | 0.3631uJy | e_IA505          | [0.02/14] IA505 uncertainty (e_IA505)                |
| 536- 538  | F3.1               | ---       | w_IA505          | [1] Weight corresponding to IA505,                   |
| 540- 562  | E23.20             | 0.3631uJy | IA527            | [-269/5411] Aperture flux in                         |
| 527       | band,              | corrected | to               | total (f_IA527) (1)                                  |
| 564- 584  | F21.18             | 0.3631uJy | e_IA527          | [0.01/11] IA527 uncertainty (e_IA527)                |
| 586- 588  | F3.1               | ---       | w_IA527          | [1] Weight corresponding to IA527,                   |
| 590- 612  | E23.20             | 0.3631uJy | IA624            | [-508/4105] Aperture flux in                         |
| 624       | band,              | corrected | to               | total (f_IA624) (1)                                  |
| 614- 634  | F21.18             | 0.3631uJy | e_IA624          | [0.01/12] IA624 uncertainty (e_IA624)                |
| 636- 638  | F3.1               | ---       | w_IA624          | [1] Weight corresponding to IA624,                   |
| 640- 661  | E22.20             | 0.3631uJy | IA709            | [-657/3754] Aperture flux in                         |
| 709       | band,              | corrected | to               | total (f_IA709) (1)                                  |
| 663- 683  | F21.18             | 0.3631uJy | e_IA709          | [0.02/14] IA709 uncertainty (e_IA709)                |
| 685- 687  | F3.1               | ---       | w_IA709          | [1] Weight corresponding to IA709,                   |
| 689- 713  | F25.20             | 0.3631uJy | IA738            | [-714/5741] Aperture flux in                         |
| 738       | band,              | corrected | to               | total (f_IA738) (1)                                  |
| 715- 735  | F21.18             | 0.3631uJy | e_IA738          | [0.02/17] IA738 uncertainty (e_IA738)                |
| 737- 739  | F3.1               | ---       | w_IA738          | [1] Weight corresponding to IA738,                   |
| 741- 765  | F25.20             | 0.3631uJy | Fr               | [-11/5958] Aperture flux in CFHT r-band,             |
| 767- 786  | F20.18             | 0.3631uJy | e_Fr             | [0.008/5] Fr uncertainty (e_R)                       |
| 788- 790  | F3.1               | ---       | w_Fr             | [1] Weight corresponding to Fr, median               |
| 792- 814  | E23.20             | 0.3631uJy | Fu               | [-16/3387] Aperture flux in CFHT u-band,             |
| 816- 835  | F20.18             | 0.3631uJy | e_Fu             | [0.01/7] Fu uncertainty (e_U)                        |
| 837- 839  | F3.1               | ---       | w_Fu             | [1] Weight corresponding to Fu, median               |
| 841- 866  | F26.20             | 0.3631uJy | FV               | [-179/3909] Aperture flux in                         |
| 868- 887  | F20.18             | 0.3631uJy | e_FV             | [0.01/6] FV uncertainty (e_V)                        |
| 889- 891  | F3.1               | ---       | w_FV             | [1] Weight corresponding to FV, median               |
| 893- 917  | F25.20             | 0.3631uJy | FRp              | [-181/3572] Aperture flux in                         |
| 919- 938  | F20.18             | 0.3631uJy | e_FRp            | [0.009/5.4] Rp uncertainty (e_Rp)                    |
| 940- 942  | F3.1               | ---       | w_FRp            | [1] Weight corresponding to FRp, median              |
| 944- 965  | E22.20             | 0.3631uJy | Fz               | [-4.1/12315] Aperture flux in CFHT                   |
| 967- 987  | F21.18             | 0.3631uJy | e_Fz             | [0.02/16] Fz uncertainty (e_Z)                       |
| 989- 991  | F3.1               | ---       | w_Fz             | [1] Weight corresponding to Fz, median               |
| 993-1016  | F24.19             | 0.3631uJy | FZp              | [-393/2186] Aperture flux in                         |
| 1018-1038 | F21.18             | 0.3631uJy | e_FZp            | [0.03/21] FZp uncertainty (e_Zp)                     |
| 1040-1042 | F3.1               | ---       | w_FZp            | [1] Weight corresponding to FZp, median              |
| 1044-1069 | F26.20             | 0.3631uJy | FHl              | [-8/48610]?=-99 Aperture flux in                     |
| 1071-1091 | F21.17             | 0.3631uJy | e_FHl            | [0.1/15.4]?=-99 FHl uncertainty (e_Hl)               |
| 1093-1096 | F4.2               | ---       | w_FHl            | [0/1.3] Weight corresponding to FHl,                 |
| 1098-1123 | F26.20             | 0.3631uJy | FHs              | [-33/41119]?=-99 Aperture flux in                    |
| 1125-1145 | F21.17             | 0.3631uJy | e_FHs            | [0.1/26]?=-99 FHs uncertainty (e_Hs)                 |
| 1147-1150 | F4.2               | ---       | w_FHs            | [0/1.3] Weight corresponding to FHs,                 |
| 1152-1176 | F25.19             | 0.3631uJy | FJ1              | [-33/25077]?=-99 Aperture flux in                    |
| 1178-1199 | F22.18             | 0.3631uJy | e_FJ1            | [0.04/22]?=-99 FJ1 uncertainty (e_J1)                |
| 1201-1204 | F4.2               | ---       | w_FJ1            | [0/1.4] Weight corresponding to FJ1,                 |
| 1206-1227 | E22.20             | 0.3631uJy | FJ2              | [-13/23328]?=-99  Aperture flux in                   |
| 1229-1250 | F22.18             | 0.3631uJy | e_FJ2            | [0.04/23]?=-99 FJ2 uncertainty (e_J2)                |
| 1252-1255 | F4.2               | ---       | w_FJ2            | [0/1.4] Weight corresponding to FJ2,                 |
| 1257-1282 | F26.20             | 0.3631uJy | FJ3              | [-7/24545]?=-99 Aperture flux in                     |
| 1284-1304 | F21.17             | 0.3631uJy | e_FJ3            | [0.06/9.1]?=-99 FJ3 uncertainty (e_J3)               |
| 1306-1309 | F4.2               | ---       | w_FJ3            | [0/1.4] Weight corresponding to FJ3,                 |
| 1311-1335 | F25.19             | 0.3631uJy | FKs              | [-22/31171]?=-99 Aperture flux in                    |
| 1337-1357 | F21.17             | 0.3631uJy | e_FKs            | [0.09/49]?=-99 FKs uncertainty (e_Ks)                |
| 1359-1362 | F4.2               | ---       | w_FKs            | [0/1.4] Weight corresponding to FKs,                 |
| 1364-1379 | F16.10             | 0.3631uJy | NB118            | [-13/48391]?=-99 Aperture flux in                    |
| 1381-1391 | F11.7              | 0.3631uJy | e_NB118          | [0.1/8]?=-99 NB118 uncertainty (e_NB118)             |
| 1393-1396 | F4.2               | ---       | w_NB118          | [0/1.3] Weight corresponding to NB118,               |
| 1398-1410 | E13.10             | 0.3631uJy | NB209            | [-33/42375]?=-99 Aperture flux in                    |
| 1412-1422 | F11.7              | 0.3631uJy | e_NB209          | [0.2/20.6]?=-99 NB209 uncertainty                    |
| 1424-1427 | F4.2               | ---       | w_NB209          | [0/1.2] Weight corresponding to NB209,               |
| 1429-1440 | E12.9              | 0.3631uJy | F125W            | [-8/157256]?=-99 Aperture flux in                    |
| 3         | F125W-band,        | corrected | to               | total (f_F125W) (1)                                  |
| 1442-1452 | F11.7              | 0.3631uJy | e_F125W          | [0.02/3]?=-99 F125W uncertainty                      |
| 1454-1457 | F4.2               | ---       | w_F125W          | [0/6.6] Weight corresponding to F125W,               |
| 1459-1470 | E12.9              | 0.3631uJy | F140W            | [-6/100892]?=-99 Aperture flux in                    |
| 3         | F140W-band,        | corrected | to               | total (f_F140W) (1)                                  |
| 1472-1482 | F11.7              | 0.3631uJy | e_F140W          | [0.07/4.5]?=-99 F140W uncertainty                    |
| 1484-1487 | F4.2               | ---       | w_F140W          | [0/3] Weight corresponding to F140W,                 |
| 1489-1504 | F16.9              | 0.3631uJy | F160W            | [-10/173059]?=-99 Aperture flux in                   |
| 3         | F160W-band,        | corrected | to               | total (f_F160W) (1)                                  |
| 1506-1516 | F11.7              | 0.3631uJy | e_F160W          | [0.02/2.6]?=-99 F160W uncertainty                    |
| 1518-1521 | F4.2               | ---       | w_F160W          | [0/3.7] Weight corresponding to F160W,               |
| 1523-1547 | F25.20             | 0.3631uJy | F606W            | [-6/2170]?=-99 Aperture flux in HST/ACS              |
| 1549-1570 | F22.18             | 0.3631uJy | e_F606W          | [0.02/9]?=-99 F606W uncertainty                      |
| 1572-1575 | F4.2               | ---       | w_F606W          | [0/2.6] Weight corresponding to F606W,               |
| 1577-1601 | F25.20             | 0.3631uJy | F814W            | [-7/7950]?=-99 Aperture flux in HST/ACS              |
| 1603-1624 | F22.18             | 0.3631uJy | e_F814W          | [0.02/4.7]?=-99 F814W uncertainty                    |
| 1626-1629 | F4.2               | ---       | w_F814W          | [0/2.6] Weight corresponding to F814W,               |
| 1631-1656 | F26.20             | 0.3631uJy | FJvista          | [-38.3/57162] Aperture flux UVISTA                   |
| 1658-1677 | F20.17             | 0.3631uJy | e_FJvista        | [0.04/29] FJvista uncertainty                        |
| 1679-1682 | F4.2               | ---       | w_FJvista        | [0.4/1.3] Weight corresponding to                    |
| 1684-1708 | F25.19             | 0.3631uJy | FHvista          | [-28/64424] Aperture flux UVISTA H-band,             |
| 1710-1729 | F20.17             | 0.3631uJy | e_FHvista        | [0.07/41] FJvista uncertainty                        |
| 1731-1734 | F4.2               | ---       | w_FHvista        | [0.2/1.3] Weight corresponding to                    |
| 1736-1760 | F25.19             | 0.3631uJy | FKsvista         | [-8/50829]?=-99 Aperture flux UVISTA                 |
| 1762-1782 | F21.17             | 0.3631uJy | e_FKsvista       | [0.07/47]?=-99 FKsvista error                        |
| 1784-1787 | F4.2               | ---       | w_FKsvista       | [0.05/1.3] Weight corresponding to                   |
| 1789-1814 | F26.20             | 0.3631uJy | FYvista          | [-23/62157]?=-99 Aperture flux UVISTA                |
| 1816-1837 | F22.18             | 0.3631uJy | e_FYvista        | [0.03/23]?=-99 FYvista error                         |
| 1839-1842 | F4.2               | ---       | w_FYvista        | [0.3/1.3] Weight corresponding to                    |
| 1844-1866 | E23.20             | 0.3631uJy | F3.6             | [-1141/19908] Spitzer/IRAC 3.6um-band,               |
| 1868-1888 | F21.17             | 0.3631uJy | e_F3.6           | [-3/25]?=-99 F3.6 uncertainty                        |
| 1890-1895 | F6.2               | ---       | w_F3.6           | [0.02/1.4]?=-99 Weight corresponding to              |
| 1897-1918 | E22.20             | 0.3631uJy | F4.5             | [-527/27177] Spitzer/IRAC 4.5um-band,                |
| 1920-1940 | F21.17             | 0.3631uJy | e_F4.5           | [-3/20]?=-99 F4.5 uncertainty                        |
| 1942-1947 | F6.2               | ---       | w_F4.5           | [0.07/1.3]?=-99 Weight corresponding to              |
| 1949-1974 | F26.20             | 0.3631uJy | F5.8             | [-197/45331] Spitzer/IRAC 5.8um-band,                |
| 1976-1995 | F20.16             | 0.3631uJy | e_F5.8           | [-53/269]?=-99 F5.8 uncertainty                      |
| 1997-2002 | F6.2               | ---       | w_F5.8           | [0.6/1.5]?=-99 Weight corresponding to               |
| 2004-2028 | F25.19             | 0.3631uJy | F8.0             | [-278/21088] Spitzer/IRAC 8.0um-band,                |
| 2030-2049 | F20.16             | 0.3631uJy | e_F8.0           | [-65/317]?=-99 F8.0 uncertainty                      |
| 2051-2056 | F6.2               | ---       | w_F8.0           | [0.7/1.5]?=-99 Weight corresponding to               |
| 2058-2060 | F3.1               | ---       | wminOpt          | [0/1] Minimum weight of groundbased                  |
| 2062-2065 | F4.2               | ---       | wminHST1         | [0/1] Minimum weight of HST optical                  |
| 2067-2070 | F4.2               | ---       | wminfs           | [0/2.6] Minimum weight of FourStar                   |
| 2072-2075 | F4.2               | ---       | wminjhk          | [0/1.4] Minimum weight of broadband JHK              |
| 2077-2080 | F4.2               | ---       | wminHST2         | [0/1.3] Minimum weight of HST NIR                    |
| 2082-2085 | F4.2               | ---       | wminIRAC         | [0/1.4] Minimum weight of Spitzer/IRAC               |
| 2087-2090 | F4.2               | ---       | wminall          | [0/1.4] Minimum weight of all filters                |
| 2092      | I1                 | ---       | Star             | [0/1] 1=star (star) (G1)                             |
| 2094      | I1                 | ---       | Nghb             | [0/1] 1=near a bright star                           |
| 2096      | I1                 | ---       | Use              | [0/1] 1=source selected (use) (G3)                   |
| 2098-2110 | F13.6              | ---       | SNR              | [0/149626] signal-to-noise                           |
| 2112-2119 | F8.4               | ---       | zspec            | [0/6.1]?=-99 Spectroscopic redshift                  |
| 4448      | 0.61               | 31.129    | -0.195           | -0.076                                               |
| 4870      | 0.90               | 26.290    | -0.015           | -0.069                                               |
| 7676      | 0.77               | 25.759    | 0.091            | -0.034                                               |
| 427       | 0.4260             | 0.79      | 31.119           | -0.202     -0.079                                    |
| 484       | 0.4847             | 0.75      | 31.214           | -0.116     -0.069                                    |
| 505       | 0.5061             | 0.82      | 31.252           | -0.083     -0.065                                    |
| 527       | 0.5259             | 0.74      | 31.281           | -0.058     -0.061                                    |
| 624       | 0.6231             | 0.72      | 31.348           | -0.002     -0.050                                    |
| 709       | 0.7074             | 0.81      | 31.343           | -0.015     -0.042                                    |
| 738       | 0.7359             | 0.80      | 31.347           | -0.014     -0.039                                    |
| 6245      | 0.79               | 25.903    | 0.023            | -0.047                                               |
| 3828      | 0.82               | 24.913    | -0.235           | -0.086                                               |
| 5470      | 0.80               | 31.418    | 0.077            | -0.059                                               |
| 6276      | 0.83               | 31.453    | 0.100            | -0.047                                               |
| 8872      | 0.74               | 24.859    | 0.121            | -0.030                                               |
| 9028      | 0.90               | 31.557    | 0.187            | -0.030                                               |
| 7020      | 0.60               | 26.624    | 0.033            | -0.010                                               |
| 5544      | 0.54               | 26.673    | 0.062            | -0.012                                               |
| 1         | 1.0540             | 0.57      | 26.358           | 0.026     -0.020                                     |
| 2         | 1.1448             | 0.55      | 26.590           | 0.038     -0.018                                     |
| 3         | 1.2802             | 0.53      | 26.573           | 0.011     -0.016                                     |
| 1538      | 0.47               | 26.918    | -0.011           | -0.006                                               |
| 118       | 1.1909             | 0.58      | 24.637           | 0.000     -0.018                                     |
| 209       | 2.0990             | 0.52      | 24.849           | 0.000     -0.006                                     |
| 2471      | 0.26               | 26.236    | -0.000           | -0.011                                               |
| 3924      | 0.26               | 26.455    | -0.000           | -0.010                                               |
| 5396      | 0.26               | 25.948    | -0.000           | -0.008                                               |
| 5921      | 0.20               | 26.437    | -0.016           | -0.038                                               |
| 8057      | 0.21               | 25.951    | 0.032            | -0.024                                               |
| 2527      | 0.82               | 30.052    | 0.062            | -0.011                                               |
| 6433      | 0.81               | 29.995    | 0.003            | -0.008                                               |
| 1503      | 0.79               | 30.028    | 0.035            | -0.006                                               |
| 0217      | 0.85               | 30.045    | 0.061            | -0.016                                               |
| 36        | 3.5569             | 1.70      | 21.530           | -0.051      0.000                                    |
| 45        | 4.5020             | 1.70      | 21.537           | -0.044      0.000                                    |
| 58        | 5.7450             | 1.90      | 21.577           | -0.004      0.000                                    |
| 80        | 7.9158             | 2.00      | 21.520           | -0.061      0.000                                    |
| 7         | Subaru/Suprime-Cam | optical   | medium-bandwidth | filters (Taniguchi+ 2007ApJS..172....9T) with seeing |

**Note**: (convolved) aperture flux in filter [] within a 1.2" diameter
          circular aperture, corrected to total (Fap[]=F[]/KsR)
          CDFS passband parameters as in table 3:
       
        Filter    lam_C_    FWHM    Zeropoint   Offset    Galactic
                   (um)    (arcsec)  (AB mag)             extinction
                                      (G6)      (AB mag)   (AB mag)
       
        B         0.4448    0.61    31.129      -0.195     -0.076
        G         0.4870    0.90    26.290      -0.015     -0.069
        I         0.7676    0.77    25.759       0.091     -0.034
        IA427     0.4260    0.79    31.119      -0.202     -0.079
        IA484     0.4847    0.75    31.214      -0.116     -0.069
        IA505     0.5061    0.82    31.252      -0.083     -0.065
        IA527     0.5259    0.74    31.281      -0.058     -0.061
        IA624     0.6231    0.72    31.348      -0.002     -0.050
        IA709     0.7074    0.81    31.343      -0.015     -0.042
        IA738     0.7359    0.80    31.347      -0.014     -0.039
        R         0.6245    0.79    25.903       0.023     -0.047
        U         0.3828    0.82    24.913      -0.235     -0.086
        V         0.5470    0.80    31.418       0.077     -0.059
        Rp        0.6276    0.83    31.453       0.100     -0.047
        Z         0.8872    0.74    24.859       0.121     -0.030
        Zp        0.9028    0.90    31.557       0.187     -0.030
        Hl        1.7020    0.60    26.624       0.033     -0.010
        Hs        1.5544    0.54    26.673       0.062     -0.012
        J1        1.0540    0.57    26.358       0.026     -0.020
        J2        1.1448    0.55    26.590       0.038     -0.018
        J3        1.2802    0.53    26.573       0.011     -0.016
        Ks        2.1538    0.47    26.918      -0.011     -0.006
        NB118     1.1909    0.58    24.637       0.000     -0.018
        NB209     2.0990    0.52    24.849       0.000     -0.006
        F125W     1.2471    0.26    26.236      -0.000     -0.011
        F140W     1.3924    0.26    26.455      -0.000     -0.010
        F160W     1.5396    0.26    25.948      -0.000     -0.008
        F606W     0.5921    0.20    26.437      -0.016     -0.038
        F814W     0.8057    0.21    25.951       0.032     -0.024
        UVISTA_J  1.2527    0.82    30.052       0.062     -0.011
        UVISTA_H  1.6433    0.81    29.995       0.003     -0.008
        UVISTA_Ks 2.1503    0.79    30.028       0.035     -0.006
        UVISTA_Y  1.0217    0.85    30.045       0.061     -0.016
        IRAC_36   3.5569    1.70    21.530      -0.051      0.000
        IRAC_45   4.5020    1.70    21.537      -0.044      0.000
        IRAC_58   5.7450    1.90    21.577      -0.004      0.000
        IRAC_80   7.9158    2.00    21.520      -0.061      0.000
       
       In COSMOS we added CFHT/u, g, r, i, z-imaging
       (Erben+ 2009A&A...493.1197E; Hildebrandt+ 2009A&A...498..725H),
       Subaru/Suprime-Cam/B, V, r+, z+-imaging and 7 Subaru/Suprime-Cam optical
       medium-bandwidth filters (Taniguchi+ 2007ApJS..172....9T) with seeing
       <1.1" (from a set of 12, including seeing >1.1" images), HST/WFC3/F125W,
       F140W,F160W and HST/ACSF606W, F814W-imaging (Grogin+ 2011ApJS..197...35G;
       Koekemoer+ 2011ApJS..197...36K; Brammer+ 2012ApJS..200...13B) and
       UltraVISTA/Y, J, H, Ks-imaging (McCracken+ 2012, J/A+A/544/A156).

</details>

<details>
<summary>zf_uds.dat</summary>

| Bytes     | Format      | Units     | Label    | Explanations                             |
|:----------|:------------|:----------|:---------|:-----------------------------------------|
| 1- 5      | I5          | ---       | Seq      | [1/22093] Running sequence number (id)   |
| 7- 14     | F8.3        | pix       | xpos     | X pixel coordinate (scale: 0.15"/pixel)  |
| 16- 23    | F8.3        | pix       | ypos     | Y pixel coordinate (scale: 0.15"/pixel)  |
| 25- 34    | F10.7       | deg       | RAdeg    | [34.1/34.5] Right ascension (J2000) (ra) |
| 36- 45    | F10.7       | deg       | DEdeg    | [-5.4/-5] Declination (J2000) (dec)      |
| 47- 48    | I2          | ---       | SE       | [0/19] Source Extractor flags            |
| 50- 56    | F7.1        | pix2      | isoArea  | [0/11593] Isophotal area above Source    |
| 58- 71    | F14.8       | 0.3631uJy | FKsap    | [0.08/27497] (convolved) Ks-band         |
| 73- 82    | F10.8       | 0.3631uJy | e_FKsap  | [0.04/0.2] FKsap uncertainty (eap_Ksall) |
| 84- 92    | F9.7        | ---       | apcorr   | [0.9/1.8] Aperture correction applied to |
| 94- 103   | F10.7       | 0.3631uJy | KsR      | [0.6/36.4] Ratio between FKsap and       |
| 105- 118  | F14.8       | 0.3631uJy | FKsapD   | [0.09/20499] Aperture flux measured      |
| 120- 129  | F10.8       | 0.3631uJy | e_FKsapD | [0.04/0.2] FKsapD uncertainty            |
| 131- 138  | F8.6        | ---       | apcorrD  | [1.7/1.8] Aperture correction applied to |
| 140- 152  | F13.7       | 0.3631uJy | FKsD     | [0.1/36322] Total (aperture corrected)   |
| 154- 163  | F10.8       | 0.3631uJy | e_FKsD   | [0.08/0.2] FKsD uncertainty              |
| 165- 179  | F15.8       | 0.3631uJy | FKsauto  | [0.08/66825] Ks-band flux within a       |
| 181- 186  | F6.3        | pix       | R50      | [0.7/32.5] Radius enclosing 50% of the   |
| 188- 193  | F6.3        | pix       | amaj     | [0.5/32.4] Major axis of a Kron-like     |
| 195- 200  | F6.3        | pix       | bmin     | [0.2/13.8] Minor axis of a Kron-like     |
| 202- 207  | F6.3        | ---       | Rad      | [0/63.3] Radius of a circularized        |
| 209- 221  | F13.7       | 0.3631uJy | FKsall   | [0.1/68011]?=-99 Total (aperture         |
| 223- 234  | F12.8       | 0.3631uJy | e_FKsall | [0.08/2.6]?=-99 FKsall uncertainty       |
| 236- 239  | F4.2        | ---       | w_FKsall | [0/1.8] Weight corresponding to FKsall,  |
| 241- 263  | E23.20      | 0.3631uJy | Fu       | [-0.5/1577]?=-99 Aperture flux in        |
| 265- 286  | F22.18      | 0.3631uJy | e_Fu     | [0.02/1.3]?=-99 Fu uncertainty (e_u)     |
| 288- 290  | F3.1        | ---       | w_Fu     | [0/1] Weight corresponding to Fu,        |
| 292- 314  | E23.20      | 0.3631uJy | FB       | [-0.1/968]?=-99 Aperture flux in         |
| 316- 338  | F23.19      | 0.3631uJy | e_FB     | [0.004/0.2]?=-99 FB uncertainty (e_B)    |
| 340- 342  | F3.1        | ---       | w_FB     | [0/1] Weight corresponding to Fu,        |
| 344- 366  | E23.20      | 0.3631uJy | FV       | [-0.2/1126]?=-99 Aperture flux in        |
| 368- 390  | F23.19      | 0.3631uJy | e_FV     | [0.004/0.3]?=-99 FV uncertainty (e_V)    |
| 392- 394  | F3.1        | ---       | w_FV     | [0/1] Weight corresponding to FV,        |
| 396- 418  | E23.20      | 0.3631uJy | FR       | [-0.2/1210]?=-99 Aperture flux in        |
| 420- 441  | F22.18      | 0.3631uJy | e_FR     | [0.006/0.4]?=-99 FR uncertainty (e_R)    |
| 443- 445  | F3.1        | ---       | w_FR     | [0/1] Weight corresponding to FR,        |
| 447- 468  | E22.20      | 0.3631uJy | Fi       | [-0.09/1217]?=-99 Aperture flux in       |
| 470- 492  | F23.19      | 0.3631uJy | e_Fi     | [0.006/0.4]?=-99 Fi uncertainty (e_i)    |
| 494- 496  | F3.1        | ---       | w_Fi     | [0/1] Weight corresponding to Fi,        |
| 498- 522  | F25.20      | 0.3631uJy | Fz       | [-0.5/2716]?=-99 Aperture flux in        |
| 524- 545  | F22.18      | 0.3631uJy | e_Fz     | [0.01/1]?=-99 Fz uncertainty (e_z)       |
| 547- 549  | F3.1        | ---       | w_Fz     | [0/1] Weight corresponding to Fz,        |
| 551- 573  | E23.20      | 0.3631uJy | FJ1      | [-7/22115]?=-99 Aperture flux in         |
| 575- 596  | F22.18      | 0.3631uJy | e_FJ1    | [0.04/23.5]?=-99 FJ1 uncertainty (e_J1)  |
| 598- 601  | F4.2        | ---       | w_FJ1    | [0/1.3] Weight corresponding to FJ1,     |
| 603- 624  | E22.20      | 0.3631uJy | FJ2      | [-4/15074]?=-99 Aperture flux in         |
| 626- 647  | F22.18      | 0.3631uJy | e_FJ2    | [0.04/2.8]?=-99 FJ2 uncertainty (e_J2)   |
| 649- 652  | F4.2        | ---       | w_FJ2    | [0/1.3] Weight corresponding to FJ2,     |
| 654- 679  | F26.20      | 0.3631uJy | FJ3      | [-19/30881]?=-99 Aperture flux in        |
| 681- 702  | F22.18      | 0.3631uJy | e_FJ3    | [0.05/26.4]?=-99 FJ3 uncertainty (e_J3)  |
| 704- 707  | F4.2        | ---       | w_FJ3    | [0/1.3] Weight corresponding to FJ3,     |
| 709- 720  | E12.9       | 0.3631uJy | FHs      | [-6/31381]?=-99 Aperture flux in         |
| 722- 732  | F11.7       | 0.3631uJy | e_FHs    | [0.08/29]?=-99 FHs uncertainty (e_Hs)    |
| 734- 737  | F4.2        | ---       | w_FHs    | [0/1.2] Weight corresponding to FHs,     |
| 739- 763  | F25.19      | 0.3631uJy | FHl      | [-5/28665]?=-99 Aperture flux in         |
| 765- 785  | F21.17      | 0.3631uJy | e_FHl    | [0.09/42]?=-99 FHl uncertainty (e_Hl)    |
| 787- 790  | F4.2        | ---       | w_FHl    | [0/1.2] Weight corresponding to FHl,     |
| 792- 814  | E23.20      | 0.3631uJy | FKs      | [-16/26455]?=-99 Aperture flux in        |
| 816- 836  | F21.17      | 0.3631uJy | e_FKs    | [0.1/38]?=-99 FKs uncertainty (e_Ks)     |
| 838- 841  | F4.2        | ---       | w_FKs    | [0/1.4] Weight corresponding to FKs,     |
| 843- 869  | F27.20      | 0.3631uJy | FJ       | [-0.6/135112]?=-99 Aperture flux in      |
| 871- 892  | F22.18      | 0.3631uJy | e_FJ     | [0.05/2.7]?=-99 FJ uncertainty (e_J)     |
| 894- 896  | F3.1        | ---       | w_FJ     | [0/1] Weight corresponding to FJ,        |
| 898- 923  | F26.20      | 0.3631uJy | FH       | [-1.6/84305]?=-99 Aperture flux in       |
| 925- 945  | F21.17      | 0.3631uJy | e_FH     | [0.05/5.4]?=-99 FH uncertainty (e_H)     |
| 947- 949  | F3.1        | ---       | w_FH     | [0/1] Weight corresponding to FH,        |
| 951- 975  | F25.19      | 0.3631uJy | FK       | [-0.4/76653]?=-99 Aperture flux in       |
| 977- 997  | F21.17      | 0.3631uJy | e_FK     | [0.06/3.4]?=-99 FK uncertainty (e_K)     |
| 999-1002  | F4.2        | ---       | w_FK     | [0/1.3] Weight corresponding to FK,      |
| 1004-1028 | F25.19      | 0.3631uJy | FKsHI    | [-4.4/11697]?=-99 Aperture flux in       |
| 1030-1050 | F21.17      | 0.3631uJy | e_FKsHI  | [0.08/4.3]?=-99 FKsHI uncertainty        |
| 1052-1055 | F4.2        | ---       | w_FKsHI  | [0/1.5] Weight corresponding to FKsHI,   |
| 1057-1071 | F15.9       | 0.3631uJy | F125W    | [-0.6/72981]?=-99 Aperture flux in       |
| 3         | F125W-band, | corrected | to       | total (f_F125W) (1)                      |
| 1073-1083 | F11.7       | 0.3631uJy | e_F125W  | [0.01/1.8]?=-99 F125W uncertainty        |
| 1085-1088 | F4.2        | ---       | w_F125W  | [0/9.8] Weight corresponding to F125W,   |
| 1090-1104 | F15.9       | 0.3631uJy | F140W    | [-0.6/46628]?=-99 Aperture flux in       |
| 3         | F140W-band, | corrected | to       | total (f_F140W) (1)                      |
| 1106-1118 | F13.7       | 0.3631uJy | e_F140W  | [0.05/3.2]?=-99 F140W uncertainty        |
| 1120-1123 | F4.2        | ---       | w_F140W  | [0/3] Weight corresponding to F140W,     |
| 1125-1136 | E12.9       | 0.3631uJy | F160W    | [-0.7/79691]?=-99 Aperture flux in       |
| 3         | F160W-band, | corrected | to       | total (f_F160W) (1)                      |
| 1138-1150 | F13.7       | 0.3631uJy | e_F160W  | [0.02/1.7]?=-99 F160W uncertainty        |
| 1152-1155 | F4.2        | ---       | w_F160W  | [0/4] Weight corresponding to F160W,     |
| 1157-1179 | E23.20      | 0.3631uJy | F606W    | [-0.8/2933]?=-99 Aperture flux in        |
| 1181-1204 | F24.18      | 0.3631uJy | e_F606W  | [0.02/1.5]?=-99 F606W uncertainty        |
| 1206-1209 | F4.2        | ---       | w_F606W  | [0/2.5] Weight corresponding to F606W,   |
| 1211-1235 | F25.19      | 0.3631uJy | F814W    | [-0.3/3425]?=-99 Aperture flux in        |
| 1237-1260 | F24.18      | 0.3631uJy | e_F814W  | [0.02/1.6]?=-99 F814W uncertainty        |
| 1262-1265 | F4.2        | ---       | w_F814W  | [0/2.6] Weight corresponding to F814W,   |
| 1267-1289 | E23.20      | 0.3631uJy | FY       | [-1/6983]?=-99 Aperture flux in          |
| 1291-1315 | F25.19      | 0.3631uJy | e_FY     | [0/1.2]?=-99 FY uncertainty (e_Y)        |
| 1317-1321 | F5.2        | ---       | w_FY     | [0/]?=99.99 Weight corresponding to FY,  |
| 1323-1344 | E22.19      | 0.3631uJy | F3.6     | [-35/18245]?=-99 Aperture flux in        |
| 1346-1366 | F21.17      | 0.3631uJy | e_F3.6   | [-5/6.5]?=-99 F3.6 uncertainty           |
| 1368-1374 | F7.2        | ---       | w_F3.6   | [0.4/1.3]?=-99 Weight corresponding to   |
| 1376-1401 | F26.20      | 0.3631uJy | F4.5     | [-27/18083]?=-99 Aperture flux in        |
| 1403-1424 | F22.18      | 0.3631uJy | e_F4.5   | [-6/7.3]?=-99 F4.5 uncertainty           |
| 1426-1432 | F7.2        | ---       | w_F4.5   | [0.4/1.3]?=-99 Weight corresponding to   |
| 1434-1456 | E23.20      | 0.3631uJy | F5.8     | [-672/16511]?=-99 Aperture flux in       |
| 1458-1479 | F22.16      | 0.3631uJy | e_F5.8   | [-672/86] F5.8 uncertainty (e_IRAC_58)   |
| 1481-1485 | F5.1        | ---       | w_F5.8   | [1]?=-99 Weight corresponding to 5.8um,  |
| 1487-1512 | F26.20      | 0.3631uJy | F8.0     | [-672/21089]?=-99 Aperture flux in       |
| 1514-1535 | F22.16      | 0.3631uJy | e_F8.0   | [-791/109] F8.0 uncertainty (e_IRAC_80)  |
| 1537-1541 | F5.1        | ---       | w_F8.0   | [1]?=-99 Weight corresponding to 8.0um,  |
| 1543-1545 | F3.1        | ---       | wminOpt  | [1] Minimum weight of groundbased        |
| 1547-1550 | F4.2        | ---       | wminHST1 | [0/1] Minimum weight of HST optical      |
| 1552-1555 | F4.2        | ---       | wminfs   | [0/2.5] Minimum weight of FourStar       |
| 1557-1560 | F4.2        | ---       | wminjhk  | [0/1.8] Minimum weight of broadband J,   |
| 1562-1565 | F4.2        | ---       | wminHST2 | [0/1] Minimum weight of HST near-IR      |
| 1567-1569 | F3.1        | ---       | wminIRAC | [0/1] Minimum weight of Spitzer/IRAC     |
| 1571-1574 | F4.2        | ---       | wminAll  | [0.3/1.8] Minimum weight of all filters  |
| 1576      | I1          | ---       | Star     | [0/1] 1=source is likely a star (G1)     |
| 1578      | I1          | ---       | Nghb     | [0/1] 1=near a bright star               |
| 1580      | I1          | ---       | Use      | [0/1] 1=selected (use) (G3)              |
| 1582-1594 | F13.6       | ---       | SNR      | [1.5/266262] Signal-to-noise             |
| 1596-1602 | F7.3        | ---       | zspec    | [0.06/6.2]?=-99 Spectroscopic redshift   |
| 3828      | 1.06        | 24.905    | -0.268   | -0.089                                   |
| 4408      | 0.91        | 24.803    | -0.123   | -0.074                                   |
| 5470      | 0.93        | 24.870    | -0.072   | -0.058                                   |
| 6508      | 0.96        | 24.914    | -0.038   | -0.049                                   |
| 7656      | 0.98        | 24.986    | 0.021    | -0.035                                   |
| 9060      | 0.99        | 24.974    | 0.001    | -0.027                                   |
| 0540      | 0.55        | 26.121    | -0.036   | -0.022                                   |
| 1448      | 0.53        | 26.408    | -0.029   | -0.019                                   |
| 2802      | 0.51        | 26.481    | -0.019   | -0.015                                   |
| 5544      | 0.49        | 26.591    | -0.000   | -0.011                                   |
| 7020      | 0.51        | 26.448    | -0.036   | -0.010                                   |
| 1538      | 0.44        | 26.804    | -0.067   | -0.006                                   |
| 2502      | 0.91        | 30.863    | -0.052   | -0.015                                   |
| 6360      | 0.89        | 31.262    | -0.108   | -0.010                                   |
| 2060      | 0.86        | 31.825    | -0.059   | -0.006                                   |
| 2471      | 0.26        | 26.214    | -0.000   | -0.016                                   |
| 3924      | 0.26        | 26.439    | -0.000   | -0.013                                   |
| 5396      | 0.26        | 25.935    | -0.000   | -0.011                                   |
| 5893      | 0.20        | 26.383    | -0.054   | -0.054                                   |
| 8057      | 0.23        | 25.926    | 0.015    | -0.033                                   |
| 0207      | 0.58        | 27.004    | 0.026    | -0.022                                   |
| 1748      | 0.46        | 27.520    | 0.026    | -0.006                                   |
| 36        | 3.5569      | 1.70      | 21.539   | -0.042    0.000                          |
| 45        | 4.5020      | 1.70      | 21.556   | -0.025    0.000                          |
| 58        | 5.7450      | 1.90      | 21.458   | -0.123    0.000                          |
| 80        | 7.9158      | 2.00      | 21.522   | -0.059    0.000                          |

**Note**: (convolved) aperture flux in filter [] within a 1.2" diameter
          circular aperture, corrected to total (Fap[]=F[]/KsR)
          CDFS passband parameters as in table 4:
       
        Filter    lam_C_    FWHM    Zeropoint   Offset   Galactic
                   (um)   (arcsec)  (AB mag)            extinction
                                     (G6)      (AB mag)  (AB mag)
       
        u         0.3828    1.06     24.905     -0.268   -0.089
        B         0.4408    0.91     24.803     -0.123   -0.074
        V         0.5470    0.93     24.870     -0.072   -0.058
        R         0.6508    0.96     24.914     -0.038   -0.049
        i         0.7656    0.98     24.986      0.021   -0.035
        z         0.9060    0.99     24.974      0.001   -0.027
        J_1_      1.0540    0.55     26.121     -0.036   -0.022
        J_2_      1.1448    0.53     26.408     -0.029   -0.019
        J_3_      1.2802    0.51     26.481     -0.019   -0.015
        H_s_      1.5544    0.49     26.591     -0.000   -0.011
        H_l_      1.7020    0.51     26.448     -0.036   -0.010
        Ks        2.1538    0.44     26.804     -0.067   -0.006
        J         1.2502    0.91     30.863     -0.052   -0.015
        H         1.6360    0.89     31.262     -0.108   -0.010
        K         2.2060    0.86     31.825     -0.059   -0.006
        F125W     1.2471    0.26     26.214     -0.000   -0.016
        F140W     1.3924    0.26     26.439     -0.000   -0.013
        F160W     1.5396    0.26     25.935     -0.000   -0.011
        F606W     0.5893    0.20     26.383     -0.054   -0.054
        F814W     0.8057    0.23     25.926      0.015   -0.033
        Y         1.0207    0.58     27.004      0.026   -0.022
        KsHI      2.1748    0.46     27.520      0.026   -0.006
        IRAC_36   3.5569    1.70     21.539     -0.042    0.000
        IRAC_45   4.5020    1.70     21.556     -0.025    0.000
        IRAC_58   5.7450    1.90     21.458     -0.123    0.000
        IRAC_80   7.9158    2.00     21.522     -0.059    0.000
       
       In UDS the additional filters are CFHT/MegaCam/U (O. Almaini 2016,
       in preparation; S. Foucaud 2016, in preparation),
       Subaru/Surpime-Cam/B, V, R, i, z (Furusawa+ 2008ASPC..399..131F),
       UKIRT/WFCAM/J, H, Ks (O. Almaini 2016, in preparation), HST/WFC3/F125W,
       F140W, F160W and HST/ACSF606W, F814W (Grogin+ 2011ApJS..197...35G;
       Koekemoer+ 2011ApJS..197...36K; Brammer+ 2012ApJS..200...13B) and
       VLT/HAWK-I/Y (Fontana+ 2014, J/A+A/570/A11).
       KsHI comes from a combined VLT/HAWKI and Magellan/FOURSTAR image.

</details>
