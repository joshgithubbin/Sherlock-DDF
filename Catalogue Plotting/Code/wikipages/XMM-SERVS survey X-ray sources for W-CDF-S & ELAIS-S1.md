**Authors:** Brandt W.N., Chen C.-T., Luo B., Nyland K., Yang G., Zou F.,, Aird J., Alexander D.M., Bauer F.E., Lacy M., Lehmer B.D., Mallick L.,, Salvato M., Schneider D.P., Tozzi P., Traulsen I., Vaccari M., Vignali C.,, Vito F., Xue Y., Banerji M., Chow K., Comastri A., Del Moro A., Gilli R.,, Mullaney J., Paolillo M., Schwope A., Shemmer O., Sun M., Timlin Iii J.D.,, Trump J.R., <Astrophys. J. Suppl. Ser., 256, 21-21 (2021)>, =2021ApJS..256...21N (SIMBAD/NED BibCode)

## Summary: XMM-SERVS survey: X-ray sources for W-CDF-S & ELAIS-S1 

We present the X-ray point-source catalogs in two of the XMM-Spitzer Extragalactic Representative Volume Survey (XMM-SERVS) fields, W-CDF-S (4.6deg^2^) and ELAIS-S1 (3.2deg^2^), aiming to fill the gap between deep pencil-beam X-ray surveys and shallow X-ray surveys over large areas. The W-CDF-S and ELAIS-S1 regions were targeted with 2.3 and 1.0Ms of XMM-Newton observations, respectively; 1.8 and 0.9Ms exposures remain after flare filtering. The survey in W-CDF-S has a flux limit of 1.0x10^-14^erg/cm^2^/s over 90% of its area in the 0.5-10keV band; 4053 sources are detected in total. The survey in ELAIS-S1 has a flux limit of 1.3x10^-14^erg/cm^2^/s over 90% of its area in the 0.5-10keV band; 2630 sources are detected in total. Reliable optical-to-IR multiwavelength counterpart candidates are identified for ~89% of the sources in W-CDF-S and ~87% of the sources in ELAIS-S1. A total of 3129 sources in W-CDF-S and 1957 sources in ELAIS-S1 are classified as active galactic nuclei (AGNs). We also provide photometric redshifts for X-ray sources; ~84% of the 3319/2001 sources in W-CDF-S/ELAIS-S1 with optical-to-near-IR forced photometry available have either spectroscopic redshifts or high-quality photometric redshifts. The completion of the XMM-Newton observations in the W-CDF-S and ELAIS-S1 fields marks the end of the XMM-SERVS survey data gathering. The ~12000 pointlike X-ray sources detected in the whole ~13deg^2^ XMM-SERVS survey will benefit future large-sample AGN studies.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-256-21/Subcatalogues/ELAIS S1/Plots/fieldcover.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-256-21/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zsp:** [0.00013/4.05]?=-99 Spectroscopic 
 

## Photometric Redshift 
 
**zphot:** [0.01/4.27]?=-99 Suggested photometric 
 

## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format       | Units   | Label   | Explanations                                       |
|:--------|:-------------|:--------|:--------|:---------------------------------------------------|
| 1- 8    | A8           | ---     | Field   | Target field ("ELAIS-S1"=31 occurrences or         |
| 80      | occurrences) | 10-     | 13      | I4    ---     Nrev    XMM-Newton revolution number |
| 15- 24  | I10          | ---     | ObsID   | XMM-Newton observation ID                          |
| 26- 44  | A19          | ---     | Date    | Observation starting date/time (UT), ISO8601       |
| 46- 54  | F9.6         | deg     | RAdeg   | [8.7/54.2] Right ascension, pointing               |
| 56- 65  | F10.6        | deg     | DEdeg   | [-45/-27] Declination, pointing center (J2000)     |
| 67- 70  | F4.1         | ks      | PN      | [0.0/41.6] Cleaned exposure time for PN (1)        |
| 72- 75  | F4.1         | ks      | MOS1    | [0.0/43.5] Cleaned exposure time for MOS1 (1)      |
| 77- 80  | F4.1         | ks      | MOS2    | [0.0/43.5] Cleaned exposure time for MOS2 (1)      |
| 82- 85  | F4.1         | ks      | Exp     | [7.0/44.9] Total EPIC exposure time                |

**Note**: Cleaned exposure time included in the "good time intervals"; GTIs.

</details>

<details>
<summary>table6.dat</summary>

