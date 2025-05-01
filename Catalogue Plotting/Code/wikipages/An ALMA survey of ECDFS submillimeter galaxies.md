**Authors:** Swinbank A.M., Smail I., Alexander D.M., Brandt W.N.,, Bertoldi F., de Breuck C., Chapman S.C., Coppin K.E.K., da Cunha E.,, Danielson A.L.R., Dannerbauer H., Greve T.R., Hodge J.A., Ivison R.J.,, Karim A., Knudsen K.K., Poggianti B.M., Schinnerer E., Thomson A.P.,, Walter F., Wardlow J.L., Weiss A., van der Werf P.P., <Astrophys. J., 788, 125 (2014)>, =2014ApJ...788..125S (SIMBAD/NED BibCode)

## Summary: An ALMA survey of ECDFS submillimeter galaxies 

We present the first photometric redshift distribution for a large sample of 870 {mu}m submillimeter galaxies (SMGs) with robust identifications based on observations with ALMA. In our analysis we consider 96 SMGs in the Extended Chandra Deep Field South, 77 of which have 4-19 band photometry. We model the SEDs for these 77 SMGs, deriving a median photometric redshift of z_phot_=2.3+/-0.1. The remaining 19 SMGs have insufficient photometry to derive photometric redshifts, but a stacking analysis of Herschel observations confirms they are not spurious. Assuming that these SMGs have an absolute H-band magnitude distribution comparable to that of a complete sample of z~1-2 SMGs, we demonstrate that they lie at slightly higher redshifts, raising the median redshift for SMGs to z_phot_=2.5+/-0.2. Critically we show that the proportion of galaxies undergoing an SMG-like phase at z>=3 is at most 35%+/-5% of the total population. We derive a median stellar mass of M_*_=(8+/-1)x10^10^ M_{sun}_, although there are systematic uncertainties of up to 5x for individual sources. Assuming that the star formation activity in SMGs has a timescale of ~100 Myr, we show that their descendants at z~0 would have a space density and M_H_ distribution that are in good agreement with those of local ellipticals. In addition, the inferred mass-weighted ages of the local ellipticals broadly agree with the look-back times of the SMG events. Taken together, these results are consistent with a simple model that identifies SMGs as events that form most of the stars seen in the majority of luminous elliptical galaxies at the present day.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-788-125/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zspec:** ? Spectroscopic redshift 
 

## Photometric Redshift 
 
