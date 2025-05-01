**Authors:** Salvato M., Nandra K., Brusa M., Bender R., Buchner J.,, Donley J.L., Kocevski D.D., Guo Y., Hathi N.P., Rangel C., Willner S.P.,, Brightman M., Georgakakis A., Budavari T., Szalay A.S., Ashby M.L.N.,, Barro G., Dahlen T., Faber S.M., Ferguson H.C., Galametz A., Grazian A.,, Grogin N.A., Huang K.-H., Koekemoer A.M., Lucas R.A., Mcgrath E.,, Mobasher B., Peth M., Rosario D.J., Trump J.R., <Astrophys. J., 796, 60 (2014)>, =2014ApJ...796...60H (SIMBAD/NED BibCode)

## Summary: ECDFS galaxies photometric redshifts & counterparts 

We present photometric redshifts and associated probability distributions for all detected sources in the Extended Chandra Deep Field South (ECDFS). This work makes use of the most up-to-date data from the Cosmic Assembly Near-IR Deep Legacy Survey (CANDELS) and the Taiwan ECDFS Near-Infrared Survey (TENIS) in addition to other data. We also revisit multi-wavelength counterparts for published X-ray sources from the 4Ms CDFS and 250ks ECDFS surveys, finding reliable counterparts for 1207 out of 1259 sources (~96%). Data used for photometric redshifts include intermediate-band photometry deblended using the TFIT method, which is used for the first time in this work. Photometric redshifts for X-ray source counterparts are based on a new library of active galactic nuclei/galaxy hybrid templates appropriate for the faint X-ray population in the CDFS. Photometric redshift accuracy for normal galaxies is 0.010 and for X-ray sources is 0.014 and outlier fractions are 4% and 5.2%, respectively. The results within the CANDELS coverage area are even better, as demonstrated both by spectroscopic comparison and by galaxy-pair statistics. Intermediate-band photometry, even if shallow, is valuable when combined with deep broadband photometry. For best accuracy, templates must include emission lines.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-796-60/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zspec:** [0.001/4.8]?=-99 Spectroscopic redshift 
 

## Photometric Redshift 
 
**zphot:** [0/6.7]?=-99 The photo-z value (zp) as defined 
 

## Catalogue Schema

<details>
<summary>table8.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                      |
|:--------|:---------|:--------|:----------|:--------------------------------------------------|
| 1- 6    | I6       | ---     | [HSN2014] | [1/105176] Running sequence number                |
| 8- 12   | I5       | ---     | CANDELS   | [1/34930]?=-99 ID from the CANDELS catalog (G1)   |
| 14- 23  | F10.6    | deg     | RACdeg    | [/53.3]?=-99 CANDELS right ascension (J2000)      |
| 25- 34  | F10.6    | deg     | DECdeg    | [/-27.6]?=-99 CANDELS declination (J2000)         |
| 36- 40  | I5       | ---     | MUSYC     | [0/84401]?=-99 ID from the MUSYC catalog (G1)     |
| 42- 51  | F10.6    | deg     | RAMdeg    | [/53.5]?=-99 MUSYC right ascension (J2000)        |
| 53- 62  | F10.6    | deg     | DEMdeg    | [/-27.5]?=-99 MUSYC declination (J2000)           |
| 64- 68  | I5       | ---     | TENIS     | [6/62326]?=-99 ID from the TENIS catalog (G1)     |
| 70- 79  | F10.6    | deg     | RATdeg    | [/53.5]?=-99 TENIS right ascension (J2000)        |
| 81- 90  | F10.6    | deg     | DETdeg    | [/-27.5]?=-99 TENIS declination (J2000)           |
| 92- 96  | I5       | ---     | SIMPLE    | [4985/54262]?=-99 ID from the SIMPLE catalog (G1) |
| 98-107  | F10.6    | deg     | RASdeg    | [/53.5]?=-99 TENIS right ascension (J2000)        |
| 109-118 | F10.6    | deg     | DESdeg    | [/-27.5]?=-99 TENIS declination (J2000)           |
| 120-122 | I3       | ---     | R13       | [1/570]?=-99 ID from R13 4Ms-CDFS catalog (G1)    |
| 124-133 | F10.6    | deg     | RARdeg    | [/53.4]?=-99 R13 right ascension (J2000)          |
| 135-144 | F10.6    | deg     | DERdeg    | [/-27.6]?=-99 R13 declination (J2000)             |
| 146-151 | F6.2     | ---     | errR13    | [0.1/1.4]?=-99 Positional error from R13          |
| 153-155 | I3       | ---     | X11       | [2/740]?=-99 ID from X11 4Ms-CDFS catalog (G1)    |
| 157-166 | F10.6    | deg     | RAXdeg    | [/53.4]?=-99 X11 right ascension (J2000)          |
| 168-177 | F10.6    | deg     | DEXdeg    | [/-27.6]?=-99 X11 declination (J2000)             |
| 179-183 | F5.1     | ---     | errX11    | [0.1/1.5]?=-99 Positional error from X11          |
| 185-187 | I3       | ---     | L05       | [2/762]?=-99 ID from L05 250ks-ECDFS catalog (G1) |
| 189-197 | F9.5     | deg     | RALdeg    | [/53.5]?=-99 L05 right ascension (J2000)          |
| 199-207 | F9.5     | deg     | DELdeg    | [/-27.5]?=-99 L05 declination (J2000)             |
| 209-213 | F5.1     | ---     | errL05    | [0.6/2.2]?=-99 Positional error from L05          |
| 215-217 | I3       | ---     | V06       | [2/651]?=-99 ID from V06 250ks-ECDFS catalog (G1) |
| 219-227 | F9.5     | deg     | RAVdeg    | [/53.5]?=-99 V06 right ascension (J2000)          |
| 229-237 | F9.5     | deg     | DEVdeg    | [/-27.5]?=-99 V06 declination (J2000)             |
| 239-244 | F6.2     | ---     | errV06    | [0.1/3]?=-99 Positional error from V06            |
| 246-248 | I3       | ---     | Flag      | [-99/7] Flag on counterpart (G2)                  |
| 250-256 | F7.3     | ---     | Prob      | [-99/1] Posterior value (p) (G3)                  |
</details>

