**Authors:** Chiappetti L., Clerc N., Pacaud F., Pierre M., Gueguen A., Paioro L.,, Polletta M., Melnyk O., Elyiv A., Surde J., Faccioli L., <Mon. Not. R. Astron. Soc. 429, 1652 (2013)>, =2013MNRAS.429.1652C

## Summary: XMM-LSS catalogue. Version II. 

We present the final release of the multiwavelength XMM-Large Scale Structure (LSS) data set, covering the full survey area of 11.1deg^2^, with X-ray data processed with the latest XMM-LSS pipeline version. The present publication supersedes the catalogue from the first paper in this series, pertaining to the initial 5deg^2^. We provide X-ray source lists in the customary energy bands (0.5-2 and 2-10keV) for a total of 6721 objects in the deep full-exposure catalogue and 5572 in the catalogue limited to 10ks, above a detection likelihood of 15 in at least one band. We also provide a multiwavelength catalogue, cross-correlating our list with infrared, near-infrared, optical and ultraviolet catalogues. Customary data products, such as X-ray fits images and thumbnail images from the Canada-France-Hawaii Telescope Legacy Survey and the Spitzer Wide-Area Infrared Extragalactic Survey, are made available, together with our data base in Milan, which can be queried interactively.
## Coverage
## Catalogue Schema

