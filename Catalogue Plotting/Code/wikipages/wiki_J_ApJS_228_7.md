**Authors:** Hemmati S., Mobasher B., Ferguson H.C., Cooray A., Barro G.,, Faber S.M., Dickinson M., Koekemoer A.M., Peth M., Salvato M.,, Ashby M.L.N., Darvish B., Donley J., Durbin M., Finkelstein S., Fontana A.,, Grogin N.A., Gruetzbauch R., Huang K., Khostovan A.A., Kocevski D.,, Kodra D., Lee B., Newman J., Pacifici C., Pforr J., Stefanon M.,, Wiklind T., Willner S.P., Wuyts S., Castellano M., Conselice C., Dolch T.,, Dunlop J.S., Galametz A., Hathi N.P., Lucas R.A., Yan H., <Astrophys. J. Suppl. Ser., 228, 7-7 (2017)>, =2017ApJS..228....7N (SIMBAD/NED BibCode)

## Summary: Multi-wavelength data in CANDELS COSMOS field 

We present a multi-wavelength photometric catalog in the COSMOS field as part of the observations by the Cosmic Assembly Near-infrared Deep Extragalactic Legacy Survey. The catalog is based on Hubble Space Telescope Wide Field Camera 3 (HST/WFC3) and Advanced Camera for Surveys observations of the COSMOS field (centered at RA:10:00:28, DEC:+02:12:21). The final catalog has 38671 sources with photometric data in 42 bands from UV to the infrared (~0.3-8{mu}m). This includes broadband photometry from HST, CFHT, Subaru, the Visible and Infrared Survey Telescope for Astronomy, and Spitzer Space Telescope in the visible, near-infrared, and infrared bands along with intermediate- and narrowband photometry from Subaru and medium-band data from Mayall NEWFIRM. Source detection was conducted in the WFC3 F160W band (at 1.6{mu}m) and photometry is generated using the Template FITting algorithm. We further present a catalog of the physical properties of sources as identified in the HST F160W band and measured from the multi-band photometry by fitting the observed spectral energy distributions of sources against templates.

## Catalogue Schema


## Spectroscopic Redshift 
 
*zbest:* [0/10]?=-99 Best phot or spectroscopic 
 

## Photometric Redshift 
 
*zphotl68:* ?=-99 Lower 68% confidence level in zphot 
 
<details>
<summary>table9.dat</summary>

