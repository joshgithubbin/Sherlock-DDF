**Authors:** Scarlata C., Capak P., Davidzon I., Faisst A., Hsieh B.C.,, Ilbert O., Jarvis M., Laigle C., Phillips J., Silverman J., Strauss M.A.,, Tanaka M., Bowler R., Coupon J., Foucaud S., Hemmati S., Masters D.,, McCracken H.J., Mobasher B., Ouchi M., Shibuya T., Wang W.-H., <Astrophys. J. Suppl. Ser., 235, 36-36 (2018)>, =2018ApJS..235...36M (SIMBAD/NED BibCode)

## Summary: SPLASH-SXDF multi-wavelength photometric catalog 

We present a multi-wavelength catalog in the Subaru/XMM-Newton Deep Field (SXDF) as part of the Spitzer Large Area Survey with Hyper-Suprime-Cam (SPLASH). We include the newly acquired optical data from the Hyper-Suprime-Cam Subaru Strategic Program, accompanied by IRAC coverage from the SPLASH survey. All available optical and near-infrared data is homogenized and resampled on a common astrometric reference frame. Source detection is done using a multi-wavelength detection image including the u-band to recover the bluest objects. We measure multi-wavelength photometry and compute photometric redshifts as well as physical properties for ~1.17 million objects over ~4.2deg^2^, with ~800000 objects in the 2.4deg^2^ HSC-Ultra-Deep coverage. Using the available spectroscopic redshifts from various surveys over the range of 0<z<6, we verify the performance of the photometric redshifts and we find a normalized median absolute deviation of 0.023 and outlier fraction of 3.2%. The SPLASH-SXDF catalog is a valuable, publicly available resource, perfectly suited for studying galaxies in the early universe and tracing their evolution through cosmic time.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-235-36/Subcatalogues/XMM-LSS/Plots/fieldcover.png)
## Photometric Redshift 
 
**zBest:** [0/6]?=-99 Best estimate of photometric 
 

## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes     | Format      | Units           | Label               | Explanations                                                                  |
|:----------|:------------|:----------------|:--------------------|:------------------------------------------------------------------------------|
| 1- 7      | I7          | ---             | Seq                 | [1/1169058] Source Identification number                                      |
| 9- 18     | F10.7       | deg             | RAdeg               | [33.4/35.6] Right Ascension (J2000) (RA)                                      |
| 20- 29    | F10.7       | deg             | DEdeg               | [-6.1/-3.9] Declination (J2000) (DEC)                                         |
| 31- 39    | E9.4        | deg             | amaj                | [2.2e-05/0.05] Semi-major axis (A)                                            |
| 41- 49    | E9.4        | deg             | bmin                | [4.8e-06/0.005]? Semi-minor axis (B)                                          |
| 51- 56    | F6.2        | deg             | PA                  | [-90/90] Position Angle (THETA)                                               |
| 58- 65    | F8.2        | pix             | Xpos                | Object position along x (X_IMAGE)                                             |
| 67- 74    | F8.2        | pix             | Ypos                | Object position along y (Y_IMAGE)                                             |
| 76- 82    | F7.2        | pix             | Aimg                | Semi-major axis (A_IMAGE)                                                     |
| 84- 89    | F6.2        | pix             | Bimg                | Semi-minor axis (B_IMAGE)                                                     |
| 91- 96    | F6.2        | deg             | PAimg               | Position Angle (THETA_IMAGE)                                                  |
| 98- 102   | F5.2        | ---             | KRad                | [3.5/14.6] Kron radius                                                        |
| 104- 108  | F5.2        | ---             | PAp                 | [3.5/11] Petrosian apertures                                                  |
| 110- 114  | I5          | pix2            | Area                | [4/99903] Isophotal area (filtered) above                                     |
| 116- 122  | F7.3        | ---             | Elon                | [1/489] Size ratio A_IMAGE/B_IMAGE                                            |
| 124- 132  | E9.3        | ---             | ell                 | Ellipticity 1-B_IMAGE/A_IMAGE (ELLIPTICITY)                                   |
| 134- 138  | F5.3        | ---             | E(B-V)              | [0.01/0.03] Galactic extinction                                               |
| 140- 184  | 5F9.1       | ---             | OffFlux             | [1/498078] Offsets (multiplicative) between                                   |
| 5         | arcsec      | apertures       | (OFFSET_FLUX)       | 186- 220 5F7.2  ---     Offmag    [-14.3/0] Offsets (linear) between AUTO and |
| 5         | arcsec      | apertures       | (OFFSET_MAG)        | 222- 231  F10.6 ---     zspec     [7e-5/6.3]?=-99 Spectroscopic redshift;     |
| 233- 248  | A16         | ---             | r_zspec             | Reference for the spectroscopic                                               |
| 250- 259  | F10.6       | ---             | zphot               | [0/6]?=-99 Best redshift for the source                                       |
| 261- 263  | I3          | ---             | S/G                 | [-99/1]?=-99 Star/galaxy classification flag                                  |
| 265- 271  | F7.3        | mag             | gmag                | [15.2/38.1]?=-99 Subaru/HSC g Kron-like                                       |
| 273- 280  | F8.3        | mag             | e_gmag              | [0/6969]?=-99 Error for gmag                                                  |
| 282- 288  | F7.2        | uJy             | Fhscg               | [-38/3042]?=-99 Subaru/HSC g-band flux                                        |
| 290- 295  | F6.2        | uJy             | e_Fhscg             | [0/9]?=-99 Fhscg uncertainty                                                  |
| 297- 303  | F7.3        | mag             | gmagISO             | [15.2/42]?=-99 Isophotal HSC g-band AB                                        |
| 305- 313  | F9.3        | mag             | e_gmagISO           | [0/46095]?=-99 gmagISO uncertainty                                            |
| 315- 321  | F7.2        | uJy             | FhscgISO            | [-12/2843]?=-99 Subaru/HSC g-band isophotal                                   |
| 323- 328  | F6.2        | uJy             | e_FhscgISO          | [0/4]?=-99 FhscgISO uncertainty                                               |
| 330- 369  | 5F8.3       | mag             | gmagAp              | [16/30]?=-99 Subaru/HSC g-band fixed                                          |
| 371- 410  | 5F8.3       | mag             | e_gmagAp            | [-1/8]?=-99 gmagAp uncertainties                                              |
| 412- 451  | 5F8.2       | uJy             | FhscgAp             | [-12/1263]?=-99 Subaru/HSC g-band fluxes                                      |
| 453- 487  | 5F7.2       | uJy             | e_FhscgAp           | [0/4]?=-99 FhscgAp uncertainties                                              |
| 489- 518  | 3F10.1      | pix             | gRad                | [-157499/1964] Fraction of light radii for                                    |
| 520- 522  | I3          | ---             | gFlag               | [0/184] Subaru/HSC g-band SExtractor                                          |
| 524       | I1          | ---             | f_gmag              | [0/1] Subaru/HSC g-band coverage flag                                         |
| 526- 532  | F7.3        | mag             | rmag                | [14.7/42]?=-99 Subaru/HSC r Kron-like                                         |
| 534- 543  | F10.3       | mag             | e_rmag              | [0/251727]?=-99 rmag uncertainty                                              |
| 545- 551  | F7.2        | uJy             | Fhscr               | [-104/4787]?=-99 Subaru/HSC r-band flux                                       |
| 553- 559  | F7.2        | uJy             | e_Fhscr             | [0/2593]?=-99 Fhscr uncertainty                                               |
| 561- 567  | F7.3        | mag             | rmagISO             | [14.7/39]?=-99 Isophotal HSC r-band AB                                        |
| 569- 577  | F9.3        | mag             | e_rmagISO           | [0/23487]?=-99 rmagISO uncertainty                                            |
| 579- 585  | F7.2        | uJy             | FhscrISO            | [-7/4901]?=-99 Subaru/HSC r-band isophotal                                    |
| 587- 593  | F7.2        | uJy             | e_FhscrISO          | [0/2430]?=-99 FhscrISO uncertainty                                            |
| 595- 634  | 5F8.3       | mag             | rmagAp              | [16/30]?=-99 Subaru/HSC r-band fixed                                          |
| 636- 675  | 5F8.3       | mag             | e_rmagAp            | [-1/719]?=-99 rmagAp uncertainties                                            |
| 677- 716  | 5F8.2       | uJy             | FhscrAp             | [-392/1358]?=-99 Subaru/HSC r-band fluxes                                     |
| 718- 757  | 5F8.2       | uJy             | e_FhscrAp           | [0/7895]?=-99 FhscrAp uncertainties                                           |
| 759- 788  | 3F10.1      | pix             | rRad                | [-186423/2135] Fraction of light radii                                        |
| 790- 792  | I3          | ---             | rFlag               | [0/184] Subaru/HSC r-band SExtractor                                          |
| 794       | I1          | ---             | f_rmag              | [0/1] Subaru/HSC g-band coverage flag                                         |
| 796- 802  | F7.3        | mag             | imag                | [14.6/39]?=-99 Subaru/HSC i Kron-like                                         |
| 804- 813  | F10.3       | mag             | e_imag              | [0/105521]?=-99 imag uncertainty                                              |
| 815- 822  | F8.2        | uJy             | Fhsci               | [-1290/5349]?=-99 Subaru/HSC i-band flux                                      |
| 824- 829  | F6.2        | uJy             | e_Fhsci             | [0/242]?=-99 Fhsci uncertainty                                                |
| 831- 837  | F7.3        | mag             | imagISO             | [14.6/39]?=-99 Isophotal HSC i-band AB                                        |
| 839- 848  | F10.3       | mag             | e_imagISO           | [0/64976]?=-99 imagISO uncertainty                                            |
| 850- 856  | F7.2        | uJy             | FhsciISO            | [-103/5007] Subaru/HSC i-band isophotal                                       |
| 858- 863  | F6.2        | uJy             | e_FhsciISO          | [0/206]?=-99 FhsciISO uncertainty                                             |
| 865- 904  | 5F8.3       | mag             | imagAp              | [16/30]?=-99 Subaru/HSC i-band fixed                                          |
| 906- 950  | 5F9.3       | mag             | e_imagAp            | [-1/1423]?=-99 imagAp uncertainty                                             |
| 952- 991  | 5F8.2       | uJy             | FhsciAp             | [-70/1427]?=-99 Subaru/HSC i-band fluxes                                      |
| 993-1027  | 5F7.2       | uJy             | e_FhsciAp           | [0/620]?=-99 FhsciAp uncertainties                                            |
| 1029-1058 | 3F10.1      | pix             | iRad                | [-829650/2024] Fraction of light radii                                        |
| 1060-1062 | I3          | ---             | iFlag               | [0/184] Subaru/HSC i-band SExtractor                                          |
| 1064      | I1          | ---             | f_imag              | [0/1] Subaru/HSC i-band coverage flag                                         |
| 1066-1072 | F7.3        | mag             | zmag                | [14/41]?=-99 Subaru/HSC z Kron-like                                           |
| 1074-1083 | F10.3       | mag             | e_zmag              | [0/681550]?=-99 zmag uncertainty                                              |
| 1085-1091 | F7.2        | uJy             | Fhscz               | [-274/8450] Subaru/HSC z-band flux within                                     |
| 1093-1099 | F7.2        | uJy             | e_Fhscz             | [0.01/30]?=-99 Fhscz uncertainty                                              |
| 1101-1107 | F7.3        | mag             | zmagISO             | [14/40]?=-99 Isophotal HSC z-band AB                                          |
| 1109-1117 | F9.3        | mag             | e_zmagISO           | [0/39194]?=-99 zmagISO uncertainty                                            |
| 1119-1125 | F7.2        | uJy             | FhsczISO            | [-82/8628]?=-99 Subaru/HSC z-band isophotal                                   |
| 1127-1132 | F6.2        | uJy             | e_FhsczISO          | [0/6]?=-99 FhsczISO uncertainty                                               |
| 1134-1173 | 5F8.3       | mag             | zmagAp              | [15.4/29]?=-99 Subaru/HSC z-band fixed                                        |
| 1175-1214 | 5F8.3       | mag             | e_zmagAp            | [-1/10]?=-99 zmagAp uncertainties                                             |
| 1216-1255 | 5F8.2       | uJy             | FhsczAp             | [-14/2514]?=-99 Subaru/HSC z-band fluxes                                      |
| 1257-1291 | 5F7.2       | uJy             | e_FhsczAp           | [0.01/9]?=-99 FhsczAp uncertainties                                           |
| 1293-1322 | 3F10.1      | pix             | zRad                | [-145493/2152] Fraction of light radii                                        |
| 1324-1326 | I3          | ---             | zFlag               | [0/184] Subaru/HSC z-band SExtractor                                          |
| 1328      | I1          | ---             | f_zmag              | [0/1] Subaru/HSC z-band coverage flag                                         |
| 1330-1336 | F7.3        | mag             | ymag                | [13.9/37]?=-99 Subaru/HSC y Kron-like                                         |
| 1338-1346 | F9.3        | mag             | e_ymag              | [0/17001]?=-99 ymag uncertainty                                               |
| 1348-1354 | F7.2        | uJy             | Fhscy               | [-345/9940] Subaru/HSC y-band flux within                                     |
| 1356-1361 | F6.2        | uJy             | e_Fhscy             | [0.01/60]?=-99 Fhscy uncertainty                                              |
| 1363-1369 | F7.3        | mag             | ymagISO             | [13.9/40]?=-99 Isophotal HSC y-band AB                                        |
| 1371-1380 | F10.3       | mag             | e_ymagISO           | [0/110537]?=-99 ymagISO uncertainty                                           |
| 1382-1389 | F8.2        | uJy             | FhscyISO            | [-63/10151]?=-99 Subaru/HSC y-band                                            |
| 1391-1396 | F6.2        | uJy             | e_FhscyISO          | [0.01/12]?=-99 FhscyISO uncertainty                                           |
| 1398-1437 | 5F8.3       | mag             | ymagAp              | [15/28]?=-99 Subaru/HSC y-band fixed                                          |
| 1439-1478 | 5F8.3       | mag             | e_ymagAp            | [-1/3]?=-99 ymagAp uncertainties                                              |
| 1480-1519 | 5F8.2       | uJy             | FhscyAp             | [-38/2913]?=-99 Subaru/HSC y-band fluxes                                      |
| 1521-1555 | 5F7.2       | uJy             | e_FhscyAp           | [0.01/6]?=-99 FhscyAp uncertainties                                           |
| 1557-1589 | 3E11.4      | pix             | yRad                | [-1.5e+6/2563] Fraction of light radii                                        |
| 1591-1593 | I3          | ---             | yFlag               | [0/184] Subaru/HSC y-band SExtractor                                          |
| 1595      | I1          | ---             | f_ymag              | [0/1] Subaru/HSC y-band coverage flag                                         |
| 1597-1603 | F7.3        | mag             | bmagscam            | [13.9/42]?=-99 Kron-like elliptical                                           |
| 1605-1613 | F9.3        | mag             | e_bmagscam          | [0/79630]?=-99 bmagscam uncertainty                                           |
| 1615-1622 | F8.2        | uJy             | Fscamb              | [-104/10095] Subaru/suprime B-band flux                                       |
| 1624-1629 | F6.2        | uJy             | e_Fscamb            | [0/3]?=-99 Fscamb uncertainty                                                 |
| 1631-1637 | F7.3        | mag             | bmagscamISO         | [13.9/41]?=-99 Isophotal Subaru/suprime                                       |
| 1639-1646 | F8.3        | mag             | e_bmagscamISO       | [0/5049]?=-99 bmagscamISO uncertainty                                         |
| 1648-1654 | F7.2        | uJy             | FscambISO           | [-12/9644]?=-99 Isophotal Subaru/suprime                                      |
| 1656-1661 | F6.2        | uJy             | e_FscambISO         | [0/0.6]?=-99 FscambISO uncertainty                                            |
| 1663-1702 | 5F8.3       | mag             | bmagscamAp          | [16/31]?=-99 Subaru/suprime B-band fixed                                      |
| 1704-1743 | 5F8.3       | mag             | e_bmagscamAp        | [-1/2]?=-99 bmagscamAp uncertainties                                          |
| 1745-1784 | 5F8.2       | uJy             | FscambAp            | [-13/1240]?=-99 Subaru/suprime B-band                                         |
| 1786-1820 | 5F7.2       | uJy             | e_FscambAp          | [0/0.2]?=-99 FscambAp uncertainties                                           |
| 1822-1851 | 3F10.1      | pix             | bscamRad            | [-276343/926] Subaru/suprime B-band                                           |
| 1853-1855 | I3          | ---             | bscamFlag           | [0/184] Subaru/suprime B-band SExtractor                                      |
| 1857      | I1          | ---             | f_bmagscam          | [0/1] Subaru/suprime B-band coverage flag                                     |
| 1859-1865 | F7.3        | mag             | vmagscam            | [14/38]?=-99 Kron-like elliptical aperture                                    |
| 1867-1874 | F8.3        | mag             | e_vmagscam          | [0/6059]?=-99 vmagscam uncertainty                                            |
| 1876-1883 | F8.2        | uJy             | Fscamv              | [-9148/7886] Subaru/suprime V-band flux                                       |
| 1885-1890 | F6.2        | uJy             | e_Fscamv            | [0/3]?=-99 Fscamv uncertainty                                                 |
| 1892-1898 | F7.3        | mag             | vmagscamISO         | [13.8/41]?=-99 Isophotal Subaru/suprime                                       |
| 1900-1908 | F9.3        | mag             | e_vmagscamISO       | [0/10873]?=-99 vmagscamISO uncertainty                                        |
| 1910-1917 | F8.2        | uJy             | FscamvISO           | [-146/11202]?=-99 Isophotal Subaru/suprime                                    |
| 1919-1924 | F6.2        | uJy             | e_FscamvISO         | [0/0.8]?=-99 FscamvISO uncertainty                                            |
| 1926-1965 | 5F8.3       | mag             | vmagscamAp          | [16.2/31]?=-99 Subaru/suprime V-band fixed                                    |
| 1967-2006 | 5F8.3       | mag             | e_vmagscamAp        | [-1/4]?=-99 vmagscamAp uncertainties                                          |
| 2008-2047 | 5F8.2       | uJy             | FscamvAp            | [-811/1216] Subaru/suprime V-band fluxes                                      |
| 2049-2083 | 5F7.2       | uJy             | e_FscamvAp          | [0/0.3]?=-99 FscamvAp uncertainties                                           |
| 2085-2114 | 3F10.1      | pix             | vscamRad            | [-285307/2201] Subaru/suprime V-band                                          |
| 2116-2118 | I3          | ---             | vscamFlag           | [0/184] Subaru/suprime V-band SExtractor                                      |
| 2120      | I1          | ---             | f_vmagscam          | [0/1] Subaru/suprime V-band coverage flag                                     |
| 2122-2128 | F7.3        | mag             | rmagscam            | [13.8/42]?=-99 Kron-like elliptical                                           |
| 2130-2138 | F9.3        | mag             | e_rmagscam          | [0/77177]?=-99 rmagscam uncertainty                                           |
| 2140-2147 | F8.2        | uJy             | Fscamr              | [-99/10632]?=-99 Subaru/suprime Rc-band                                       |
| 2149-2154 | F6.2        | uJy             | e_Fscamr            | [0/4]?=-99 Fscamr uncertainty                                                 |
| 2156-2162 | F7.3        | mag             | rmagscamISO         | [13.5/41]?=-99 Isophotal Subaru/suprime                                       |
| 2164-2172 | F9.3        | mag             | e_rmagscamISO       | [0/19730]?=-99 rmagscamISO uncertainty                                        |
| 2174-2181 | F8.2        | uJy             | FscamrISO           | [-11/13950]?=-99 Isophotal Subaru/suprime                                     |
| 2183-2188 | F6.2        | uJy             | e_FscamrISO         | [0/1]?=-99 FscamrISO uncertainty                                              |
| 2190-2229 | 5F8.3       | mag             | rmagscamAp          | [16/31]?=-99 Subaru/suprime Rc-band fixed                                     |
| 2231-2270 | 5F8.3       | mag             | e_rmagscamAp        | [-1/3]?=-99 rmagscamAp uncertainties                                          |
| 2272-2311 | 5F8.2       | uJy             | FscamrAp            | [-91/1405]?=-99 Subaru/suprime Rc-band                                        |
| 2313-2347 | 5F7.2       | uJy             | e_FscamrAp          | [0/0.3]?=-99 FscamrAp uncertainties                                           |
| 2349-2381 | 3E11.4      | pix             | rscamRad            | [-2e+6/954] Subaru/suprime Rc-band                                            |
| 2383-2385 | I3          | ---             | rscamFlag           | [0/184] Subaru/suprime Rc-band SExtractor                                     |
| 2387      | I1          | ---             | f_rmagscam          | [0/1] Subaru/suprime Rc-band coverage flag                                    |
| 2389-2395 | F7.3        | mag             | imagscam            | [13.8/39]?=-99 Kron-like elliptical                                           |
| 2397-2405 | F9.3        | mag             | e_imagscam          | [0/14850]?=-99 imagscam uncertainty                                           |
| 2407-2414 | F8.2        | uJy             | Fscami              | [-83/10523]?=-99 Subaru/suprime i'-band                                       |
| 2416-2421 | F6.2        | uJy             | e_Fscami            | [0/5]?=-99 RedshiftsFscami uncertainty                                        |
| 2423-2429 | F7.3        | mag             | imagscamISO         | [13.5/39]?=-99 Isophotal Subaru/suprime                                       |
| 2431-2438 | F8.3        | mag             | e_imagscamISO       | [0/1364]?=-99 imagscamISO uncertainty                                         |
| 2440-2447 | F8.2        | uJy             | FscamiISO           | [-7/14566]?=-99 Isophotal Subaru/suprime                                      |
| 2449-2454 | F6.2        | uJy             | e_FscamiISO         | [0/1]?=-99 FscamiISO uncertainty                                              |
| 2456-2495 | 5F8.3       | mag             | imagscamAp          | [15.7/30]?=-99 Subaru/suprime i'-band fixed                                   |
| 2497-2536 | 5F8.3       | mag             | e_imagscamAp        | [-1/3]?=-99 imagscamAp uncertainties                                          |
| 2538-2577 | 5F8.2       | uJy             | FscamiAp            | [-10/1904]?=-99 Subaru/suprime i'-band                                        |
| 2579-2613 | 5F7.2       | uJy             | e_FscamiAp          | [0/0.4]?=-99 FscamiAp uncertainties                                           |
| 2615-2644 | 3F10.1      | pix             | iscamRad            | [-161651/966.2] Subaru/suprime i'-band                                        |
| 2646-2648 | I3          | ---             | iscamFlag           | [0/184] Subaru/suprime i'-band SExtractor                                     |
| 2650      | I1          | ---             | f_imagscam          | [0/1] Subaru/suprime i'-band coverage flag                                    |
| 2652-2658 | F7.3        | mag             | zmagscam            | [13/37]?=-99 Kron-like elliptical aperture                                    |
| 2660-2667 | F8.3        | mag             | e_zmagscam          | [0/7358]?=-99 zmagscam uncertainty                                            |
| 2669-2676 | F8.2        | uJy             | Fscamz              | [-185/19755]?=-99 Subaru/suprime z'-band                                      |
| 2678-2683 | F6.2        | uJy             | e_Fscamz            | [0/8]?=-99 Fscamz uncertainty                                                 |
| 2685-2691 | F7.3        | mag             | zmagscamISO         | [12.7/41]?=-99 Isophotal Subaru/suprime                                       |
| 2693-2701 | F9.3        | mag             | e_zmagscamISO       | [0/25832]?=-99 zmagscamISO uncertainty                                        |
| 2703-2710 | F8.2        | uJy             | FscamzISO           | [-17/29391]?=-99 Isophotal Subaru/suprime                                     |
| 2712-2717 | F6.2        | uJy             | e_FscamzISO         | [0/2]?=-99 FscamzISO uncertainty                                              |
| 2719-2758 | 5F8.3       | mag             | zmagscamAp          | [14/30]?=-99 Subaru/suprime z'-band fixed                                     |
| 2760-2799 | 5F8.3       | mag             | e_zmagscamAp        | [-1/2]?=-99 zmagscamAp uncertainties                                          |
| 2801-2840 | 5F8.2       | uJy             | FscamzAp            | [-19/7493]?=-99 Subaru/suprime z'-band                                        |
| 2842-2876 | 5F7.2       | uJy             | e_FscamzAp          | [0/0.5]?=-99 FscamzAp uncertainties                                           |
| 2878-2910 | 3E11.4      | pix             | zscamRad            | [-1.5e+7/968] Subaru/suprime z'-band                                          |
| 2912-2914 | I3          | ---             | zscamFlag           | [0/184] Subaru/suprime z'-band SExtractor                                     |
| 2916      | I1          | ---             | f_zmagscam          | [0/1] Subaru/suprime z'-band coverage flag                                    |
| 2918-2924 | F7.3        | mag             | jmaguds             | [10.5/37]?=-99 UKIRT/WFCAM J-band Kron-like                                   |
| 2926-2933 | F8.3        | mag             | e_jmaguds           | [0/5019]?=-99 jmaguds uncertainty                                             |
| 2935-2943 | F9.2        | uJy             | Fudsj               | [-63/218081]?=-99 UKIRT/WFCAM J-band flux                                     |
| 2945-2950 | F6.2        | uJy             | e_Fudsj             | [0.01/17]?=-99 Fudsj uncertainty                                              |
| 2952-2958 | F7.3        | mag             | jmagudsISO          | [10.5/38]?=-99 UKIRT/WFCAM J-band isophotal                                   |
| 2960-2967 | F8.3        | mag             | e_jmagudsISO        | [0/3869]?=-99 jmagudsISO uncertainty                                          |
| 2969-2977 | F9.2        | uJy             | FudsjISO            | [-82/219389]?=-99 UKIRT/WFCAM J-band                                          |
| 2979-2984 | F6.2        | uJy             | e_FudsjISO          | [0.01/11]?=-99 FudsjISO uncertainty                                           |
| 2986-3025 | 5F8.3       | mag             | jmagudsAp           | [10.5/29]?=-99 UKIRT/WFCAM J-band fixed                                       |
| 3027-3066 | 5F8.3       | mag             | e_jmagudsAp         | [-1/15]?=-99 jmagudsAp uncertainties                                          |
| 3068-3117 | 5F10.2      | uJy             | FudsjAp             | [-80/215382]?=-99 UKIRT/WFCAM J-band fluxes                                   |
| 3119-3153 | 5F7.2       | uJy             | e_FudsjAp           | [0.01/8]?=-99 FudsjAp uncertainties                                           |
| 3155-3187 | 3E11.4      | pix             | udsjRad             | [-3.6e+7/6753] UKIRT/WFCAM J-band fraction                                    |
| 3189-3191 | I3          | ---             | udsjFlag            | [0/184] UKIRT/WFCAM J-band SExtractor                                         |
| 3193      | I1          | ---             | f_jmaguds           | [0/1] UKIRT/WFCAM J-band coverage flag                                        |
| 3195-3201 | F7.3        | mag             | hmaguds             | [10.4/37]?=-99 UKIRT/WFCAM H-band Kron-like                                   |
| 3203-3210 | F8.3        | mag             | e_hmaguds           | [0/9294]?=-99 hmaguds uncertainty                                             |
| 3212-3220 | F9.2        | uJy             | Fudsh               | [-388/240430]?=-99 UKIRT/WFCAM H-band flux                                    |
| 3222-3227 | F6.2        | uJy             | e_Fudsh             | [0.02/17]?=-99 Fudsh uncertainty                                              |
| 3229-3235 | F7.3        | mag             | hmagudsISO          | [10.4/37]?=-99 UKIRT/WFCAM H-band isophotal                                   |
| 3237-3244 | F8.3        | mag             | e_hmagudsISO        | [0/5658]?=-99 hmagudsISO uncertainty                                          |
| 3246-3254 | F9.2        | uJy             | FudshISO            | [-83/242285]?=-99 UKIRT/WFCAM H-band                                          |
| 3256-3261 | F6.2        | uJy             | e_FudshISO          | [0.01/11]?=-99 FudshISO uncertainty                                           |
| 3263-3302 | 5F8.3       | mag             | hmagudsAp           | [10.5/28]?=-99 UKIRT/WFCAM H-band fixed                                       |
| 3304-3343 | 5F8.3       | mag             | e_hmagudsAp         | [-1/16]?=-99 hmagudsAp uncertainties                                          |
| 3345-3394 | 5F10.2      | uJy             | FudshAp             | [-80/232326]?=-99 UKIRT/WFCAM H-band fluxes                                   |
| 3396-3430 | 5F7.2       | uJy             | e_FudshAp           | [0.01/12]?=-99 FudshAp uncertainties                                          |
| 3432-3461 | 3F10.1      | pix             | udshRad             | [-144641/6753] UKIRT/WFCAM H-band fraction                                    |
| 3463-3465 | I3          | ---             | udshFlag            | [0/184] UKIRT/WFCAM H-band SExtractor                                         |
| 3467      | I1          | ---             | f_hmaguds           | [0/1] UKIRT/WFCAM H-band coverage flag                                        |
| 3469-3475 | F7.3        | mag             | kmaguds             | [10.8/41]?=-99  UKIRT/WFCAM K-band                                            |
| 3477-3486 | F10.3       | mag             | e_kmaguds           | [0/119162]?=-99 kmaguds uncertainty                                           |
| 3488-3496 | F9.2        | uJy             | Fudsk               | [-134/169660]?=-99 UKIRT/WFCAM K-band flux                                    |
| 3498-3503 | F6.2        | uJy             | e_Fudsk             | [0.01/27]?=-99 Fudsk uncertainty                                              |
| 3505-3511 | F7.3        | mag             | kmagudsISO          | [10.8/39]?=-99 UKIRT/WFCAM K-band isophotal                                   |
| 3513-3520 | F8.3        | mag             | e_kmagudsISO        | [0/8769]?=-99 kmagudsISO uncertainty                                          |
| 3522-3530 | F9.2        | uJy             | FudskISO            | [-24/171242]?=-99 UKIRT/WFCAM K-band                                          |
| 3532-3537 | F6.2        | uJy             | e_FudskISO          | [0.01/9]?=-99 FudskISO uncertainty                                            |
| 3539-3578 | 5F8.3       | mag             | kmagudsAp           | [10.8/29]?=-99 UKIRT/WFCAM K-band fixed                                       |
| 3580-3619 | 5F8.3       | mag             | e_kmagudsAp         | [-1/9]?=-99 kmagudsAp uncertainties                                           |
| 3621-3670 | 5F10.2      | uJy             | FudskAp             | [-26/166117]?=-99 UKIRT/WFCAM K-band fluxes                                   |
| 3672-3706 | 5F7.2       | uJy             | e_FudskAp           | [0.01/7]?=-99 FudskAp uncertainties                                           |
| 3708-3737 | 3F10.1      | pix             | udskRad             | [-248191/6753] UKIRT/WFCAM K-band fraction                                    |
| 3739-3741 | I3          | ---             | udskFlag            | [0/184] UKIRT/WFCAM K-band SExtractor                                         |
| 3743      | I1          | ---             | f_kmaguds           | [0/1] UKIRT/WFCAM K-band coverage flag                                        |
| 3745-3751 | F7.3        | mag             | zmagvi              | [11/38]?=-99 VISTA Z-band Kron-like                                           |
| 3753-3760 | F8.3        | mag             | e_zmagvi            | [0/4312]?=-99 zmagvi uncertainty                                              |
| 3762-3770 | F9.2        | uJy             | Fviz                | [-321/132228]?=-99 VISTA Z-band flux within                                   |
| 3772-3777 | F6.2        | uJy             | e_Fviz              | [0/25]?=-99 Fviz uncertainty                                                  |
| 3779-3785 | F7.3        | mag             | zmagviISO           | [11/39]?=-99 VISTA Z-band isophotal                                           |
| 3787-3794 | F8.3        | mag             | e_zmagviISO         | [0/2872]?=-99 zmagviISO uncertainty                                           |
| 3796-3804 | F9.2        | uJy             | FvizISO             | [-17/136140]?=-99 VISTA Z-band isophotal                                      |
| 3806-3811 | F6.2        | uJy             | e_FvizISO           | [0/9]?=-99 FvizISO uncertainty                                                |
| 3813-3852 | 5F8.3       | mag             | zmagviAp            | [11.2/29]?=-99 VISTA Z-band fixed circular                                    |
| 3854-3893 | 5F8.3       | mag             | e_zmagviAp          | [-1/27]?=-99 zmagviAp uncertainties                                           |
| 3895-3944 | 5F10.2      | uJy             | FvizAp              | [-21/112922]?=-99 VISTA Z-band fluxes                                         |
| 3946-3980 | 5F7.2       | uJy             | e_FvizAp            | [0.01/27]?=-99 FvizAp uncertainties                                           |
| 3982-4014 | 3E11.4      | pix             | vizRad              | [-3.7e+6/1988] VISTA Z-band fraction of                                       |
| 4016-4018 | I3          | ---             | vizFlag             | [0/184] VISTA Z-band SExtractor extraction                                    |
| 4020      | I1          | ---             | f_zmagvi            | [0/1] VISTA Z-band coverage flag                                              |
| 4022-4028 | F7.3        | mag             | ymagvi              | [10.9/40]?=-99 VISTA Y-band Kron-like                                         |
| 4030-4038 | F9.3        | mag             | e_ymagvi            | [0/92148]?=-99 ymagvi uncertainty                                             |
| 4040-4048 | F9.2        | uJy             | Fviy                | [-367/152008]?=-99 VISTA Y-band flux within                                   |
| 4050-4055 | F6.2        | uJy             | e_Fviy              | [0.01/45]?=-99 Fviy uncertainty                                               |
| 4057-4063 | F7.3        | mag             | ymagviISO           | [10.9/39]?=-99 VISTA Y-band isophotal                                         |
| 4065-4072 | F8.3        | mag             | e_ymagviISO         | [0/8666]?=-99 ymagviISO uncertainty                                           |
| 4074-4082 | F9.2        | uJy             | FviyISO             | [-89/156116]?=-99 VISTA Y-band isophotal                                      |
| 4084-4089 | F6.2        | uJy             | e_FviyISO           | [0.01/17]?=-99 FviyISO uncertainty                                            |
| 4091-4130 | 5F8.3       | mag             | ymagviAp            | [11/29]?=-99 VISTA Y-band fixed circular                                      |
| 4132-4171 | 5F8.3       | mag             | e_ymagviAp          | [-1/28]?=-99 ymagviAp uncertainties                                           |
| 4173-4222 | 5F10.2      | uJy             | FviyAp              | [-47/131047]?=-99 VISTA Y-band fluxes                                         |
| 4224-4258 | 5F7.2       | uJy             | e_FviyAp            | [0.01/24]?=-99 FviyAp uncertainties                                           |
| 4260-4292 | 3E11.4      | pix             | viyRad              | [-1.9e+6/2866] VISTA Y-band fraction of                                       |
| 4294-4296 | I3          | ---             | viyFlag             | [0/184] VISTA Y-band SExtractor extraction                                    |
| 4298      | I1          | ---             | f_ymagvi            | [0/1] VISTA Y-band coverage flag                                              |
| 4300-4306 | F7.3        | mag             | jmagvi              | [11.2/39]?=-99 VISTA J-band Kron-like                                         |
| 4308-4316 | F9.3        | mag             | e_jmagvi            | [0/61927]?=-99 jmagvi uncertainty                                             |
| 4318-4326 | F9.2        | uJy             | Fvij                | [-433/114755]?=-99 VISTA J-band flux within                                   |
| 4328-4333 | F6.2        | uJy             | e_Fvij              | [0.02/164]?=-99 Fvij uncertainty                                              |
| 4335-4341 | F7.3        | mag             | jmagviISO           | [11.2/39]?=-99 VISTA J-band isophotal                                         |
| 4343-4351 | F9.3        | mag             | e_jmagviISO         | [0/23726]?=-99 jmagviISO uncertainty                                          |
| 4353-4361 | F9.2        | uJy             | FvijISO             | [-96/118703]?=-99 VISTA J-band isophotal                                      |
| 4363-4368 | F6.2        | uJy             | e_FvijISO           | [0.01/137]?=-99 FvijISO uncertainty                                           |
| 4370-4409 | 5F8.3       | mag             | jmagviAp            | [11.5/29]?=-99 VISTA J-band fixed circular                                    |
| 4411-4450 | 5F8.3       | mag             | e_jmagviAp          | [-1/88]?=-99 jmagviAp uncertainties                                           |
| 4452-4496 | 5F9.2       | uJy             | FvijAp              | [-48/91297]?=-99 VISTA J-band fluxes                                          |
| 4498-4532 | 5F7.2       | uJy             | e_FvijAp            | [0.02/187]?=-99 FvijAp uncertainties                                          |
| 4534-4566 | 3E11.4      | pix             | vijRad              | [-3.1e+6/3962] VISTA J-band fraction of                                       |
| 4568-4570 | I3          | ---             | vijFlag             | [0/184] VISTA J-band SExtractor extraction                                    |
| 4572      | I1          | ---             | f_jmagvi            | [0/1] VISTA J-band coverage flag                                              |
| 4574-4580 | F7.3        | mag             | hmagvi              | [11.4/37]?=-99 VISTA H-band Kron-like                                         |
| 4582-4590 | F9.3        | mag             | e_hmagvi            | [0/24654]?=-99 hmagvi uncertainty                                             |
| 4592-4600 | F9.2        | uJy             | Fvih                | [-365/102690]?=-99 VISTA H-band flux within                                   |
| 4602-4607 | F6.2        | uJy             | e_Fvih              | [0.02/90]?=-99 Fvih uncertainty                                               |
| 4609-4615 | F7.3        | mag             | hmagviISO           | [11.3/40]?=-99 VISTA H-band isophotal                                         |
| 4617-4625 | F9.3        | mag             | e_hmagviISO         | [0/47182]?=-99 hmagviISO uncertainty                                          |
| 4627-4635 | F9.2        | uJy             | FvihISO             | [-137/107160]?=-99 VISTA H-band isophotal                                     |
| 4637-4642 | F6.2        | uJy             | e_FvihISO           | [0.01/34]?=-99 FvihISO uncertainty                                            |
| 4644-4683 | 5F8.3       | mag             | hmagviAp            | [11.7/28]?=-99 VISTA H-band fixed circular                                    |
| 4685-4724 | 5F8.3       | mag             | e_hmagviAp          | [-1/44]?=-99 hmagviAp uncertainties                                           |
| 4726-4770 | 5F9.2       | uJy             | FvihAp              | [-1282/74633] VISTA H-band fluxes                                             |
| 4772-4806 | 5F7.2       | uJy             | e_FvihAp            | [0.02/311]?=-99 FvihAp uncertainties                                          |
| 4808-4840 | 3E11.4      | pix             | vihRad              | [-1.3e+6/3962] VISTA H-band fraction of                                       |
| 4842-4844 | I3          | ---             | vihFlag             | [0/184] VISTA H-band SExtractor extraction                                    |
| 4846      | I1          | ---             | f_hmagvi            | [0/1] VISTA H-band coverage flag                                              |
| 4848-4854 | F7.3        | mag             | ksmagvi             | [11.6/39]?=-99 VISTA Ks-band Kron-like                                        |
| 4856-4865 | F10.3       | mag             | e_ksmagvi           | [0/313384]?=-99 ksmagvi uncertainty                                           |
| 4867-4874 | F8.2        | uJy             | Fviks               | [-586/84220] VISTA Ks-band flux within                                        |
| 4876-4881 | F6.2        | uJy             | e_Fviks             | [0.03/102]?=-99 Fviks uncertainty                                             |
| 4883-4889 | F7.3        | mag             | ksmagviISO          | [11.5/37]?=-99 VISTA Ks-band isophotal                                        |
| 4891-4899 | F9.3        | mag             | e_ksmagviISO        | [0/11735]?=-99 ksmagviISO uncertainty                                         |
| 4901-4908 | F8.2        | uJy             | FviksISO            | [-140/87331]?=-99 VISTA Ks-band isophotal                                     |
| 4910-4915 | F6.2        | uJy             | e_FviksISO          | [0.02/26]?=-99 FviksISO uncertainty                                           |
| 4917-4956 | 5F8.3       | mag             | ksmagviAp           | [11.9/28]?=-99 VISTA Ks-band fixed circular                                   |
| 4958-4997 | 5F8.3       | mag             | e_ksmagviAp         | [-1/27]?=-99 ksmagviAp uncertainties                                          |
| 4999-5043 | 5F9.2       | uJy             | FviksAp             | [-1882/64674] VISTA Ks-band fluxes                                            |
| 5045-5079 | 5F7.2       | uJy             | e_FviksAp           | [0.03/77]?=-99 FviksAp uncertainties                                          |
| 5081-5113 | 3E11.4      | pix             | viksRad             | [-4.4e+6/2889] VISTA Ks-band fraction of                                      |
| 5115-5117 | I3          | ---             | viksFlag            | [0/184] VISTA Ks-band SExtractor                                              |
| 5119      | I1          | ---             | f_ksmagvi           | [0/1] VISTA Ks-band coverage flag                                             |
| 5121-5127 | F7.3        | mag             | umagM               | [13/40]?=-99 MUSUBI CFHT/Megacam u-band                                       |
| 5129-5137 | F9.3        | mag             | e_umagM             | [0/10432]?=-99 umagM uncertainty                                              |
| 5139-5146 | F8.2        | uJy             | FMu                 | [-82/20877]?=-99 MUSUBI CFHT/Megacam u-band                                   |
| 5148-5153 | F6.2        | uJy             | e_FMu               | [0/9]?=-99 FMu uncertainty                                                    |
| 5155-5161 | F7.3        | mag             | umagMISO            | [13/41]?=-99 MUSUBI CFHT/Megacam u-band                                       |
| 5163-5171 | F9.3        | mag             | e_umagMISO          | [0/11226]?=-99 umagMISO uncertainty                                           |
| 5173-5180 | F8.2        | uJy             | FMuISO              | [-27/21949]?=-99 MUSUBI CFHT/Megacam u-band                                   |
| 5182-5187 | F6.2        | uJy             | e_FMuISO            | [0/3]?=-99 FMuISO uncertainty                                                 |
| 5189-5228 | 5F8.3       | mag             | umagMAp             | [13.3/31]?=-99 MUSUBI CFHT/Megacam u-band                                     |
| 5230-5269 | 5F8.3       | mag             | e_umagMAp           | [-1/6]?=-99 umagMAp uncertainties                                             |
| 5271-5315 | 5F9.2       | uJy             | FMuAp               | [-22/17152]?=-99 MUSUBI CFHT/Megacam u-band                                   |
| 5317-5351 | 5F7.2       | uJy             | e_FMuAp             | [0/0.7]?=-99 FMuAp uncertainties                                              |
| 5353-5385 | 3E11.4      | pix             | MuRad               | [-1.1e+6/2590] MUSUBI CFHT/Megacam u-band                                     |
| 5387-5389 | I3          | ---             | MuFlag              | [0/184] MUSUBI CFHT/Megacam u-band                                            |
| 5391      | I1          | ---             | f_umagM             | [0/1] MUSUBI CFHT/Megacam u-band coverage                                     |
| 5393-5399 | F7.3        | mag             | umagC               | [13.4/40]?=-99 CFHTLS CFHT/Megacam u-band                                     |
| 5401-5409 | F9.3        | mag             | e_umagC             | [0/56715]?=-99 umagC uncertainty                                              |
| 5411-5418 | F8.2        | uJy             | FCu                 | [-478/15775] CFHTLS CFHT/Megacam u-band                                       |
| 5420-5425 | F6.2        | uJy             | e_FCu               | [0.01/11]?=-99 FCu uncertainty                                                |
| 5427-5433 | F7.3        | mag             | umagCISO            | [13.4/42]?=-99 CFHTLS CFHT/Megacam u-band                                     |
| 5435-5444 | F10.3       | mag             | e_umagCISO          | [0/141324]?=-99 umagCISO uncertainty                                          |
| 5446-5453 | F8.2        | uJy             | FCuISO              | [-328/16151] CFHTLS CFHT/Megacam u-band                                       |
| 5455-5460 | F6.2        | uJy             | e_FCuISO            | [0/2]?=-99 FCuISO uncertainty                                                 |
| 5462-5501 | 5F8.3       | mag             | umagCAp             | [13.5/30]?=-99 CFHTLS CFHT/Megacam u-band                                     |
| 5503-5542 | 5F8.3       | mag             | e_umagCAp           | [-1/2]?=-99 umagCAp uncertainties                                             |
| 5544-5588 | 5F9.2       | uJy             | FCuAp               | [-49/13632]?=-99 CFHTLS CFHT/Megacam u-band                                   |
| 5590-5624 | 5F7.2       | uJy             | e_FCuAp             | [0/0.3]?=-99 FCuAp uncertainties                                              |
| 5626-5658 | 3E11.4      | pix             | CuRad               | [-1.4e+6/4643] CFHTLS CFHT/Megacam u-band                                     |
| 5660-5662 | I3          | ---             | CuFlag              | [0/184] CFHTLS CFHT/Megacam u-band                                            |
| 5664      | I1          | ---             | f_umagC             | [0/1] CFHTLS CFHT/Megacam u-band coverage                                     |
| 5666-5672 | F7.3        | mag             | gmagC               | [13/38]?=-99 CFHT/Megacam g-band Kron-like                                    |
| 5674-5682 | F9.3        | mag             | e_gmagC             | [0/13717]?=-99 gmagC uncertainty                                              |
| 5684-5691 | F8.2        | uJy             | FCg                 | [-337/20092] CFHT/Megacam g-band flux                                         |
| 5693-5698 | F6.2        | uJy             | e_FCg               | [0/7]?=-99 FCg uncertainty                                                    |
| 5700-5706 | F7.3        | mag             | gmagCISO            | [13/40]?=-99 CFHT/Megacam g-band isophotal                                    |
| 5708-5716 | F9.3        | mag             | e_gmagCISO          | [0/18794]?=-99 gmagCISO uncertainty                                           |
| 5718-5725 | F8.2        | uJy             | FCgISO              | [-193/16425] CFHT/Megacam g-band isophotal                                    |
| 5727-5732 | F6.2        | uJy             | e_FCgISO            | [0/2]?=-99 FCgISO uncertainty                                                 |
| 5734-5773 | 5F8.3       | mag             | gmagCAp             | [14.4/31]?=-99 CFHT/Megacam g-band fixed                                      |
| 5775-5814 | 5F8.3       | mag             | e_gmagCAp           | [-1/2]?=-99 gmagCAp uncertainties                                             |
| 5816-5855 | 5F8.2       | uJy             | FCgAp               | [-63/6431]?=-99 CFHT/Megacam g-band fluxes                                    |
| 5857-5891 | 5F7.2       | uJy             | e_FCgAp             | [0/0.3]?=-99 FCgAp uncertainties                                              |
| 5893-5925 | 3E11.4      | pix             | CgRad               | [-5e+6/3676] CFHT/Megacam g-band fraction                                     |
| 5927-5929 | I3          | ---             | CgFlag              | [0/184] CFHT/Megacam g-band SExtractor                                        |
| 5931      | I1          | ---             | f_gmagC             | [0/1] CFHT/Megacam g-band coverage flag                                       |
| 5933-5939 | F7.3        | mag             | rmagC               | [12.7/40]?=-99 CFHT/Megacam r-band                                            |
| 5941-5950 | F10.3       | mag             | e_rmagC             | [0/149678]?=-99 rmagC uncertainty                                             |
| 5952-5959 | F8.2        | uJy             | FCr                 | [-890/28545] CFHT/Megacam g-band flux                                         |
| 5961-5966 | F6.2        | uJy             | e_FCr               | [0.01/11]?=-99 FCr uncertainty                                                |
| 5968-5974 | F7.3        | mag             | rmagCISO            | [12/41]?=-99 CFHT/Megacam r-band isophotal                                    |
| 5976-5984 | F9.3        | mag             | e_rmagCISO          | [0/36485]?=-99 rmagCISO uncertainty                                           |
| 5986-5993 | F8.2        | uJy             | FCrISO              | [-533/56777] CFHT/Megacam r-band isophotal                                    |
| 5995-6000 | F6.2        | uJy             | e_FCrISO            | [0/2]?=-99 FCrISO uncertainty                                                 |
| 6002-6041 | 5F8.3       | mag             | rmagCAp             | [13.9/30]?=-99 CFHT/Megacam r-band fixed                                      |
| 6043-6082 | 5F8.3       | mag             | e_rmagCAp           | [-1/2]?=-99 rmagCAp uncertainties                                             |
| 6084-6123 | 5F8.2       | uJy             | FCrAp               | [-48/9406]?=-99 CFHT/Megacam r-band fluxes                                    |
| 6125-6159 | 5F7.2       | uJy             | e_FCrAp             | [0.01/0.4]?=-99 FCrAp uncertainties                                           |
| 6161-6193 | 3E11.4      | pix             | CrRad               | [-2.5e+6/4333] CFHT/Megacam r-band fraction                                   |
| 6195-6197 | I3          | ---             | CrFlag              | [0/188] CFHT/Megacam r-band SExtractor                                        |
| 6199      | I1          | ---             | f_rmagC             | [0/1] CFHT/Megacam r-band coverage flag                                       |
| 6201-6207 | F7.3        | mag             | imagC               | [12.8/37]?=-99 CFHT/Megacam i-band                                            |
| 6209-6217 | F9.3        | mag             | e_imagC             | [0/20661]?=-99 imagC uncertainty                                              |
| 6219-6227 | F9.2        | uJy             | FCi                 | [-22924/27361] CFHT/Megacam i-band flux                                       |
| 6229-6234 | F6.2        | uJy             | e_FCi               | [0.01/18]?=-99 FCi uncertainty                                                |
| 6236-6242 | F7.3        | mag             | imagCISO            | [12.8/41]?=-99 CFHT/Megacam i-band                                            |
| 6244-6253 | F10.3       | mag             | e_imagCISO          | [0/160875]?=-99 imagCISO uncertainty                                          |
| 6255-6262 | F8.2        | uJy             | FCiISO              | [-7686/28075] CFHT/Megacam i-band isophotal                                   |
| 6264-6269 | F6.2        | uJy             | e_FCiISO            | [0.01/4]?=-99 FCiISO uncertainty                                              |
| 6271-6310 | 5F8.3       | mag             | imagCAp             | [13.9/29]?=-99 CFHT/Megacam i-band fixed                                      |
| 6312-6351 | 5F8.3       | mag             | e_imagCAp           | [-1/1.5]?=-99 imagCAp uncertainty                                             |
| 6353-6402 | 5F10.2      | uJy             | FCiAp               | [-10219/9602] CFHT/Megacam i-band fluxes                                      |
| 6404-6438 | 5F7.2       | uJy             | e_FCiAp             | [0.01/1]?=-99 FCiAp uncertainties                                             |
| 6440-6472 | 3E11.4      | pix             | CiRad               | [-9e+6/3870] CFHT/Megacam i-band fraction                                     |
| 6474-6476 | I3          | ---             | CiFlag              | [0/188] CFHT/Megacam i-band SExtractor                                        |
| 6478      | I1          | ---             | f_imagC             | [0/1] CFHT/Megacam i-band coverage flag                                       |
| 6480-6486 | F7.3        | mag             | zmagC               | [12/39]?=-99 CFHT/Megacam z-band Kron-like                                    |
| 6488-6497 | F10.3       | mag             | e_zmagC             | [0/351086]?=-99 zmagC uncertainty                                             |
| 6499-6506 | F8.2        | uJy             | FCz                 | [-1247/46479] CFHT/Megacam z-band flux                                        |
| 6508-6513 | F6.2        | uJy             | e_FCz               | [0.02/94]?=-99 FCz uncertainty                                                |
| 6515-6521 | F7.3        | mag             | zmagCISO            | [12/39]?=-99 CFHT/Megacam i-band isophotal                                    |
| 6523-6531 | F9.3        | mag             | e_zmagCISO          | [0/36963]?=-99 zmagCISO uncertainty                                           |
| 6533-6540 | F8.2        | uJy             | FCzISO              | [-967/47209] CFHT/Megacam i-band isophotal                                    |
| 6542-6547 | F6.2        | uJy             | e_FCzISO            | [0.01/17]?=-99 FCzISO uncertainty                                             |
| 6549-6588 | 5F8.3       | mag             | zmagCAp             | [13/28]?=-99 CFHT/Megacam z-band fixed                                        |
| 6590-6629 | 5F8.3       | mag             | e_zmagCAp           | [-1/5]?=-99 zmagCAp uncertainties                                             |
| 6631-6675 | 5F9.2       | uJy             | FCzAp               | [-159/20729] CFHT/Megacam z-band fluxes                                       |
| 6677-6711 | 5F7.2       | uJy             | e_FCzAp             | [0.03/5]?=-99 FCzAp uncertainty                                               |
| 6713-6745 | 3E11.4      | pix             | CzRad               | [-1.3e+6/4003] CFHT/Megacam i-band fraction                                   |
| 6747-6749 | I3          | ---             | CzFlag              | [0/184] CFHT/Megacam z-band SExtractor                                        |
| 6751      | I1          | ---             | f_zmagC             | [0/1] CFHT/Megacam z-band coverage flag                                       |
| 6753-6761 | F9.2        | uJy             | F3.6um              | [-47332/18148]?=-99 Spitzer/IRAC 3.6um                                        |
| 6763-6769 | F7.2        | uJy             | e_F3.6um            | [0/6525]?=-99 F3.6um uncertainty                                              |
| 6771-6777 | F7.3        | mag             | 3.6mag              | [13/39]?=-99 Spitzer/IRAC 3.6um AB                                            |
| 6779-6787 | F9.3        | mag             | e_3.6mag            | [-1/36444]?=-99 3.6mag uncertainty                                            |
| 6789      | I1          | ---             | f_3.6mag            | [0/2] 3.6um source extraction flag                                            |
| 6791      | I1          | ---             | f_F3.6um            | [0/1] 3.6um coverage flag (0=not covered)                                     |
| 6793-6801 | F9.2        | uJy             | F4.5um              | [-12666/17536]?=-99 Spitzer/IRAC 4.5um                                        |
| 6803-6809 | F7.2        | uJy             | e_F4.5um            | [0/3648]?=-99 F4.5um uncertainty                                              |
| 6811-6817 | F7.3        | mag             | 4.5mag              | [13/38]?=-99 Spitzer/IRAC 4.5um                                               |
| 6819-6827 | F9.3        | mag             | e_4.5mag            | [-1/16343]?=-99 4.5mag uncertainty                                            |
| 6829      | I1          | ---             | f_4.5mag            | [0/2] 4.5um source extraction flag                                            |
| 6831      | I1          | ---             | f_F4.5um            | [0/1] 4.5um coverage flag (0=not covered)                                     |
| 6833-6841 | F9.2        | uJy             | F5.8um              | [-11850/26670]?=-99 Spitzer/IRAC 5.8um                                        |
| 6843-6849 | F7.2        | uJy             | e_F5.8um            | [0/3882]?=-99 F5.8um uncertainty                                              |
| 6851-6857 | F7.3        | mag             | 5.8mag              | [12.8/36]?=-99 Spitzer/IRAC 5.8um                                             |
| 6859-6868 | F10.3       | mag             | e_5.8mag            | [-1/127339]?=-99 5.8mag uncertainty                                           |
| 6870      | I1          | ---             | f_5.8mag            | [0/2] 5.8um source extraction flag                                            |
| 6872      | I1          | ---             | f_F5.8um            | [0/1] 5.8um coverage flag (0=not covered)                                     |
| 6874-6882 | F9.2        | uJy             | F8um                | [-10554/54983]?=-99 Spitzer/IRAC 8um total                                    |
| 6884-6890 | F7.2        | uJy             | e_F8um              | [0/2336]?=-99 F8um uncertainty                                                |
| 6892-6898 | F7.3        | mag             | 8mag                | [12/36]?=-99 Spitzer/IRAC 8um AB magnitude                                    |
| 6900-6909 | F10.3       | mag             | e_8mag              | [-1/211823]?=-99 8mag uncertainty                                             |
| 6911      | I1          | ---             | f_8mag              | [0/2] 8um source extraction flag                                              |
| 6913      | I1          | ---             | f_F8um              | [0/1] 8um coverage flag (0=not covered)                                       |
| 6915-6917 | I3          | ---             | [SMR2006]           | [2/505]?=-99 Source ID in Simpson+, 2006,                                     |
| 741       | (           | 1_4GHz_ID)      | 6919-6928           | F10.6 deg    RARdeg     ?=-99 Right Ascension of the radio source             |
| 6930-6939 | F10.6       | deg             | DERdeg              | ?=-99 Declination of the radio source                                         |
| 6941-6948 | F8.2        | uJy             | F1.4GHz             | [100/62110]?=-99 1.4GHz total Flux                                            |
| 6950-6955 | F6.2        | uJy             | e_F1.4GHz           | [11/161]?=-99 F1.4GHz uncertainty                                             |
| 6957-6964 | F8.4        | ---             | R1.4GHz             | [-1/1]?=-99 Reliability of the optical                                        |
| 6966-6967 | A2          | ---             | n_R1.4GHz           | Note when no reliability value                                                |
| 6969-6976 | A8          | ---             | XID                 | Source ID in Akiyama+, 2015PASJ...67...82A                                    |
| 6978-6987 | F10.6       | deg             | RAXdeg              | ?=-99 Right Ascension of the X-ray source                                     |
| 6989-6998 | F10.6       | deg             | DEXdeg              | ?=-99 Declination  of the X-ray source                                        |
| 7000-7006 | F7.3        | ---             | zUse                | [0.03/4.1]?=-99 Redshift used for NH, LHX                                     |
| 7008-7013 | F6.2        | ---             | HR2                 | [-1/1]?=-99 Hardness ratio (Xray_HR2)                                         |
| 7015-7019 | F5.1        | 10+4/m2         | logNH               | [20/24]?=-99 Log of best-estimated hydrogen                                   |
| 7021-7025 | F5.1        | [10-7W]         | logLHX              | [39/46]?=-99 Log of best-estimated X-ray                                      |
| 7027-7034 | F8.4        | ---             | zMed                | [0.002/6]?=-99 Photo-z from median of P(z)                                    |
| 7036-7043 | F8.4        | ---             | zMedL68             | [0.0008/6]?=-99 Lower limit of 68% CI for                                     |
| 7045-7052 | F8.4        | ---             | zMedU68             | [0.004/6]?=-99 Upper limit of 68% CI for                                      |
| 7054-7061 | F8.4        | ---             | zBest               | [0/6]?=-99 Best estimate of photometric                                       |
| 7063-7070 | F8.4        | ---             | zBestL68            | [0/6]?=-99 Lower limit of 68% CI for the                                      |
| 7072-7079 | F8.4        | ---             | zBestU68            | [0/6]?=-99 Upper limit of 68% CI for the                                      |
| 7081-7089 | E9.4        | ---             | ChiBest             | [2e-5/1e+10] Reduced chi sq. value for best                                   |
| 7091-7097 | F7.3        | ---             | PDZBest             | [0/117] Probability dist. between                                             |
| 7099-7104 | F6.2        | ---             | zSec                | [0/6]?=-99 Secondary photo-z solution                                         |
| 7106-7114 | E9.4        | ---             | ChiSec              | [0.001/1e+10] Reduced chi sq. value for                                       |
| 7116-7121 | F6.2        | ---             | zQSO                | [0/6]?=-99 Best photo-z solution for the                                      |
| 7123-7131 | E9.4        | ---             | ChiQSO              | [0.0002/1e+10] Reduced chi sq. value for                                      |
| 7133-7141 | E9.4        | ---             | ChiStar             | [0.001/1e+10] Reduced chi sq. value for                                       |
| 7143-7144 | I2          | ---             | Nb                  | [0/26] No. of bands used for the photometric                                  |
| 7146-7151 | F6.2        | mag             | EBV_Best            | [0/1.2]?=-99 E(B-V) (EBV_BEST)                                                |
| 7153      | I1          | ---             | n_EBV_Best          | [0/2] Extinction law used (EXTLAW_BEST) (7)                                   |
| 7155-7163 | F9.5        | Msun            | Mass                | [-99/14]? Mass (MASS_BEST)                                                    |
| 7165-7172 | E8.2        | yr              | Age                 | [1e+7/1.3e+10]?=-99 Age (AGE_BEST)                                            |
| 7174-7180 | F7.3        | Msun/yr         | SFR                 | [-99/5.6]? Star formation rate                                                |
| 7182-7189 | F8.3        | 1/yr            | sSFR                | [-112/0]? Specific SFR (SSFR_BEST)                                            |
| 7191-7199 | E9.4        | ---             | ChiPhys             | [4e-05/1e+10] Reduced chi sq. value for                                       |
| 7201-7209 | F9.5        | Lsun            | LNUV                | [-99/14]? NUV luminosity from best-fit model                                  |
| 7211-7219 | F9.5        | Lsun            | LR                  | [-99/13.2]? R-band luminosity from best-fit                                   |
| 7221-7229 | F9.5        | Lsun            | LK                  | [-99/12.5]? K-band luminosity from best-fit                                   |
| 7232-7238 | F7.3        | mag             | gMag                | [-56/25]?=-99.99 Absolute HSC g-band                                          |
| 7240-7246 | F7.3        | mag             | rMag                | [-58/25]?=-99.99 Absolute HSC r-band                                          |
| 7248-7254 | F7.3        | mag             | iMag                | [-59/25]?=-99.99 Absolute HSC i-band                                          |
| 7256-7262 | F7.3        | mag             | zMag                | [-59/25]?=-99.99 Absolute HSC z-band                                          |
| 7264-7270 | F7.3        | mag             | yMag                | [-60/25]?=-99.99 Absolute HSC y-band                                          |
| 7272-7278 | F7.3        | mag             | BMag                | [-56/25]?=-99.99 Absolute SupCam B-band                                       |
| 7280-7286 | F7.3        | mag             | VMag                | [-57/25]?=-99.99 Absolute SupCam V-band                                       |
| 7288-7294 | F7.3        | mag             | RcMag               | [-58/25]?=-99.99 Absolute SupCam Rc-band                                      |
| 7296-7302 | F7.3        | mag             | iMagSCam            | [-59/25]?=-99.99 Absolute SupCam i'-band                                      |
| 7304-7310 | F7.3        | mag             | zMagSCam            | [-59/25]?=-99.99 Absolute SupCam z'-band                                      |
| 7312-7318 | F7.3        | mag             | JMag                | [-61/25]?=-99.99 Absolute UDS J-band                                          |
| 7320-7326 | F7.3        | mag             | HMag                | [-61/25]?=-99.99 Absolute UDS H-band                                          |
| 7328-7334 | F7.3        | mag             | KMag                | [-61/25]?=-99.99 Absolute UDS K-band                                          |
| 7336-7342 | F7.3        | mag             | ZMag                | [-59/25]?=-99.99 Absolute VIDEO Z-band                                        |
| 7344-7350 | F7.3        | mag             | YMag                | [-60/25]?=-99.99 Absolute VIDEO Y-band                                        |
| 7352-7358 | F7.3        | mag             | JMagVI              | [-61/25]?=-99.99 Absolute VIDEO J-band                                        |
| 7360-7366 | F7.3        | mag             | HMagVI              | [-61/25]?=-99.99 Absolute VIDEO H-band                                        |
| 7368-7374 | F7.3        | mag             | KsMagVI             | [-61/25]?=-99.99 Absolute VIDEO Ks-band                                       |
| 7376-7382 | F7.3        | mag             | uMagMU              | [-54/25]?=-99.99 Absolute MUSUBI u-band                                       |
| 7384-7390 | F7.3        | mag             | uMagC               | [-54/25]?=-99.99 Absolute CFHTLS u-band                                       |
| 7392-7398 | F7.3        | mag             | gMagC               | [-56/25]?=-99.99 Absolute CFHTLS g-band                                       |
| 7400-7406 | F7.3        | mag             | rMagC               | [-58/25]?=-99.99 Absolute CFHTLS r-band                                       |
| 7408-7414 | F7.3        | mag             | iMagC               | [-59/25]?=-99.99 Absolute CFHTLS i-band                                       |
| 7416-7422 | F7.3        | mag             | zMagC               | [-59/25]?=-99.99 Absolute CFHTLS z-band                                       |
| 7424-7430 | F7.3        | mag             | 3.6Mag              | [-61/25]?=-99.99 Absolute IRAC 3.6um                                          |
| 7432-7438 | F7.3        | mag             | 4.5Mag              | [-61/25]?=-99.99 Absolute IRAC 4.5um                                          |
| 7440-7446 | F7.3        | mag             | 5.8Mag              | [-60/25]?=-99.99 Absolute IRAC 5.8um                                          |
| 7448-7454 | F7.3        | mag             | 8Mag                | [-60/25]?=-99.99 Absolute IRAC 8.0um                                          |
| 7456-7457 | I2          | ---             | NbPhys              | [0/28] Number of bands used for the physical                                  |
| 571       | occurrences | VIPERS          | =                   | VIMOS Public Extragalactic Redshift Survey                                    |
| 23        | ;           | Guzzo+          | 2014A&A...566A.108G | ;                                                                             |
| 8434      | occurrences | XUDS_comp       | =                   | X-UDS compilation: This sample includes spectroscopic                         |
| 2094      | catalog     | sources.        | See                 | Section 5.1 of the paper -- 1724 occurrences.                                 |
| 1486      | occurrences | C3R2            | =                   | Complete Calibration of the Color-Redshift relation survey                    |
| 319       | occurrences | Akiyama+15      | =                   | Akiyama et al. 2015PASJ...67...82A -- 168 occurrences                         |
| 10        | =           | Finoguenov+,    | 2010,               | J/MNRAS/403/2063                                                              |
| 91        | occurrences | Ono+17          | =                   | Ono+, 2018, J/PASJ/70/S10 -- 66 occurrences                                   |
| 48        | occurrences | Ouchi+08        | =                   | Ouchi+, 2008, J/ApJS/176/301                                                  |
| 44        | occurrences | Santini+15      | =                   | Santini+, 2015, J/ApJ/801/97                                                  |
| 38        | occurrences | vanBreukelen+07 | =                   | van Breukelen et al. 2007MNRAS.382..971V                                      |
| 22        | occurrences | Geach+07        | =                   | Geach+, 2007, J/MNRAS/381/1369                                                |
| 14        | occurrences | Yamada+05       | =                   | Yamada+, 2005, J/ApJ/634/861                                                  |
| 6         | occurrences | CurtisLake+12   | =                   | Curtis-Lake+ 2012MNRAS.422.1425C -- 5 occurrences                             |
| 5         | occurrences | Momcheva+16     | =                   | Momcheva+, 2016, J/ApJS/225/27 (3D-HST grism;                                 |
| 4         | occurrences | Paris+17        | =                   | Paris+, 2017, VII/279 (SDSS-DR12Q) -- 3 occurrences                           |
| 17        | =           | Shibuya+        | 2018PASJ...70S..15S | -- 3 occurrences                                                              |
| 08        | =           | Saito+          | 2008ApJ...675.1076S | -- 2 occurrences                                                              |
| 06        | =           | Simpson+,       | 2006,               | J/MNRAS/372/741                                                               |
| 2         | occurrences | Wang+16         | =                   | Wang+, 2016, J/ApJ/819/24 -- 2 occurrences                                    |
| 16        | =           | Matsuoka+       | 2016ApJ...828...26M | (<[MOK2016b] HSC JHHMM+DDMM> in Simbad) -- 1 occurrence                       |
| 4816      | 0.1386      | 26.84/26.13     | 2.4                 | r       0.6234    0.1504  26.36/25.65     2.4                                 |
| 7741      | 0.1552      | 26.11/25.43     | 2.4                 | z       0.8912    0.0773  25.52/24.84     2.4                                 |

**Note**: Reference as follows:
              --  = No redshift -- 1,156,571 occurrences
           VIPERS = VIMOS Public Extragalactic Redshift Survey
                    (Garilli+ 2014, J/A+A/562/A23 ; Guzzo+ 2014A&A...566A.108G ;
                     Scodeggio+ 2018A&A...609A..84S) -- 8434 occurrences
        XUDS_comp = X-UDS compilation: This sample includes spectroscopic
                     redshifts for 2094 catalog sources.
                     See Section 5.1 of the paper -- 1724 occurrences.
             UDSz = UKIDSS Ultra-Deep Survey (Bradshaw+ 2013MNRAS.433..194B ;
                     McLure+ 2013MNRAS.428.1088M) -- 1486 occurrences
             C3R2 = Complete Calibration of the Color-Redshift relation survey
                     (Masters et al. 2017, J/ApJ/841/111) -- 319 occurrences
       Akiyama+15 = Akiyama et al. 2015PASJ...67...82A -- 168 occurrences
    Finoguenov+10 = Finoguenov+, 2010, J/MNRAS/403/2063
                     (<[FWT2010] DDD.dddddd+DD.dddddd> in Simbad)
                     -- 91 occurrences
           Ono+17 = Ono+, 2018, J/PASJ/70/S10 -- 66 occurrences
 Harikane_in_prep = Y. Harikane et al. (2018, in preparation) -- 48 occurrences
         Ouchi+08 = Ouchi+, 2008, J/ApJS/176/301
                     (<[OSA2008] NBNNN-A-NNNNNN> in Simbad) -- 44 occurrences
       Santini+15 = Santini+, 2015, J/ApJ/801/97
                     (<[SFF2015] NNNNNNNN> in Simbad) -- 38 occurrences
  vanBreukelen+07 = van Breukelen et al. 2007MNRAS.382..971V
                     (<[VCR2007] CVB13-NNA> in Simbad) -- 22 occurrences
         Geach+07 = Geach+, 2007, J/MNRAS/381/1369
                     (<[GSR2007] SXDF-iS-NNNNNN> in Simbad) -- 14 occurrences
        Yamada+05 = Yamada+, 2005, J/ApJ/634/861
                     (<SXDS JHHMMSS.ss+DDMMSS.s> in Simbad) -- 6 occurrences
    CurtisLake+12 = Curtis-Lake+ 2012MNRAS.422.1425C -- 5 occurrences
  Higuchi_in_prep = R. Higuchi et al. (2018, in preparation) -- 5 occurrences
      Momcheva+16 = Momcheva+, 2016, J/ApJS/225/27 (3D-HST grism;
                     <[SWM2014] UDS NNNNN> in Simbad) -- 4 occurrences
         Paris+17 = Paris+, 2017, VII/279 (SDSS-DR12Q) -- 3 occurrences
       Shibuya+17 = Shibuya+ 2018PASJ...70S..15S -- 3 occurrences
         Saito+08 = Saito+ 2008ApJ...675.1076S -- 2 occurrences
       Simpson+06 = Simpson+, 2006, J/MNRAS/372/741
                     (<[SMR2006] NNNN> in Simbad) -- 2 occurrences
          Wang+16 = Wang+, 2016, J/ApJ/819/24 -- 2 occurrences
      Matsuoka+16 = Matsuoka+ 2016ApJ...828...26M
                     (<[MOK2016b] HSC JHHMM+DDMM> in Simbad) -- 1 occurrence
Note (2): This is identical to Z_MED for all objects except
    those flagged as stars, STAR_FLAG. For objects where Z_MED estimate is
    not available, Z_BEST is used instead.
Note (3): Filters included in the multi-wavelength catalog (see Table 1):
    
     Inst/    Filt    Central   FWHM    5{sigma}         Area
     Survey           {lambda}            depth
                       [um]     [um]     [mag]          [deg^2^]
                                         (2"/3")
    
     HSC      g       0.4816    0.1386  26.84/26.13     2.4
              r       0.6234    0.1504  26.36/25.65     2.4
              i       0.7741    0.1552  26.11/25.43     2.4
              z       0.8912    0.0773  25.52/24.84     2.4
              y       0.9780    0.0783  24.79/24.09     2.4

</details>
