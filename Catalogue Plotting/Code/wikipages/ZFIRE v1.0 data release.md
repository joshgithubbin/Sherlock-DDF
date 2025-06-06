**Authors:** Glazebrook K., Kacprzak G.G., Yuan T., Tran K.-V.,, Spitler L., Kewley L., Straatman C., Cowley M., Fisher D., Labbe I.,, Tomczak A., Allen R., Alcorn L., <Astrophys. J., 828, 21-21 (2016)>, =2016ApJ...828...21N (SIMBAD/NED BibCode)

## Summary: ZFIRE v1.0 data release 

We present an overview and the first data release of ZFIRE, a spectroscopic redshift survey of star-forming galaxies that utilizes the MOSFIRE instrument on Keck-I to study galaxy properties in rich environments at 1.5<z<2.5. ZFIRE measures accurate spectroscopic redshifts and basic galaxy properties derived from multiple emission lines. The galaxies are selected from a stellar mass limited sample based on deep near infrared imaging (K_AB_<25) and precise photometric redshifts from the ZFOURGE and UKIDSS surveys as well as grism redshifts from 3DHST. Between 2013 and 2015, ZFIRE has observed the COSMOS and UDS legacy fields over 13 nights and has obtained 211 galaxy redshifts over 1.57<z<2.66 from a combination of nebular emission lines (such as H{alpha}, [NII], H{beta}, [OII], [OIII], and [SII]) observed at 1-2{mu}m. Based on our medium-band near infrared photometry, we are able to spectrophotometrically flux calibrate our spectra to ~10% accuracy. ZFIRE reaches 5{sigma} emission line flux limits of ~3x10^-18^erg/s/cm^2^ with a resolving power of R=3500 and reaches masses down to ~10^9^M_{sun}_. We confirm that the primary input survey, ZFOURGE, has produced photometric redshifts for star-forming galaxies (including highly attenuated ones) accurate to {Delta}z/(1+z_spec_)=0.015 with 0.7% outliers. We measure a slight redshift bias of <0.001, and we note that the redshift bias tends to be larger at higher masses. We also examine the role of redshift on the derivation of rest-frame colors and stellar population parameters from SED fitting techniques. The ZFIRE survey extends spectroscopically confirmed z~2 samples across a richer range of environments, here we make available the first public release of the data for use by the community.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-828-21/Subcatalogues/XMM-LSS/Plots/fieldcover.png)
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-828-21/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zsp:**  
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-828-21/Subcatalogues/XMM-LSS/Plots/zspec.png)
<details>
<summary>Quality flag . . .</summary>

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-828-21/Subcatalogues/XMM-LSS/Plots/q_zspec.png)</details>
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-828-21/Subcatalogues/COSMOS/Plots/zspec.png)
<details>
<summary>Quality flag . . .</summary>

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-828-21/Subcatalogues/COSMOS/Plots/q_zspec.png)</details>
## Catalogue Schema

<details>
<summary>zfire*.dat</summary>

