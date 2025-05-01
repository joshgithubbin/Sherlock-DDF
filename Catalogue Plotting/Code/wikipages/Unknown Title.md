**Authors:** Vettolani G., Paltani S., Tresse L., Zamorani G., Le Brun V.,, Moreau C., Bottini D., Maccagni D., Picat J.P., Scaramella R.,, Scodeggio M., Zanichelli A., Adami C., Arnouts S., Bardelli S.,, Bolzonella M., Cappi A., Charlot S., Contini T., Foucaud S., Franzetti P.,, Garilli B., Gavignaud I., Guzzo L., Ilbert O., Iovino A., Mccracken H.J.,, Mancini D., Marano B., Marinoni C., Mathez G., Mazure A., Meneux B.,, Merighi R., Pello R., Pollo A., Pozzetti L., Radovich M., Zucca E.,, Arnaboldi M., Bondi M., Bongiorno A., Busarello G., Ciliegi P.,, Gregorini L., Mellier Y., Merluzzi P., Ripepi V., Rizzo D., <Astron. Astrophys., 428, 1043-1049 (2004)>, =2004A&A...428.1043L

## Summary: Unknown Title 

This paper presents the VIMOS VLT Deep Survey around the Chandra Deep Field South (CDFS). We have measured 1599 new redshifts with VIMOS on the European Observatory Very Large Telescope - UT3, in an area 21x21.6arcmin^2^, including 784 redshifts in the Hubble Space Telescope - Advanced Camera for Surveys GOODS area. 30% of all objects with I_AB_=24 have been observed independently of magnitude, indicating that the sample is purely magnitude limited. We have reached an unprecedented completeness level of 84% in terms of the ratio of secure measurements vs. observed objects, while 95% of all objects have a redshift measurement. A total of 1452 galaxies, 139 stars, 8 QSOs have a redshift identification, 141 of these being unsecure measurements. The redshift distribution down to IAB=24 is peaked at a median redshift z=0.73, with a significant high redshift tail extending up to ~4. Several high density peaks in the distribution of galaxies are identified. In particular, the strong peak at z=0.735 contains more than 130 galaxies in a velocity range +/-2000km/s distributed all across the transverse ~20h^-1^Mpc of the survey. We are releasing all redshifts to the community, along with the cross identification with HST-ACS GOODS sources on the CENCOS database environment http://cencosw.oamp.fr .

## Photometric Redshift 
 
**z:** Redshift 
 

## Catalogue Schema

<details>
<summary>vcdfs.dat</summary>

| Bytes   | Format   | Units   | Label      | Explanations                                        |
|:--------|:---------|:--------|:-----------|:----------------------------------------------------|
| 1- 19   | A19      | ---     | HST-GOODS  | HST UAI designation (JHHMMSS.ss+DDMMSS.s)           |
| 21- 26  | I6       | ---     | VCDFS      | VVDS-CDFS sequential number                         |
| 28- 37  | F10.7    | deg     | RAdeg      | Right ascension in decimal degrees (J2000)          |
| 39- 48  | F10.6    | deg     | DEdeg      | Declination in decimal degrees (J2000)              |
| 50- 55  | F6.4     | ---     | z          | Redshift                                            |
| 57- 58  | I2       | ---     | f_z        | Flag on z (1)                                       |
| 60- 66  | F7.4     | mag     | Imag       | VVDS I band AB magnitude (MAG_AUTO_I)               |
| 1       | =        | 50%     | confidence | in the redshift (Primary target)                    |
| 2       | =        | 75%     | confidence | in the redshift (Primary target)                    |
| 3       | =        | 95%     | confidence | (Primary target)                                    |
| 4       | =        | 100%    | confidence | (Primary target)                                    |
| 8       | =        | not     | specified  | (one case) (Primary target)                         |
| 9       | =        | Single  | isolated   | emission line spectra. (Primary target)             |
| 11      | =        | 50%     | confidence | in the redshift (Primary QSO target)                |
| 12      | =        | 75%     | confidence | in the redshift (Primary QSO target)                |
| 13      | =        | 95%     | confidence | (Primary QSO target)                                |
| 14      | =        | 100%    | confidence | (Primary QSO target)                                |
| 21      | =        | 50%     | confidence | in the redshift (Secondary Identified target)       |
| 22      | =        | 75%     | confidence | in the redshift (Secondary Identified target)       |
| 23      | =        | 95%     | confidence | (Secondary Identified target)                       |
| 24      | =        | 100%    | confidence | (Secondary Identified target)                       |
| 29      | =        | Single  | isolated   | emission line spectra (Secondary Identified target) |

**Note**: Flags as follows:
      1 = 50% confidence in the redshift (Primary target)
      2 = 75% confidence in the redshift (Primary target)
      3 = 95% confidence (Primary target)
      4 = 100% confidence (Primary target)
      8 = not specified (one case) (Primary target)
      9 = Single isolated emission line spectra. (Primary target)
     11 = 50% confidence in the redshift (Primary QSO target)
     12 = 75% confidence in the redshift (Primary QSO target)
     13 = 95% confidence (Primary QSO target)
     14 = 100% confidence (Primary QSO target)
     21 = 50% confidence in the redshift (Secondary Identified target)
     22 = 75% confidence in the redshift (Secondary Identified target)
     23 = 95% confidence (Secondary Identified target)
     24 = 100% confidence (Secondary Identified target)
     29 = Single isolated emission line spectra (Secondary Identified target)
     (Primary Target means the object which has been targeted in the VIMOS
      spectral slit; secondary Target means an object which is present by 
      chance in the spectral slit in addition of the primary target. Thus 
      the secondary object is not ensured to be fully centered within the slit)

</details>
