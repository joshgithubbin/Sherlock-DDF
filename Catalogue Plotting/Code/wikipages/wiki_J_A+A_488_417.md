**Authors:** Feruglio C., Fiore F., La Franca F., Sacchi N., Puccetti S., Comastri A.,, Berta S., Gruppioni C., Mathur S, Matute I., Mignoli M., Vignali C.,, Zamorani G., <Astron. Astrophys. 488, 417 (2008)>, =2008A&A...488..417F

## Summary: XMM-Newton survey of the ELAIS-S1 field. II. 

We present the optical identifications and a multi-band catalogue of a sample of 478 X-ray sources detected in the XMM-Newton and Chandra surveys of the central 0.6deg^2^ of the ELAIS-S1 field. The most likely optical/infrared counterpart of each X-ray source was identified using the chance coincidence probability in the R and IRAC 3.6 micron bands.This method was complemented by the precise positions obtained through Chandra observations. We were able to associate a counterpart to each X-ray source in the catalogue. Approximately 94% of them are detected in the R band, while the remaining are blank fields in the optical down to R~24.5, but have a near-infrared counterpart detected by IRAC within 6 arcsec from the XMM-Newton centroid. The multi-band catalogue, produced using the positions of the identified optical counterparts, contains photometry in ten photometric bands, from B to the MIPS 24 micron band. The spectroscopic follow-up allowed us to determine the redshift and classification for 237 sources (~50% of the sample) brighter than R=24. The spectroscopic redshifts were complemented by reliable photometric redshifts for 68 sources. We classified 47% of the sources with spectroscopic redshift as broad-line active galactic nuclei (BL AGNs) with z=0.1-3.5, while sources without broad-lines (NOT BL AGNs) are about 46% of the spectroscopic sample and are found up to z=2.6. The remaining fraction is represented by extended X-ray sources and stars. We spectroscopically identified 11 type 2 QSOs among the sources with X/O>8, with redshift between 0.9 and 2.6, high 2-10keV luminosity (logLx>=43.8erg/s) and hard X-ray colors suggesting large absorbing columns at the rest frame (logN_H_ up to 23.6cm^-2^). BL AGNs show on average blue optical-to-near-infrared colors, softer X-ray colors and X-ray-to-optical colors typical of optically selected AGNs. Conversely, narrow-line sources show redder optical colors, harder X-ray flux ratio and span a wider range of X-ray-to-optical colors. On average the Spectral Energy Distributions (SEDs) of high-luminosity BL AGNs resemble the power-law typical of unobscured AGNs. The SEDs of NOT BLAGNs are dominated by the galaxy emission in the optical/near-infrared, and show a rise in the mid-infrared which suggests the presence of an obscured active nucleus. We study the infrared-to-optical colors and near-infrared SEDs to infer the properties of the AGN host galaxies.

## Spectroscopic Redshift 
 
**z:** ?=-9.0 or -1.0 Spectroscopic redshift 
 

## Photometric Redshift 
 
**zpho:** ?=-1.0 Best fit Photometric redshift 
 

## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes   | Format   | Units     | Label          | Explanations                                                    |
|:--------|:---------|:----------|:---------------|:----------------------------------------------------------------|
| 1- 3    | I3       | ---       | XMMES1         | [1/479] XMM sequential number                                   |
| 5- 11   | F7.5     | deg       | RAdeg          | XMM Right ascension (J2000.0)                                   |
| 13- 21  | F9.5     | deg       | DEdeg          | XMM Declination (J2000.0)                                       |
| 23- 34  | E12.7    | mW/m2     | FX0.5-10       | Flux 0.5-10keV                                                  |
| 36- 40  | F5.2     | ---       | SN0.5-10       | S/N in 0.5-10keV band                                           |
| 42- 53  | E12.7    | mW/m2     | e_FX0.5-10     | ?=99.0 Error on Flux 0.5-10keV                                  |
| 55- 66  | E12.7    | mW/m2     | FX2-10         | Flux 2-10keV band                                               |
| 68- 72  | F5.2     | ---       | SN2-10         | S/N in 2-10keV band                                             |
| 74- 85  | E12.7    | mW/m2     | e_FX2-10       | ?=99.0 Error on Flux 2-10keV                                    |
| 87- 98  | E12.7    | mW/m2     | FX0.5-2        | Flux 0.5-2keV band                                              |
| 100-104 | F5.2     | ---       | SNX0.5-2       | S/N in 0.5-2keV band                                            |
| 106-117 | E12.7    | mW/m2     | e_FX0.5-2      | ?=99.0 Error on Flux 0.5-2keV                                   |
| 119-130 | E12.7    | mW/m2     | FX5-10         | Flux 5-10 keV band                                              |
| 132-135 | F4.2     | ---       | SNFX5-10       | S/N in 5-10keV band                                             |
| 137-148 | E12.7    | mW/m2     | e_FX5-10       | ?=99.0 Error on Flux 5-10keV                                    |
| 150-153 | I4       | ---       | Chandra        | ?=-999 Chandra ID                                               |
| 155-163 | F9.6     | deg       | RACdeg         | ?=-9.9999 Chandra Right ascension (J2000.0)                     |
| 165-173 | F9.5     | deg       | DECdeg         | ?=-99. Chandra Declination (J2000.0)                            |
| 175     | I1       | ---       | covCh          | [0/1] Flag, if area is covered by Chandra                       |
| 177-182 | I6       | ---       | ESIS           | ?=0 ID in ESIS catalog                                          |
| 184-195 | F12.9    | deg       | RAEdeg         | ?=-9.9999 Right ascension (J2000.0)                             |
| 199-211 | F13.9    | deg       | DEEdeg         | ?=-99. Declination (J2000.0) in ESIS catalog                    |
| 213     | A1       | ---       | l_BmagE        | Limit flag on BmagE                                             |
| 214-219 | F6.3     | mag       | BmagE          | ?=99.0 B band magnitude (Vega) from ESIS                        |
| 221-227 | F7.4     | mag       | e_BmagE        | ?=99.0 B mag error                                              |
| 229     | A1       | ---       | l_VmagE        | Limit flag on VmagE                                             |
| 230-235 | F6.3     | mag       | VmagE          | ?=99.0 V band magnitude (Vega) from                             |
| 237-243 | F7.4     | mag       | e_VmagE        | ?=99.0 V mag error                                              |
| 245     | A1       | ---       | l_RmagE        | Limit flag on RmagE                                             |
| 246-251 | F6.3     | mag       | RmagE          | ?=99.0 R band magnitude (Vega) from                             |
| 253-259 | F7.4     | mag       | e_RmagE        | ?=99.0 R mag error                                              |
| 261-270 | F10.7    | deg       | RAVdeg         | ?=99. VIMOS/VLT Right ascension (J2000.0)                       |
| 272-282 | F11.7    | deg       | DEVdeg         | ?=99. VIMOS/VLT Declination (J2000.0)                           |
| 284     | A1       | ---       | l_RmagBest     | Limit flag on RmagBest                                          |
| 285-289 | F5.2     | mag       | RmagBest       | ?=99. R band magnitude (Vega) from VIMOS                        |
| 291-295 | F5.2     | mag       | e_RmagBest     | ?=99.0 R mag error                                              |
| 297-303 | F7.4     | ---       | Rell           | ?=99.0 Ellipticity in R band                                    |
| 305-306 | I2       | ---       | Rflg           | ?=99 Sextractor flags in R band                                 |
| 308-314 | F7.2     | ---       | Rs/g           | ?=99.0 Star/galaxy separation in R band                         |
| 0       | for      | galaxy)   | 316-320        | F5.3  ---     ProbOpt   Chance coincidence probability (R band) |
| 322-326 | F5.2     | arcsec    | DXOpt          | ?=99.0 X-ray to optical position offset                         |
| 329-337 | F9.6     | deg       | RAOdeg         | ?=-99.0 J-band Right ascension (J2000.0)                        |
| 339-347 | F9.5     | deg       | DEOdeg         | ?=-99.0 J-band Declination (J2000.0)                            |
| 349-353 | F5.2     | mag       | JmagBest       | ?=99.0 J band magnitude (Vega)                                  |
| 355-359 | F5.2     | mag       | e_JmagBest     | ?=99.0 J mag error                                              |
| 361     | A1       | ---       | l_Kmag         | Limit flag on Kmag                                              |
| 362-366 | F5.2     | mag       | Kmag           | ?=99.0 K band magnitude (Vega) (mag_best)                       |
| 368-374 | F7.4     | mag       | e_Kmag         | ?=99.0 K mag error                                              |
| 376-384 | F9.4     | ---       | Kell           | ?=99.0 Ellipticity in K band                                    |
| 386-387 | I2       | ---       | Kflg           | ?=99 Sextractor flags in K band                                 |
| 389-393 | F5.2     | ---       | Ks/g           | ?=99.0 Star/galaxy separation in K band                         |
| 0       | for      | galaxy)   | 395-400        | I6    ---     IRAC      ?=0 Swire IRAC ID                       |
| 402-411 | F10.6    | deg       | RAIdeg         | ?=-99.0 IRAC Right ascension (J2000.0)                          |
| 413-421 | F9.5     | deg       | DEIdeg         | ?=-99.0 IRAC Declination (J2000.0)                              |
| 423-430 | F8.2     | uJy       | F3.6um         | ?=-999.0 IRAC 3.6um flux                                        |
| 432-436 | F5.2     | uJy       | e_F3.6um       | ?=99.0 IRAC 3.6um flux error                                    |
| 437-445 | F9.2     | uJy       | F4.5um         | ?=-999.0 IRAC 4.5um flux                                        |
| 447-451 | F5.2     | uJy       | e_F4.5um       | ?=99.0 IRAC 4.5um flux error                                    |
| 453-460 | F8.2     | uJy       | F5.8um         | ?=-999.0 IRAC 5.8um flux                                        |
| 462-466 | F5.2     | uJy       | e_F5.8um       | ?=99.0 IRAC 5.8um flux error                                    |
| 468-475 | F8.2     | uJy       | F8.0um         | ?=-999.0 IRAC 8.0um flux                                        |
| 478-482 | F5.2     | uJy       | e_F8.0um       | ?=99.0 IRAC 8.0um flux error                                    |
| 484-491 | F8.2     | uJy       | F24um          | ?=-999.0 MIPS 24um flux                                         |
| 494-498 | F5.2     | uJy       | e_F24um        | ?=99.0 MIPS 24um flux error                                     |
| 500-504 | F5.2     | arcsec    | DXIR           | ?=-9.0 X-ray to IRAC position offset                            |
| 506-511 | F6.3     | ---       | ProbIR         | ?=-9.0 Chance coincidence probability                           |
| 6       | micron)  | 513-515   | F3.1           | ---     Tel       Photometry from : 2.2=ESO/WFI  8.0=VIMOS/VLT  |
| 517-520 | I4       | ---       | SpID           | Spectrum ID (unexplained)                                       |
| 522-526 | I5       | ---       | SpCode         | Spectrum code (unexplained)                                     |
| 528-534 | F7.4     | ---       | z              | ?=-9.0 or -1.0 Spectroscopic redshift                           |
| 536-539 | F4.1     | ---       | q_z            | ?=-9.0 Redshift quality flag (1)                                |
| 541-542 | I2       | ---       | Class          | ?=-9.0 Classification (2)                                       |
| 544-546 | I3       | ---       | Inst           | Instrument (3)                                                  |
| 548-549 | I2       | ---       | SED            | ?=0 SED classification (4)                                      |
| 551-557 | F7.4     | ---       | zpho           | ?=-1.0 Best fit Photometric redshift                            |
| 559-575 | E17.8    | ---       | chi2           | ?=0.0 Chi squared for Photometric redshift fit                  |
| 2       | =        | secure    | 1              | = only 1 emission line                                          |
| 1       | =        | tentative | Note           | (2): Classification as follows:                                 |
| 1       | =        | type      | 1              | AGN                                                             |
| 2       | =        | emission  | line           | galaxy                                                          |
| 3       | =        | galaxy    | without        | emission lines                                                  |
| 4       | =        | star      | 5              | = type 2 AGN                                                    |
| 6       | =        | galaxies  | associated     | to extended sources (clusters)                                  |
| 15      | =        | spectra   | of             | bright sources from La Franca et al. (2004,                     |
| 73      | =        | VIMOS/VLT | 75             | = VIMOS/VLT                                                     |
| 77      | =        | FORS2/VLT | 78             | = FORS2/VLT                                                     |
| 360     | =        | EFOSC/VLT | Note           | (4): SED classification as follows:                             |
| 0       | =        | no        | classification | 2 = early-type-like                                             |
| 3       | =        | infrared  | excess         | 4 = infrared excess                                             |
| 5       | =        | dominated | by             | emission features                                               |
| 11      | =        | optically | blue           | power-law                                                       |
| 12      | =        | optically | red            | power-law                                                       |

**Note**: Spectroscopic redshift quality flag as follows:
      2 = secure
      1 = only 1 emission line
     <1 = tentative
Note (2): Classification as follows:
      1 = type 1 AGN
      2 = emission line galaxy
      3 = galaxy without emission lines
      4 = star
      5 = type 2 AGN
      6 = galaxies associated to extended sources (clusters)
Note (3): Instrument code as follows:
     15 = spectra of bright sources from La Franca et al. (2004,
          Cat. <J/AJ/127/3075>
     73 = VIMOS/VLT
     75 = VIMOS/VLT
     77 = FORS2/VLT
     78 = FORS2/VLT
    360 = EFOSC/VLT
Note (4): SED classification as follows:
      0 = no classification
      2 = early-type-like
      3 = infrared excess
      4 = infrared excess
      5 = dominated by emission features
     11 = optically blue power-law
     12 = optically red power-law

</details>
