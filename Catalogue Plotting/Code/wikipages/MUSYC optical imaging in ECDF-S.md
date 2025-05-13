**Authors:** Van Dokkum P.G., Urry C.M., Taniguchi Y., Gawiser E.,, Brammer G., Taylor E., Damen M., Treister E., Cobb B.E., Bond N.,, Schawinski K., Lira P., Murayama T., Saito T., Sumikawa K., <Astrophys. J. Suppl. Ser., 189, 270-285 (2010)>, =2010ApJS..189..270C

## Summary: MUSYC optical imaging in ECDF-S 

We present deep optical 18-medium-band photometry from the Subaru telescope over the ~30'x30' Extended Chandra Deep Field-South, as part of the Multiwavelength Survey by Yale-Chile (MUSYC). This field has a wealth of ground- and space-based ancillary data, and contains the GOODS-South field and the Hubble Ultra Deep Field. We combine the Subaru imaging with existing UBVRIzJHK and Spitzer IRAC images to create a uniform catalog. Detecting sources in the MUSYC "BVR" image we find ~40,000 galaxies with R_AB_<25.3, the median 5{sigma} limit of the 18 medium bands. Photometric redshifts are determined using the EAzY code and compared to ~2000 spectroscopic redshifts in this field. The medium-band filters provide very accurate redshifts for the (bright) subset of galaxies with spectroscopic redshifts, particularly at 0.1<z<1.2 and at z~>3.5. For 0.1<z<1.2, we find a 1{sigma} scatter in {DELTA}z/(1+z) of 0.007, similar to results obtained with a similar filter set in the COSMOS field. As a demonstration of the data quality, we show that the red sequence and blue cloud can be cleanly identified in rest-frame color-magnitude diagrams at 0.1<z<1.2. We find that ~20% of the red sequence galaxies show evidence of dust emission at longer rest-frame wavelengths. The reduced images, photometric catalog, and photometric redshifts are provided through the public MUSYC Web site (http://www.astro.yale.edu/MUSYC/).
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-189-270/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zsp:** ?=-1 Best Spectroscopic redshift 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-189-270/Subcatalogues/ECDFS/Plots/zspec.png)
<details>
<summary>Quality flag . . .</summary>

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-189-270/Subcatalogues/ECDFS/Plots/q_zspec.png)</details>
## Catalogue Schema

<details>
<summary>bvrdetv1.dat</summary>

