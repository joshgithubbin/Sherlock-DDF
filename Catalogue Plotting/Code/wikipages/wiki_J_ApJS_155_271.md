**Authors:** Bergeron J., Hasinger G., Lehmann I., Kewley L., Mainieri V.,, Nonino M., Rosati P., Giacconi R., Gilli R., Gilmozzi R., Norman C.,, Romaniello M., Schreier E., Tozzi P., Wang J.X., Zheng W., Zirm A., <Astrophys. J. Suppl. Ser., 155, 271-349 (2004)>, =2004ApJS..155..271S

## Summary: Chandra Deep Field-South: Optical spectroscopy 

We present the results of our spectroscopic follow-up program of the X-ray sources detected in the 942ks exposure of the Chandra Deep Field-South (CDFS). A total of 288 possible counterparts were observed at the VLT with the FORS1/FORS2 spectrographs for 251 of the 349 Chandra sources (including three additional faint X-ray sources). Spectra and R-band images are shown for all the observed sources and R-K colors are given for most of them. Spectroscopic redshifts were obtained for 168 X-ray sources, of which 137 have both reliable optical identification and redshift estimate (including 16 external identifications). The R<24 observed sample comprises 161 X-ray objects (181 optical counterparts), and 126 of them have unambiguous spectroscopic identification.

## Catalogue Schema

<details>
<summary>table4.dat</summary>

| Bytes   | Format   | Units   | Label       | Explanations                                  |
|:--------|:---------|:--------|:------------|:----------------------------------------------|
| 1- 3    | I3       | ---     | EName       | ? Extended source name                        |
| 5       | A1       | ---     | f_EName     | [wn] Source association (1)                   |
| 7- 9    | I3       | ---     | [GZW2002]   | Unique Detection identification number,       |
| 10      | A1       | ---     | m_[GZW2002] | [a-e] Multiplicity index on [GZW2002] (G1)    |
| 11      | A1       | ---     | n_[GZW2002] | [*] *: Extended X-ray objects                 |
| 13- 23  | A11      | ---     | Mask        | Mask designations                             |
| 25- 26  | I2       | h       | RAh         | Hour of Right Ascension (J2000) (3)           |
| 28- 29  | I2       | min     | RAm         | Minute of Right Ascension (J2000) (3)         |
| 31- 35  | F5.2     | s       | RAs         | Second of Right Ascension (J2000) (3)         |
| 37      | A1       | ---     | DE-         | Sign of the Declination (J2000) (3)           |
| 38- 39  | I2       | deg     | DEd         | Degree of Declination (J2000) (3)             |
| 41- 42  | I2       | arcmin  | DEm         | Arcminute of Declination (J2000) (3)          |
| 44- 47  | F4.1     | arcsec  | DEs         | Arcsecond of Declination (J2000) (3)          |
| 49- 53  | F5.2     | mag     | Rmag        | ? The R band magnitude (Vega)                 |
| 54      | A1       | ---     | f_Rmag      | [XW-] Flag on Rmag (G2)                       |
| 56      | A1       | ---     | l_R-K       | Limit flag on R-K                             |
| 57- 61  | F5.2     | mag     | R-K         | ? The (R-K) color (Vega)                      |
| 62- 63  | A2       | ---     | f_R-K       | Flag on R-K (G3)                              |
| 65- 68  | F4.1     | [10-7W] | logLX       | ? Log base 10 of the 0.5-10keV luminosity (4) |
| 70- 74  | F5.2     | ---     | HR          | Hardness ratio (G4)                           |
| 76- 80  | F5.3     | ---     | z           | ? Best redshift estimate (5)                  |
| 82- 87  | A6       | ---     | OClass      | Optical classification (6)                    |
| 89- 97  | A9       | ---     | XClass      | X-ray classification (7)                      |
| 99-101  | F3.1     | ---     | Qual        | Redshift reliability determination (8)        |
| 102     | A1       | ---     | f_Qual      | [+] +: we consider the identification final   |
| 104-161 | A58      | ---     | Comm        | Additional comments (9)                       |
</details>

