**Authors:** Mainieri V., Padovani P., Kellermann K.I., Miller N.,, Rosati P., Tozzi P., Vattakunnel S., Balestra I., Brandt W.N., Luo B.,, Xue Y.Q., <Astrophys. J. Suppl. Ser., 203, 15 (2012)>, =2012ApJS..203...15B

## Summary: Counterparts to 1.4GHz sources in ECDF-S 

We study a sample of 883 sources detected in a deep Very Large Array survey at 1.4GHz in the Extended Chandra Deep Field South. This paper focuses on the identification of their optical and infrared (IR) counterparts. We use a likelihood-ratio technique that is particularly useful when dealing with deep optical images to minimize the number of spurious associations. We find a reliable counterpart for 95% of our radio sources. Most of the counterparts (74%) are detected at optical wavelengths, but there is a significant fraction (21%) that are only detectable in the IR. Combining newly acquired optical spectra with data from the literature, we are able to assign a redshift to 81% of the identified radio sources (37% spectroscopic). We also investigate the X-ray properties of the radio sources using the Chandra 4Ms and 250ks observations. In particular, we use a stacking technique to derive the average properties of radio objects undetected in the Chandra images. The results of our analysis are collected in a new catalog containing the position of the optical/IR counterpart, the redshift information, and the X-ray fluxes. It is the deepest multi-wavelength catalog of radio sources, which will be used for future study of this galaxy population.
## Coverage
## Spectroscopic Redshift 
 
**zsp:** [0/4.5]?=99 Spectroscopic redshift 
 

## Photometric Redshift 
 
**zph:** ?=99 Photometric redshift 
 

## Catalogue Schema

<details>
<summary>table3.dat</summary>

| Bytes   | Format   | Units     | Label       | Explanations                                       |
|:--------|:---------|:----------|:------------|:---------------------------------------------------|
| 1- 3    | I3       | ---       | RID         | Radio source identification number                 |
| 5       | I1       | h         | RAh         | [3] Radio Hour of Right Ascension (J2000)          |
| 7- 8    | I2       | min       | RAm         | [31/33] Radio Minute Right Ascension (J2000)       |
| 10- 14  | F5.2     | s         | RAs         | Radio Second of Right Ascension (J2000)            |
| 16      | A1       | ---       | DE-         | [-] Sign of the Radio Declination (J2000)          |
| 17- 18  | I2       | deg       | DEd         | [27/28] Radio Degree of Declination (J2000)        |
| 20- 21  | I2       | arcmin    | DEm         | Radio Arcminute of Declination (J2000)             |
| 23- 26  | F4.1     | arcsec    | DEs         | Radio Arcsecond of Declination (J2000)             |
| 28- 34  | F7.1     | uJy       | Sr          | [30.2/90450] Radio flux density at 1.4GHz          |
| 36- 40  | F5.1     | uJy       | e_Sr        | The 1{sigma} error in Sr                           |
| 42- 47  | F6.1     | ---       | S/N         | Signal-to-Noise                                    |
| 49      | I1       | h         | RACh        | ?=0 Counterpart Hour of Right Ascension (J2000)    |
| 51- 52  | I2       | min       | RACm        | ?=0 Counterpart Minute of Right Ascension (J2000)  |
| 54- 58  | F5.2     | s         | RACs        | ?=0 Counterpart Second of Right Ascension (J2000)  |
| 60      | A1       | ---       | DEC-        | [-] Sign of the Counterpart Declination (J2000)    |
| 61- 62  | I2       | deg       | DECd        | ?=0 Counterpart Degree of Declination (J2000)      |
| 64- 65  | I2       | arcmin    | DECm        | ?=0 Counterpart Arcminute of Declination (J2000)   |
| 67- 71  | F5.2     | arcsec    | DECs        | ?=0 Counterpart Arcsecond of Declination (J2000)   |
| 73- 77  | F5.2     | ---       | Rel         | [0.6/10]?=0 Reliability of the association (1)     |
| 79- 82  | F4.1     | arcsec    | Sep         | [0/2.3]?=99 Distance between radio and counterpart |
| 84- 95  | A12      | ---       | CCat        | Counterpart catalog (2)                            |
| 00      | =        | revisited | association | (see Section 3.4).                                 |
| 2       | and      | 3.5       | for         | further explanations.                              |