| Bytes     | Format   | Units    | Label     | Explanations                                            |
|:----------|:---------|:---------|:----------|:--------------------------------------------------------|
| 4- 8      | I5       | ---      | Seq       | [0/84401] Sequential Object Identifier                  |
| 12- 21    | F10.6    | deg      | RAdeg     | Right ascension J2000 from SExtractor                   |
| 25- 34    | F10.6    | deg      | DEdeg     | Declination J2000 from SExtractor                       |
| 43- 47    | F5.3     | ---      | S/G       | [0/1] Sextractor neural network classifier,             |
| 0         | (Galaxy) | ->       | 1         | (star)                                                  |
| 55- 60    | F6.3     | pix      | Rkron     | Sextractor Kron_radius                                  |
| 67- 73    | F7.3     | pix      | A         | Sextractor parameter measuring major axis               |
| 81- 86    | F6.3     | pix      | B         | Sextractor parameter measuring minor axis               |
| 93- 99    | F7.3     | deg      | theta     | [-90/90] Sextractor parameter measuring angle           |
| 107- 112  | F6.3     | pix      | Aptot     | [0.99/12.8] Size of total aperture radius               |
| 120- 125  | F6.3     | ---      | Totcor    | [0/18.3] Approximate correction factor from             |
| 129- 138  | F10.3    | uJy      | FAuto     | SExtractor AUTO flux measured on BVR image              |
| 147- 151  | F5.3     | uJy      | e_FAuto   | [0.008] SExtractor AUTO flux error measured on          |
| 157- 164  | F8.3     | uJy      | Flux      | BVR image Sextractor flux (1)                           |
| 172- 177  | F6.3     | uJy      | e_Flux    | [-0.8/30] Error in flux (2)                             |
| 183- 190  | F8.3     | uJy      | FU38      | U38 band Sextractor flux (1)                            |
| 198- 203  | F6.3     | uJy      | e_FU38    | [-0.7/0.32] Error in flux (2)                           |
| 209- 216  | F8.3     | uJy      | FU        | U band Sextractor flux (1)                              |
| 224- 229  | F6.3     | uJy      | e_FU      | [-0.1/0.8] Error in flux (2)                            |
| 235- 242  | F8.3     | uJy      | FB        | B band Sextractor flux (1)                              |
| 250- 255  | F6.3     | uJy      | e_FB      | [-0.2/0.2] Error in flux (2)                            |
| 261- 268  | F8.3     | uJy      | FV        | V band Sextractor flux (1)                              |
| 276- 281  | F6.3     | uJy      | e_FV      | [-0.2/0.7] Error in flux (2)                            |
| 287- 294  | F8.3     | uJy      | FR        | R band Sextractor flux (1)                              |
| 303- 307  | F5.3     | uJy      | e_FR      | [0.012] Error in flux (2)                               |
| 313- 320  | F8.3     | uJy      | FI        | I band Sextractor flux (1)                              |
| 328- 333  | F6.3     | uJy      | e_FI      | [-6.2/2.9] Error in flux (2)                            |
| 339- 346  | F8.3     | uJy      | Fz        | z band Sextractor flux (1)                              |
| 354- 359  | F6.3     | uJy      | e_Fz      | [-2/4.2] Error in flux (2)                              |
| 364- 372  | F9.3     | uJy      | FJ        | J band Sextractor flux (1)                              |
| 379- 385  | F7.3     | uJy      | e_FJ      | [-30/32] Error in flux (2)                              |
| 388- 398  | F11.3    | uJy      | FH        | H band Sextractor flux (1)                              |
| 405- 411  | F7.3     | uJy      | e_FH      | [-40/24] Error in flux (2)                              |
| 416- 424  | F9.3     | uJy      | FK        | K band Sextractor flux (1)                              |
| 431- 437  | F7.3     | uJy      | e_FK      | [-12.8/27.2] Error in flux (2)                          |
| 443- 450  | F8.3     | uJy      | FIA427    | IA427 (4256.3{AA}) band Sextractor flux (1)             |
| 458- 463  | F6.3     | uJy      | e_FIA427  | [-3.9/7.5] Error in flux (2)                            |
| 469- 476  | F8.3     | uJy      | FIA445    | IA445 (4450{AA}, B) band Sextractor flux (1)            |
| 483- 489  | F7.3     | uJy      | e_FIA445  | [-11/2.1] Error in flux (2)                             |
| 494- 502  | F9.3     | uJy      | FIA464    | IA464 (4633.3{AA}) band Sextractor flux (1)             |
| 509- 515  | F7.3     | uJy      | e_FIA464  | [-10.5/176.4] Error in flux (2)                         |
| 522- 528  | F7.3     | uJy      | FIA484    | IA484 (4845.9{AA}) band Sextractor flux (1)             |
| 537- 541  | F5.3     | uJy      | e_FIA484  | [0.014] Error in flux (2)                               |
| 547- 554  | F8.3     | uJy      | FIA505    | IA505 (5060.7{AA}) band Sextractor flux (1)             |
| 562- 567  | F6.3     | uJy      | e_FIA505  | [-0.63/0.31] Error in flux (2)                          |
| 574- 580  | F7.3     | uJy      | FIA527    | IA527 (5258.9{AA}) band Sextractor flux (1)             |
| 589- 593  | F5.3     | uJy      | e_FIA527  | [0.014] Error in flux (2)                               |
| 600- 606  | F7.3     | uJy      | FIA550    | IA550 (V) band Sextractor flux (1)                      |
| 614- 619  | F6.3     | uJy      | e_FIA550  | [-3.8/44.7] Error in flux (2)                           |
| 625- 632  | F8.3     | uJy      | FIA574    | IA574 (5762.1{AA}) band Sextractor flux (1)             |
| 640- 645  | F6.3     | uJy      | e_FIA574  | [-0.62/0.43] Error in flux (2)                          |
| 652- 658  | F7.3     | uJy      | FIA598    | IA598 (6000{AA}) band Sextractor flux (1)               |
| 667- 671  | F5.3     | uJy      | e_FIA598  | [0.016] Error in flux (2)                               |
| 678- 684  | F7.3     | uJy      | FIA624    | IA624 (6230.0{AA}) band Sextractor flux (1)             |
| 693- 697  | F5.3     | uJy      | e_FIA624  | [0.018] Error in flux (2)                               |
| 704- 710  | F7.3     | uJy      | FIA651    | IA651 (6502{AA}) band Sextractor flux (1)               |
| 719- 723  | F5.3     | uJy      | e_FIA651  | [0.015] Error in flux (2)                               |
| 730- 736  | F7.3     | uJy      | FIA679    | IA679 (6778.8{AA}) band Sextractor flux (1)             |
| 745- 749  | F5.3     | uJy      | e_FIA679  | [0.016] Error in flux (2)                               |
| 755- 762  | F8.3     | uJy      | FIA709    | IA709 (7010.7{AA}) band Sextractor flux (1)             |
| 769- 775  | F7.3     | uJy      | e_FIA709  | [-79/6] Error in flux (2)                               |
| 782- 788  | F7.3     | uJy      | FIA738    | IA738 (7358.7{AA}) band Sextractor flux (1)             |
| 797- 801  | F5.3     | uJy      | e_FIA738  | [0.018] Error in flux (2)                               |
| 808- 814  | F7.3     | uJy      | FIA767    | IA767 (7681.2{AA}) band Sextractor flux (1)             |
| 823- 827  | F5.3     | uJy      | e_FIA767  | [0.045] Error in flux (2)                               |
| 834- 840  | F7.3     | uJy      | FIA797    | IA797 (7970{AA}) band Sextractor flux (1)               |
| 849- 853  | F5.3     | uJy      | e_FIA797  | [0.056] Error in flux (2)                               |
| 859- 866  | F8.3     | uJy      | FIA827    | IA827 (8240.9{AA}) band Sextractor flux (1)             |
| 873- 879  | F7.3     | uJy      | e_FIA827  | [-29/52]?=- Error in flux (2)                           |
| 886- 892  | F7.3     | uJy      | FIA856    | IA856 (8560{AA}) band Sextractor flux (1)               |
| 901- 905  | F5.3     | uJy      | e_FIA856  | [0.072] Error in flux (2)                               |
| 910- 918  | F9.3     | uJy      | F3.6      | Spitzer/IRAC 3.6{mu}m band Sextractor flux (1)          |
| 924- 931  | F8.3     | uJy      | e_F3.6    | [-304/8200] Error in flux (2)                           |
| 937- 944  | F8.3     | uJy      | F4.5      | Spitzer/IRAC 4.5{mu}m band Sextractor flux (1)          |
| 950- 957  | F8.3     | uJy      | e_F4.5    | [-106/311] Error in flux (2)                            |
| 962- 970  | F9.3     | uJy      | F5.8      | Spitzer/IRAC 5.8{mu}m band Sextractor flux (1)          |
| 976- 983  | F8.3     | uJy      | e_F5.8    | [-233/472] Error in flux (2)                            |
| 988- 996  | F9.3     | uJy      | F8.0      | Spitzer/IRAC 8.0{mu}m band Sextractor flux (1)          |
| 1002-1009 | F8.3     | uJy      | e_F8.0    | [-276/197] Error in flux (2)                            |
| 1016-1019 | I4       | ---      | Flags     | SExtractor Flag from BVR detection image (3)            |
| 1022-1027 | I6       | ---      | MUSYC     | Number of Corresponding source in MUSYC broad           |
| 1         | =        | The      | object    | has neighbours, bright and close enough to              |
| 2         | =        | The      | object    | was originally blended with another one                 |
| 4         | =        | At       | least     | one pixel of the object is saturated (or very close to) |
| 8         | =        | The      | object    | is truncated (too close to an image boundary)           |
| 16        | =        | Object's | aperture  | data are incomplete or corrupted                        |
| 32        | =        | Object's | isophotal | data are incomplete or corrupted                        |
| 64        | =        | A        | memory    | overflow occurred during deblending                     |
| 128       | =        | A        | memory    | overflow occurred during extraction                     |

