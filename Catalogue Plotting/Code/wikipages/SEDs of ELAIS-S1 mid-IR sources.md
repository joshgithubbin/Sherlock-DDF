**Authors:** Pozzi F., Polletta M., Zamorani G., La Franca F., Sacchi N.,, Comastri A., Pozzetti L., Vignali C., Lonsdale C., Rowan-Robinson M.,, Surace J., Shupe D., Fang F., Matute I., Berta S., <Astrophys. J., 684, 136-152 (2008)>, =2008ApJ...684..136G

## Summary: SEDs of ELAIS-S1 mid-IR sources 

We present the broadband SEDs of the largest available highly complete (72%) spectroscopic sample of MIR-selected galaxies and AGNs at intermediate redshift. The sample contains 203 extragalactic sources from the 15um ELAIS-SWIRE survey, all with measured spectroscopic redshift. Most of these sources have full multiwavelength coverage from the FUV (GALEX) to the FIR (Spitzer) and lie in the redshift range 0.1<z<1.3. This large sample allows us for the first time to characterize the spectral properties of sources responsible for the strong evolution observed in the MIR. Based on SED-fitting, we have classified the MIR sources, identifying AGN signatures in about 50% of them. This fraction is significantly higher than that derived from optical spectroscopy (~29%) and is due in particular to the identification of AGN activity in objects spectroscopically classified as galaxies (the spectroscopic classification may be somewhat unreliable because of host galaxy dilution in the optical). It is likely that in most of our objects, the AGN is either obscured or low luminosity, and thus dominates the energetic output only in the MIR, showing up just in the range where the host galaxy SED has a minimum. The fraction of AGNs strongly depends on flux density, with that derived through the SED-fitting about 20% at S_15um_~0.5-1mJy and gradually increasing to 100% at S_15um_>10mJy, while that obtained from optical spectroscopy is never >30%, even at higher flux densities.
## Coverage
## Spectroscopic Redshift 
 