| Bytes   | Format   | Units     | Label    | Explanations                                                 |
|:--------|:---------|:----------|:---------|:-------------------------------------------------------------|
| 1- 5    | I5       | ---       | Name     | [66/46922] Unique ZFIRE identifier                           |
| 6       | A1       | ---       | m_Name   | [bc ] b,c: other measurements on the object                  |
| 8- 18   | F11.7    | deg       | RAdeg    | Right ascension (J2000)                                      |
| 20- 29  | F10.7    | deg       | DEdeg    | Declination (J2000)                                          |
| 31- 36  | A6       | ---       | Field    | Field ("COSMOS" or "UDS")                                    |
| 38- 50  | F13.10   | mag       | Ksmag    | [18.9/25.4]? Ks-band AB magnitude                            |
| 52- 67  | F16.14   | mag       | e_Ksmag  | [0.002/1.1]? Ksmag uncertainty                               |
| 69- 76  | F8.6     | ---       | zsp      | [0.5/3.6]? ZFIRE spectroscopic redshift                      |
| 78- 85  | E8.6     | ---       | e_zsp    | [6e-06/0.0005]? zsp uncertainty                              |
| 87      | I1       | ---       | q_zsp    | [1/3] ZFIRE redshift quality flag (2)                        |
| 89- 93  | A5       | ---       | Mm       | Cluster membership flag (3)                                  |
| 95- 99  | F5.2     | [Msun]    | Mass     | [6.8/11.6]? Stellar mass from FAST                           |
| 101-105 | F5.2     | mag       | Av       | [0/3.3]? Dust extinction from FAST                           |
| 107-111 | A5       | ---       | AGN      | AGN flag (4)                                                 |
| 113-118 | F6.3     | 10-20W/m2 | FHa      | [0/37]? Emission line H{alpha} flux                          |
| 120-126 | F7.3     | 10-20W/m2 | e_FHa    | [0.03/111]? FHa uncertainty (5)(6)                           |
| 128-133 | F6.3     | 10-20W/m2 | FHalim   | [0/13]? 1{sigma} upper limit for the                         |
| 135-140 | F6.3     | 10-20W/m2 | FNII     | [0/15]? Emission line [NII] flux (6585{AA})                  |
| 142-146 | F5.3     | 10-20W/m2 | e_FNII   | [0.02/1]? FNII uncertainty (5)(6)                            |
| 148-152 | F5.3     | 10-20W/m2 | FNIIlim  | [0/7]? 1{sigma} upper limit for the                          |
| 154-158 | F5.3     | 10-20W/m2 | FHb      | [0/10]? Emission line H{beta} flux                           |
| 160-168 | F9.3     | 10-20W/m2 | e_FHb    | [0.02/10789]? FHb uncertainty (5)(6)                         |
| 170-174 | F5.3     | 10-20W/m2 | FHblim   | [0/8]? 1{sigma} upper limit for the                          |
| 176-181 | F6.3     | 10-20W/m2 | FOIII    | [0/29]? Emission line [OIII] flux                            |
| 183-191 | F9.3     | 10-20W/m2 | e_FOIII  | [0.03/10235]? FOIII uncertainty (5)(6)                       |
| 193-197 | F5.3     | 10-20W/m2 | FOIIIlim | [0/3]? 1{sigma} upper limit for the                          |
| 199-205 | F7.3     | 10-20W/m2 | FOII     | [0.05/247]? Emission line [OII] flux (5)                     |
| 207-215 | F9.3     | 10-20W/m2 | e_FOII   | [0/65093]? FOII uncertainty (5)(6)                           |
| 217-221 | F5.3     | 10-20W/m2 | FOIIlim  | [0/3]? 1{sigma} upper limit for the                          |
| 1       | and      | Appendix  | B        | for further explanations.                                    |
| 1       | =        | These     | are      | objects with no line detection with S/N<5. These objects are |
| 2       | =        | These     | are      | objects with one emission line with S/N>5 and                |
| 3       | =        | These     | are      | objects with more than one emission line identified with     |
| 5       | or       | one       | emission | line identified with S/N>5 with                              |

**Note**: The survey selection for this data release was done using the ZFOURGE
          internal catalogs, and therefore the results presented here onwards
          could vary slightly from the ZFOURGE public data release (see
          Straatman+, 2016, J/ApJ/830/51).
          See section 3.1 and Appendix B for further explanations.
Note (2): Quality flag as follows:
   1  = These are objects with no line detection with S/N<5. These objects are
        not included in our final spectroscopic sample.
   2  = These are objects with one emission line with S/N>5 and
        a |z_spec_-z_phot_|>0.2.
   3  = These are objects with more than one emission line identified with
        S/N>5 or one emission line identified with S/N>5 with
        a |z_spec_-z_phot_|<0.2.
Note (3):
 True = True objects that are spectroscopically confirmed cluster members
        in either the COSMOS (Yuan+ 2014ApJ...795L..20Y) or
        UDS (Tran+ 2015ApJ...811...28T) fields.
Note (4): AGNs are flagged following Cowley+ (2016MNRAS.457..629C) and/or
          Coil+ (2015ApJ...801...35C) selection criteria.
Note (5): The nebular emission line fluxes (along with errors and limits) are
          given in units of 10-17erg/s/cm^2^.
Note (6): The error of the line fluxes are from the integration of the error
          spectrum within the same limits used for the emission line extraction.

</details>

<details>
<summary>spcos.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                      |
|:--------|:---------|:--------|:----------|:----------------------------------|
| 1- 64   | A64      | ---     | FileName1 | "KbandLargeArea" file name        |
| 66-118  | A53      | ---     | FileName2 | Hband file name                   |
| 120-180 | A61      | ---     | FileName3 | "shallowmask" in K-band file name |
| 182-231 | A50      | ---     | FileName4 | "DeepKband" file name             |
| 233-296 | A64      | ---     | FileName5 | Other file name                   |
| 298-350 | A53      | ---     | FileName6 | Other file name                   |
| 352-404 | A53      | ---     | FileName7 | Other file name                   |
</details>

<details>
<summary>spuds.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations       |
|:--------|:---------|:--------|:----------|:-------------------|
| 1- 37   | A37      | ---     | FileNameJ | J-band file name   |
| 39- 81  | A43      | ---     | FileNameH | H-band file name   |
| 83-127  | A45      | ---     | FileNameY | Y-band file name   |
| 129-163 | A35      | ---     | FileName4 | Other file name(s) |
| 165-199 | A35      | ---     | FileName5 | Other file name(s) |
</details>
