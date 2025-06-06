**Authors:** Ashby M.L.N., Willner S.P., Fazio G.G., Dunlop J.S., Egami E., Faber S.M.,, Ferguson H.C., Grogin N.A., Hora J.L., Huang J.-S., Koekemoer A.M.,, Labbe I., Wang Z., <Astrophys. J. Suppl. Ser., 218, 33 (2015)>, =2015ApJS..218...33A

## Summary: Spitzer-CANDELS catalog within 5 deep fields 

The Spitzer-Cosmic Assembly Near-infrared Deep Extragalactic Legacy Survey (S-CANDELS; PI G.Fazio) is a Cycle 8 Exploration Program designed to detect galaxies at very high redshifts (z>5). To mitigate the effects of cosmic variance and also to take advantage of deep coextensive coverage in multiple bands by the Hubble Space Telescope (HST) Multi-cycle Treasury Program CANDELS, S-CANDELS was carried out within five widely separated extragalactic fields: the UKIDSS Ultra-deep Survey, the Extended Chandra Deep Field South, COSMOS, the HST Deep Field North, and the Extended Groth Strip. S-CANDELS builds upon the existing coverage of these fields from the Spitzer Extended Deep Survey (SEDS), a Cycle 6 Exploration Program, by increasing the integration time from SEDS' 12hr to a total of 50hr but within a smaller area, 0.16deg^2^. The additional depth significantly increases the survey completeness at faint magnitudes. This paper describes the S-CANDELS survey design, processing, and publicly available data products. We present Infrared Array Camera (IRAC) dual-band 3.6+4.5{mu}m catalogs reaching to a depth of 26.5 AB mag. Deep IRAC counts for the roughly 135000 galaxies detected by S-CANDELS are consistent with models based on known galaxy populations. The increase in depth beyond earlier Spitzer/IRAC surveys does not reveal a significant additional contribution from discrete sources to the diffuse Cosmic Infrared Background (CIB). Thus it remains true that only roughly half of the estimated CIB flux from COBE/DIRBE is resolved.
## Coverage
## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format   | Units         | Label    | Explanations                             |
|:--------|:---------|:--------------|:---------|:-----------------------------------------|
| 1- 6    | A6       | ---           | Field    | Field identifier                         |
| 8- 9    | I2       | h             | RAh      | Hour of right ascension (J2000)          |
| 11- 12  | I2       | min           | RAm      | Minute of right ascension (J2000)        |
| 14- 15  | I2       | s             | RAs      | Second of right ascension (J2000)        |
| 17      | A1       | ---           | DE-      | Sign of declination (J2000)              |
| 18- 19  | I2       | deg           | DEd      | Degree of declination (J2000)            |
| 21- 22  | I2       | arcmin        | DEm      | Arcminute of declination (J2000)         |
| 24- 25  | I2       | arcsec        | DEs      | Arcsecond of declination (J2000)         |
| 27- 31  | F5.3     | deg2          | A3.6     | [0.01/0.05] Field area observed in 3.6um |
| 33- 37  | F5.3     | deg2          | A4.5     | [0.02/0.06] Field area observed in 4.5um |
| 39- 43  | I5       | ---           | PID      | [8/80218] Spitzer program ID number      |
| 45- 55  | A11      | "YYYY/MMM/DD" | Date1    | First date of observation                |
| 57- 67  | A11      | "YYYY/MMM/DD" | Date2    | ? Second date of observation             |
| 69- 72  | I4       | ---           | BCD3.6   | [114/6840] 3.6um BCD used                |
| 74- 77  | I4       | ---           | BCD4.5   | [24/6840] 4.5um BCD used                 |
| 79      | A1       | ---           | n_BCD4.5 | [bc] Basic Calibrated Data (BCD) frames: |
| 81- 88  | A8       | ---           | Version  | Pipeline version                         |
</details>

<details>
<summary>table[789].dat</summary>

| Bytes   | Format   | Units     | Label      | Explanations                                                    |
|:--------|:---------|:----------|:-----------|:----------------------------------------------------------------|
| 1- 6    | A6       | ---       | Field      | Field identifier                                                |
| 8- 15   | A8       | ---       | ---        | [SCANDLES]                                                      |
| 17- 35  | A19      | ---       | SCANDELS   | S-CANDLES project identifier                                    |
| 37- 45  | F9.5     | deg       | RAdeg      | Right Ascension in decimal degrees (J2000)                      |
| 47- 55  | F9.5     | deg       | DEdeg      | Declination in decimal degrees (J2000)                          |
| 57- 61  | F5.2     | mag       | [3.6]psf   | [11.1/27.4] Spitzer/IRAC 3.6um PSF-fitted AB                    |
| 63- 68  | F6.2     | mag       | [3.6]2.4   | ?=-99 Spitzer/IRAC 3.6{mu}m 2.4" diameter                       |
| 70- 75  | F6.2     | mag       | [3.6]3.6   | ?=-99 Spitzer/IRAC 3.6{mu}m 3.6" diameter                       |
| 77- 82  | F6.2     | mag       | [3.6]4.8   | ?=-99 Spitzer/IRAC 3.6{mu}m 4.8" diameter                       |
| 84- 89  | F6.2     | mag       | [3.6]6.0   | ?=-99 Spitzer/IRAC 3.6{mu}m 6.0" diameter                       |
| 91- 96  | F6.2     | mag       | [3.6]7.2   | ?=-99 Spitzer/IRAC 3.6{mu}m 7.2" diameter                       |
| 98-103  | F6.2     | mag       | [3.6]12    | ?=-99 Spitzer/IRAC 3.6{mu}m 12.0" diameter                      |
| 105-108 | F4.2     | mag       | e_[3.6]2.4 | [0.03/0.4] Error in [3.6]2.4                                    |
| 110-113 | F4.2     | mag       | B3.6       | [0/0.4] Photometric bias already applied to                     |
| 6       | aperture | magnitude | 115-118    | I4    hs      C3.6      [0/4580] Depth of 3.6{mu}m coverage (1) |
| 120-124 | F5.2     | mag       | [4.5]psf   | [11.6/27.1] Spitzer/IRAC 4.5um PSF-fitted AB                    |
| 126-131 | F6.2     | mag       | [4.5]2.4   | ?=-99 Spitzer/IRAC 4.5{mu}m 2.4" diameter                       |
| 133-138 | F6.2     | mag       | [4.5]3.6   | ?=-99 Spitzer/IRAC 4.5{mu}m 3.6" diameter                       |
| 140-145 | F6.2     | mag       | [4.5]4.8   | ?=-99 Spitzer/IRAC 4.5{mu}m 4.8" diameter                       |
| 147-152 | F6.2     | mag       | [4.5]6.0   | ?=-99 Spitzer/IRAC 4.5{mu}m 6.0" diameter                       |
| 154-159 | F6.2     | mag       | [4.5]7.2   | ?=-99 Spitzer/IRAC 4.5{mu}m 7.2" diameter                       |
| 161-166 | F6.2     | mag       | [4.5]12    | ?=-99 Spitzer/IRAC 4.5{mu}m 12.0" diameter                      |
| 168-171 | F4.2     | mag       | e_[4.5]2.4 | [0.03/0.4] Error in [4.5]2.4                                    |
| 173-176 | F4.2     | mag       | B4.5       | [0/0.4] Photometric bias already applied to                     |
| 5       | aperture | magnitude | 178-181    | I4    hs      C4.5      [0/4248] Depth of 4.5{mu}m coverage (2) |

**Note**: Version 2, generated May 22nd, 2015.
Note (2): In units of 100s exposures at the position of this source.

</details>
