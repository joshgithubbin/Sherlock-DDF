**Authors:** McCracken H.J., Hudelot W., Rouberol O., Herent O., Mellier Y.,, Dunlop J., Le Fevre O., Franx M., Fynbo J., Bowler R., Caputi K.,, Kauffmann O., Milvang-Jensen B., Gonzalez-Fernandez C., Gonzalez-Solares E.,, Irwin M., Lewis J., Blake R., Cross N., Read M., Sutorius E., <Institut d'Astrophysique de Paris, UltraVISTA, Cambridge Astronomical, Survey Unit (CASU) and Wide Field Astronomy Unit (WFAU), 2019>, =2023yCat.2373....0M, =2012A&A...544A.156M

## Summary: The fourth UltraVISTA data release (DR4) 

UltraVISTA is an ultra-deep near-infrared survey of the central region of the COSMOS field (Scoville+ 2007ApJS..172..196K). In this fourth release (DR4) we provide five stacked images and their corresponding weight maps for Y JHKs and NB118 narrow-band data taken during the first seven years of UltraVISTA survey operations. In addition, single band individual source lists and source lists created in dual-image mode (using the Ks image as a detection image) are provided (note that in ESO terminology, single-band tabular data are referred to as "Source lists" and multi-band merged data are referred to as catalogues). We also provide a five-band catalogue that meets the requirement for a catalogue in the Phase 3 framework. The data volume is ~90GB as in DR3. The total survey area is close to 1.9deg^2^.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/II-373/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes    | Format   | Units   | Label      | Explanations                                  |
|:---------|:---------|:--------|:-----------|:----------------------------------------------|
| 1- 9     | A9       | ---     | ---        | [UVISTADR4]                                   |
| 11- 29   | A19      | ---     | UVISTADR4  | UltraVISTA source designation (DR4)           |
| 31- 36   | I6       | ---     | Seq        | [1/451587] Running object number (NUMBER)     |
| 38- 48   | F11.7    | deg     | RAdeg      | [149/151] Right ascension of barycenter       |
| 50- 58   | F9.7     | deg     | DEdeg      | [1.5/3] Declination of barycenter (J2000)     |
| 60- 67   | F8.2     | pix     | Xpos       | Object position along x (X_IMAGE)             |
| 69- 76   | F8.2     | pix     | Ypos       | Object position along y (Y_IMAGE)             |
| 78       | I1       | ---     | F          | [0/1] Bad region flag: !=0 for bad region     |
| 80- 86   | F7.5     | mag     | EBV        | [0.015/0.03] Galactic reddening E(B-V) based  |
| 88- 94   | F7.4     | mag     | Yap2       | [12.6/37]? Y fixed aperture AB magnitude in   |
| 96- 106  | F11.6    | mag     | e_Yap2     | [3e-6/1542]? Yap2 error (Y_APER2_ERR)         |
| 108- 114 | F7.4     | mag     | Yap7       | [10.4/37.1]? Y fixed aperture AB magnitude    |
| 116- 127 | F12.6    | mag     | e_Yap7     | [1e-6/22565]? Yap7 error (Y_APER7_ERR)        |
| 129- 135 | F7.4     | mag     | Ymag       | [10.1/36.5]? VISTA Y auto AB magnitude        |
| 137- 147 | F11.6    | mag     | e_Ymag     | [2e-6/1436]? Ymag error (Y_AUTO_ERR)          |
| 149- 156 | F8.4     | pix     | Yrad       | [0.005/242]? Radius of aperture containing    |
| 158- 159 | I2       | ---     | Ysf        | [0/52] SExtractor Y flag (Y_FLAG) (1)         |
| 161- 167 | F7.4     | mag     | Jap2       | [13/35.3]? J fixed aperture AB magnitude in   |
| 169- 179 | F11.6    | mag     | e_Jap2     | [3e-6/1432]? Jap2 error (J_APER2_ERR)         |
| 181- 187 | F7.4     | mag     | Jap7       | [10.8/38]? J fixed aperture AB magnitude in   |
| 189- 200 | F12.6    | mag     | e_Jap7     | [2e-6/58792]? Jap7 error (J_APER7_ERR)        |
| 202- 208 | F7.4     | mag     | Jmag       | [10.2/34.6]? VISTA J auto AB magnitude        |
| 210- 219 | F10.6    | mag     | e_Jmag     | [2e-6/955]? Jmag error (J_AUTO_ERR)           |
| 221- 228 | F8.4     | pix     | Jrad       | [0.004/226]? Radius of aperture containing    |
| 230- 231 | I2       | ---     | Jsf        | [0/52] SExtractor J flag (J_FLAG) (1)         |
| 233- 239 | F7.4     | mag     | Hap2       | [12.6/38.2]? H fixed aperture AB magnitude    |
| 241- 252 | F12.6    | mag     | e_Hap2     | [3e-6/29111]? Hap2 error (H_APER2_ERR)        |
| 254- 260 | F7.4     | mag     | Hap7       | [10.3/36]? H fixed aperture AB magnitude in   |
| 262- 273 | F12.6    | mag     | e_Hap7     | [3e-6/13636]? Hap7 error (H_APER7_ERR)        |
| 275- 281 | F7.4     | mag     | Hmag       | [9.7/35.5]? VISTA H auto AB magnitude         |
| 283- 293 | F11.6    | mag     | e_Hmag     | [4e-6/2977]? Hmag error (H_AUTO_ERR)          |
| 295- 304 | F10.6    | pix     | Hrad       | [0.005/268]? Radius of aperture containing    |
| 306- 307 | I2       | ---     | Hsf        | [0/52] SExtractor H flag (H_FLAG) (1)         |
| 309- 315 | F7.4     | mag     | Ksap2      | [12.7/31.5]? Ks fixed aperture AB magnitude   |
| 317- 325 | F9.6     | mag     | e_Ksap2    | [2e-6/27]? Ksap2 error (KS_APER2_ERR)         |
| 327- 333 | F7.4     | mag     | Ksap7      | [10.6/35]? Ks fixed aperture AB magnitude in  |
| 335- 345 | F11.6    | mag     | e_Ksap7    | [3e-6/3851]? Ksap7 error (KS_APER7_ERR)       |
| 347- 353 | F7.4     | mag     | Ksmag      | [9.8/30.8]? VISTA Ks auto AB magnitude        |
| 355- 363 | F9.6     | mag     | e_Ksmag    | [6e-6/15]? Ksmag error (KS_AUTO_ERR)          |
| 365- 372 | F8.4     | pix     | Ksrad      | [0.16/222]? Radius of aperture containing     |
| 374- 375 | I2       | ---     | Ksf        | [0/52] SExtractor Ks flag [detection image]   |
| 377- 383 | F7.4     | mag     | NB118ap2   | [11.6/37]? NB118 fixed aperture AB magnitude  |
| 385- 396 | F12.6    | mag     | e_NB118ap2 | [4e-6/25607]? NB118ap2 error                  |
| 398- 404 | F7.4     | mag     | NB118ap7   | [9.8/39.1]? NB118 fixed aperture AB           |
| 406- 418 | F13.6    | mag     | e_NB118ap7 | [2e-6/193362]? NB118ap7 error                 |
| 420- 426 | F7.4     | mag     | NB118mag   | [9.5/42]? VISTA NB118 (1.18um) auto AB        |
| 428- 440 | F13.6    | mag     | e_NB118mag | [3e-6/826846]? NB118mag error                 |
| 442- 452 | F11.6    | pix     | NB118rad   | [8e-6/1884]? Radius of aperture containing    |
| 454- 455 | I2       | ---     | NB118sf    | [0/53] SExtractor NB118 flag (NB118_FLAG) (1) |

**Note**: The best possible object sample are those objects which have all
          flags equal to zero.

</details>
