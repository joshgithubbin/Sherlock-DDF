## Summary

In this paper, we present photometric redshifts for 2.7 million galaxies in the XMM-LSS and COSMOS fields, both with rich optical and near-infrared data from VISTA and HyperSuprimeCam. Both template fitting (using galaxy and active galactic nuclei templates within LePhare) and machine learning (using gpz) methods are run on the aperture photometry of sources selected in the Ks-band. The resulting predictions are then combined using a Hierarchical Bayesian model, to produce consensus photometric redshift point estimates and probability distribution functions that outperform each method individually. Our point estimates have a root mean square error of ~0.08-0.09, and an outlier fraction of ~3-4 percent when compared to spectroscopic redshifts. We also compare our results to the COSMOS2020 photometric redshifts, which contain fewer sources, but had access to a larger number of bands and greater wavelength coverage, finding that comparable photo-z quality can be achieved (for bright and intermediate luminosity sources where a direct comparison can be made). Our resulting redshifts represent the most accurate set of photometric redshifts (for a catalogue this large) for these deep multisquare degree multiwavelength fields to date.

## Catalogue Schema

<details>
<summary>cosphotz.dat catalogue schema</summary>

| Bytes   | Format   | Units    | Label       | Explanations                               |
|:--------|:---------|:---------|:------------|:-------------------------------------------|
| 1- 18   | F18.14   | deg      | RAdeg       | Celestial right ascension (J2000) (RA2000) |
| 20- 37  | F18.16   | deg      | DEdeg       | Celestial declination (J2000) (DEC2000)    |
| 39- 48  | F10.8    | ---      | zphMLbest   | Machine learning (GPz) based photometric   |
| 50- 57  | F8.6     | ---      | e_zphMLbest | Uncertainty on zphMLbest (photo_z_ML_err)  |
| 59- 78  | F20.18   | ---      | zphTemp     | Template fitting (LePhare) based           |
| 80- 98  | F19.17   | ---      | e_zphTemp   | Uncertainty on zphTemp                     |
| 100-120 | F21.19   | ---      | zphHBbest   | Hybrid (Hierarchical Bayesian combination) |
| 122-141 | E20.18   | ---      | e_zphHBbest | ? Uncertainty on zphHBbest                 |
| 143     | I1       | ---      | Flag        | [0/1] Flag identifying quality of          |
| 145-167 | E23.17   | mW/m2/Hz | FCFHT-u     | ?=-99 u-band flux (from CFHT data)         |
| 169-191 | E23.17   | mW/m2/Hz | FHSC-g      | ?=-99 g-band flux (from HSC data)          |
| 193-215 | E23.17   | mW/m2/Hz | FHSC-r      | ?=-99 r-band flux (from HSC data)          |
| 217-239 | E23.17   | mW/m2/Hz | FHSC-i      | ?=-99 i-band flux (from HSC data)          |
| 241-263 | E23.17   | mW/m2/Hz | FHSC-z      | ?=-99 z-band flux (from HSC data)          |
| 265-287 | E23.17   | mW/m2/Hz | FHSC-y      | ?=-99 y-band flux (from HSC data)          |
| 289-311 | E23.17   | mW/m2/Hz | FVISTA-Y    | ?=-99 Y-band flux (from VISTA data)        |
| 313-335 | E23.17   | mW/m2/Hz | FVISTA-J    | ?=-99 J-band flux (from VISTA data)        |
| 337-359 | E23.17   | mW/m2/Hz | FVISTA-H    | ?=-99 H-band flux (from VISTA data)        |
| 361-383 | E23.17   | mW/m2/Hz | FVISTA-Ks   | ?=-99 Ks-band flux (from VISTA data)       |
| 385-407 | E23.17   | mW/m2/Hz | e_FCFHT-u   | []?=-99 Uncertainty on u-band flux         |
| 409-431 | E23.17   | mW/m2/Hz | e_FHSC-g    | ?=-99 Uncertainty on g-band flux           |
| 433-455 | E23.17   | mW/m2/Hz | e_FHSC-r    | ?=-99 Uncertainty on r-band flux           |
| 457-479 | E23.17   | mW/m2/Hz | e_FHSC-i    | ?=-99 Uncertainty on i-band flux           |
| 481-503 | E23.17   | mW/m2/Hz | e_FHSC-z    | ?=-99 Uncertainty on z-band flux           |
| 505-527 | E23.17   | mW/m2/Hz | e_FHSC-y    | ?=-99 Uncertainty on y-band flux           |
| 529-550 | E22.17   | mW/m2/Hz | e_FVISTA-Y  | Uncertainty on Y-band flux                 |
| 552-573 | E22.17   | mW/m2/Hz | e_FVISTA-J  | Uncertainty on J-band flux                 |
| 575-596 | E22.17   | mW/m2/Hz | e_FVISTA-H  | Uncertainty on H-band flux                 |
| 598-619 | E22.17   | mW/m2/Hz | e_FVISTA-Ks | ? Uncertainty on Ks-band flux              |
</details>

