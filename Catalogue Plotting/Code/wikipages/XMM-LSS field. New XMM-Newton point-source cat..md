**Authors:** Brandt W.N., Luo B., Ranalli P., Yang G., Alexander D.M.,, Bauer F.E., Kelson D.D., Lacy M., Nyland K., Tozzi P., Vito F.,, Cirasuolo M., Gilli R., Jarvis M.J., Lehmer B.D., Paolillo M.,, Schneider D.P., Shemmer O., Smail I., Sun M., Tanaka M., Vaccari M.,, Vignali C., Xue Y.Q., Banerji M., Chow K.E., Haussler B., Norris R.P.,, Silverman J.D., Trump J.R., <Mon. Not. R. Astron. Soc., 478, 2132-2163 (2018)>, =2018MNRAS.478.2132C (SIMBAD/NED BibCode)

## Summary: XMM-LSS field. New XMM-Newton point-source cat. 

We present an X-ray point-source catalogue from the XMM-Large Scale Structure (XMM-LSS) survey region, one of the XMM-Spitzer Extragalactic Representative Volume Survey (XMM-SERVS) fields. We target the XMM-LSS region with 1.3Ms of new XMM-Newton AO-15 observations, transforming the archival X-ray coverage in this region into a 5.3deg^2^ contiguous field with uniform X-ray coverage totaling 2.7Ms of flare-filtered exposure, with a 46ks median PN exposure time. We provide an X-ray catalogue of 5242 sources detected in the soft (0.5-2keV), hard (2-10keV), and/or full (0.5-10keV) bands with a 1 per cent expected spurious fraction determined from simulations. A total of 2381 new X-ray sources are detected compared to previous source catalogues in the same area. Our survey has flux limits of 1.7x10^-15^, 1.3x10^-14^, and 6.5x10^-15^erg/cm^2^/s over 90 per cent of its area in the soft, hard, and full bands, respectively, which is comparable to those of the XMM-COSMOS survey. We identify multiwavelength counterpart candidates for 99.9 per cent of the X-ray sources, of which 93 per cent are considered as reliable based on their matching likelihood ratios. The reliabilities of these high-likelihood-ratio counterparts are further confirmed to be ~=97 per cent reliable based on deep Chandra coverage over ~=5 per cent of the XMM-LSS region. Results of multiwavelength identifications are also included in the source catalogue, along with basic optical-to-infrared photometry and spectroscopic redshifts from publicly available surveys. We compute photometric redshifts for X-ray sources in 4.5 deg^2^ of our field where forced-aperture multiband photometry is available; >70 per cent of the X-ray sources in this subfield have either spectroscopic or high-quality photometric redshifts.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/XMM-LSS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zsp:** ?=-99 Spectroscopic redshift (ZSEPC) 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/ELAIS%20S1/Plots/zspec.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/XMM-LSS/Plots/zspec.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/ECDFS/Plots/zspec.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/COSMOS/Plots/zspec.png)
## Photometric Redshift 
 
**zph:** Photometric redshift (ZPHOT) 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/XMM-LSS/Plots/zphot.png)
<details>
<summary>Quality flag . . .

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-478-2132/Subcatalogues/XMM-LSS/Plots/q_zphot.png)</summary>
## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units    | Label     | Explanations                            |
|:--------|:---------|:---------|:----------|:----------------------------------------|
| 1- 19   | A19      | ---      | Field     | Target field                            |
| 21- 24  | I4       | ---      | Rev       | XMM-Newton revolution number            |
| 26- 35  | I10      | ---      | ObsID     | XMM-Newton ObsID                        |
| 37- 55  | A19      | "datime" | Date      | UT observation starting date/time       |
| 57- 64  | F8.5     | deg      | RAdeg     | Pointing center right ascension (J2000) |
| 66- 73  | F8.5     | deg      | DEdeg     | Pointing center declination (J2000)     |
| 75- 79  | F5.2     | ks       | GTI(PN)   | Cleaned exposure time for PN            |
| 81- 85  | F5.2     | ks       | GTI(MOS1) | Cleaned exposure time for MOS1          |
| 87- 91  | F5.2     | ks       | GTI(MOS2) | Cleaned exposure time for MOS2          |
</details>

<details>
<summary>table3.dat</summary>

| Bytes   | Format   | Units   | Label           | Explanations                             |
|:--------|:---------|:--------|:----------------|:-----------------------------------------|
| 1- 6    | F6.2     | [mW/m2] | logS(0.5-2keV)  | Soft-band (0.5-2keV) flux                |
| 8- 12   | F5.3     | deg+2   | O(0.5-2keV)     | Soft-band (0.5-2keV) survey solid angle  |
| 14- 19  | F6.2     | [mW/m2] | logS(2-10keV)   | Hard band (2-10keV) flux                 |
| 21- 25  | F5.3     | deg+2   | O(2-10keV)      | Hard band (2-10keV)  survey solid angle  |
| 27- 32  | F6.2     | [mW/m2] | logS(0.5-10keV) | Full band (0.5-10keV) flux               |
| 34- 38  | F5.3     | deg+2   | O(0.5-10keV)    | Full band (0.5-10keV) survey solid angle |
</details>

<details>
<summary>tablea.dat</summary>