| Bytes    | Format   | Units   | Label      | Explanations                                                            |
|:---------|:---------|:--------|:-----------|:------------------------------------------------------------------------|
| 1- 5     | I5       | ---     | Seq        | SExtractor identifier from F160W image                                  |
| 7- 27    | A21      | ---     | ---        | [CANDELS_COSMOS_F160W_]                                                 |
| 28- 46   | A19      | ---     | ID         | IAU designation (1)                                                     |
| 48- 57   | F10.6    | deg     | RAdeg      | Right Ascension in decimal degrees (J2000)                              |
| 59- 66   | F8.6     | deg     | DEdeg      | Declination in decimal degrees (J2000)                                  |
| 68- 77   | F10.3    | uJy     | APCOR      | [-19091/102557] Aperture correction (2)                                 |
| 79- 88   | E10.3    | uJy     | uCFHT      | [-6.1/5239] CFHT/MegaCam u band flux density                            |
| 90- 98   | E9.3     | uJy     | e_uCFHT    | [0.0006/1.5] Uncertainty in uCFHT                                       |
| 100- 109 | E10.3    | uJy     | gCFHT      | [-10.1/3489] CFHT/MegaCam g band flux density                           |
| 111- 119 | E9.3     | uJy     | e_gCFHT    | [0.0003/1.1] Uncertainty in gCFHT                                       |
| 121- 130 | E10.3    | uJy     | rCFHT      | [-11.1/3520] CFHT/MegaCam r band flux density                           |
| 132- 140 | E9.3     | uJy     | e_rCFHT    | [0.0004/1.2] Uncertainty in rCFHT                                       |
| 142- 151 | E10.3    | uJy     | iCFHT      | [-4.7/2560] CFHT/MegaCam i band flux density                            |
| 153- 161 | E9.3     | uJy     | e_iCFHT    | [0.0006/1.2] Uncertainty in iCFHT                                       |
| 163- 172 | E10.3    | uJy     | zCFHT      | [-13.5/8024] CFHT/MegaCam z band flux density                           |
| 174- 182 | E9.3     | uJy     | e_zCFHT    | [0.001/3] Uncertainty in zCFHT                                          |
| 184- 193 | E10.3    | uJy     | BSub       | [-0.05/199] Subaru/Suprime-Cam B band flux                              |
| 195- 203 | E9.3     | uJy     | e_BSub     | [0.0001/0.3] Uncertainy in BSub                                         |
| 205- 214 | E10.3    | uJy     | gSub       | [-0.3/317] Subaru/Suprime-Cam g band flux                               |
| 216- 224 | E9.3     | uJy     | e_gSub     | [0.0009/0.7] Uncertainy in gSub                                         |
| 226- 235 | E10.3    | uJy     | VSub       | [-0.2/314.1] Subaru/Suprime-Cam V band flux                             |
| 237- 245 | E9.3     | uJy     | e_VSub     | [0.0005/0.4] Uncertainy in VSub                                         |
| 247- 256 | E10.3    | uJy     | rSub       | [-0.2/447.5] Subaru/Suprime-Cam r band flux                             |
| 258- 266 | E9.3     | uJy     | e_rSub     | [0.0004/0.5] Uncertainy in rSub                                         |
| 268- 277 | E10.3    | uJy     | iSub       | [-0.2/667] Subaru/Suprime-Cam i band flux                               |
| 279- 287 | E9.3     | uJy     | e_iSub     | [0.0004/1.2] Uncertainy in iSub                                         |
| 289- 298 | E10.3    | uJy     | zSub       | [-0.8/1000] Subaru/Suprime-Cam z band flux                              |
| 300- 308 | E9.3     | uJy     | e_zSub     | [0.002/0.9] Uncertainy in zSub                                          |
| 310- 319 | E10.3    | uJy     | F606W      | [-3980/21960]?=-99 HST/ACS F606W band flux                              |
| 321- 330 | E10.3    | uJy     | e_F606W    | [0/252]?=-99 Uncertainy in F606W                                        |
| 332- 341 | E10.3    | uJy     | F814W      | [-6487/31500]?=-99 HST/ACS F814W band flux                              |
| 343- 352 | E10.3    | uJy     | e_F814W    | [0/386]?=-99 Uncertainy in F814W                                        |
| 354- 363 | E10.3    | uJy     | F125W      | [/14590]?=-99 HST/WFC3 F125W band flux                                  |
| 365- 374 | E10.3    | uJy     | e_F125W    | [0/13]?=-99 Uncertainy in F125W                                         |
| 376- 385 | E10.3    | uJy     | F160W      | [/27850]?=-99 HST/WFC3 F160W band flux                                  |
| 387- 396 | E10.3    | uJy     | e_F160W    | [0/13]?=-99 Uncertainy in F160W                                         |
| 398- 407 | E10.3    | uJy     | YVISTA     | [-6.3/24760] UltraVISTA Y band flux density                             |
| 409- 417 | E9.3     | uJy     | e_YVISTA   | [0.003/1.4] Uncertainty in YVISTA                                       |
| 419- 428 | E10.3    | uJy     | JVISTA     | [-1.8/12180] UltraVISTA J band flux density                             |
| 430- 438 | E9.3     | uJy     | e_JVISTA   | [0.004/0.8] Uncertainty in JVISTA                                       |
| 440- 449 | E10.3    | uJy     | HVISTA     | [-2.7/19080] UltraVISTA H band flux density                             |
| 451- 459 | E9.3     | uJy     | e_HVISTA   | [0.005/1.4] Uncertainty in HVISTA                                       |
| 461- 470 | E10.3    | uJy     | KsVISTA    | [-2.2/14520] UltraVISTA Ks  band flux density                           |
| 472- 480 | E9.3     | uJy     | e_KsVISTA  | [0.007/0.9] Uncertainty in KsVISTA                                      |
| 482- 491 | E10.3    | uJy     | 3.4IRAC    | [-147/8816] Spitzer/IRAC 3.4um band flux                                |
| 493- 501 | E9.3     | uJy     | e_3.4IRAC  | [0.01/2] Uncertainty in 3.4IRAC                                         |
| 503- 512 | E10.3    | uJy     | 4.5IRAC    | [-93/5790] Spitzer/IRAC 4.5um band flux                                 |
| 514- 522 | E9.3     | uJy     | e_4.5IRAC  | [0.01/1.7] Uncertainty in 4.5IRAC                                       |
| 524- 533 | E10.3    | uJy     | 5.8IRAC    | [-151/5548] Spitzer/IRAC 5.8um band flux                                |
| 535- 544 | E10.3    | uJy     | e_5.8IRAC  | [0.3/39]?=-99 Uncertainty in 5.8IRAC                                    |
| 546- 555 | E10.3    | uJy     | 8.0IRAC    | [-151/3038] Spitzer/IRAC 8.0um band flux                                |
| 557- 566 | E10.3    | uJy     | e_8.0IRAC  | [0.3/45]?=-99 Uncertainty in 8.0IRAC                                    |
| 568- 577 | E10.3    | uJy     | J1NFIRM    | [-224/12030] NEWFIRM J1 band flux density                               |
| 579- 587 | E9.3     | uJy     | e_J1NFIRM  | [0.005/1.5] Uncertainty in J1NFIRM                                      |
| 589- 598 | E10.3    | uJy     | J2NFIRM    | [-159/11400] NEWFIRM J2 band flux density                               |
| 600- 608 | E9.3     | uJy     | e_J2NFIRM  | [0.008/2.2] Uncertainty in J2NFIRM                                      |
| 610- 619 | E10.3    | uJy     | J3NFIRM    | [-165/9385] NEWFIRM J3 band flux density                                |
| 621- 629 | E9.3     | uJy     | e_J3NFIRM  | [0.009/4] Uncertainty in J3NFIRM                                        |
| 631- 640 | E10.3    | uJy     | H1NFIRM    | [-144/16760] NEWFIRM H1 band flux density                               |
| 642- 650 | E9.3     | uJy     | e_H1NFIRM  | [0.01/6.3] Uncertainty in H1NFIRM                                       |
| 652- 661 | E10.3    | uJy     | H2NFIRM    | [-309/18360] NEWFIRM H2 band flux density                               |
| 663- 671 | E9.3     | uJy     | e_H2NFIRM  | [0.02/5] Uncertainty in H2NFIRM                                         |
| 673- 682 | E10.3    | uJy     | KNFIRM     | [-214/18980] NEWFIRM K band flux density                                |
| 684- 692 | E9.3     | uJy     | e_KNFIRM   | [0.02/17] Uncertainty in KNFIRM                                         |
| 694- 703 | E10.3    | uJy     | Sub427     | [-1/1967] Subaru IB427 (4263{AA}) band flux                             |
| 705- 713 | E9.3     | uJy     | e_Sub427   | [0.0009/1.1] Uncertainty in Sub427                                      |
| 715- 724 | E10.3    | uJy     | Sub464     | [-1.7/2521] Subaru IB464 (4635{AA}) band flux                           |
| 726- 734 | E9.3     | uJy     | e_Sub464   | [0.002/1.4] Uncertainty in Sub464                                       |
| 736- 745 | E10.3    | uJy     | Sub484     | [-0.5/665] Subaru IA484 (4849{AA}) band flux                            |
| 747- 755 | E9.3     | uJy     | e_Sub484   | [0.0008/0.8] Uncertainty in Sub484                                      |
| 757- 766 | E10.3    | uJy     | Sub505     | [-1.1/1724] Subaru IB505 (5062{AA}) band flux                           |
| 768- 776 | E9.3     | uJy     | e_Sub505   | [0.001/1] Uncertainty in Sub505                                         |
| 778- 787 | E10.3    | uJy     | Sub527     | [-0.2/747] Subaru IA527 (5261{AA}) band flux                            |
| 789- 797 | E9.3     | uJy     | e_Sub527   | [0.0007/0.8] Uncertainty in Sub527                                      |
| 799- 808 | E10.3    | uJy     | Sub574     | [-3.2/1584] Subaru IB574 (5764{AA}) band flux                           |
| 810- 818 | E9.3     | uJy     | e_Sub574   | [0.002/1.1] Uncertainty in Sub574                                       |
| 820- 829 | E10.3    | uJy     | Sub624     | [-1.7/903] Subaru IA624 (6232{AA}) band flux                            |
| 831- 839 | E9.3     | uJy     | e_Sub624   | [0.0008/0.8] Uncertainty in Sub624                                      |
| 841- 850 | E10.3    | uJy     | Sub679     | [-3/1456] Subaru IA679 (6780{AA}) band flux                             |
| 852- 860 | E9.3     | uJy     | e_Sub679   | [0.001/1] Uncertainty in Sub679                                         |
| 862- 871 | E10.3    | uJy     | Sub709     | [-1.3/933] Subaru IB709 (7073{AA}) band flux                            |
| 873- 881 | E9.3     | uJy     | e_Sub709   | [0.001/0.8] Uncertainty in Sub709                                       |
| 883- 892 | E10.3    | uJy     | Sub711     | [-1.8/2031] Subaru NB711 (7120{AA}) band flux                           |
| 894- 902 | E9.3     | uJy     | e_Sub711   | [0.001/1.2] Uncertainty in Sub711                                       |
| 904- 913 | E10.3    | uJy     | Sub738     | [-2/978] Subaru IA738 (7361{AA}) band flux                              |
| 915- 923 | E9.3     | uJy     | e_Sub738   | [0.001/0.9] Uncertainty in Sub738                                       |
| 925- 934 | E10.3    | uJy     | Sub767     | [-1.9/1485] Subaru IA767 (7684{AA}) band flux                           |
| 936- 944 | E9.3     | uJy     | e_Sub767   | [0.002/1] Uncertainty in Sub767                                         |
| 946- 955 | E10.3    | uJy     | Sub816     | [-2/1537] Subaru NB816 (8149{AA}) band flux                             |
| 957- 965 | E9.3     | uJy     | e_Sub816   | [0.001/1] Uncertainty in Sub816                                         |
| 967- 976 | E10.3    | uJy     | Sub827     | [-4.6/1307] Subaru IB827 (8244{AA}) band flux                           |
| 978- 986 | E9.3     | uJy     | e_Sub827   | [0.002/1] Uncertainty in Sub827                                         |
| 988- 994 | F7.3     | pix     | FWHM       | [-2.3/444] SExtractor F160W image Full-Width                            |
| 996- 996 | I1       | ---     | Flag       | [0/2]? Photometry flag (0=good) (3)                                     |
| 998-1001 | F4.2     | ---     | G/S        | SExtractor stellar classification; 1=Star                               |
| 6491     | names    | have    | a          | format JHHMMSS.ss+DDMMS.ss with a missing "0" in arcseconds             |
| 3        | bands.   | Note    | (3):       | Photometry flag as follows:                                             |
| 0        | =        | good    | photometry | 1 = bright stars and spikes associated with those stars; photometry for |
| 2        | =        | edges   | of         | the image as measured from the F160W rms maps.                          |