| Bytes      | Format       | Units        | Label           | Explanations                                                                 |
|:-----------|:-------------|:-------------|:----------------|:-----------------------------------------------------------------------------|
| 1- 5       | A5           | ---          | Field           | [WCDFS] W-CDF-S field ("WCDFS")                                              |
| 6- 9       | I04          | ---          | WCDFS           | [0/4052] The source ID of each X-ray                                         |
| 11- 19     | F9.6         | deg          | RAdeg           | [51.6/54.5] Right ascension (J2000.0)                                        |
| 21- 30     | F10.6        | deg          | DEdeg           | [-29/-26] Declination (J2000.0)                                              |
| 32- 39     | F8.6         | arcsec       | eXPos           | [0.07/4.4] X-ray positional                                                  |
| 41- 48     | F8.6         | arcsec       | R68             | [0.1/6.7] The 68% positional-                                                |
| 50- 58     | F9.6         | arcsec       | R99             | [0.2/15.1] The 99.73%                                                        |
| 60- 67     | F8.6         | arcsec       | eEMPos          | [0.04/8] Positional uncertainty                                              |
| 69- 78     | F10.6        | deg          | RASBdeg         | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 80- 89     | F10.6        | deg          | DESBdeg         | [-29/-26]?=-99 Declination (J2000.0) as                                      |
| 91- 100    | F10.6        | deg          | RAHBdeg         | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 102- 111   | F10.6        | deg          | DEHBdeg         | [-29/-26]?=-99 Declination (J2000.0) as                                      |
| 113- 122   | F10.6        | deg          | RAFBdeg         | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 124- 133   | F10.6        | deg          | DEFBdeg         | [-29/-26]?=-99 Declination (J2000.0) as                                      |
| 135- 148   | F14.6        | ---          | detSB           | [3.5/109715]?=-99 The emldetect                                              |
| 150- 162   | F13.6        | ---          | detHB           | [9.5/11681]?=-99 The emldetect                                               |
| 164- 177   | F14.6        | ---          | detFB           | [3.5/121389]?=-99 The emldetect                                              |
| 179- 188   | F10.3        | s            | ExpSB           | [2261/217999] Total (PN+MOS1+MOS2)                                           |
| 190- 199   | F10.3        | s            | ExpHB           | [1507/179250] Total (PN+MOS1+MOS2)                                           |
| 201- 210   | F10.3        | s            | ExpFB           | [1721/223271] Total (PN+MOS1+MOS2)                                           |
| 212- 220   | F9.3         | s            | PNExpSB         | [1617/55520]?=0 PN exposure time in the                                      |
| 222- 230   | F9.3         | s            | M1ExpSB         | [60/84807]?=0 MOS1 exposure time in the                                      |
| 232- 240   | F9.3         | s            | M2ExpSB         | [1472/86841]?=0 MOS2 exposure time in the                                    |
| 242- 250   | F9.3         | s            | PNExpHB         | [1056/52663]?=0 PN exposure time in the                                      |
| 252- 260   | F9.3         | s            | M1ExpHB         | [13/68738]?=0 MOS1 exposure time in the                                      |
| 262- 270   | F9.3         | s            | M2ExpHB         | [2166/77002]?=0 MOS2 exposure time in the                                    |
| 272- 280   | F9.3         | s            | PNExpFB         | [1144/57280]?=0 PN exposure time in the                                      |
| 282- 290   | F9.3         | s            | M1ExpFB         | [1457/85675]?=0 MOS1 exposure time in the                                    |
| 292- 300   | F9.3         | s            | M2ExpFB         | [3092/84105]?=0 MOS2 exposure time in the                                    |
| 302- 310   | F9.6         | ct/pix       | BkgSB           | [0.08/5.5]?=99 Total background-map                                          |
| 312- 320   | F9.6         | ct/pix       | BkgHB           | [0/4.7]?=99 Total background-map                                             |
| 322- 330   | F9.6         | ct/pix       | BkgFB           | [0/8.3]?=99 Total background-map value                                       |
| 332- 339   | F8.6         | ct/pix       | PNBkgSB         | [0/3.8] PN background-map value in the                                       |
| 341- 348   | F8.6         | ct/pix       | M1BkgSB         | [0/1.3] MOS1 background-map value in the                                     |
| 350- 357   | F8.6         | ct/pix       | M2BkgSB         | [0/1.1] MOS2 background-map value in th                                      |
| 359- 366   | F8.6         | ct/pix       | PNBkgHB         | [0/2.4] PN background-map value in the                                       |
| 368- 375   | F8.6         | ct/pix       | M1BkgHB         | [0/1.6] MOS1 background-map value in th                                      |
| 377- 384   | F8.6         | ct/pix       | M2BkgHB         | [0/1.4] MOS2 background-map value in the                                     |
| 386- 393   | F8.6         | ct/pix       | PNBkgFB         | [0/5.5] PN background-map value in the                                       |
| 395- 402   | F8.6         | ct/pix       | M1BkgFB         | [0/2.7] MOS1 background-map value in the                                     |
| 404- 411   | F8.6         | ct/pix       | M2BkgFB         | [0/2.4] MOS2 background-map value in th                                      |
| 413- 424   | F12.6        | ct           | CtsSB           | [6/26510] Total (PN+MOS1+MOS2) net                                           |
| 426- 436   | F11.6        | ct           | CtsHB           | [17/4126] Total (PN+MOS1+MOS2) net                                           |
| 438- 449   | F12.6        | ct           | CtsFB           | [7/30391] Total (PN+MOS1+MOS2) net                                           |
| 451- 462   | F12.6        | ct           | PNCtsSB         | [0/9997]?=-99 PN net counts in the soft                                      |
| 464- 475   | F12.6        | ct           | M1CtsSB         | [0/6585]?=-99 MOS1 net counts in the                                         |
| 477- 488   | F12.6        | ct           | M2CtsSB         | [0/9928]?=-99 MOS2 net counts in the                                         |
| 490- 501   | F12.6        | ct           | PNCtsHB         | [0/2392]?=-99 PN net counts in the hard                                      |
| 503- 514   | F12.6        | ct           | M1CtsHB         | [0/1065]?=-99 MOS1 net counts in the                                         |
| 516- 527   | F12.6        | ct           | M2CtsHB         | [0/1991]?=-99 MOS2 net counts in the                                         |
| 529- 541   | F13.6        | ct           | PNCtsFB         | [0/10824]?=-99 PN net counts in the                                          |
| 543- 554   | F12.6        | ct           | M1CtsFB         | [0/7649]?=-99 MOS1 net counts in the                                         |
| 556- 568   | F13.6        | ct           | M2CtsFB         | [0/11919]?=-99 MOS2 net counts in the                                        |
| 570- 581   | F12.6        | ct           | e_CtsSB         | [3.8/7978]?=-99 Uncertainty on CtsSB                                         |
| 583- 594   | F12.6        | ct           | e_CtsHB         | [5.3/6678]?=-99 Uncertainty on CtsHB                                         |
| 596- 608   | F13.6        | ct           | e_CtsFB         | [5/16029]?=-99 Uncertainty on CtsFB                                          |
| 610- 621   | F12.6        | ct           | e_PNCtsSB       | [0/5543]?=-99 Uncertainty on PNCtsSB                                         |
| 623- 632   | F10.6        | ct           | e_M1CtsSB       | [0/85]?=-99 Uncertainty of M1CtsSB                                           |
| 634- 645   | F12.6        | ct           | e_M2CtsSB       | [0/7978]?=-99 Uncertainty of M2CtsSB                                         |
| 647- 658   | F12.6        | ct           | e_PNCtsHB       | [0/6678]?=-99 Uncertainty on PNCtsHB                                         |
| 660- 671   | F12.6        | ct           | e_M1CtsHB       | [0/2925]?=-99 Uncertainty on M1CtsHB                                         |
| 673- 682   | F10.6        | ct           | e_M2CtsHB       | [0/49]?=-99 Uncertainty of M2CtsHB                                           |
| 684- 696   | F13.6        | ct           | e_PNCtsFB       | [0/16029]?=-99 Uncertainty on PNCtsFB                                        |
| 698- 709   | F12.6        | ct           | e_M1CtsFB       | [0/4963]?=-99 Uncertainty of M1CtsFB                                         |
| 711- 723   | F13.6        | ct           | e_M2CtsFB       | [0/15920]?=-99 Uncertainty of M2CtsFB                                        |
| 725- 734   | F10.8        | ct/s         | CRtSB           | [0.0003/1.16] Total (PN+MOS1+MOS2) net                                       |
| 736- 745   | F10.8        | ct/s         | CRtHB           | [0.0009/0.15] Total (PN+MOS1+MOS2) net                                       |
| 747- 756   | F10.8        | ct/s         | CRtFB           | [0.0003/1.31] Total (PN+MOS1+MOS2) net                                       |
| 758- 766   | E9.4         | ct/s         | PNCRtSB         | [0/0.8]?=99 PN net count rates in the                                        |
| 768- 776   | E9.4         | ct/s         | M1CRtSB         | [0/0.21]?=99 MOS1 net count rates in the                                     |
| 778- 786   | E9.4         | ct/s         | M2CRtSB         | [0/0.24]?=99 MOS2 net count rates in the                                     |
| 788- 798   | F11.8        | ct/s         | PNCRtHB         | [0/0.08]?=99 PN net count rates in the                                       |
| 800- 808   | E9.4         | ct/s         | M1CRtHB         | [0/0.04]?=99 MOS1 net count rates in the                                     |
| 810- 818   | E9.4         | ct/s         | M2CRtHB         | [0/0.05]?=99 MOS2 net count rates in the                                     |
| 820- 826   | E7.2         | ct/s         | PNCRtFB         | [0/0.8]?=99 PN net count rates in the                                        |
| 828- 836   | E9.4         | ct/s         | M1CRtFB         | [0/0.25]?=99 MOS1 net count rates in the                                     |
| 838- 846   | E9.4         | ct/s         | M2CRtFB         | [0/0.3]?=99 MOS2 net count rates in the                                      |
| 848- 858   | F11.8        | ct/s         | e_CRtSB         | [0.0002/0.5]?=99 Uncertainty on CRtSB                                        |
| 860- 870   | F11.8        | ct/s         | e_CRtHB         | [0.0002/0.32]?=99 Uncertainty on CRtHB                                       |
| 872- 882   | F11.8        | ct/s         | e_CRtFB         | [0.0003/0.94]?=99 Uncertainty on CRtFB                                       |
| 884- 894   | F11.8        | ct/s         | e_PNCRtSB       | [0/0.33]?=99 Uncertainty of PNCRtSB                                          |
| 896- 904   | E9.4         | ct/s         | e_M1CRtSB       | [0/0.005]?=99 Uncertainty on M1CRtSB                                         |
| 906- 914   | E9.4         | ct/s         | e_M2CRtSB       | [0/0.5]?=99 Uncertainty on M2CRtSB                                           |
| 916- 926   | F11.8        | ct/s         | e_PNCRtHB       | [0/0.32]?=99 Uncertainty on PNCRtHB                                          |
| 928- 936   | E9.4         | ct/s         | e_M1CRtHB       | [0/0.2]?=99 Uncertainty on M1CRtHB                                           |
| 938- 948   | F11.8        | ct/s         | e_M2CRtHB       | [0/0.0021]?=99 Uncertainty on M2CRtHB                                        |
| 950- 960   | F11.8        | ct/s         | e_PNCRtFB       | [0/0.94]?=99 Uncertainty on PNCRtFB                                          |
| 962- 972   | F11.8        | ct/s         | e_M1CRtFB       | [0/0.2]?=99 Uncertainty on M1CRtFB                                           |
| 974- 984   | F11.8        | ct/s         | e_M2CRtFB       | [0/0.7]?=99 Uncertainty on M2CRtFB                                           |
| 986- 991   | F6.3         | ---          | BR              | [0.019/33.5] Total hard-to-soft band                                         |
| 993- 998   | F6.3         | ---          | e_BR            | [0.003/39]?=99 Uncertainty on BR (BR_ERR)                                    |
| 1000- 1005 | F6.3         | ---          | PNBR            | [0.014/6]?=99 PN hard-to-soft band ratio                                     |
| 1007- 1012 | F6.3         | ---          | e_PNBR          | [0.004/30]?=99 Uncertainty on PNBR                                           |
| 1014- 1019 | F6.3         | ---          | M1BR            | [0.009/23]?=99 MOS1 hard-to-soft band                                        |
| 1021- 1027 | F7.3         | ---          | e_M1BR          | [0.006/169]?=99 Uncertainty on M1BR                                          |
| 1029- 1034 | F6.3         | ---          | M2BR            | [0.03/9]?=99 MOS2 hard-to-soft band ratio                                    |
| 1036- 1041 | F6.3         | ---          | e_M2BR          | [0.006/6]?=99 Uncertainty on M2BR                                            |
| 1043- 1048 | F6.3         | ---          | HR              | [-0.97/0.95] Hardness ratio                                                  |
| 1050- 1056 | F7.3         | ---          | e_HR            | [-2/14.1]?=-99 Uncertainty on HR (HR_ERR)                                    |
| 1058- 1061 | F4.1         | ---          | Gamma           | [-1/2.9] The effective power-law                                             |
| 1063- 1073 | F11.8        | fW/m2        | F0.5-2keV       | [0.0004/0.81]?=99 Apparent flux in                                           |
| 1075- 1085 | F11.8        | fW/m2        | e_F0.5-2keV     | [0.0001/0.011]?=99 Uncertainty on                                            |
| 1087- 1097 | F11.8        | fW/m2        | F2-10keV        | [0.004/1.1]?=99 Apparent flux in                                             |
| 1099- 1109 | F11.8        | fW/m2        | e_F2-10keV      | [0.001/0.08]?=99 Uncertainty on F2-10keV                                     |
| 1111- 1121 | F11.8        | fW/m2        | F0.5-10keV      | [0.001/1.7]?=99 Apparent flux in                                             |
| 1123- 1133 | F11.8        | fW/m2        | e_F0.5-10keV    | [0.0005/0.07]?=99 Uncertainty on                                             |
| 1135- 1140 | F6.2         | [10-7W]      | LX              | [35.27/45.55]? Log rest-frame apparent                                       |
| 1142- 1144 | I3           | ---          | CCat            | [1/3]?=-99 The catalog origin of the                                         |
| 1146- 1167 | A22          | ---          | CID             | Source ID in the matched Chandra                                             |
| 1169- 1178 | F10.6        | deg          | RACdeg          | [52.2/54.4]?=-99 Right ascension (J2000)                                     |
| 1180- 1189 | F10.6        | deg          | DECdeg          | [-28.2/-27]?=-99 Declination (J2000) of                                      |
| 1191- 1200 | F10.6        | ---          | Pany            | [0.1/1]?=-99 The posterior probability of                                    |
| 1202- 1211 | F10.6        | ---          | Pi              | [0.2/1]?=-99 The relative probability of                                     |
| 1          | counterpart  | to           | be              | the correct match                                                            |
| 1213       | I1           | ---          | F2              | [0/1] Warning flag for sources where a                                       |
| 1215- 1224 | F10.6        | deg          | RAIRdeg         | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 1226- 1235 | F10.6        | deg          | DEIRdeg         | [-29/-26]?=-99 Declination (J2000.0) of                                      |
| 1237- 1246 | F10.6        | deg          | RAVdeg          | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 1248- 1257 | F10.6        | deg          | DEVdeg          | [-29/-26]?=-99 Declination (J2000.0) of                                      |
| 1259- 1268 | F10.6        | deg          | RAHdeg          | [51.7/54.5]?=-99 Right ascension (J2000)                                     |
| 1270- 1279 | F10.6        | deg          | DEHdeg          | [-29/-26]?=-99 Declination (J2000.0) of                                      |
| 1281- 1290 | F10.6        | deg          | RADdeg          | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 1292- 1301 | F10.6        | deg          | DEDdeg          | [-29/-27]?=-99 Declination (J2000.0) of                                      |
| 1303- 1313 | F11.6        | arcsec       | SepIRAC         | [0.02/9.8]?=-99 Separation of the X-ray                                      |
| 1315- 1325 | F11.6        | arcsec       | SepVIDEO        | [0.01/9.9]?=-99 Separation of the X-ray                                      |
| 1327- 1336 | F10.6        | arcsec       | SepHSC          | [0.01/9.8]?=-99 Separation of the X-ray                                      |
| 1338- 1347 | F10.6        | arcsec       | SepDES          | [0.1/9.6]?=-99 Separation of the X-ray                                       |
| 1349- 1357 | F9.6         | mag          | 3.6magAp        | [12.68/23]?=99 1.9 arcsec aperture                                           |
| 6          | micron       | band         | reported        | in the DeepDrill catalog                                                     |
| 1359- 1367 | F9.6         | mag          | e_3.6magAp      | [0.03/0.3]?=99 The uncertainty on                                            |
| 1369- 1377 | F9.6         | mag          | 4.5magAp        | [12.9/22.8]?=99 1.9 arcsec aperture                                          |
| 5          | micron       | band         | reported        | in the DeepDrill catalog                                                     |
| 1379- 1387 | F9.6         | mag          | e_4.5magAp      | [0.03/0.3]?=99 The uncertainty on                                            |
| 1389- 1397 | F9.6         | mag          | Zapc3           | [12.34/27.5]?=99 VIDEO 2" aperture                                           |
| 1399- 1405 | E7.2         | mag          | e_Zapc3         | [4e-6/1.8]?=99 Uncertainty on Zapc3                                          |
| 1407- 1415 | F9.6         | mag          | Yapc3           | [11.5/26.3]?=99 VIDEO 2 arcsec aperture                                      |
| 1417- 1423 | E7.2         | mag          | e_Yapc3         | [3e-6/1.2]?=99 Uncertainty on Yapc3                                          |
| 1425- 1433 | F9.6         | mag          | Japc3           | [12.19/26.1]?=99 VIDEO 2 arcsec aperture                                     |
| 1435- 1441 | E7.2         | mag          | e_Japc3         | [5e-6/0.5]?=99 Uncertainty on Japc3                                          |
| 1443- 1451 | F9.6         | mag          | Hapc3           | [12.22/27.3]?=99 VIDEO 2 arcsec aperture                                     |
| 1453- 1459 | E7.2         | mag          | e_Hapc3         | [5e-6/2.2]?=99 Uncertainty on Hapc3                                          |
| 1461- 1469 | F9.6         | mag          | Ksapc3          | [12.24/24]?=99 VIDEO 2 arcsec aperture                                       |
| 1471- 1477 | E7.2         | mag          | e_Ksapc3        | [6e-6/0.3]?=99 Uncertainty on Ksapc3                                         |
| 1479- 1487 | F9.6         | mag          | gmag            | [16.65/29.2]?=99 HSC CModel photometry in                                    |
| 1489- 1497 | F9.6         | mag          | e_gmag          | [0.0001/2.9]?=99 Uncertainty on gmag                                         |
| 1499- 1507 | F9.6         | mag          | rmag            | [16.42/29]?=99 HSC CModel photometry in                                      |
| 1509- 1517 | F9.6         | mag          | e_rmag          | [0.0002/7.2]?=99 Uncertainty on rmag                                         |
| 1519- 1527 | F9.6         | mag          | imag            | [15.54/26.9]?=99 HSC CModel photometry in                                    |
| 1529- 1537 | F9.6         | mag          | e_imag          | [0.0001/0.5]?=99 Uncertainty of HSC                                          |
| 1539- 1547 | F9.6         | mag          | zmag            | [15.37/26.8]?=99 HSC CModel photometry in                                    |
| 1549- 1557 | F9.6         | mag          | e_zmag          | [0.0001/1.7]?=99 Uncertainty on zmag                                         |
| 1559- 1567 | F9.6         | mag          | gmagDES         | [12/27.9]?=99 DES Kron photometry in the                                     |
| 1569- 1575 | E7.2         | mag          | e_gmagDES       | [6.5e-5/1.8]?=99 Uncertainty on gmagDES                                      |
| 1577- 1585 | F9.6         | mag          | rmagDES         | [11.99/26.9]?=99 DES Kron photometry in                                      |
| 1587- 1593 | E7.2         | mag          | e_rmagDES       | [5.9e-5/1.3]?=99 Uncertainty on rmagDES                                      |
| 1595- 1603 | F9.6         | mag          | imagDES         | [11.95/25.8]?=99 DES Kron photometry in                                      |
| 1605- 1611 | E7.2         | mag          | e_imagDES       | [9.3e-5/1]?=99 Uncertainty on imagDES                                        |
| 1613- 1621 | F9.6         | mag          | zmagDES         | [11.45/25.9]?=99 DES Kron photometry in                                      |
| 1623- 1631 | F9.6         | mag          | e_zmagDES       | [0.0001/1.2]?=99 Uncertainty on zmagDES                                      |
| 1633- 1641 | F9.6         | mag          | YmagDES         | [10.15/25]?=99 DES Kron photometry in                                        |
| 1643- 1651 | F9.6         | mag          | e_YmagDES       | [0.0001/5.7]?=99 Uncertainty on YmagDES                                      |
| 1653- 1658 | I6           | ---          | Tractor         | [10/804323]?=-99 The object ID of the                                        |
| 1660- 1669 | F10.6        | mag          | 3.6mag          | [11.6/25.4]?=-99 Forced photometry in                                        |
| 6          | micron       | band         | (IRAC_1_FP_MAG) | 1671- 1680 F10.6  mag     e_3.6mag     [0.09/0.8]?=-99 Uncertainty on 3.6mag |
| 1682- 1691 | F10.6        | mag          | 4.5mag          | [11.6/25.3]?=-99 Forced photometry in                                        |
| 5          | micron       | band         | (IRAC_2_FP_MAG) | 1693- 1702 F10.6  mag     e_4.5mag     [0.09/1.2]?=-99 Uncertainty on 4.5mag |
| 1704- 1713 | F10.6        | mag          | Zpmag           | [10.5/28.5]?=-99 Forced photometry in                                        |
| 1715- 1724 | F10.6        | mag          | e_Zpmag         | [0.09/7.3]?=-99 Uncertainty on Zpmag                                         |
| 1726- 1735 | F10.6        | mag          | Ypmag           | [10/26]?=-99 Forced photometry in VIDEO                                      |
| 1737- 1746 | F10.6        | mag          | e_Ypmag         | [0.09/0.8]?=-99 Uncertainty on Ypmag                                         |
| 1748- 1757 | F10.6        | mag          | Jpmag           | [10.7/28.5]?=-99 Forced photometry in                                        |
| 1759- 1768 | F10.6        | mag          | e_Jpmag         | [0.09/3.6]?=-99 Uncertainty on Jpmag                                         |
| 1770- 1779 | F10.6        | mag          | Hpmag           | [10.9/25]?=-99 Forced photometry in VIDEO                                    |
| 1781- 1790 | F10.6        | mag          | e_Hpmag         | [0.09/0.5]?=-99 Uncertainty on Hpmag                                         |
| 1792- 1801 | F10.6        | mag          | Kspmag          | [10.8/27.8]?=-99 Forced photometry in                                        |
| 1803- 1812 | F10.6        | mag          | e_Kspmag        | [0.09/2.8]?=-99 Uncertainty on Kspmag                                        |
| 1814- 1823 | F10.6        | mag          | gmagFP          | [15.2/30.2]?=-99 Forced photometry in HSC                                    |
| 1825- 1834 | F10.6        | mag          | e_gmagFP        | [0.09/19.4]?=-99 Uncertainty on gmagFP                                       |
| 1836- 1845 | F10.6        | mag          | rmagFP          | [14.4/30]?=-99 Forced photometry in HSC r                                    |
| 1847- 1856 | F10.6        | mag          | e_rmagFP        | [0.09/38]?=-99 Uncertainty on rmagFP                                         |
| 1858- 1867 | F10.6        | mag          | imagFP          | [15.4/27.3]?=-99 Forced photometry in HSC                                    |
| 1869- 1878 | F10.6        | mag          | e_imagFP        | [0.09/2.1]?=-99 Uncertainty on imagFP                                        |
| 1880- 1889 | F10.6        | mag          | zmagFP          | [13.7/26.5]?=-99 Forced photometry in HSC                                    |
| 1891- 1900 | F10.6        | mag          | e_zmagFP        | [0.09/2.6]?=-99 Uncertainty on zmagFP                                        |
| 1902- 1911 | F10.6        | mag          | umagV           | [9.9/34.6]?=-99 Forced photometry in                                         |
| 1913- 1924 | F12.6        | mag          | e_umagV         | [0.09/1705]?=-99 Uncertainty on umagV                                        |
| 1926- 1935 | F10.6        | mag          | gmagV           | [11/31]?=-99 Forced photometry in VOICE                                      |
| 1937- 1946 | F10.6        | mag          | e_gmagV         | [0.09/64.1]?=-99 Uncertainty on gmagV                                        |
| 1948- 1957 | F10.6        | mag          | rmagV           | [10.9/30.3]?=-99 Forced photometry in                                        |
| 1959- 1968 | F10.6        | mag          | e_rmagV         | [0.09/41]?=-99 Uncertainty on rmagV                                          |
| 1970- 1979 | F10.6        | mag          | imagV           | [10.6/30]?=-99 Forced photometry in VOICE                                    |
| 1981- 1990 | F10.6        | mag          | e_imagV         | [0.09/69.6]?=-99 Uncertainty on imagV                                        |
| 1992- 2001 | F10.6        | ---          | zsp             | [0.00015/4.6]?=-99 Spectroscopic redshift                                    |
| 2003- 2005 | I3           | ---          | zCl             | [-1/1]?=-99 Spectroscopic classification                                     |
| 2007- 2009 | I3           | ---          | q_zsp           | [2/6]?=-99 Spectroscopic quality flag                                        |
| 2011- 2021 | F11.6        | deg          | RAzsdeg         | [51.6/54.5]?=-99 Right ascension (J2000)                                     |
| 2023- 2033 | F11.6        | deg          | DEzsdeg         | [-29/-27]?=-99 Declination (J2000.0) of                                      |
| 2035- 2041 | A7           | ---          | r_zsp           | The spectroscopic catalog that                                               |
| 2043- 2047 | F5.1         | ---          | Fsed            | [0/1]?=-99 Flag for BL AGN candidates                                        |
| 2049- 2058 | F10.6        | deg          | RAspdeg         | [51.6/54.5]? Right ascension (J2000.0)                                       |
| 2060- 2070 | F11.6        | deg          | DEzpdeg         | [-29/-26]? Declination (J2000.0) of the                                      |
| 2072- 2079 | F8.4         | ---          | zphot           | [0.01/4.5]?=-99 Suggested photometric                                        |
| 2081- 2087 | F7.3         | ---          | zpEazy          | [0.01/6]?=-99 Photometric redshift                                           |
| 2089- 2096 | F8.3         | ---          | E_zpEazy        | [-0.9/3.8]? Upper uncertainty of                                             |
| 2098- 2105 | F8.3         | ---          | e_zpEazy        | [-0.05/4]? Lower uncertainty of                                              |
| 2107- 2126 | F20.6        | ---          | q_zpEazy        | [-99/398127000000]? Quality of                                               |
| 2128- 2135 | F8.4         | ---          | zpLP            | [0.02/6]?=-99 Photometric redshift                                           |
| 2137- 2144 | F8.4         | ---          | E_zpLP          | [0/5.4]?=-99 Upper uncertainty of                                            |
| 2146- 2153 | F8.4         | ---          | e_zpLP          | [0/3.3]?=-99 Lower uncertainty of                                            |
| 2155       | I1           | ---          | Fagn            | [0/1] Flag for AGNs identified (1=AGN;                                       |
| 3129       | occurrences) | (AGN_FLAG)   | 2157-           | 2159 I3     ---       Fstar      [0/1]?=-99 Flag for stars identified        |
| 169        | occurrences) | (STAR_FLAG)  | Note            | (1): Catalog origin of the nearest Chandra source as follows:                |
| 1          | =            | the          | CDF-S           | catalog (Luo+ 2017, J/ApJS/228/2J)                                           |
| 2          | =            | the          | E-CDF-S         | catalog (Xue+ 2016, J/ApJS/224/15)                                           |
| 3          | =            | the          | CSC             | 2.0 catalog (Evans+ 2010ApJS..189...37E ; Cat. IX/57)                        |
| 1          | =            | BL           | AGNs            | (280 occurrences)                                                            |
| 0          | =            | galaxies     | or              | non-BL AGNs (491 occurrences)                                                |
| 1          | =            | stars        | (1              | occurrence)                                                                  |
| 273        | (406         | occurrences) | PRIMUS          | = The PRIsm MUlti-object Survey (Coil+ 2011ApJ...741....8C ;                 |
| 252        | occurrences) | ATLAS        | =               | The Australia Telescope Large Area Survey                                    |
| 2015       | ;            | 97           | occurrences)    | S+10   = Silverman+ 2010, J/ApJS/191/124 (70 occurrences)                    |
| 2116       | ;            | 61           | occurrences)    | 2dfGRS = The 2dF Galaxy Redshift Survey (Cat. VII/250 ; 5 occurrences)       |
| 259        | ;            | 4            | occurrences)    | HELP   = HELP database (Shirley+ 2019MNRAS.490..634S ; 3 occurrences)        |
| 0          | =            | sources      | that            | are classified as BL AGN candidates by two different                         |
| 424        | occurrences) | 0.5          | =               | sources identified as BL AGN candidates using one method but not the         |
| 625        | occurrences) | 0.0          | =               | sources identified as non-BL AGNs by both methods (1539 occurrences)         |

