**Authors:** Fontana A., De Santis C., Nonino M., Salimbeni S., Giallongo E.,, Cristiani S., Gallozzi S., Vanzella E., <Astron. Astrophys. 449, 951 (2006)>, =2006A&A...449..951G

## Summary: GOODS-MUSIC sample: multicolour catalog 

We present a high quality multiwavelength (from 0.3 to 8.0 micron) catalog of the large and deep area in the GOODS Southern Field covered by the deep near-IR observations obtained with the ESO VLT. The catalog is entirely based on public data: in our analysis, we have included the F435W, F606W, F775W and F850LP ACS images, the JHKs VLT data, the Spitzer data provided by IRAC instrument (3.6, 4.5, 5.8 and 8.0 micron), and publicly available U-band data from the 2.2ESO and VLT-VIMOS. We describe in detail the procedures adopted to obtain this multiwavelength catalog. In particular, we developed a specific software for the accurate "PSF-matching" of space and ground-based images of different resolution and depth (ConvPhot), of which we analyse performances and limitations. We have included both z-selected, as well as Ks-selected objects, yielding a unique, self-consistent catalog. The largest fraction of the sample is 90% complete at z~26 or Ks~23.8 (AB scale). Finally, we cross-correlated our data with all the spectroscopic catalogs available to date, assigning a spectroscopic redshift to more than 1000 sources. The final catalog is made up of 14847 objects, at least 72 of which are known stars, 68 are AGNs, and 928 galaxies with spectroscopic redshift (668 galaxies with reliable redshift determination). We applied our photometric redshift code to this data set, and the comparison with the spectroscopic sample shows that the quality of the resulting photometric redshifts is excellent, with an average scatter of only 0.06. The full catalog, which we named GOODS-MUSIC (MUltiwavelength Southern Infrared Catalog), including the spectroscopic information, is made publicly available, together with the software specifically designed to this end.

## Spectroscopic Redshift 
 
**zspec:**  
 

## Photometric Redshift 
 
**zphot:**  
 

## Catalogue Schema

<details>
<summary>table5.dat</summary>

| Bytes   | Format   | Units     | Label       | Explanations                                                  |
|:--------|:---------|:----------|:------------|:--------------------------------------------------------------|
| 1- 5    | I5       | ---       | Seq         | Identification number                                         |
| 7- 15   | F9.6     | deg       | RAdeg       | Right ascension, in decimal degrees (J2000)                   |
| 17- 26  | F10.6    | deg       | DEdeg       | Declination, in decimal degrees (J2000)                       |
| 28- 33  | F6.3     | ---       | zspec       | ?=-1.0 Spectroscopic Redshift                                 |
| 35- 43  | A9       | ---       | SpClass     | Spectroscopic class (1)                                       |
| 45- 54  | A10      | ---       | r_SpClass   | Spectroscopic Catalog (2)                                     |
| 56- 57  | I2       | ---       | q_zspec     | ?=99 Quality of Spectroscopic Redshift (3)                    |
| 59- 64  | F6.3     | ---       | zphot       | ?=-1.0 Photometric redshift                                   |
| 66      | I1       | ---       | POS         | Position flag (4)                                             |
| 68      | I1       | ---       | star        | Star flag (5)                                                 |
| 70      | I1       | ---       | AGN         | AGN flag (6)                                                  |
| 72- 77  | F6.3     | ---       | zlim        | z band magnitude limit (7)                                    |
| 79- 84  | F6.3     | mag       | kslim       | Ks band magnitude limit (8)                                   |
| 86- 90  | F5.3     | ---       | S/G         | Star-galaxy classifier of SExtractor                          |
| 0       | for      | galaxy,   | 1           | for star)                                                     |
| 0       | =        | Vanzella  | et          | al., 2005, Cat. <J/A+A/434/53>                                |
| 20      | =        | Mignoli   | et          | al., 2005, Cat. <J/A+A/437/883>                               |
| 17      | =        | Wolf      | et          | al., 2004A&A...421..913W, Cat. <II/253>                       |
| 0       | =        | very      | good        | 1 = good                                                      |
| 2       | =        | uncertain | 3           | = bad quality                                                 |
| 99      | =        | not       | available   | Note (4): Position flag  as follows:                          |
| 1       | =        | inside    | GOODS-MUSIC | area                                                          |
| 0       | =        | outside   | GOODS-MUSIC | area                                                          |
| 1       | =        | probable  | star        | 0 = no star (A galaxy should have star flag=0 and AGN flag=0) |
| 1       | =        | probable  | AGN         | 0 = no AGN (A galaxy should have star flag=0 and AGN flag=0)  |