**Note**: Warning: the format should be JHHMMSS.ss+DDMMSS.s but 6491 names
    have a format JHHMMSS.ss+DDMMS.ss with a missing "0" in arcseconds
    (format should be JHHMMSS.ss+DDMM0S.s). Note added by CDS (a column with
    corrected names is added in VizieR).
Note (2): F160W FLUX AUTO/FLUX ISO, applied to ACS and WFC3 bands.
Note (3): Photometry flag as follows:
    0 = good photometry
    1 = bright stars and spikes associated with those stars; photometry for
         objects contaminated by this would be unreliable
    2 = edges of the image as measured from the F160W rms maps.

</details>

<details>
<summary>table10.dat</summary>

| Bytes   | Format      | Units               | Label      | Explanations                                          |
|:--------|:------------|:--------------------|:-----------|:------------------------------------------------------|
| 1- 5    | I5          | ---                 | Seq        | SExtractor identifier from F160W image                |
| 7- 14   | F8.4        | ---                 | zspec      | [0.0027/2.5]?=-99 Spectroscopic redshift              |
| 16- 18  | I3          | ---                 | q_zspec    | [-99/3] Quality flag on zspec (1)                     |
| 20- 26  | F7.3        | ---                 | Wuyts      | [0/10]?=-99 Wuyts photometric redshift (2)            |
| 28- 34  | F7.3        | ---                 | 68lWuyts   | ?=-99 Lower 68% confidence level in 68lWuyts          |
| 36- 42  | F7.3        | ---                 | 68uWuyts   | ?=-99 Upper 68% confidence level in 68uWuyts          |
| 44- 50  | F7.3        | ---                 | 95lWuyts   | ?=-99 Lower 95% confidence level in 95lWuyts          |
| 52- 58  | F7.3        | ---                 | 95uWuyts   | ?=-99 Upper 95% confidence level in 95uWuyts          |
| 60- 65  | F6.3        | ---                 | Pforr      | [0.001/10] Pforr photometric redshift (2)             |
| 67- 71  | F5.3        | ---                 | 68lPforr   | Lower 68% confidence level in 68lPforr                |
| 73- 78  | F6.3        | ---                 | 68uPforr   | Upper 68% confidence level in 68uPforr                |
| 80- 84  | F5.3        | ---                 | 95lPforr   | Lower 95% confidence level in 95lPforr                |
| 86- 91  | F6.3        | ---                 | 95uPforr   | Upper 95% confidence level in 95uPforr                |
| 93- 98  | F6.3        | ---                 | Wiklind    | [0.05/10] Wiklind photometric redshift (2)            |
| 100-104 | F5.3        | ---                 | 68lWiklind | Lower 68% confidence level in 68lWiklind              |
| 106-111 | F6.3        | ---                 | 68uWiklind | Upper 68% confidence level in 68uWiklind              |
| 113-117 | F5.3        | ---                 | 95lWiklind | Lower 95% confidence level in 95lWiklind              |
| 119-124 | F6.3        | ---                 | 95uWiklind | Upper 95% confidence level in 95uWiklind              |
| 126-130 | F5.3        | ---                 | Finkel     | [0/10] Finkelstein photometric redshift (2)           |
| 132-136 | F5.3        | ---                 | 68lFinkel  | Lower 68% confidence level in 68lFinkel               |
| 138-142 | F5.3        | ---                 | 68uFinkel  | Upper 68% confidence level in 68uFinkel               |
| 144-148 | F5.3        | ---                 | 95lFinkel  | Lower 95% confidence level in 95lFinkel               |
| 150-154 | F5.3        | ---                 | 95uFinkel  | Upper 95% confidence level in 95uFinkel               |
| 156-162 | F7.3        | ---                 | Gruetz     | [0/10]?=-99 Gruetz photometric redshift (2)           |
| 164-170 | F7.3        | ---                 | 68lGruetz  | ?=-99 Lower 68% confidence level in 68lGruetz         |
| 172-178 | F7.3        | ---                 | 68uGruetz  | ?=-99 Upper 68% confidence level in 68uGruetz         |
| 180-186 | F7.3        | ---                 | 95lGruetz  | ?=-99 Lower 95% confidence level in 95lGruetz         |
| 188-194 | F7.3        | ---                 | 95uGruetz  | ?=-99 Upper 95% confidence level in 95uGruetz         |
| 196-202 | F7.3        | ---                 | Salvato    | [0.03/10]?=-99 Salvato photometric                    |
| 204-210 | F7.3        | ---                 | 68lSalvato | ?=-99 Lower 68% confidence level in 68lSalvato        |
| 212-218 | F7.3        | ---                 | 68uSalvato | ?=-99 Upper 68% confidence level in 68uSalvato        |
| 220-224 | F5.3        | ---                 | 95lSalvato | Lower 95% confidence level in 95lSalvato              |
| 226-230 | F5.3        | ---                 | 95uSalvato | Upper 95% confidence level in 95uSalvato              |
| 1       | =           | secure              | (418       | occurrences),                                         |
| 2       | =           | intermediate        | (114       | occurrences),                                         |
| 3       | =           | uncertain           | (116       | occurrences),                                         |
| 99      | =           | no                  | value      | (38023 occurrences).                                  |
| 7       | in          | Appendix            | B,         | excerpt below:                                        |
| 418     | Brammer+    | 2008ApJ...686.1503B | Erb+       | 2010ApJ...719.1168E                                   |
| 05      | Bolzonella+ | 2000A&A...363..476B | Maraston   | 2005MNRAS.362..799M                                   |
| 03      | Wiklind+    | 2008ApJ...676..781W | Wuyts      | EAZY    EAZY             Brammer+ 2008ApJ...686.1503B |