**zsp:** Spectroscopic redshift (6)(4) 
 

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format          | Units    | Label             | Explanations                                                                |
|:--------|:----------------|:---------|:------------------|:----------------------------------------------------------------------------|
| 1- 8    | A8              | ---      | ---               | [ELAISC15]                                                                  |
| 10- 23  | A14             | ---      | ELAISC15          | ISOCAM name (JHHMMSS+DDMMSS) (1)                                            |
| 24      | A1              | ---      | n_ELAISC15        | [a-g ] Individual notes (2)                                                 |
| 26- 30  | F5.1            | uJy      | FFUV              | ? GALEX FUV flux density (120-177nm)                                        |
| 32- 37  | F6.1            | uJy      | FNUV              | ? GALEX NUV flux density (177-300nm)                                        |
| 39- 44  | F6.1            | uJy      | FB                | ? ESIS B-band flux density                                                  |
| 46- 52  | F7.1            | uJy      | FV                | ? ESIS V-band flux density                                                  |
| 54- 60  | F7.1            | uJy      | FR                | ? R-band flux density (3)                                                   |
| 62- 67  | F6.1            | uJy      | FJ                | ? 2MASS J-band flux density                                                 |
| 69- 75  | F7.1            | uJy      | FKs               | ? 2MASS Ks-band flux density                                                |
| 77      | A1              | ---      | l_F3.6            | Limit flag on F3.6                                                          |
| 78- 84  | F7.1            | uJy      | F3.6              | ? Spitzer/IRAC 3.6um band flux density                                      |
| 86      | A1              | ---      | l_F4.5            | Limit flag on F4.5                                                          |
| 87- 91  | I5              | uJy      | F4.5              | ? Spitzer/IRAC 4.5um band flux density                                      |
| 93      | A1              | ---      | l_F5.8            | Limit flag on F5.8                                                          |
| 94- 98  | I5              | uJy      | F5.8              | ? Spitzer/IRAC 5.8um band flux density                                      |
| 100     | A1              | ---      | l_F8.0            | Limit flag on F8.0                                                          |
| 101-105 | I5              | uJy      | F8.0              | ? Spitzer/IRAC 8.0um band flux density                                      |
| 107-110 | F4.1            | mJy      | F15               | 15um band flux density from Lari et al.,                                    |
| 1173    | 112             | A1       | ---               | l_F24       Limit flag on F24                                               |
| 113-116 | F4.1            | mJy      | F24               | Spitzer/MIPS 24um band flux density                                         |
| 118     | A1              | ---      | l_F70             | Limit flag on F70                                                           |
| 119-124 | F6.1            | mJy      | F70               | Spitzer/MIPS 70um band flux density                                         |
| 126     | A1              | ---      | l_F160            | Limit flag on F160                                                          |
| 127-132 | F6.1            | mJy      | F160              | Spitzer/MIPS 160um band flux density                                        |
| 134-138 | F5.3            | ---      | zsp               | Spectroscopic redshift (6)(4)                                               |
| 140-146 | E7.3            | Lsun     | LIR               | Total infrared luminosity (5)                                               |
| 148-152 | A5              | ---      | SpCl              | Optical spectroscopy object type (6)                                        |
| 154-157 | A4              | ---      | SEDCl             | SED-fitting object type (6)                                                 |
| 15      | J003317-431706  | was      | spectroscopically | identified through Very                                                     |
| 3       | galaxy          | showing  | [OII]             | emission at                                                                 |
| 15      | J003447-432447  | was      | spectroscopically | identified through Very                                                     |
| 2       | at              | redshift | 1.076.            | c = For ELAISC15 J003915-430426, z-value of 0.013 is from the NED database. |
| 15      | J003545-431833  | we       | were              | able to measure z through a more                                            |
| 15      | J003330-431553, | which    | was               | wrongly classified as a starburst                                           |
| 1       | activity.       | f        | =                 | ELAISC15 J003603-433152, which was classified as AGN2, showed a broad       |
| 1       | activity.       | g        | =                 | ELAISC15 J003622-432826, which was classified as a starburst galaxy,        |
| 2       | activity.       | Note     | (3):              | In the area not covered by ESIS (Berta et al. 2006,                         |
| 1       | sources         | were     | carried           | out at the AAT 2dF, ESO Danish 1.5 and                                      |

**Note**: Source name from Lari et al. (2001, Cat. J/MNRAS/325/1173). This
          sample, complete at the 5{sigma} level, is the only ISOCAM sample
          covering the whole flux density range 0.5-150mJy.
Note (2): Flag as follows:
    a = ELAISC15 J003317-431706 was spectroscopically identified through Very
        Large Telescope (VLT) VIMOS observations (La Franca et al.,
        2007A&A...472..797L) and is a R=24.3 galaxy showing [OII] emission at
        redshift 0.689.
    b = ELAISC15 J003447-432447 was spectroscopically identified through Very
        Large Telescope (VLT) VIMOS observations (La Franca et al.,
        2007A&A...472..797L) and is an AGN2 at redshift 1.076.
    c = For ELAISC15 J003915-430426, z-value of 0.013 is from the NED database.
    d = For ELAISC15 J003545-431833 we were able to measure z through a more
        accurate reduction of the spectrum.
    e = ELAISC15 J003330-431553, which was wrongly classified as a starburst
        galaxy at z=0.473, showed broad CIII and MgII emission at z=2.170,
        typical of AGN1 activity.
    f = ELAISC15 J003603-433152, which was classified as AGN2, showed a broad
        MgII emission typical of AGN1 activity.
    g = ELAISC15 J003622-432826, which was classified as a starburst galaxy,
        showed a clear [OIII]/H{beta} ratio typical of AGN2 activity.
Note (3): In the area not covered by ESIS (Berta et al. 2006,
          Cat. J/A+A/451/881), R magnitudes are from the La Franca et
          al. catalog (2004, Cat. J/AJ/127/3075).
Note (4): Three sources with previously poor-quality spectra had their
          spectroscopic classification changed after being reobserved with VIMOS
          at ESO VLT (La Franca et al., 2007A&A...472..797L). See flags e to g
          in column f_ELAISC15.
Note (5): Total infrared luminosity; obtained by integrating the best-fitting
          SED in the range 8-1000um.
Note (6): Spectroscopic observations of the optical counterparts of the
     ISOCAM S1 sources were carried out at the AAT 2dF, ESO Danish 1.5 and
     3.6m telescopes, and the New Technology Telescope (NTT) (La Franca et
     al. 2004, Cat. J/AJ/127/3075).
     The Objects classes are AGN1, AGN2, GAL, ULIG, STB (starburst galaxy), 
     LINER or UNCL (unclassified).

</details>