| Bytes     | Format   | Units   | Label      | Explanations                                |
|:----------|:---------|:--------|:-----------|:--------------------------------------------|
| 1- 8      | A8       | ---     | XID        | XID, XMMNNNNN (XID)                         |
| 10- 19    | F10.6    | deg     | RAdeg      | Mean source right ascension (J2000) (RA)    |
| 21- 30    | F10.6    | deg     | DEdeg      | Mean source declination (J2000) (DEC)       |
| 32- 35    | F4.2     | arcsec  | eXpos      | X-ray positional uncertainty (XPOSERR)      |
| 37- 40    | F4.2     | arcsec  | R68        | 68% X-ray positional uncertainty (R68)      |
| 42- 45    | F4.2     | arcsec  | R99        | 99.73% X-ray positional uncertainty (R99)   |
| 47- 52    | F6.3     | arcsec  | eEML       | Positional uncertainty calculated by        |
| 54- 63    | F10.6    | deg     | RASdeg     | ?=-99 Soft band right ascension (J2000)     |
| 65- 74    | F10.6    | deg     | DESdeg     | ?=-99 Soft band declination (J2000)         |
| 76- 85    | F10.6    | deg     | RAHdeg     | ?=-99 Hard band right ascension (J2000)     |
| 87- 96    | F10.6    | deg     | DEHdeg     | ?=-99 Hard band declination (J2000)         |
| 98- 107   | F10.6    | deg     | RAFdeg     | ?=-99 Full band right ascension (J2000)     |
| 109- 118  | F10.6    | deg     | DEFdeg     | ?=-99 Full band declination (J2000)         |
| 120- 127  | F8.1     | ---     | SdetML     | ?=-99 Soft band Source detection threshold  |
| 129- 136  | F8.1     | ---     | HdetML     | ?=-99 Hard band Source detection threshold  |
| 138- 145  | F8.1     | ---     | FdetML     | Full band Source detection threshold        |
| 147- 152  | F6.2     | ---     | SRel       | ?=-99 Soft band detection reliability       |
| 154- 159  | F6.2     | ---     | HRel       | ?=-99 Hard band detection reliability       |
| 161- 166  | F6.2     | ---     | FRel       | ?=-99 Full band detection reliability       |
| 168- 175  | F8.1     | s       | Sexp       | Soft band total exposure time (SB_EXP)      |
| 177- 184  | F8.1     | s       | Hexp       | Hard band total exposure time (HB_EXP)      |
| 186- 193  | F8.1     | s       | Fexp       | Full band total exposure time (FB_EXP)      |
| 195- 202  | F8.1     | s       | SexpPN     | Soft band PN exposure time (SB_EXPPN)       |
| 204- 211  | F8.1     | s       | SexpM1     | Soft band M1 exposure time (SB_EXPM1)       |
| 213- 220  | F8.1     | s       | SexpM2     | Soft band M2 exposure time (SB_EXPM2)       |
| 222- 229  | F8.1     | s       | HexpPN     | Hard band PN exposure time (HB_EXPPN)       |
| 231- 238  | F8.1     | s       | HexpM1     | Hard band M1 exposure time (HB_EXPM1)       |
| 240- 247  | F8.1     | s       | HexpM2     | Hard band M2 exposure time (HB_EXPM2)       |
| 249- 256  | F8.1     | s       | FexpPN     | Full band PN exposure time (FB_EXPPN)       |
| 258- 265  | F8.1     | s       | FexpM1     | Full band M1 exposure time (FB_EXPM1)       |
| 267- 274  | F8.1     | s       | FexpM2     | Full band M2 exposure time (FB_EXPM2)       |
| 276- 284  | F9.5     | ct/pix  | Sbkg       | ?=-99 Soft band total background map value  |
| 286- 294  | F9.5     | ct/pix  | Hbkg       | ?=-99 Hard band total background map value  |
| 296- 304  | F9.5     | ct/pix  | Fbkg       | ?=-99 Full band total background map value  |
| 306- 314  | F9.5     | ct/pix  | SbkgPN     | ?=-99 Soft band PN background map value     |
| 316- 324  | F9.5     | ct/pix  | SbkgM1     | ?=-99 Soft band M1 background map value     |
| 326- 334  | F9.5     | ct/pix  | SbkgM2     | ?=-99 Soft band M2 background map value     |
| 336- 344  | F9.5     | ct/pix  | HbkgPN     | ?=-99 Hard band PN background map value     |
| 346- 354  | F9.5     | ct/pix  | HbkgM1     | ?=-99 Hard band M1 background map value     |
| 356- 364  | F9.5     | ct/pix  | HbkgM2     | ?=-99 Hard band M2 background map value     |
| 366- 374  | F9.5     | ct/pix  | FbkgPN     | ?=-99 Full band PN background map value     |
| 376- 384  | F9.5     | ct/pix  | FbkgM1     | ?=-99 Full band M1 background map value     |
| 386- 394  | F9.5     | ct/pix  | FbkgM2     | ?=-99 Full band M2 background map value     |
| 396- 403  | F8.2     | ct      | Sct        | Soft band total net counts (SB_SCTS)        |
| 405- 412  | F8.2     | ct      | Hct        | Hard band total net counts (HB_SCTS)        |
| 414- 421  | F8.2     | ct      | Fct        | Full band total net counts (FB_SCTS)        |
| 423- 430  | F8.2     | ct      | SctPN      | Soft band PN net counts (SB_SCTPN)          |
| 432- 439  | F8.2     | ct      | SctM1      | ?=-99 Soft band M1 net counts (SB_SCTM1)    |
| 441- 448  | F8.2     | ct      | SctM2      | ?=-99 Soft band M2 net counts (SB_SCTM2)    |
| 450- 457  | F8.2     | ct      | HctPN      | ?=-99 Hard band PN net counts (HB_SCTPN)    |
| 459- 466  | F8.2     | ct      | HctM1      | ?=-99 Hard band M1 net counts (HB_SCTM1)    |
| 468- 475  | F8.2     | ct      | HctM2      | ?=-99 Hard band M2 net counts (HB_SCTM2)    |
| 477- 484  | F8.2     | ct      | FctPN      | Full band PN net counts (FB_SCTPN)          |
| 486- 493  | F8.2     | ct      | FctM1      | ?=-99 Full band M1 net counts (FB_SCTM1)    |
| 495- 502  | F8.2     | ct      | FctM2      | ?=-99 Full band M2 net counts (FB_SCTM2)    |
| 504- 511  | F8.2     | ct      | e_Sct      | ?=-99 Error on Sct (SB_SCTS_ERR)            |
| 513- 520  | F8.2     | ct      | e_Hct      | ?=-99 Error on Hct (HB_SCTS_ERR)            |
| 522- 529  | F8.2     | ct      | e_Fct      | ?=-99 Error on Fct (FB_SCTS_ERR)            |
| 531- 538  | F8.2     | ct      | e_SctPN    | ?=-99 Error on SctPN (SB_SCTPN_ERR)         |
| 540- 547  | F8.2     | ct      | e_SctM1    | ?=-99 Error on SctM1 (SB_SCTM1_ERR)         |
| 549- 556  | F8.2     | ct      | e_SctM2    | ?=-99 Error on SctM2 (SB_SCTM2_ERR)         |
| 558- 565  | F8.2     | ct      | e_HctPN    | ?=-99 Error on HctPN (HB_SCTPN_ERR)         |
| 567- 574  | F8.2     | ct      | e_HctM1    | ?=-99 Error on HctM1 (HB_SCTM1_ERR)         |
| 576- 583  | F8.2     | ct      | e_HctM2    | ?=-99 Error on HctM2 (HB_SCTM2_ERR)         |
| 585- 592  | F8.2     | ct      | e_FctPN    | ?=-99 Error on FctPN (FB_SCTPN_ERR)         |
| 594- 601  | F8.2     | ct      | e_FctM1    | ?=-99 Error on FctM1 (FB_SCTM1_ERR)         |
| 603- 610  | F8.2     | ct      | e_FctM2    | ?=-99 Error on FctM2 (FB_SCTM2_ERR)         |
| 612- 619  | F8.6     | ct/s    | Srate      | Soft band total net count rate (SB_RATE)    |
| 621- 628  | F8.6     | ct/s    | SratePN    | Soft band PN net count rate (SB_RATEPN)     |
| 630- 639  | F10.6    | ct/s    | SrateM1    | Soft band M1 net count rate (SB_RATEM1)     |
| 641- 650  | F10.6    | ct/s    | SrateM2    | Soft band M2 net count rate (SB_RATEM2)     |
| 652- 659  | F8.6     | ct/s    | Hrate      | Hard band total net count rate (HB_RATE)    |
| 661- 670  | F10.6    | ct/s    | HratePN    | Hard band PN net count rate (HB_RATEPN)     |
| 672- 681  | F10.6    | ct/s    | HrateM1    | Hard band M1 net count rate (HB_RATEM1)     |
| 683- 692  | F10.6    | ct/s    | HrateM2    | Hard band M2 net count rate (HB_RATEM2)     |
| 694- 701  | F8.6     | ct/s    | Frate      | Full band total net count rate (FB_RATE)    |
| 703- 710  | F8.6     | ct/s    | FratePN    | Full band PN net count rate (FB_RATEPN)     |
| 712- 721  | F10.6    | ct/s    | FrateM1    | Full band M1 net count rate (FB_RATEM1)     |
| 723- 732  | F10.6    | ct/s    | FrateM2    | Full band M2 net count rate (FB_RATEM2)     |
| 734- 743  | F10.6    | ct/s    | e_Srate    | ?=-99 Error on Srate (SB_RATE_ERR)          |
| 745- 754  | F10.6    | ct/s    | e_SratePN  | ?=-99 Error on SratePN (SB_RATEPN_ERR)      |
| 756- 765  | F10.6    | ct/s    | e_SrateM1  | ?=-99 Error on SrateM1 (SB_RATEM1_ERR)      |
| 767- 776  | F10.6    | ct/s    | e_SrateM2  | ?=-99 Error on SrateM2 (SB_RATEM2_ERR)      |
| 778- 787  | F10.6    | ct/s    | e_Hrate    | ?=-99 Error on Hrate (HB_RATE_ERR)          |
| 789- 798  | F10.6    | ct/s    | e_HratePN  | ?=-99 Error on HratePN (HB_RATEPN_ERR)      |
| 800- 809  | F10.6    | ct/s    | e_HrateM1  | ?=-99 Error on HrateM1 (HB_RATEM1_ERR)      |
| 811- 820  | F10.6    | ct/s    | e_HrateM2  | ?=-99 Error on HrateM2 (HB_RATEM2_ERR)      |
| 822- 831  | F10.6    | ct/s    | e_Frate    | ?=-99 Error on Frate (FB_RATE_ERR)          |
| 833- 842  | F10.6    | ct/s    | e_FratePN  | ?=-99 Error on FratePN (FB_RATEPN_ERR)      |
| 844- 853  | F10.6    | ct/s    | e_FrateM1  | ?=-99 Error on FrateM1 (FB_RATEM1_ERR)      |
| 855- 864  | F10.6    | ct/s    | e_FrateM2  | ?=-99 Error on FrateM2 (FB_RATEM2_ERR)      |
| 866- 877  | E12.6    | mW/m2   | SFlux      | Soft band flux (SB_FLUX)                    |
| 879- 890  | E12.6    | mW/m2   | e_SFlux    | ?=-99 Error on soft band flux (SB_FLUXERR)  |
| 892- 903  | E12.6    | mW/m2   | HFlux      | Hard band flux (HB_FLUX)                    |
| 905- 916  | E12.6    | mW/m2   | e_HFlux    | ?=-99 Error on hard band flux (HB_FLUXERR)  |
| 918- 929  | E12.6    | mW/m2   | FFlux      | Full band flux (FB_FLUX)                    |
| 931- 942  | E12.6    | mW/m2   | e_FFlux    | ?=-99 Error on full band flux (FB_FLUXERR)  |
| 944- 953  | F10.6    | ---     | HR         | ?=-99 Total hardness ratio (HR)             |
| 955- 964  | F10.6    | ---     | e_HR       | ?=-99 Error on HR (lower value) (HR_LERR)   |
| 966- 975  | F10.6    | ---     | E_HR       | ?=-99 Error on HR (upper value) (HR_UERR)   |
| 977- 986  | F10.6    | ---     | HRPN       | ?=-99 PN hardness ratio (BEHR_PN)           |
| 988- 997  | F10.6    | ---     | e_HRPN     | []?=-99 Error on HRPN (lower value)         |
| 999-1008  | F10.6    | ---     | E_HRPN     | []?=-99 Error on HRPN (upper value)         |
| 1010-1019 | F10.6    | ---     | HRM1       | ?=-99 M1 hardness ratio (BEHR_M1)           |
| 1021-1030 | F10.6    | ---     | e_HRM1     | []?=-99 Error on HRM1 (lower value)         |
| 1032-1041 | F10.6    | ---     | E_HRM1     | []?=-99 Error on HRM1 (upper value)         |
| 1043-1052 | F10.6    | ---     | HRM2       | ?=-99 M2 hardness ratio (BEHR_M2)           |
| 1054-1063 | F10.6    | ---     | e_HRM2     | []?=-99 Error on HRM2 (lower value)         |
| 1065-1074 | F10.6    | ---     | E_HRM2     | []?=-99 Error on HRM2 (upper value)         |
| 1076-1087 | E12.6    | 10-7W   | LX         | ?=-99 Rest-frame apparent 2-10keV           |
| 1089-1117 | A29      | ---     | CSCID      | ?=-99 CSC 2.0 source name (CSCID)           |
| 1119-1126 | A8       | ---     | XXLID      | ?=-99 XXM-XXL-North source name (XXLID)     |
| 1128      | I1       | ---     | NSERVS     | Number of counterpart candidates from SERVS |
| 10        | arcsec   | search  | radius     | of each X-ray source (NALL_SERVS)           |
| 1130-1131 | I2       | ---     | NVIDEO     | Number of counterpart candidates from VIDEO |
| 10        | arcsec   | search  | radius     | of each X-ray source (NALL_VIDEO)           |
| 1133-1134 | I2       | ---     | NCFHT      | Number of counterpart candidates from CFHT  |
| 10        | arcsec   | search  | radius     | of each X-ray source (NALL_CFHT)            |
| 1136-1137 | I2       | ---     | NHSC       | Number of counterpart candidates from HSC   |
| 10        | arcsec   | search  | radius     | of each X-ray source (NALL_HSC)             |
| 1139-1141 | I3       | ---     | NMSERVS    | ?=-99 Number of sources from SERVS that     |
| 1143-1145 | I3       | ---     | NMVIDEO    | ?=-99 Number of sources from VIDEO that     |
| 1147-1149 | I3       | ---     | NMCFHT     | ?=-99 Number of sources from CGHT that      |
| 1151-1153 | I3       | ---     | NMHSC      | ?=-99 Number of sources from HSC that       |
| 1155      | I1       | ---     | LRRel      | [0/1] Flag set to 1 if a reliable           |
| 1157      | I1       | ---     | Sblend     | [0/1] Flag set to 1 if the primary          |
| 1159-1164 | A6       | ---     | Catalog1   | Catalog from which the primary counterpart  |
| 1166-1175 | F10.6    | deg     | RA1deg     | ?=-99 Catalog 1 right ascension (J2000)     |
| 1177-1186 | F10.6    | deg     | DE1deg     | ?=-99 Catalog 1 declination (J2000)         |
| 1188-1197 | F10.6    | arcsec  | Sep1X      | ?=-99 Separation of primary counterpart     |
| 1199-1209 | F11.6    | ---     | LR1        | ?=-99 matching likelihood ratio of the      |
| 1211-1220 | F10.6    | deg     | RA1Sdeg    | ?=-99 SERVS right ascension (J2000)         |
| 1222-1231 | F10.6    | deg     | DE1Sdeg    | ?=-99 SERVS declination (J2000) (SERVS_DEC) |
| 1233-1239 | I7       | ---     | SERVSID1   | ?=-99 SERVS source name (SERVS_ID)          |
| 1241-1243 | I3       | ---     | SERVSMR1   | ?=-99 SERVS matching reliability (SERVS_MR) |
| 1245-1254 | F10.6    | deg     | RA1Vdeg    | ?=-99 VIDEO right ascension (J2000)         |
| 1256-1265 | F10.6    | deg     | DE1Vdeg    | ?=-99 VIDEO declination (J2000) (VIDEO_DEC) |
| 1267-1278 | I12      | ---     | VIDEOID1   | ?=-99 VIDEO source name (VIDEO_ID)          |
| 1280-1282 | I3       | ---     | VIDEOMR1   | ?=-99 VIDEO matching reliability (VIDEO_MR) |
| 1284-1293 | F10.6    | deg     | RA1Cdeg    | ?=-99 CFHT right ascension (J2000)          |
| 1295-1304 | F10.6    | deg     | DE1Cdeg    | ?=-99 CFHT declination (J2000)(CFHT_DEC)    |
| 1306-1316 | A11      | ---     | CFHTID1    | ?=-99 CFHT source name (CFHT_ID)            |
| 1318-1320 | I3       | ---     | CFHTMR1    | ?=-99 CFHT matching reliability (CFHT_MR)   |
| 1322-1331 | F10.6    | deg     | RA1Hdeg    | ?=-99 HSC right ascension (J2000) (HSC_RA)  |
| 1333-1342 | F10.6    | deg     | DE1Hdeg    | ?=-99 HSC declination (J2000) (HSC_DEC)     |
| 1344-1360 | I17      | ---     | HSCID1     | ?=-99 HSC source name (HSC_ID)              |
| 1362-1364 | I3       | ---     | HSCMR1     | ?=-99 HSC matching reliability (HSC_MR)     |
| 1366-1373 | F8.4     | mag     | [3.6]SE1   | ?=-99 SERVS 3.6um magnitude (SERVS_MAG1)    |
| 1375-1382 | F8.4     | mag     | [4.5]SE1   | ?=-99 SERVS 4.5um magnitude (SERVS_MAG2)    |
| 1384-1391 | F8.4     | mag     | e_[3.6]SE1 | ?=-99 SERVS 3.6um magnitude error           |
| 1393-1400 | F8.4     | mag     | e_[4.5]SE1 | ?=-99 SERVS 4.5um magnitude error           |
| 1402-1409 | F8.4     | mag     | [3.6]SW1   | ?=-99 SWIRE 3.6um magnitude (SWIRE_MAG1)    |
| 1411-1418 | F8.4     | mag     | [4.5]SW1   | ?=-99 SWIRE 4.5um magnitude (SWIRE_MAG2)    |
| 1420-1427 | F8.4     | mag     | [5.8]SW1   | ?=-99 SWIRE 5.8um magnitude (SWIRE_MAG3)    |
| 1429-1436 | F8.4     | mag     | [8.0]SW1   | ?=-99 SWIRE 8.0um magnitude (SWIRE_MAG4)    |
| 1438-1445 | F8.4     | mag     | e_[3.6]SW1 | ?=-99 SWIRE 3.6um magnitude error           |
| 1447-1454 | F8.4     | mag     | e_[4.5]SW1 | ?=-99 SWIRE 4.5um magnitude error           |
| 1456-1463 | F8.4     | mag     | e_[5.8]SW1 | ?=-99 SWIRE 5.8um magnitude error           |
| 1465-1472 | F8.4     | mag     | e_[8.0]SW1 | ?=-99 SWIRE 8.0um magnitude error           |
| 1474-1481 | F8.4     | mag     | [24]SW1    | ?=-99 SWIRE-MIPS 24um magnitude             |
| 1483-1490 | F8.4     | mag     | e_[24]SW1  | []?=-99 SWIRE-MIPS 24um magnitude error     |
| 1492-1499 | F8.4     | mag     | Zmag1      | ?=-99 VIDEO Z magnitude (AB) (VIDEO_ZMAG)   |
| 1501-1508 | F8.4     | mag     | e_Zmag1    | ?=-99 VIDEO Z magnitude error               |
| 1510-1517 | F8.4     | mag     | Ymag1      | ?=-99 VIDEO Y magnitude (AB) (VIDEO_YMAG)   |
| 1519-1526 | F8.4     | mag     | e_Ymag1    | ?=-99 VIDEO Y magnitude error               |
| 1528-1535 | F8.4     | mag     | Jmag1      | ?=-99 VIDEO J magnitude (AB) (VIDEO_JMAG)   |
| 1537-1544 | F8.4     | mag     | e_Jmag1    | ?=-99 VIDEO J magnitude error               |
| 1546-1553 | F8.4     | mag     | Hmag1      | ?=-99 VIDEO H magnitude (AB) (VIDEO_HMAG)   |
| 1555-1562 | F8.4     | mag     | e_Hmag1    | ?=-99 VIDEO H magnitude error               |
| 1564-1571 | F8.4     | mag     | Ksmag1     | ?=-99 VIDEO Ks magnitude (AB) (VIDEO_KSMAG) |
| 1573-1580 | F8.4     | mag     | e_Ksmag1   | ?=-99 VIDEO Ks magnitude error              |
| 1582-1588 | F7.3     | mag     | umag1C     | ?=-99 CFHTLS u magnitude (AB) (CFHT_UMAG)   |
| 1589-1595 | F7.3     | mag     | e_umag1C   | ?=-99 CFHTLS u magnitude error              |
| 1597-1603 | F7.3     | mag     | gmag1C     | ?=-99 CFHTLS g magnitude (AB) (CFHT_GMAG)   |
| 1604-1610 | F7.3     | mag     | e_gmag1C   | ?=-99 CFHTLS g magnitude error              |
| 1612-1618 | F7.3     | mag     | rmag1C     | ?=-99 CFHTLS r magnitude (AB) (CFHT_RMAG)   |
| 1619-1625 | F7.3     | mag     | e_rmag1C   | ?=-99 CFHTLS r magnitude error              |
| 1627-1633 | F7.3     | mag     | imag1C     | ?=-99 CFHTLS i magnitude (AB) (CFHT_IMAG)   |
| 1635-1641 | F7.3     | mag     | e_imag1C   | ?=-99 CFHTLS i magnitude error              |
| 1643-1649 | F7.3     | mag     | zmag1C     | ?=-99 CFHTLS z magnitude (AB) (CFHT_ZMAG)   |
| 1651-1656 | A6       | mag     | e_zmag1C   | ?=-99 CFHTLS z magnitude error              |
| 1658-1664 | F7.3     | mag     | gmag1H     | ?=-99 HSC g magnitude (AB) (HSC_GMAG)       |
| 1666-1673 | F8.3     | mag     | e_gmag1H   | ?=-99 HSC g magnitude error (HSC_GMAGERR)   |
| 1675-1681 | F7.3     | mag     | rmag1H     | ?=-99 HSC r magnitude (AB) (HSC_RMAG)       |
| 1683-1689 | F7.3     | mag     | e_rmag1H   | ?=-99 HSC r magnitude error (HSC_RMAGERR)   |
| 1691-1697 | F7.3     | mag     | imag1H     | ?=-99 HSC i magnitude (AB) (HSC_IMAG)       |
| 1699-1705 | F7.3     | mag     | e_imag1H   | ?=-99 HSC i magnitude error (HSC_IMAGERR)   |
| 1707-1713 | F7.3     | mag     | zmag1H     | ?=-99 HSC z magnitude (AB) (HSC_ZMAG)       |
| 1715-1721 | F7.3     | mag     | e_zmag1H   | ?=-99 HSC z magnitude error (HSC_ZMAGERR)   |
| 1723-1729 | F7.3     | mag     | ymag1H     | ?=-99 HSC y magnitude (AB) (HSC_YMAG)       |
| 1731-1738 | F8.3     | mag     | e_ymag1H   | ?=-99 HSC y magnitude error (HSC_YMAGERR)   |
| 1740-1749 | F10.6    | deg     | RAz1deg    | ?=-99 Redshift catalog for the primary      |
| 1751-1760 | F10.6    | deg     | DEz1deg    | ?=-99 Redshift catalog for the primary      |
| 1762-1780 | A19      | ---     | Z1ID       | ?=-99 Redshift catalog source name          |
| 1782-1791 | F10.6    | ---     | z1sp       | ?=-99 Spectroscopic redshift adopted for    |
| 1793-1798 | A6       | ---     | r_z1sp     | ?=-99 catalogue that provided the redshift  |
| 1800-1817 | A18      | ---     | z1Oflag    | Original redshift flag from one of the      |
| 1819-1825 | F7.3     | ---     | z1ph       | ?=-99 Photometric redshift (ZPHOT)          |
| 1827-1833 | F7.3     | ---     | E_z1ph     | ?=-99 Error on zph (upper value)            |
| 1835-1841 | F7.3     | ---     | e_z1ph     | ?=-99 Error on zph (lower value)            |
| 1843-1854 | E12.6    | ---     | q_z1ph     | ?=-99 Photometric-redshift quality          |
| 1856-1860 | A5       | ---     | Class1     | five-digit AGN classification flag (CLASS)  |
| 1862-1874 | A13      | ---     | Catalog2   | ?=-99 Catalog from which the secondary      |
| 1876-1885 | F10.6    | deg     | RA2deg     | ?=-99 Catalog 2 right ascension (J2000)     |
| 1887-1896 | F10.6    | deg     | DE2deg     | ?=-99 Catalog 2 declination (J2000)         |
| 1898-1907 | F10.6    | arcsec  | Sep2X      | ?=-99 Separation of secondary counterpart   |
| 1909-1918 | F10.6    | ---     | LR2        | ?=-99 matching likelihood ratio of the      |
| 1920-1929 | F10.6    | deg     | RA2Sdeg    | ?=-99 SERVS right ascension (J2000)         |
| 1931-1940 | F10.6    | deg     | DE2Sdeg    | ?=-99 SERVS declination (J2000)             |
| 1942-1948 | I7       | ---     | SERVSID2   | ?=-99 SERVS source name                     |
| 1950-1952 | I3       | ---     | SERVSMR2   | [0/1]?=-99 SERVS matching reliability       |
| 1954-1963 | F10.6    | deg     | RA2Vdeg    | ?=-99 VIDEO right ascension (J2000)         |
| 1965-1974 | F10.6    | deg     | DE2Vdeg    | ?=-99 VIDEO declination (J2000)             |
| 1976-1987 | I12      | ---     | VIDEOID2   | ?=-99 VIDEO source name                     |
| 1989-1991 | I3       | ---     | VIDEOMR2   | [0/1]?=-99 VIDEO matching reliability       |
| 1993-2002 | F10.6    | deg     | RA2Cdeg    | ?=-99 CFHT right ascension (J2000)          |
| 2004-2013 | F10.6    | deg     | DE2Cdeg    | ?=-99 CFHT declination (J2000)              |
| 2015-2025 | A11      | ---     | CFHTID2    | ?=-99 CFHT source name (SECONDARY_CFHT_ID)  |
| 2027-2029 | I3       | ---     | CFHTMR2    | [0/1]?=-99 CFHT matching reliability        |
| 2031-2040 | F10.6    | deg     | RA2Hdeg    | ?=-99 HSC right ascension (J2000)           |
| 2042-2051 | F10.6    | deg     | DE2Hdeg    | ?=-99 HSC declination (J2000)               |
| 2053-2069 | I17      | ---     | HSCID2     | ?=-99 HSC source name (SECONDARY_HSC_ID)    |
| 2071-2073 | I3       | ---     | HSCMR2     | [0/1]?=-99 HSC matching reliability         |
| 2075-2082 | F8.4     | mag     | [3.6]SE2   | ?=-99 SERVS 3.6um magnitude                 |
| 2084-2091 | F8.4     | mag     | [4.5]SE2   | ?=-99 SERVS 4.5um magnitude                 |
| 2093-2100 | F8.4     | mag     | e_[3.6]SE2 | ?=-99 SERVS 3.6um magnitude error           |
| 2102-2109 | F8.4     | mag     | e_[4.5]SE2 | ?=-99 SERVS 4.5um magnitude error           |
| 2111-2118 | F8.4     | mag     | [3.6]SW2   | ?=-99 SWIRE 3.6um magnitude                 |
| 2120-2127 | F8.4     | mag     | [4.5]SW2   | ?=-99 SWIRE 4.5um magnitude                 |
| 2129-2136 | F8.4     | mag     | [5.8]SW2   | ?=-99 SWIRE 5.8um magnitude                 |
| 2138-2145 | F8.4     | mag     | [8.0]SW2   | ?=-99 SWIRE 8.0um magnitude                 |
| 2147-2154 | F8.4     | mag     | e_[3.6]SW2 | ?=-99 SWIRE 3.6um magnitude error           |
| 2156-2163 | F8.4     | mag     | e_[4.5]SW2 | ?=-99 SWIRE 4.5um magnitude error           |
| 2165-2172 | F8.4     | mag     | e_[5.8]SW2 | ?=-99 SWIRE 5.8um magnitude error           |
| 2174-2181 | F8.4     | mag     | e_[8.0]SW2 | ?=-99 SWIRE 8.0um magnitude error           |
| 2183-2190 | F8.4     | mag     | [24]SW2    | ?=-99 SWIRE-MIPS 24um magnitude             |
| 2192-2199 | F8.4     | mag     | e_[24]SW2  | ?=-99 SWIRE-MIPS 24um magnitude error       |
| 2201-2208 | F8.4     | mag     | Zmag2      | ?=-99 VIDEO Z magnitude (AB)                |
| 2210-2217 | F8.4     | mag     | e_Zmag2    | ?=-99 VIDEO Z magnitude error               |
| 2219-2226 | F8.4     | mag     | Ymag2      | ?=-99 VIDEO Y magnitude (AB)                |
| 2228-2235 | F8.4     | mag     | e_Ymag2    | ?=-99 VIDEO Y magnitude error               |
| 2237-2244 | F8.4     | mag     | Jmag2      | ?=-99 VIDEO J magnitude (AB)                |
| 2246-2253 | F8.4     | mag     | e_Jmag2    | ?=-99 VIDEO J magnitude error               |
| 2255-2262 | F8.4     | mag     | Hmag2      | ?=-99 VIDEO H magnitude (AB)                |
| 2264-2271 | F8.4     | mag     | e_Hmag2    | ?=-99 VIDEO H magnitude error               |
| 2273-2280 | F8.4     | mag     | Ksmag2     | ?=-99 VIDEO Ks magnitude (AB)               |
| 2282-2289 | F8.4     | mag     | e_Ksmag2   | ?=-99 VIDEO Ks magnitude error              |
| 2290-2296 | F7.3     | mag     | umag2C     | ?=-99 CFHTLS u magnitude (AB)               |
| 2297-2303 | F7.3     | mag     | e_umag2C   | ?=-99 CFHTLS u magnitude error              |
| 2304-2310 | F7.3     | mag     | gmag2C     | ?=-99 CFHTLS g magnitude (AB)               |
| 2311-2317 | F7.3     | mag     | e_gmag2C   | ?=-99 CFHTLS g magnitude error              |
| 2318-2324 | F7.3     | mag     | rmag2C     | ?=-99 CFHTLS r magnitude (AB)               |
| 2325-2331 | F7.3     | mag     | e_rmag2C   | ?=-99 CFHTLS r magnitude error              |
| 2333-2339 | F7.3     | mag     | imag2C     | ?=-99 CFHTLS i magnitude (AB)               |
| 2341-2347 | F7.3     | mag     | e_imag2C   | ?=-99 CFHTLS i magnitude error              |
| 2348-2354 | F7.3     | mag     | zmag2C     | ?=-99 CFHTLS z magnitude (AB)               |
| 2355-2361 | F7.3     | mag     | e_zmag2C   | ?=-99 CFHTLS z magnitude error              |
| 2363-2369 | F7.3     | mag     | gmag2H     | ?=-99 HSC g magnitude (AB)                  |
| 2371-2377 | F7.3     | mag     | e_gmag2H   | ?=-99 HSC g magnitude error                 |
| 2379-2385 | F7.3     | mag     | rmag2H     | ?=-99 HSC r magnitude (AB)                  |
| 2387-2393 | F7.3     | mag     | e_rmag2H   | ?=-99 HSC r magnitude error                 |
| 2395-2401 | F7.3     | mag     | imag2H     | ?=-99 HSC i magnitude (AB)                  |
| 2403-2409 | F7.3     | mag     | e_imag2H   | ?=-99 HSC i magnitude error                 |
| 2411-2417 | F7.3     | mag     | zmag2H     | ?=-99 HSC z magnitude (AB)                  |
| 2419-2425 | F7.3     | mag     | e_zmag2H   | ?=-99 HSC z magnitude error                 |
| 2427-2433 | F7.3     | mag     | ymag2H     | ?=-99 HSC y magnitude (AB)                  |
| 2435-2443 | F9.3     | mag     | e_ymag2H   | ?=-99 HSC y magnitude error                 |
| 2445-2454 | F10.6    | deg     | RAz2deg    | ?=-99 Redshift catalog for the secondary    |
| 2456-2465 | F10.6    | deg     | DEz2deg    | ?=-99 Redshift catalog for the secondary    |
| 2467-2485 | A19      | ---     | Z2ID       | ?=-99 Redshift catalog source name          |
| 2487-2496 | F10.6    | deg     | z2sp       | ?=-99 Spectroscopic redshift adopted for    |
| 2498-2503 | A6       | ---     | r_z2sp     | ?=-99 Catalogue that provided the redshift  |
| 2505-2522 | A18      | ---     | z2Oflag    | ?=-99 Original redshift flag from one of    |
| 2524-2529 | A6       | ---     | Catalog3   | ?=-99 Catalog from which the tertiary       |
| 2531-2540 | F10.6    | deg     | RA3deg     | ?=-99 Catalog 3 right ascension (J2000)     |
| 2542-2551 | F10.6    | deg     | DE3deg     | ?=-99 Catalog 3 declination (J2000)         |
| 2553-2562 | F10.6    | arcsec  | Sep3X      | ?=-99 Separation of tertiary counterpart    |
| 2564-2573 | F10.6    | ---     | LR3        | ?=-99 matching likelihood ratio of the      |
| 2575-2584 | F10.6    | deg     | RA3Sdeg    | ?=-99 SERVS right ascension (J2000)         |
| 2586-2595 | F10.6    | deg     | DE3Sdeg    | ?=-99 SERVS declination (J2000)             |
| 2597-2603 | I7       | ---     | SERVSID3   | ?=-99 SERVS source name                     |
| 2605-2607 | I3       | ---     | SERVSMR3   | [0/1]?=-99 SERVS matching reliability       |
| 2609-2618 | F10.6    | deg     | RA3Vdeg    | ?=-99 VIDEO right ascension (J2000)         |
| 2620-2629 | F10.6    | deg     | DE3Vdeg    | ?=-99 VIDEO declination (J2000)             |
| 2631-2642 | I12      | ---     | VIDEOID3   | ?=-99 VIDEO source name                     |
| 2644-2653 | F10.6    | ---     | VIDEOMR3   | [0/1]?=-99 VIDEO matching reliability       |
| 2655-2664 | F10.6    | deg     | RA3Cdeg    | ?=-99 CFHT right ascension (J2000)          |
| 2666-2675 | F10.6    | deg     | DE3Cdeg    | ?=-99 CFHT declination (J2000)              |
| 2677-2687 | A11      | ---     | CFHTID3    | ?=-99 CFHT source name                      |
| 2689-2698 | F10.6    | ---     | CFHTMR3    | [0/1]?=-99 CFHT matching reliability        |
| 2700-2709 | F10.6    | deg     | RA3Hdeg    | ?=-99 HSC right ascension (J2000)           |
| 2711-2720 | F10.6    | deg     | DE3Hdeg    | ?=-99 HSC declination (J2000)               |
| 2722-2738 | I17      | ---     | HSCID3     | ?=-99 HSC source name                       |
| 2740-2749 | F10.6    | ---     | HSCMR3     | [0/1]?=-99 HSC matching reliability         |
| 2751-2758 | F8.4     | mag     | [3.6]SE3   | ?=-99 SERVS 3.6um magnitude                 |
| 2760-2767 | F8.4     | mag     | [4.5]SE3   | ?=-99 SERVS 4.5um magnitude                 |
| 2769-2776 | F8.4     | mag     | e_[3.6]SE3 | ?=-99 SERVS 3.6um magnitude error           |
| 2778-2785 | F8.4     | mag     | e_[4.5]SE3 | ?=-99 SERVS 4.5um magnitude error           |
| 2787-2794 | F8.4     | mag     | [3.6]SW3   | ?=-99 SWIRE 3.6um magnitude                 |
| 2796-2803 | F8.4     | mag     | [4.5]SW3   | ?=-99 SWIRE 4.5um magnitude                 |
| 2805-2812 | F8.4     | mag     | [5.8]SW3   | ?=-99 SWIRE 5.8um magnitude                 |
| 2814-2821 | F8.4     | mag     | [8.0]SW3   | ?=-99 SWIRE 8.0um magnitude                 |
| 2823-2830 | F8.4     | mag     | e_[3.6]SW3 | ?=-99 SWIRE 3.6um magnitude error           |
| 2832-2839 | F8.4     | mag     | e_[4.5]SW3 | ?=-99 SWIRE 4.5um magnitude error           |
| 2841-2848 | F8.4     | mag     | e_[5.8]SW3 | ?=-99 SWIRE 5.8um magnitude error           |
| 2850-2857 | F8.4     | mag     | e_[8.0]SW3 | ?=-99 SWIRE 8.0um magnitude error           |
| 2859-2866 | F8.4     | mag     | [24]SW3    | ?=-99 SWIRE-MIPS 24um magnitude             |
| 2868-2875 | F8.4     | mag     | e_[24]SW3  | ?=-99 SWIRE-MIPS 24um magnitude error       |
| 2877-2884 | F8.4     | mag     | Zmag3      | ?=-99 VIDEO Z magnitude (AB)                |
| 2886-2893 | F8.4     | mag     | e_Zmag3    | ?=-99 VIDEO Z magnitude (AB) error          |
| 2895-2902 | F8.4     | mag     | Ymag3      | ?=-99 VIDEO Y magnitude (AB)                |
| 2904-2911 | F8.4     | mag     | e_Ymag3    | ?=-99 VIDEO Y magnitude error               |
| 2913-2920 | F8.4     | mag     | Jmag3      | ?=-99 VIDEO J magnitude (AB)                |
| 2922-2929 | F8.4     | mag     | e_Jmag3    | ?=-99 VIDEO J magnitude error               |
| 2931-2938 | F8.4     | mag     | Hmag3      | ?=-99 VIDEO H magnitude (AB)                |
| 2940-2947 | F8.4     | mag     | e_Hmag3    | ?=-99 VIDEO H magnitude error               |
| 2949-2956 | F8.4     | mag     | Ksmag3     | ?=-99 VIDEO Ks magnitude (AB)               |
| 2958-2965 | F8.4     | mag     | e_Ksmag3   | ?=-99 VIDEO Ks magnitude error              |
| 2966-2972 | F7.3     | mag     | umag3C     | ?=-99 CFHTLS u magnitude (AB)               |
| 2973-2979 | F7.3     | mag     | e_umag3C   | ?=-99 CFHTLS u magnitude error              |
| 2980-2986 | F7.3     | mag     | gmag3C     | ?=-99 CFHTLS g magnitude (AB)               |
| 2987-2993 | F7.3     | mag     | e_gmag3C   | ?=-99 CFHTLS g magnitude error              |
| 2994-3000 | F7.3     | mag     | rmag3C     | ?=-99 CFHTLS r magnitude (AB)               |
| 3001-3007 | F7.3     | mag     | e_rmag3C   | ?=-99 CFHTLS r magnitude error              |
| 3009-3015 | F7.3     | mag     | imag3C     | ?=-99 CFHTLS i magnitude (AB)               |
| 3017-3023 | F7.3     | mag     | e_imag3C   | ?=-99 CFHTLS i magnitude error              |
| 3025-3030 | A6       | mag     | zmag3C     | ?=-99 CFHTLS z magnitude (AB)               |
| 3032-3037 | A6       | mag     | e_zmag3C   | ?=-99 CFHTLS z magnitude error              |
| 3039-3045 | F7.3     | mag     | gmag3H     | ?=-99 HSC g magnitude (AB)                  |
| 3047-3053 | F7.3     | mag     | e_gmag3H   | ?=-99 HSC g magnitude error                 |
| 3055-3061 | F7.3     | mag     | rmag3H     | ?=-99 HSC r magnitude (AB)                  |
| 3063-3069 | F7.3     | mag     | e_rmag3H   | ?=-99 HSC r magnitude error                 |
| 3071-3077 | F7.3     | mag     | imag3H     | ?=-99 HSC i magnitude (AB)                  |
| 3079-3085 | F7.3     | mag     | e_imag3H   | ?=-99 HSC i magnitude error                 |
| 3087-3093 | F7.3     | mag     | zmag3H     | ?=-99 HSC z magnitude (AB)                  |
| 3095-3101 | F7.3     | mag     | e_zmag3H   | ?=-99 HSC z magnitude error                 |
| 3103-3109 | F7.3     | mag     | ymag3H     | ?=-99 HSC y magnitude (AB)                  |
| 3111-3117 | F7.3     | mag     | e_ymag3H   | ?=-99 HSC y magnitude error                 |
| 3119-3128 | F10.6    | deg     | RAz3deg    | ?=-99 catalog for the tertiary counterpart  |
| 3130-3139 | F10.6    | deg     | DEz3deg    | ?=-99 Redshift catalog for the tertiary     |
| 3141-3149 | A9       | ---     | Z3ID       | ?=-99 Redshift catalog source name          |
| 3151-3160 | F10.6    | ---     | z3sp       | ?=-99 Spectroscopic redshift adopted for    |
| 3162-3167 | A6       | ---     | r_z3sp     | ?=-99 Catalogue that provided the redshift  |
| 3169-3173 | A5       | ---     | z3Oflag    | ?=-99 Original redshift flag from one of    |
| 3175-3193 | I19      | ---     | SDSS       | ?=-99 Supplementary SDSS id                 |
| 3195-3204 | F10.6    | deg     | RAsdeg     | ?=-99 Supplmentary SDSS right ascension     |
| 3206-3215 | F10.6    | deg     | DEsdeg     | ?=-99 Supplmentary SDSS declination (J2000) |
| 3219-3226 | F8.4     | mag     | umag       | ?=-99 Supplmentary SDSS u magnitude         |
| 3230-3237 | F8.4     | mag     | e_umag     | []?=-99 Supplmentary SDSS u magnitude error |
| 3241-3248 | F8.4     | mag     | gmag       | ?=-99 Supplmentary SDSS g magnitude         |
| 3252-3259 | F8.4     | mag     | e_gmag     | []?=-99 Supplmentary SDSS g magnitude error |
| 3263-3270 | F8.4     | mag     | rmag       | ?=-99 Supplmentary SDSS r magnitude         |
| 3274-3281 | F8.4     | mag     | e_rmag     | []?=-99 Supplmentary SDSS r magnitude error |
| 3285-3292 | F8.4     | mag     | imag       | ?=-99 Supplmentary SDSS i magnitude         |
| 3296-3303 | F8.4     | mag     | e_imag     | []?=-99 Supplmentary SDSS i magnitude error |
| 3307-3314 | F8.4     | mag     | zmag       | ?=-99 Supplmentary SDSS z magnitude         |
| 3318-3325 | F8.4     | mag     | e_zmag     | []?=-99 Supplmentary SDSS z magnitude error |
| 3327-3342 | A16      | ---     | 2MASS      | ?=-99 Supplementary 2MASS ID                |
| 3344-3353 | F10.6    | deg     | RA2mdeg    | ?=-99 2MASS right ascension (J2000)         |
| 3355-3364 | F10.6    | deg     | DE2mdeg    | ?=-99 2MASS declination (J2000)             |
| 3366-3372 | F7.3     | mag     | J2mag      | ?=-99 2MASS J magnitude                     |
| 3374-3380 | F7.3     | mag     | e_J2mag    | ?=-99 2MASS J magnitude error               |
| 3382-3388 | F7.3     | mag     | H2mag      | ?=-99 2MASS H magnitude                     |
| 3390-3396 | F7.3     | mag     | e_H2mag    | ?=-99 2MASS H magnitude error               |
| 3398-3404 | F7.3     | mag     | Ks2mag     | ?=-99 2MASS Ks magnitude                    |
| 3406-3412 | F7.3     | mag     | e_Ks2mag   | ?=-99 2MASS Ks magnitude error              |
| 3414-3425 | I12      | ---     | DXS        | ?=-99 Supplementary DXS ID                  |
| 3427-3436 | F10.6    | deg     | RADdeg     | ?=-99 Supplementary DXS right ascension     |
| 3438-3447 | F10.6    | deg     | DEDdeg     | ?=-99 Supplementary DXS declination (J2000) |
| 3449-3456 | F8.4     | mag     | JDmag      | ?=-99 Supplementary DXS J magnitude         |
| 3458-3465 | F8.4     | mag     | e_JDmag    | ?=-99 Supplementary DXS J magnitude error   |
| 3467-3474 | F8.4     | mag     | KsDmag     | ?=-99 Supplementary DXS Ks magnitude        |
| 3476-3483 | F8.4     | mag     | e_KsDmag   | ?=-99 Supplementary DXS Ks magnitude error  |
</details>