**Note**: Catalog origin of the nearest Chandra source as follows:
  1 = the CDF-S catalog (Luo+ 2017, J/ApJS/228/2J)
  2 = the E-CDF-S catalog (Xue+ 2016, J/ApJS/224/15)
  3 = the CSC 2.0 catalog (Evans+ 2010ApJS..189...37E ; Cat. IX/57)
Note (2): Spectroscopic classification of the source as follows:
   1 = BL AGNs (280 occurrences)
   0 = galaxies or non-BL AGNs (491 occurrences)
  -1 = stars (1 occurrence)
Note (3): Spectroscopic catalog as follows:
 OzDES  = see DR1: Childress+, 2017, J/MNRAS/472/273 (406 occurrences)
 PRIMUS = The PRIsm MUlti-object Survey (Coil+ 2011ApJ...741....8C ;
           252 occurrences)
 ATLAS  = The Australia Telescope Large Area Survey
           (Franzen+ 2015 ; 97 occurrences)
 S+10   = Silverman+ 2010, J/ApJS/191/124 (70 occurrences)
 ACES   = The Arizona CDFS Environment Survey (Cooper+, 2012, J/MNRAS/425/2116 ;
           61 occurrences)
 2dfGRS = The 2dF Galaxy Redshift Survey (Cat. VII/250 ; 5 occurrences)
 6df    = The 6dF galaxy survey (Cat. VII/259 ; 4 occurrences)
 HELP   = HELP database (Shirley+ 2019MNRAS.490..634S ; 3 occurrences)
