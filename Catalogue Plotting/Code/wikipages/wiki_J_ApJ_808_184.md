## Summary

We present the initial results and the source catalog from the Nuclear Spectroscopic Telescope Array (NuSTAR) survey of the Extended Chandra Deep Field South (hereafter, ECDFS) --currently the deepest contiguous component of the NuSTAR extragalactic survey program. The survey covers the full ~30'x30' area of this field to a maximum depth of ~360ks (~220ks when corrected for vignetting at 3-24keV), reaching sensitivity limits of ~1.3x10^-14^erg/s/cm^2^ (3-8keV), ~3.4x10^-14^erg/s/cm^2^ (8-24keV), and ~3.0x10^-14^erg/s/cm^2^ (3-24keV). A total of 54 sources are detected over the full field, although five of these are found to lie below our significance threshold once contaminating flux from neighboring (i.e., blended) sources is taken into account. Of the remaining 49 that are significant, 19 are detected in the 8-24keV band. The 8-24 to 3-8keV band ratios of the 12 sources that are detected in both bands span the range 0.39-1.7, corresponding to a photon index range of {Gamma}~0.5-2.3, with a median photon index of {Gamma}{bar}=1.70+/-0.52. The redshifts of the 49 sources in our main sample span the range z=0.21-2.7, and their rest-frame 10-40keV luminosities (derived from the observed 8-24keV fluxes) span the range L_10-40keV_~(0.7-300)x10^43^erg/s, sampling below the "knee" of the X-ray luminosity function out to z~0.8-1. Finally, we identify one NuSTAR source that has neither a Chandra nor an XMM-Newton counterpart, but that shows evidence of nuclear activity at infrared wavelengths and thus may represent a genuine, new X-ray source detected by NuSTAR in the ECDFS.

## Catalogue Schema

