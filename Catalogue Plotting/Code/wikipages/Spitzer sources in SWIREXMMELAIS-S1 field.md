**Authors:** La Franca F., Feruglio C., Fiore F., Puccetti S., Cocchia F.,, Berta S., Brusa M., Cimatti A., Comastri A., Franceschini A., Gruppioni C.,, Maiolino R., Matute I., Polletta M., Pozzetti L., Pozzi F., Vignali C.,, Zamorani G., Oliver S., Rowan-Robinson M., Smith G., Lonsdale C., <Astrophys. J., 703, 1778-1790 (2009)>, =2009ApJ...703.1778S

## Summary: Spitzer sources in SWIRE/XMM/ELAIS-S1 field 

We present a catalog of optical spectroscopic identifications of sources detected by Spitzer at 3.6 or 24um down to ~10 and ~280uJy, respectively, in the SWIRE/XMM-Newton/ELAIS-S1 field and classified via line width analysis and diagnostic diagrams. A total of 1376 sources down to R~24.2mag have been identified (1362 detected at 3.6um, 419 at 24um, and 405 at both) by low-resolution optical spectroscopy carried out with FORS2, VIMOS, and EFOSC2 at the Very Large Telescope and 3.6m ESO telescope. The spectroscopic campaigns have been carried out over the central 0.6deg^2^ area of ELAIS-S1 which, in particular, has also been observed by XMM-Newton and Chandra. We find the first direct optical spectroscopic evidence that the fraction of active galactic nuclei (AGNs; mostly AGN2) increases with increasing F(24um)/F(R) ratio, reaching values of 70(+/-20)% in the range 316<F(24um)/F(R)<1000. We present an Infrared Array Camera-Multiband Imaging Photometer color-color diagram able to separate AGN1 from obscured AGN2 candidates. After having corrected for the spectroscopic incompleteness of our sample, the result is that the AGN fraction at F(24um)~0.8mJy is ~22(+/-7)% and decreases slowly to ~19(+/-5)% down to F(24um)~0.3mJy.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-703-1778/Subcatalogues/ELAIS%20S1/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**z:** Redshift (spectroscopic) 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-703-1778/Subcatalogues/ELAIS%20S1/Plots/zspec.png)
<details>
<summary>Quality flag . . .</summary>

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-703-1778/Subcatalogues/ELAIS%20S1/Plots/q_zspec.png)</details>
## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units         | Label      | Explanations                                       |
|:--------|:---------|:--------------|:-----------|:---------------------------------------------------|
| 1- 4    | I4       | ---           | Seq        | Running identification number                      |
| 6- 25   | A20      | ---           | ESIS       | ESIS identification from Berta et al., 2006,       |
| 27- 33  | F7.5     | deg           | RAdeg      | Right Ascension in decimal degrees (J2000)         |
| 35- 43  | F9.5     | deg           | DEdeg      | Declination in decimal degrees (J2000)             |
| 45- 49  | F5.2     | mag           | Rmag       | R band Vega magnitude                              |
| 51- 55  | F5.3     | ---           | z          | Redshift (spectroscopic)                           |
| 57- 59  | F3.1     | ---           | q_z        | Quality code for z (2=reliable) (1)                |
| 61      | I1       | ---           | Class      | [1/5] Spectroscopic classification code (2)        |
| 63- 88  | A26      | ---           | SWIRE      | SWIRE identification name,                         |
| 90- 96  | F7.4     | [uJy]         | S3.6um     | ? Log of 3.6 micron band flux density              |
| 98-104  | F7.4     | [uJy]         | S24um      | ? Log of 24 micron band flux density               |
| 106-108 | I3       | ---           | XMMES1     | ? XMM source name (4)                              |
| 0       | =        | reliable,     | based      | on >2 confirmed lines                              |
| 5       | =        | very          | plausible, | based on 2 lines                                   |
| 0       | =        | uncertain     | Note       | (2): Spectroscopic classification code as follows: |
| 1       | =        | type-1        | AGN        | 2 = type-2 AGN                                     |
| 3       | =        | Emission-Line | Galaxy     | (ELG)                                              |
| 4       | =        | normal        | galaxy     | 5 = star                                           |

**Note**: Quality code is numbered as:
    2.0 = reliable, based on >2 confirmed lines
    1.5 = very plausible, based on 2 lines
    1.0 = uncertain
Note (2): Spectroscopic classification code as follows:
      1 = type-1 AGN
      2 = type-2 AGN
      3 = Emission-Line Galaxy (ELG)
      4 = normal galaxy
      5 = star
Note (3): Of the most probable corresponding Spitzer source.
     Contains in a few cases a number in place of the SWIRE identification,
     not explained in the paper.
Note (4): see Feruglio et al., 2008, Cat. <J/A+A/488/417>.

</details>