Note (4): Flag for broad-line (BL) AGN candidates as follows:
 1.0 = sources that are classified as BL AGN candidates by two different
        methods (424 occurrences)
 0.5 = sources identified as BL AGN candidates using one method but not the
        other (625 occurrences)
 0.0 = sources identified as non-BL AGNs by both methods (1539 occurrences)

</details>

<details>
<summary>table7.dat</summary>

| Bytes      | Format       | Units        | Label           | Explanations                                                                   |
|:-----------|:-------------|:-------------|:----------------|:-------------------------------------------------------------------------------|
| 1- 2       | A2           | ---          | Field           | [ES] ELAIS-S1 field ("ES")                                                     |
| 3- 6       | I04          | ---          | ES              | [0/2629] The source ID of each X-ray                                           |
| 1          | field        | (XID)        | 8-              | 16 F9.6   deg       RAdeg       [8/10.6] Right ascension (J2000.0)             |
| 18- 27     | F10.6        | deg          | DEdeg           | [-44.9/-42.8] Declination (J2000.0)                                            |
| 29- 36     | F8.6         | arcsec       | eXPos           | [0.04/4.4] X-ray positional                                                    |
| 38- 45     | F8.6         | arcsec       | R68             | [0.07/6.7] The 68% positional-                                                 |
| 47- 55     | F9.6         | arcsec       | R99             | [0.16/15] The 99.73%                                                           |
| 57- 65     | F9.6         | arcsec       | eEMPos          | [0.05/13.18] Positional uncertainty                                            |
| 67- 76     | F10.6        | deg          | RASBdeg         | [8/10.6]?=-99 Right ascension (J2000.0)                                        |
| 78- 87     | F10.6        | deg          | DESBdeg         | [-45/-42.8]?=-99 Declination (J2000.0)                                         |
| 89- 98     | F10.6        | deg          | RAHBdeg         | [8.1/10.6]?=-99 Right ascension                                                |
| 100- 109   | F10.6        | deg          | DEHBdeg         | [-45/-42.9]?=-99 Declination (J2000.0)                                         |
| 111- 120   | F10.6        | deg          | RAFBdeg         | [8/10.6]?=-99 Right ascension (J2000.0)                                        |
| 122- 131   | F10.6        | deg          | DEFBdeg         | [-45/-42.8]?=-99 Declination (J2000.0)                                         |
| 133- 146   | F14.6        | ---          | detSB           | [4/108359]?=-99 The emldetect                                                  |
| 148- 159   | F12.6        | ---          | detHB           | [8/5354]?=-99 The emldetect                                                    |
| 161- 174   | F14.6        | ---          | detFB           | [4/113691]?=-99 The emldetect                                                  |
| 176- 185   | F10.3        | s            | ExpSB           | [2357/197488] Total (PN+MOS1+MOS2)                                             |
| 187- 196   | F10.3        | s            | ExpHB           | [2807/186467] Total (PN+MOS1+MOS2)                                             |
| 198- 207   | F10.3        | s            | ExpFB           | [2259/197427] Total (PN+MOS1+MOS2)                                             |
| 209- 217   | F9.3         | s            | PNExpSB         | [1972/65089]?=0 PN exposure time in the                                        |
| 219- 227   | F9.3         | s            | M1ExpSB         | [2788/68139]?=0 MOS1 exposure time in                                          |
| 229- 237   | F9.3         | s            | M2ExpSB         | [2540/70852]?=0 MOS2 exposure time in                                          |
| 239- 247   | F9.3         | s            | PNExpHB         | [1280/57452]?=0 PN exposure time in the                                        |
| 249- 257   | F9.3         | s            | M1ExpHB         | [395/67355]?=0 MOS1 exposure time in the                                       |
| 259- 267   | F9.3         | s            | M2ExpHB         | [155/67353]?=0 MOS2 exposure time in the                                       |
| 269- 277   | F9.3         | s            | PNExpFB         | [1677/65029]?=0 PN exposure time in                                            |
| 279- 287   | F9.3         | s            | M1ExpFB         | [478/68177]?=0 MOS1 exposure time in the                                       |
| 289- 297   | F9.3         | s            | M2ExpFB         | [2539/70018]?=0 MOS2 exposure time in                                          |
| 299- 307   | F9.6         | ct/pix       | BkgSB           | [0.06/4.3]?=99 Total background-map                                            |
| 309- 317   | F9.6         | ct/pix       | BkgHB           | [0.17/4.1]?=99 Total background-map                                            |
| 319- 327   | F9.6         | ct/pix       | BkgFB           | [0.06/7.1]?=99 Total background-map                                            |
| 329- 336   | F8.6         | ct/pix       | PNBkgSB         | [0.0002/3.1] PN background-map value                                           |
| 338- 344   | E7.2         | ct/pix       | M1BkgSB         | [9.4e-05/1.1] MOS1 background-map value                                        |
| 346- 353   | F8.6         | ct/pix       | M2BkgSB         | [0.0002/1.2] MOS2 background-map value                                         |
| 355- 361   | E7.2         | ct/pix       | PNBkgHB         | [6.3e-05/2.2] PN background-map value                                          |
| 363- 369   | E7.2         | ct/pix       | M1BkgHB         | [6.3e-05/0.9] MOS1 background-map value                                        |
| 371- 377   | E7.2         | ct/pix       | M2BkgHB         | [9.4e-05/1.1] MOS2 background-map value                                        |
| 379- 386   | F8.6         | ct/pix       | PNBkgFB         | [0.0002/3.8] PN background-map value                                           |
| 388- 394   | E7.2         | ct/pix       | M1BkgFB         | [9.4e-05/2] MOS1 background-map value                                          |
| 396- 403   | F8.6         | ct/pix       | M2BkgFB         | [0.0002/2.2] MOS2 background-map value                                         |
| 405- 416   | F12.6        | ct           | CtsSB           | [8/29041] Total (PN+MOS1+MOS2) net                                             |
| 418- 428   | F11.6        | ct           | CtsHB           | [16/2258] Total (PN+MOS1+MOS2) net                                             |
| 430- 441   | F12.6        | ct           | CtsFB           | [7/31299] Total (PN+MOS1+MOS2) net                                             |
| 443- 455   | F13.6        | ct           | PNCtsSB         | [0/17844]?=-99 PN net counts in the                                            |
| 457- 468   | F12.6        | ct           | M1CtsSB         | [0/5802]?=-99 MOS1 net counts in the                                           |
| 470- 481   | F12.6        | ct           | M2CtsSB         | [0/5396]?=-99 MOS2 net counts in the                                           |
| 483- 493   | F11.6        | ct           | PNCtsHB         | [0/888]?=-99 PN net counts in the hard                                         |
| 495- 505   | F11.6        | ct           | M1CtsHB         | [0/695]?=-99 MOS1 net counts in the                                            |
| 507- 517   | F11.6        | ct           | M2CtsHB         | [0/675]?=-99 MOS2 net counts in the                                            |
| 519- 531   | F13.6        | ct           | PNCtsFB         | [0/18732]?=-99 PN net counts in the                                            |
| 533- 544   | F12.6        | ct           | M1CtsFB         | [0/6497]?=-99 MOS1 net counts in the                                           |
| 546- 557   | F12.6        | ct           | M2CtsFB         | [0/6071]?=-99 MOS2 net counts in the                                           |
| 559- 570   | F12.6        | ct           | e_CtsSB         | [3.9/8661]?=-99 Uncertainty on CtsSB                                           |
| 572- 584   | F13.6        | ct           | e_CtsHB         | [5.9/10472]?=-99 Uncertainty on CtsHB                                          |
| 586- 598   | F13.6        | ct           | e_CtsFB         | [6.5/15847]?=-99 Uncertainty on CtsFB                                          |
| 600- 611   | F12.6        | ct           | e_PNCtsSB       | [0/8661]?=-99 Uncertainty on PNCtsSB                                           |
| 613- 624   | F12.6        | ct           | e_M1CtsSB       | [0/8141]?=-99 Uncertainty on M1CtsSB                                           |
| 626- 635   | F10.6        | ct           | e_M2CtsSB       | [0/77]?=-99 Uncertainty on M2CtsSB                                             |
| 637- 649   | F13.6        | ct           | e_PNCtsHB       | [0/10472]?=-99 Uncertainty on PNCtsHB                                          |
| 651- 660   | F10.6        | ct           | e_M1CtsHB       | [0/30]?=-99 Uncertainty on M1CtsHB                                             |
| 662- 671   | F10.6        | ct           | e_M2CtsHB       | [0/30]?=-99 Uncertainty on M2CtsHB                                             |
| 673- 685   | F13.6        | ct           | e_PNCtsFB       | [0/13811]?=-99 Uncertainty on PNCtsFB                                          |
| 687- 696   | F10.6        | ct           | e_M1CtsFB       | [0/85]?=-99 Uncertainty on M1CtsFB                                             |
| 698- 710   | F13.6        | ct           | e_M2CtsFB       | [0/15847]?=-99 Uncertainty on M2Cts                                            |
| 712- 721   | F10.8        | ct/s         | CRtSB           | [0.0003/1.11] Total (PN+MOS1+MOS2) net                                         |
| 723- 732   | F10.8        | ct/s         | CRtHB           | [0.0005/0.1] Total (PN+MOS1+MOS2) net                                          |
| 734- 743   | F10.8        | ct/s         | CRtFB           | [0.0003/1.21] Total (PN+MOS1+MOS2) net                                         |
| 745- 753   | E9.4         | ct/s         | PNCRtSB         | [0/0.8]?=99 PN net count rates in the                                          |
| 755- 763   | E9.4         | ct/s         | M1CRtSB         | [0/0.2]?=99 MOS1 net count rates in the                                        |
| 765- 773   | E9.4         | ct/s         | M2CRtSB         | [0/0.2]?=99 MOS2 net count rates in the                                        |
| 775- 783   | E9.4         | ct/s         | PNCRtHB         | [0/0.05]?=99 PN net count rates in the                                         |
| 785- 793   | E9.4         | ct/s         | M1CRtHB         | [0/0.03]?=99 MOS1 net count rates in                                           |
| 795- 803   | E9.4         | ct/s         | M2CRtHB         | [0/0.03]?=99 MOS2 net count rates in                                           |
| 805- 813   | E9.4         | ct/s         | PNCRtFB         | [0/0.8]?=99 PN net count rates in the                                          |
| 815- 823   | E9.4         | ct/s         | M1CRtFB         | [0/0.3]?=99 MOS1 net count rates in the                                        |
| 825- 833   | E9.4         | ct/s         | M2CRtFB         | [0/0.2]?=99 MOS2 net count rates in the                                        |
| 835- 845   | F11.8        | ct/s         | e_CRtSB         | [0.0002/1.6]?=99  Uncertainty in CRtSB                                         |
| 847- 857   | F11.8        | ct/s         | e_CRtHB         | [0.0002/1]?=99  Uncertainty in CRtHB                                           |
| 859- 869   | F11.8        | ct/s         | e_CRtFB         | [0.0003/1.7]?=99  Uncertainty in CRtFB                                         |
| 871- 881   | F11.8        | ct/s         | e_PNCRtSB       | [0/0.4]?=99  Uncertainty in PNCRtSB                                            |
| 883- 891   | E9.4         | ct/s         | e_M1CRtSB       | [0/1.6]?=99 Uncertainty in M1CRtSB                                             |
| 893- 901   | E9.4         | ct/s         | e_M2CRtSB       | [0/0.004]?=99 Uncertainty in M2CRtSB                                           |
| 903- 913   | F11.8        | ct/s         | e_PNCRtHB       | [0/0.93]?=99  Uncertainty in PNCRtHB                                           |
| 915- 923   | E9.4         | ct/s         | e_M1CRtHB       | [0/0.004]?=99 Uncertainty in M1CRtHB                                           |
| 925- 933   | E9.4         | ct/s         | e_M2CRtHB       | [0/0.004]?=99 Uncertainty in M2CRtHB                                           |
| 935- 945   | F11.8        | ct/s         | e_PNCRtFB       | [0/0.7]?=99  Uncertainty in PNCRtFB                                            |
| 947- 957   | F11.8        | ct/s         | e_M1CRtFB       | [0/0.005]?=99  Uncertainty in M1CRtFB                                          |
| 959- 967   | E9.4         | ct/s         | e_M2CRtFB       | [0/1.7]?=99 Uncertainty in M2CRtFB                                             |
| 969- 974   | F6.3         | ---          | BR              | [0.01/29.62] Total hard-to-soft band                                           |
| 976- 981   | F6.3         | ---          | e_BR            | [0.002/13.4]?=99 Uncertainty in BR                                             |
| 983- 988   | F6.3         | ---          | PNBR            | [0.02/6.1]?=99 PN hard-to-soft band                                            |
| 990- 995   | F6.3         | ---          | e_PNBR          | [0.003/24.3]?=99 Uncertainty in PNBR                                           |
| 997- 1002  | F6.3         | ---          | M1BR            | [0.03/99] MOS1 hard-to-soft band ratio                                         |
| 1004- 1010 | F7.3         | ---          | e_M1BR          | [0.006/619.1] Uncertainty in M1BR                                              |
| 1012- 1017 | F6.3         | ---          | M2BR            | [0.029/22.5]?=99 MOS2 hard-to-soft band                                        |
| 1019- 1024 | F6.3         | ---          | e_M2BR          | [0.006/58.5]?=99 Uncertainty in M2BR                                           |
| 1026- 1031 | F6.3         | ---          | HR              | [-0.98/0.94] Hardness ratio                                                    |
| 1033- 1039 | F7.3         | ---          | e_HR            | [-2/14]?=-99 Uncertainty in HR (HR_ERR)                                        |
| 1041- 1044 | F4.1         | ---          | Gamma           | [-1/2.9] The effective power-law                                               |
| 1046- 1056 | F11.8        | fW/m2        | F0.5-2keV       | [0.0004/0.7]?=99 Apparent flux in the                                          |
| 1058- 1068 | F11.8        | fW/m2        | e_F0.5-2keV     | [0.0001/0.009]?=99 Uncertainty in                                              |
| 1070- 1080 | F11.8        | fW/m2        | F2-10keV        | [0.005/0.5]?=99 Apparent flux in the                                           |
| 1082- 1092 | F11.8        | fW/m2        | e_F2-10keV      | [0.001/0.05]?=99 Uncertainty in F2-10keV                                       |
| 1094- 1104 | F11.8        | fW/m2        | F0.5-10keV      | [0.001/1.2]?=99 Apparent flux in the                                           |
| 1106- 1116 | F11.8        | fW/m2        | e_F0.5-10keV    | [0.0004/0.04]?=99 Uncertainty in                                               |
| 1118- 1123 | F6.2         | [10-7W]      | LX              | [35/45.52]?=-99 Log rest-frame apparent                                        |
| 1125- 1127 | I3           | ---          | CCat            | [3]?=-99 The catalog origin of the                                             |
| 1129- 1150 | A22          | ---          | CID             | Source ID in the matched Chandra                                               |
| 1152- 1161 | F10.6        | deg          | RACdeg          | [8.2/10.52]?=-99 Right ascension                                               |
| 1163- 1172 | F10.6        | deg          | DECdeg          | [-44.4/-42.92]?=-99 Declination (J2000)                                        |
| 1174- 1183 | F10.6        | ---          | Pany            | [0.1/1]?=-99 The posterior probability                                         |
| 1185- 1194 | F10.6        | ---          | Pi              | [0.2/1]?=-99 The relative probability of                                       |
| 1          | counterpart  | to           | be              | the correct match                                                              |
| 1196       | I1           | ---          | F2              | [0/1] Warning flag for sources where a                                         |
| 1198- 1207 | F10.6        | deg          | RAIRdeg         | [8.1/10.6]?=-99 Right ascension (J2000)                                        |
| 1209- 1218 | F10.6        | deg          | DEIRdeg         | [-45/-42.8]?=-99 Declination (J2000) of                                        |
| 1220- 1229 | F10.6        | deg          | RAVdeg          | [8.4/10.6]?=-99 Right ascension (J2000)                                        |
| 1231- 1240 | F10.6        | deg          | DEVdeg          | [-45/-42.8]?=-99 Declination (J2000)                                           |
| 1242- 1251 | F10.6        | deg          | RADdeg          | [8/10.6]?=-99 Right ascension (J2000)                                          |
| 1253- 1262 | F10.6        | deg          | DEDdeg          | [-45/-42.8]?=-99 Declination (J2000)                                           |
| 1264- 1273 | F10.6        | arcsec       | SepIRAC         | [0.02/9.9]?=-99 Separation of the X-ray                                        |
| 1275- 1284 | F10.6        | arcsec       | SepVIDEO        | [0.02/9.8]?=-99 Separation of the X-ray                                        |
| 1286- 1295 | F10.6        | arcsec       | SepDES          | [0.01/9.9]?=-99 Separation of the X-ray                                        |
| 1297- 1305 | F9.6         | mag          | 3.6magAp        | [13.56/23]?=99 1.9 arcsec aperture                                             |
| 6          | micron       | band         | reported        | in the DeepDrill catalog                                                       |
| 1307- 1315 | F9.6         | mag          | e_3.6magAp      | [0.001/0.3]?=99 Uncertainty in 3.6magAp                                        |
| 1317- 1325 | F9.6         | mag          | 4.5magAp        | [13.32/22.9]?=99 1.9 arcsec aperture                                           |
| 5          | micron       | band         | reported        | in the DeepDrill catalog                                                       |
| 1327- 1335 | F9.6         | mag          | e_4.5magAp      | [0.002/0.3]?=99 Uncertainty in 4.5magAp                                        |
| 1337- 1345 | F9.6         | mag          | Zapc3           | [12.13/28.3]?=99 VIDEO 2 arcsec aperture                                       |
| 1347- 1353 | E7.2         | mag          | e_Zapc3         | Uncertainty in Zapc3 (VIDEO_Z_MAG_ERR)                                         |
| 1355- 1363 | F9.6         | mag          | Yapc3           | [11.34/25.5]?=99 VIDEO 2 arcsec aperture                                       |
| 1365- 1371 | E7.2         | mag          | e_Yapc3         | Uncertainty in Yapc3 (VIDEO_Y_MAG_ERR)                                         |
| 1373- 1381 | F9.6         | mag          | Japc3           | [12.07/25.4]?=99 VIDEO 2 arcsec aperture                                       |
| 1383- 1389 | E7.2         | mag          | e_Japc3         | Uncertainty in Japc3 (VIDEO_J_MAG_ERR)                                         |
| 1391- 1399 | F9.6         | mag          | Hapc3           | [12.05/24.7]?=99 VIDEO 2 arcsec aperture                                       |
| 1401- 1407 | E7.2         | mag          | e_Hapc3         | Uncertainty in Hapc3 (VIDEO_H_MAG_ERR)                                         |
| 1409- 1417 | F9.6         | mag          | Ksapc3          | [11.91/23.8]?=99 VIDEO 2 arcsec aperture                                       |
| 1419- 1425 | E7.2         | mag          | e_Ksapc3        | Uncertainty in Ksapc3 (VIDEO_KS_MAG_ERR)                                       |
| 1427- 1435 | F9.6         | mag          | gmagDES         | [11.45/29.51]?=99 DES Kron photometry in                                       |
| 1437- 1443 | E7.2         | mag          | e_gmagDES       | Uncertainty in gmagDES (DES_G_MAG_ERR)                                         |
| 1445- 1453 | F9.6         | mag          | rmagDES         | [11.43/29.5]?=99 DES Kron photometry in                                        |
| 1455- 1461 | E7.2         | mag          | e_rmagDES       | Uncertainty in rmagDES (DES_R_MAG_ERR)                                         |
| 1463- 1471 | F9.6         | mag          | imagDES         | [11.52/27.5]?=99 DES Kron photometry in                                        |
| 1473- 1479 | E7.2         | mag          | e_imagDES       | Uncertainty in imagDES (DES_I_MAG_ERR)                                         |
| 1481- 1489 | F9.6         | mag          | zmagDES         | [10.93/27.1]?=99 DES Kron photometry in                                        |
| 1491- 1497 | E7.2         | mag          | e_zmagDES       | Uncertainty in zmagDES (DES_Z_MAG_ERR)                                         |
| 1499- 1507 | F9.6         | mag          | YmagDES         | [9.4/29.2]?=99 DES Kron photometry in                                          |
| 1509- 1515 | E7.2         | mag          | e_YmagDES       | Uncertainty in YmagDES (DES_Y_MAG_ERR)                                         |
| 1517- 1528 | I12          | ---          | Tractor         | The object ID of the VIDEO counterpart                                         |
| 1530- 1539 | F10.6        | mag          | 3.6mag          | [14.5/24.02]?=-99 Forced photometry in                                         |
| 6          | micron       | band         | (IRAC_1_FP_MAG) | 1541- 1550 F10.6  mag     e_3.6mag      [0.09/0.58]?=-99 Uncertainty in 3.6mag |
| 1552- 1561 | F10.6        | mag          | 4.5mag          | [14.7/25.48]?=-99 Forced photometry in                                         |
| 5          | micron       | band         | (IRAC_2_FP_MAG) | 1563- 1572 F10.6  mag     e_4.5mag      [0.09/0.82]?=-99 Uncertainty in 4.5mag |
| 1574- 1583 | F10.6        | mag          | Zpmag           | [13.8/27.23]?=-99 Forced photometry in                                         |
| 1585- 1594 | F10.6        | mag          | e_Zpmag         | [0.09/1.1]?=-99 Uncertainty in Zpmag                                           |
| 1596- 1605 | F10.6        | mag          | Ypmag           | [13.4/26.48]?=-99 Forced photometry in                                         |
| 1607- 1616 | F10.6        | mag          | e_Ypmag         | [0.09/1.05]?=-99 Uncertainty in Ypmag                                          |
| 1618- 1627 | F10.6        | mag          | Jpmag           | [14.1/27.68]?=-99 Forced photometry in                                         |
| 1629- 1638 | F10.6        | mag          | e_Jpmag         | [0.09/0.43]?=-99 Uncertainty in Jpmag                                          |
| 1640- 1649 | F10.6        | mag          | Hpmag           | [14/25.38]?=-99 Forced photometry in                                           |
| 1651- 1660 | F10.6        | mag          | e_Hpmag         | [0.09/0.24]?=-99 Uncertainty in Hpmag                                          |
| 1662- 1671 | F10.6        | mag          | Kspmag          | [14/24.94]?=-99 Forced photometry in                                           |
| 1673- 1682 | F10.6        | mag          | e_Kspmag        | [0.09/1.18]?=-99 Uncertainty in Kspmag                                         |
| 1684- 1693 | F10.6        | mag          | gmag            | [14.5/31.78]?=-99 Forced photometry in                                         |
| 1695- 1704 | F10.6        | mag          | e_gmag          | [0.08/92.45]?=-99 Uncertainty in gmag                                          |
| 1706- 1715 | F10.6        | mag          | rmag            | [13.6/28.99]?=-99 Forced photometry in                                         |
| 1717- 1726 | F10.6        | mag          | e_rmag          | [0.08/9.33]?=-99 Uncertainty in rmag                                           |
| 1728- 1737 | F10.6        | mag          | imag            | [13.2/27.31]?=-99 Forced photometry in                                         |
| 1739- 1748 | F10.6        | mag          | e_imag          | [0.08/6.38]?=-99 Uncertainty in imag                                           |
| 1750- 1759 | F10.6        | mag          | zmag            | [13/28.42]?=-99 Forced photometry in DES                                       |
| 1761- 1770 | F10.6        | mag          | e_zmag          | [0.08/18.22]?=-99 Uncertainty in zmag                                          |
| 1772- 1781 | F10.6        | mag          | Ymag            | [12.9/30.53]?=-99 Forced photometry in                                         |
| 1783- 1793 | F11.6        | mag          | e_Ymag          | [0.08/578.83]?=-99 Uncertainty in Ymag                                         |
| 1795- 1804 | F10.6        | mag          | Bmag            | [14.5/28.99]?=-99 Forced photometry in                                         |
| 1806- 1815 | F10.6        | mag          | e_Bmag          | [0.08/12.26]?=-99 Uncertainty in Bmag                                          |
| 1817- 1826 | F10.6        | mag          | Vmag            | [14.4/31.64]?=-99 Forced photometry in                                         |
| 1828- 1838 | F11.6        | mag          | e_Vmag          | [0.08/121.36]?=-99 Uncertainty in Vmag                                         |
| 1840- 1849 | F10.6        | mag          | Rmag            | [14.3/29.54]?=-99 Forced photometry in                                         |
| 1851- 1860 | F10.6        | mag          | e_Rmag          | [0.08/42.77]?=-99 Uncertainty in Rmag                                          |
| 1862- 1871 | F10.6        | mag          | umagV           | [11/31.35]?=-99 Forced photometry in                                           |
| 1873- 1883 | F11.6        | mag          | e_umagV         | [0.09/103.33]?=-99 Uncertainty in umagV                                        |
| 1885- 1894 | F10.6        | ---          | zsp             | [0.00013/4.05]?=-99 Spectroscopic                                              |
| 1896- 1898 | I3           | ---          | zCl             | [-1/1]?=-99 Spectroscopic classification                                       |
| 1900- 1902 | I3           | ---          | q_zsp           | [1/128]?=-99 Spectroscopic quality flag                                        |
| 1904- 1913 | F10.6        | deg          | RAzsdeg         | [8.14/10.53]?=-99 Right ascension                                              |
| 1915- 1924 | F10.6        | deg          | DEzsdeg         | [-45/-42.89]?=-99 Declination (J2000.0)                                        |
| 1926- 1932 | A7           | ---          | r_zsp           | The spectroscopic catalog that                                                 |
| 1934- 1938 | F5.1         | ---          | Fsed            | [0/1]?=-99 Flag for BL AGN candidates                                          |
| 1940- 1949 | F10.6        | deg          | RAzpdeg         | [8.4/10.53]?=-99 Right ascension                                               |
| 1951- 1960 | F10.6        | deg          | DEzpdeg         | [-45/-42.87]?=-99 Declination (J2000.0)                                        |
| 1962- 1969 | F8.4         | ---          | zphot           | [0.01/4.27]?=-99 Suggested photometric                                         |
| 1971- 1977 | F7.3         | ---          | zpEazy          | [0.01/5.97]?=-99 Photometric redshift                                          |
| 1979- 1985 | F7.3         | ---          | E_zpEazy        | [-0.7/3.35]?=-99 Upper uncertainty of                                          |
| 1987- 1993 | F7.3         | ---          | e_zpEazy        | [-0.02/3.29]?=-99 Lower uncertainty of                                         |
| 1995- 2012 | F18.6        | ---          | q_zpEazy        | [0.008/5450440000]?=-99 Quality of                                             |
| 2014- 2021 | F8.4         | ---          | zpLP            | [0.1/4.27]?=-99 Photometric redshift                                           |
| 2023- 2030 | F8.4         | ---          | E_zpLP          | [0.005/2.11]?=-99 Upper uncertainty of                                         |
| 2032- 2039 | F8.4         | ---          | e_zpLP          | [0.005/2.45]?=-99 Lower uncertainty of                                         |
| 2041       | I1           | ---          | Fagn            | [0/1] Flag for AGNs identified (1=AGN;                                         |
| 1957       | occurrences) | (AGN_FLAG)   | 2043-           | 2045 I3     ---       Fstar       [0/1]?=-99 Flag for stars identified         |
| 92         | occurrences) | (STAR_FLAG)  | Note            | (1): Catalog origin of the nearest Chandra source as follows:                  |
| 1          | =            | the          | CDF-S           | catalog (Luo+ 2017, J/ApJS/228/2)                                              |
| 2          | =            | the          | E-CDF-S         | catalog (Xue+ 2016, J/ApJS/224/15)                                             |
| 3          | =            | the          | CSC             | 2.0 catalog (Evans+ 2010ApJS..189...37E ; Cat. IX/57)                          |
| 1          | =            | BL           | AGNs            | (208 occurrences)                                                              |
| 0          | =            | galaxies     | or              | non-BL AGNs (369 occurrences)                                                  |
| 1          | =            | stars        | (1              | occurrence)                                                                    |
| 273        | (293         | occurrences) | PRIMUS          | = The PRIsm MUlti-object Survey (Coil+ 2011ApJ...741....8C ;                   |
| 123        | occurrences) | Fer          | =               | Feruglio+ 2008, J/A+A/488/417 (106 occurrences)                                |
| 2015       | ;            | 30           | occurrences)    | sacchi = Sacchi+, 2009, J/ApJ/703/1778 (22 occurrences)                        |
| 259        | ;            | 6            | occurrences)    | HELP   = HELP database (Shirley+ 2019MNRAS.490..634S ; 4 occurrences)          |
| 250        | ;            | 1            | occurrence)     | Note (4): Flag for broad-line (BL) AGN candidates as follows:                  |
| 0          | =            | sources      | that            | are classified as BL AGN candidates by two different                           |
| 221        | occurrences) | 0.5          | =               | sources identified as BL AGN candidates using one method but not the           |
| 354        | occurrences) | 0.0          | =               | sources identified as non-BL AGNs by both methods (913 occurrences)            |

