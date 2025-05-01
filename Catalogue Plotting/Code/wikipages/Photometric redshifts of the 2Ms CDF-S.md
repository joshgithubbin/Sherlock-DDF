**Authors:** Brandt W.N., Xue Y.Q., Brusa M., Alexander D.M., Bauer F.E.,, Comastri A., Koekemoer A., Lehmer B.D., Mainieri V., Rafferty D.A.,, Schneider D.P., Silverman J.D., Vignali C., <Astrophys. J. Suppl. Ser., 187, 560-580 (2010)>, =2010ApJS..187..560L

## Summary: Photometric redshifts of the 2Ms CDF-S 

We present reliable multiwavelength identifications and high-quality photometric redshifts for the 462 X-ray sources in the ~2Ms Chandra Deep Field-South (CDF-S) survey (Cat. J/ApJS/179/19). Source identifications are carried out using deep optical-to-radio multiwavelength catalogs, and are then combined to create lists of primary and secondary counterparts for the X-ray sources. We identified reliable counterparts for 442 (95.7%) of the X-ray sources, with an expected false-match probability of ~6.2%; we also selected four additional likely counterparts. The majority of the other 16 X-ray sources appear to be off-nuclear sources, sources associated with galaxy groups and clusters, high-redshift active galactic nuclei (AGNs), or spurious X-ray sources. A likelihood-ratio method is used for source matching, which effectively reduces the false-match probability at faint magnitudes compared to a simple error-circle matching method. We construct a master photometric catalog for the identified X-ray sources including up to 42 bands of UV-to-infrared data, and then calculate their photometric redshifts (photo-z's). The typical photo-z accuracy is ~6%-7%.

## Spectroscopic Redshift 
 
**zs:** ?=-1 Spectroscopic redshift 
 

## Photometric Redshift 
 
**zp:** ?=-1 ZEBRA derived photometric redshift (3) 
 

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format   | Units    | Label   | Explanations                                                          |
|:--------|:---------|:---------|:--------|:----------------------------------------------------------------------|
| 1- 7    | A7       | ---      | Cat     | Catalog identification (1)                                            |
| 9- 14   | A6       | ---      | Filt    | Catalog band for the magnitude                                        |
| 16- 19  | F4.1     | ---      | Det     | The minimum threshold used for source                                 |
| 21- 24  | F4.1     | mag      | Depth   | Catalog depth in AB magnitude (3)                                     |
| 26- 29  | I4       | arcmin2  | Angle   | Catalog solid-angle coverage                                          |
| 31- 35  | I5       | ---      | Nonir   | Number of ONIR sources in the ~2Ms CDF-S region                       |
| 37- 39  | F3.1     | arcsec   | sigmao  | 1{sigma} positional error of the ONIR sources                         |
| 41- 44  | F4.2     | ---      | Lth     | Threshold value for the likelihood ratio (4)                          |
| 46- 49  | F4.2     | ---      | R       | Sample reliability. See Section 2.2 for details.                      |
| 51- 54  | F4.2     | ---      | C       | Sample completeness. See Section 2.2 for details.                     |
| 56- 58  | I3       | ---      | Nx      | Total number of X-ray sources that are within                         |
| 60- 62  | I3       | ---      | Nid     | Number of X-ray sources identified with at least                      |
| 64- 66  | I3       | ---      | Nnoid   | Number of X-ray sources not identified                                |
| 68      | I1       | ---      | Nmul    | Number of X-ray sources identified with two ONIR                      |
| 70- 73  | F4.1     | ---      | Nfalse  | Expected number of false matches (5)                                  |
| 75      | I1       | %        | False   | False-match probability. (5)                                          |
| 77- 80  | F4.1     | %        | Recov   | Counterpart recovery rate (6)                                         |
| 82- 85  | F4.1     | %        | X-O     | Fraction of ONIR objects that are detected in                         |
| 87- 89  | I3       | ---      | Npri    | Number of primary counterparts selected from                          |
| 3       | for      | details. | Note    | (6): Defined as the expected number of true counterparts (Nid-Nfalse) |

**Note**: Catalog references as follows:
  WFI     = Giavalisco et al. (2004, Cat. II/261);
  GOODS-S = Giavalisco et al. (2004, Cat. II/261);
  GEMS    = Caldwell et al. (2008ApJS..174..136C);
  MUSIC   = Grazian et al. (2006, Cat. J/A+A/449/951);
  MUSYC   = Taylor et al. (2009, Cat. J/ApJS/183/295);
  SIMPLE  = Damen et al. (2010, ApJ, submitted);
  VLA     = Miller et al. (2008, Cat. J/ApJS/179/114).
Note (2): Note that in some cases multiple searches have been performed with
          different thresholds for deblending purposes.
Note (3): The AB magnitudes for radio sources were converted from the radio flux
          densities, m(AB)=-2.5log(F_{nu}_)-48.60.
Note (4): to discriminate between spurious and real identifications. The
          threshold value is catalog dependent, and generally scales with the
          typical values of likelihood ratios (see Equation (1)), which usually
          increase when the catalog depth or positional errors decrease.
Note (5): See Section 2.3 for details.
Note (6): Defined as the expected number of true counterparts (Nid-Nfalse)
          divided by the number of X-ray sources (Nx).
Note (7): Defined as the expected number of true counterparts (Nid-Nfalse)
          divided by the number of ONIR sources in the CDF-S region (Nonir).

</details>

<details>
<summary>table[23].dat</summary>

| Bytes   | Format   | Units   | Label     | Explanations                                  |
|:--------|:---------|:--------|:----------|:----------------------------------------------|
| 1- 3    | I3       | ---     | [LBB2008] | Running source index number (J/ApJS/179/19)   |
| 5- 8    | F4.2     | arcsec  | sigX      | 1{sigma} X-ray source positional error        |
| 10- 14  | I5       | ---     | ONIR      | ?=0 ONIR (optical/near-IR) ID number          |
| 16- 23  | F8.5     | deg     | RAdeg     | ?=0 ONIR Right Ascension (J2000)              |
| 25- 33  | F9.5     | deg     | DEdeg     | ?=0 ONIR Declination (J2000)                  |
| 35- 37  | F3.1     | arcsec  | sigO      | ?=0 1{sigma} ONIR positional error            |
| 39- 42  | F4.2     | arcsec  | off       | ?=0 X-ray source/counterpart angular distance |
| 44- 47  | F4.2     | ---     | off/s     | ?=0 Angular distance divided by quadratic sum |
| 49- 52  | F4.2     | ---     | Rc        | [0/1]? Counterpart reliability parameter      |
| 54- 60  | A7       | ---     | Cat       | ? ONIR catalog of primary counterpart         |
| 62- 66  | F5.2     | mag     | magO      | ?=0 ONIR magnitude of primary counterpart     |
| 68      | I1       | ---     | n_ONIR    | [0/1]? Muliple ONIR counterparts?             |
| 70- 77  | A8       | ---     | Note      | Remarks (only for table 2)                    |
</details>

<details>
<summary>table4a.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                               |
|:--------|:---------|:--------|:--------|:-------------------------------------------|
| 1- 5    | A5       | ---     | Filt    | Filtre, as labelled in table4              |
| 7- 11   | F5.2     | mag     | Medmag  | Median magnitude                           |
| 14- 17  | F4.2     | mag     | NMAD    | Normalized median absolute deviation (1)   |
| 19- 21  | I3       | ---     | N       | Number of X-ray sources used to derive the |

**Note**: The NMAD is a robust measure of the spread of the magnitudes ({sigma})
     in a given band, defined as NMAD=1.48xmedian(|m(AB)-median(m(AB))|).

</details>

<details>
<summary>table4.dat</summary>

| Bytes   | Format   | Units   | Label      | Explanations                                            |
|:--------|:---------|:--------|:-----------|:--------------------------------------------------------|
| 1- 3    | I3       | ---     | [LBB2008]  | Running source index number (J/ApJS/179/19) (1)         |
| 5       | A1       | ---     | l_NUV      | Upper limit flag on NUV                                 |
| 6- 10   | F5.2     | mag     | NUV        | ?=99 GALEX NUV (177-300nm) AB magnitude                 |
| 12- 16  | F5.2     | mag     | e_NUV      | ?=99 Error in NUV                                       |
| 18- 19  | I2       | ---     | f_NUV      | [-1/1] Flag on NUV (2)                                  |
| 21      | A1       | ---     | l_FUV      | Limit flag on FUV                                       |
| 22- 26  | F5.2     | mag     | FUV        | ?=99 GALEX FUV (120-177nm) AB magnitude                 |
| 28- 32  | F5.2     | mag     | e_FUV      | ?=99 Error in FUV                                       |
| 34- 35  | I2       | ---     | f_FUV      | [-1/1] Flag on FUV (2)                                  |
| 37      | A1       | ---     | l_Umag     | Limit flag on Umag                                      |
| 38- 42  | F5.2     | mag     | Umag       | ?=99 VIMOS U band AB magnitude                          |
| 44- 48  | F5.2     | mag     | e_Umag     | ?=99 Error in Umag                                      |
| 50- 52  | I3       | ---     | f_Umag     | [-1/1] Flag on Umag (2)                                 |
| 54- 58  | F5.2     | mag     | 428mag     | ?=99 COMBO-17 428nm narrow band AB magnitude            |
| 60- 64  | F5.2     | mag     | e_428mag   | ?=99 Error in 428mag                                    |
| 66- 68  | I3       | ---     | f_428mag   | [-1/1] Flag on 428mag (2)                               |
| 70- 74  | F5.2     | mag     | 462mag     | ?=99 COMBO-17 462nm narrow band AB magnitude            |
| 76- 80  | F5.2     | mag     | e_462mag   | ?=99 Error in 462mag                                    |
| 82- 84  | I3       | ---     | f_462mag   | [-1/1] Flag on 462mag (2)                               |
| 86- 90  | F5.2     | mag     | 486mag     | ?=99 COMBO-17 486nm narrow band AB magnitude            |
| 92- 96  | F5.2     | mag     | e_486mag   | ?=99 Error in 486mag                                    |
| 98-100  | I3       | ---     | f_486mag   | [-1/1] Flag on 486mag (2)                               |
| 102-106 | F5.2     | mag     | 519mag     | ?=99 COMBO-17 519nm narrow band AB magnitude            |
| 108-112 | F5.2     | mag     | e_519mag   | ?=99 Error in 519mag                                    |
| 114-116 | I3       | ---     | f_519mag   | [-1/1] Flag on 519mag (2)                               |
| 118-122 | F5.2     | mag     | 572mag     | ?=99 COMBO-17 572nm narrow band AB magnitude            |
| 124-128 | F5.2     | mag     | e_572mag   | ?=99 Error in 572mag                                    |
| 130-132 | I3       | ---     | f_572mag   | [-1/1] Flag on 572mag (2)                               |
| 134-138 | F5.2     | mag     | 605mag     | ?=99 COMBO-17 605nm narrow band AB magnitude            |
| 140-144 | F5.2     | mag     | e_605mag   | ?=99 Error in 605mag                                    |
| 146-148 | I3       | ---     | f_605mag   | [-1/1] Flag on 605mag (2)                               |
| 150-154 | F5.2     | mag     | 645mag     | ?=99 COMBO-17 645nm narrow band AB magnitude            |
| 156-160 | F5.2     | mag     | e_645mag   | ?=99 Error in 645mag                                    |
| 162-164 | I3       | ---     | f_645mag   | [-1/1] Flag on 645mag (2)                               |
| 166-170 | F5.2     | mag     | 696mag     | ?=99 COMBO-17 696nm narrow band AB magnitude            |
| 172-176 | F5.2     | mag     | e_696mag   | ?=99 Error in 696mag                                    |
| 178-180 | I3       | ---     | f_696mag   | [-1/1] Flag on 696mag (2)                               |
| 182-186 | F5.2     | mag     | 753mag     | ?=99 COMBO-17 753nm narrow band AB magnitude            |
| 188-192 | F5.2     | mag     | e_753mag   | ?=99 Error in 753mag                                    |
| 194-196 | I3       | ---     | f_753mag   | [-1/1] Flag on 753mag (2)                               |
| 198-202 | F5.2     | mag     | 816mag     | ?=99 COMBO-17 816nm narrow band AB magnitude            |
| 204-208 | F5.2     | mag     | e_816mag   | ?=99 Error in 816mag                                    |
| 210-212 | I3       | ---     | f_816mag   | [-1/1] Flag on 816mag (2)                               |
| 214-218 | F5.2     | mag     | 857mag     | ?=99 COMBO-17 857nm narrow band AB magnitude            |
| 220-224 | F5.2     | mag     | e_857mag   | ?=99 Error in 857mag                                    |
| 226-228 | I3       | ---     | f_857mag   | [-1/1] Flag on 857mag (2)                               |
| 230-234 | F5.2     | mag     | 914mag     | ?=99 COMBO-17 914nm narrow band AB magnitude            |
| 236-240 | F5.2     | mag     | e_914mag   | ?=99 Error in 914mag                                    |
| 242-244 | I3       | ---     | f_914mag   | [-1/1] Flag on 914mag (2)                               |
| 246-250 | F5.2     | mag     | UCmag      | ?=99 COMBO-17 U-band AB magnitude                       |
| 252-256 | F5.2     | mag     | e_UCmag    | ?=99 Error in UCmag                                     |
| 258-260 | I3       | ---     | f_UCmag    | [-1/1] Flag on UCmag (2)                                |
| 262-266 | F5.2     | mag     | BCmag      | ?=99 COMBO-17 B-band AB magnitude                       |
| 268-272 | F5.2     | mag     | e_BCmag    | ?=99 Error in BCmag                                     |
| 274-276 | I3       | ---     | f_BCmag    | [-1/1] Flag on BCmag (2)                                |
| 278-282 | F5.2     | mag     | VCmag      | ?=99 COMBO-17 V-band AB magnitude                       |
| 284-288 | F5.2     | mag     | e_VCmag    | ?=99 Error in VCmag                                     |
| 290-292 | I3       | ---     | f_VCmag    | [-1/1] Flag on VCmag (2)                                |
| 294-298 | F5.2     | mag     | RCmag      | ?=99 COMBO-17 R-band AB magnitude                       |
| 300-304 | F5.2     | mag     | e_RCmag    | ?=99 Error in RCmag                                     |
| 306-308 | I3       | ---     | f_RCmag    | [-1/1] Flag on RCmag (2)                                |
| 310-314 | F5.2     | mag     | ICmag      | ?=99 COMBO-17 I-band AB magnitude                       |
| 316-320 | F5.2     | mag     | e_ICmag    | ?=99 Error in ICmag                                     |
| 322-324 | I3       | ---     | f_ICmag    | [-1/1] Flag on ICmag (2)                                |
| 326-330 | F5.2     | mag     | UM1mag     | ?=99 MUSYC BVR-detected U-band AB magnitude             |
| 332-336 | F5.2     | mag     | e_UM1mag   | ?=99 Error in UM1mag                                    |
| 338-340 | I3       | ---     | f_UM1mag   | [-1/1] Flag on UM1mag (2)                               |
| 342-346 | F5.2     | mag     | BM1mag     | ?=99 MUSYC BVR-detected B-band AB magnitude             |
| 348-352 | F5.2     | mag     | e_BM1mag   | ?=99 Error in BM1mag                                    |
| 354-356 | I3       | ---     | f_BM1mag   | [-1/1] Flag on BM1mag (2)                               |
| 358-362 | F5.2     | mag     | VM1mag     | ?=99 MUSYC BVR-detected V-band AB magnitude             |
| 364-368 | F5.2     | mag     | e_VM1mag   | ?=99 Error in VM1mag                                    |
| 370-372 | I3       | ---     | f_VM1mag   | [-1/1] Flag on VM1mag (2)                               |
| 374-378 | F5.2     | mag     | RM1mag     | ?=99 MUSYC BVR-detected R-band AB magnitude             |
| 380-384 | F5.2     | mag     | e_RM1mag   | ?=99 Error in RM1mag                                    |
| 386-388 | I3       | ---     | f_RM1mag   | [-1/1] Flag on RM1mag (2)                               |
| 390-394 | F5.2     | mag     | IM1mag     | ?=99 MUSYC BVR-detected I-band AB magnitude             |
| 396-400 | F5.2     | mag     | e_IM1mag   | ?=99 Error in IM1mag                                    |
| 402-404 | I3       | ---     | f_IM1mag   | [-1/1] Flag on IM1mag (2)                               |
| 406-410 | F5.2     | mag     | zM1mag     | ?=99 MUSYC BVR-detected z-band AB magnitude             |
| 412-416 | F5.2     | mag     | e_zM1mag   | ?=99 Error in zM1mag                                    |
| 418-420 | I3       | ---     | f_zM1mag   | [-1/1] Flag on zM1mag (2)                               |
| 422-426 | F5.2     | mag     | o3M1mag    | ?=99 MUSYC BVR-detected o3 (501nm) AB magnitude         |
| 428-432 | F5.2     | mag     | e_o3M1mag  | ?=99 Error in o3M1mag                                   |
| 434-436 | I3       | ---     | f_o3M1mag  | [-1/1] Flag on o3M1mag (2)                              |
| 438     | A1       | ---     | l_BM2mag   | Limit flag on BM2mag                                    |
| 439-443 | F5.2     | mag     | BM2mag     | ?=99 MUSYC K-detected B-band AB magnitude               |
| 445-449 | F5.2     | mag     | e_BM2mag   | ?=99 Error in BM2mag                                    |
| 451-453 | I3       | ---     | f_BM2mag   | [-1/1] Flag on BM2mag (2)                               |
| 455     | A1       | ---     | l_VM2mag   | Limit flag on VM2mag                                    |
| 456-460 | F5.2     | mag     | VM2mag     | ?=99 MUSYC K-detected V-band AB magnitude               |
| 462-466 | F5.2     | mag     | e_VM2mag   | ?=99 Error in VM2mag                                    |
| 468-470 | I3       | ---     | f_VM2mag   | [-1/1] Flag on VM2mag (2)                               |
| 472-476 | F5.2     | mag     | RM2mag     | ?=99 MUSYC K-detected R-band AB magnitude               |
| 478-482 | F5.2     | mag     | e_RM2mag   | ?=99 Error in RM2mag                                    |
| 484-486 | I3       | ---     | f_RM2mag   | [-1/1] Flag on RM2mag (2)                               |
| 488     | A1       | ---     | l_IM2mag   | Limit flag on IM2mag                                    |
| 489-493 | F5.2     | mag     | IM2mag     | ?=99 MUSYC K-detected I-band AB magnitude               |
| 495-499 | F5.2     | mag     | e_IM2mag   | ?=99 Error in IM2mag                                    |
| 501-503 | I3       | ---     | f_IM2mag   | [-1/1] Flag on IM2mag (2)                               |
| 505-509 | F5.2     | mag     | zM2mag     | ?=99 MUSYC K-detected z-band AB magnitude               |
| 511-515 | F5.2     | mag     | e_zM2mag   | ?=99 Error in zM2mag                                    |
| 517-519 | I3       | ---     | f_zM2mag   | [-1/1] Flag on zM2mag (2)                               |
| 521     | A1       | ---     | l_JM2mag   | Limit flag on JM2mag                                    |
| 522-526 | F5.2     | mag     | JM2mag     | ?=99 MUSYC K-detected J-band AB magnitude               |
| 528-532 | F5.2     | mag     | e_JM2mag   | ?=99 Error in JM2mag                                    |
| 534-536 | I3       | ---     | f_JM2mag   | [-1/1] Flag on JM2mag (2)                               |
| 538     | A1       | ---     | l_KM2mag   | Limit flag on KM2mag                                    |
| 539-543 | F5.2     | mag     | KM2mag     | ?=99 MUSYC K-detected K-band AB magnitude               |
| 545-549 | F5.2     | mag     | e_KM2mag   | ?=99 Error in KM2mag                                    |
| 551-553 | I3       | ---     | f_KM2mag   | [-1/1] Flag on KM2mag (2)                               |
| 555-559 | F5.2     | mag     | U35GMmag   | ?=99 GOODS-S MUSIC U35 AB magnitude                     |
| 561-565 | F5.2     | mag     | e_U35GMmag | ?=99 Error in U35GMmag                                  |
| 567-569 | I3       | ---     | f_U35GMmag | [-1/1] Flag on U35GMmag (2)                             |
| 571-575 | F5.2     | mag     | U38GMmag   | ?=99 GOODS-S MUSIC U38 AB magnitude                     |
| 577-581 | F5.2     | mag     | e_U38GMmag | ?=99 Error in U38GMmag                                  |
| 583-585 | I3       | ---     | f_U38GMmag | [-1/1] Flag on U38GMmag (2)                             |
| 587-591 | F5.2     | mag     | UGMmag     | ?=99 GOODS-S MUSIC U-band AB magnitude                  |
| 593-597 | F5.2     | mag     | e_UGMmag   | ?=99 Error in UGMmag                                    |
| 599-601 | I3       | ---     | f_UGMmag   | [-1/1] Flag on UGMmag (2)                               |
| 603-607 | F5.2     | mag     | BGMmag     | ?=99 GOODS-S MUSIC F435W AB magnitude                   |
| 609-613 | F5.2     | mag     | e_BGMmag   | ?=99 Error in BGMmag                                    |
| 615-617 | I3       | ---     | f_BGMmag   | [-1/1] Flag on BGMmag (2)                               |
| 619-623 | F5.2     | mag     | VGMmag     | ?=99 GOODS-S MUSIC F606W AB magnitude                   |
| 625-629 | F5.2     | mag     | e_VGMmag   | ?=99 Error in VGMmag                                    |
| 631-633 | I3       | ---     | f_VGMmag   | [-1/1] Flag on VGMmag (2)                               |
| 635-639 | F5.2     | mag     | iGMmag     | ?=99 GOODS-S MUSIC F775W AB magnitude                   |
| 641-645 | F5.2     | mag     | e_iGMmag   | ?=99 Error in iGMmag                                    |
| 647-649 | I3       | ---     | f_iGMmag   | [-1/1] Flag on iGMmag (2)                               |
| 651-655 | F5.2     | mag     | zGMmag     | ?=99 GOODS-S MUSIC F850LP AB magnitude                  |
| 657-661 | F5.2     | mag     | e_zGMmag   | ?=99 Error in zGMmag                                    |
| 663-665 | I3       | ---     | f_zGMmag   | [-1/1] Flag on zGMmag (2)                               |
| 667-671 | F5.2     | mag     | JGMmag     | ?=99 GOODS-S MUSIC J AB magnitude                       |
| 673-677 | F5.2     | mag     | e_JGMmag   | ?=99 Error in JGMmag                                    |
| 679-681 | I3       | ---     | f_JGMmag   | [-1/1] Flag on JGMmag (2)                               |
| 683-687 | F5.2     | mag     | HGMmag     | ?=99 GOODS-S MUSIC H AB magnitude                       |
| 689-693 | F5.2     | mag     | e_HGMmag   | ?=99 Error in HGMmag                                    |
| 695-697 | I3       | ---     | f_HGMmag   | [-1/1] Flag on HGMmag (2)                               |
| 699-703 | F5.2     | mag     | KGMmag     | ?=99 GOODS-S MUSIC K AB magnitude                       |
| 705-709 | F5.2     | mag     | e_KGMmag   | ?=99 Error in KGMmag                                    |
| 711-713 | I3       | ---     | f_KGMmag   | [-1/1] Flag on KGMmag (2)                               |
| 715-719 | F5.2     | mag     | 3.6GMmag   | ?=99 GOODS-S MUSIC 3.6um AB magnitude                   |
| 721-725 | F5.2     | mag     | e_3.6GMmag | ?=99 Error in 3.6GMmag                                  |
| 727-729 | I3       | ---     | f_3.6GMmag | [-1/1] Flag on 3.6GMmag (2)                             |
| 731-735 | F5.2     | mag     | 4.5GMmag   | ?=99 GOODS-S MUSIC 4.5um AB magnitude                   |
| 737-741 | F5.2     | mag     | e_4.5GMmag | ?=99 Error in 4.5GMmag                                  |
| 743-745 | I3       | ---     | f_4.5GMmag | [-1/1] Flag on 4.5GMmag (2)                             |
| 747-751 | F5.2     | mag     | 5.8GMmag   | ?=99 GOODS-S MUSIC 5.8um AB magnitude                   |
| 753-757 | F5.2     | mag     | e_5.8GMmag | ?=99 Error in 5.8GMmag                                  |
| 759-761 | I3       | ---     | f_5.8GMmag | [-1/1] Flag on 5.8GMmag (2)                             |
| 763-767 | F5.2     | mag     | 8.0GMmag   | ?=99 GOODS-S MUSIC 8.0um AB magnitude                   |
| 769-773 | F5.2     | mag     | e_8.0GMmag | ?=99 Error in 8.0GMmag                                  |
| 775-777 | I3       | ---     | f_8.0GMmag | [-1/1] Flag on 8.0GMmag (2)                             |
| 779     | A1       | ---     | l_RWmag    | Limit flag on RWmag                                     |
| 780-784 | F5.2     | mag     | RWmag      | ?=99 WFI catalog R-band AB magnitude                    |
| 786-790 | F5.2     | mag     | e_RWmag    | ?=99 Error in RWmag                                     |
| 792-794 | I3       | ---     | f_RWmag    | [-1/1] Flag on RWmag (2)                                |
| 796-800 | F5.2     | mag     | BGmag      | ?=99 GOODS-S catalog F435W AB magnitude                 |
| 802-806 | F5.2     | mag     | e_BGmag    | ?=99 Error in BGmag                                     |
| 808-810 | I3       | ---     | f_BGmag    | [-1/1] Flag on BGmag (2)                                |
| 812-816 | F5.2     | mag     | VGSmag     | ?=99 GOODS-S catalog F606W AB magnitude                 |
| 818-822 | F5.2     | mag     | e_VGSmag   | ?=99 Error in VGSmag                                    |
| 824-826 | I3       | ---     | f_VGSmag   | [-1/1] Flag on VGSmag (2)                               |
| 828-832 | F5.2     | mag     | iGSmag     | ?=99 GOODS-S catalog F775W AB magnitude                 |
| 834-838 | F5.2     | mag     | e_iGSmag   | ?=99 Error in iGSmag                                    |
| 840-842 | I3       | ---     | f_iGSmag   | [-1/1] Flag on iGSmag (2)                               |
| 844     | A1       | ---     | l_zGSmag   | Limit flag on zGSmag                                    |
| 845-849 | F5.2     | mag     | zGSmag     | ?=99 GOODS-S catalog F850LP AB magnitude                |
| 851-855 | F5.2     | mag     | e_zGSmag   | ?=99 Error in zGSmag                                    |
| 857-859 | I3       | ---     | f_zGSmag   | [-1/1] Flag on zGSmag (2)                               |
| 861-865 | F5.2     | mag     | VGmag      | ?=99 GEMS catalog F606W AB magnitude                    |
| 867-871 | F5.2     | mag     | e_VGmag    | ?=99 Error in VGmag                                     |
| 873-875 | I3       | ---     | f_VGmag    | [-1/1] Flag on VGmag (2)                                |
| 877     | A1       | ---     | l_zGmag    | Limit flag on zGmag                                     |
| 878-882 | F5.2     | mag     | zGmag      | ?=99 GEMS catalog F850LP AB magnitude                   |
| 884-888 | F5.2     | mag     | e_zGmag    | ?=99 Error in zGmag                                     |
| 890-892 | I3       | ---     | f_zGmag    | [-1/1] Flag on zGmag (2)                                |
| 894-898 | F5.2     | mag     | 3.6S       | ?=99 SIMPLE catalog 3.6um AB magnitude                  |
| 900-904 | F5.2     | mag     | e_3.6S     | ?=99 Error in 3.6S                                      |
| 906-908 | I3       | ---     | f_3.6S     | [-1/1] Flag on 3.6S (2)                                 |
| 910-914 | F5.2     | mag     | 4.5S       | ?=99 SIMPLE catalog 4.5um AB magnitude                  |
| 916-920 | F5.2     | mag     | e_4.5S     | ?=99 Error in 4.5S                                      |
| 922-924 | I3       | ---     | f_4.5S     | [-1/1] Flag on 4.5S (2)                                 |
| 926     | A1       | ---     | l_5.8S     | Limit flag on 5.8S                                      |
| 927-931 | F5.2     | mag     | 5.8S       | ?=99 SIMPLE catalog 5.8um AB magnitude                  |
| 933-937 | F5.2     | mag     | e_5.8S     | ?=99 Error in 5.8S                                      |
| 939-941 | I3       | ---     | f_5.8S     | [-1/1] Flag on 5.8S (2)                                 |
| 943     | A1       | ---     | l_8.0S     | Limit flag on 8.0S                                      |
| 944-948 | F5.2     | mag     | 8.0S       | ?=99 SIMPLE catalog 8.0um AB magnitude                  |
| 950-954 | F5.2     | mag     | e_8.0S     | ?=99 Error in 8.0S                                      |
| 956-958 | I3       | ---     | f_8.0S     | [-1/1] Flag on 8.0S (2)                                 |
| 960-964 | F5.2     | mag     | VLA        | ?=99 VLA 1.4GHz magnitude in AB system                  |
| 966-970 | F5.2     | mag     | e_VLA      | ?=99 Error in VLA                                       |
| 972-973 | I2       | ---     | f_VLA      | [-1/1] Flag on VLA (2)                                  |
| 1       | =        | the     | data       | point was used in the photometric redshift calculation, |
| 0       | =        | the     | data       | point was not used or not available,                    |
| 1       | =        | the     | data       | point is probably problematic, either being blended or  |

**Note**: The radio data are used only in the X-ray source identification
     process, and are not used in the photometric redshift calculation.
     All photometric data are given in AB magnitudes.
     For the first line, value in parenthesis:
Note (2): the flag has the values:
    1 = the data point was used in the photometric redshift calculation,
    0 = the data point was not used or not available,
   -1 = the data point is probably problematic, either being blended or
        disagreeing with other data.

</details>

<details>
<summary>table5.dat</summary>

| Bytes   | Format   | Units     | Label            | Explanations                                                              |
|:--------|:---------|:----------|:-----------------|:--------------------------------------------------------------------------|
| 1- 3    | I3       | ---       | [LBB2008]        | Running source index number (J/ApJS/179/19)                               |
| 5- 10   | F6.3     | ---       | zs               | ?=-1 Spectroscopic redshift                                               |
| 12- 17  | F6.3     | ---       | zp               | ?=-1 ZEBRA derived photometric redshift (3)                               |
| 19- 24  | F6.3     | ---       | zLow             | ?=-1 Lower 1{sigma} redshift confidence interval                          |
| 26- 31  | F6.3     | ---       | zUp              | ?=-1 Upper 1{sigma} redshift confidence interval                          |
| 33- 34  | I2       | ---       | NDet             | Number of filters source is detected                                      |
| 36- 37  | I2       | ---       | NFilt            | Number of filters used in the zp calculation                              |
| 39- 43  | F5.2     | ---       | chi2             | Reduced {chi}^2^ of best-fit result                                       |
| 45- 50  | F6.3     | ---       | Azp              | ?=-1 Alternative photometric redshift                                     |
| 52- 56  | F5.2     | ---       | Achi2            | ?=-1 Reduced {chi}^2^ for alternative zp                                  |
| 58      | I1       | ---       | ODet             | [0/1] X-ray source detected in optical? (4)                               |
| 60- 61  | I2       | ---       | r_zs             | ?=-1 zs reference code (5)                                                |
| 16      | sources  | without   | identifications. | Note (4): A value of "0" means no optical detection, in which case the zp |
| 20      | sources  | in        | the              | photometric sample that do not have optical detections.                   |
| 1       | =        | Le        | Fevre            | et al. (2004, Cat. J/A+A/428/1043)                                        |
| 2       | =        | Szokoly   | et               | al. (2004, Cat. J/ApJS/155/271)                                           |
| 3       | =        | Zheng     | et               | al. (2004, Cat. J/ApJS/155/73)                                            |
| 4       | =        | Mignoli   | et               | al. (2005, Cat. J/A+A/437/883)                                            |
| 5       | =        | Ravikumar | et               | al. (2007, Cat. J/A+A/465/1099)                                           |
| 6       | =        | Vanzella  | et               | al. (2008, Cat. J/A+A/478/83)                                             |
| 7       | =        | Popesso   | et               | al. (2009A&A...494..443P)                                                 |
| 8       | =        | Silverman | et               | al. (2010, in prep)                                                       |

**Note**: Set to "0" for the six stars and "-1" for the 16 sources without
     identifications.
Note (4): A value of "0" means no optical detection, in which case the zp
     was calculated using only the IR/NIR data and the optical upper-limit
     information (and is probably not very reliable). There are 20 sources
     in the photometric sample that do not have optical detections.
Note (5): References as follows:
      1 = Le Fevre et al. (2004, Cat. J/A+A/428/1043)
      2 = Szokoly et al. (2004, Cat. J/ApJS/155/271)
      3 = Zheng et al. (2004, Cat. J/ApJS/155/73)
      4 = Mignoli et al. (2005, Cat. J/A+A/437/883)
      5 = Ravikumar et al. (2007, Cat. J/A+A/465/1099)
      6 = Vanzella et al. (2008, Cat. J/A+A/478/83)
      7 = Popesso et al. (2009A&A...494..443P)
      8 = Silverman et al. (2010, in prep)

</details>