**zphot:** Photometric redshift 
 

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                       |
|:--------|:---------|:--------|:--------|:-----------------------------------|
| 1- 19   | A19      | ---     | Filter  | Filter used in the observation     |
| 21- 24  | F4.2     | um      | lambda  | Effective wavelength               |
| 26- 29  | F4.1     | ---     | Limit   | 3{sigma} detection limit in AB mag |
| 31- 48  | A18      | ---     | r_Limit | Detection limit reference          |
| 50- 68  | A19      | ---     | Bibcode | Reference bibcode                  |
| 70- 83  | A14      | ---     | Cat     | Catalog reference in VizieR        |
| 85- 98  | A14      | ---     | Com     | Comment on reference               |
</details>

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units   | Label    | Explanations                                     |
|:--------|:---------|:--------|:---------|:-------------------------------------------------|
| 1- 5    | A5       | ---     | ---      | [ALESS]                                          |
| 7- 11   | A5       | ---     | ALESS    | SMG identifier (NN.NN; NNN.N) (1)                |
| 13      | A1       | ---     | f_ALESS  | [a] Flag on ALESS (2)                            |
| 15      | A1       | ---     | l_UMmag  | [>] The 3{sigma} upper limit on UMmag            |
| 17- 21  | F5.2     | mag     | UMmag    | ? MUSYC U band magnitude                         |
| 23- 26  | F4.2     | mag     | e_UMmag  | ? Uncertainty in UMmag                           |
| 28      | A1       | ---     | l_U38mag | [>] The 3{sigma} upper limit on U38mag           |
| 30- 34  | F5.2     | mag     | U38mag   | ? MUSYC U38 band magnitude                       |
| 36- 39  | F4.2     | mag     | e_U38mag | ? Uncertainty in U38mag                          |
| 41      | A1       | ---     | l_UVmag  | [>] The 3{sigma} upper limit on UVmag            |
| 43- 47  | F5.2     | mag     | UVmag    | ? VIMOS U band magnitude                         |
| 49- 52  | F4.2     | mag     | e_UVmag  | ? Uncertainty in UVmag                           |
| 54      | A1       | ---     | l_Bmag   | [>] The 3{sigma} upper limit on Bmag             |
| 56- 60  | F5.2     | mag     | Bmag     | ? MUSYC WFI B band magnitude                     |
| 62- 65  | F4.2     | mag     | e_Bmag   | ? Uncertainty in Bmag                            |
| 67      | A1       | ---     | l_Vmag   | [>] The 3{sigma} upper limit on Vmag             |
| 69- 73  | F5.2     | mag     | Vmag     | ? MUSYC WFI V band magnitude                     |
| 75- 78  | F4.2     | mag     | e_Vmag   | ? Uncertainty in Vmag                            |
| 80      | A1       | ---     | l_Rmag   | [>] The 3{sigma} upper limit on Rmag             |
| 82- 86  | F5.2     | mag     | Rmag     | ? MUSYC WFI R band magnitude                     |
| 88- 91  | F4.2     | mag     | e_Rmag   | ? Uncertainty in Rmag                            |
| 93      | A1       | ---     | l_Imag   | [>] The 3{sigma} upper limit on Imag             |
| 95- 99  | F5.2     | mag     | Imag     | ? MUSYC WFI I band magnitude                     |
| 101-104 | F4.2     | mag     | e_Imag   | ? Uncertainty in Imag                            |
| 106     | A1       | ---     | l_zmag   | [>] The 3{sigma} upper limit on zmag             |
| 108-112 | F5.2     | mag     | zmag     | ? MUSYC Mosaic-II z band magnitude               |
| 114-117 | F4.2     | mag     | e_zmag   | ? Uncertainty in zmag                            |
| 119     | A1       | ---     | l_Jmag   | [>] The 3{sigma} upper limit on Jmag             |
| 121-125 | F5.2     | mag     | Jmag     | ? J band magnitude (TENIS if nothing in f_Ksmag) |
| 127-130 | F4.2     | mag     | e_Jmag   | ? Uncertainty in Jmag                            |
| 132-133 | A2       | ---     | f_Jmag   | Flag on Jmag (4)                                 |
| 135     | A1       | ---     | l_Hmag   | [>] The 3{sigma} upper limit on Hmag             |
| 137-141 | F5.2     | mag     | Hmag     | ? H band magnitude                               |
| 143-146 | F4.2     | mag     | e_Hmag   | ? Uncertainty in Hmag                            |
| 148     | A1       | ---     | l_Ksmag  | [>] The 3{sigma} upper limit on Ksmag            |
| 150-154 | F5.2     | mag     | Ksmag    | ? K_S_ band magnitude (TENIS if nothing          |
| 156-159 | F4.2     | mag     | e_Ksmag  | ? Uncertainty in Ksmag                           |
| 161-162 | A2       | ---     | f_Ksmag  | [* **] Flag on Ksmag and Jmag (4)                |
| 164     | A1       | ---     | l_3.6mag | [>] The 3{sigma} upper limit on 3.6mag           |
| 166-170 | F5.2     | mag     | 3.6mag   | SIMPLE/IRAC 3.6 micron band magnitude            |
| 172-175 | F4.2     | mag     | e_3.6mag | ? Uncertainty in 3.6mag                          |
| 177     | A1       | ---     | l_4.5mag | [>] The 3{sigma} upper limit on 4.5mag           |
| 179-183 | F5.2     | mag     | 4.5mag   | SIMPLE/IRAC 4.5 micron band magnitude            |
| 185-188 | F4.2     | mag     | e_4.5mag | ? Uncertainty in 4.5mag                          |
| 190     | A1       | ---     | l_5.8mag | [>] The 3{sigma} upper limit on 5.8mag           |
| 192-196 | F5.2     | mag     | 5.8mag   | ? SIMPLE/IRAC 5.8 micron band magnitude          |
| 198-201 | F4.2     | mag     | e_5.8mag | ? Uncertainty in 5.8mag                          |
| 203     | A1       | ---     | l_8.0mag | [>] The 3{sigma} upper limit on 8.0mag           |
| 205-209 | F5.2     | mag     | 8.0mag   | ? SIMPLE/IRAC 8.0 micron band magnitude          |
| 211-214 | F4.2     | mag     | e_8.0mag | ? Uncertainty in 8.0mag                          |
| 6       | micron   | source  | of       | comparable, or greater,                          |

**Note**: All photometry is left blank where a source is not covered by
  available imaging.
Note (2): Flag as follows:
  a = Source is within 4" of a 3.6 micron source of comparable, or greater,
      flux.
Note (3): We measure J and K_S_ photometry from three imaging surveys, but quote
  a single value, in order of 3{sigma} detection limit (see Table 1).
Note (4): Flag as follows:
   * = Photometry measured from HAWK-I imaging;
  ** = Photometry measured from MUSYC imaging,
       otherwise photometry measured from TENIS imaging.

</details>

<details>
<summary>table3.dat</summary>

| Bytes   | Format   | Units     | Label   | Explanations                      |
|:--------|:---------|:----------|:--------|:----------------------------------|
| 1- 5    | A5       | ---       | ---     | [ALESS]                           |
| 7- 12   | A6       | ---       | ALESS   | SMG identifier (NNN.NN)           |
| 14      | A1       | ---       | f_ALESS | [a] Flag on ALESS (1)             |
| 16- 17  | I2       | h         | RAh     | Hour of Right Ascension (J2000)   |
| 19- 20  | I2       | min       | RAm     | Minute of Right Ascension (J2000) |
| 22- 26  | F5.2     | s         | RAs     | Second of Right Ascension (J2000) |
| 28      | A1       | ---       | DE-     | Sign of the Declination (J2000)   |
| 29- 30  | I2       | deg       | DEd     | Degree of Declination (J2000)     |
| 32- 33  | I2       | arcmin    | DEm     | Arcminute of Declination (J2000)  |
| 35- 38  | F4.1     | arcsec    | DEs     | Arcsecond of Declination (J2000)  |
| 40- 43  | F4.2     | ---       | zphot   | Photometric redshift              |
| 45- 48  | F4.2     | ---       | E_zphot | Upper limit uncertainty in zphot  |
| 50- 53  | F4.2     | ---       | e_zphot | Lower limit uncertainty in zphot  |
| 55- 58  | F4.2     | ---       | zspec   | ? Spectroscopic redshift          |
| 60      | A1       | ---       | r_zspec | zspec reference (2)               |
| 62- 66  | F5.2     | ---       | Chi2    | Reduced {Chi}^2^                  |
| 68- 69  | I2       | ---       | Detec   | Number of detection               |
| 71- 72  | I2       | ---       | Obs     | Number of observation             |
| 74- 79  | F6.2     | mag       | HMag    | Absolute H band AB magnitude      |
| 81- 84  | F4.2     | Msun/Lsun | M/L     | H band mass-to-light ratio        |
| 1       | these    | SMGs      | are     | potential gravitational           |

**Note**: Flag as follows:
  a = As discussed in Section 3.2.1 these SMGs are potential gravitational
      lenses, or have significantly contaminated photometry. We advise that the
      photometric redshifts for these SMGs are treated with extreme caution.
Note (2): Reference as follows:
  b = Casey et al. (2011MNRAS.411.2739C);
  c = Zheng et al. (2004, J/ApJS/155/73);
  d = Swinbank et al. (2012MNRAS.427.1066S);
  e = Silverman et al. (2010, J/ApJS/191/124);
  f = Kriek et al. (2008ApJ...677..219K);
  g = Coppin et al. (2009MNRAS.395.1905C);
  h = Coppin et al. (2012MNRAS.427..520C); Danielson et al. in prep;
  i = Bonzini et al. (2012, J/ApJS/203/15).

</details>
