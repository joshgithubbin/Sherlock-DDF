**Authors:** Brandt W.N., Alexander D.M., Xue Y.Q., Bauer F.E.,, Lehmer B.D., Luo B., Papovich C., <Astrophys. J., 742, 3 (2011)>, =2011ApJ...742....3R

## Summary: Photometric catalogs for ECDF-S and CDF-N 

We present an analysis of deep multiwavelength data for z~0.3-3 starburst galaxies selected by their 70um emission in the Extended-Chandra Deep Field-South and Extended Groth Strip. We identify active galactic nuclei (AGNs) in these infrared sources through their X-ray emission and quantify the fraction that host an AGN. Lastly, we investigate the ratio between the supermassive black hole accretion rate (inferred from the AGN X-ray luminosity) and the bulge growth rate of the host galaxy (approximated as the SFR) and find that, for sources with detected AGNs and star formation (and neglecting systems with low star formation rates to which our data are insensitive), this ratio in distant starbursts agrees well with that expected from the local scaling relation assuming the black holes and bulges grew at the same epoch. These results imply that black holes and bulges grow together during periods of vigorous star formation and AGN activity.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-742-3/Subcatalogues/ECDFS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zsp:** [0.0/5.5]?=-1 Spectroscopic redshift 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-742-3/Subcatalogues/ECDFS/Plots/zspec.png)
## Photometric Redshift 
 
