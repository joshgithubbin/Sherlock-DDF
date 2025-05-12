**Authors:** Benitez N., Moles M., Fernandez-Soto A., Cristobal-Hornillos D.,, Ascaso B., Jimenez-Teja Y., Schoenell W., Arnalte-Mur P., Povic M., Coe D.,, Lopez-Sanjuan C., Diaz-Garcia L.A., Varela J., Stefanon M., Cenarro J.,, Matute I., Masegosa J., Marquez I., Perea J., Del Olmo A., Husillos C.,, Alfaro E., Aparicio-Villegas T., Cervino M., Huertas-Company M.,, Aguerri J.A.L., Broadhurst T., Cabrera-Cano J., Cepa J., Gonzalez R.M.,, Infante L., Martinez V.J., Prada F., Quintana J.M., <Mon. Not. R. Astron. Soc., 441, 2891-2922 (2014)>, =2014MNRAS.441.2891M (SIMBAD/NED BibCode)

## Summary: ALHAMBRA Survey 

The Advance Large Homogeneous Area Medium-Band Redshift Astronomical (ALHAMBRA) survey has observed eight different regions of the sky, including sections of the Cosmic Evolution Survey (COSMOS), DEEP2, European Large-Area Infrared Space Observatory Survey (ELAIS), Great Observatories Origins Deep Survey North (GOODS-N), Sloan Digital Sky Survey (SDSS) and Groth fields using a new photometric system with 20 optical, contiguous ~300{AA} filters plus the JHKs bands. The filter system is designed to optimize the effective photometric redshift depth of the survey, while having enough wavelength resolution for the identification of faint emission lines. The observations, carried out with the Calar Alto 3.5-m telescope using the wide-field optical camera Large Area Imager for Calar Alto (LAICA) and the near-infrared (NIR) instrument Omega-2000, represent a total of ~700h of on-target science images. Here we present multicolour point-spread function (PSF) corrected photometry and photometric redshifts for ~438000 galaxies, detected in synthetic F814W images. The catalogues are complete down to a magnitude I~24.5AB and cover an effective area of 2.79deg^2^. Photometric zero-points were calibrated using stellar transformation equations and refined internally, using a new technique based on the highly robust photometric redshifts measured for emission-line galaxies. We calculate Bayesian photometric redshifts with the Bayesian Photometric Redshift (bpz)2.0 code, obtaining a precision of {delta}z/(1+z_s_)=1 per cent for I<22.5 and {delta}z/(1+z_s_)=1.4 per cent for 22.5<I<24.5. The global n(z) distribution shows a mean redshift <z>=0.56 for I<22.5AB and <z>=0.86 for I<24.5AB. Given its depth and small cosmic variance, ALHAMBRA is a unique data set for galaxy evolution studies.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-441-2891/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Photometric Redshift 
 
**zml:** Maximum Likelihood most likely redshift (z_ml) 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-441-2891/Subcatalogues/COSMOS/Plots/zphot.png)
## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                   |
|:--------|:---------|:--------|:--------|:-----------------------------------------------|
| 1- 9    | A9       | ---     | HField  | ALHAMBRA sub-field designation fNNpNNcNN,      |
| 11- 13  | I3       | ---     | PID     | Identification number of the pair              |
| 15- 25  | I11      | ---     | ID1     | ALHAMBRA ID of principal galaxy                |
| 27- 37  | I11      | ---     | ID2     | ALHAMBRA ID of companion galaxy                |
| 39- 46  | F8.4     | deg     | RA1deg  | Right ascension of principal galaxy (J2000)    |
| 48- 54  | F7.4     | deg     | DE1deg  | Declination of principal galaxy (J2000)        |
| 56- 63  | F8.4     | deg     | RA2deg  | Right ascension of companion galaxy (J2000)    |
| 65- 71  | F7.4     | deg     | DE2deg  | Declination of companion galaxy (J2000)        |
| 73- 78  | F6.3     | arcsec  | theta   | Separation                                     |
| 80- 84  | F5.3     | ---     | z1      | Best photometric redshift of principal galaxy  |
| 86- 90  | F5.3     | ---     | z2      | Best photometric redshift of companion galaxy  |
| 92- 97  | F6.4     | ---     | PPF     | Integrated pair probability function           |
| 99-104  | F6.4     | ---     | PPFw    | Integrated PPF corrected by selection effects  |
| 106-110 | F5.2     | mag     | Imag1   | F814W magnitude of principal galaxy            |
| 112-116 | F5.2     | mag     | Imag2   | F814W magnitude of companion galaxy            |
| 118-122 | F5.3     | ---     | wosr1   | Odds weight of principal galaxy                |
| 124-128 | F5.3     | ---     | wosr2   | Odds weight of companion galaxy                |
| 130-134 | F5.3     | ---     | warea   | Average area weight of the pair                |
| 136-141 | F6.2     | mag     | BMAG1   | Absolute B magnitude of principal galaxy at z1 |
| 143-148 | F6.2     | mag     | BMAG2   | Absolute B magnitude of companion galaxy at z2 |
</details>

