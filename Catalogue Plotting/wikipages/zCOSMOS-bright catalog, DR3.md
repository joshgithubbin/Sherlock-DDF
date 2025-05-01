**Authors:** Fevre O.L., Renzini A., Zamorani G., Scodeggio M., Contini T.,, Carollo C.M., Hasinger G., Kneib J.-P., Iovino A., Le Brun V., Maier C.,, Mainieri V., Mignoli M., Silverman J., Tasca L.A.M., Bolzonella M.,, Bongiorno A., Bottini D., Capak P., Caputi K., Cimatti A., Cucciati O.,, Daddi E., Feldmann R., Franzetti P., Garilli B., Guzzo L., Ilbert O.,, Kampczyk P., Kovac K., Lamareille F., Leauthaud A., Le Borgne J.-F.,, Mccracken H.J., Marinoni C., Pello R., Ricciardelli E., Scarlata C.,, Vergani D., Sanders D.B., Schinnerer E., Scoville N., Taniguchi Y.,, Arnouts S., Aussel H., Bardelli S., Brusa M., Cappi A., Ciliegi P.,, Finoguenov A., Foucaud S., Franceschini R., Halliday C., Impey C.,, Knobel C., Koekemoer A., Kurk J., Maccagni D., Maddox S., Marano B.,, Marconi G., Meneux B., Mobasher B., Moreau C., Peacock J.A., Porciani C.,, Pozzetti L., Scaramella R., Schiminovich D., Shopbell P., Smail I.,, Thompson D., Tresse L., Vettolani G., Zanichelli A., Zucca E., <Astrophys. J. Suppl. Ser., 172, 70-85 (2007)>, =2007ApJS..172...70L

## Summary: zCOSMOS-bright catalog, DR3 

zCOSMOS is a large-redshift survey that is being undertaken in the COSMOS field using 600hr of observation with the VIMOS spectrograph on the 8m VLT. The survey is designed to characterize the environments of COSMOS galaxies from the 100kpc scales of galaxy groups up to the 100Mpc scale of the cosmic web and to produce diagnostic information on galaxies and active galactic nuclei. The zCOSMOS survey consists of two parts: (1) zCOSMOS-bright, a magnitude-limited I-band I_AB_<22.5 sample of about 20000 galaxies with 0.1<z<1.2 covering the whole 1.7deg^2^ COSMOS ACS field, for which the survey parameters at z~0.7 are designed to be directly comparable to those of the 2dFGRS at z~0.1; and (2) zCOSMOS-deep, a survey of approximately 10000 galaxies selected through color-selection criteria to have 1.4<z<3.0, within the central 1deg^2^. This paper describes the survey design and the construction of the target catalogs and briefly outlines the observational program and the data pipeline. In the first observing season, spectra of 1303 zCOSMOS-bright targets and 977 zCOSMOS-deep targets have been obtained.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-172-70/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**z:** ?=- Redshift (REDSHIFT) 
 

## Catalogue Schema

<details>
<summary>zcosmos3.dat</summary>

| Bytes   | Format   | Units   | Label    | Explanations                                  |
|:--------|:---------|:--------|:---------|:----------------------------------------------|
| 1- 6    | I6       | ---     | zCOSMOS  | [700137/960004] zCOSMOS identification number |
| 8- 17   | F10.6    | deg     | RAdeg    | Right ascension (J2000) (RAJ2000)             |
| 19- 26  | F8.6     | deg     | DEdeg    | Declination (J2000) (DEJ2000)                 |
| 28- 33  | F6.4     | ---     | z        | ?=- Redshift (REDSHIFT)                       |
| 35- 39  | F5.1     | ---     | CC       | Confidence class (CC) (1)                     |
| 41- 45  | F5.2     | mag     | Imag     | Selection mag F814W AB (IMAG_AB)              |
| 47- 48  | I2       | ---     | FlagS    | [-1/1] Flag for satisfying bright sample      |
| 50      | I1       | ---     | FlagX    | [0/2] Flag for X-ray selection (FLAG_X)       |
| 52      | I1       | ---     | FlagR    | [0/2] Flag for radio selection (FLAG_R)       |
| 54      | I1       | ---     | FlagUV   | [0/2] Flag for UV selection (FLAG_UV)         |
| 56-107  | A52      | ---     | FileName | Name of the spectrum fits file in             |

**Note**: Confidence Class (CC) defined as 3 digits (ab.c).

</details>
