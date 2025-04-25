## Summary

We present observations collected in the CFHTLS-VIPERS region in the ultraviolet with the GALEX satellite (far- and near-ultraviolet channels) and in the near-infrared with the CFHT/WIRCam camera (Ks band) over an area of 22 and 27deg^2^, respectively. The depth of the photometry was optimised to measure the physical properties (e.g., star formation rate, stellar masses) of all the galaxies in the VIPERS spectroscopic survey. The large volume explored by VIPERS will enable a unique investigation of the relationship between the galaxy properties and their environment (density field and cosmic web) at high redshift (0.5<=z<=1.2). In this paper, we present the observations, the data reductions, and the build-up of the multi-colour catalogues. The CFHTLS-T0007 (gri-{chi}^2^) images are used as reference to detect and measure the Ks -band photometry, while the T0007 u*-selected sources are used as priors to perform the GALEX photometry based on a dedicated software (EMphot). Our final sample reaches NUV_AB_~25 (at 5{sigma}) and K_AB_~22 (at 3{sigma}). The large spectroscopic sample (~51,000 spectroscopic redshifts) allows us to highlight the robustness of our star/galaxy separation and the reliability of our photometric redshifts with a typical accuracy of {sigma]_z_<=0:04 and a fraction of catastrophic failures {eta}<=2% down to i~23. We present various tests on the Ks -band completeness and photometric redshift accuracy by comparing our results with existing overlapping deep photometric catalogues. Finally, we discuss the BzK sample of passive and active galaxies at high redshift and the evolution of galaxy morphology in the (NUV-r) vs (r-Ks) diagram at low redshift (z<=0.25) based on the high image quality of the CFHTLS. The images, catalogues, and photometric redshifts for 1.5 million sources (down to NUV<=25 {union} Ks<=22) are released and available at this URL: http://cesam.lam.fr/vipers-mls/.

## Catalogue Schema

<details>
<summary>vipmlsw1.dat catalogue schema</summary>

