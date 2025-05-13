**Authors:** Cimatti A., Zamorani G., Pozzetti L., Daddi E., Renzini A.,, Broadhurst T., Cristiani S., D'Odorico S., Fontana A., Giallongo E.,, Gilmozzi R., Menci N., Saracco P., <Astron. Astrophys. 437, 883 (2005)>, =2005A&A...437..883M

## Summary: K20 survey: spectroscopic catalogue 

The K20 survey is a near infrared-selected, deep (Ks<20) redshift survey targeting galaxies in two independent regions of the sky, the Chandra Deep Field South and the field around the quasar 0055-2659, for a total area of 52arcmin^2^. The total Ks-selected sample includes 545 objects. Low-resolution (R~300-600) optical spectra for 525 of them have been obtained with the FORS1/FORS2 spectrographs at the ESO/VLT, providing 501 spectroscopic identifications (including 12 type-1 AGN and 45 stars); consequently, we were able to measure redshifts and identify stars in 96% of the observed objects, whereas the spectroscopic completeness with respect to the total photometrically selected sample is 92% (501/545). The K20 survey is therefore the most complete spectroscopic survey of a near infrared-selected sample to date. The K20 survey contains 444 spectroscopically identified galaxies, covering a redshift range of 0.05<z<2.73, with a mean redshift <z>=0.75; excluding the 32 "low-quality" redshifts does not significantly change these values.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-A+A-437-883/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**z:** ? Spectroscopic redshift 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-A+A-437-883/Subcatalogues/ECDFS/Plots/zspec.png)
<details>
<summary>Quality flag . . .

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-A+A-437-883/Subcatalogues/ECDFS/Plots/q_zspec.png)</summary>
## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes   | Format   | Units        | Label         | Explanations                                                  |
|:--------|:---------|:-------------|:--------------|:--------------------------------------------------------------|
| 1- 11   | A11      | ---          | Seq           | K20 identification number,                                    |
| 13- 14  | I2       | h            | RAh           | Right ascension (J2000.0)                                     |
| 16- 17  | I2       | min          | RAm           | Right ascension (J2000.0)                                     |
| 19- 24  | F6.3     | s            | RAs           | Right ascension (J2000.0)                                     |
| 26      | A1       | ---          | DE-           | Declination sign (J2000.0)                                    |
| 27- 28  | I2       | deg          | DEd           | Declination (J2000.0)                                         |
| 30- 31  | I2       | arcmin       | DEm           | Declination (J2000.0)                                         |
| 33- 37  | F5.2     | arcsec       | DEs           | Declination (J2000.0)                                         |
| 39- 43  | F5.2     | mag          | Ksmag         | Total (SExtractor BEST) Ks-band magnitude                     |
| 45- 48  | F4.2     | mag          | R-K           | R-K colour index, measured in a 2"-diameter                   |
| 50- 54  | F5.3     | ---          | z             | ? Spectroscopic redshift                                      |
| 55      | A1       | ---          | ---           | [I] (indef) when no redshift (q_z=-1)                         |
| 56- 57  | I2       | ---          | q_z           | [-1/1]? Quality flag on redshfit (1)                          |
| 59- 61  | A3       | ---          | Class         | Spectroscopic classes code (2)                                |
| 63- 79  | A17      | ---          | FileName      | Spectra file name in "sp" subdirectory                        |
| 81- 92  | A12      | ---          | Com           | Comment                                                       |
| 1       | =        | solid        | redshift      | determination;                                                |
| 0       | =        | tentative    | redshift      | determination;                                                |
| 1       | =        | no           | redshfit      | determination.                                                |
| 0       | =        | objects      | classified    | as stars;                                                     |
| 1       | =        | red          | passive       | early-type galaxies;                                          |
| 2       | =        | blue         | emission-line | galaxies;                                                     |
| 5       | =        | intermediate | galaxies      | with emission lines but red continuum indices;                |
| 3       | =        | galaxies     | which         | are not included in one of the three previous classes;        |
| 4       | =        | broad-line   | AGN.          | We remind that objects with only a tentative redshift (q_z=0) |

**Note**: Quality flag on redshfit as follows:
      1 = solid redshift determination;
      0 = tentative redshift determination;
     -1 = no redshfit determination.
Note (2): Spectroscopic classes as follows:
      0 = objects classified as stars;
      1 = red passive early-type galaxies;
      2 = blue emission-line galaxies;
    1.5 = intermediate galaxies with emission lines but red continuum indices;
      3 = galaxies which are not included in one of the three previous classes;
      4 = broad-line AGN.
      We remind that objects with only a tentative redshift (q_z=0)
      are not classified.

</details>