**Note**: From aperture radius = 1xFWHM; not corrected from Galactic absorption.
Note (2): From empty apertures of size 1xFWHM
Note (3): SExtractor flag FLAGS contain, coded in additive numbers, all the
          extraction flags as a sum of powers of 2:
    1 = The object has neighbours, bright and close enough to
         significantly bias the MAG AUTO photometry or bad pixels
         (more than 10% of the integrated area affected)
    2 = The object was originally blended with another one
    4 = At least one pixel of the object is saturated (or very close to)
    8 = The object is truncated (too close to an image boundary)
   16 = Object's aperture data are incomplete or corrupted
   32 = Object's isophotal data are incomplete or corrupted
   64 = A memory overflow occurred during deblending
  128 = A memory overflow occurred during extraction

</details>

<details>
<summary>photomv1.dat</summary>

| Bytes   | Format   | Units     | Label    | Explanations                                 |
|:--------|:---------|:----------|:---------|:---------------------------------------------|
| 2- 6    | I5       | ---       | Seq      | [0/84401] Sequential Object Identifier       |
| 10- 19  | F10.6    | deg       | RAdeg    | Right ascension J2000 from SExtractor        |
| 24- 33  | F10.6    | deg       | DEdeg    | Declination J2000 from SExtractor            |
| 42      | I1       | ---       | X        | [0/1] Flag 1 if detected source is an X-ray  |
| 46- 51  | F6.3     | ---       | zsp      | ?=-1 Best Spectroscopic redshift             |
| 59- 60  | I2       | ---       | r_zsp    | [1/24]?=-1 Catalog from which adopted        |
| 66- 67  | I2       | ---       | q_zsp    | ?=-1 Quality Flag from Orginal Survey (5)    |
| 70- 76  | F7.3     | ---       | zph      | ?=-99.000 Redshift estimate from EAzY        |
| 79- 85  | F7.3     | ---       | E_zph    | ?=-99.000 68% confidence lower limit EAzY    |
| 88- 94  | F7.3     | ---       | e_zph    | ?=-99.000 68% confidence upper limit EAzY    |
| 96-103  | F8.3     | ---       | chizph   | ?=-99.000 Chi-squared value of EAzY best fit |
| 105-112 | F8.3     | ---       | q_zph    | ?=-99.000 Quality Flag from EAzY (best <=1)  |
| 120     | I1       | ---       | S/G2     | [0/1] 1 if EAzY fit to stellar template is   |
| 124-129 | F6.2     | mag       | FVRF     | ?=99.00 Rest-frame V-band flux from EAzY     |
| 134-138 | F5.2     | mag       | U-VRF    | ?=99.00 Rest-frame U-V band color from EAzY  |
| 143-147 | F5.2     | mag       | V-JRF    | ?=99.00 Rest-frame V-J band color from EAzY  |
| 1       | =        | VVDS,     | CIMOS    | VLT Deep Survey                              |
| 2       | =        | Szokoly   | et       | al., 2004, Cat. J/ApJS/155/271               |
| 3       | =        | Croom     | et       | al., 2001, Cat. J/MNRAS/328/150              |
| 5       | =        | Van       | der      | Wel et al., 2004ApJ...601L...5V              |
| 10      | =        | Cristiani | et       | al. 2000A&A...359..489C                      |
| 11      | =        | Strogler  | et       | al., 2004, Cat. J/ApJ/613/200                |
| 18      | =        | MUSYC,    | Lira     | et al., in prep                              |
| 19      | =        | Treister  | et       | al, 2009, Cat. J/ApJ/693/1713                |
| 20      | =        | Cimatti   | et       | al., 2002, Cat. J/A+A/392/395 (K20)          |
| 21      | =        | Kriek     | et       | al., 2008, Cat. J/ApJ/677/219                |
| 22      | =        | VLT/FORS2 | Vanzella | et al., 2008, Cat. J/A+A/478/83;             |
| 23      | =        | GOODS     | VIMOS    | (Balestra et al., 2010, Cat. J/A+A/512/A12)  |
| 24      | =        | GOODS     | VIMOS    | (Balestra et al., 2010, Cat. J/A+A/512/A12)  |