<details>
<summary>2xlss.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                  |
|:--------|:---------|:--------|:----------|:----------------------------------------------|
| 1- 5    | I5       | ---     | Xseq      | Internal sequence identifier (G1)             |
| 7- 11   | A5       | ---     | ---       | [2XLSS]                                       |
| 13- 29  | A17      | ---     | 2XLSS     | catalog name of the object (Xcatname) (G2)    |
| 32- 39  | F8.5     | deg     | XRAdeg    | Right ascension (J2000)                       |
| 41- 48  | F8.5     | deg     | XDEdeg    | Declination (J2000)                           |
| 50- 54  | I5       | ---     | Bseq      | ? Identifier in 0.5-2keV band (G3)            |
| 56- 61  | A6       | ---     | ---       | [2XLSSB]                                      |
| 63- 78  | A16      | ---     | 2XLSSB    | Alternate name in 0.5-2keV band (Bcatname)    |
| 80      | I1       | ---     | Bc1c2     | [0/2]? extended source class (G4)             |
| 82- 87  | F6.2     | arcsec  | Bcorerad  | ? core radius for extended sources (G5)       |
| 89-100  | F12.5    | ---     | Bextlike  | ? 0.5-2keV extension likelihood               |
| 102-113 | F12.5    | ---     | Bdetlike  | ? 0.5-2keV detection likelihood               |
| 115-119 | F5.2     | arcmin  | Boffaxis  | ? 0.5-2keV off-axis angle                     |
| 121-128 | F8.5     | deg     | BRAdeg    | ? 0.5-2keV Right ascension (J2000) (G6)       |
| 130-137 | F8.5     | deg     | BDEdeg    | ? 0.5-2keV Declination (J2000) (G6)           |
| 139-141 | F3.1     | arcsec  | Bposerr   | ? Position error in 0.5-2keV band (G7)        |
| 143-149 | F7.4     | ct/s    | Bratemos  | ? 0.5-2keV MOS count rate                     |
| 151-157 | F7.4     | ct/s    | Bratepn   | ? 0.5-2keV pn  count rate                     |
| 159-163 | F5.1     | aW/m2   | Bflux     | ? Flux in 0.5-2keV band (expressed in         |
| 165     | I1       | ---     | f_Bflux   | [0/2]? Flux difference flag (Bfluxflag) (G9)  |
| 167-171 | I5       | ---     | CDseq     | ? Identifier in 2-10keV band (G10)            |
| 173-179 | A7       | ---     | ---       | [2XLSSCD]                                     |
| 181-196 | A16      | ---     | 2XLSSCD   | ? alternate name in 2-10keV band (CDcatname)  |
| 198-203 | F6.2     | arcsec  | CDcorerad | ? Core radius for extended sources (G5)       |
| 205-216 | F12.5    | ---     | CDextlike | ? extension likelihood                        |
| 218-229 | F12.5    | ---     | CDdetlike | ? detection likelihood                        |
| 231-235 | F5.2     | arcmin  | CDoffaxis | ? off-axis angle                              |
| 237-244 | F8.5     | deg     | CDRAdeg   | ? Right ascension (J2000) (G6)                |
| 246-253 | F8.5     | deg     | CDDEdeg   | ? Declination (J2000) (G6)                    |
| 255-257 | F3.1     | arcsec  | CDposerr  | ? Position error in 2-10keV band (G7)         |
| 259-265 | F7.4     | ct/s    | CDratemos | ? 2-10keV MOS count rate                      |
| 267-273 | F7.4     | ct/s    | CDratepn  | ? 2-10keV pn  count rate                      |
| 275-280 | F6.1     | aW/m2   | CDflux    | ? Flux in 2-10keV band (expressed in          |
| 282     | I1       | ---     | f_CDflux  | [0/2]? Flux difference flag (CDfluxflag) (G9) |
| 284-288 | I5       | ---     | Xlss1     | [0/13118] Pointer to version I XLSS (G11)     |
| 290-294 | I5       | ---     | Xdeep     | Pointer to deep 2XLSSd catalog (G12)          |
</details>

<details>
<summary>2xlssd.dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                  |
|:--------|:---------|:--------|:----------|:----------------------------------------------|
| 1- 5    | I5       | ---     | Xseq      | Internal sequence identifier (G1)             |
| 7- 12   | A6       | ---     | ---       | [2XLSSd]                                      |
| 14- 30  | A17      | ---     | 2XLSSd    | Catalog name of the object (Xcatname) (G2)    |
| 32- 39  | F8.5     | deg     | XRAdeg    | Right ascension (J2000)                       |
| 41- 48  | F8.5     | deg     | XDEdeg    | Declination (J2000)                           |
| 50- 54  | I5       | ---     | Bseq      | ? Identifier in 0.5-2keV band (G3)            |
| 56- 61  | A6       | ---     | ---       | [2XLSSB]                                      |
| 63- 78  | A16      | ---     | 2XLSSB    | Alternate name in 0.5-2keV band (Bcatname)    |
| 80      | I1       | ---     | Bc1c2     | [0/2]? extended source class (G4)             |
| 82- 87  | F6.2     | arcsec  | Bcorerad  | ? core radius for extended sources (G5)       |
| 89-100  | F12.5    | ---     | Bextlike  | ? 0.5-2keV extension likelihood               |
| 102-113 | F12.5    | ---     | Bdetlike  | ? 0.5-2keV detection likelihood               |
| 115-119 | F5.2     | arcmin  | Boffaxis  | ? 0.5-2keV off-axis angle                     |
| 121-128 | F8.5     | deg     | BRAdeg    | ? 0.5-2keV Right ascension (J2000) (G6)       |
| 130-137 | F8.5     | deg     | BDEdeg    | ? 0.5-2keV Declination (J2000) (G6)           |
| 139-141 | F3.1     | arcsec  | Bposerr   | ? Position error in 0.5-2keV band (G7)        |
| 143-149 | F7.4     | ct/s    | Bratemos  | ? 0.5-2keV MOS count rate                     |
| 151-157 | F7.4     | ct/s    | Bratepn   | ? 0.5-2keV pn  count rate                     |
| 159-163 | F5.1     | aW/m2   | Bflux     | ? Flux in 0.5-2keV band (expressed in         |
| 165     | I1       | ---     | f_Bflux   | [0/2]? Flux difference flag (Bfluxflag) (G9)  |
| 167-171 | I5       | ---     | CDseq     | ? Identifier in 2-10keV band (G10)            |
| 173-179 | A7       | ---     | ---       | [2XLSSCD]                                     |
| 181-196 | A16      | ---     | 2XLSSCD   | ? alternate name in 2-10keV band (CDcatname)  |
| 198-203 | F6.2     | arcsec  | CDcorerad | ? Core radius for extended sources (G5)       |
| 205-216 | F12.5    | ---     | CDextlike | ? extension likelihood                        |
| 218-229 | F12.5    | ---     | CDdetlike | ? detection likelihood                        |
| 231-235 | F5.2     | arcmin  | CDoffaxis | ? off-axis angle                              |
| 237-244 | F8.5     | deg     | CDRAdeg   | ? Right ascension (J2000) (G6)                |
| 246-253 | F8.5     | deg     | CDDEdeg   | ? Declination (J2000) (G6)                    |
| 255-257 | F3.1     | arcsec  | CDposerr  | ? Position error in 2-10keV band (G7)         |
| 259-265 | F7.4     | ct/s    | CDratemos | ? 2-10keV MOS count rate                      |
| 267-273 | F7.4     | ct/s    | CDratepn  | ? 2-10keV pn  count rate                      |
| 275-280 | F6.1     | aW/m2   | CDflux    | ? Flux in 2-10keV band (expressed in          |
| 282     | I1       | ---     | f_CDflux  | [0/2]? Flux difference flag (CDfluxflag) (G9) |
| 284-288 | I5       | ---     | Xlss1     | [0/13118] Pointer to version I XLSS (G11)     |
</details>