<details>
<summary>catalog.dat catalogue schema</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                                   |
|:--------|:---------|:--------|:----------|:---------------------------------------------------------------|
| 1- 2    | I2       | ---     | ID        | [1/54] Unique NuSTAR ECDFS survey source                       |
| 4- 9    | A6       | ---     | ---       | [NuSTAR]                                                       |
| 11- 24  | A14      | ---     | NuSTAR    | Name of NuSTAR source (JHHMMSS+DDMM.m)                         |
| 26- 34  | F9.6     | deg     | RAdeg     | [52.8/53.4] Right ascension (J2000)                            |
| 36- 45  | F10.6    | deg     | DEdeg     | [-28.1/-27.5] Declination (J2000)                              |
| 47      | I1       | ---     | Sdet      | [0/1] 1: source is detected                                    |
| 49      | I1       | ---     | Hdet      | [0/1] 1: source is detected                                    |
| 51      | I1       | ---     | Fdet      | [0/1] 1: source is detected                                    |
| 53      | I1       | ---     | Sdet0     | [0/1] 1: source is detected post-deblending                    |
| 55      | I1       | ---     | Hdet0     | [0/1] 1: source is detected post-deblending                    |
| 57      | I1       | ---     | Fdet0     | [0/1] 1: source is detected post-deblending                    |
| 59- 64  | F6.2     | ---     | FPSB      | [-51.3/-0.1] Logarithm of the undeblended                      |
| 66- 71  | F6.2     | ---     | FPHB      | [-23.4/-0.1] Logarithm of the undeblended                      |
| 73- 78  | F6.2     | ---     | FPFB      | [-72.3/-2.2] Logarithm of the undeblended                      |
| 80- 85  | F6.2     | ---     | FPSB0     | [-41.3/-0.1] Logarithm of the deblended false                  |
| 87- 92  | F6.2     | ---     | FPHB0     | [-20.7/-0.1] Logarithm of the deblended false                  |
| 94- 99  | F6.2     | ---     | FPFB0     | [-59.8/-0.7] Logarithm of the deblended false                  |
| 101     | I1       | ---     | Sig       | [0/1] 1: the source remains significant                        |
| 103-105 | I3       | ct      | Scts      | [121/818] Total source count in soft band                      |
| 107-108 | I2       | ct      | e_Scts    | [12/30] Scts uncertainty (SB_SRC_CTS_ERR)                      |
| 110-112 | I3       | ct      | BgScts    | [84/433] Background source count in soft band                  |
| 114-116 | I3       | ct      | NScts     | [-8/410] Net source count in soft band                         |
| 118-120 | I3       | ct      | e_NScts   | [-22/30] NScts uncertainty (SB_NET_CTS_ERR)                    |
| 122-124 | I3       | ct      | Hcts      | [130/707] Total source count in hard band                      |
| 126-127 | I2       | ct      | e_Hcts    | [12/28] Hcts uncertainty (HB_SRC_CTS_ERR)                      |
| 129-131 | I3       | ct      | BgHcts    | [105/507] Background source count in hard band                 |
| 133-135 | I3       | ct      | NHcts     | [-2/222] Net source count in hard band                         |
| 137-139 | I3       | ct      | e_NHcts   | [-24/28] NHcts uncertainty (HB_NET_CTS_ERR)                    |
| 141-144 | I4       | ct      | Fcts      | [251/1508] Total source count in full band                     |
| 146-147 | I2       | ct      | e_Fcts    | [17/40] Fcts uncertainty (FB_SRC_CTS_ERR)                      |
| 149-151 | I3       | ct      | BgFcts    | [189/940] Background source count in full band                 |
| 153-155 | I3       | ct      | NFcts     | [30/616] Net source count in full band                         |
| 157-159 | I3       | ct      | e_NFcts   | [-32/40] NFcts uncertainty (FB_NET_CTS_ERR)                    |
| 161-163 | I3       | ct      | Scts0     | [121/818] Deblended total source count in                      |
| 165-167 | I3       | ct      | BgScts0   | [84/506] Deblended background source count                     |
| 169-171 | I3       | ct      | NScts0    | [-8/365] Deblended net source count                            |
| 173-175 | I3       | ct      | e_NScts0  | [-27/34] NScts0 uncertainty                                    |
| 177-179 | I3       | ct      | Hcts0     | [130/707] Deblended total source count in                      |
| 181-183 | I3       | ct      | BgHcts0   | [105/547] Deblended background source count                    |
| 185-187 | I3       | ct      | NBcts0    | [-17/198] Deblended net source count                           |
| 189-191 | I3       | ct      | e_NBcts0  | [-29/32] NBcts0 uncertainty                                    |
| 193-196 | I4       | ct      | Fcts0     | [251/1508] Deblended total source count                        |
| 198-201 | I4       | ct      | BgFcts0   | [189/1051] Deblended background source count                   |
| 203-205 | I3       | ct      | NFcts0    | [9/545] Deblended net source count                             |
| 207-209 | I3       | ct      | e_NFcts0  | [-38/46] NFcts0 uncertainty                                    |
| 211-216 | I6       | s       | ExpSB     | [105428/497401] Effective exposure time                        |
| 218-223 | I6       | s       | ExpHB     | [93694/452896] Effective exposure time                         |
| 225-230 | I6       | s       | ExpFB     | [101101/482773] Effective exposure time                        |
| 232-238 | F7.5     | ct/s    | SctR      | [0.0007/0.002] Total count rate in soft band                   |
| 240-246 | F7.5     | ct/s    | e_SctR    | [0/0.0002] SctR uncertainty (SB_SRC_CTRT_ERR)                  |
| 248-254 | F7.5     | ct/s    | BgSctR    | [0.0005/0.002] Background count rate                           |
| 256-263 | F8.5     | ct/s    | NSctR     | [-0.00002/0.001] Net count rate in soft                        |
| 265-272 | F8.5     | ct/s    | e_NSctR   | [-0.0002/0.0002] NSctR uncertainty                             |
| 274-280 | F7.5     | ct/s    | HctR      | [0.0007/0.002] Total count rate                                |
| 282-288 | F7.5     | ct/s    | e_HctR    | [0/0.0002] HctR uncertainty (HB_SRC_CTRT_ERR)                  |
| 290-296 | F7.5     | ct/s    | BgHctR    | [0.0006/0.002] Background count rate                           |
| 298-306 | F9.6     | ct/s    | NHctR     | [/0.000633] Net count rate in hard                             |
| 308-316 | F9.6     | ct/s    | e_NHctR   | [-0.0002/0.0002] NHctR uncertainty                             |
| 318-324 | F7.5     | ct/s    | FctR      | [0.001/0.004] Total count rate                                 |
| 326-332 | F7.5     | ct/s    | e_FctR    | [0/0.0002] FctR uncertainty (FB_SRC_CTRT_ERR)                  |
| 334-340 | F7.5     | ct/s    | BgFctR    | [0.001/0.003] Background count rate                            |
| 342-348 | F7.5     | ct/s    | NFctR     | [0.0001/0.002] Net count rate in                               |
| 350-357 | F8.5     | ct/s    | e_NFctR   | [-0.0002/0.0002] NFctR uncertainty                             |
| 359-366 | F8.5     | ct/s    | NSctR0    | [-0.00002/0.0009] Deblended net count rate                     |
| 368-375 | F8.5     | ct/s    | e_NSctR0  | [-0.0002/0.0002] SctR0 uncertainty                             |
| 377-384 | F8.5     | ct/s    | NHSctR0   | [-0.00004/0.0007] Deblended net count rate                     |
| 386-393 | F8.5     | ct/s    | e_NHSctR0 | [-0.0002/0.0002] NHSctR0 uncertainty                           |
| 395-401 | F7.5     | ct/s    | NFSctR0   | [0/0.002] Deblended net count rate                             |
| 403-410 | F8.5     | ct/s    | e_NFSctR0 | [-0.0002/0.0002] NFSctR0 uncertainty                           |
| 412-416 | F5.2     | ---     | BRav      | [0.1/26.3] Mean band ratio (BR_MEAN) (1)                       |
| 418-421 | F4.2     | ---     | BRmed     | [0.1/5] Median band ratio (BR_MED) (1)                         |
| 423-426 | F4.2     | ---     | BRmod     | [0/2] Mode band ratio (BR_MODE) (1)                            |
| 428-431 | F4.2     | ---     | BRll      | [0/1.2] Band ratio lower limit (BR_LL) (1)                     |
| 433-437 | F5.2     | ---     | BRul      | [0.1/15] Band ratio upper limit (BR_UL) (1)                    |
| 439-442 | F4.2     | ---     | Gamma     | [0.5/2.3] Effective photon index (GAMMA)                       |
| 444-448 | F5.2     | ---     | b_Gamma   | [-7.4/2.8]? Lower limit on Gamma (GAMMA_LL)                    |
| 450-454 | F5.2     | ---     | B_Gamma   | [-7.4/2.8]? Upper limit on Gamma (GAMMA_UL)                    |
| 456-464 | E9.3     | mW/m2   | SFlux     | Derived soft band flux (SB_FLUX)                               |
| 466-474 | E9.3     | mW/m2   | e_SFlux   | [-8.83e-15/] SFlux uncertainty (SB_FLUX_ERR)                   |
| 476-484 | E9.3     | mW/m2   | HFlux     | Derived hard band flux (HB_FLUX)                               |
| 486-494 | E9.3     | mW/m2   | e_HFlux   | [-1.94e-14/] HFlux uncertainty (HB_FLUX_ERR)                   |
| 496-503 | E8.3     | mW/m2   | FFlux     | Derived full band flux (FB_FLUX)                               |
| 505-513 | E9.3     | mW/m2   | e_FFlux   | [-1.53e-14/] FFlux uncertainty (FB_FLUX_ERR)                   |
| 515-523 | E9.3     | mW/m2   | SFlux0    | Derived deblended flux in soft band                            |
| 525-533 | E9.3     | mW/m2   | e_SFlux0  | [-8.83e-15/] SFlux0 uncertainty                                |
| 535-543 | E9.3     | mW/m2   | HFlux0    | Derived deblended flux in hard band                            |
| 545-553 | E9.3     | mW/m2   | e_HFlux0  | [-1.94e-14/] HFlux0 uncertainty                                |
| 555-562 | E8.3     | mW/m2   | FFlux0    | Derived deblended flux in full band                            |
| 564-572 | E9.3     | mW/m2   | e_FFlux0  | [-1.53e-14/] FFlux0 uncertainty                                |
| 574-576 | A3       | ---     | CRef      | Counterpart catalog code (C_REF) (2)                           |
| 578-580 | I3       | ---     | CSeq      | [7/739]? Unique identification number of the                   |
| 582-590 | F9.6     | deg     | RACdeg    | [52.8/53.4]? Counterpart right ascension                       |
| 592-601 | F10.6    | deg     | DECdeg    | [-28.1/-27.5]? Counterpart declination                         |
| 603-607 | F5.2     | arcsec  | CSep      | [1.2/29.4]? Separation between the NuSTAR                      |
| 609-617 | E9.3     | mW/m2   | F3-8keV   | ? 3-8keV Chandra or XMM-Newton flux of the                     |
| 619-627 | E9.3     | mW/m2   | F3-8keVc  | ? Combined 3-8keV or Chandra or XMM-Newton                     |
| 629-633 | F5.3     | ---     | Czsp      | [0.1/2.8]? Spectroscopic redshift of the                       |
| 635-639 | F5.3     | ---     | Czph      | [0.09/2.8]? Photometric redshift of the                        |
| 641-645 | F5.3     | ---     | Cz        | [0.1/2.8]? Adopted redshift (C_ADOPTED_Z)                      |
| 647-655 | E9.3     | [10-7W] | L10-40    | ?=-99 Non-absorption-corrected rest-frame                      |
| 657-665 | E9.3     | [10-7W] | e_L10-40  | [-9.06e+44/]?=-99 L10-40 uncertainty                           |
| 667     | A1       | ---     | n_NuSTAR  | [n] Note on NuSTAR J033202-2746.7 (NOTES) (3)                  |
| 8-24    | to       | 3-8keV  | band      | ratios output by the BEHR algorithm. Because this              |
| 05      | =        | Lehmer  | et        | al. 2005, J/ApJS/161/21 (<[LBA2005] NNN> in Simbad)            |
| 13      | =        | Ranalli | et        | al. 2013, J/A+A/555/A42 (<XMMCDFS JHHMMSS.s+DDMMSS> in Simbad) |
| 11      | =        | Xue     | et        | al. 2011, J/ApJS/195/10 (<[XLB2011] NNN> in Simbad)            |
| 8       | in       | Del     | Moro      | et al. (2014ApJ...786...16D)                                   |

**Note**: 8-24 to 3-8keV band ratios output by the BEHR algorithm. Because this
    algorithm is a Bayesian estimator, it calculates the band ratio probability
    distribution function and provides the mean, median, mode, and upper and
    lower 68th percentiles, which we report here.
Note (2): Counterpart catalog code as follows:
 L05 = Lehmer et al. 2005, J/ApJS/161/21 (<[LBA2005] NNN> in Simbad)
 R13 = Ranalli et al. 2013, J/A+A/555/A42 (<XMMCDFS JHHMMSS.s+DDMMSS> in Simbad)
 X11 = Xue et al. 2011, J/ApJS/195/10 (<[XLB2011] NNN> in Simbad)
Note (3):
   n = NuSTAR J033202-2746.8 in Del Moro et al. (2014ApJ...786...16D)

</details>