<details>
<summary>table5.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                             |
|:--------|:---------|:--------|:----------|:-----------------------------------------|
| 1- 3    | I3       | ---     | [GZW2002] | Unique Detection identification number,  |
| 5- 20   | A16      | ---     | CXO       | CXO designation (JHHMMSS.s-DDMMSS)       |
| 22- 23  | I2       | h       | RAh       | Right ascension (J2000.0)                |
| 25- 26  | I2       | min     | RAm       | Right ascension (J2000.0)                |
| 28- 32  | F5.2     | s       | RAs       | Right ascension (J2000.0)                |
| 34      | A1       | ---     | DE-       | Declination sign (J2000.0)               |
| 35- 36  | I2       | deg     | DEd       | Declination (J2000.0)                    |
| 38- 39  | I2       | arcmin  | DEm       | Declination (J2000.0)                    |
| 41- 45  | F5.2     | arcsec  | DEs       | Declination (J2000.0)                    |
| 47      | A1       | ---     | l_SCts    | Limit flag on S                          |
| 48- 51  | F4.1     | ct      | SCts      | Net counts in soft (0.5-2keV) band       |
| 53- 56  | F4.1     | ct      | e_SCts    | ? rms uncertainty on S                   |
| 58      | A1       | ---     | l_HCts    | Limit flag on H                          |
| 59- 62  | F4.1     | ct      | HCts      | Net counts in hard (2-10keV) band        |
| 64- 66  | F3.1     | ct      | e_HCts    | ? rms uncertainty on H                   |
| 68- 72  | F5.1     | ks      | STime     | Effective exposure time in the soft band |
| 74- 78  | F5.1     | ks      | HTime     | Effective exposure time in the soft band |
| 80      | A1       | ---     | l_SFlux   | Limit flag on FS                         |
| 81- 87  | E7.1     | mW/m2   | SFlux     | Flux in soft band                        |
| 89- 95  | E7.1     | mW/m2   | e_SFlux   | ? rms uncertainty on FS                  |
| 97      | A1       | ---     | l_HFlux   | Limit flag on FH                         |
| 98-104  | E7.1     | mW/m2   | HFlux     | Flux in hard band                        |
| 106-112 | E7.1     | mW/m2   | e_HFlux   | ? rms uncertainty on FH                  |
| 114-115 | I2       | ---     | HR        | Hardness ratio, (H-S)/(H+S) (G4)         |
</details>

<details>
<summary>table8.dat</summary>

| Bytes   | Format   | Units   | Label       | Explanations                               |
|:--------|:---------|:--------|:------------|:-------------------------------------------|
| 1       | I1       | ---     | Type        | [1/4] Counterpart type code (1)            |
| 3- 5    | I3       | ---     | [GZW2002]   | Unique Detection identification number,    |
| 6       | A1       | ---     | m_[GZW2002] | [a-e] Multiplicity index on [GZW2002] (G1) |
| 7       | A1       | ---     | n_[GZW2002] | [*] *: Extended X-ray object               |
| 9- 10   | I2       | h       | RAh         | Hour of Right Ascension (J2000) (2)        |
| 12- 13  | I2       | min     | RAm         | Minute of Right Ascension (J2000) (2)      |
| 15- 19  | F5.2     | s       | RAs         | Second of Right Ascension (J2000) (2)      |
| 21      | A1       | ---     | DE-         | Sign of the Declination (J2000) (2)        |
| 22- 23  | I2       | deg     | DEd         | Degree of Declination (J2000) (2)          |
| 25- 26  | I2       | arcmin  | DEm         | Arcminute of Declination (J2000) (2)       |
| 28- 32  | F5.2     | arcsec  | DEs         | Arcsecond of Declination (J2000) (2)       |
| 34- 38  | F5.2     | mag     | Rmag        | ? The R band magnitude (Vega)              |
| 39      | A1       | ---     | f_Rmag      | [W] Flag on Rmag (G2)                      |
| 41- 45  | F5.2     | mag     | R-K         | ? The (R-K) band color (Vega)              |
| 46- 47  | A2       | ---     | f_R-K       | [K - NA] Flag on R-K (G3)                  |
| 49- 53  | F5.2     | ---     | HR          | Hardness ratio (G4)                        |
</details>

<details>
<summary>table9.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                  |
|:--------|:---------|:--------|:--------|:----------------------------------------------|
| 1- 5    | I5       | ---     | Seq     | Sequential number                             |
| 7- 17   | A11      | ---     | Mask    | Mask designations                             |
| 19- 20  | I2       | h       | RAh     | Hour of Right Ascension (J2000)               |
| 22- 23  | I2       | min     | RAm     | Minute of Right Ascension (J2000)             |
| 25- 29  | F5.2     | s       | RAs     | Second of Right Ascension (J2000)             |
| 31      | A1       | ---     | DE-     | Sign of the Declination (J2000)               |
| 32- 33  | I2       | deg     | DEd     | Degree of Declination (J2000)                 |
| 35- 36  | I2       | arcmin  | DEm     | Arcminute of Declination (J2000)              |
| 38- 41  | F4.1     | arcsec  | DEs     | Arcsecond of Declination (J2000)              |
| 43- 47  | F5.2     | mag     | Rmag    | ? The R band magnitude (Vega)                 |
| 48- 49  | A2       | ---     | f_Rmag  | [NA ] NA: No data to determine magnitude      |
| 51- 55  | F5.3     | ---     | z       | Best redshift estimate (1)                    |
| 57- 62  | A6       | ---     | Class   | Classification (2)                            |
| 64      | I1       | ---     | Qual    | [1/2]? Redshift reliability determination (3) |
| 66- 94  | A29      | ---     | Comm    | Additional comments                           |
</details>
