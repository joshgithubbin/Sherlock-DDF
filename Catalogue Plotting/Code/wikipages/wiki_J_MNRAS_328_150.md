**Authors:** Warren S.J., Glazebrook K., <Mon. Not. R. Astron. Soc. 328, 150 (2001)>, =2001MNRAS.328..150C

## Summary: KX redshift survey 

In this paper we present preliminary spectroscopic results from a small-area faint K-excess (KX) survey, and compare KX selection against UVX selection. The aim of the KX method is to produce complete samples of QSOs that are flux-limited in the K band, in order to minimize any selection bias in samples of QSOs from the effects of reddening and extinction. Using the photometric catalogue of the ESO Imaging Survey Chandra Deep Field South (48arcmin^2^) we have identified compact objects with J-K colours redder than the stellar sequence that are brighter than K=19.5. We have obtained spectra of 33 candidates, using the LDSS++ spectrograph on the Anglo-Australian Telescope (AAT). Amongst the 11 bluer candidates, with V-J<3, three are confirmed as QSOs. Identification of the 22 redder candidates with V-J>=3 is substantially incomplete, but so far no reddened QSOs have been found. Near-infrared spectroscopy will be more effective in identifying some of these targets. Only two UVX (U-B<-0.2) sources brighter than K=19.5 are found that are not also KX selected. These are both identified as galactic stars. Thus KX selection appears to select all UVX QSOs. The surface density of QSOs in the blue subsample (V-J<3) at K<=19.5 is 325^+136^_-177_{deg}^-2^. Because identification of the red subsample (V-J>=3) is substantially incomplete, the 2{sigma} upper limit on the density of reddened QSOs is large, <1150{deg}^-2^. As anticipated, at these faint magnitudes the KX sample includes several compact galaxies. Of the 14 with measured redshifts, there are roughly equal numbers of early- and late-type objects. Nearly all the early-type galaxies are found in a single structure at z=0.66.

## Spectroscopic Redshift 
 
**z:** ? Redshift 
 

## Catalogue Schema

<details>
<summary>table?.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                          |
|:--------|:---------|:--------|:----------|:------------------------------------------------------|
| 1- 4    | A4       | ---     | [CWG2001] | Designation (1)                                       |
| 6       | I1       | h       | RAh       | Right ascension (J2000.0)                             |
| 8- 9    | I2       | min     | RAm       | Right ascension (J2000.0)                             |
| 11- 15  | F5.2     | s       | RAs       | Right ascension (J2000.0)                             |
| 17      | A1       | ---     | DE-       | Declination sign (J2000.0)                            |
| 18- 19  | I2       | deg     | DEd       | Declination (J2000.0)                                 |
| 21- 22  | I2       | arcmin  | DEm       | Declination (J2000.0)                                 |
| 24- 27  | F4.1     | arcsec  | DEs       | Declination (J2000.0)                                 |
| 29- 33  | F5.2     | mag     | Umag      | ? Bessel U magnitude                                  |
| 35- 39  | F5.2     | mag     | Bmag      | ? Bessel B magnitude                                  |
| 41- 45  | F5.2     | mag     | Vmag      | ? Bessel V magnitude                                  |
| 47- 51  | F5.2     | mag     | Rmag      | ? Bessel R magnitude                                  |
| 53- 57  | F5.2     | mag     | Jmag      | J magnitude                                           |
| 59- 63  | F5.2     | mag     | Kmag      | K magnitude                                           |
| 65- 68  | F4.2     | ---     | S/GK      | K-band SExtractor stellarity parameter                |
| 70- 74  | F5.3     | ---     | z         | ? Redshift                                            |
| 76- 81  | A6       | ---     | Type      | Type of object (Gal or QSO) (2)                       |
| 83-131  | A49      | ---     | Lines     | Spectral features, both absorption                    |
| 1       | and      | 2       | UVXN      | for table 3                                           |
| 4       | Note     | (2):    | An        | (e) or (a) after gal denotes emission- or absorption- |

**Note**: Designations:
      KX NN for tables 1 and 2
      UVXN  for table 3
      KG NN for table 4
Note (2): An (e) or (a) after gal denotes emission- or absorption-
      dominated spectra respectively; an "?" indicates that the type 
      could not be identified from the spectra.

</details>