<details>
<summary>xmmphotz.dat catalogue schema</summary>

| Bytes   | Format   | Units    | Label       | Explanations                               |
|:--------|:---------|:---------|:------------|:-------------------------------------------|
| 1- 18   | F18.15   | deg      | RAdeg       | Celestial right ascension (J2000) (RA2000) |
| 20- 38  | F19.16   | deg      | DEdeg       | Celestial declination (J2000) (DEC2000)    |
| 40- 49  | E10.5    | ---      | zphMLbest   | Machine learning (GPz) based photometric   |
| 51- 58  | F8.6     | ---      | e_zphMLbest | Uncertainty on zphMLbest (photo_z_ML_e)    |
| 60- 80  | F21.19   | ---      | zphTemp     | Template fitting (LePhare) based           |
| 82-100  | F19.17   | ---      | e_zphTemp   | Uncertainty on zphTemp (photo_z_TEMP)      |
| 102-122 | F21.19   | ---      | zphHBbest   | Hybrid (Hierarchical Bayesian combination) |
| 124-145 | F22.18   | ---      | e_zphHBbest | ? Uncertainty on zphHBbest (photo_z_HB_e)  |
| 147     | I1       | ---      | Flag        | [0/1] Flag identifying quality of photo-z  |
| 149-172 | E24.1    | mW/m2/Hz | FCFHT-u     | ?=-99 u-band flux (from CFHT data)         |
| 174-197 | E24.17   | mW/m2/Hz | FHSC-g      | ?=-99 g-band flux (from HSC data)          |
| 199-222 | E24.17   | mW/m2/Hz | FHSC-r      | ?=-99 r-band flux (from HSC data)          |
| 224-247 | E24.17   | mW/m2/Hz | FHSC-i      | ?=-99 i-band flux (from HSC data)          |
| 249-272 | E24.17   | mW/m2/Hz | FHSC-z      | ?=-99 z-band flux (from HSC data)          |
| 274-297 | E24.17   | mW/m2/Hz | FHSC-y      | ?=-99 y-band flux (from HSC data)          |
| 299-322 | E24.17   | mW/m2/Hz | FVISTA-Y    | ?=-99 Y-band flux (from VISTA data)        |
| 324-347 | E24.17   | mW/m2/Hz | FVISTA-J    | ?=-99 J-band flux (from VISTA data)        |
| 349-372 | E24.17   | mW/m2/Hz | FVISTA-H    | ?=-99 H-band flux (from VISTA data)        |
| 374-397 | E24.17   | mW/m2/Hz | FVISTA-Ks   | ?=-99 Ks-band flux (from VISTA data)       |
| 399-421 | E23.17   | mW/m2/Hz | e_FCFHT-u   | ?=-99 Uncertainty on u-band flux           |
| 423-445 | E23.17   | mW/m2/Hz | e_FHSC-g    | ?=-99 Uncertainty on g-band flux           |
| 447-469 | E23.17   | mW/m2/Hz | e_FHSC-r    | ?=-99 Uncertainty on r-band flux           |
| 471-493 | E23.17   | mW/m2/Hz | e_FHSC-i    | ?=-99 Uncertainty on i-band flux           |
| 495-517 | E23.17   | mW/m2/Hz | e_FHSC-z    | ?=-99 Uncertainty on z-band flux           |
| 519-541 | E23.17   | mW/m2/Hz | e_FHSC-y    | ?=-99 Uncertainty on y-band flux           |
| 543-564 | E22.17   | mW/m2/Hz | e_FVISTA-Y  | ?=-99 Uncertainty on Y-band flux           |
| 566-587 | E22.17   | mW/m2/Hz | e_FVISTA-J  | ?=-99 Uncertainty on J-band flux           |
| 589-610 | E22.17   | mW/m2/Hz | e_FVISTA-H  | ?=-99 Uncertainty on H-band flux           |
| 612-633 | E22.17   | mW/m2/Hz | e_FVISTA-Ks | ?=-99 Uncertainty on Ks-band flux          |
</details>
