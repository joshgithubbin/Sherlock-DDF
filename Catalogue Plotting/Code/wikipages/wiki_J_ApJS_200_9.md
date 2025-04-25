**Authors:** Cooper M.C., Newman J.A., Moustakas L.A., Stern D.,, Comerford J.M., Davis M., Lotz J.M., Barden M., Conselice C.J., Capak P.L.,, Faber S.M., Kirkpatrick J.D., Koekemoer A.M., Koo D.C., Noeske K.G.,, Scoville N., Sheth K., Shopbell P., Willmer C.N.A., Weiner B., <Astrophys. J. Suppl. Ser., 200, 9 (2012)>, =2012ApJS..200....9G

## Summary: The ACS-GC catalog 

We present the Advanced Camera for Surveys General Catalog (ACS-GC), a photometric and morphological database using publicly available data obtained with the Advanced Camera for Surveys (ACS) instrument on the Hubble Space Telescope. The goal of the ACS-GC database is to provide a large statistical sample of galaxies with reliable structural and distance measurements to probe the evolution of galaxies over a wide range of look-back times. The ACS-GC includes approximately 470000 astronomical sources (stars + galaxies) derived from the AEGIS, COSMOS, GEMS, and GOODS surveys. Galapagos code (Hausler et al. 2011ASPC..442..155H) was used to construct photometric (SExtractor) and morphological (Galfit) catalogs. The analysis assumes a single Sersic model for each object to derive quantitative structural parameters. We include publicly available redshifts from the DEEP2, COMBO-17, TKRS, PEARS, ACES, CFHTLS, and zCOSMOS surveys to supply redshifts (spectroscopic and photometric) for a considerable fraction (~74%) of the imaging sample. The ACS-GC includes color postage stamps, Galfit residual images, and photometry, structural parameters, and redshifts combined into a single catalog.

## Spectroscopic Redshift 
 
**zsp:**  
 

## Photometric Redshift 
 
**zph:**  
 

## Catalogue Schema

<details>
<summary>acs-gc.dat</summary>

