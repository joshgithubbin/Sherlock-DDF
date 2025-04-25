## Summary

We present the optical and infrared identifications of the 266 radio sources detected at 20cm with the Very Large Array in the Chandra Deep Field-South. Using deep i-band Advanced Camera for Surveys, R-band Wide Field Imager, K-band SOFI NTT, K-band ISAAC VLT and Spitzer imaging data, we are able to find reliable counterparts for 254 (~95%) VLA sources. Twelve radio sources remain unidentified, and three of them are "empty fields". Using literature and our own data we are able to assign redshifts to 186 (~70%) radio sources: 108 are spectroscopic redshifts and 78 are reliable photometric redshifts. Based on the rest-frame colors and morphological distributions of the host galaxies, we find evidences for a change in the submillijansky radio source population: (1) above ~0.08mJy early-type galaxies are dominating and (2) at flux densities below ~0.08mJy, starburst galaxies become dominant.

## Catalogue Schema

<details>
<summary>table[34].dat catalogue schema</summary>

| Bytes   | Format   | Units          | Label    | Explanations                                        |
|:--------|:---------|:---------------|:---------|:----------------------------------------------------|
| 1- 3    | I3       | ---            | Seq      | Running identification number                       |
| 4       | A1       | ---            | m_Seq    | [AB] Multiplicity index (for source 178)            |
| 6       | I1       | h              | RAh      | Radio Hour of Right Ascension (J2000)               |
| 8- 9    | I2       | min            | RAm      | Radio Minute of Right Ascension (J2000)             |
| 11- 15  | F5.2     | s              | RAs      | Radio Second of Right Ascension (J2000)             |
| 17      | A1       | ---            | DE-      | Sign of the Radio Declination (J2000)               |
| 18- 19  | I2       | deg            | DEd      | Radio Degree of Declination (J2000)                 |
| 21- 22  | I2       | arcmin         | DEm      | Radio Arcminute of Declination (J2000)              |
| 24- 27  | F4.1     | arcsec         | DEs      | Radio Arcsecond of Declination (J2000)              |
| 29      | I1       | h              | RAOh     | ? Optical Hour of Right Ascension (J2000) (1)       |
| 31- 32  | I2       | min            | RAOm     | ? Optical Minute of Right Ascension (J2000) (1)     |
| 34- 38  | F5.2     | s              | RAOs     | ? Optical Second of Right Ascension (J2000) (1)     |
| 40      | A1       | ---            | DEO-     | Sign of the Optical Declination (J2000)(1)          |
| 41- 42  | I2       | deg            | DEOd     | ? Optical Degree of Declination (J2000) (1)         |
| 44- 45  | I2       | arcmin         | DEOm     | ? Optical Arcminute of Declination (J2000) (1)      |
| 47- 50  | F4.1     | arcsec         | DEOs     | ? Optical Arcsecond of Declination (J2000) (1)      |
| 52- 54  | F3.1     | arcsec         | Sep      | ? Separation between Radio and Optical positions    |
| 55      | A1       | ---            | ---      | [0]                                                 |
| 57- 63  | F7.2     | ---            | LR       | ? Likelihood ratio (2)                              |
| 65- 68  | F4.2     | ---            | Rel      | ? Reliability parameter (3)                         |
| 70- 76  | A7       | ---            | Cat      | Catalog counterpart selected from (4)               |
| 78      | A1       | ---            | l_Rmag   | Limit flag on Rmag                                  |
| 79- 83  | F5.2     | mag            | Rmag     | ? R-band AB magnitude                               |
| 85- 88  | F4.2     | mag            | e_Rmag   | ? Uncertainty in Rmag                               |
| 90      | A1       | ---            | f_Rmag   | [S] Flag on Rmag (only for table3) (5)              |
| 92      | A1       | ---            | l_Kmag   | Limit flag on Kmag                                  |
| 93- 97  | F5.2     | mag            | Kmag     | ? K-band AB magnitude                               |
| 99-102  | F4.2     | mag            | e_Kmag   | ? Uncertainty in Kmag                               |
| 104-108 | F5.3     | ---            | zsp      | ? Spectroscopic redshift of counterpart             |
| 109     | A1       | ---            | r_zsp    | [a-g] zsp reference (6)                             |
| 111     | I1       | ---            | q_zsp    | [1/2]? Quality flag for zsp (2=secure) (7)          |
| 113-116 | F4.2     | ---            | zph      | ? Photometric redshift of counterpart               |
| 118-122 | F5.3     | ---            | e_zph    | ? Uncertainty in zph                                |
| 124-125 | A2       | ---            | r_zph    | Origin and note on zph (only for table3) (8)        |
| 3       | for      | further        | details. | Note (4): Catalog as follows:                       |
| 2005    | (Cat.    | J/A+A/434/53), | 2006     | (Cat. J/A+A/454/423), 2008 (Cat. J/A+A/478/83). The |
| 2       | =        | secure         | redshift | (multiple spectral features);                       |
| 1       | =        | tentative      | redshift | (e.g. based on a single emission line).             |
| 1       | =        | Photometric    | redshift | from Wolf et al. (2004, Cat. II/253,                |
| 2       | =        | Photometric    | redshift | from Grazian et al. (2006, Cat. J/A+A/449/951,      |
| 3       | =        | Photometric    | redshift | from Zheng et al. (2004, Cat. J/ApJS/155/73,        |

**Note**: Of the primary counterpart. The positional error is 0.05".
Note (2): LR=(q(m)f(r))/n(m) where q(m) is the expected probability
     distribution as a function of magnitude of the true counterparts, f(r)
     is the probability distribution of the positional errors, and n(m) is
     the surface density as a function of magnitude of background objects.
Note (3): The reliability of a particular source j to be the true
     counterpart is given by R_j_=LR_j_/({Sigma}_i_LR_i_+(1-Q)') where i
     runs over the set of all candidate counterparts for that particular
     radio source, and Q is the probability that the counterpart of the
     source is above the magnitude limit of the optical/NIR catalog. See
     section 3 for further details.
Note (4): Catalog as follows:
    ACS-i = i band catalog from ACS/GOODS;
    WFI-R = R band catalog from WFI;
  ISAAC-K = K band catalog from ISAAC;
   SOFI-K = K band catalog from SOFI;
     GEMS = z band catalog from ACS/GEMS;
  SPITZER = IRAC and MIPS images.
Note (5):
    S = The optical photometry could be contaminated by a close-by bright star.
Note (6): Flag as follows:
    a = Spectroscopic redshift from Szokoly et al. (2004, Cat. J/ApJS/155/271,
        <[SBH2004] JHHMMSS.ss+DDMMSS.s> in Simbad). The average redshift
        uncertainty is {Delta}z=0.005.
    b = Spectroscopic redshift from Silvermann et al., in preparation.
    c = Spectroscopic redshift from Vanzella et al. 2005 (Cat. J/A+A/434/53),
        2006 (Cat. J/A+A/454/423), 2008 (Cat. J/A+A/478/83). The
        average redshift uncertainty is {Delta}z=0.00055.
    d = Spectroscopic redshift from Popesso et al. (2009A&A...494..443P).
    e = Spectroscopic redshift from Le Fevre (2004, Cat. J/A+A/428/1043,
        <VCDFS NNNNNN> in Simbad). The average redshift uncertainty is
        {Delta}z=0.0012.
    f = Spectroscopic redshift from Mignoli et al. (2005, Cat. J/A+A/437/883).
    g = Spectroscopic redshift from Ravikumar et al. (2007,
        Cat. J/A+A/465/1099, <[RPF2007] EIS JHHMMSS.ss+DDMMSS.s> in Simbad).
Note (7): Quality flag as follows:
    2 = secure redshift (multiple spectral features);
    1 = tentative redshift (e.g. based on a single emission line).
Note (8): Flag as follows:
    1 = Photometric redshift from Wolf et al. (2004, Cat. II/253,
        <[WDK2001] NNNNN> or <COMBO JHHMMSSs+DDMMSS> in Simbad)).
    2 = Photometric redshift from Grazian et al. (2006, Cat. J/A+A/449/951,
        <GOODS-MUSIC NNNNN> in Simbad).
    3 = Photometric redshift from Zheng et al. (2004, Cat. J/ApJS/155/73,
        <[GZW2002] XID NNN> in Simbad).
    * = The optical photometry could be contaminated by a close-by
        (~1.3") source.

</details>
