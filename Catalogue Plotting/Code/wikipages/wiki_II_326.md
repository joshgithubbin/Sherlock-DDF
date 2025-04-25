## Summary

We have revised the Spitzer Wide-Area Infrared Extragalactic survey (SWIRE) Photometric Redshift Catalogue to take account of new optical photometry in several of the SWIRE areas, and incorporating Two Micron All Sky Survey (2MASS) and UKIRT Infrared Deep Sky Survey (UKIDSS) near-infrared data. Aperture matching is an important issue for combining near-infrared and optical data, and we have explored a number of methods of doing this. The increased number of photometric bands available for the redshift solution results in improvements both in the rms error and, especially, in the outlier rate. We have also found that incorporating the dust torus emission into the quasi-stellar object (QSO) templates improves the performance for QSO redshift estimation. Our revised redshift catalogue contains over 1 million extragalactic objects, of which 26 288 are QSOs.

## Catalogue Schema

<details>
<summary>zcatrev.dat catalogue schema</summary>

| Bytes    | Format   | Units       | Label    | Explanations                                  |
|:---------|:---------|:------------|:---------|:----------------------------------------------|
| 1- 8     | I8       | ---         | IR       | [2/714568] Infrared identifier                |
| 10- 17   | I8       | ---         | Opt      | [0/13182599] Optical identifier               |
| 19- 29   | F11.6    | deg         | RAdeg    | Right ascension (J2000)                       |
| 31- 41   | F11.6    | deg         | DEdeg    | Declination (J2000)                           |
| 43- 52   | F10.2    | uJy         | S3.6     | ?=-99 Spitzer/IRAC flux density at 3.6um      |
| 54- 63   | F10.2    | uJy         | S4.5     | ?=-99 Spitzer/IRAC flux density at 4.5um      |
| 65- 74   | F10.2    | uJy         | S5.8     | ?=-99 Spitzer/IRAC flux density at 5.8um      |
| 76- 85   | F10.2    | uJy         | S8.0     | ?=-99 Spitzer/IRAC flux density at 8.0um      |
| 87- 96   | F10.2    | uJy         | S24      | ?=-99 Spitzer/MIPS flux density at 24um       |
| 98-107   | F10.2    | uJy         | S70      | ?=-99 Spitzer/MIPS flux density at 70um       |
| 109-118  | F10.2    | uJy         | S160     | ?=-99 Spitzer/MIPS flux density at 160um      |
| 120-129  | F10.2    | uJy         | e_S3.6   | []?=-99 rms uncertainty on S3.6               |
| 131-140  | F10.2    | uJy         | e_S4.5   | []?=-99 rms uncertainty on S4.5               |
| 142-151  | F10.2    | uJy         | e_S5.8   | []?=-99 rms uncertainty on S5.8               |
| 153-162  | F10.2    | uJy         | e_S8.0   | []?=-99 rms uncertainty on S8.0               |
| 164-173  | F10.2    | uJy         | e_S24    | ?=-99 rms uncertainty on S24                  |
| 175-184  | F10.2    | uJy         | e_S70    | ?=-99 rms uncertainty on S70                  |
| 186-195  | F10.2    | uJy         | e_S160   | ?=-99 rms uncertainty on S160                 |
| 197-204  | F8.2     | mag         | Umag     | ?=-99 SWIRE U magnitude (am1) (1)             |
| 206-213  | F8.2     | mag         | gmag     | ?=-99 SWIRE g magnitude (am2) (1)             |
| 215-222  | F8.2     | mag         | rmag     | ?=-99 SWIRE r magnitude (am3) (1)             |
| 224-231  | F8.2     | mag         | imag     | ?=-99 SWIRE i magnitude (am4) (1)             |
| 233-240  | F8.2     | mag         | Zmag     | ?=-99 SWIRE Z magnitude (am5) (1)             |
| 242-249  | F8.2     | mag         | e_Umag   | ?=-99 rms uncertainty on Umag                 |
| 251-258  | F8.2     | mag         | e_gmag   | ?=-99 rms uncertainty on gmag                 |
| 260-267  | F8.2     | mag         | e_rmag   | ?=-99 rms uncertainty on rmag                 |
| 269-276  | F8.2     | mag         | e_imag   | ?=-99 rms uncertainty on imag                 |
| 278-285  | F8.2     | mag         | e_Zmag   | ?=-99 rms uncertainty on Zmag                 |
| 287-294  | F8.2     | mag         | umag2    | ?=-99 u magnitude (am21) (1)                  |
| 296-303  | F8.2     | mag         | gmag2    | ?=-99 g magnitude (am22) (1)                  |
| 305-312  | F8.2     | mag         | rmag2    | ?=-99 r magnitude (am23) (1)                  |
| 314-321  | F8.2     | mag         | imag2    | ?=-99 i magnitude (am25) (1)                  |
| 323-330  | F8.2     | mag         | zmag2    | ?=-99 z magnitude (am26) (1)                  |
| 332-339  | F8.2     | mag         | e_umag2  | ?=-99 rms uncertainty on umag2                |
| 341-348  | F8.2     | mag         | e_gmag2  | ?=-99 rms uncertainty on gmag2                |
| 350-357  | F8.2     | mag         | e_rmag2  | ?=-99 rms uncertainty on rmag2                |
| 359-366  | F8.2     | mag         | e_imag2  | ?=-99 rms uncertainty on imag2                |
| 368-375  | F8.2     | mag         | e_zmag2  | ?=-99 rms uncertainty on zmag2                |
| 377-384  | F8.2     | mag         | Jmag     | ?=-99 J magnitude (am6) (1)                   |
| 386-393  | F8.2     | mag         | Hmag     | ?=-99 H magnitude (am7) (1)                   |
| 395-402  | F8.2     | mag         | Kmag     | ?=-99 K magnitude (am8) (1)                   |
| 404-411  | F8.2     | mag         | e_Jmag   | ?=-99 rms uncertainty on Jmag                 |
| 413-420  | F8.2     | mag         | e_Hmag   | ?=-99 rms uncertainty on Hmag                 |
| 422-429  | F8.2     | mag         | e_Kmag   | ?=-99 rms uncertainty on Kmag                 |
| 433-434  | I2       | ---         | mst      | [-5/5] Stellar flag (-1=star, 1=galaxy,       |
| 436-443  | F8.3     | mag         | dmag     | ? Aperture correction in magnitudes,          |
| 445-452  | F8.3     | mag         | dmag1    | Other aperture correction in magnitudes       |
| 454-456  | I3       | ---         | J1       | [1/36] Optical template type (1-11 galaxies,  |
| 13-30    | QSOs)    | for         | A_V_=0   | solution (2)                                  |
| 458-464  | F7.3     | ---         | alz      | [0/0.85] log(1+zph) for A_V_=0 solution       |
| 466-475  | F10.3    | ---         | err0     | Reduced chi^2^ for A_V_=0 solution            |
| 477-479  | I3       | ---         | J2       | [1/36] Optical template type (1-11 galaxies,  |
| 13-15    | QSOs)    | for         | free     | A_V_ solution (2)                             |
| 481-487  | F7.3     | ---         | alz2     | [0/0.85] log(1+zph) for free A_V_ solution    |
| 489-494  | F6.2     | mag         | AV1      | Absorption in V band                          |
| 496-505  | F10.3    | ---         | err1     | Reduced chi^2^ for free A_V_ solution         |
| 507-509  | I3       | ---         | N91      | [1/17] Total number of photometric bands      |
| 511-513  | I3       | ---         | Nopt     | [-9/10] Number of optical bands in solution   |
| 515-522  | F8.2     | mag         | BMAG     | ?=0.00 M_B_ (corrected for extinction) for    |
| 524-531  | F8.2     | [Lsun]      | logLB    | B-band luminosity                             |
| 533-542  | F10.5    | ---         | zsp      | ?=0.00000 Spectroscopic redshift              |
| 544-547  | I4       | ---         | q_zsp    | [0/219] Redshift class (VVDS) (3)             |
| 549-552  | I4       | ---         | r_zsp    | [-9/40] Reference for zsp (3)                 |
| 554-556  | I3       | ---         | NIR      | [0/6] Number of bands with infrared excess    |
| 558-563  | F6.2     | ---         | alp1     | [0/1]? Relative amplitude of cirrus component |
| 565-570  | F6.2     | ---         | alp2     | [0/1]? Relative amplitude of M82 starburst    |
| 572-577  | F6.2     | ---         | alp3     | [0/1]? Relative amplitude of AGN dust torus   |
| 579-584  | F6.2     | ---         | alp4     | [0/1]? Relative amplitude of A220 starburst   |
| 586-595  | F10.3    | ---         | errIR    | Reduced chi_{nu}_^2^ of infrared template fit |
| 597-604  | F8.2     | [Lsun]      | logL1    | ?=0.00 Cirrus component luminosity (1-1000um) |
| 606-613  | F8.2     | [Lsun]      | logL2    | ?=0.00 M82 starburst component luminosity     |
| 615-622  | F8.2     | [Lsun]      | logL3    | ?=0.00 AGN dust torus component luminosity    |
| 624-631  | F8.2     | [Lsun]      | logL4    | ?=0.00 A220 component luminosity,             |
| 633-640  | F8.2     | [Lsun]      | logLIR   | ?=0.00 Infrared luminosity,                   |
| 642-644  | I3       | ---         | IRt      | [1/6] IR template type (4)                    |
| 646-650  | F5.2     | [mJy]       | logS70   | ?=0.00 Predicted flux density at 70um         |
| 652-657  | F6.2     | [mJy]       | logS160  | ?=0.00 Predicted flux density at 160um        |
| 659-664  | F6.2     | [mJy]       | logS350  | ?=0.00 Predicted flux density at 350um        |
| 666-671  | F6.2     | [mJy]       | logS450  | ?=0.00 Predicted flux density at 450um        |
| 673-678  | F6.2     | [mJy]       | logS850  | ?=0.00 Predicted flux density at 850um        |
| 680-685  | F6.2     | [mJy]       | logS1250 | ?=0.00 Predicted flux density at 1250um       |
| 687-692  | F6.2     | [Lsun]      | logL3.6  | Luminosity at 3.6um                           |
| 694-699  | F6.2     | [Msun]      | logM*    | Stellar mass                                  |
| 701-706  | F6.2     | [Msun/yr]   | logSFR   | ?=-9.99 Star formation rate                   |
| 708-713  | F6.2     | [Msun]      | logMdust | ?=0.00 Dust mass                              |
| 715-1479 | 85F9.2   | ---         | chi2A    | ?=-99.00 Array of reduced {chi}_{nu}_^2^ as   |
| 01       | in       | log(1+zph), | from     | 0.01 to 0.85                                  |
</details>