| Bytes   | Format              | Units       | Label    | Explanations                                                          |
|:--------|:--------------------|:------------|:---------|:----------------------------------------------------------------------|
| 1- 8    | I8                  | ---         | ObjNo    | Unique object number (OBJNO) (1)                                      |
| 10- 17  | I8                  | ---         | Survey   | ?=- Unique survey ID if available (SURVEY_ID)                         |
| 19- 28  | F10.6               | deg         | RAdeg    | Right Ascension (J2000) (RA)                                          |
| 30- 39  | F10.6               | deg         | DEdeg    | Declination (DEC)                                                     |
| 41- 42  | I2                  | ---         | Nf1      | [0/23] Total number of objects simultaneously                         |
| 1       | (NTOT_HI)           | 44-         | 45       | I2    ---     Nf2      [0/15]? Total number of objects simultaneously |
| 2       | (NTOT_LOW)          | 47-         | 53       | A7    ---     Imaging  Imaging survey: AEGIS, COSMOS, GEMS,           |
| 55- 63  | F9.6                | ---         | zsp      | ? Spectroscopic redshift (SPECZ)                                      |
| 65- 70  | F6.3                | ---         | zph      | ? Photometric redshift (PHOTOZ)                                       |
| 72- 78  | F7.1                | ---         | zchi2    | ? Reduced {chi}^2^ for zph (PHOTOZ_CHI2)                              |
| 80- 85  | F6.3                | ---         | e_zph    | ? Error on zph (PHOTOZ_ERR) (2)                                       |
| 87- 91  | F5.1                | ---         | q_zsp    | [-2/212]? Quality flag for zsp (ZQUALITY) (3)                         |
| 93-103  | A11                 | ---         | r_zsp    | Origin of zsp (Z_ORIGIN)                                              |
| 105-113 | F9.6                | ---         | z        | ? Best available redshift (Z)                                         |
| 115-120 | F6.3                | ---         | Bmag     | ? B-band apparent magnitude (MAGB)                                    |
| 122-127 | F6.3                | ---         | e_Bmag   | ? Error in Bmag (MAGB_ERR)                                            |
| 129-134 | F6.3                | ---         | Rmag1    | ? R-band apparent magnitude (MAGR)                                    |
| 136-141 | F6.3                | ---         | e_Rmag1  | ? Error in Rmag (MAGR_ERR)                                            |
| 143-148 | F6.3                | ---         | Imag1    | ? I-band apparent magnitude (MAGI)                                    |
| 150-155 | F6.3                | ---         | e_Imag1  | ? Error in Imag (MAGI_ERR)                                            |
| 157-162 | F6.3                | ---         | umag     | ? u-band apparent magnitude (CFHT_U)                                  |
| 164-169 | F6.3                | ---         | e_umag   | ? Error in umag (CFHT_U_ERR)                                          |
| 171-176 | F6.3                | ---         | gmag     | ? g-band apparent magnitude (CFHT_G)                                  |
| 178-183 | F6.3                | ---         | e_gmag   | ? Error in gmag (CFHT_G_ERR)                                          |
| 185-190 | F6.3                | ---         | rmag     | ? r-band apparent magnitude (CFHT_R)                                  |
| 192-197 | F6.3                | ---         | e_rmag   | ? Error in rmag (CFHT_R_ERR)                                          |
| 199-204 | F6.3                | ---         | imag     | ? i-band apparent magnitude (CFHT_I)                                  |
| 206-211 | F6.3                | ---         | e_imag   | ? Error in imag (CFHT_I_ERR)                                          |
| 213-218 | F6.3                | ---         | zmag     | ? z-band apparent magnitude (CFHT_Z)                                  |
| 220-225 | F6.3                | ---         | e_zmag   | ? Error in zmag (CFHT_Z_ERR)                                          |
| 227-232 | F6.3                | ---         | E(B-V)   | [0/0.5]? Extinction (color excess) (EBV)                              |
| 234-248 | A15                 | ---         | Class    | Source classification from DEEP2 and                                  |
| 250-255 | F6.3                | mag/arcsec2 | mu1      | ? Surface brightness in filter#1 (MU_HI)                              |
| 257-262 | F6.3                | mag/arcsec2 | mu2      | ? Surface brightness in filter#2 (MU_LOW)                             |
| 264-268 | F5.1                | deg         | PAim1    | [-90/90] SExtractor image orientation,                                |
| 1       | (THETA_IMAGE_HI)    | 270-274     | F5.1     | deg     PAim2    [-90/90]? SExtractor image orientation,              |
| 2       | (THETA_IMAGE_LOW)   | 276-280     | F5.1     | deg     PA1      [-90/90] SExtractor position angle,                  |
| 1       | (THETA_WORLD_HI)    | 282-286     | F5.1     | deg     PA2      [-90/90]? SExtractor position angle,                 |
| 1       | (THETA_WORLD_LOW)   | 288-292     | F5.3     | ---     b/a1     [0/1] SExtractor axis ratio b/a,                     |
| 1       | (BA_HI)             | 294-298     | F5.3     | ---     b/a2     [0/1]? SExtractor axis ratio b/a,                    |
| 2       | (BA_LOW)            | 300-304     | F5.2     | ---     rKron1   [0/14] SExtractor Kron radius,                       |
| 1       | (KRON_RADIUS_HI)    | 306-310     | F5.2     | ---     rKron2   [0/14]? SExtractor Kron radius,                      |
| 2       | (KRON_RADIUS_LOW)   | 312-317     | F6.2     | pix     FWHM1    SExtractor full width at half maximum,               |
| 1       | (FWHM_HI            | 319-324     | F6.2     | pix     FWHM2    ? SExtractor full width at half maximum,             |
| 2       | (FWHM_LOW)          | 326-332     | F7.3     | pix     a1       SExtractor major axis, filter#1 (A_IMAGE_HI)         |
| 334-340 | F7.3                | pix         | a2       | ? SExtractor major axis, filter#2 (A_IMAGE_LOW)                       |
| 342-348 | F7.3                | pix         | b1       | SExtractor minor axis, filter#1 (B_IMAGE_HI)                          |
| 350-356 | F7.3                | pix         | b2       | ? SExtractor minor axis, filter#2 (B_IMAGE_LOW)                       |
| 358-364 | F7.3                | ct          | bg1      | ? SExtractor sky background,                                          |
| 1       | (BACKGROUND_HI)     | 366-372     | F7.3     | ct      bg2      ? SExtractor sky background,                         |
| 2       | (BACKGROUND_LOW)    | 374-383     | E10.4    | ct      Fbest1   SExtractor best flux, filt#1 (FLUX_BEST_HI)          |
| 385-394 | E10.4               | ct          | Fbest2   | ? SExtractor best flux, filt#2 (FLUX_BEST_LOW)                        |
| 396-404 | E9.3                | ct          | e_Fbest1 | Error on Fbest1 (FLUXERR_BEST_HI)                                     |
| 406-414 | E9.3                | ct          | e_Fbest2 | ? Error on Fbest2 (FLUXERR_BEST_LOW)                                  |
| 416-421 | F6.3                | mag         | mbest1   | ?=0 SExtractor best magnitude,                                        |
| 1       | (MAG_BEST_HI)       | 423-428     | F6.3     | mag     mbest2   ? SExtractor best magnitude,                         |
| 2       | (MAG_BEST_LOW)      | 430-435     | F6.3     | mag   e_mbest1   ? Error on mbest1 (MAGERR_BEST_HI)                   |
| 437-442 | F6.3                | mag         | e_mbest2 | ? Error on mbest2 (MAGERR_BEST_LOW)                                   |
| 444-451 | F8.3                | pix         | Re.S1    | ? SExtractor effective radius,                                        |
| 1       | (FLUX_RADIUS_HI)    | 453-460     | F8.3     | pix     Re.S2    ? SExtractor effective radius,                       |
| 2       | (FLUX_RADIUS_LOW)   | 462-468     | I7       | pix     Area1    ? SExtractor isophotal area,                         |
| 1       | (ISOAREA_IMAGE_HI)  | 470-476     | I7       | pix     Area2    ? SExtractor isophotal area,                         |
| 2       | (ISOAREA_IMAGE_LOW) | 478-479     | I2       | ---     Sf1      [0/31]? SExtractor flags,                            |
| 1       | (SEX_FLAGS_HI)      | 481-482     | I2       | ---     Sf2      [0/31]? SExtractor flags,                            |
| 2       | (SEX_FLAGS_LOW)     | 484         | I1       | ---     Gf1      GALFIT flag: 0=good, 1=bad (FLAG_GALFIT_HI)          |
| 486     | I1                  | ---         | Gf2      | ? GALFIT flag: 0=good, 1=bad (FLAG_GALFIT_LOW)                        |
| 488-499 | E12.5               | ---         | Gchi1    | ? GALFIT reduced {chi}^2^ (CHI2NU_HI)                                 |
| 501-512 | E12.5               | ---         | Gchi2    | ? GALFIT reduced {chi}^2^ (CHI2NU_LOW)                                |
| 514-517 | F4.2                | ---         | s/g1     | [0/1] SExtractor star(1)/galaxy(0) class                              |
| 519-522 | F4.2                | ---         | s/g2     | [0/1]? SExtractor star(1)/galaxy(0) class                             |
| 524-531 | F8.2                | pix         | Xpos1    | GALFIT X position (X_GALFIT_HI)                                       |
| 533-540 | F8.2                | pix         | Xpos2    | ? GALFIT X position (X_GALFIT_LOW)                                    |
| 542-549 | F8.2                | pix         | Ypos1    | GALFIT Y position (Y_GALFIT_HI)                                       |
| 551-558 | F8.2                | pix         | Ypos2    | ? GALFIT Y position (Y_GALFIT_LOW)                                    |
| 560-564 | F5.2                | mag         | mGal1    | ?=0 GALFIT magnitude, filter#1 (MAG_GALFIT_HI)                        |
| 566-570 | F5.2                | mag         | mGal2    | ? GALFIT magnitude, filter#2 (MAG_GALFIT_LOW)                         |
| 572-577 | F6.2                | pix         | Re.G1    | GALFIT effective radius (RE_GALFIT_HI)                                |
| 579-584 | F6.2                | pix         | Re.G2    | ? GALFIT effective radius (RE_GALFIT_LOW)                             |
| 586-589 | F4.2                | ---         | n.G1     | [0/8]? GALFIT Sersic index (N_GALFIT_HI)                              |
| 591-594 | F4.2                | ---         | n.G2     | [0/8]? GALFIT Sersic index (N_GALFIT_LOW)                             |
| 596-601 | F6.2                | ---         | b/a.G1   | [0/360]? GALFIT axis ratio (BA_GALFIT_HI)                             |
| 603-608 | F6.2                | ---         | b/a.G2   | [0/360]? GALFIT axis ratio (BA_GALFIT_LOW)                            |
| 610-615 | F6.2                | deg         | pa.G1    | [-90/90]? GALFIT position angle (PA_GALFIT_HI)                        |
| 617-622 | F6.2                | deg         | pa.G2    | [-90/90]? GALFIT position angle (PA_GALFIT_LOW)                       |
| 624-629 | F6.2                | ct          | bg.G1    | GALFIT background (SKY_GALFIT_HI)                                     |
| 631-636 | F6.2                | ct          | bg.G2    | ? GALFIT background (SKY_GALFIT_LOW)                                  |
| 638-642 | F5.2                | mag         | e_mGal1  | ? Error on mGal1 (MAGERR_GALFIT_HI)                                   |
| 644-648 | F5.2                | mag         | e_mGal2  | ? Error on mGal2 (MAGERR_GALFIT_LOW)                                  |
| 650-655 | F6.2                | pix         | e_Re.G1  | ? Error on Re.G1 (REERR_GALFIT_HI)                                    |
| 657-662 | F6.2                | pix         | e_Re.G2  | ? Error on Re.G2 (REERR_GALFIT_LOW)                                   |
| 664-667 | F4.2                | ---         | e_n.G1   | ? Error on n.G1 (NERR_GALFIT_HI)                                      |
| 669-672 | F4.2                | ---         | e_n.G2   | ? Error on n.G2 (NERR_GALFIT_LOW)                                     |
| 674-678 | F5.2                | ---         | e_b/a.G1 | ? Error on b/a.G1 (BAERR_GALFIT_HI)                                   |
| 680-684 | F5.2                | ---         | e_b/a.G2 | ? Error on b/a.G2 (BAERR_GALFIT_LOW)                                  |
| 686-691 | F6.2                | deg         | e_pa.G1  | ? Error on pa.G1 (PAERR_GALFIT_HI)                                    |
| 693-698 | F6.2                | deg         | e_pa.G2  | ? Error on pa.G2 (PAERR_GALFIT_LOW)                                   |
| 700-711 | A12                 | ---         | Morph    | Visual morphology classification (VIS_MORPH)                          |
</details>

<details>
<summary>refs.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                               |
|:--------|:---------|:--------|:--------|:-------------------------------------------|
| 1- 14   | A14      | ---     | Ref     | Origin of spectroscopic redshift (zORIGIN) |
| 16- 33  | A18      | ---     | Auth    | First author's name                        |
| 35- 53  | A19      | ---     | BibCode | Bibcode                                    |
| 55- 74  | A20      | ---     | Note    | Note                                       |
</details>