| Bytes   | Format   | Units        | Label      | Explanations                                                     |
|:--------|:---------|:-------------|:-----------|:-----------------------------------------------------------------|
| 1- 7    | I7       | ---          | VIPERS-MLS | Running number in the considered                                 |
| 9- 24   | A16      | ---          | TileT07    | CFHTLS T0007 Tile                                                |
| 26- 36  | F11.7    | deg          | RAdeg      | Right ascension (J2000)                                          |
| 38- 48  | F11.8    | deg          | DEdeg      | Declination (J2000)                                              |
| 50- 56  | F7.3     | mag          | FUV        | ?=-99 GALEX FUV magnitude                                        |
| 58- 64  | F7.3     | mag          | NUV        | ?=-99 GALEX NUV magnitude                                        |
| 66- 72  | F7.3     | mag          | umag       | ?=-99 CFHTLS u magnitude (AB)                                    |
| 74- 80  | F7.3     | mag          | gmag       | ?=-99 CFHTLS g magnitude (AB)                                    |
| 82- 88  | F7.3     | mag          | rmag       | ?=-99 CFHTLS r magnitude (AB)                                    |
| 90- 96  | F7.3     | mag          | imag       | ?=-99 CFHTLS i magnitude (AB)                                    |
| 98-104  | F7.3     | mag          | ymag       | ?=-99 CFHTLS y magnitude (AB)                                    |
| 106-112 | F7.3     | mag          | zmag       | ?=-99 CFHTLS z magnitude (AB)                                    |
| 114-120 | F7.3     | mag          | Ksmag      | ?=-99 WIRCam Ks (2146nm) magnitude, AB                           |
| 122-146 | F25.22   | mag          | deltamag   | Weighted mean rescaling factor (from ISO                         |
| 148-157 | F10.2    | arcsec       | r2         | Half-light radius (see T0007 doc.)                               |
| 159-165 | F7.4     | mag/arcsec+2 | mumaxi     | i-band maximum surface brightness                                |
| 167     | I1       | ---          | flagpls    | [0/1] Point-Like Source (PLS) flag (1)                           |
| 169     | I1       | ---          | flagfake   | [0/1] Potential fake object flag (2)                             |
| 171-176 | F6.2     | ---          | zsec       | Redshift at the second significant PDF peak                      |
| 178-183 | F6.2     | ---          | zqso       | Best Redshift for the QSO                                        |
| 185-188 | I4       | ---          | Classks    | Classification (3)                                               |
| 190-197 | F8.4     | ---          | zphot      | ?=-99 Most reliable photo-z based on                             |
| 199-207 | F9.5     | ---          | E_zphot    | ?=-99 zphot upper error (delimiting the 32%                      |
| 209-216 | F8.4     | ---          | e_zphot    | ?=-99 zphot lower error (delimiting the 32%                      |
| 218     | I1       | ---          | mopt       | [0/1] CFHTLenS Masks (mask_opt) (4)                              |
| 220     | I1       | ---          | mgalex     | [0/1] GALEX Masks (mask_galex) (4)                               |
| 222     | I1       | ---          | lfuv       | [0/1] FUV observed region (layout_fuv) (5)                       |
| 224     | I1       | ---          | lnuv       | [0/1] NUV observed region (layout_nuv) (5)                       |
| 226     | I1       | ---          | lks        | [0/1] WIRCam observed region                                     |
| 228-235 | F8.4     | mag          | e_FUV      | ?=-99 rms uncertainty on FUV                                     |
| 237-246 | F10.4    | mag          | e_NUV      | ?=-99 rms uncertainty on FUV                                     |
| 248-257 | F10.4    | mag          | e_umag     | ?=-99 rms uncertainty on umag                                    |
| 259-267 | F9.4     | mag          | e_gmag     | ?=-99 rms uncertainty on gamg                                    |
| 269-277 | F9.4     | mag          | e_rmag     | ?=-99 rms uncertainty on rmag                                    |
| 279-286 | F8.4     | mag          | e_imag     | ?=-99 rms uncertainty on imag                                    |
| 288-296 | F9.4     | mag          | e_ymag     | ?=-99 rms uncertainty on ymag                                    |
| 298-304 | F7.3     | mag          | i+ymag     | ?=-99 CFHTLS combined i-bands                                    |
| 306-314 | F9.4     | mag          | e_i+ymag   | ?=-99 rms uncertainty on i+ymag                                  |
| 316-325 | F10.4    | mag          | e_zmag     | ?=-99 rms uncertainty on zmag                                    |
| 327-336 | F10.4    | mag          | e_Ksmag    | ?=-99 rms uncertainty on Ksmag                                   |
| 338-342 | F5.1     | ---          | Context    | Selected bands for SED fitting                                   |
| 344     | I1       | ---          | Nband      | [1/8] Number of bands used in the SED                            |
| 346-357 | F12.6    | ---          | chibest    | ?=99999 Minimum Chi-square for the galaxy                        |
| 359-362 | I4       | ---          | modbest    | ?=-999 Best model from the galaxy                                |
| 364-371 | F8.4     | ---          | zbest      | ?=-99 Redshift at minimum                                        |
| 373-379 | F7.3     | ---          | pdzbest    | Integrated PDF(z) in between                                     |
| 381-392 | F12.6    | ---          | chistar    | ?=99999 Minimum Chi-square for the STAR                          |
| 394-397 | I4       | ---          | modstar    | ?=-999 Best model from the STAR                                  |
| 399-410 | F12.6    | ---          | chiqso     | ?=99999 Minimum Chi-square for the QSO                           |
| 412-415 | I4       | ---          | modqso     | ?=-999 Best model from the QSO                                   |
| 0       | =        | Extended     | 1          | = Point-like source in at least two detection bands OR saturated |
| 0       | =        | Good         | object     | 1 = Fake object                                                  |
| 0       | =        | Outside      | (good      | object)                                                          |
| 1       | =        | Inside       | (bad       | object)                                                          |
| 0       | =        | Inside       | (good      | object)                                                          |
| 1       | =        | Outside      | (bad       | object)                                                          |

**Note**: Point-Like Source (PLS) flag as follows:
           0 = Extended
           1 = Point-like source in at least two detection bands OR saturated
Note (2): Potential fake object flag as follows:
           0 = Good object
           1 = Fake object
Note (3): Classification:
          GALAXY [0-9]  /  STAR [10-19] /  QSO [20-29]
Note (4): CFHTLenS and GALEX masks codes as follows:
           0 = Outside (good object)
           1 = Inside (bad object)
Note (5): Layout flags as follows:
           0 = Inside (good object)
           1 = Outside (bad object)

</details>