**Note**: After a careful analysis, we decided to consider as reliable only
          counterparts with reliability greater than 0.6. This threshold ensures
          that the expected number of spurious associations is below 5% for each
          auxiliary catalog. 9.00 = revisited association (see Section 3.4).
          See Sections 3.2 and 3.5 for further explanations.
Note (2): Counterpart catalog, as in table 1, as follows:
 24um-FIDEL  = Spitzer/MIPS; Dickinson & FIDEL Team (2007AAS...211.5216D)
 IRAC-SIMPLE = Spitzer/IRAC; Damen et al. (2011, Cat. J/ApJ/727/1)
 Ks-MUSYC    = CTIO 4m/ISPI; Taylor et al. (2009, Cat. J/ApJS/183/295;
               <[TFV2009] ECDFS NNNNN> for Simbad)
 Ks-ISAAC    = ESO VLT/ISAAC; Retzlaff et al. (2010, Cat. J/A+A/511/A50)
 H-SOFI      = ESO NTT/SOFI; Olsen et al. (2006, Cat. J/A+A/456/881)
 H-GNS       = HST/NICMOS; Conselice et al. (2011MNRAS.413...80C)
 z-GOODS     = HST/ACS; Dickinson et al. (2003mglh.conf..324D) and Giavalisco
               et al. (2004, Cat. II/261; <GOODS JHHMMSS.ss+DDMMSS.s> in Simbad)
 R-WFI       = ESO 2.2m/WFI; Giavalisco et al. (2004, Cat. II/261)
 v-GEMS      = HST/ACS; Rix et al. (2004ApJS..152..163R) and Caldwell et al.
               (2008ApJS..174..136C)
 U-VIMOS     = ESO VLT/VIMOS; Nonino et al. (2009ApJS..183..244N)

</details>

<details>
<summary>table5.dat</summary>

| Bytes   | Format   | Units       | Label       | Explanations                                               |
|:--------|:---------|:------------|:------------|:-----------------------------------------------------------|
| 1- 3    | I3       | ---         | RID         | Radio identification number                                |
| 5- 9    | F5.2     | mag         | Rmag        | [16.23/26.77]?=0 WFI catalog (Cat. II/261)                 |
| 11- 15  | F5.2     | mag         | e_Rmag      | ?=0 Error in Rmag                                          |
| 17- 21  | F5.2     | mag         | Kmag        | [14.73/22.62]?=0 MUSYC catalog                             |
| 23- 26  | F4.2     | mag         | e_Kmag      | ?=0 Error in Kmag                                          |
| 28- 32  | F5.2     | mag         | [3.6]       | ?=0 SIMPLE catalog (Cat. J/ApJ/727/1) 3.6 micron           |
| 34- 37  | F4.2     | mag         | e_[3.6]     | ?=0 Error in 3.6mag                                        |
| 39- 43  | F5.2     | ---         | z           | [0/6.99]?=99 Best redshift of counterpart (1)              |
| 45- 49  | F5.2     | ---         | zph         | ?=99 Photometric redshift                                  |
| 51- 55  | F5.2     | ---         | e_zph       | ?=99 Lower 68% uncertainty in zphot                        |
| 57- 61  | F5.2     | ---         | E_zph       | ?=99 Upper 68% uncertainty in zphot                        |
| 63- 68  | A6       | ---         | r_zph       | Reference for zphot (2)                                    |
| 70- 74  | F5.2     | mag         | zsp         | [0/4.5]?=99 Spectroscopic redshift                         |
| 76      | I1       | ---         | q_zsp       | ?=0 Quality flag, 3=secure (3)                             |
| 78- 82  | A5       | ---         | r_zsp       | Reference for zspec (4)                                    |
| 84- 91  | E8.2     | mW/m2       | Soft        | ? Soft X-ray (0.5-2keV) band flux; erg/s/cm^2^             |
| 93-100  | E8.2     | mW/m2       | e_Soft      | ? Error in Soft                                            |
| 102-109 | E8.2     | mW/m2       | Hard        | ? Hard X-ray (2-10keV) band flux; erg/s/cm^2^              |
| 111-118 | E8.2     | mW/m2       | e_Hard      | ? Error in Hard                                            |
| 120-123 | I4       | ---         | XID         | ? X-ray identifier (5)                                     |
| 3       | =        | secure      | redshift;   | 2 = reasonable redshift;                                   |
| 1       | =        | one         | line        | detection or tentative redshift.                           |
| 83      | GMASS    | =           | FORS2;      | Kurk et al. (2012arXiv1209.1561K)                          |
| 07      | =        | Keck        | (N=32       | zspec adopted); Silverman et al. 2010, Cat. J/ApJS/191/124 |
| 08      | =        | Keck        | (N=18       | zspec adopted); Silverman et al. 2010, Cat. J/ApJS/191/124 |
| 06      | =        | 2dF;        | Norris      | et al. (2006, Cat. J/AJ/132/2409)                          |
| 80      | =        | VIMOS;      | Silverman   | et al. 2010, Cat. J/ApJS/191/124                           |
| 81      | =        | VIMOS;      | this        | work                                                       |
| 07      | =        | VIMOS;      | Ravikumar   | et al. 2007, Cat. J/A+A/465/1099                           |
| 04      | =        | FORS1/FORS2 | (N=38       | zspec adopted); Szokoly et al. 2004,                       |
| 271     | S04F     | =           | FORS1/FORS2 | (N=1 zspec adopted); Szokoly et al. 2004,                  |
| 271     | T09      | =           | VIMOS;      | Treister et al. 2009, Cat. J/ApJ/693/1713                  |
| 124     | VLR      | =           | VIMOS-LR;   | Balestra et al. 2010, Cat. J/A+A/512/A1                    |
| 1       | VVDS     | =           | VIMOS;      | Le Fevre et al. 2004, Cat. J/A+A/428/1043                  |

