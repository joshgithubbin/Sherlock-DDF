**Authors:** Sanders D.B., Surace J.A., Aussel H., Salvato M.,, Le Floc'h E., Huynh M.T., Scoville N.Z., Afonso-Luis A., Bhattacharya B.,, Capak P., Fadda D., Fu H., Helou G., Ilbert O., Kartaltepe J.S.,, Koekemoer A.M., Lee N., Murphy E., Sargent M.T., Schinnerer E., Sheth K.,, Shopbell P.L., Shupe D.L., Yan L., <Astron. J., 138, 1261-1270 (2009)>, =2009AJ....138.1261F

## Summary: Spitzer/MIPS observations of the COSMOS field 

We present Spitzer 70 and 160um observations of the COSMOS Spitzer survey (S-COSMOS). The data processing techniques are discussed for the publicly released products consisting of images and source catalogs. We present accurate 70 and 160um source counts of the COSMOS field and find reasonable agreement with measurements in other fields and with model predictions. The previously reported counts for GOODS-North and the extragalactic First Look Survey are updated with the latest calibration, and counts are measured based on the large area SWIRE survey to constrain the bright source counts. We measure an extragalactic confusion noise level of {sigma}_c_=9.4+/-3.3mJy (q=5) for the MIPS 160um band based on the deep S-COSMOS data and report an updated confusion noise level of {sigma}_c_=0.35+/-0.15mJy (q=5) for the MIPS 70um band.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-AJ-138-1261/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>table3.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                                  |
|:--------|:---------|:--------|:----------|:--------------------------------------------------------------|
| 1- 9    | A9       | ---     | ---       | [SCOSMOS70]                                                   |
| 11- 26  | A16      | ---     | SCOSMOS70 | Source Name (JHHMMSS.s+DDMMSS)                                |
| 28- 37  | F10.6    | deg     | RAdeg     | Right Ascension in decimal degrees (J2000)                    |
| 39- 46  | F8.6     | deg     | DEdeg     | Declination in decimal degrees (J2000)                        |
| 48- 50  | F3.1     | arcsec  | e_pos     | The 2{sigma} radial positional error                          |
| 52- 56  | F5.1     | mJy     | S70       | Total Spitzer/MIPS 70 micron band flux density                |
| 58- 62  | F5.1     | mJy     | e_S70     | The 1{sigma} error on S70 (1)                                 |
| 64- 67  | F4.1     | ---     | SNR       | Signal-to-Noise Ratio of the source peak                      |
| 69- 70  | A2       | ---     | Flag      | [ap ] Measurement method flag (2)                             |
| 96      | arcsec;  | ap      | =         | aperture measurement whose whose flux was divided between two |

**Note**: Including calibration uncertainty.
Note (2): Flag as follows:
    p = Point-source Response Function (PRF);
    a = aperture measurement with a diameter of 96 arcsec;
   ap = aperture measurement whose whose flux was divided between two
        components based on the strengths of their peaks.

</details>

<details>
<summary>table4.dat</summary>

| Bytes   | Format   | Units   | Label      | Explanations                               |
|:--------|:---------|:--------|:-----------|:-------------------------------------------|
| 1- 10   | A10      | ---     | ---        | [SCOSMOS160]                               |
| 12- 27  | A16      | ---     | SCOSMOS160 | Source Name (JHHMMSS.s+DDMMSS)             |
| 29- 38  | F10.6    | deg     | RAdeg      | Right Ascension in decimal degrees (J2000) |
| 40- 47  | F8.6     | deg     | DEdeg      | Declination in decimal degrees (J2000)     |
| 49- 52  | F4.1     | arcsec  | e_pos      | The 2{sigma} radial positional error       |
| 54- 60  | F7.1     | mJy     | S160       | Total Spitzer/MIPS 160 micron band flux    |
| 62- 67  | F6.1     | mJy     | e_S160     | The 1{sigma} error on S160 (1)             |
| 69- 72  | F4.1     | ---     | SNR        | Signal-to-Noise Ratio of the source peak   |
| 74      | A1       | ---     | Flag       | [ap] Measurement method flag (2)           |

**Note**: Including calibration uncertainty.
Note (2): Flag as follows:
    p = Point-source Response Function (PRF);
    a = aperture measurement with a diameter of 4 arcmin.

</details>
