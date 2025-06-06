**Authors:** Ferguson H.C., Giavalisco M., Barro G., Willner S.P., Ashby M.L.N.,, Dahlen T., Donley J.L., Faber S.M., Fontana A., Galametz A., Grazian A.,, Huang K.-H., Kocevski D.D., Koekemoer A.M., Koo D.C., McGrath E.J.,, Peth M., Salvato M., Wuyts S., Castellano M., Cooray A.R., Dickinson M.E.,, Dunlop J.S., Fazio G.G., Gardner J.P., Gawiser E., Grogin N.A., Hathi N.P.,, Hsu L.-T., Lee K.-S., Lucas R.A., Mobasher B., Nandra K., Newman J.A.,, van der Wel A., <Astrophys. J. Suppl. Ser., 207, 24 (2013)>, =2013ApJS..207...24G

## Summary: GOODS-S CANDELS multiwavelength catalog 

We present a UV to mid-infrared multi-wavelength catalog in the CANDELS/GOODS-S field, combining the newly obtained CANDELS HST/WFC3 F105W, F125W, and F160W data with existing public data. The catalog is based on source detection in the WFC3 F160W band. The F160W mosaic includes the data from CANDELS deep and wide observations as well as previous ERS and HUDF09 programs. The mosaic reaches a 5{sigma} limiting depth (within an aperture of radius 0.17") of 27.4, 28.2, and 29.7 AB for CANDELS wide, deep, and HUDF regions, respectively. The catalog contains 34930 sources with the representative 50% completeness reaching 25.9, 26.6, and 28.1 AB in the F160W band for the three regions. In addition to WFC3 bands, the catalog also includes data from UV (U band from both CTIO/MOSAIC and VLT/VIMOS), optical (HST/ACS F435W, F606W, F775W, F814W, and F850LP), and infrared (HST/WFC3 F098M, VLT/ISAAC Ks, VLT/HAWK-I Ks, and Spitzer/IRAC 3.6, 4.5, 5.8, 8.0{mu}m) observations. The catalog is validated via stellar colors, comparison with other published catalogs, zero-point offsets determined from the best-fit templates of the spectral energy distribution of spectroscopically observed objects, and the accuracy of photometric redshifts. The catalog is able to detect unreddened star-forming (passive) galaxies with stellar mass of 10^10^M_{sun}_ at a 50% completeness level to z~3.4 (2.8), 4.6 (3.2), and 7.0 (4.2) in the three regions. As an example of application, the catalog is used to select both star-forming and passive galaxies at z~2-4 via the Balmer break. It is also used to study the color-magnitude diagram of galaxies at 0<z<4.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-207-24/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes   | Format     | Units            | Label        | Explanations                                                                  |
|:--------|:-----------|:-----------------|:-------------|:------------------------------------------------------------------------------|
| 1- 5    | I5         | ---              | Seq          | F160W SExtractor running sequence number                                      |
| 7- 24   | A18        | ---              | ---          | [CANDELS_GDS_F160W_]                                                          |
| 25- 43  | A19        | ---              | Name         | IAU name (JHHMMSS.ss+DDMMSS.s)                                                |
| 45- 54  | F10.7      | deg              | RAdeg        | [52.9/53.3] F160W right ascension (J2000) (RA)                                |
| 56- 66  | F11.7      | deg              | DEdeg        | [-28/-27.6] F160W declination (J2000) (DEC)                                   |
| 68- 73  | F6.2       | mag              | Hlim         | [26.3/30.3]?=-99 F160W limiting                                               |
| 75      | I1         | ---              | Q            | [0/3]? Source reliability (0=ok) (2)                                          |
| 77- 81  | F5.3       | ---              | S/G          | [0/1] F160W SExtractor S/G classifier output                                  |
| 83- 94  | E12.6      | uJy              | FU           | [-210.1/2603] Blanco/CTIO U flux                                              |
| 96-106  | E11.6      | uJy              | e_FU         | [0/0.08] FU uncertainty                                                       |
| 108-118 | E11.6      | ---              | w_FU         | [84507/118675] Blanco/CTIO U weight                                           |
| 120-131 | E12.6      | uJy              | FUv          | [-0.4/774] VLT/VIMOS U flux                                                   |
| 133-143 | E11.6      | uJy              | e_FUv        | [0/0.3] FUv uncertainty                                                       |
| 145-155 | E11.6      | ---              | w_FUv        | [0.01/0.05] VLT/VIMOS U weight                                                |
| 157-168 | E12.6      | uJy              | F435W        | [-0.7/333]?=-99 HST/ACS F435W flux                                            |
| 170-181 | E12.6      | uJy              | e_F435W      | [0/2.5]?=-99 F435W uncertainty                                                |
| 183-193 | E11.6      | ---              | w_F435W      | [0/148492]?=0 ACS F435W weight (3)                                            |
| 195-206 | E12.6      | uJy              | F606W        | [-0.5/965]?=-99 HST/ACS F606W flux                                            |
| 208-219 | E12.6      | uJy              | e_F606W      | [0/2.9]?=-99 F606W uncertainty                                                |
| 221-231 | E11.6      | ---              | w_F606W      | [0/151645]?=0 ACS F606W weight (3)                                            |
| 233-244 | E12.6      | uJy              | F775W        | [-0.4/1481]?=-99 HST/ACS F775W flux                                           |
| 246-257 | E12.6      | uJy              | e_F775W      | [0/7.8]?=-99 F775W uncertainty                                                |
| 259-269 | E11.6      | ---              | w_F775W      | [0/361449]?=0 ACS F775W weight (3)                                            |
| 271-282 | E12.6      | uJy              | F814W        | [-1.5/1884]?=-99 HST/ACS F814W flux                                           |
| 284-295 | E12.6      | uJy              | e_F814W      | [0/6.1]?=-99 F814W uncertainty                                                |
| 297-307 | E11.6      | ---              | w_F814W      | [0/35593]?=0 ACS F814W weight (3)                                             |
| 309-320 | E12.6      | uJy              | F850LP       | [-3.5/2163]?=-99 HST/ACS F850LP flux                                          |
| 322-333 | E12.6      | uJy              | e_F850LP     | [0/4.8]?=-99 F850LP uncertainty                                               |
| 335-345 | E11.6      | ---              | w_F850LP     | [0/366976]?=0 ACS F850LP weight (3)                                           |
| 347-358 | E12.6      | uJy              | F098M        | [-1.6/10005]?=-99 HST/WFC3 F098M flux                                         |
| 360-371 | E12.6      | uJy              | e_F098M      | [0/1.3]?=-99 F098M uncertainty                                                |
| 373-383 | E11.6      | ---              | w_F098M      | [0/9655]?=0 WFC3 F098M weight (3)                                             |
| 385-396 | E12.6      | uJy              | F105W        | [-68.4/11423]?=-99 HST/WFC3 F105W flux                                        |
| 398-409 | E12.6      | uJy              | e_F105W      | [0/2.8]?=-99 F105W uncertainty                                                |
| 411-421 | E11.6      | ---              | w_F105W      | [0/76124]?=0 WFC3 F105W weight (3)                                            |
| 423-434 | E12.6      | uJy              | F125W        | [-0.5/11714]?=-99 HST/WFC3 F125W flux                                         |
| 436-447 | E12.6      | uJy              | e_F125W      | [0/2.5]?=-99 F125W uncertainty                                                |
| 449-459 | E11.6      | ---              | w_F125W      | [0/107528]?=0 WFC3 F125W weight (3)                                           |
| 461-472 | E12.6      | uJy              | F160W        | [-0.1/11446]?=-99 HST/WFC3 F160W flux                                         |
| 474-485 | E12.6      | uJy              | e_F160W      | [0/0.8]?=-99 F160W uncertainty                                                |
| 487-497 | E11.6      | ---              | w_F160W      | [0/159492]?=0 WFC3 F160W weight (3)                                           |
| 499-510 | E12.6      | uJy              | FKsI         | [-1.1/7370]?=-99 VLT/ISAAC Ks flux                                            |
| 512-523 | E12.6      | uJy              | e_FKsI       | [0.03/0.8]?=-99 FKsI uncertainty                                              |
| 525-535 | E11.6      | ---              | w_FKsI       | [0/255]?=0 VLT/ISAAC KS weight                                                |
| 537-548 | E12.6      | uJy              | FKsH         | [-0.5/3342]?=-99 VLT/HAWK-I Ks flux                                           |
| 550-561 | E12.6      | uJy              | e_FKsH       | [0/1]?=-99 FKsH uncertainty                                                   |
| 563-573 | E11.6      | ---              | w_FKsH       | [0/336]?=0 HAWK-I Ks weight                                                   |
| 575-586 | E12.6      | uJy              | Fch1         | [-1734.1/4843] Spitzer/IRAC 3.5um (CH1) flux                                  |
| 588-598 | E11.6      | uJy              | e_Fch1       | [0.04/1.5] Fch1 uncertainty                                                   |
| 600-610 | E11.6      | ---              | w_Fch1       | [124/4399] IRAC CH1 weight                                                    |
| 612-623 | E12.6      | uJy              | Fch2         | [-236/2120] Spitzer/IRAC 4.5um (CH2) flux                                     |
| 625-635 | E11.6      | uJy              | e_Fch2       | [0.03/0.8] Fch2 uncertainty                                                   |
| 637-647 | E11.6      | ---              | w_Fch2       | [368/5390] IRAC CH2 weight                                                    |
| 649-660 | E12.6      | uJy              | Fch3         | [-1726/2685] Spitzer/IRAC 5.8um (CH3) flux                                    |
| 662-673 | E12.6      | uJy              | e_Fch3       | [0.2/279307]?=-99 FCH3 uncertainty                                            |
| 675-685 | E11.6      | ---              | w_Fch3       | [0/576826]?=0 IRAC CH3 WEIGHT                                                 |
| 687-698 | E12.6      | uJy              | Fch4         | [-330.1/8822] Spitzer/IRAC 8um (CH4) flux                                     |
| 700-710 | E11.6      | uJy              | e_Fch4       | [0.2/60476] Fch4 uncertainty                                                  |
| 712-722 | E11.6      | ---              | w_Fch4       | [626/60270] IRAC CH4 weight                                                   |
| 724-735 | E12.6      | uJy              | FI(H)        | [-1.4/11838] F160W isophotal flux                                             |
| 737-747 | E11.6      | uJy              | e_FI(H)      | FI(H) uncertainty                                                             |
| 749-760 | E12.6      | uJy              | FA(H)        | [-0.002/11446] SExtractor F160W (FLUX_AUTO)                                   |
| 762-772 | E11.6      | uJy              | e_FA(H)      | [0.0008/9.8] FA(H) uncertainty                                                |
| 774-781 | F8.4       | pix              | FWHM(H)      | [-9.6/521.4] FWHM of F160W                                                    |
| 1       | pixel=0.06 | arcsec)          | (FWHM_IMAGE) | 783-789  F7.3  pix     a(H)    [0.5/181] F160W SExtractor profile RMS along   |
| 791-796 | F6.3       | pix              | b(H)         | [0.2/42] F160W SExtractor profile RMS along                                   |
| 798-803 | F6.3       | ---              | r1(H)        | [0/11.9] F160W SExtractor Kron aperture                                       |
| 805-811 | F7.3       | pix              | Fr1(H)       | [-1.3/113] F160W SExtractor 20% of light                                      |
| 813-819 | F7.3       | pix              | Fr2(H)       | [-3.3/172] F160W SExtractor 50% of light                                      |
| 821-828 | F8.3       | pix              | Fr3(H)       | [-304/253] F160W SExtractor 80% of light                                      |
| 830-834 | F5.1       | deg              | PA           | [-90/90] F160W SExtractor position angle                                      |
| 835-836 | A2         | ---              | ---          | [0]                                                                           |
| 838-844 | F7.3       | ---              | FHap         | [-28/470] F160W FLUX_AUTO / FLUX_ISO, applied                                 |
| 3       | bands      | (APCORR)         | 846          | I1    ---     H/C     [0/1] Source is a hot detection (1) or a                |
| 848-852 | I5         | pix2             | A(H)         | [4/90330] SExtractor F160W isophotal area                                     |
| 853-855 | A3         | ---              | ---          | [.00]                                                                         |
| 1       | arcsec2,   | and              | zp           | is the zero point of F160W.                                                   |
| 0       | =          | non-contaminated | sources      | 1 = sources detected on star spikes, halos; and the bright stars that produce |
| 2       | =          | sources          | detected     | by SExtractor at the image edges or on the few artifacts                      |
| 3       | =          | sources          | with         | both the flag of "1" and "2".                                                 |
| 08      | pixels,    | these            | parameters   | are replaced by FLUX_APER and FLUXERR_APER measured                           |
| 08      | pixels).   | See              | Section      | 3.2 for details.                                                              |

**Note**: The limiting magnitude here is derived as
      m_lim_=-2.5log_10_(A<{sigma}^2^>)^0.5^+zp, 
  where <{sigma}^2^> is the average of the squared rms in the SExtractor
  F160W segmentation map of each source, A is the area of 1 arcsec2, and
  zp is the zero point of F160W.
Note (2): Flag as follows:
  0 = non-contaminated sources
  1 = sources detected on star spikes, halos; and the bright stars that produce
      those spikes and halos
  2 = sources detected by SExtractor at the image edges or on the few artifacts
      of the F160W image
  3 = sources with both the flag of "1" and "2".
Note (3): In HST bands, the weight is the exposure time of the source,
     while in other bands, it is a relative weight.
Note (4): For sources whose isophotal radius smaller than 2.08 pixels,
     these parameters are replaced by FLUX_APER and FLUXERR_APER measured
     within a radius of 0.125" (2.08 pixels). See Section 3.2 for details.

</details>
