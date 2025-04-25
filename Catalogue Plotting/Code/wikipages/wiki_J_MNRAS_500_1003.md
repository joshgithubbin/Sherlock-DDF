## Summary

We first present a catalogue of photometric redshifts for 14.68 million galaxies derived from the 7-band photometric data of Hyper Suprime-Cam Subaru Strategic Program and the Wide-field Infrared Survey Explorer using the nearest-neighbour algorithm. The redshift uncertainty is about 0.024 for galaxies of z=<0.7, and steadily increases with redshift to about 0.11 at z~2. From such a large data set, we identify 21661 clusters of galaxies, among which 5537 clusters have redshifts z>1 and 642 clusters have z>1.5, significantly enlarging the high redshift sample of galaxy clusters. Cluster richness and mass are estimated, and these clusters have an equivalent mass of M_500_>=0.7x10^14^M_{sun}_. We find that the stellar mass of the brightest cluster galaxies (BCGs) in each richness bin does not significantly evolve with redshift. The fraction of star-forming BCGs increases with redshift, but does not depend on cluster mass.

## Catalogue Schema

<details>
<summary>table1.dat catalogue schema</summary>

| Bytes   | Format   | Units     | Label                | Explanations                                   |
|:--------|:---------|:----------|:---------------------|:-----------------------------------------------|
| 1- 5    | I5       | ---       | IDcl                 | [1/21661] Internal cluster identifier          |
| 7- 25   | A19      | ---       | Name                 | Cluster name (WH JHHMMSS.s+DDMMSS)             |
| 27- 35  | F9.5     | deg       | RAdeg                | Right ascension (J2000) of the BCG (1)         |
| 37- 44  | F8.5     | deg       | DEdeg                | Declination (J2000) of the BCG (1)             |
| 46- 51  | F6.4     | ---       | z                    | Redshift of the cluster                        |
| 53- 58  | F6.3     | mag       | imag                 | i-band magnitude of the BCG (AB system)        |
| 60- 65  | F6.3     | mag       | W1mag                | W1-band magnitude of the BCG (AB system)       |
| 67- 71  | F5.2     | ---       | S/N                  | Signal to noise ratio                          |
| 73- 77  | F5.3     | Mpc       | r500                 | Cluster radius                                 |
| 79- 84  | F6.2     | ---       | lambda500            | Cluster richness                               |
| 86- 90  | F5.2     | 10+14Msun | M500                 | Dervied cluster mass                           |
| 92- 94  | I3       | ---       | Ngal                 | Number of member galaxy candidates             |
| 96- 103 | A8       | ---       | Ref                  | Reference for previously known clusters        |
| 11      | =        | Wen       | &                    | Han 2011ApJ...734...68W, Cat. J/ApJ/734/68     |
| 14      | =        | Oguri     | 2014MNRAS.444..147O, | Cat. J/MNRAS/444/147                           |
| 18      | =        | Oguri     | et                   | al. 2018PASJ...70S..20O, Cat. J/PASJ/70/S20    |
| 18      | =        | Wen       | &                    | Han 2018MNRAS.481.4158W, Cat. J/MNRAS/481/4158 |

**Note**: Properties of the brightest cluster galaxy
Note (2): Reference as follows:
  WH11     = Wen & Han 2011ApJ...734...68W, Cat. J/ApJ/734/68
  WHL      = Wen et al. 2012ApJS..199...34W, Cat. J/ApJS/199/34;
             Wen & Han 2015ApJ...807..178W, Cat. J/ApJ/807/178)
  CAMIRA14 = Oguri 2014MNRAS.444..147O, Cat. J/MNRAS/444/147
  CAMIRA18 = Oguri et al. 2018PASJ...70S..20O, Cat. J/PASJ/70/S20
  WH18     = Wen & Han 2018MNRAS.481.4158W, Cat. J/MNRAS/481/4158
  XXL      = Adami et al. 2018A&A...620A...5A
  ACT      = Hilton et al. 2018ApJS..235...20H
  MaDCoWS  = Gonzalez et al. 2019ApJS..240...33G, Cat. J/ApJS/240/33

</details>

<details>
<summary>table2.dat catalogue schema</summary>

| Bytes    | Format   | Units   | Label   | Explanations                             |
|:---------|:---------|:--------|:--------|:-----------------------------------------|
| 1- 5     | I5       | ---     | IDcl    | [1/21661] Internal cluster identifier    |
| 7- 15    | F9.5     | deg     | RAdeg   | Right ascension (J2000) of member galaxy |
| 17- 24   | F8.5     | deg     | DEdeg   | Declination (J2000) of member galaxy     |
| 26- 31   | F6.4     | ---     | zph     | Photometric redshift of the galaxy       |
| 33- 38   | F6.3     | mag     | gmag    | ?=99 HSC-ssp g-band magnitude            |
| 40- 45   | F6.3     | mag     | e_gmag  | ?=99 Error on gmag                       |
| 47- 52   | F6.3     | mag     | rmag    | ?=99 HSC-ssp r-band magnitude            |
| 54- 59   | F6.3     | mag     | e_rmag  | ?=99 Error on rmag                       |
| 61- 66   | F6.3     | mag     | imag    | ?=99 HSC-ssp i-band magnitude            |
| 68- 73   | F6.3     | mag     | e_imag  | ?=99 Error on imag                       |
| 75- 80   | F6.3     | mag     | zmag    | ?=99 HSC-ssp z-band magnitude            |
| 82- 87   | F6.3     | mag     | e_zmag  | ?=99 Error on zmag                       |
| 89- 94   | F6.3     | mag     | ymag    | ?=99 HSC-ssp y-band magnitude            |
| 96- 101  | F6.3     | mag     | e_ymag  | ?=99 Error on ymag                       |
| 103- 108 | F6.3     | mag     | W1mag   | ?=99 WISE W1 (3.4um) band magnitude      |
| 110- 114 | F5.3     | mag     | e_W1mag | ?=99 Error on W1mag                      |
| 116- 121 | F6.3     | mag     | W2mag   | ?=99 WISE W2 (4.6um) band magnitude      |
| 123- 128 | F6.3     | mag     | e_W2mag | ?=99 Error on W2mag                      |
| 130- 135 | F6.3     | [Msun]  | logMass | Logarithm of galaxy stellar mass         |
| 137- 141 | F5.3     | Mpc     | rp      | Projected distance to the cluster centre |
</details>