**b_zph:** Lower 68% confidence interval on zph 
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-742-3/Subcatalogues/ECDFS/Plots/zphot.png)
## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units      | Label     | Explanations                                                  |
|:--------|:---------|:-----------|:----------|:--------------------------------------------------------------|
| 1- 10   | F10.7    | deg        | RAdeg     | [52.80/53.42] Right Ascension J2000)                          |
| 12- 22  | F11.7    | deg        | DEdeg     | [-28.07/-27.52] Declination (J2000)                           |
| 24- 32  | F9.7     | ---        | zph       | [0/6.3] Photometric redshift                                  |
| 34- 42  | F9.7     | ---        | b_zph     | Lower 68% confidence interval on zphot                        |
| 44- 52  | F9.7     | ---        | B_zph     | Upper 68% confidence interval on zphot                        |
| 54- 62  | F9.7     | ---        | lz95      | Lower 95% confidence interval on zphot                        |
| 64- 72  | F9.7     | ---        | uz95      | Upper 95% confidence interval on zphot                        |
| 74- 80  | F7.4     | ---        | zsp       | [0.0034/5.828]?=-1 Spectroscopic redshift                     |
| 82- 83  | I2       | ---        | r_zsp     | ?=-1 Reference for zsp (1)                                    |
| 85- 90  | A6       | ---        | T         | Type of best-fit template (Galaxy, Hybrid, Star               |
| 92- 96  | I5       | ---        | X-ID      | ?=-1 Associated 2Ms CDF-S or 250ks                            |
| 98      | I1       | ---        | G-ID      | [0/1] Source inside GOODS-S region? (1=yes)                   |
| 100-107 | F8.4     | mag        | FUV       | ?=-99 GALEX FUV band AB magnitude (153nm) [DR4]               |
| 109-116 | F8.4     | mag        | e_FUV     | ?=-99 Uncertainty in FUV                                      |
| 118-125 | F8.4     | mag        | NUV       | ?=-99 GALEX NUV band AB magnitude (231nm) [DR4]               |
| 127-134 | F8.4     | mag        | e_NUV     | ?=-99 Uncertainty in NUV                                      |
| 136-146 | F11.7    | mag        | UMYC      | ?=-99 MUSYC U band AB magnitude (3)                           |
| 148-155 | F8.4     | mag        | e_UMYC    | ?=-99 Uncertainty in UMYC                                     |
| 157-164 | F8.4     | mag        | BMYC      | ?=-99 MUSYC B band AB magnitude (3)                           |
| 166-173 | F8.4     | mag        | e_BMYC    | ?=-99 Uncertainty in BMYC                                     |
| 175-182 | F8.4     | mag        | VMYC      | ?=-99 MUSYC V band AB magnitude (3)                           |
| 184-191 | F8.4     | mag        | e_VMYC    | ?=-99 Uncertainty in VMYC                                     |
| 193-200 | F8.4     | mag        | RMYC      | ?=-99 MUSYC R band AB magnitude (3)                           |
| 202-209 | F8.4     | mag        | e_RMYC    | ?=-99 Uncertainty in RMYC                                     |
| 211-218 | F8.4     | mag        | IMYC      | ?=-99 MUSYC I band AB magnitude (3)                           |
| 220-227 | F8.4     | mag        | e_IMYC    | ?=-99 Uncertainty in IMYC                                     |
| 229-236 | F8.4     | mag        | O3MYC     | ?=-99 MUSYC O3 (501nm) band AB magnitude (3)                  |
| 238-245 | F8.4     | mag        | e_O3MYC   | ?=-99 Uncertainty in O3MYC                                    |
| 247-254 | F8.4     | mag        | ZMYC      | ?=-99 MUSYC Z band AB magnitude (3)                           |
| 256-263 | F8.4     | mag        | e_ZMYC    | ?=-99 Uncertainty in ZMYC                                     |
| 265-272 | F8.4     | mag        | JMYC      | ?=-99 MUSYC J band AB magnitude (3)                           |
| 274-281 | F8.4     | mag        | e_JMYC    | ?=-99 Uncertainty in JMYC                                     |
| 283-290 | F8.4     | mag        | KMYC      | ?=-99 MUSYC K band AB magnitude (3)                           |
| 292-299 | F8.4     | mag        | e_KMYC    | ?=-99 Uncertainty in KMYC                                     |
| 301-308 | F8.4     | mag        | UMIC      | ?=-99 MUSIC U band AB magnitude (5)                           |
| 310-317 | F8.4     | mag        | e_UMIC    | ?=-99 Uncertainty in UMIC                                     |
| 319-325 | F7.3     | mag        | U35MIC    | ?=-99 MUSIC U_35_ band AB magnitude (359nm) (5)               |
| 327-334 | F8.4     | mag        | e_U35MIC  | ?=-99 Uncertainty in U35MIC                                   |
| 336-342 | F7.3     | mag        | U38MIC    | ?=-99 MUSIC U_38_ band AB magnitude (368nm) (5)               |
| 344-351 | F8.4     | mag        | e_U38MIC  | ?=-99 Uncertainty in U38MIC                                   |
| 353-359 | F7.3     | mag        | F435W     | ?=-99 HST/WFPC2 F435W band AB magnitude                       |
| 361-368 | F8.4     | mag        | e_F435W   | ?=-99 Uncertainty in F435W                                    |
| 370-376 | F7.3     | mag        | F606W     | ?=-99 HST/WFPC2 F606W band AB magnitude                       |
| 378-385 | F8.4     | mag        | e_F606W   | ?=-99 Uncertainty in F606W                                    |
| 387-393 | F7.3     | mag        | F775W     | ?=-99 HST/WFPC2 F775W band AB magnitude                       |
| 395-402 | F8.4     | mag        | e_F775W   | ?=-99 Uncertainty in F775W                                    |
| 404-410 | F7.3     | mag        | F850LP    | ?=-99 HST/WFPC2 F850LP band AB magnitude                      |
| 412-419 | F8.4     | mag        | e_F850LP  | ?=-99 Uncertainty in F850LP                                   |
| 421-427 | F7.3     | mag        | JMIC      | ?=-99 MUSIC J band AB magnitude (5)                           |
| 429-436 | F8.4     | mag        | e_JMIC    | ?=-99 Uncertainty in JMIC                                     |
| 438-444 | F7.3     | mag        | HMIC      | ?=-99 MUSIC H band AB magnitude (5)                           |
| 446-453 | F8.4     | mag        | e_HMIC    | ?=-99 Uncertainty in HMIC                                     |
| 455-461 | F7.3     | mag        | KMIC      | ?=-99 MUSIC K band AB magnitude (5)                           |
| 463-470 | F8.4     | mag        | e_KMIC    | ?=-99 Uncertainty in KMIC                                     |
| 472-479 | F8.4     | mag        | UC17      | ?=-99 COMBO-17 U band AB magnitude (4)                        |
| 481-488 | F8.4     | mag        | e_UC17    | ?=-99 Uncertainty in UC17                                     |
| 490-497 | F8.4     | mag        | BC17      | ?=-99 COMBO-17 B band AB magnitude (4)                        |
| 499-506 | F8.4     | mag        | e_BC17    | ?=-99 Uncertainty in BC17                                     |
| 508-515 | F8.4     | mag        | VC17      | ?=-99 COMBO-17 V band AB magnitude (4)                        |
| 517-524 | F8.4     | mag        | e_VC17    | ?=-99 Uncertainty in VC17                                     |
| 526-533 | F8.4     | mag        | RC17      | ?=-99 COMBO-17 R band AB magnitude (4)                        |
| 535-542 | F8.4     | mag        | e_RC17    | ?=-99 Uncertainty in RC17                                     |
| 544-551 | F8.4     | mag        | IC17      | ?=-99 COMBO-17 I band AB magnitude (4)                        |
| 553-560 | F8.4     | mag        | e_IC17    | ?=-99 Uncertainty in IC17                                     |
| 562-569 | F8.4     | mag        | 420C17    | ?=-99 COMBO-17 filter 420nm AB magnitude (4)                  |
| 571-578 | F8.4     | mag        | e_420C17  | ?=-99 Uncertainty in 420C17                                   |
| 580-587 | F8.4     | mag        | 464C17    | ?=-99 COMBO-17 filter 464nm AB magnitude (4)                  |
| 589-596 | F8.4     | mag        | e_464C17  | ?=-99 Uncertainty in 464C17                                   |
| 598-605 | F8.4     | mag        | 485C17    | ?=-99 COMBO-17 filter 485nm AB magnitude (4)                  |
| 607-614 | F8.4     | mag        | e_485C17  | ?=-99 Uncertainty in 485C17                                   |
| 616-623 | F8.4     | mag        | 518C17    | ?=-99 COMBO-17 filter 518nm AB magnitude (4)                  |
| 625-632 | F8.4     | mag        | e_518C17  | ?=-99 Uncertainty in 518C17                                   |
| 634-641 | F8.4     | mag        | 571C17    | ?=-99 COMBO-17 filter 571nm AB magnitude (4)                  |
| 643-650 | F8.4     | mag        | e_571C17  | ?=-99 Uncertainty in 571C17                                   |
| 652-659 | F8.4     | mag        | 604C17    | ?=-99 COMBO-17 filter 604nm AB magnitude (4)                  |
| 661-668 | F8.4     | mag        | e_604C17  | ?=-99 Uncertainty in 604C17                                   |
| 670-677 | F8.4     | mag        | 646C17    | ?=-99 COMBO-17 filter 646nm AB magnitude (4)                  |
| 679-686 | F8.4     | mag        | e_646C17  | ?=-99 Uncertainty in 646C17                                   |
| 688-695 | F8.4     | mag        | 696C17    | ?=-99 COMBO-17 filter 696nm AB magnitude (4)                  |
| 697-704 | F8.4     | mag        | e_696C17  | ?=-99 Uncertainty in 696C17                                   |
| 706-713 | F8.4     | mag        | 753C17    | ?=-99 COMBO-17 filter 753nm AB magnitude (4)                  |
| 715-722 | F8.4     | mag        | e_753C17  | ?=-99 Uncertainty in 753C17                                   |
| 724-731 | F8.4     | mag        | 815C17    | ?=-99 COMBO-17 filter 815nm AB magnitude (4)                  |
| 733-740 | F8.4     | mag        | e_815C17  | ?=-99 Uncertainty in 815C17                                   |
| 742-749 | F8.4     | mag        | 855C17    | ?=-99 COMBO-17 filter 855nm AB magnitude (4)                  |
| 751-758 | F8.4     | mag        | e_855C17  | ?=-99 Uncertainty in 855C17                                   |
| 760-767 | F8.4     | mag        | 915C17    | ?=-99 COMBO-17 filter 915nm AB magnitude (4)                  |
| 769-776 | F8.4     | mag        | e_915C17  | ?=-99 Uncertainty in 915C17                                   |
| 778-785 | F8.4     | mag        | [3.6]     | ?=-99 Spitzer/IRAC 3.6um band AB magnitude (6)                |
| 787-794 | F8.4     | mag        | e_[3.6]   | ?=-99 Uncertainty in [3.6]                                    |
| 796-803 | F8.4     | mag        | [4.5]     | ?=-99 Spitzer/IRAC 4.5um band AB magnitude (6)                |
| 805-812 | F8.4     | mag        | e_[4.5]   | ?=-99 Uncertainty in [4.5]                                    |
| 814-821 | F8.4     | mag        | [5.8]     | ?=-99 Spitzer/IRAC 5.8um band AB magnitude (6)                |
| 823-830 | F8.4     | mag        | e_[5.8]   | ?=-99 Uncertainty in [5.8]                                    |
| 832-839 | F8.4     | mag        | [8.0]     | ?=-99 Spitzer/IRAC 8.0um band AB magnitude (6)                |
| 841-848 | F8.4     | mag        | e_[8.0]   | ?=-99 Uncertainty in [8.0]                                    |
| 1       | =        | Vanzella   | et        | al. 2008, Cat. J/A+A/478/83;                                  |
| 2       | =        | Le         | Fevre     | et al. 2004, Cat. J/A+A/428/1043;                             |
| 3       | =        | Szokoly    | et        | al. 2004, Cat. J/ApJS/155/271;                                |
| 4       | =        | Croom      | et        | al. 2001, Cat. J/MNRAS/328/150;                               |
| 5       | =        | Dickinson  | et        | al. 2004, Cat. J/ApJ/600/L99;                                 |
| 6       | =        | van        | der       | Wel et al. 2004ApJ...601L...5V;                               |
| 7       | =        | Bunker     | et        | al. 2003MNRAS.342L..47B;                                      |
| 8       | =        | Stanway    | et        | al. 2004ApJ...607..704S;                                      |
| 9       | =        | Mignoli    | et        | al. 2005, Cat. J/A+A/437/883;                                 |
| 10      | =        | Silverman, | Mainieri, | et al., in preparation;                                       |
| 11      | =        | Cristiani  | et        | al. 2000A&A...359..489C;                                      |
| 12      | =        | Strolger   | et        | al. 2004, Cat. J/ApJ/613/200;                                 |
| 13      | =        | Ravikumar  | et        | al. 2007, Cat. J/A+A/465/1099;                                |
| 14      | =        | Stanway    | et        | al. 2004ApJ...607..704S;                                      |
| 15      | =        | Treister   | et        | al. 2009, Cat. J/ApJ/693/1713;                                |
| 16      | =        | Popesso    | et        | al. 2009A&A...494..443P (VIMOS VLT low-resolution survey);    |
| 17      | =        | Popesso    | et        | al. 2009A&A...494..443P (VIMOS VLT medium-resolution survey); |
| 18      | =        | Grazian    | et        | al. 2006, Cat. J/A+A/449/951;                                 |
| 19      | =        | Zheng      | et        | al. 2004, Cat. J/ApJS/155/73.                                 |
| 1003    | to       | -1033      | numbers   | and                                                           |
| 17      | optical  | catalog    | (Wolf     | et al. 2004, Cat. II/253;                                     |

**Note**: Spectroscopic reference as follows:
   1 = Vanzella et al. 2008, Cat. J/A+A/478/83;
   2 = Le Fevre et al. 2004, Cat. J/A+A/428/1043;
   3 = Szokoly et al. 2004, Cat. J/ApJS/155/271;
   4 = Croom et al. 2001, Cat. J/MNRAS/328/150;
   5 = Dickinson et al. 2004, Cat. J/ApJ/600/L99;
   6 = van der Wel et al. 2004ApJ...601L...5V;
   7 = Bunker et al. 2003MNRAS.342L..47B;
   8 = Stanway et al. 2004ApJ...607..704S;
   9 = Mignoli et al. 2005, Cat. J/A+A/437/883;
  10 = Silverman, Mainieri, et al., in preparation;
  11 = Cristiani et al. 2000A&A...359..489C;
  12 = Strolger et al. 2004, Cat. J/ApJ/613/200;
  13 = Ravikumar et al. 2007, Cat. J/A+A/465/1099;
  14 = Stanway et al. 2004ApJ...607..704S;
  15 = Treister et al. 2009, Cat. J/ApJ/693/1713;
  16 = Popesso et al. 2009A&A...494..443P (VIMOS VLT low-resolution survey);
  17 = Popesso et al. 2009A&A...494..443P (VIMOS VLT medium-resolution survey);
  18 = Grazian et al. 2006, Cat. J/A+A/449/951;
  19 = Zheng et al. 2004, Cat. J/ApJS/155/73.
Note (2): ID of the associated X-ray source (if any) from the 2Ms CDF-S catalog
          of Luo et al. (2008, Cat. J/ApJS/179/19, <[LBB2008] NNN> in Simbad) or
          the 250ks E-CDF-S catalog of Lehmer et al. (2005, Cat. J/ApJS/161/21,
          <[LBA2005] SNN> in Simbad (S1-S33) for -1003 to -1033 numbers and
          <[LBA2005] NNN> in Simbad) for other negative numbers.
Note (3): From the MUSYC BVR-detected optical catalog (Gawiser et al.
          2006, Cat. J/ApJS/162/1) and the MUSYC near-infrared catalog (Taylor
          et al. 2009, Cat. J/ApJS/183/295)
Note (4): From the COMBO-17 optical catalog (Wolf et al. 2004, Cat. II/253;
          2008A&A...492..933W)
Note (5): From the MUSIC catalog (Grazian et al. 2006, Cat. J/A+A/449/951)
Note (6): From the SIMPLE Spitzer IRAC catalog (Damen et al.
          2009ApJ...690..937D)

</details>

<details>
<summary>table3.dat</summary>

| Bytes   | Format   | Units    | Label    | Explanations                                    |
|:--------|:---------|:---------|:---------|:------------------------------------------------|
| 1- 11   | F11.7    | deg      | RAdeg    | [188.740/189.692] Right Ascension (J2000)       |
| 13- 22  | F10.7    | deg      | DEdeg    | [61.963/62.410] Declination (J2000)             |
| 24- 30  | F7.5     | ---      | zph      | [0/6.04918] Photometric redshift                |
| 32- 38  | F7.5     | ---      | b_zph    | Lower 68% confidence interval on zph            |
| 40- 46  | F7.5     | ---      | B_zph    | Upper 68% confidence interval on zph            |
| 48- 54  | F7.5     | ---      | lz95     | Lower 95% confidence interval on zph            |
| 56- 62  | F7.5     | ---      | uz95     | Upper 95% confidence interval on zph            |
| 64- 71  | F8.5     | ---      | zsp      | [0.0/5.5]?=-1 Spectroscopic redshift            |
| 73- 74  | I2       | ---      | r_zsp    | [1/7]?=-1 Reference for zsp (1)                 |
| 76      | I1       | ---      | T        | [0/4] Type of best-fit template (4=WD, 3=star,  |
| 78- 80  | I3       | ---      | X-ID     | [1/582]?=-1 In 2Ms CDF-N X-ray source catalog?  |
| 82      | I1       | ---      | G-ID     | [0/1] Source inside GOODS-N region? (1=yes)     |
| 84- 94  | F11.7    | mag      | Umag     | ?=-99 U band AB magnitude (2)                   |
| 96-106  | F11.7    | mag      | e_Umag   | ?=-99 Uncertainty in Umag                       |
| 108-118 | F11.7    | mag      | Bmag     | ?=-99 B band AB magnitude (2)                   |
| 120-130 | F11.7    | mag      | e_Bmag   | ?=-99 Uncertainty in Bmag                       |
| 132-142 | F11.7    | mag      | Vmag     | ?=-99 V band AB magnitude (2)                   |
| 144-154 | F11.7    | mag      | e_Vmag   | ?=-99 Uncertainty in Vmag                       |
| 156-166 | F11.7    | mag      | Rmag     | ?=-99 R band AB magnitude (2)                   |
| 168-178 | F11.7    | mag      | e_Rmag   | ?=-99 Uncertainty in Rmag                       |
| 180-190 | F11.7    | mag      | Imag     | ?=-99 I band AB magnitude (2)                   |
| 192-202 | F11.7    | mag      | e_Imag   | ?=-99 Uncertainty in Imag                       |
| 204-214 | F11.7    | mag      | Zmag     | ?=-99 Z band AB magnitude (2)                   |
| 216-226 | F11.7    | mag      | e_Zmag   | ?=-99 Uncertainty in Zmag                       |
| 228-238 | F11.7    | mag      | HKmag    | ?=-99 HK band AB magnitude (2)                  |
| 240-250 | F11.7    | mag      | e_HKmag  | ?=-99 Uncertainty in HKmag                      |
| 252-262 | F11.7    | mag      | [3.6]    | ?=-99 Spitzer/IRAC 3.6um band AB magnitude (2)  |
| 264-274 | F11.7    | mag      | e_[3.6]  | ?=-99 Uncertainty in [3.6]                      |
| 276-286 | F11.7    | mag      | [4.5]    | ?=-99 Spitzer/IRAC 4.5um band AB magnitude (2)  |
| 288-298 | F11.7    | mag      | e_[4.5]  | ?=-99 Uncertainty in [4.5]                      |
| 300-310 | F11.7    | mag      | [5.8]    | ?=-99 Spitzer/IRAC 5.8um band AB magnitude (2)  |
| 312-322 | F11.7    | mag      | e_[5.8]  | ?=-99 Uncertainty in [5.8]                      |
| 324-334 | F11.7    | mag      | [8.0]    | ?=-99 Spitzer/IRAC 8.0um band AB magnitude (2)  |
| 336-346 | F11.7    | mag      | e_[8.0]  | ?=-99 Uncertainty in [8.0]                      |
| 348-358 | F11.7    | mag      | F435W    | ?=-99 HST/WFPC2 F435W band mag (2)              |
| 360-370 | F11.7    | mag      | e_F435W  | ?=-99 Uncertainty in F435W                      |
| 372-382 | F11.7    | mag      | F606W    | ?=-99 HST/WFPC2 F606W band AB magnitude (2)     |
| 384-394 | F11.7    | mag      | e_F606W  | ?=-99 Uncertainty in F606W                      |
| 396-406 | F11.7    | mag      | F775W    | ?=-99 HST/WFPC2 F775W band mag (2)              |
| 408-418 | F11.7    | mag      | e_F775W  | ?=-99 Uncertainty in F775W                      |
| 420-430 | F11.7    | mag      | F850LP   | ?=-99 HST/WFPC2 F850LP band AB magnitude (2)    |
| 432-442 | F11.7    | mag      | e_F850LP | ?=-99 Uncertainty in F850LP                     |
| 444-454 | F11.7    | mag      | NUV      | ?=-99 GALEX NUV band AB magnitude (231nm) [DR4] |
| 456-466 | F11.7    | mag      | e_NUV    | ?=-99 Uncertainty in NUV                        |
| 468-478 | F11.7    | mag      | FUV      | ?=-99 GALEX FUV band AB magnitude (153nm) [DR4] |
| 480-490 | F11.7    | mag      | e_FUV    | ?=-99 Uncertainty in FUV                        |
| 492-502 | F11.7    | mag      | Kmag     | ?=-99 Ks band AB magnitude (3)                  |
| 1       | =        | Barger   | et       | al. (2008, Cat. J/ApJ/689/687);                 |
| 2       | =        | Cowie    | et       | al. (2004, Cat. J/AJ/127/3137);                 |
| 3       | =        | Wirth    | et       | al. (2004, Cat. J/AJ/127/3121);                 |
| 4       | =        | Reddy    | et       | al. (2006, Cat. J/ApJ/653/1004);                |
| 5       | =        | Barger   | et       | al. (2003, Cat. J/AJ/126/632);                  |
| 6       | =        | Trouille | et       | al. (2008, Cat. J/ApJS/179/1);                  |
| 7       | =        | Chapman  | et       | al. (2005, Cat. J/ApJ/622/772).                 |

**Note**: Reference as follows:
   1 = Barger et al. (2008, Cat. J/ApJ/689/687);
   2 = Cowie et al. (2004, Cat. J/AJ/127/3137);
   3 = Wirth et al. (2004, Cat. J/AJ/127/3121);
   4 = Reddy et al. (2006, Cat. J/ApJ/653/1004);
   5 = Barger et al. (2003, Cat. J/AJ/126/632);
   6 = Trouille et al. (2008, Cat. J/ApJS/179/1);
   7 = Chapman et al. (2005, Cat. J/ApJ/622/772).
Note (2): From the GOODS-N HST ACS and Spitzer IRAC photometric catalogs
     (Dickinson et al. 2003mglh.conf..324D) and the CDF-N Spitzer IRAC
     catalog derived from unpublished IRAC archival data.
Note (3): From the the ACS GOODS-N region Ks (<24.5) catalog (Barger et al.
     2008, Cat. J/ApJ/689/687).

</details>
