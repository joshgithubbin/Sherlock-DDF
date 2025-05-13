**Authors:** Franx M., Van Dokkum P.G., Quadri R.F., Gawiser E., Bell E.F.,, Barrientos L.F., Blanc G.A., Castander F.J., Damen M., Gonzalez-Perez V.,, Hall P.B., Herrera D., Hildebrandt H., Kriek M., Labbe I., Lira P.,, Maza J., Rudnick G., Treister E., Urry C.M., Willis J.P., Wuyts S., <Astrophys. J. Suppl. Ser., 183, 295-319 (2009)>, =2009ApJS..183..295T

## Summary: A K-selected catalog of the ECDFS from MUSYC 

We present a new, K-selected, optical-to-near infrared photometric catalog of the Extended Chandra Deep Field South (ECDFS), making it publicly available to the astronomical community. The data set is founded on publicly available imaging, supplemented by original z'JK imaging data collected as part of the MUltiwavelength Survey by Yale-Chile (MUSYC). The final photometric catalog consists of photometry derived from UU_38_BVRIz'JK imaging covering the full 1/2x1/2{deg} of the ECDFS, plus H-band photometry for approximately 80% of the field. The 5{sigma} flux limit for point sources is K^(AB)^_tot_=22.0. This is also the nominal completeness and reliability limit of the catalog: the empirical completeness for 21.75<K<22.00 is >~85%. We have verified the quality of the catalog through both internal consistency checks, and comparisons to other existing and publicly available catalogs. As well as the photometric catalog, we also present catalogs of photometric redshifts and rest-frame photometry derived from the 10-band photometry. We have collected robust spectroscopic redshift determinations from published sources for 1966 galaxies in the catalog. Based on these sources, we have achieved a (1{sigma}) photometric redshift accuracy of {Delta}z/(1+z)=0.036, with an outlier fraction of 7.8%. Most of these outliers are X-ray sources. Finally, we describe and release a utility for interpolating rest-frame photometry from observed spectral energy distributions, dubbed InterRest available via http://www.strw.leidenuniv.nl/~ent/InterRest
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-183-295/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zs:**  
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-183-295/Subcatalogues/ECDFS/Plots/zspec.png)
<details>
<summary>Quality flag . . .

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-183-295/Subcatalogues/ECDFS/Plots/q_zspec.png)</summary>
## Photometric Redshift 
 
**RFGz:** ?=-99.000 Rest-frame photometry for 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-183-295/Subcatalogues/ECDFS/Plots/zphot.png)
## Catalogue Schema

<details>
<summary>photcat.dat</summary>