**Note**: Spectroscopic classification as follows:
      GALAXY = galaxy
       EARLY = early-type galaxy
    EMISSION = late-type galaxy
   COMPOSITE = early+late type galaxy
         AGN = Active Galactic Nucleus
        STAR = star
     UNKNOWN = spectrum not available
Note (2): Reference spectroscopic catalog as follows:
   GOODSV1.0 = Vanzella et al., 2005, Cat. <J/A+A/434/53>
         K20 = Mignoli et al., 2005, Cat. <J/A+A/437/883>
    CXO-CDFS = Szokoly et al., 2004, Cat. <J/ApJS/155/271>
        VVDS = Le Fevre et al., 2004A&A...428..1043L
      MASTER = http://www.eso.org/science/goods/spectroscopy/CDFS_Mastercat/
       LCIRS = Doherty et al., 2005MNRAS.361..525D
    COMBO-17 = Wolf et al., 2004A&A...421..913W, Cat. <II/253>
       DADDI = Daddi et al., 2005ApJ...626..680D
         SIC = Cristiani et al., 2000A&A...359..489C
     UNKNOWN = spectrum not available.
Note (3): Quality of spectroscopic redshift as follows:
      0 = very good
      1 = good
      2 = uncertain
      3 = bad quality
     99 = not available
Note (4): Position flag  as follows:
      1 = inside  GOODS-MUSIC area
      0 = outside GOODS-MUSIC area
Note (5): Star flag on the basis of spectroscopy, morphology, 
          and BzK colours as follows:
      1 = probable star
      0 = no star (A galaxy should have star flag=0 and AGN flag=0)
Note (6): AGN flag, based only on spectroscopy, as follows:
      1 = probable AGN
      0 = no AGN (A galaxy should have star flag=0 and AGN flag=0)
Note (7): Magnitude limit in the z band in 1arcsec^2^ and at S/N=1.
Note (8): Magnitude limit in the Ks band in 1arcsec^2^ and at S/N=1.

</details>