<details>
<summary>tableb.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                 |
|:--------|:---------|:--------|:----------|:---------------------------------------------|
| 1- 8    | A8       | ---     | XID       | Unique source ID (XID) assigned to           |
| 10- 31  | E22.20   | ---     | Pany      | Posterior probability of the X-ray source    |
| 33- 51  | F19.17   | ---     | Pi        | [0/1] Relative probability of a counterpart  |
| 53- 71  | F19.15   | deg     | RASdeg    | ?=-99 Right ascension (J2000) in             |
| 73- 92  | F20.16   | deg     | DESdeg    | ?=-99 Declination (J2000) in SERVS catalog   |
| 94-112  | F19.15   | deg     | RAVdeg    | ?=-99 Right ascension (J2000)                |
| 114-133 | F20.16   | deg     | DEVdeg    | ?=-99 Declination (J2000) in VIDEO catalog   |
| 135-153 | F19.15   | deg     | RACdeg    | ?=-99 Right ascension (J2000)                |
| 155-173 | F19.15   | deg     | DECdeg    | ?=-99 Declination (J2000) in CFHTLS catalog  |
| 175-193 | F19.15   | deg     | RAHdeg    | ?=-99 Right ascension (J2000) in HSC catalog |
| 195-214 | F20.16   | deg     | DEHdeg    | ?=-99 Declination (J2000) in HSC catalog     |
| 216-223 | F8.1     | ---     | SERVSID   | ?=-99 SERVS catalog designation              |
| 225-236 | I12      | ---     | VIDEOID   | ?=-99 VIDEO catalog designation              |
| 238-248 | A11      | ---     | CFHTID    | CFHTLS catalog designation                   |
| 250-266 | I17      | ---     | HSCID     | ?=-99 HSC catalog catalog designation        |
| 268-289 | F22.18   | arcsec  | SERVSSep  | ?=-99 Separation of the X-ray position from  |
| 291-312 | F22.18   | arcsec  | VIDEOSep  | ?=-99 Separation of the X-ray position from  |
| 314-335 | F22.18   | arcsec  | CFHTSep   | ?=-99 Separation of the X-ray position from  |
| 337-358 | F22.18   | arcsec  | HSCSep    | ?=-99 Separation of the X-ray position from  |
| 360-378 | F19.15   | mag     | [3.6]SE   | ?=-99 SERVS 1.9 arcsec aperture photometry   |
| 380-398 | F19.15   | mag     | [4.5]SE   | ?=-99 SERVS 1.9 arcsec aperture photometry   |
| 400-423 | F24.20   | mag     | e_[3.6]SE | ?=-99 rms uncertainty on [3.6]SE             |
| 425-448 | F24.20   | mag     | e_[4.5]SE | ?=-99 rms uncertainty on [4.5]SE             |
| 450-468 | F19.15   | mag     | Ymag      | ?=-99 VIDEO PSF photometry in Y band (AB)    |
| 470-493 | F24.20   | mag     | e_Ymag    | ?=-99 rms uncertainty on Ymag                |
| 495-513 | F19.15   | mag     | Jmag      | ?=-99 VIDEO PSF photometry in J band (AB)    |
| 515-538 | F24.20   | mag     | e_Jmag    | ?=-99 rms uncertainty on Jmag                |
| 540-558 | F19.15   | mag     | Hmag      | ?=-99 VIDEO PSF photometry in H band (AB)    |
| 560-583 | F24.20   | mag     | e_Hmag    | ?=-99 rms uncertainty on Hmag                |
| 585-603 | F19.15   | mag     | Ksmag     | ?=-99 VIDEO PSF photometry in Ks band (AB)   |
| 605-628 | F24.20   | mag     | e_Ksmag   | ?=-99 rms uncertainty on Ksmag               |
| 630-636 | F7.3     | mag     | umagC     | ?=-99 CFHTLS PSF photometry in u band (AB)   |
| 638-644 | F7.3     | mag     | e_umagC   | ?=-99 rms uncertainty on umagC               |
| 646-652 | F7.3     | mag     | gmagC     | ?=-99 CFHTLS PSF photometry in g band (AB)   |
| 654-660 | F7.3     | mag     | e_gmagC   | ?=-99 rms uncertainty on gmagC               |
| 662-668 | F7.3     | mag     | rmagC     | ?=-99 CFHTLS PSF photometry in r band (AB)   |
| 670-676 | F7.3     | mag     | e_rmagC   | ?=-99 rms uncertainty on rmagC               |
| 678-682 | F5.1     | mag     | imagC     | ?=-99 CFHTLS PSF photometry in i band (AB)   |
| 684-688 | F5.1     | mag     | e_imagC   | ?=-99 rms uncertainty on imagC               |
| 690-696 | F7.3     | mag     | zmagC     | ?=-99 CFHTLS PSF photometry in z band (AB)   |
| 698-704 | F7.3     | mag     | e_zmagC   | ?=-99 rms uncertainty on zmagC               |
| 706-724 | F19.15   | mag     | gmagH     | ?=-99 HSC CModel photometry in g band (AB)   |
| 725     | A1       | ---     | n_gmagH   | [i] i for infinity                           |
| 726-749 | F24.20   | mag     | e_gmagH   | ?=-99 rms uncertainty on gmagH               |
| 751-769 | F19.15   | mag     | rmagH     | ?=-99 HSC CModel photometry in r band (AB)   |
| 771-794 | F24.20   | mag     | e_rmagH   | ?=-99 rms uncertainty on rmagH               |
| 796-800 | F5.1     | mag     | imagH     | ?=-99 HSC CModel photometry in i band (AB)   |
| 802-806 | F5.1     | mag     | e_imagH   | ?=-99 rms uncertainty on imagH               |
| 808-826 | F19.15   | mag     | zmagH     | ?=-99 HSC CModel photometry in z band (AB)   |
| 827     | A1       | ---     | n_zmagH   | [i] i for infinity                           |
| 828-851 | F24.20   | mag     | e_zmagH   | ?=-99 rms uncertainty on zmagH               |
| 853-871 | F19.15   | mag     | YmagH     | ?=-99 HSC CModel photometry in Y band (AB)   |
| 872     | A1       | ---     | n_YmagH   | [i] i for infinity                           |
| 873-896 | F24.20   | mag     | e_YmagH   | ?=-99 rms uncertainty on YmagH               |
| 898     | I1       | ---     | MatchFlg  | [1/2] Matching flag (1)                      |

