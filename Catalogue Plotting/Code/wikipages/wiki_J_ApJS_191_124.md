## Summary

We present the results of a program to acquire high-quality optical spectra of X-ray sources detected in the Extended-Chandra Deep Field-South (E-CDF-S) and its central 2Ms area. New spectroscopic redshifts, up to z=4, are measured for 283 counterparts to Chandra sources with deep exposures (t~2-9hr per pointing) using multi-slit facilities on both VLT (VIMOS) and Keck (DEIMOS), thus bringing the total number of spectroscopically identified X-ray sources to over 500 in this survey field. Since our new spectroscopic identifications are mainly associated with X-ray sources in the shallower 250ks coverage, we provide a comprehensive catalog of X-ray sources detected in the E-CDF-S including the optical and near-infrared counterparts, determined by a likelihood routine, and redshifts (both spectroscopic and photometric), that incorporate published spectroscopic catalogs, thus resulting in a final sample with a high fraction (80%) of X-ray sources having secure identifications. Our redshift catalog includes 17 type-2 QSOs at 1<~z<~3.5. Based on our deepest (9 hr) VLT/VIMOS observation, we identify "elusive" optically faint galaxies (Rmag~25) at z~2-3 based upon the detection of interstellar absorption lines (e.g., OII+SiIV, CII], CIV).

## Catalogue Schema

<details>
<summary>table4.dat catalogue schema</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                                                   |
|:--------|:---------|:--------|:----------|:-------------------------------------------------------------------------------|
| 1- 3    | I3       | ---     | XID       | Lehmer et al., 2005 (Cat. J/ApJS/161/21)                                       |
| 5- 12   | F8.5     | deg     | RAdeg     | Right Ascension in decimal degrees (J2000) (1)                                 |
| 14- 22  | F9.5     | deg     | DEdeg     | Declination in decimal degrees (J2000) (1)                                     |
| 24- 30  | A7       | ---     | Cat       | Catalog associated with counterpart (2)                                        |
| 32- 34  | F3.1     | arcsec  | Sep       | Separation between X-ray and its counterpart                                   |
| 36- 40  | F5.1     | ---     | LR        | Likelihood ratio (3)                                                           |
| 42- 45  | F4.2     | ---     | Rel       | Reliability for true counterpart (4)                                           |
| 47- 50  | F4.1     | mag     | Rmag      | ? R band AB magnitude                                                          |
| 52- 56  | F5.3     | ---     | zsp       | ? Counterpart spectroscopic redshift                                           |
| 58- 60  | F3.1     | ---     | q_zsp     | ? Quality flag on zspec (5)                                                    |
| 62- 63  | I2       | ---     | r_zsp     | ? Spectroscopic catalog (G2)                                                   |
| 65- 69  | A5       | ---     | Class     | Spectroscopic classification (G1)                                              |
| 71- 75  | F5.3     | ---     | zph       | ? Photometric redshift (6)                                                     |
| 77- 81  | F5.3     | ---     | e_zph     | ? Lower limit uncertainty in zphot                                             |
| 83- 87  | F5.3     | ---     | E_zph     | ? Upper limit uncertainty in zphot                                             |
| 2       | for      | further | details.  | Note (4): Reliability (0<R_j_<1; Sutherland & Saunders 1992) that a particular |
| 2       | for      | further | details.  | Note (5): Where "2" is secure, "1" for some uncertainty, "0" for no redshift.  |
| 5       | if       | in      | agreement | with photometric redshift.                                                     |

**Note**: Of the optical/near-infrared counterpart.
Note (2): Catalogs associated are:
    ACS-z = GOODS-z or GEMS-z; z-band HST/ACS catalog;
    WFI-R = WFI R-band catalog;
   SOFI-H = H-band catalog from SOFI;
   SOFI-K = K-band catalog from SOFI, 
  ISSAC-K = K-band catalog from VLT/ISAAC
Note (3): The likelihood ratio (LR; Equation (1)) is the probability that a
          given optical or near-infrared source is the true counterpart to the
          X-ray detection, relative to the chance that the same object is a
          random background source. LR=(q(m)f(r))/n(m); see section 2 for
          further details.
Note (4): Reliability (0<R_j_<1; Sutherland & Saunders 1992) that a particular
          source (j) is the true counterpart: R_j_=LR_j_/{Sigma}_i_LR_i_+(1-Q)
          See section 2 for further details.
Note (5): Where "2" is secure, "1" for some uncertainty, "0" for no redshift.
          A +0.5 if in agreement with photometric redshift.
Note (6): From Rafferty et al. (2010, in prep) and Luo et al. (2010,
          Cat. J/ApJS/187/560).

</details>

<details>
<summary>table7.dat catalogue schema</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                   |
|:--------|:---------|:--------|:--------|:-----------------------------------------------|
| 1- 3    | I3       | ---     | XID     | Luo et al. 2008 (Cat. J/ApJS/179/19) number,   |
| 5- 12   | F8.5     | deg     | RAdeg   | Right Ascension of optical counterpart (J2000) |
| 14- 22  | F9.5     | deg     | DEdeg   | Declination of optical counterpart (J2000)     |
| 24- 27  | F4.1     | mag     | Rmag    | R band AB magnitude                            |
| 29- 33  | F5.3     | ---     | zsp     | Spectroscopic redshift                         |
| 35      | I1       | ---     | q_zsp   | Quality of z: 1=some uncertainty, 2=secure.    |
| 37- 41  | A5       | ---     | Class   | Spectroscopic classification (G1)              |
| 43- 44  | I2       | ---     | r_zsp   | Spectroscopic origin (G2)                      |
</details>

<details>
<summary>table8.dat catalogue schema</summary>

| Bytes   | Format   | Units         | Label   | Explanations                                   |
|:--------|:---------|:--------------|:--------|:-----------------------------------------------|
| 1- 3    | I3       | ---           | RID     | Radio identification number (1)                |
| 5- 12   | F8.5     | deg           | RAdeg   | Right Ascension of optical counterpart (J2000) |
| 14- 22  | F9.5     | deg           | DEdeg   | Declination of optical counterpart (J2000)     |
| 24- 27  | F4.1     | mag           | Rmag    | R band AB magnitude                            |
| 29- 33  | F5.3     | ---           | zsp     | Spectroscopic redshift                         |
| 35      | I1       | ---           | q_zsp   | Quality of zsp: 1=some uncertainty, 2=secure.  |
| 37- 41  | A5       | ---           | Class   | Spectroscopic classification (G1)              |
| 43- 46  | A4       | ---           | Tel     | Origin of z (Keck or VLT)                      |
| 2008    | Cat.     | J/ApJS/179/71 | and     | Miller et al., 2008, Cat. J/ApJS/179/114,      |

**Note**: Radio identification number from Kellermann et al., 2008
          Cat. J/ApJS/179/71 and Miller et al., 2008, Cat. J/ApJS/179/114,
          <[KFM2008] RID NNNA> in simbad.

</details>
