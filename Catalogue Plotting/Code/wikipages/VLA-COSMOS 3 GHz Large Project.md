**Authors:** Novak M., Bondi M., Ciliegi P., Mooley K.P., Schinnerer E.,, Zamorani G., Navarrete F., Bourke S., Karim A., Vardoulaki E., Leslie S.,, Delhaize J., Carilli C.L., Myers S.T., Baran N., Delvecchio I.,, Miettinen O., Banfield J., Balokovic M., Bertoldi F., Capak P., Frail D.A.,, Hallinan G., Hao H., Herrera Ruiz N., Horesh A., Ilbert O., Intema H.,, Jelic V., Klockner H-R., Krpan J., Kulkarni S.R., McCracken H., Laigle C.,, Middleberg E., Murphy E., Sargent M., Scoville N.Z., Sheth K., <Astron. Astrophys. 602, A1 (2017)>, =2017A&A...602A...1S (SIMBAD/NED BibCode)

## Summary: VLA-COSMOS 3 GHz Large Project 

We present the VLA-COSMOS 3GHz Large Project based on 384 hours of observations with the Karl G. Jansky Very Large Array (VLA) at 3GHz (10cm) toward the two square degree Cosmic Evolution Survey (COSMOS) field. The final mosaic reaches a median rms of 2.3 uJy/beam over the two square degrees at an angular resolution of 0.75". To fully account for the spectral shape and resolution variations across the broad (2GHz) band, we image all data with a multiscale, multifrequency synthesis algorithm. We present a catalog of 10,830 radio sources down to 5{sigma}, out of which 67 are combined from multiple components. Comparing the positions of our 3GHz sources with those from the Very Long Baseline Array (VLBA)-COSMOS survey, we estimate that the astrometry is accurate to 0.01" at the bright end (signal-to-noise ratio, S/N_3GHz_>20). Survival analysis on our data combined with the VLA-COSMOS 1.4GHz Joint Project catalog yields an expected median radio spectral index of {alpha}=-0.7. We compute completeness corrections via Monte Carlo simulations to derive the corrected 3GHz source counts. Our counts are in agreement with previously derived 3GHz counts based on single-pointing (0.087 square degrees) VLA data. In summary, the VLA-COSMOS 3GHz Large Project simultaneously provides the largest and deepest radio continuum survey at high (0.75") angular resolution to date, bridging the gap between last-generation and next-generation surveys.

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format   | Units    | Label      | Explanations                              |
|:--------|:---------|:---------|:-----------|:------------------------------------------|
| 2- 6    | I5       | ---      | ID         | Numerical ID of the source (1)            |
| 8- 17   | A10      | ---      | ---        | [COSMOSVLA3]                              |
| 19- 37  | A19      | ---      | COSMOSVLA3 | COSMOSVLA3 name (JHHMMSS.ss+DDMMSS.s)     |
| 39- 48  | F10.6    | deg      | RAdeg      | Right ascension (J2000)                   |
| 50- 54  | F5.3     | arcsec   | e_RAdeg    | ?=9.999 Positional error in RAdeg (4)     |
| 56- 63  | F8.6     | deg      | DEdeg      | Declination (J2000)                       |
| 65- 69  | F5.3     | arcsec   | e_DEdeg    | ?=9.999 Positional error in DEdeg (4)     |
| 71- 77  | F7.1     | uJy      | Flux       | Total integrated flux density at 3GHz (2) |
| 79- 83  | F5.1     | uJy      | e_Flux     | ?=-99.0 Error on the total integrated     |
| 85- 89  | F5.2     | uJy/beam | rms        | Local rms noise at the source position    |
| 91- 97  | F7.2     | ---      | SNR        | ?=-99.0 Signal-to-noise ratio (S/N) (5)   |
| 99-103  | I5       | ---      | Npix       | Number of pixels used for flux            |
| 105     | I1       | ---      | Res        | [0/1] Resolved flag (1 for yes)           |
| 107     | I1       | ---      | Multi      | [0/1] Multi-component flag (1 for yes)    |
| 10966   | although | there    | are        | 10830 sources. Some IDs were              |

**Note**: Maximum ID is 10966 although there are 10830 sources. Some IDs were
   removed by joining them into multi-component sources.
Note (2): Peak surface brightness of sources [uJy/beam] is not reported,
   but can be obtained by multiplying SNR with rms.
Note (3): High NPIX usually indicates extended or very bright sources.
Note (4): Reported positional errors on resolved and extended sources should
  be considered lower limits.
Note (5): Multicomponent sources have errors and S/N column values
  set to -99.0.

</details>