**Note**: The best redshift is spectroscopic if q_zsp>=2, photometric otherwise.
Note (2): Reference as follows:
   ZEB_pz = Rafferty et al. (2011ApJ...742....3R);
   C10_pz = Cardamone et al. (2010, cat. J/ApJS/189/270);
   S09_pz = Santini et al. (2009, Cat. J/A+A/504/751);
    KM_pz = Taylor et al. (2009, Cat. J/ApJS/183/295).
Note (3): Quality flag as follows:
    3 = secure redshift;
    2 = reasonable redshift;
    1 = one line detection or tentative redshift.
Note (4): References for spectroscopic redshift, as in table 4, as follows:
  FORS  = FORS2; Vanzella et al. 2008, Cat. J/A+A/478/83
  GMASS = FORS2; Kurk et al. (2012arXiv1209.1561K)
  K07   = Keck (N=32 zspec adopted); Silverman et al. 2010, Cat. J/ApJS/191/124
  K08   = Keck (N=18 zspec adopted); Silverman et al. 2010, Cat. J/ApJS/191/124
  N06   = 2dF; Norris et al. (2006, Cat. J/AJ/132/2409)
  P80   = VIMOS; Silverman et al. 2010, Cat. J/ApJS/191/124
  P81   = VIMOS; this work
  R07   = VIMOS; Ravikumar et al. 2007, Cat. J/A+A/465/1099
  S04   = FORS1/FORS2 (N=38 zspec adopted); Szokoly et al. 2004,
          Cat. J/ApJS/155/271
  S04F  = FORS1/FORS2 (N=1 zspec adopted); Szokoly et al. 2004,
          Cat. J/ApJS/155/271
  T09   = VIMOS; Treister et al. 2009, Cat. J/ApJ/693/1713
  VJB   = VIMOS; Silverman et al. 2010, Cat. J/ApJS/191/124
  VLR   = VIMOS-LR; Balestra et al. 2010, Cat. J/A+A/512/A1
  VMR   = VIMOS-MR; Balestra et al. 2010, Cat. J/A+A/512/A1
  VVDS  = VIMOS; Le Fevre et al. 2004, Cat. J/A+A/428/1043
Note (5): Source of XID:
  * XID<1000: from Xue et al. 2011, Cat. J/ApJS/195/10;
       <[XLB2011] JHHMMSS.ss+DDMMSS.s> in Simbad.
  * XID>1000: from Lehmer et al. 2005, Cat. J/ApJS/161/21; 
       <[LBA2005] NNN> in Simbad, where "NNN" is XID-1000.

</details>