**Note**: Catalog origin of the nearest Chandra source as follows:
  1 = the CDF-S catalog (Luo+ 2017, J/ApJS/228/2)
  2 = the E-CDF-S catalog (Xue+ 2016, J/ApJS/224/15)
  3 = the CSC 2.0 catalog (Evans+ 2010ApJS..189...37E ; Cat. IX/57)
Note (2): Spectroscopic classification of the source as follows:
   1 = BL AGNs (208 occurrences)
   0 = galaxies or non-BL AGNs (369 occurrences)
  -1 = stars (1 occurrence)
Note (3): Spectroscopic catalog as follows:
 OzDES  = see DR1: Childress+, 2017, J/MNRAS/472/273 (293 occurrences)
 PRIMUS = The PRIsm MUlti-object Survey (Coil+ 2011ApJ...741....8C ;
           123 occurrences)
 Fer    = Feruglio+ 2008, J/A+A/488/417 (106 occurrences)
 ATLAS  = The Australia Telescope Large Area Survey
           (Franzen+ 2015 ; 30 occurrences)
 sacchi = Sacchi+, 2009, J/ApJ/703/1778 (22 occurrences)
 6df    = The 6dF galaxy survey (Cat. VII/259 ; 6 occurrences)
 HELP   = HELP database (Shirley+ 2019MNRAS.490..634S ; 4 occurrences)
 2dfGRS = The 2dF Galaxy Redshift Survey (Cat. VII/250 ; 1 occurrence)
Note (4): Flag for broad-line (BL) AGN candidates as follows:
 1.0 = sources that are classified as BL AGN candidates by two different
        methods (221 occurrences)
 0.5 = sources identified as BL AGN candidates using one method but not the
        other (354 occurrences)
 0.0 = sources identified as non-BL AGNs by both methods (913 occurrences)

</details>