**Note**: Quality flag as follows:
    1 = secure (418 occurrences),
    2 = intermediate (114 occurrences),
    3 = uncertain (116 occurrences),
  -99 = no value (38023 occurrences).
Note (2): References for each of these model codes are provided in Table 7
          in Appendix B, excerpt below:
 
 PI           Code    Template Set     References
 
 Finkelstein  EAZY    EAZY+BX418       Brammer+ 2008ApJ...686.1503B
                                       Erb+ 2010ApJ...719.1168E
 Gruetzbauch  EAZY    EAZY             Brammer+ 2008ApJ...686.1503B
 Pforr        HyperZ  Maraston05       Bolzonella+ 2000A&A...363..476B
                                       Maraston 2005MNRAS.362..799M
 Salvato      LePhare BC03+Polletta    Arnouts & Ilbert 2011ascl.soft08009A
                                       Bruzual & Charlot 2003MNRAS.344.1000B
                                       Polletta+ 2007ApJ...663...81P
 Wiklind      WikZ    BC03             Wiklind+ 2008ApJ...676..781W
 Wuyts        EAZY    EAZY             Brammer+ 2008ApJ...686.1503B

</details>

<details>
<summary>table11.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                     |
|:--------|:---------|:--------|:----------|:-------------------------------------------------|
| 1- 5    | I5       | ---     | Seq       | SExtractor identifier from F160W image           |
| 7- 12   | F6.3     | mag     | Hmag      | [12.7/32.6]?=99 F160W SExtractor MAG AUTO        |
| 14- 14  | I1       | ---     | PFlag     | [0/2] Photometry flag (0=good; otherwise         |
| 16- 19  | F4.2     | ---     | G/S       | SExtractor stellar classification; 1=Star        |
| 21- 21  | I1       | ---     | AGN       | AGN flag; 1=AGN                                  |
| 23- 30  | F8.4     | ---     | zbest     | [0/10]?=-99 Best phot or spectroscopic           |
| 32- 39  | F8.4     | ---     | zspec     | [0/5.7]?=-99 Spectroscopic redshift              |
| 41- 43  | I3       | ---     | q_zspec   | [-99/3] Quality of zspec; 1=good                 |
| 45- 49  | F5.3     | ---     | zphot     | [0/10] Photometric redshift                      |
| 51- 56  | F6.2     | ---     | zphotl68  | ?=-99 Lower 68% confidence level in zphot        |
| 58- 62  | F5.2     | ---     | zphotu68  | Upper 68% confidence level in zphot              |
| 64- 69  | F6.2     | ---     | zphotl95  | ?=-99 Lower 95% confidence level in zphot        |
| 71- 75  | F5.2     | ---     | zphotu95  | Upper 95% confidence level in zphot              |
| 77- 82  | F6.2     | ---     | zCOSMOS   | [0/10]?=-99 COSMOS catalog photometric           |
| 84- 91  | E8.2     | [Msun]  | Mass      | [4.2/14] Log CANDELS reference median stellar    |
| 93-100  | E8.2     | [Msun]  | e_Mass    | [0.006/6] Standard deviation on Mass             |
| 102-109 | E8.2     | [Msun]  | Mneb      | [3.4/13.6] Log median stellar mass include       |
| 111-119 | E9.2     | [Msun]  | e_Mneb    | [0/4]?=-99 Standard deviation on Mneb            |
| 121-126 | F6.2     | [Msun]  | M14cons   | [-43/12.1] Log stellar mass from                 |
| 128-133 | F6.2     | [Msun]  | M11tau    | [7/12]?=-99 Log stellar mass from                |
| 135-139 | F5.2     | [Msun]  | M6tauNEB  | [1.5/14] Log stellar mass from                   |
| 141-146 | F6.2     | [Msun]  | M13tau    | [3.9/14.4]?=-99 Log stellar mass from            |
| 148-152 | F5.2     | [Msun]  | M12       | [-9/13.1] Log stellar mass from Method 12        |
| 154-158 | F5.2     | [Msun]  | M6tau     | [1.5/13.7] Log stellar mass from Method 6_tau    |
| 160-164 | F5.2     | [Msun]  | M2tau     | [3.7/14] Log stellar mass from Method 2_tau      |
| 166-170 | F5.2     | [Msun]  | M6deltau  | [1.7/13.5] Log stellar mass from                 |
| 172-176 | F5.2     | [Msun]  | M6invtau  | [1.5/13.4] Log stellar mass from                 |
| 178-183 | F6.2     | [Msun]  | M10       | [2.6/14]?=-99 Log stellar mass from Method 10    |
| 185-190 | F6.2     | [Msun]  | M4        | [1.3/14]?=-99 Log stellar mass from Method 4     |
| 192-197 | F6.2     | [Msun]  | M14lin    | [6.3/12]?=-99 Log stellar mass from              |
| 199-204 | F6.2     | [Msun]  | M14deltau | [6.3/12]?=-99 Log stellar mass from              |
| 206-211 | F6.2     | [Msun]  | M14tau    | [6.3/11.8]?=-99 Log stellar mass from            |
| 213-218 | F6.2     | [Msun]  | M14inctau | [6.3/12.1]?=-99 Log stellar mass from            |
| 220-225 | F6.2     | [Msun]  | M14       | [6.3/11.7]?=-99 Log stellar mass                 |
| 14      | 227-234  | E8.2    | [Msun]    | Mneblin   [3.4/13.6] Log median stellar mass (1) |
| 236-244 | E9.2     | [Msun]  | e_Mneblin | [0/194]?=-99 Standard deviation                  |
| 246-253 | E8.2     | [Msun]  | Mlin      | [4.5/13.8] Log median stellar mass (2)           |
| 255-262 | E8.2     | [Msun]  | e_Mlin    | [0.006/102000] Standard deviation in Mlin        |

**Note**: Including nebular component calculated by the Hodges-Lehmann
          estimator in the linear space and standard deviation.
Note (2): With no nebular component calculated by the Hodges-Lehmann estimator
          in the linear space and standard deviation.

</details>