| Bytes   | Format   | Units    | Label   | Explanations                                            |
|:--------|:---------|:---------|:--------|:--------------------------------------------------------|
| 1- 5    | I5       | ---      | Seq     | [1,16910]+ Object identifier number                     |
| 7- 16   | F10.7    | deg      | RAdeg   | [52.8547,53.432] Right ascension in degrees             |
| 18- 28  | F11.7    | deg      | DEdeg   | [-28.0668,-27.5507] Declination in degrees              |
| 30      | I1       | ---      | Field   | [8] Internal MUSYC field identifier (ECDFS=8)           |
| 32- 39  | F8.3     | pix      | Xpix    | X center of light position                              |
| 41- 48  | F8.3     | pix      | Ypix    | Y center of light position                              |
| 50- 54  | F5.2     | arcsec   | diam1   | [2.5,78.23] Effective diameter (1)                      |
| 56- 67  | E12.6    | 0.363mJy | FU      | [-0.384,32365.4] Observed flux in U-band (2)            |
| 69- 77  | E9.4     | 0.363mJy | e_FU    | [0.04957,3.294] FU measurement uncertainty              |
| 79- 90  | E12.6    | 0.363mJy | FU38    | [-0.681,35010] Observed flux in U_38_ band (2)          |
| 92-100  | E9.5     | 0.363mJy | e_FU38  | [0.083,7.711] FU38 measurement uncertainty              |
| 102-113 | E12.6    | 0.363mJy | FB      | [-0.6,30406] Observed flux in B-band (2)                |
| 115-123 | E9.6     | 0.363mJy | e_FB    | [0.03,3.08] FB measurement uncertainty                  |
| 125-136 | E12.6    | 0.363mJy | FV      | [-0.8,61857] Observed flux in V-band (2)                |
| 138-146 | E9.6     | 0.363mJy | e_FV    | [0.04,4.551] FV measurement uncertainty                 |
| 148-159 | E12.6    | 0.363mJy | FR      | [-1.3,114880] Observed flux in R-band (2)               |
| 161-169 | E9.6     | 0.363mJy | e_FR    | [0.05,6.221] FR measurement uncertainty                 |
| 171-182 | E12.6    | 0.363mJy | FI      | [-2.6,282972] Observed flux in I-band (2)               |
| 184-192 | E9.7     | 0.363mJy | e_FI    | [0.24,23.61] FI measurement uncertainty                 |
| 194-205 | E12.6    | 0.363mJy | Fz'     | [-116,574102] Observed flux in z' band (2)              |
| 207-215 | E9.5     | 0.363mJy | e_Fz'   | [0.49,52.52] Fz' measurement uncertainty                |
| 217-228 | E12.6    | 0.363mJy | FJ      | [-35,1.273e+6] Observed flux in J-band (2)              |
| 230-238 | E9.4     | 0.363mJy | e_FJ    | [0.633,137.5] FJ measurement uncertainty                |
| 240-251 | E12.6    | 0.363mJy | FH      | [-2e+8,8.23e+9] Observed flux in H-band (2)             |
| 253-261 | E9.4     | 0.363mJy | e_FH    | [1.1,30.3] FH measurement uncertainty                   |
| 263-274 | E12.6    | 0.363mJy | FK      | [-2,2.115e+6] Observed flux in K-band (2)               |
| 276-284 | E9.4     | 0.363mJy | e_FK    | [1.37,96.41] FK measurement uncertainty                 |
| 286-290 | F5.2     | arcsec   | diam2   | [2.5,69.6] Effective diameter of the AUTO               |
| 292-311 | F20.13   | ---      | FKtot   | [-29,760570] Total K flux-based on                      |
| 313-321 | E9.4     | ---      | e_FKtot | [1.5,18.95] FK_tot measurement uncertainty (3)          |
| 323-332 | E10.4    | ---      | FK4ap   | [-47,492100] K flux, as measured in a                   |
| 334-342 | E9.4     | ---      | e_FK4ap | [0,2.301] FK_4ap measurement uncertainty                |
| 344-363 | F20.13   | ---      | FKSEx   | [-28,760570] K flux within SExtractor's                 |
| 365-373 | E9.4     | ---      | e_FKSEx | [1.3,92.3] FK_auto measurement uncertainty              |
| 375-384 | F10.6    | arcsec   | R50     | [-10,119.113] K-band half-light radius                  |
| 386-390 | F5.3     | ---      | Ell     | [0,0.788] K band ellipticity (4)                        |
| 392-397 | F6.2     | deg      | PA      | [-90,90] K band position angle (4)                      |
| 399-402 | F4.2     | ---      | Uw      | [0,1.51] Relative weight in the U-band                  |
| 404-407 | F4.2     | ---      | U38w    | [0,1.01] Relative weight in the U_38_-band              |
| 409-412 | F4.2     | ---      | Bw      | [0,1.77] Relative weight in the B-band                  |
| 414-417 | F4.2     | ---      | Vw      | [0,2.64] Relative weight in the V-band                  |
| 419-422 | F4.2     | ---      | Rw      | [0,1.91] Relative weight in the R-band                  |
| 424-427 | F4.2     | ---      | Iw      | [0,1.33] Relative weight in the I-band                  |
| 429-432 | F4.2     | ---      | z'w     | [0,1] Relative weight in the z' band                    |
| 434-438 | F5.2     | ---      | Jw      | [0,2.64] Relative weight in the J-b                     |
| 440-444 | F5.2     | ---      | Hw      | [0,56.98] Relative weight in the H-band (5)             |
| 446-449 | F4.2     | ---      | Kw      | [0.21,2.82] Relative weight in the K-band (5)           |
| 451-455 | I5       | ---      | idSEx   | [770,24285] The original SExtractor identifier          |
| 457     | I1       | ---      | f1      | [1,1] Deblending flag from SExtractor                   |
| 459     | I1       | ---      | f2      | [0,1] Deblending flag from SExtractor                   |
| 461-471 | F11.8    | ---      | zs      | ?=-1. Literature spectroscopic redshift                 |
| 473-479 | A7       | ---      | r_zs    | Source code for zs (7)                                  |
| 481-484 | A4       | ---      | q_zs    | Quality flag for zs, from source                        |
| 486-491 | A6       | ---      | Sptype  | Spectral classification, from source                    |
| 493-509 | E17.9    | ---      | Qzs     | ?=-99. Figure of merit for zs, from                     |
| 510     | A1       | ---      | n_Qzs   | [I] I for infinity                                      |
| 512     | I1       | ---      | n_zs    | [0,5] Number of corroborating zs                        |
| 514     | I1       | ---      | f_zs    | [0,1] Flag indicating wheter zs is considered           |
| 12      | minutes  | from     | the     | catalog output by SExtractor.                           |
| 20      | =        | Cimatti  | et      | al. (2002, Cat. <J/A+A/392/395>), Mignoli et al. (2005, |

**Note**: Effective diameter (i.e., (4{pi}A)^0.5^, where A is the aperture area)
          we use the larger of SExtractor's ISO aperture and a 2.5" diameter
          aperture to measure colors (see Section 4.5).
Note (2): All fluxes are given in such a way that they can be transformed to AB
          magnitudes using a zero-point of 25; in other words, fluxes are given
          in units of 0.363mJy.
Note (3): Total K flux-based on SExtractor's AUTO measurement - with corrections
          applied for missed flux and background over-subtraction (see Section
          4.3) - and the associated measurement uncertainty, which accounts for
          correlated noise, random background subtraction errors, spatial
          variations in the noise, Poisson shot noise, etc. (see Section 4.6)
Note (4): Morphological parameters from SExtractor, measured from the 1" FWHM
          K image.
Note (5): For all but the z' and H bands, this is essentially the exposure time,
          normalized by the nominal values.
          For the H band, this value is derived from the mock exposure map
          described in Section 3.1;
          for the z' band, this is a binary flag indicating whether the z'
          photometry is significantly affected by light from a nearby bright
          star.
Note (6): Recall that we have excised all detections with an effective exposure
          time of less than 12 minutes from the catalog output by SExtractor.
Note (7): Spectroscopic redshifts have been collected from a number of public,
          published works. In collacting these redshifts, where multiple
          (consistent) redshift determinations are available for a given object,
          we have chosen to adopt the first published determination, except
          where a later determination includes spectral classification data not
          given previously. We also choose Xray selected catalogues (viz.
          Szokoly et al. (2004, Cat. <J/ApJS/155/271> and Treister et al.,
          2009ApJ...693.1713T) in preference to others,
          considering Xray selection as an additional piece of classification
          information. Where there is no consensus (e.g. two different redshifts
          from two different sources), we have chosen according to the quality
          flags. The codes for spectroscopic redshift sources are as follows:
    K20 = Cimatti et al. (2002, Cat. <J/A+A/392/395>), Mignoli et al. (2005,
          Cat. <J/A+A/437/883>)
   Xray = Szokoly et al. (2004, Cat. <J/ApJS/155/271>)
   VVDS = Le Fevre et al. (2004, Cat. <J/A+A/428/1043>)
  GDS-F = Vanzella et al. (2005, Cat. <J/A+A/434/53>,
          2006, Cat. <J/A+A/454/423>, 2008, Cat. <J/A+A/478/83>)
  GDS-V = Popesso et al. (2008, 2009A&A...494..443P)
 IMAGES = Ravikumar et al. (2007, Cat. <J/A+A/465/1099>)
 MUS-I, MUS-V = Treister et al. (2009ApJ...693.1713T)
  Kopsv = Koposov et al. (in prep.)
  KX    = Croom et al. (2001, Cat. <J/MNRAS/328/150>)
  SNe   = Strolger et al. (2004, Cat. <J/ApJ/613/200>)
 vdWel  = Van der Wel et al. (2004ApJ...601L...5V, 2005ApJ...631..145V)
 Daddi  = Daddi et al. (2005ApJ...626..680D)
 LCIRS  = Doherty et al. (2005, Cat. <J/MNRAS/361/525>)
 Kriek  = Kriek et al. (2006ApJ...649L..71K).
Note (8): For each spectroscopic redshift determination, we have evaluated a
          "figure of merit", characterising the consistency of the photometry
          with that redshift, using the recipe described by Brammer et al.
          (2008ApJ...686.1503B).

</details>

<details>
<summary>zphot.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                    |
|:--------|:---------|:--------|:--------|:------------------------------------------------|
| 1- 5    | I5       | ---     | Seq     | [1,16910]+ Object identifier as in the          |
| 7- 16   | F10.6    | ---     | ---     | [-99] Spectroscopic redshift determination as   |
| 18- 24  | F7.3     | ---     | za      | ?=-99 Maximum likelihood redshift, allowing     |
| 26- 32  | F7.3     | ---     | zm1     | ?=-99 Probability-weighted mean redshift        |
| 34- 45  | E12.6    | ---     | chia    | ?=-99.000 Chi2 value associated with each fit   |
| 47- 53  | F7.3     | ---     | zp      | ?=-99 Maximum likelihood redshift, allowing     |
| 55- 66  | E12.6    | ---     | chip    | ?=-99 Chi2 value associated with each fit       |
| 68- 74  | F7.3     | ---     | zm2     | ?=-99 Probability-weighted mean redshift with   |
| 76- 82  | F7.3     | ---     | odds    | ?=-99 The fraction of the total integrated      |
| 2       | of       | the     | zm2     | value                                           |
| 84- 90  | F7.3     | ---     | z68l    | ?=-99 Lower limit on redshift at 68% confidence |
| 92- 98  | F7.3     | ---     | z68u    | ?=-99 Upper limit on redshift at 68% confidence |
| 100-106 | F7.3     | ---     | z95l    | ?=-99 Lower limit on redshift at 95% confidence |
| 108-114 | F7.3     | ---     | z95u    | ?=-99 Upper limit on redshift at 95% confidence |
| 116-122 | F7.3     | ---     | z99l    | ?=-99 Lower limit on redshift at 99% confidence |
| 124-130 | F7.3     | ---     | z99u    | ?=-99 Upper limit on redshift at 99% confidence |
| 132-134 | I3       | ---     | Npt     | ?=-99 The number of photometric points used to  |
</details>

<details>
<summary>restfr.dat</summary>

| Bytes   | Format   | Units   | Label    | Explanations                                  |
|:--------|:---------|:--------|:---------|:----------------------------------------------|
| 1- 5    | I5       | ---     | Seq      | [1,16910]+ Object identifier as in the        |
| 7- 13   | F7.3     | ---     | z        | ?=-99.000 Assumed redshift; we use either the |
| 2       | value    | output  | by       | EAZY, or the spectroscopic                    |
| 15- 24  | E10.4    | ---     | RFBU     | ?=-99.000 Rest-frame photometry for           |
| 26- 27  | I2       | ---     | extrapnf | [-1,1] Extrapn flag from InterRest (1)        |
| 29      | I1       | ---     | wigapnf  | [0,3] Widegapn flag from InterRest (2)        |
| 31- 40  | E10.4    | ---     | RFBB     | ?=-99.000 Rest-frame photometry for           |
| 42- 43  | I2       | ---     | exBBf    | [-1,1] Extrapn flag (1)                       |
| 45      | I1       | ---     | wiBBf    | [0,3] Widegapn flag (2)                       |
| 47- 56  | E10.4    | ---     | RFBV     | ?=-99.000 Rest-frame photometry for           |
| 58- 59  | I2       | ---     | exBVf    | [-1,1] Extrapn flag (1)                       |
| 61      | I1       | ---     | wiBVf    | [0,3] Widegapn flag (2)                       |
| 63- 72  | E10.4    | ---     | RFBR     | ?=-99.000 Rest-frame photometry for           |
| 74- 75  | I2       | ---     | exBRf    | [-1,1] Extrapn flag (1)                       |
| 77      | I1       | ---     | wiBRf    | [0,3] Widegapn flag (2)                       |
| 79- 88  | E10.4    | ---     | RFBI     | ?=-99.000 Rest-frame photometry for           |
| 90- 91  | I2       | ---     | exBIf    | [-1,1] Extrapn flag (1)                       |
| 93      | I1       | ---     | wiBIf    | [0,3] Widegapn flag (2)                       |
| 95-104  | E10.4    | ---     | RFJU     | ?=-99.000 Rest-frame photometry for           |
| 106-107 | I2       | ---     | exJUf    | [-1,1] Extrapn flag (1)                       |
| 109     | I1       | ---     | wiJUf    | [0,3] Widegapn flag (2)                       |
| 111-120 | E10.4    | ---     | RFJB     | ?=-99.000 Rest-frame photometry for           |
| 122-123 | I2       | ---     | exJBf    | [-1,1] Extrapn flag (1)                       |
| 125     | I1       | ---     | wiJBf    | [0,3] Widegapn flag (2)                       |
| 127-136 | E10.4    | ---     | RFJV     | ?=-99.000 Rest-frame photometry for           |
| 138-139 | I2       | ---     | exJVf    | [-1,1] Extrapn flag (1)                       |
| 141     | I1       | ---     | wiJVf    | [0,3] Widegapn flag (2)                       |
| 143-152 | E10.4    | ---     | RFJR     | ?=-99.000 Rest-frame photometry for           |
| 154-155 | I2       | ---     | exJRf    | [-1,1] Extrapn flag (1)                       |
| 157     | I1       | ---     | wiJRf    | [0,3] Widegapn flag (2)                       |
| 159-168 | E10.4    | ---     | RFJI     | ?=-99.000 ] Rest-frame photometry for         |
| 170-171 | I2       | ---     | exJIf    | [-1,1] Extrapnflag  (1)                       |
| 173     | I1       | ---     | wiJIf    | [0,3] Widegapn flag (2)                       |
| 175-184 | E10.4    | ---     | RFGu     | ?=-99.000 Rest-frame photometry for           |
| 186-187 | I2       | ---     | exGuf    | [-1,1] Extrapn flag (1)                       |
| 189     | I1       | ---     | wiGuf    | [0,3] Widegapn flag (2)                       |
| 191-200 | E10.4    | ---     | RFGg     | ?=-99.000 Rest-frame photometry for           |
| 202-203 | I2       | ---     | exGgf    | [-1,1] Extrapn flag (1)                       |
| 205     | I1       | ---     | wiGgf    | [0,3] Widegapn flag (2)                       |
| 207-216 | E10.4    | ---     | RFGr     | ?=-99.000 Rest-frame photometry for           |
| 218-219 | I2       | ---     | exGrf    | [-1,1] Extrapn flag (1)                       |
| 221     | I1       | ---     | wiGrf    | [0,3] Widegapn flag (2)                       |
| 223-232 | E10.4    | ---     | RFGi     | ?=-99.000 Rest-frame photometry for           |
| 234-235 | I2       | ---     | exGif    | [-1,1] Extrapn flag (1)                       |
| 237     | I1       | ---     | wiGif    | [0,3] Widegapn flag (2)                       |
| 239-248 | E10.4    | ---     | RFGz     | ?=-99.000 Rest-frame photometry for           |
| 250-251 | I2       | ---     | exGzf    | [-1,1] Extrapn flag (1)                       |
| 253     | I1       | ---     | wiGzf    | [0,3] Widegapn flag (2)                       |
| 255-264 | E10.4    | ---     | RFNUV    | ?=-99.000 Rest-frame photometry for           |
| 266-267 | I2       | ---     | exNUVf   | [-1,0] Extrapn flag (1)                       |
| 269     | I1       | ---     | wiNUVf   | [0,3] Widegapn flag (2)                       |
| 271-280 | E10.4    | ---     | RFFUV    | ?=-99.000 Rest-frame photometry for           |
| 282-283 | I2       | ---     | exFUVf   | [-1,0] Extrapnflag (1)                        |
| 285     | I1       | ---     | wiFUVf   | [0,3] Widegapn flag (2)                       |
| 287-292 | F6.2     | ---     | Dist     | ?=-99.00 The distance modulus implied by      |
| 99      | in       | the     | RFFUV    | column means Infinite value.                  |

**Note**: Flag outputs by InteRest, extrapn, where n refers to the
     rest-frame filter number, which indicates where it has extrapolated
     beyond the observed SED.
Note (2): Flag outputs by InteRest, widegapn, where n refers to the
     rest-frame filter number, which indicates where it has not used
     neighboring filters due to, for example, missing or negative
     photometry.
Note (3): -99 in the RFFUV column means Infinite value.
Note (4): the fluxes are observed fluxes through rest-frame filters:
     therefore the conversion to apparent and rest-frame magnitudes using
     the appropriate zero-point and distanc modulus should be performed.

</details>
