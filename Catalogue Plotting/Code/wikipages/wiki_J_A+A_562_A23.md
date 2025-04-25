**Authors:** Garilli B., Guzzo L., Scodeggio M., Bolzonella M., Abbas U., Adami C.,, Arnouts S., Bel J., Bottini D., Branchini E., Cappi A., Coupon J.,, Cucciati O., Davidzon I., De Lucia G., De La Torre S., Franzetti P.,, Fritz A., Fumana M., Granett B.R., Ilbert O., Iovino A., Krywult J.,, Le Brun V., Le Fevre O., Maccagni D., Malek K., Marulli F., Mccracken H.J.,, Paioro L., Polletta M., Pollo A., Schlagenhaufer H., Tasca L.A.M.,, Tojeiro R., Vergani D., Zamorani G., Zanichelli A., Burden A., Di Porto C.,, Marchetti A., Marinoni C., Mellier Y., Moscardini L., Nichol R.C.,, Peacock J.A., Percival W.J., Phleps S., Wolk M., <Astron. Astrophys., 562, A23-23 (2014)>, =2014A&A...562A..23G

## Summary: VIMOS Public Extragalactic Survey (VIPERS) DR1 

We present the first Public Data Release (PDR-1) of the VIMOS Public Extragalactic Survey (VIPERS). It comprises 57204 spectroscopic measurements together with all additional information necessary for optimal scientific exploitation of the data, in particular the associated photometric measurements and quantification of the photometric and survey completeness. VIPERS is an ESO Large Programme designed to build a spectroscopic sample of =~100000 galaxies with i_AB_<22.5 and 0.5<z<1.2 with high sampling rate (=~45%). The survey spectroscopic targets are selected from the CFHTLS-Wide five-band catalogues in the W1 and W4 fields. The final survey will cover a total area of nearly 24 deg^2^, for a total comoving volume between z=0.5 and 1.2 of =~4x10^7^(Mpc/h)^3^ and a median galaxy redshift of z=~0.8. The release presented in this paper includes data from virtually the entire W4 field and nearly half of the W1 area, thus representing 64% of the final dataset. We provide a detailed description of sample selection, observations and data reduction procedures; we summarise the global properties of the spectroscopic catalogue and explain the associated data products and their use, and provide all the details for accessing the data through the survey database (http://vipers.inaf.it) where all information can be queried interactively.

## Spectroscopic Redshift 
 
**zsp:** ?=9.9999 Spectroscopic redshift 
 

## Catalogue Schema

<details>
<summary>w1ppdr1.dat</summary>

| Bytes   | Format     | Units        | Label      | Explanations                                                 |
|:--------|:-----------|:-------------|:-----------|:-------------------------------------------------------------|
| 1- 6    | A6         | ---          | ---        | [VIPERS]                                                     |
| 8- 16   | I9         | ---          | VIPERS     | VIPERS number (G1)                                           |
| 18- 26  | I9         | ---          | Num        | Internal id number (identical to VIPERS)                     |
| 28- 37  | F10.6      | deg          | RAdeg      | J2000 Righ Ascension in decimal degrees (alpha)              |
| 39- 47  | F9.6       | deg          | DEdeg      | J2000 Declination in decimal degrees (delta)                 |
| 49- 56  | F8.4       | mag          | selmag     | iAB selection magnitude. The selection                       |
| 0005    | catalogues | 58-          | 65         | F8.4  mag   e_selmag   Error on the selection magnitude      |
| 67- 74  | F8.4       | mag          | umag       | ?=-99 u magnitude (AB) from CFHTLS T0005 (2)                 |
| 76- 83  | F8.4       | mag          | gmag       | ?=-99 g magnitude (AB) from CFHTLS T0005 (2)                 |
| 85- 92  | F8.4       | mag          | rmag       | ?=-99 r magnitude (AB) from CFHTLS T0005 (2)                 |
| 94-101  | F8.4       | mag          | imag       | i magnitude (AB) from CFHTLS T0005 (2)                       |
| 103-110 | F8.4       | mag          | zmag       | ?=-99 z magnitude (AB) from CFHTLS T0005 (2)                 |
| 112-119 | F8.4       | mag          | e_umag     | ?=-99 rms uncertainty on umag (AB) (erru)                    |
| 121-128 | F8.4       | mag          | e_gmag     | ?=-99 rms uncertainty on gmag (AB) (errg)                    |
| 130-137 | F8.4       | mag          | e_rmag     | ?=-99 rms uncertainty on rmag (AB) (errr)                    |
| 139-146 | F8.4       | mag          | e_imag     | rms uncertainty on imag (AB) (erri)                          |
| 148-155 | F8.4       | mag          | e_zmag     | ?=-99 rms uncertainty on zmag (AB) (errz)                    |
| 157-164 | F8.4       | mag          | uT07       | ?=-99 u magnitude (AB) from CFHTLS T0007 (3)                 |
| 166-173 | F8.4       | mag          | gT07       | ?=-99 g magnitude (AB) from CFHTLS T0007 (3)                 |
| 175-182 | F8.4       | mag          | rT07       | ?=-99 r magnitude (AB) from CFHTLS T0007 (3)                 |
| 184-191 | F8.4       | mag          | iT07       | ?=-99 i magnitude (AB) from CFHTLS T0007 (3)                 |
| 193-200 | F8.4       | mag          | yT07       | ?=-99 y magnitude (AB) from CFHTLS T0007 (3)                 |
| 202-209 | F8.4       | mag          | zT07       | ?=-99 z magnitude (AB) from CFHTLS T0007 (3)                 |
| 211-218 | F8.4       | mag          | e_uT07     | ?=-99 error on uT07 (3)                                      |
| 220-227 | F8.4       | mag          | e_gT07     | ?=-99 error on gT07 (3)                                      |
| 229-236 | F8.4       | mag          | e_rT07     | ?=-99 error on rT07 (3)                                      |
| 238-245 | F8.4       | mag          | e_iT07     | ?=-99 error on iT07 (3)                                      |
| 247-254 | F8.4       | mag          | e_yT07     | ?=-99 error on yT07 (3)                                      |
| 256-263 | F8.4       | mag          | e_zT07     | ?=-99 error on zT07 (3)                                      |
| 265-272 | F8.4       | mag          | dUG        | ?=-99 Tile to tile color offset {delta}_UG_ (4)              |
| 274-281 | F8.4       | mag          | dGR        | ?=-99 Tile to tile color offset {delta}_GR_ (4)              |
| 283-290 | F8.4       | mag          | dRI        | ?=-99 Tile to tile color offset {delta}_RI_ (4)              |
| 292-298 | F7.5       | mag          | E(B-V)     | [0.01/0.05] Extinction factor E(B-V) derived                 |
| 300-307 | F8.2       | pix          | r2         | Radius enclosing half the object light as                    |
| 0005    | catalogue  | 309-316      | F8.2       | pix     r2T07    Radius enclosing half the object light as   |
| 0007    | catalogue  | 318-320      | I3         | ---     cl       [-88/1]?=-99 VIPERS selection flag based on |
| 0005    | catalogue  | (see         | Guzzo      | et al.                                                       |
| 322-324 | I3         | ---          | fa         | [-88/1]?=-99 A value equal to 1 is assigned to               |
| 0       | otherwise  | (see         | Sect.      | 2.2) (agnFlag)                                               |
| 326     | I1         | ---          | fp         | [0/1] 1 = object inside photometric mask,                    |
| 0       | =          | object       | outside    | (photoMask)                                                  |
| 328     | I1         | ---          | fs         | [0/1] 1 = object inside the spectroscopic mask,              |
| 0       | =          | object       | outside    | (spectMask)                                                  |
| 0005    | catalogue, | supplemented | by         | T0006 catalogue in some specific cases (see Guzzo et al.,    |
| 3       | and        | Appendix     | C,         | for details on the tile to tile color                        |
| 0005    | and        | T0006        | catalogue  | differences).                                                |
| 0007    | catalogue. | All          | magnitudes | are corrected for Galactic extinction.                       |
| 0005    | data       | (see         | Guzzo      | et al., arXiv:1303.2623,                                     |

**Note**: u,g,r,i,z magnitudes (AB system) from the CFHTLS T0005 catalogue,
 supplemented by T0006 catalogue in some specific cases (see Guzzo et al.,
 arXiv:1303.2623, Sect. 3 and Appendix C, for details on the tile to tile color
 offsets, as well as for T0005 and T0006 catalogue differences).
 All magnitudes are corrected for Galactic extinction. When an object has not
 been observed in a given band, magnitude and error are set equal to -99.
Note (3): Magnitudes (AB system) from the CFHTLS T0007 catalogue.
  All magnitudes are corrected for Galactic extinction.
Note (4): Tile to tile color offsets used in the targets sample selection
 applied to the CFHTLS T0005 data (see Guzzo et al., arXiv:1303.2623,
 Sect. 3.1).

</details>

<details>
<summary>w1spdr1.dat</summary>

| Bytes   | Format     | Units    | Label      | Explanations                                                        |
|:--------|:-----------|:---------|:-----------|:--------------------------------------------------------------------|
| 1- 6    | A6         | ---      | ---        | [VIPERS]                                                            |
| 8- 16   | I9         | ---      | VIPERS     | VIPERS number                                                       |
| 18- 26  | I9         | ---      | Num        | Internal id number (G1)                                             |
| 28- 37  | F10.6      | deg      | RAdeg      | Right Ascension (J2000) (alpha)                                     |
| 39- 47  | F9.6       | deg      | DEdeg      | Declination (J2000) (delta)                                         |
| 49- 55  | F7.4       | mag      | imag       | AB selection (i-band) magnitude. The selection                      |
| 0005    | catalogues | 57-      | 62         | F6.4  mag   e_imag     Error on the selection magnitude (errselmag) |
| 64- 69  | A6         | ---      | Point      | Pointing name                                                       |
| 71      | I1         | ---      | Q          | [1/4] Quadrant                                                      |
| 73- 77  | F5.1       | ---      | q_zsp      | [0/230] Redshift confidence flag (1)                                |
| 79- 84  | F6.4       | ---      | zsp        | ?=9.9999 Spectroscopic redshift                                     |
| 86      | I1         | ---      | Ep         | [1/2] Observing epoch (2)                                           |
| 88      | I1         | ---      | fp         | [0/1] 1 = object inside photometric mask,                           |
| 0       | =          | object   | outside    | (photoMask)                                                         |
| 90- 97  | F8.4       | ---      | TSR        | [-1/1]?=-99 Target sampling rate (3)                                |
| 99-105  | F7.3       | ---      | SSR        | [-1/1]?=-99 Spectroscopic sampling rate (4)                         |
| 10      | indicate   | an       | AGN.       | The values are:                                                     |
| 4       | =          | a        | highly     | reliable redshift (estimated to have >95% probability of            |
| 3       | =          | also     | a          | very reliable redshift, comparable in confidence with Flag 4,       |
| 2       | =          | a        | fairly     | reliable redshift measurement, but not as straightforward to        |
| 3       | and        | 4,       | supported  | by cross-correlation results,                                       |
| 1       | =          | a        | reasonable | redshift measurement, based on weak spectral features               |
| 0       | =          | no       | reliable   | spectroscopic redshift measurement was possible.                    |
| 9       | =          | a        | redshift   | based on only one single clear spectral emission feature.           |
| 10      | =          | spectrum | with       | clear problems in the observation or data processing                |
| 14      | =          | secure   | AGN        | with a >95% reliable redshift, including at least 2                 |
| 13      | =          | secure   | AGN        | with good confidence redshift, based on one broad line              |
| 19      | =          | secure   | AGN        | with one single secure emission line feature, redshift              |
| 12      | =          | a        | >95%       | reliable redshift measurement, but lines are not significantly      |
| 11      | =          | a        | tentative  | redshift measurement, with spectral features not                    |
| 20      | when       | q<10,    | or         | 200                                                                 |

**Note**: as described in Sect. 4.3. It is in the form q.X, 2q.X, where:
  * the decimal part (X) indicates concordance X>=4) or discordance
    (X<3) with the photometric redshift. 
  * "q" is a quality flag for the spectrum; values >10 indicate an AGN.
    The values are:
  4 = a highly reliable redshift (estimated to have >95% probability of
      being correct), based on a high SNR spectrum and supported by obvious
      and consistent spectral features.
  3 = also a very reliable redshift, comparable in confidence with Flag 4,
      supported by clear spectral features in the spectrum, but not
      necessarily with high SNR.
  2 = a fairly reliable redshift measurement, but not as straightforward to
      confirm as for Flags 3 and 4, supported by cross-correlation results,
      continuum shape and some spectral features, with expected chance of
      ~=75% to be correct. We shall see in the following that the actual
      estimated confidence level will turn out to be significantly better.
  1 = a reasonable redshift measurement, based on weak spectral features
      and/or continuum shape, for which there is roughly a 50% chance that
      the redshift is actually wrong.
  0 = no reliable spectroscopic redshift measurement was possible.
  9 = a redshift based on only one single clear spectral emission feature.
 10 = spectrum with clear problems in the observation or data processing
      phases. It can be a failure in the vmmps Sky to CCD conversion
      (especially at field corners), or a failed extraction by VIPGI
      (Scodeggio et al.  2005PASP..117.1284S), or a bad sky subtraction
      because the object is too close to the edge of the slit.
 14 = secure AGN with a >95% reliable redshift, including at least 2
      broad lines.
 13 = secure AGN with good confidence redshift, based on one broad line
      and some faint additional feature.
 19 = secure AGN with one single secure emission line feature, redshift
      based on this line only.
 12 = a >95% reliable redshift measurement, but lines are not significantly
      broad, might not be an AGN.
 11 = a tentative redshift measurement, with spectral features not
      significantly broad.
  * "2" added in front of the number (i.e. adding 20 when q<10, or 200
    for an AGN), indicates a serendipitous (also called secondary) object
    appearing by chance within the slit of the main target.

</details>