<details>
<summary>table6.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                     |
|:--------|:---------|:--------|:----------|:-------------------------------------------------|
| 1- 5    | I5       | ---     | Seq       | Identification number                            |
| 7       | A1       | ---     | l_U35mag  | Limit flag on U35mag                             |
| 8- 13   | F6.3     | mag     | U35mag    | ?=99.000 U35 magnitude, in AB photometric system |
| 15      | A1       | ---     | l_U38mag  | Limit flag on U38mag                             |
| 16- 21  | F6.3     | mag     | U38mag    | ?=99.000 U38 magnitude, in AB photometric system |
| 23      | A1       | ---     | l_UVIMmag | Limit flag on UVIMmag                            |
| 24- 29  | F6.3     | mag     | UVIMmag   | ?=99.000 U-VIMOS magnitude, in AB                |
| 31      | A1       | ---     | l_Bmag    | Limit flag on Bmag                               |
| 32- 37  | F6.3     | mag     | Bmag      | ?=99.000 B magnitude, in AB photometric system   |
| 39      | A1       | ---     | l_Vmag    | Limit flag on Vmag                               |
| 40- 45  | F6.3     | mag     | Vmag      | ?=99.000 V magnitude, in AB photometric system   |
| 47      | A1       | ---     | l_imag    | Limit flag on imag                               |
| 48- 53  | F6.3     | mag     | imag      | ?=99.000 i magnitude, in AB photometric system   |
| 55      | A1       | ---     | l_zmag    | Limit flag on zmag                               |
| 56- 61  | F6.3     | mag     | zmag      | ?=99.000 z magnitude, in AB photometric system   |
| 63- 68  | F6.3     | mag     | e_U35mag  | ?=99.000 U35 magnitude error                     |
| 70- 75  | F6.3     | mag     | e_U38mag  | ?=99.000 U38 magnitude error                     |
| 77- 82  | F6.3     | mag     | e_UVIMmag | ?=99.000 U-VIMOS magnitude error                 |
| 84- 89  | F6.3     | mag     | e_Bmag    | ?=99.000 B magnitude error                       |
| 91- 96  | F6.3     | mag     | e_Vmag    | ?=99.000 V magnitude error                       |
| 98-103  | F6.3     | mag     | e_imag    | ?=99.000 i magnitude error                       |
| 105-110 | F6.3     | mag     | e_zmag    | ?=99.000 z magnitude error                       |
</details>

<details>
<summary>table7.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                    |
|:--------|:---------|:--------|:----------|:------------------------------------------------|
| 1- 5    | I5       | ---     | Seq       | Identification number                           |
| 7       | A1       | ---     | l_Jmag    | Limit flag on Jmag                              |
| 8- 13   | F6.3     | mag     | Jmag      | ?=99.000 J magnitude, in AB photometric system  |
| 15      | A1       | ---     | l_Hmag    | Limit flag on Hmag                              |
| 16- 21  | F6.3     | mag     | Hmag      | ?=99.000 H magnitude, in AB photometric system  |
| 23      | A1       | ---     | l_Ksmag   | Limit flag on Ksmag                             |
| 24- 29  | F6.3     | mag     | Ksmag     | ?=99.000 Ks magnitude, in AB photometric system |
| 31      | A1       | ---     | l_IR36mag | Limit flag on IR36mag                           |
| 32- 37  | F6.3     | mag     | IR36mag   | ?=99.000 IRAC 3.6{mu}m magnitude,               |
| 39      | A1       | ---     | l_IR45mag | Limit flag on IR45mag                           |
| 40- 45  | F6.3     | mag     | IR45mag   | ?=99.000 IRAC 4.5{mu}m magnitude,               |
| 47      | A1       | ---     | l_IR58mag | Limit flag on IR58mag                           |
| 48- 53  | F6.3     | mag     | IR58mag   | ?=99.000 IRAC 5.8{mu}m magnitude,               |
| 55      | A1       | ---     | l_IR80mag | Limit flag on IR80mag                           |
| 56- 61  | F6.3     | mag     | IR80mag   | ?=99.000 IRAC 8.0{mu}m magnitude,               |
| 63- 68  | F6.3     | mag     | e_Jmag    | ?=99.000 J magnitude error                      |
| 70- 75  | F6.3     | mag     | e_Hmag    | ?=99.000 H magnitude error                      |
| 77- 82  | F6.3     | mag     | e_Ksmag   | ?=99.000 Ks magnitude error                     |
| 84- 89  | F6.3     | mag     | e_IR36mag | ?=99.000 IRAC 3.6 micron magnitude error        |
| 91- 96  | F6.3     | mag     | e_IR45mag | ?=99.000 IRAC 4.5 micron magnitude error        |
| 98-103  | F6.3     | mag     | e_IR58mag | ?=99.000 IRAC 5.8 micron magnitude error        |
| 105-110 | F6.3     | mag     | e_IR80mag | ?=99.000 IRAC 8.0 micron magnitude error        |
</details>
