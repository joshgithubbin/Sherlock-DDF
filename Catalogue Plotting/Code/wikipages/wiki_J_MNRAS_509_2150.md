## Summary

MIGHTEE is a galaxy evolution survey using simultaneous radio continuum, spectropolarimetry, and spectral line observations from the South African MeerKAT telescope. When complete, the survey will image ~20 deg2 over the COSMOS, E-CDFS, ELAIS-S1, and XMM-Newton Large Scale Structure field (XMM-LSS) extragalactic deep fields with a central frequency of 1284 MHz. These were selected based on the extensive multiwavelength data sets from numerous existing and forthcoming observational campaigns. Here, we describe and validate the data processing strategy for the total intensity continuum aspect of MIGHTEE, using a single deep pointing in COSMOS (1.6 deg^2^) and a three-pointing mosaic in XMM-LSS (3.5 deg^2^). The processing includes the correction of direction-dependent effects, and results in thermal noise levels below 2 {mu}Jy.beam^-1^ in both fields, limited in the central regions by classical confusion at ~8 arcsec angular resolution, and meeting the survey specifications. We also produce images at ~5 arcsec resolution that are ~3 times shallower. The resulting image products form the basis of the Early Science continuum data release for MIGHTEE. From these images we extract catalogues containing 9896 and 20274 radio components in COSMOS and XMM-LSS, respectively. We also process a close-packed mosaic of 14 additional pointings in COSMOS and use these in conjunction with the Early Science pointing to investigate methods for primary beam correction of broad-band radio images, an analysis that is of relevance to all full-band MeerKAT continuum observations, and wide-field interferometric imaging in general. A public release of the MIGHTEE Early Science continuum data products accompanies this article.

## Catalogue Schema

<details>
<summary>cosmosl1.dat catalogue schema</summary>

| Bytes   | Format   | Units    | Label      | Explanations                               |
|:--------|:---------|:---------|:-----------|:-------------------------------------------|
| 1- 19   | A19      | ---      | ID         | Radio component identifier name in form    |
| 21- 29  | F9.5     | deg      | RAdeg      | Right Ascension (RA) (J2000) (G1)          |
| 31- 37  | F7.5     | deg      | e_RAdeg    | Mean 1{sigma} positional uncertainty of    |
| 39- 45  | F7.5     | deg      | DEdeg      | Declination (DEC) (J2000) (G1)             |
| 47- 53  | F7.5     | deg      | e_DEdeg    | Mean 1{sigma} positional uncertainty of    |
| 55- 63  | F9.7     | Jy       | Snu        | Integrated flux density at an given        |
| 65- 73  | F9.7     | Jy       | e_Snu      | Mean 1{sigma} uncertainty of S_{nu}_       |
| 75- 83  | F9.7     | Jy/beam  | Speak      | The peak brightness at {nu}_eff_ (S_PEAK)  |
| 85- 93  | F9.7     | Jy/beam  | e_Speak    | Mean 1{sigma} uncertainty of S_peak_       |
| 95-104  | I10      | Hz       | nueff      | Observational effective frequency          |
| 106-114 | F9.7     | Jy       | S1.4       | Integrated flux density corrected          |
| 4       | GHz      | assuming | {nu}_eff_  | values                                     |
| 116-124 | F9.7     | Jy       | e_S1.4     | Mean 1{sigma} uncertainty of S1.4          |
| 126-134 | F9.7     | Jy/beam  | Speak1.4   | The peak brightness corrected to 1.4 GHz   |
| 136-144 | F9.7     | Jy/beam  | e_Speak1.4 | Mean 1{sigma} uncertainty of Speak1.4      |
| 146-152 | F7.5     | deg      | MajAxis    | The major axis of the 2D Gaussian fitted   |
| 154-160 | F7.5     | deg      | e_MajAxis  | Mean 1{sigma} uncertainty of MajAxis       |
| 162-168 | F7.5     | deg      | MinAxis    | The minor axis of the 2D Gaussian fitted   |
| 170-176 | F7.5     | deg      | e_MinAxis  | Mean 1{sigma} uncertainty of MinAxis       |
| 178-182 | F5.1     | deg      | PA         | The position angle measured east of north  |
| 184-188 | F5.1     | deg      | e_PA       | Mean 1{sigma} uncertainty of PA (E_IM_PA)  |
| 190-196 | F7.5     | deg      | ThetaM     | The major axis of the deconvolved source   |
| 198-206 | F9.5     | deg      | e_ThetaM   | Mean 1{sigma} uncertainty of {Theta}_M_    |
| 208-214 | F7.5     | deg      | Thetam     | The minor axis of the deconvolved source   |
| 216-224 | F9.5     | deg      | e_Thetam   | Mean 1{sigma} uncertainty of {Theta}_m_    |
| 226     | I1       | ---      | Res        | Resolved flag (equal to 1) if it satisfies |
| 228-236 | F9.7     | Jy/beam  | RMSnoise   | Average background rms noise around the    |
| 238-241 | I4       | ---      | IDgauss    | A unique identifier for the Gaussian       |
| 243-246 | I4       | ---      | IDsrc      | A unique identifier for the source from    |
| 248-251 | I4       | ---      | IDisl      | A unique identifier for the island from    |
</details>

