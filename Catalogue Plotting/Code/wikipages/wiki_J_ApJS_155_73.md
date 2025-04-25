## Summary

Based on the photometry of 10 near-ultraviolet, optical, and near-infrared bands of the Chandra Deep Field-South, we estimate the photometric redshifts for 342 X-ray sources, which constitute ~99% of all the detected X-ray sources in the field.

## Catalogue Schema

<details>
<summary>table1.dat catalogue schema</summary>

| Bytes   | Format   | Units         | Label         | Explanations                                    |
|:--------|:---------|:--------------|:--------------|:------------------------------------------------|
| 1- 3    | I3       | ---           | XID           | CDFS Unique Detection identification number (1) |
| 5- 6    | I2       | h             | RAh           | Hour of Right Ascension (J2000) (2)             |
| 8- 9    | I2       | min           | RAm           | Minute of Right Ascension (J2000) (2)           |
| 11- 15  | F5.2     | s             | RAs           | Second of Right Ascension (J2000) (2)           |
| 17      | A1       | ---           | DE-           | Sign of the Declination (J2000) (2)             |
| 18- 19  | I2       | deg           | DEd           | Degree of Declination (J2000) (2)               |
| 21- 22  | I2       | arcmin        | DEm           | Arcminute of Declination (J2000) (2)            |
| 24- 27  | F4.1     | arcsec        | DEs           | Arcsecond of Declination (J2000) (2)            |
| 29- 31  | F3.1     | arcsec        | Sep           | Offset from the X-ray position                  |
| 33- 36  | F4.2     | ---           | z             | Redshift                                        |
| 38- 42  | F5.2     | ---           | zmin          | Lower limit to z at 95% confidence level (3)    |
| 44- 48  | F5.2     | ---           | zmax          | ? Upper limit to z at 95% confidence level (3)  |
| 50- 55  | A6       | ---           | Type          | X-ray classification                            |
| 57- 59  | F3.1     | ---           | q_z           | [0,3] Quality index (4)                         |
| 00      | =        | spectroscopic | redshift.     | Note (4): Quality index, defined as follows:    |
| 2       | =        | HyperZ        | (Bolzonella   | et al., 2000A&A...363..476B) model only;        |
| 3       | =        | BPZ           | (Benitez,     | 2000ApJ...536..571B) model only;                |
| 4       | =        | COMBO-17      | (see          | Cat. <II/253>) survey only;                     |
| 5       | =        | BPZ           | and           | HyperZ;                                         |
| 6       | =        | COMBO-17      | and           | HyperZ;                                         |
| 7       | =        | COMBO-17      | and           | BPZ;                                            |
| 9       | =        | COMBO-17,     | BPZ           | and HyperZ;                                     |
| 2       | =        | Single-line   | spectrum      | and HyperZ;                                     |
| 6       | =        | Single-line   | spectrum,     | COMBO-17, and HyperZ;                           |
| 9       | =        | Single-line   | spectrum,     | COMBO-17, BPZ and HyperZ;                       |
| 0       | =        | Secure        | spectroscopic | redshift, but optical counterpart uncertain;    |
| 0       | =        | Secure        | spectroscopic | redshift.                                       |

**Note**: Identified as [GZW2002] XID NNN in Simbad.
Note (2): Optical counterpart position.
Note (3): Lower and upper limits to z at 95% confidence level:
    -1.00 = spectroscopic redshift.
Note (4): Quality index, defined as follows:
    0.2 = HyperZ (Bolzonella et al., 2000A&A...363..476B) model only;
    0.3 = BPZ (Benitez, 2000ApJ...536..571B) model only;
    0.4 = COMBO-17 (see Cat. <II/253>) survey only;
    0.5 = BPZ and HyperZ;
    0.6 = COMBO-17 and HyperZ;
    0.7 = COMBO-17 and BPZ;
    0.9 = COMBO-17, BPZ and HyperZ;
    1.2 = Single-line spectrum and HyperZ;
    1.6 = Single-line spectrum, COMBO-17, and HyperZ;
    1.9 = Single-line spectrum, COMBO-17, BPZ and HyperZ;
    2.0 = Secure spectroscopic redshift, but optical counterpart uncertain;
    3.0 = Secure spectroscopic redshift.

</details>