**Note**: For the most-probable counterparts the flag is set to 1.
   For other counterparts that are almost as likely as the most-probable
   counterpart (i.e. with p_i_>=p_iBest_), the flag is set to 2.

</details>

<details>
<summary>tablec.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                   |
|:--------|:---------|:--------|:--------|:-----------------------------------------------|
| 1- 12   | I12      | ---     | VIDEOID | VIDEO name (VIDEO_ID)                          |
| 14- 23  | F10.6    | deg     | RAdeg   | VIDEO right ascension (J2000) (VIDEO_RA)       |
| 25- 34  | F10.6    | deg     | DEdeg   | VIDEO declination (J2000) (VIDEO_DEC)          |
| 36- 42  | I7       | ---     | SERVSID | ?=-99 SERVS name (SERVS_ID)                    |
| 44- 53  | F10.6    | deg     | RASdeg  | ?=-99 SERVS right ascension (J2000) (SERVS_RA) |
| 55- 64  | F10.6    | deg     | DESdeg  | ?=-99 SERVS declination (J2000) (SERVS_DEC)    |
| 66- 70  | F5.3     | ---     | zph     | Photometric redshift (ZPHOT)                   |
| 72- 78  | F7.5     | ---     | q_zph   | Photometric redshift quality parameter (QZ)    |
| 80- 88  | F9.5     | ---     | zsp     | ?=-99 Spectroscopic redshift (ZSEPC)           |
| 90- 95  | A6       | ---     | r_zsp   | Catalogue that provided the redshift (ZSOURCE) |
| 97-114  | A18      | ---     | zOflag  | Original redshift flag (ZFLAG) (G1)            |
</details>