<details>
<summary>xmmlssl1.dat catalogue schema</summary>

| Bytes   | Format   | Units    | Label      | Explanations                               |
|:--------|:---------|:---------|:-----------|:-------------------------------------------|
| 1- 19   | A19      | ---      | ID         | Radio component identifier name in form    |
| 21- 28  | F8.5     | deg      | RAdeg      | Right Ascension (RA) (J2000) (G1)          |
| 30- 36  | F7.5     | deg      | e_RAdeg    | Mean 1{sigma} positional uncertainty of    |
| 38- 45  | F8.5     | deg      | DEdeg      | Declination (DEC) (J2000) (G1)             |
| 47- 53  | F7.5     | deg      | e_DEdeg    | Mean 1{sigma} positional uncertainty of    |
| 55- 63  | F9.7     | Jy       | Snu        | Integrated flux density at an given        |
| 65- 73  | F9.7     | Jy       | e_Snu      | Mean 1{sigma} uncertainty of S_{nu}_       |
| 75- 83  | F9.7     | Jy/beam  | Speak      | The peak brightness at {nu}_eff_ (S_PEAK)  |
| 85- 93  | F9.7     | Jy/beam  | e_Speak    | Mean 1{sigma} uncertainty of S_peak_       |
| 95-104  | I10      | Hz       | nueff      | Observational effective frequency          |
| 106-114 | F9.7     | Jy       | S1.4       | Integrated flux density corrected          |
| 4       | GHz      | assuming | {nu}_eff_  | values                                     |
| 116-124 | F9.7     | Jy       | e_S1.4     | Mean 1{sigma} uncertainty of S1.4          |
| 126-134 | F9.7     | Jy/beam  | Speak1.4   | The peak brightness corrected to 1.4 GHz   |
| 136-144 | F9.7     | Jy/beam  | e_Speak1.4 | Mean 1{sigma} uncertainty of Speak1.4      |
| 146-152 | F7.5     | deg      | MajAxis    | The major axis of the 2D Gaussian fitted   |
| 154-160 | F7.5     | deg      | e_MajAxis  | Mean 1{sigma} uncertainty of MajAxis       |
| 162-168 | F7.5     | deg      | MinAxis    | The minor axis of the 2D Gaussian fitted   |
| 170-176 | F7.5     | deg      | e_MinAxis  | Mean 1{sigma} uncertainty of MinAxis       |
| 178-182 | F5.1     | deg      | PA         | The position angle measured east of north  |
| 184-188 | F5.1     | deg      | e_PA       | Mean 1{sigma} uncertainty of PA (E_IM_PA)  |
| 190-196 | F7.5     | deg      | ThetaM     | The major axis of the deconvolved source   |
| 198-204 | F7.5     | deg      | e_ThetaM   | Mean 1{sigma} uncertainty of {Theta}_M_    |
| 206-212 | F7.5     | deg      | Thetam     | The minor axis of the deconvolved source   |
| 214-220 | F7.5     | deg      | e_Thetam   | Mean 1{sigma} uncertainty of {Theta}_m_    |
| 222     | I1       | ---      | Res        | Resolved flag (equal to 1) if it satisfies |
| 224-232 | F9.7     | Jy/beam  | RMSnoise   | Average background rms noise around the    |
| 234-238 | I5       | ---      | IDgauss    | A unique identifier for the Gaussian       |
| 240-244 | I5       | ---      | IDsrc      | A unique identifier for the source from    |
| 246-250 | I5       | ---      | IDisl      | A unique identifier for the island from    |
</details>