<details>
<summary>table9.dat</summary>

| Bytes   | Format   | Units    | Label     | Explanations                                                                |
|:--------|:---------|:---------|:----------|:----------------------------------------------------------------------------|
| 1- 3    | I3       | ---      | R13       | [1/571]?=-99 ID from R13 4Ms-CDFS catalog (G1)                              |
| 5- 7    | I3       | ---      | X11       | [1/740]?=-99 ID from X11 4Ms-CDFS catalog (G1)                              |
| 9- 11   | I3       | ---      | L05       | [1/762]?=-99 ID from L05 250ks-ECDFS (G1)                                   |
| 13- 15  | I3       | ---      | V06       | [1/651]?=-99 ID from V06 250ks-ECDFS (G1)                                   |
| 17- 25  | F9.6     | deg      | RAdeg     | [52.7/53.5] Right ascension of the X-ray                                    |
| 27- 36  | F10.6    | deg      | DEdeg     | [-28.2/-27.5] Declination of the X-ray                                      |
| 38- 46  | E9.3     | 10-3W/m2 | F0.5-2    | Soft band X-ray flux (0.5-2keV;                                             |
| 48- 56  | E9.3     | 10-3W/m2 | F2-8      | Hard band X-ray flux (2-8keV;                                               |
| 58- 66  | E9.3     | 10-3W/m2 | F0.5-8    | Full band X-ray flux (0.5-8keV;                                             |
| 68- 74  | F7.3     | 10-7W    | L0.5-2    | [35.3/45]?=-99 Soft band X-ray luminosity                                   |
| 76- 82  | F7.3     | 10-7W    | L2-8      | [38.8/45.2]?=-99 Hard band X-ray luminosity                                 |
| 84- 90  | F7.3     | 10-7W    | L0.5-8    | [35.6/45.4]?=-99 Full band X-ray luminosity                                 |
| 92- 98  | F7.3     | 10-7W    | L2-10     | [38.9/45.3]?=-99 2-10keV hard band X-ray                                    |
| 100-107 | F8.4     | ---      | zbest     | [0/6.9]?=-99 Redshift used to calculate Lx (3)                              |
| 109-116 | F8.4     | ---      | zspec     | [0.001/4.8]?=-99 Spectroscopic redshift                                     |
| 118-125 | F8.4     | ---      | zphot     | [0/6.9]?=-99 Photometric redshift (4)                                       |
| 127-132 | I6       | ---      | [HSN2014] | [125/105176]?=-99 ID of the Optical/NIR/MIR                                 |
| 2014    | (this    | paper)   | Note      | (1): We chose the original X-ray data from, in order of priority, R13, X11, |
| 05      | and      | V06.     | Note      | (2): The X-ray luminosity is the rest-frame luminosity uncorrected for      |
| 4       | Note     | (3):     | We        | used reliable spec-z if available, otherwise photo-z as in                  |
| 2014    | (this    | work).   | Note      | (4): Check the detail information in the photo-z catalog (table 11).        |

**Note**: We chose the original X-ray data from, in order of priority, R13, X11,
          L05 and V06.
Note (2): The X-ray luminosity is the rest-frame luminosity uncorrected for
          absorption.
          Lx=4*pi*luminosityDistance^2*fx*(1+zbest)^(gamma-2), where gamma=1.4
Note (3): We used reliable spec-z if available, otherwise photo-z as in
          Hsu+ 2014 (this work).
Note (4): Check the detail information in the photo-z catalog (table 11).

</details>

<details>
<summary>table10.dat</summary>

| Bytes   | Format                         | Units              | Label         | Explanations                                                              |
|:--------|:-------------------------------|:-------------------|:--------------|:--------------------------------------------------------------------------|
| 1- 6    | I6                             | ---                | [HSN2014]     | [72/105150] Sequential number adopted in                                  |
| 8- 10   | I3                             | ---                | R13           | [1/570]?=-99 ID from R13 4Ms-CDFS catalog (G1)                            |
| 12- 14  | I3                             | ---                | X11           | [1/740]?=-99 ID from X11 4Ms-CDFS catalog (G1)                            |
| 16- 18  | I3                             | ---                | L05           | [2/756]?=-99 ID from L05 250ks-ECDFS (G1)                                 |
| 20- 22  | I3                             | ---                | V06           | [2/651]?=-99 ID from V06 250ks-ECDFS (G1)                                 |
| 24      | I1                             | ---                | Flag          | [1/7] Flag on counterpart (G2)                                            |
| 26- 32  | F7.3                           | ---                | Prob          | [0.6/1] Posterior value (p) (G3)                                          |
| 34- 45  | F12.9                          | deg                | RAdeg         | [52.8/53.5] Opt/NIR/MIR right ascension                                   |
| 47- 59  | F13.9                          | deg                | DEdeg         | [-28.1/-27.5] Opt/NIR/MIR declination                                     |
| 61- 67  | F7.3                           | mag                | FUVmag        | [19.8/26]?=-99 GALEX FUV AB magnitude (2)                                 |
| 69- 75  | F7.3                           | mag                | e_FUVmag      | [/0.5]?=-99 FUVmag uncertainty                                            |
| 77- 83  | F7.3                           | mag                | NUVmag        | [15/27]?=-99 GALEX NUV AB magnitude (2)                                   |
| 85- 91  | F7.3                           | mag                | e_NUVmag      | [/0.7]?=-99 NUVmag uncertainty                                            |
| 93- 99  | F7.3                           | mag                | UCTIO         | [17.5/32]?=-99 Blanco/Mosaic-II U-band AB                                 |
| 101-107 | F7.3                           | mag                | e_UCTIO       | [0/17]?=-99 UCTIO uncertainty                                             |
| 109-115 | F7.3                           | mag                | UVIMOS        | [17.7/35.4]?=-99 VLT/VIMOS U-band AB                                      |
| 117-123 | F7.3                           | mag                | e_UVIMOS      | [/35]?=-99 UVIMOS uncertainty                                             |
| 125-131 | F7.3                           | mag                | F435W         | [17.5/35]?=-99 HST/ACS F435W AB magnitude (2)                             |
| 133-139 | F7.3                           | mag                | e_F435W       | [/263]?=-99 F435W uncertainty                                             |
| 141-147 | F7.3                           | mag                | F606W         | [16/31]?=-99 HST/ACS F606W AB magnitude (2)                               |
| 149-155 | F7.3                           | mag                | e_F606W       | [0/5]?=-99 F606W uncertainty                                              |
| 157-163 | F7.3                           | mag                | F775W         | [15.9/32]?=-99 HST/ACS F775W AB magnitude (2)                             |
| 165-171 | F7.3                           | mag                | e_F775W       | [0/24]?=-99 F775W uncertainty                                             |
| 173-179 | F7.3                           | mag                | F814W         | [15.6/32]?=-99 HST/ACS F814W AB magnitude (2)                             |
| 181-187 | F7.3                           | mag                | e_F814W       | [0/41]?=-99 F814W uncertainty                                             |
| 189-195 | F7.3                           | mag                | F850LP        | [15.5/30]?=-99 HST/ACS F850LP AB magnitude (2)                            |
| 197-203 | F7.3                           | mag                | e_F850LP      | [0/5]?=-99 F850LP uncertainty                                             |
| 205-211 | F7.3                           | mag                | F098M         | [16/30]?=-99 HST/WFC3 F098M AB magnitude (2)                              |
| 213-219 | F7.3                           | mag                | e_F098M       | [0/6]?=-99 F098M uncertainty                                              |
| 221-227 | F7.3                           | mag                | F105W         | [15/29]?=-99 HST/WFC3 F105W AB magnitude (2)                              |
| 229-235 | F7.3                           | mag                | e_F105W       | [0/4]?=-99 F105W uncertainty                                              |
| 237-243 | F7.3                           | mag                | F125W         | [15/32]?=-99 HST/WFC3 F125W AB magnitude (2)                              |
| 245-251 | F7.3                           | mag                | e_F125W       | [0/6]?=-99 F125W uncertainty                                              |
| 253-259 | F7.3                           | mag                | F140W         | [14/29]?=-99 HST/WFC3 F140W AB magnitude (2)                              |
| 261-267 | F7.3                           | mag                | e_F140W       | [0/3]?=-99 F140W uncertainty                                              |
| 269-275 | F7.3                           | mag                | F160W         | [14.8/27.5]?=-99 HST/WFC3 F160W AB magnitude (2)                          |
| 277-283 | F7.3                           | mag                | e_F160W       | [0/0.4]?=-99 F160W uncertainty                                            |
| 285-291 | F7.3                           | mag                | KsISAAC       | [14.8/29]?=-99 VLT/ISAAC Ks-band AB                                       |
| 293-299 | F7.3                           | mag                | e_KsISAAC     | [0/9]?=-99 KsISAAC uncertainty                                            |
| 301-307 | F7.3                           | mag                | KsHAWKI       | [15.9/30]?=-99 VLT/HAWK-I Ks-band AB                                      |
| 309-315 | F7.3                           | mag                | e_KsHAWKI     | [0/5]?=-99 KsHAWKI uncertainty                                            |
| 317-323 | F7.3                           | mag                | IA427         | [12.7/32]?=-99 Subaru IA427 AB magnitude (2)                              |
| 325-331 | F7.3                           | mag                | e_IA427       | [0/42]?=-99 IA427 uncertainty                                             |
| 333-339 | F7.3                           | mag                | IA445         | [14.8/33]?=-99 Subaru IA445 AB magnitude (2)                              |
| 341-347 | F7.3                           | mag                | e_IA445       | [0/88]?=-99 IA445 uncertainty                                             |
| 349-355 | F7.3                           | mag                | IA464         | [13/32]?=-99 Subaru IA464 AB magnitude (2)                                |
| 357-363 | F7.3                           | mag                | e_IA464       | [0/98]?=-99 IA464 uncertainty                                             |
| 365-371 | F7.3                           | mag                | IA484         | [16.5/34]?=-99 Subaru IA484 AB magnitude (2)                              |
| 373-379 | F7.3                           | mag                | e_IA484       | [0/135]?=-99 IA484 uncertainty                                            |
| 381-387 | F7.3                           | mag                | IA505         | [13/31]?=-99 Subaru IA505 AB magnitude (2)                                |
| 389-395 | F7.3                           | mag                | e_IA505       | [0/16]?=-99 IA505 uncertainty                                             |
| 397-403 | F7.3                           | mag                | IA527         | [16/32]?=-99 Subaru IA527 AB magnitude (2)                                |
| 405-411 | F7.3                           | mag                | e_IA527       | [0/18]?=-99 IA527 uncertainty                                             |
| 413-419 | F7.3                           | mag                | IA550         | [14.8/31]?=-99 Subaru IA550 AB magnitude (2)                              |
| 421-427 | F7.3                           | mag                | e_IA550       | [0/12]?=-99 IA550 uncertainty                                             |
| 429-435 | F7.3                           | mag                | IA574         | [13.8/34]?=-99 Subaru IA574 AB magnitude (2)                              |
| 437-443 | F7.3                           | mag                | e_IA574       | [0/255]?=-99 IA574 uncertainty                                            |
| 445-451 | F7.3                           | mag                | IA598         | [14.6/32]?=-99 Subaru IA598 AB magnitude (2)                              |
| 453-459 | F7.3                           | mag                | e_IA598       | [0/11]?=-99 IA598 uncertainty                                             |
| 461-467 | F7.3                           | mag                | IA624         | [14/35]?=-99 Subaru IA624 AB magnitude (2)                                |
| 469-475 | F7.3                           | mag                | e_IA624       | [0/265]?=-99 IA624 uncertainty                                            |
| 477-483 | F7.3                           | mag                | IA651         | [14.7/32]?=-99 Subaru IA651 AB magnitude (2)                              |
| 485-491 | F7.3                           | mag                | e_IA651       | [0/11]?=-99 IA651 uncertainty                                             |
| 493-499 | F7.3                           | mag                | IA679         | [15/32]?=-99 Subaru IA679 AB magnitude (2)                                |
| 501-507 | F7.3                           | mag                | e_IA679       | [0/23]?=-99 IA679 uncertainty                                             |
| 509-515 | F7.3                           | mag                | IA709         | [14.5/32]?=-99 Subaru IA709 AB magnitude (2)                              |
| 517-523 | F7.3                           | mag                | e_IA709       | [0/135]?=-99 IA709 uncertainty                                            |
| 525-531 | F7.3                           | mag                | IA738         | [14.7/31]?=-99 Subaru IA738 AB magnitude (2)                              |
| 533-539 | F7.3                           | mag                | e_IA738       | [0/6]?=-99 IA738 uncertainty                                              |
| 541-547 | F7.3                           | mag                | IA767         | [14.9/31]?=-99 Subaru IA767 AB magnitude (2)                              |
| 549-555 | F7.3                           | mag                | e_IA767       | [0/15]?=-99 IA767 uncertainty                                             |
| 557-563 | F7.3                           | mag                | IA797         | [15/33]?=-99 Subaru IA797 AB magnitude (2)                                |
| 565-571 | F7.3                           | mag                | e_IA797       | [0/136]?=-99 IA797 uncertainty                                            |
| 573-579 | F7.3                           | mag                | IA827         | [15/33]?=-99 Subaru IA827 AB magnitude (2)                                |
| 581-587 | F7.3                           | mag                | e_IA827       | [0/411]?=-99 IA827 uncertainty                                            |
| 589-595 | F7.3                           | mag                | IA856         | [14.7/32]?=-99 Subaru IA856 AB magnitude (2)                              |
| 597-603 | F7.3                           | mag                | e_IA856       | [0/89]?=-99 IA856 uncertainty                                             |
| 605-611 | F7.3                           | mag                | U38mag        | [13.9/31]?=-99 WFI/ESO MPG U38 AB magnitude (2)                           |
| 613-619 | F7.3                           | mag                | e_U38mag      | [0/11]?=-99 U38mag uncertainty                                            |
| 621-627 | F7.3                           | mag                | Umag          | [14/31]?=-99 ESO MPG/WFI U-band AB magnitude (2)                          |
| 629-635 | F7.3                           | mag                | e_Umag        | [0/6]?=-99 Umag uncertainty                                               |
| 637-643 | F7.3                           | mag                | Bmag          | [14.5/30]?=-99 ESO MPG/WFI B-band AB                                      |
| 645-651 | F7.3                           | mag                | e_Bmag        | [0/2]?=-99 Bmag uncertainty                                               |
| 653-659 | F7.3                           | mag                | Vmag          | [14/30]?=-99 ESO MPG/WFI V-band AB magnitude (2)                          |
| 661-667 | F7.3                           | mag                | e_Vmag        | [0/2]?=-99 Vmag uncertainty                                               |
| 669-675 | F7.3                           | mag                | Rmag          | [14/27]?=-99 ESO MPG/WFI R-band AB magnitude (2)                          |
| 677-683 | F7.3                           | mag                | e_Rmag        | [0/2]?=-99 Rmag uncertainty                                               |
| 685-691 | F7.3                           | mag                | Imag          | [14/27]?=-99 ESO MPG/WFI I-band AB magnitude (2)                          |
| 693-699 | F7.3                           | mag                | e_Imag        | [0/2]?=-99 Imag uncertainty                                               |
| 701-707 | F7.3                           | mag                | zmag          | [12/28]?=-99 Blanco/Mosaic-II z-band AB                                   |
| 709-715 | F7.3                           | mag                | e_zmag        | [0/5]?=-99 zmag uncertainty                                               |
| 717-723 | F7.3                           | mag                | Jmag          | [10.8/31]?=-99 Blanco/ISPI J-band AB                                      |
| 725-731 | F7.3                           | mag                | e_Jmag        | [0/228]?=-99 Jmag uncertainty                                             |
| 733-739 | F7.3                           | mag                | Hmag          | [5.9/32]?=-99 ESO NTT/SofI H-band AB                                      |
| 741-747 | F7.3                           | mag                | e_Hmag        | [0/319]?=-99 Hmag uncertainty                                             |
| 749-755 | F7.3                           | mag                | Kmag          | [9.6/32]?=-99 Blanco/ISPI K-band AB                                       |
| 757-763 | F7.3                           | mag                | e_Kmag        | [0/560]?=-99 Kmag uncertainty                                             |
| 765-771 | F7.3                           | mag                | JTENIS        | [13/28]?=-99 CFHT/WIRCam J-band AB magnitude (2)                          |
| 773-779 | F7.3                           | mag                | e_JTENIS      | [0/5]?=-99 JTENIS uncertainty                                             |
| 781-787 | F7.3                           | mag                | KsTENIS       | [13/26]?=-99 CFHT/WIRCam Ks-band AB                                       |
| 789-795 | F7.3                           | mag                | e_KsTENIS     | [0/1]?=-99 KsTENIS uncertainty                                            |
| 797-803 | F7.3                           | mag                | 3.6mag        | [12/32]?=-99 Spitzer/IRAC 3.6um SEDS AB                                   |
| 805-811 | F7.3                           | mag                | e_3.6mag      | [0/61]?=-99 3.6mag uncertainty                                            |
| 813-819 | F7.3                           | mag                | 4.5mag        | [12.5/28]?=-99 Spitzer/IRAC 4.5um SEDS AB                                 |
| 821-827 | F7.3                           | mag                | e_4.5mag      | [0/3]?=-99 4.5mag uncertainty                                             |
| 829-835 | F7.3                           | mag                | 5.8mag        | [12/34]?=-99 Spitzer/IRAC 5.8um GOODS AB                                  |
| 837-844 | F8.3                           | mag                | e_5.8mag      | [0/1911]?=-99 5.8mag uncertainty                                          |
| 846-852 | F7.3                           | mag                | 8.0mag        | [13/30]?=-99 Spitzer/IRAC 8.0um GOODS AB                                  |
| 854-860 | F7.3                           | mag                | e_8.0mag      | [0/89]?=-99 8.0mag uncertainty                                            |
| 63      | |Blanco/Mosaic-II|1            | U-VIMOS^a          | |             | 3722|  297|27.97              |VLT/VIMOS       |1                         |
| 1       | F606W^a                        | |                  | 5918|         | 2324|29.35/31.05^b      |HST/ACS         |1                               |
| 1       | F814W^a                        | |                  | 8047|         | 1826|28.84              |HST/ACS         |1                               |
| 1       | F098M^a                        | |                  | 9851|         | 1696|28.77              |HST/WFC3        |1                               |
| 3       | |1                             | F125W^a            | |12486|       | 3005|27.66/28.34/29.78^c|HST/WFC3        |1                               |
| 3       | |1                             | F160W^a            | |15370|       | 2874|27.36/28.16/29.74^c|HST/WFC3        |1                               |
| 09      | |VLT/ISAAC                     | |1                 | Ks-HAWKI^a    | |21463| 3250|26.45              |VLT/HAWK-I      |1                       |
| 6       | mum-SEDS^a                     | |35508|            | 7432|26.52    | |Spitzer/IRAC    |1                                                       |
| 5       | mum-SEDS^a                     | |44960|10097|26.25 | |Spitzer/IRAC | |1                                                                        |
| 8       | mum-GOODS^a                    | |57245|13912|23.75 | |Spitzer/IRAC | |1                                                                        |
| 0       | mum-GOODS^a                    | |78840|28312|23.72 | |Spitzer/IRAC | |1                                                                        |
| 6       | mum-SIMPLE^e|35508|            | 7432|23.89         | |Spitzer/IRAC | |2, 3                                                                     |
| 5       | mum-SIMPLE^e|44960|10097|23.75 | |Spitzer/IRAC      | |2,           | 3                                                                         |
| 8       | mum-SIMPLE^e|57245|13912|22.42 | |Spitzer/IRAC      | |2,           | 3                                                                         |
| 0       | mum-SIMPLE^e|78840|28312|22.50 | |Spitzer/IRAC      | |2,           | 3                                                                         |
| 33      | |WFI/ESO                       | MPG                | |2,           | 3                                                                         |
| 86      | |ESO                           | MPG/WFI            | |2,           | 3                                                                         |
| 45      | |ESO                           | MPG/WFI            | |2,           | 3                                                                         |
| 27      | |ESO                           | MPG/WFI            | |2,           | 3                                                                         |
| 37      | |ESO                           | MPG/WFI            | |2,           | 3                                                                         |
| 30      | |ESO                           | MPG/WF             | |2,           | 3                                                                         |
| 69      | |Blanco/Mosaic-II|2,           | 3                  | J^e           | |12395| 1620|22.44              |Blanco/ISPI     |2, 3                    |
| 46      | |ESO                           | NTT/SofI           | |2,           | 3                                                                         |
| 98      | |Blanco/ISPI                   | |2,                | 3             | J^f             |12481| 1588|24.50              |CFHT/WIRCam     |2, 3    |
| 90      | |CFHT/WIRCam                   | |2,                | 3             | FUV^g           | 1543|  228|25.69              |GALEX           |1, 2, 3 |
| 99      | |GALEX                         | |1,                | 2,            | 3                                                                         |
| 01      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 18      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 38      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 22      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 29      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 18      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 45      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 16      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 05      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 91      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 14      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 02      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 52      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 93      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 92      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 69      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 60      | |Subaru                        | |1,                | 2,            | 3                                                                         |
| 41      | |Subaru                        | |1,                | 2,            | 3                                                                         |

**Note**: R.A. (J2000) and Dec. (J2000) of the optical/NIR/MIR source
          associated to the X-ray detection.
Note (2): Photometric data (table 1):
   
   Filter          |lam  |FWHM |5sigma Limiting    |Instrument      |Area
                   | eff |     |    Depth          | Telescope      |
                   |{AA} |{AA} |  (AB mag)         |                |
   
   U-CTIO^a        | 3734|  387|26.63              |Blanco/Mosaic-II|1
   U-VIMOS^a       | 3722|  297|27.97              |VLT/VIMOS       |1
   F435W^a         | 4317|  920|28.95/30.55^b      |HST/ACS         |1
   F606W^a         | 5918| 2324|29.35/31.05^b      |HST/ACS         |1
   F775W^a         | 7693| 1511|28.55/30.85^b      |HST/ACS         |1
   F814W^a         | 8047| 1826|28.84              |HST/ACS         |1
   F850LP^a        | 9055| 1236|28.55/30.25^b      |HST/ACS         |1
   F098M^a         | 9851| 1696|28.77              |HST/WFC3        |1
   F105W^a         |10550| 2916|27.45/28.45/29.45^c|HST/WFC3        |1
   F125W^a         |12486| 3005|27.66/28.34/29.78^c|HST/WFC3        |1
   F140W^a         |13635| 3947|26.89/29.84^d      |HST/WFC3        |1
   F160W^a         |15370| 2874|27.36/28.16/29.74^c|HST/WFC3        |1
   Ks-ISAAC^a      |21605| 2746|25.09              |VLT/ISAAC       |1
   Ks-HAWKI^a      |21463| 3250|26.45              |VLT/HAWK-I      |1
   3.6 mum-SEDS^a  |35508| 7432|26.52              |Spitzer/IRAC    |1
   4.5 mum-SEDS^a  |44960|10097|26.25              |Spitzer/IRAC    |1
   5.8 mum-GOODS^a |57245|13912|23.75              |Spitzer/IRAC    |1
   8.0 mum-GOODS^a |78840|28312|23.72              |Spitzer/IRAC    |1
   3.6 mum-SIMPLE^e|35508| 7432|23.89              |Spitzer/IRAC    |2, 3
   4.5 mum-SIMPLE^e|44960|10097|23.75              |Spitzer/IRAC    |2, 3
   5.8 mum-SIMPLE^e|57245|13912|22.42              |Spitzer/IRAC    |2, 3
   8.0 mum-SIMPLE^e|78840|28312|22.50              |Spitzer/IRAC    |2, 3
   U38^e           | 3706|  357|25.33              |WFI/ESO MPG     |2, 3
   U^e             | 3528|  625|25.86              |ESO MPG/WFI     |2, 3
   B^e             | 4554|  915|26.45              |ESO MPG/WFI     |2, 3
   V^e             | 5343|  900|26.27              |ESO MPG/WFI     |2, 3
   R^e             | 6411| 1602|26.37              |ESO MPG/WFI     |2, 3
   I^e             | 8554| 1504|24.30              |ESO MPG/WF      |2, 3
   z^e             | 8989| 1285|23.69              |Blanco/Mosaic-II|2, 3
   J^e             |12395| 1620|22.44              |Blanco/ISPI     |2, 3
   H^e             |16154| 2950|22.46              |ESO NTT/SofI    |2, 3
   K^e             |21142| 3312|21.98              |Blanco/ISPI     |2, 3
   J^f             |12481| 1588|24.50              |CFHT/WIRCam     |2, 3
   Ks^f            |21338| 3270|23.90              |CFHT/WIRCam     |2, 3
   FUV^g           | 1543|  228|25.69              |GALEX           |1, 2, 3
   NUV^g           | 2278|  796|25.99              |GALEX           |1, 2, 3
   IA427^e,h       | 4253|  210|25.01              |Subaru          |1, 2, 3
   IA445^e,h       | 4445|  204|25.18              |Subaru          |1, 2, 3
   IA464^e,h       | 4631|  216|24.38              |Subaru          |1, 2, 3
   IA484^e,h       | 4843|  230|26.22              |Subaru          |1, 2, 3
   IA505^e,h       | 5059|  234|25.29              |Subaru          |1, 2, 3
   IA527^e,h       | 5256|  243|26.18              |Subaru          |1, 2, 3
   IA550^e,h       | 5492|  276|25.45              |Subaru          |1, 2, 3
   IA574^e,h       | 5760|  276|25.16              |Subaru          |1, 2, 3
   IA598^e,h       | 6003|  297|26.05              |Subaru          |1, 2, 3
   IA624^e,h       | 6227|  300|25.91              |Subaru          |1, 2, 3
   IA651^e,h       | 6491|  324|26.14              |Subaru          |1, 2, 3
   IA679^e,h       | 6778|  339|26.02              |Subaru          |1, 2, 3
   IA709^e,h       | 7070|  321|24.52              |Subaru          |1, 2, 3
   IA738^e,h       | 7356|  324|25.93              |Subaru          |1, 2, 3
   IA768^e,h       | 7676|  366|24.92              |Subaru          |1, 2, 3
   IA797^e,h       | 7962|  354|24.69              |Subaru          |1, 2, 3
   IA827^e,h       | 8243|  339|23.60              |Subaru          |1, 2, 3
   IA856^e,h       | 8562|  324|24.41              |Subaru          |1, 2, 3
   
   Notes:
   a = CANDELS-TFIT catalog (Guo+ 2013, J/ApJS/207/24).
   b = Measurements from two regions: GOODS-S and HUDF09. See the details in
       Guo+ (2013, J/ApJS/207/24).
   c = Measurements from three regions: CANDELS wide, CANDELS deep, and HUDF09.
       See Guo+ (2013, J/ApJS/207/24) for details.
   d = Measurements from two regions: 3D-HST and HUDF12. This is an updated
       version of Guo+ (2013, J/ApJS/207/24).
   e = MUSYC catalog (Cardamone+ 2010, J/ApJS/189/270).
   f = TENIS catalog (Hsieh+ 2012ApJS..203...23H).
   g = GALEX DR6/7.
   h = IB-TFIT catalog (J. L. Donley et al. 2014, in preparation).

</details>

<details>
<summary>table11[ab].dat</summary>

| Bytes   | Format   | Units         | Label     | Explanations                                                            |
|:--------|:---------|:--------------|:----------|:------------------------------------------------------------------------|
| 1- 6    | I6       | ---           | [HSN2014] | [72/105176] Sequential number adopted in                                |
| 8- 10   | I3       | ---           | R13       | [1/570]?=-99 ID from R13 4Ms-CDFS catalog (G1)                          |
| 12- 14  | I3       | ---           | X11       | [1/740]?=-99 ID from X11 4Ms-CDFS catalog (G1)                          |
| 16- 18  | I3       | ---           | L05       | [2/762]?=-99 ID from L05 250ks-ECDFS (G1)                               |
| 20- 22  | I3       | ---           | V06       | [2/651]?=-99 ID from V06 250ks-ECDFS (G1)                               |
| 24      | I1       | ---           | Flag      | [1/7] Flag on counterpart (G2)                                          |
| 26- 30  | F5.3     | ---           | Prob      | [0.6/1] Posterior value (p) (G3)                                        |
| 32- 40  | F9.6     | deg           | RAdeg     | [52.8/53.5] Right ascension of the                                      |
| 42- 51  | F10.6    | deg           | DEdeg     | [-28.2/-27.5] Declination of the                                        |
| 53- 60  | F8.4     | ---           | zspec     | [0.001/4.8]?=-99 Spectroscopic redshift                                 |
| 62- 64  | I3       | ---           | q_zspec   | [-99/3]? Quality of the spectroscopic                                   |
| 66- 73  | F8.4     | ---           | zphot     | [0/6.7]?=-99 The photo-z value (zp) as defined                          |
| 75- 80  | F6.2     | ---           | e_zphot   | [0/6]?=-99 Lower 1-sigma value of zp                                    |
| 82- 87  | F6.2     | ---           | E_zphot   | [0/7]?=-99 Upper 1-sigma value of zp                                    |
| 89- 94  | F6.2     | ---           | e_zphot3  | [0/6]?=-99 Lower 3-sigma value of zp                                    |
| 96-101  | F6.2     | ---           | E_zphot3  | [0/7]?=-99 Upper 3-sigma value of zp                                    |
| 103-109 | F7.3     | ---           | Area      | [0/100]?=-99 Normalized area under the curve                            |
| 111-113 | I3       | ---           | Num       | [1/230]?=-99 Template number (2)                                        |
| 115-120 | F6.2     | ---           | zp2       | [0/7]?=-99 Second solution in the photo-z (zp2)                         |
| 5       | 122-128  | F7.3          | ---       | Area2    [0/82]?=-99 Normalized area under the curve                    |
| 130-132 | I3       | ---           | Num2      | [1/226]?=-99 Template number used for SED                               |
| 2       | (as      | in            | col.      | Num)                                                                    |
| 0       | =        | High,         | 1         | = Good,                                                                 |
| 2       | =        | Intermediate, | 3         | = Poor.                                                                 |
| 99      | =        | Unavailable.  | Note      | (2): Template number used for SED fitting for the best photo-z solution |
| 1- 48   | are      | the           | templates | from Lib-EXT;                                                           |
| 101-130 | are      | the           | templates | from Lib-PT;                                                            |
| 201-230 | are      | the           | templates | from S09;                                                               |

**Note**: Quality of the spectroscopic redshift as follows:
    0 = High,
    1 = Good,
    2 = Intermediate,
    3 = Poor.
  -99 = Unavailable.
Note (2): Template number used for SED fitting for the best photo-z solution
          listed in col zphot.
             1- 48 are the templates from Lib-EXT;
           101-130 are the templates from Lib-PT;
           201-230 are the templates from S09;

</details>