**Note**: X-ray counterparts included an additional QSO template when
     finding redshift solutions and rest frame colors in EAzY
Note (5): Best redshift taken from compilations by Gabe & the GOODS team as
          well as the literature, as follows:
   1 = VVDS, CIMOS VLT Deep Survey
       1: 50% confidence in the redshift;
       2: 75% confidence in the redshift;
       3: 95% confidence in the redshift;
       4: 100% confidence in the redshift;
       9:  Single emission line objects
   2 = Szokoly et al., 2004, Cat. J/ApJS/155/271
       3.0: reliable redshift determination with unambigous X-ray counterpart;
       2.0: reliable redshift determination;
       1.0: detection of some features (typically single narrow EL);
       0.5: hint of some spectral features;
       0.0: no success
   3 = Croom et al., 2001, Cat. J/MNRAS/328/150
   5 = Van der Wel et al., 2004ApJ...601L...5V
  10 = Cristiani et al. 2000A&A...359..489C
  11 = Strogler et al., 2004, Cat. J/ApJ/613/200
  18 = MUSYC, Lira et al., in prep
  19 = Treister et al, 2009, Cat. J/ApJ/693/1713
  20 = Cimatti et al., 2002, Cat. J/A+A/392/395 (K20)
  21 = Kriek et al., 2008, Cat. J/ApJ/677/219
  22 = VLT/FORS2 Vanzella et al., 2008, Cat. J/A+A/478/83;
       A: Solid redshift determination;
       B: likely redshift determination;
       C: tentative redshift determination
  23 = GOODS VIMOS (Balestra et al., 2010, Cat. J/A+A/512/A12)
       Low Res Blue (LR) spectra v2.0.1:
       1:100% confidence in the redshift;
       2: 60% confidence in the redshift;
       3: 20% confidence in the redshift
  24 = GOODS VIMOS (Balestra et al., 2010, Cat. J/A+A/512/A12)
       Med Res Orange (MR) spectra v2.0:
       1: 100% confidence in the redshift;
       2: 95% confidence in the redshift;
       3: 60% confidence in the redshift

</details>
