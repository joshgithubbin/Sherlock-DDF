**Authors:** Swinbank A.M., Smail I., Simpson J.M., Casey C.M.,, Chapman S.C., da Cunha E., Hodge J.A., Walter F., Wardlow J.L.,, Alexander D.M., Brandt W.N., de Breuck C., Coppin K.E.K., Dannerbauer H.,, Dickinson M., Edge A.C., Gawiser E., Ivison R.J., Karim A., Kovacs A.,, Lutz D., Menten K., Schinnerer E., Weiss A., van der Werf P., <Astrophys. J., 840, 78 (2017)>, =2017ApJ...840...78D

## Summary: Redshift survey of ALMA-identified SMGs in ECDFS 

We present spectroscopic redshifts of S_870{mu}m_>~2mJy submillimeter galaxies (SMGs), which have been identified from the ALMA follow-up observations of 870{mu}m detected sources in the Extended Chandra Deep Field South (the ALMA-LESS survey). We derive spectroscopic redshifts for 52 SMGs, with a median of z=2.4+/-0.1. However, the distribution features a high-redshift tail, with ~23% of the SMGs at z>=3. Spectral diagnostics suggest that the SMGs are young starbursts, and the velocity offsets between the nebular emission and UV ISM absorption lines suggest that many are driving winds, with velocity offsets of up to 2000km/s. Using the spectroscopic redshifts and the extensive UV-to-radio photometry in this field, we produce optimized spectral energy distributions (SEDs) using Magphys, and use the SEDs to infer a median stellar mass of M_*_=(6+/-1)x10^10^M_{sun}_ for our SMGs with spectroscopic redshift. By combining these stellar masses with the star formation rates (measured from the far-infrared SEDs), we show that SMGs (on average) lie a factor of ~5 above the so-called "main sequence" at z~2. We provide this library of 52 template fits with robust and uniquely well-sampled SEDs as a resource for future studies of SMGs, and also release the spectroscopic catalog of ~2000 (mostly infrared-selected) galaxies targeted as part of the spectroscopic campaign.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-840-78/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zspec:** [0.6/5]? Spectroscopic redshift 
 

## Photometric Redshift 
 
**zphot:** [0.3/7]? Photometric redshift 
 

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                               |
|:--------|:---------|:--------|:--------|:-------------------------------------------|
| 1- 8    | A8       | ---     | ID      | Identifier                                 |
| 10- 17  | F8.5     | deg     | RAdeg   | Right Ascension in decimal degrees (J2000) |
| 19- 27  | F9.5     | deg     | DEdeg   | Declination in decimal degrees (J2000)     |
| 29- 37  | E9.5     | ---     | zspec   | [0/5.7]? Spectroscopic redshift            |
| 39      | I1       | ---     | q_zspec | Quality flag for zspec (1=secure) (G1)     |
| 41- 45  | A5       | ---     | Inst    | Instruments used (G2)                      |
</details>

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                               |
|:--------|:---------|:--------|:--------|:-------------------------------------------|
| 1- 5    | A5       | ---     | ---     | [ALESS]                                    |
| 7- 12   | A6       | ---     | ALESS   | ALESS identifier (1)                       |
| 14      | A1       | ---     | f_ALESS | [i] i = A supplementary SMGs source        |
| 16- 24  | F9.6     | deg     | RAdeg   | Right Ascension in decimal degrees (J2000) |
| 26- 35  | F10.6    | deg     | DEdeg   | Declination in decimal degrees (J2000)     |
| 37- 42  | F6.4     | ---     | zspec   | [0.6/5]? Spectroscopic redshift            |
| 44      | A1       | ---     | f_zspec | [d] Flag on zspec (2)                      |
| 46      | I1       | ---     | q_zspec | Quality flag for zspec (1=secure) (G1)     |
| 48- 51  | F4.2     | ---     | zphot   | [0.3/7]? Photometric redshift              |
| 53- 57  | F5.2     | ---     | E_zphot | ? Upper uncertainty in zphot               |
| 59- 62  | F4.2     | ---     | e_zphot | ? Lower uncertainty in zphot               |
| 64      | A1       | ---     | Set     | Source; M(ain) or S(upplementary) catalogs |
| 66- 74  | A9       | ---     | Inst    | Instruments used (G2)                      |
| 76-295  | A220     | ---     | Notes   | Additional notes                           |
| 22      | ALESS    | SMGs    | not     | targeted in our spectroscopy programme     |

**Note**: The 22 ALESS SMGs not targeted in our spectroscopy programme
          (and without redshifts from literature) are not listed here.
Note (2):
    d = These redshifts are for the six sources which also have literature
        spectroscopic redshifts described in Section 3.

</details>