<details>
<summary>photom.dat</summary>

| Bytes   | Format          | Units       | Label      | Explanations                                                   |
|:--------|:----------------|:------------|:-----------|:---------------------------------------------------------------|
| 1- 9    | A9              | ---         | HField     | ALHAMBRA sub-field designation fNNpNNcNN                       |
| 11- 21  | I11             | ---         | ID         | Object ID Number                                               |
| 23      | I1              | ---         | Field      | ALHAMBRA field (Field)                                         |
| 25      | I1              | ---         | Pointing   | Pointing within the field (Pointing)                           |
| 27      | I1              | ---         | CCD        | Detector within the pointing (CCD)                             |
| 29- 36  | F8.4            | deg         | RAdeg      | Right Ascension (J2000) (RA)                                   |
| 38- 44  | F7.4            | deg         | DEdeg      | Declination (J2000) (Dec)                                      |
| 46- 53  | F8.3            | pix         | xpos       | X-pixel coordinate (x)                                         |
| 55- 62  | F8.3            | pix         | ypos       | Y-pixel coordinate (y)                                         |
| 64- 68  | I5              | pix         | Area       | Isophotal aperture area (area)                                 |
| 70- 75  | F6.2            | arcsec      | FWHM       | Full width at half maximum for detection                       |
| 77- 80  | F4.2            | ---         | Stell      | [0/1] SExtractor 'stellarity'                                  |
| 1       | =               | star;       | 0          | = galaxy) (stell)                                              |
| 82- 87  | F6.4            | ---         | ell        | Ellipticity = 1-b/a (ell)                                      |
| 89- 95  | F7.3            | pix         | amaj       | Profile RMS along major axis (a)                               |
| 97-102  | F6.3            | pix         | bmin       | Profile RMS along minor axis (b)                               |
| 104-108 | F5.1            | deg         | theta      | Position Angle (CCW/x) (theta)                                 |
| 110-114 | F5.2            | pix         | rk         | Kron apertures in units of A or B (rk)                         |
| 116-124 | F9.3            | pix         | rf         | Fraction-of-light radii (pixels) (rf)                          |
| 126-133 | F8.2            | ---         | S/N        | Signal to Noise                                                |
| 135-136 | I2              | ---         | PhotFlag   | SExtractor Photometric Flag (photoflag)                        |
| 137     | A1              | ---         | l_F365W    | Limit flag on F365W                                            |
| 138-144 | F7.3            | mag         | F365W      | ?=-99 Isophotal magnitude [AB] (F365W)                         |
| 146-151 | F6.3            | mag         | e_F365W    | ? Isophotal magnitude uncertainty [AB]                         |
| 152     | A1              | ---         | l_F396W    | Limit flag on F396W                                            |
| 153-159 | F7.3            | mag         | F396W      | ?=-99 Isophotal magnitude [AB] (F396W)                         |
| 161-166 | F6.3            | mag         | e_F396W    | ? Isophotal magnitude uncertainty [AB]                         |
| 167     | A1              | ---         | l_F427W    | Limit flag on F427W                                            |
| 168-174 | F7.3            | mag         | F427W      | ?=-99 Isophotal magnitude [AB] (F427W)                         |
| 176-181 | F6.3            | mag         | e_F427W    | ? Isophotal magnitude uncertainty [AB]                         |
| 182     | A1              | ---         | l_F458W    | Limit flag on F458W                                            |
| 183-189 | F7.3            | mag         | F458W      | ?=-99 Isophotal magnitude [AB] (F458W)                         |
| 191-196 | F6.3            | mag         | e_F458W    | ? Isophotal magnitude uncertainty [AB]                         |
| 197     | A1              | ---         | l_F489W    | Limit flag on F489W                                            |
| 198-204 | F7.3            | mag         | F489W      | ?=-99 Isophotal magnitude [AB] (F489W)                         |
| 206-211 | F6.3            | mag         | e_F489W    | ? Isophotal magnitude uncertainty [AB]                         |
| 212     | A1              | ---         | l_F520W    | Limit flag on F520W                                            |
| 213-219 | F7.3            | mag         | F520W      | ?=-99 Isophotal magnitude [AB] (F520W)                         |
| 221-226 | F6.3            | mag         | e_F520W    | ? Isophotal magnitude uncertainty [AB]                         |
| 227     | A1              | ---         | l_F551W    | Limit flag on F551W                                            |
| 228-234 | F7.3            | mag         | F551W      | ?=-99 Isophotal magnitude [AB] (F551W)                         |
| 236-241 | F6.3            | mag         | e_F551W    | ? Isophotal magnitude uncertainty [AB]                         |
| 242     | A1              | ---         | l_F582W    | Limit flag on F582W                                            |
| 243-249 | F7.3            | mag         | F582W      | ?=-99 Isophotal magnitude [AB] (F582W)                         |
| 251-256 | F6.3            | mag         | e_F582W    | ? Isophotal magnitude uncertainty [AB]                         |
| 257     | A1              | ---         | l_F613W    | Limit flag on F613W                                            |
| 258-264 | F7.3            | mag         | F613W      | ?=-99 Isophotal magnitude [AB] (F613W)                         |
| 266-271 | F6.3            | mag         | e_F613W    | ? Isophotal magnitude uncertainty [AB]                         |
| 272     | A1              | ---         | l_F644W    | Limit flag on F644W                                            |
| 273-279 | F7.3            | mag         | F644W      | ?=-99 Isophotal magnitude [AB] (F644W)                         |
| 281-286 | F6.3            | mag         | e_F644W    | ? Isophotal magnitude uncertainty [AB]                         |
| 287     | A1              | ---         | l_F675W    | Limit flag on F675W                                            |
| 288-294 | F7.3            | mag         | F675W      | ?=-99 Isophotal magnitude [AB] (F675W)                         |
| 296-301 | F6.3            | mag         | e_F675W    | ? Isophotal magnitude uncertainty [AB]                         |
| 302     | A1              | ---         | l_F706W    | Limit flag on F706W                                            |
| 303-309 | F7.3            | mag         | F706W      | ?=-99 Isophotal magnitude [AB] (F706W)                         |
| 311-316 | F6.3            | mag         | e_F706W    | ? Isophotal magnitude uncertainty [AB]                         |
| 317     | A1              | ---         | l_F737W    | Limit flag on F737W                                            |
| 318-324 | F7.3            | mag         | F737W      | ?=-99  Isophotal magnitude [AB] (F737W)                        |
| 326-331 | F6.3            | mag         | e_F737W    | ? Isophotal magnitude uncertainty [AB]                         |
| 332     | A1              | ---         | l_F768W    | Limit flag on F768W                                            |
| 333-339 | F7.3            | mag         | F768W      | ?=-99 Isophotal magnitude [AB] (F768W)                         |
| 341-346 | F6.3            | mag         | e_F768W    | ? Isophotal magnitude uncertainty [AB]                         |
| 347     | A1              | ---         | l_F799W    | Limit flag on F799W                                            |
| 348-354 | F7.3            | mag         | F799W      | ?=-99 Isophotal magnitude [AB] (F799W)                         |
| 356-361 | F6.3            | mag         | e_F799W    | ? Isophotal magnitude uncertainty [AB]                         |
| 362     | A1              | ---         | l_F830W    | Limit flag on F830W                                            |
| 363-369 | F7.3            | mag         | F830W      | ?=-99 Isophotal magnitude [AB] (F830W)                         |
| 371-376 | F6.3            | mag         | e_F830W    | ? Isophotal magnitude uncertainty [AB]                         |
| 377     | A1              | ---         | l_F861W    | Limit flag on F861W                                            |
| 378-384 | F7.3            | mag         | F861W      | ?=-99 Isophotal magnitude [AB] (F861W)                         |
| 386-391 | F6.3            | mag         | e_F861W    | ? Isophotal magnitude uncertainty [AB]                         |
| 392     | A1              | ---         | l_F892W    | Limit flag on F892W                                            |
| 393-399 | F7.3            | mag         | F892W      | ?=-99 Isophotal magnitude [AB] (F892W)                         |
| 401-406 | F6.3            | mag         | e_F892W    | ? Isophotal magnitude uncertainty [AB]                         |
| 407     | A1              | ---         | l_F923W    | Limit flag on F923W                                            |
| 408-414 | F7.3            | mag         | F923W      | ?=-99 Isophotal magnitude [AB] (F923W)                         |
| 416-421 | F6.3            | mag         | e_F923W    | ? Isophotal magnitude uncertainty [AB]                         |
| 422     | A1              | ---         | l_F954W    | Limit flag on F954W                                            |
| 423-428 | F6.3            | mag         | F954W      | Isophotal magnitude [AB] (F954W)                               |
| 430-435 | F6.3            | mag         | e_F954W    | ? Isophotal magnitude uncertainty [AB]                         |
| 436     | A1              | ---         | l_Jmag     | Limit flag on Jmag                                             |
| 437-443 | F7.3            | mag         | Jmag       | ?=-99 Isophotal magnitude [AB] (J)                             |
| 445-450 | F6.3            | mag         | e_Jmag     | ? Isophotal magnitude uncertainty [AB] (dJ)                    |
| 451     | A1              | ---         | l_Hmag     | Limit flag on Hmag                                             |
| 452-458 | F7.3            | mag         | Hmag       | ?=-99 Isophotal magnitude [AB] (H)                             |
| 460-465 | F6.3            | mag         | e_Hmag     | ? Isophotal magnitude uncertainty [AB] (dH)                    |
| 466     | A1              | ---         | l_Ksmag    | Limit flag on Ksmag                                            |
| 467-473 | F7.3            | mag         | Ksmag      | ?=-99 Isophotal magnitude [AB] (KS)                            |
| 475-480 | F6.3            | mag         | e_Ksmag    | ? Isophotal magnitude uncertainty [AB] (dKS)                   |
| 482-487 | F6.3            | mag         | F814W      | Isophotal magnitude [AB] (F814W)                               |
| 489-493 | F5.3            | mag         | e_F814W    | Isophotal magnitude uncertainty [AB] (dF814W)                  |
| 494     | A1              | ---         | l_F814W3   | Limit flag on F814W3                                           |
| 495-500 | F6.3            | mag         | F814W3     | 3arcsec Circular Aperture magnitude [AB]                       |
| 502-507 | F6.3            | mag         | e_F814W3   | ? 3arcsec Circular Aperture magnitude                          |
| 508-514 | F7.3            | mag         | F814W3c    | ?=-99 Corrected 3arcsec Circular Aperture                      |
| 516-517 | I2              | ---         | nfobs      | Number Filters Detected (out of 24) (nfobs)                    |
| 519     | I1              | ---         | xray       | [0/1] X-Ray Source [0:NO,1:YES]                                |
| 521-525 | F5.3            | %           | PercW      | Percentual Photometric Weight                                  |
| 527     | I1              | ---         | FSatur     | [0/1] Photometric Saturation-Flag                              |
| 529-532 | F4.2            | ---         | FStellar   | [0/1] Statistical STAR/GALAXY Discriminator                    |
| 534     | I1              | ---         | FDupDet    | [0/1] Duplicated Detection Flag                                |
| 536-540 | F5.3            | ---         | zb1        | BPZ most likely redshift for the First Peak                    |
| 542-546 | F5.3            | ---         | zb1l       | Lower limit (95p confidence) for the First                     |
| 548-552 | F5.3            | ---         | zb1u       | Upper limit (95p confidence) for the First                     |
| 554-559 | F6.3            | ---         | tb1        | BPZ most likely spectral type for the First                    |
| 561-565 | F5.3            | ---         | Odds1      | P(z) contained within zb +/- 2*0.01*(1+z) for                  |
| 567-571 | F5.3            | ---         | zml        | Maximum Likelihood most likely redshift (z_ml)                 |
| 573-578 | F6.3            | ---         | tml        | Maximum Likelihood most likely spectral type                   |
| 580-585 | F6.3            | ---         | Chi2       | ?=99 Poorness of BPZ fit: observed vs. model                   |
| 587-592 | F6.3            | [Msun]      | logM*1     | Stellar Mass for the First Peak                                |
| 594-600 | F7.3            | mag         | BMAG1      | Absolute Magnitude [AB] (B_JOHNSON) for the                    |
| 602-607 | F6.3            | mag         | BMAGPrior  | Magnitude Used for the Prior (F814W)                           |
| 609-613 | F5.3            | %           | irmsF365W  | Percentual Weight on F365W 1/RMS image                         |
| 615-619 | F5.3            | %           | irmsF396W  | Percentual Weight on F396W 1/RMS image                         |
| 621-625 | F5.3            | %           | irmsF427W  | Percentual Weight on F427W 1/RMS image                         |
| 627-631 | F5.3            | %           | irmsF458W  | Percentual Weight on F458W 1/RMS image                         |
| 633-637 | F5.3            | %           | irmsF489W  | Percentual Weight on F489W 1/RMS image                         |
| 639-643 | F5.3            | %           | irmsF520W  | Percentual Weight on F520W 1/RMS image                         |
| 645-649 | F5.3            | %           | irmsF551W  | Percentual Weight on F551W 1/RMS image                         |
| 651-655 | F5.3            | %           | irmsF582W  | Percentual Weight on F582W 1/RMS image                         |
| 657-661 | F5.3            | %           | irmsF613W  | Percentual Weight on F613W 1/RMS image                         |
| 663-667 | F5.3            | %           | irmsF644W  | Percentual Weight on F644W 1/RMS image                         |
| 669-673 | F5.3            | %           | irmsF675W  | Percentual Weight on F675W 1/RMS image                         |
| 675-679 | F5.3            | %           | irmsF706W  | Percentual Weight on F706W 1/RMS image                         |
| 681-685 | F5.3            | %           | irmsF737W  | Percentual Weight on F737W 1/RMS image                         |
| 687-691 | F5.3            | %           | irmsF768W  | Percentual Weight on F768W 1/RMS image                         |
| 693-697 | F5.3            | %           | irmsF799W  | Percentual Weight on F799W 1/RMS image                         |
| 699-703 | F5.3            | %           | irmsF830W  | Percentual Weight on F830W 1/RMS image                         |
| 705-709 | F5.3            | %           | irmsF861W  | Percentual Weight on F861W 1/RMS image                         |
| 711-715 | F5.3            | %           | irmsF892W  | Percentual Weight on F892W 1/RMS image                         |
| 717-721 | F5.3            | %           | irmsF923W  | Percentual Weight on F923W 1/RMS image                         |
| 723-727 | F5.3            | %           | irmsF954W  | Percentual Weight on F954W 1/RMS image                         |
| 729-733 | F5.3            | %           | irmsJ      | Percentual Weight on J 1/RMS image                             |
| 735-739 | F5.3            | %           | irmsH      | Percentual Weight on H 1/RMS image                             |
| 741-745 | F5.3            | %           | irmsKs     | Percentual Weight on Ks 1/RMS image                            |
| 747-751 | F5.3            | %           | irmsF814W  | Percentual Weight on F814W 1/RMS image                         |
| 753-754 | I2              | ---         | OPTFlag    | Optical-Quality-Flag. Number of Optical                        |
| 8       | (irms_OPT_Flag) | 756         | I1         | ---     NIRFlag   NIR-Quality-Flag. Number of NIR Filters with |
| 8       | (irms_NIR_Flag) | Note        | (1):       | Photometric Saturation-Flag as follows:                        |
| 0       | =               | Good        | Detection  | 1 = Saturated Detection                                        |
| 0       | =               | Pure-Galaxy | 0.5        | = Unknown                                                      |
| 1       | =               | Pure-Star   | Note       | (3): Duplicated Detection Flag as follows:                     |
| 0       | =               | Non         | duplicated | 1 = Duplicated                                                 |

**Note**: Photometric Saturation-Flag as follows:
  0 = Good Detection
  1 = Saturated Detection
Note (2): Statistical STAR/GALAXY Discriminator:
  0   = Pure-Galaxy
  0.5 = Unknown
  1   = Pure-Star
Note (3): Duplicated Detection Flag as follows:
  0 = Non duplicated
  1 = Duplicated

</details>
