**Authors:** Takey A., Schwope A., Lamer G., <Astron. Astrophys. 564, A54 (2014)>, =2014A&A...564A..54T

## Summary: 2XMMi/SDSS Galaxy Cluster Survey. III. 

We present a sample of 383 X-ray selected galaxy groups and clusters with spectroscopic redshift measurements (up to z~0.79) from the 2XMMi/SDSS Galaxy Cluster Survey. The X-ray cluster candidates were selected as serendipitously detected sources from the 2XMMi-DR3 catalogue that were located in the footprint of the Sloan Digital Sky Survey (SDSS-DR7). The cluster galaxies with available spectroscopic redshifts were selected from the SDSS-DR10. We developed an algorithm for identifying the cluster candidates that are associated with spectroscopically targeted luminous red galaxies and for constraining the cluster spectroscopic redshift. A cross-correlation of the constructed cluster sample with published optically selected cluster catalogues yielded 264 systems with available redshifts. The present redshift measurements are consistent with the published values. The current cluster sample extends the optically confirmed cluster sample from our cluster survey by 67 objects. Moreover, it provides spectroscopic confirmation for 78 clusters among our published cluster sample, which previously had only photometric redshifts. Of the new cluster sample that comprises 67 systems, 55 objects are newly X-ray discovered clusters and 52 systems are sources newly discovered as galaxy clusters in optical and X-ray wavelengths. Based on the measured redshifts and the fluxes given in the 2XMMi-DR3 catalogue, we estimated the X-ray luminosities and masses of the cluster sample.

## Spectroscopic Redshift 
 
**zs:** Cluster spectroscopic redshift (2) 
 

## Photometric Redshift 
 
**zp:** Cluster photometric redshift (2) 
 

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format    | Units      | Label   | Explanations                                                          |
|:--------|:----------|:-----------|:--------|:----------------------------------------------------------------------|
| 1- 6    | I6        | ---        | Seq     | X-ray detection number in the 2XMMi-DR3 (1)                           |
| 10- 13  | A4        | ---        | ---     | [2XMM]                                                                |
| 14      | A1        | ---        | n_2XMM  | [I] when 2XMMi release (Cat. IX/40)                                   |
| 16- 31  | A16       | ---        | 2XMM    | IAU name given in the 2XMMi-DR3 cat. (1)                              |
| 34- 42  | F9.5      | deg        | RAdeg   | X-ray detection right ascension (J2000) (1)                           |
| 44- 52  | F9.5      | deg        | DEdeg   | X-ray detection declination (J2000) (1)                               |
| 54- 63  | I010      | ---        | ObsID   | XMM-Newton observation number (1)                                     |
| 65- 70  | F6.4      | ---        | z       | Cluster redshift (identical to zs)                                    |
| 72- 75  | F4.2      | kpc/arcsec | Scale   | Scale at the cluster redshift                                         |
| 77- 83  | F7.2      | kpc        | R500    | Estimated radius R_500_ (mean density is 500                          |
| 85- 90  | F6.2      | 10-17W/m2  | Fcat    | X-ray flux in [0.5-2.0]keV band (1)                                   |
| 92- 95  | F4.2      | 10-17W/m2  | e_Fcat  | Error in Fcat                                                         |
| 97-102  | F6.2      | 10+35W     | Lcat    | X-ray luminosity in [0.5-2]keV band                                   |
| 104-108 | F5.2      | 10+35W     | e_Lcat  | Error in Lcat                                                         |
| 110-116 | F7.2      | 10+35W     | L500    | X-ray bolometric luminosity within R_500_                             |
| 118-123 | F6.2      | 10+35W     | e_L500  | Error in L500                                                         |
| 125-129 | F5.2      | 10+13Msun  | M500    | Mass within R_500_                                                    |
| 131-135 | F5.2      | 10+13Msun  | e_M500  | Error in M500                                                         |
| 137-155 | I19       | ---        | BCG     | Id in the SDSS-DR10 of the likely BCG (2)                             |
| 157-165 | F9.5      | deg        | RABdeg  | Likely BCG right ascension (J2000) (2)                                |
| 167-175 | F9.5      | deg        | DEBdeg  | Likely BCG declination (J2000) (2)                                    |
| 177-182 | F6.3      | mag        | rmag    | Likely BCG apparent magnitude in r-band                               |
| 184-189 | F6.4      | ---        | zs      | Cluster spectroscopic redshift (2)                                    |
| 191-192 | I2        | ---        | Ns      | Number of cluster galaxies with spectra (2)                           |
| 194-199 | F6.4      | ---        | zp      | Cluster photometric redshift (2)                                      |
| 201-202 | I2        | ---        | Np      | Number of cluster galaxies with zp (2)                                |
| 204-209 | F6.2      | kpc        | Offset  | Optical/X-ray offset                                                  |
| 211-245 | A35       | ---        | NED     | Literature name (NED)                                                 |
| 247-255 | A9        | ---        | Note    | A note about the status of each cluster (3)                           |
| 3       | catalogue | (IX/41)    | Note    | (2): These parameters are obtained from the current developed optical |

**Note**: Parameters extracted from the 2XMMi-DR3 catalogue (IX/41)
Note (2): These parameters are obtained from the current developed optical
          cluster detection algorithm.
Note (3): The note is:
   Paper-III = new cluster from the current work
   Paper-II  = a cluster in Paper II (J/A+A/558/A75) and confirmed
               spectroscopically with the present procedure

</details>
