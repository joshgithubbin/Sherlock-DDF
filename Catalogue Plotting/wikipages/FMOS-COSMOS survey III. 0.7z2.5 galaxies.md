**Authors:** Silverman J.D., Kashino D., Sanders D., Kartaltepe J.S., Arimoto N.,, Renzini A., Rodighiero G., Daddi E., Zahid J., Nagao T., Kewley L.J.,, Lilly S.J., Sugiyama N., Baronchelli I., Capak P., Carollo C.M., Chu J.,, Hasinger G., Ilbert O., Juneau S., Kajisawa M., Koekemoer A.M., Kovac K.,, Le Fevre O., Masters D., McCracken H.J., Onodera M., Schulze A.,, Scoville N., Strazzullo V., Taniguchi Y., <Astrophys. J. Suppl. Ser., 220, 12 (2015)>, =2015ApJS..220...12S (SIMBAD/NED BibCode)

## Summary: FMOS-COSMOS survey III. 0.7<z<2.5 galaxies 

We present a spectroscopic survey of galaxies in the COSMOS field using the Fiber Multi-object Spectrograph (FMOS), a near-infrared instrument on the Subaru Telescope. Our survey is specifically designed to detect the H{alpha} emission line that falls within the H-band (1.6-1.8{mu}m) spectroscopic window from star-forming galaxies with 1.4<z<1.7 and M_stellar_>~10^10^M_{sun}_. With the high multiplex capability of FMOS, it is now feasible to construct samples of over 1000 galaxies having spectroscopic redshifts at epochs that were previously challenging. The high-resolution mode (R~2600) effectively separates H{alpha} and [NII]{lambda}6585, thus enabling studies of the gas-phase metallicity and photoionization state of the interstellar medium. The primary aim of our program is to establish how star formation depends on stellar mass and environment, both recognized as drivers of galaxy evolution at lower redshifts. In addition to the main galaxy sample, our target selection places priority on those detected in the far-infrared by Herschel/PACS to assess the level of obscured star formation and investigate, in detail, outliers from the star formation rate (SFR)--stellar mass relation. Galaxies with H{alpha} detections are followed up with FMOS observations at shorter wavelengths using the J-long (1.11-1.35{mu}m) grating to detect H{beta} and [OIII]{lambda}5008 which provides an assessment of the extinction required to measure SFRs not hampered by dust, and an indication of embedded active galactic nuclei. With 460 redshifts measured from 1153 spectra, we assess the performance of the instrument with respect to achieving our goals, discuss inherent biases in the sample, and detail the emission-line properties. Our higher-level data products, including catalogs and spectra, are available to the community.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-220-12/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**z:** [0.7/2.5]?=-99 Best measurement of redshift 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-220-12/Subcatalogues/COSMOS/Plots/zspec.png)
## Catalogue Schema

<details>
<summary>table6.dat</summary>

| Bytes   | Format   | Units      | Label     | Explanations                                          |
|:--------|:---------|:-----------|:----------|:------------------------------------------------------|
| 1- 5    | A5       | ---        | ---       | [FMOS_]                                               |
| 6- 21   | A16      | ---        | FMOS      | FMOS unique identifier (JHHMMSS.s+DDMMSS)             |
| 23- 31  | F9.5     | deg        | RAdeg     | Right Ascension in decimal degrees (J2000)            |
| 33- 39  | F7.5     | deg        | DEdeg     | Declination in decimal degrees (J2000)                |
| 41- 47  | F7.3     | ---        | z         | [0.7/2.5]?=-99 Best measurement of redshift           |
| 49      | I1       | ---        | q_z       | [0/4] Quality flag for z (z>=2: highly                |
| 51      | A1       | ---        | l_FHa     | Limit flag on FHa (2)                                 |
| 52- 58  | F7.3     | 10-17mW/m2 | FHa       | [0.3/23.3]?=-99 Observed H{alpha} flux (3)            |
| 60- 65  | F6.2     | ---        | SNHa      | [1.5/37.1]?=-99 S/N of observed H{alpha} flux         |
| 67- 73  | F7.2     | km/s       | FWHMHa    | [42/1099]?=-99 Velocity FWHM of                       |
| 75- 80  | F6.2     | km/s       | e_FWHMHa  | ?=-99 The 1{sigma} error in FWHMHa                    |
| 82      | A1       | ---        | l_FNII    | Limit flag on FNII (2)                                |
| 83- 89  | F7.3     | 10-17mW/m2 | FNII      | [0.2/24]?=-99 Observed [NII] (6584A) flux (3)         |
| 91- 96  | F6.2     | ---        | SNNII     | [1.5/18.1]?=-99 S/N of observed                       |
| 98-103  | F6.2     | ---        | ApCor1    | [1.1/5.6]?=-99 Aperture correction factor (5)         |
| 105     | A1       | ---        | l_FHb     | Limit flag on FHb (2)                                 |
| 106-112 | F7.3     | 10-17mW/m2 | FHb       | [0.3/19.8]?=-99 Observed H{beta} flux (3)             |
| 114-119 | F6.2     | ---        | SNHb      | [1.5/14]?=-99 S/N of observed H{beta} flux            |
| 121     | A1       | ---        | l_FOIII   | Limit flag on FOIII (2)                               |
| 122-128 | F7.3     | 10-17mW/m2 | FOIII     | [0.3/36]?=-99 Observed [OIII](5007A) flux (3)         |
| 130-135 | F6.2     | ---        | SNOIII    | [1.6/46]?=-99 S/N of observed                         |
| 137-142 | F6.2     | ---        | ApCor2    | [1.4/6.3]?=-99 Aperture correction factor (6)         |
| 144-150 | F7.3     | ---        | zCOS      | [0/3.4]?=-99 Redshift measurement from                |
| 152-156 | F5.1     | ---        | q_zCOS    | [0/22.5]?=-99 Quality flag for zCOS (7)               |
| 1       | and      | 4,         | otherwise | 0; as follows:                                        |
| 1       | =        | Presence   | of        | a single emission line with S/N between 1.5 and 3.    |
| 2       | =        | One        | emission  | line having S/N greater than 3 and less than 5.       |
| 3       | =        | One        | emission  | line having S/N greater than 5.                       |
| 4       | =        | One        | emission  | line having S/N greater than 5 (usually H{alpha}) and |
| 0       | indicate | a          | NULL      | detection.                                            |
| 0       | or       | higher     | (with     | 0 being undetected).                                  |

**Note**: Based on the S/N of the H{alpha} detection and corroborative
          information as described in Section 9. If detected then a value
          between 1 and 4, otherwise 0; as follows:
 1 = Presence of a single emission line with S/N between 1.5 and 3.
 2 = One emission line having S/N greater than 3 and less than 5.
 3 = One emission line having S/N greater than 5.
 4 = One emission line having S/N greater than 5 (usually H{alpha}) and
     a second line that both confirms the redshift and has S/N greater than 1.5.
Note (2): Upper limits (non-detections) on the fluxes are given at a level
           of 2{sigma} and described in Section 8.2.
Note (3): Not corrected for aperture loss. In units of 1e-17erg/s/cm^2^.
          A -99.0 indicate a NULL detection.
Note (4): Not deconvolved with spectral resolution.
Note (5): For H{alpha} and [NII](6584{AA}) fluxes to compensate for the effect
          of the aperture size and should be multiplied to the flux
          measurements.
Note (6): For H{beta} and [OIII](5007{AA}) fluxes to compensate for the effect
          of the aperture size and should be multiplied to the flux
          measurements.
Note (7): If observed a value of 0 or higher (with 0 being undetected).

</details>
