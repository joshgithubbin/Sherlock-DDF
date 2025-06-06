**Authors:** Marchesini D., Stefanon M., Franx M., Milvang-Jensen B.,, Dunlop J.S., Fynbo J.P.U., Brammer G., Labbe I., van Dokkum P., <Astrophys. J. Suppl. Ser., 206, 8 (2013)>, =2013ApJS..206....8M (SIMBAD/NED BibCode)

## Summary: COSMOS/UltraVISTA Ks-selected catalogs v4.1 

We present a catalog covering 1.62deg^2^ of the COSMOS/UltraVISTA field with point-spread function (PSF) matched photometry in 30 photometric bands. The catalog covers the wavelength range 0.15-24{mu}m including the available GALEX, Subaru, Canada-France-Hawaii Telescope, VISTA, and Spitzer data. Catalog sources have been selected from the DR1 UltraVISTA K_s_ band imaging that reaches a depth of K_s,tot_=23.4 AB (90% completeness). The PSF-matched catalog is generated using position-dependent PSFs ensuring accurate colors across the entire field. Also included is a catalog of photometric redshifts (z_phot_) for all galaxies computed with the EAZY code. Comparison with spectroscopy from the zCOSMOS 10k bright sample shows that up to z~1.5 the z_phot_ are accurate to {Delta}z/(1+z)=0.013, with a catastrophic outlier fraction of only 1.6%. The z_phot_ also show good agreement with the z_phot_ from the NEWFIRM Medium Band Survey out to z~3. A catalog of stellar masses and stellar population parameters for galaxies determined using the FAST spectral energy distribution fitting code is provided for all galaxies. Also included are rest-frame U-V and V-J colors, L_2800_ and L_IR_. The UVJ color-color diagram confirms that the galaxy bi-modality is well-established out to z~2. Star-forming galaxies also obey a star-forming "main sequence" out to z~2.5, and this sequence evolves in a manner consistent with previous measurements. The COSMOS/UltraVISTA K_s_-selected catalog covers a unique parameter space in both depth, area, and multi-wavelength coverage and promises to be a useful tool for studying the growth of the galaxy population out to z~3-4.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-206-8/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zsp:**  
 

![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-206-8/Subcatalogues/COSMOS/Plots/zspec.png)
## Photometric Redshift 
 
**zpk:** [/6]?=-1 Photometric redshift from the peak of 
 

## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes   | Format       | Units       | Label         | Explanations                                                                |
|:--------|:-------------|:------------|:--------------|:----------------------------------------------------------------------------|
| 1- 6    | I6           | ---         | Seq           | [1/262615] Running sequence number                                          |
| 8- 16   | F9.5         | deg         | RAdeg         | [149.3/150.8] Right ascension (J2000)                                       |
| 18- 26  | F9.7         | deg         | DEdeg         | [1.6/2.9] Declination (J2000)                                               |
| 28- 38  | F11.5        | pix         | xpix          | X position of object in the Ks image                                        |
| 40- 50  | F11.5        | pix         | ypix          | Y position of object in the Ks image                                        |
| 52- 61  | F10.3        | ---         | FKstot        | [-41/644028] Total Ks-band flux with apcor                                  |
| 63- 68  | F6.3         | ---         | e_FKstot      | [0.1/53] Kstot uncertainty                                                  |
| 70- 78  | F9.3         | 0.3631uJy   | FKs           | [0.01/75226] UltraVISTA Ks flux (2)                                         |
| 80- 85  | F6.3         | 0.3631uJy   | e_FKs         | [0.6/17] FKs uncertainty                                                    |
| 87- 95  | F9.3         | 0.3631uJy   | FH            | [-16/93819] UltraVISTA H flux (2)                                           |
| 97-102  | F6.3         | 0.3631uJy   | e_FH          | [0.5/13] FH uncertainty                                                     |
| 104-112 | F9.3         | 0.3631uJy   | FJ            | [-19.1/64555] UltraVISTA J flux (2)                                         |
| 114-119 | F6.3         | 0.3631uJy   | e_FJ          | [0.3/10.3] FJ uncertainty                                                   |
| 121-130 | F10.3        | 0.3631uJy   | FY            | [-14.8/116197] UltraVISTA Y (broadband at                                   |
| 132-137 | F6.3         | 0.3631uJy   | e_FY          | [0.3/17] FY uncertainty                                                     |
| 139-147 | F9.3         | 0.3631uJy   | Fch4          | [-5255/44148]?=-99.9 Spitzer/IRAC                                           |
| 149-158 | F10.3        | 0.3631uJy   | e_Fch4        | [3.9/103098]?=-99.9 Fch4 uncertainty                                        |
| 160-168 | F9.3         | 0.3631uJy   | Fch3          | [-1501/63780]?=-99.9 Spitzer/IRAC                                           |
| 170-177 | F8.3         | 0.3631uJy   | e_Fch3        | [4.1/3195]?=-99.9 Fch3 uncertainty                                          |
| 179-187 | F9.3         | 0.3631uJy   | Fch2          | [-223/26394]?=-99.9 Spitzer/IRAC                                            |
| 189-196 | F8.3         | 0.3631uJy   | e_Fch2        | [0.6/1322]?=-99.9 Fch2 uncertainty                                          |
| 198-206 | F9.3         | 0.3631uJy   | Fch1          | [-218/23086]?=-99.9 Spitzer/IRAC                                            |
| 208-215 | F8.3         | 0.3631uJy   | e_Fch1        | [0.5/1156]?=-99.9 Fch1 uncertainty                                          |
| 217-224 | F8.3         | 0.3631uJy   | Fzp           | [-7/2060]?=-99.999 Subaru/SuprimeCam                                        |
| 226-232 | F7.3         | 0.3631uJy   | e_Fzp         | [0.1/2]?=-99.999 Fzp uncertainty                                            |
| 234-240 | F7.3         | 0.3631uJy   | Fip           | [-6.2/514]?=-99.999 Subaru/SuprimeCam                                       |
| 242-248 | F7.3         | 0.3631uJy   | e_Fip         | [0.08/0.8]?=-99.999 Fip uncertainty                                         |
| 250-256 | F7.3         | 0.3631uJy   | Frp           | [-17/876]?=-99.999 Subaru/SuprimeCam                                        |
| 258-264 | F7.3         | 0.3631uJy   | e_Frp         | [0.05/1.3]?=-99.999 Frp uncertainty                                         |
| 266-273 | F8.3         | 0.3631uJy   | FV            | [-6.6/1175]?=-99.999 Subaru/SuprimeCam                                      |
| 275-281 | F7.3         | 0.3631uJy   | e_FV          | [0.05/1.3]?=-99.999 FV uncertainty                                          |
| 283-290 | F8.3         | 0.3631uJy   | Fgp           | [-46/1249]?=-99.999 Subaru/SuprimeCam                                       |
| 292-298 | F7.3         | 0.3631uJy   | e_Fgp         | [0.05/0.8]?=-99.999 Fgp uncertainty                                         |
| 300-307 | F8.3         | 0.3631uJy   | FB            | [-7.4/1138]?=-99.999 Subaru/SuprimeCam                                      |
| 309-315 | F7.3         | 0.3631uJy   | e_FB          | [0.03/1.2]?=-99.999 FB uncertainty                                          |
| 317-325 | F9.3         | 0.3631uJy   | Fu            | [-54.1/16050] CFHT/MegaCam u* flux (2)                                      |
| 327-332 | F6.3         | 0.3631uJy   | e_Fu          | [0.03/14.2] Fu uncertainty                                                  |
| 334-341 | F8.3         | 0.3631uJy   | FIA484        | [-257/2448]?=-99.999 Subaru/SuprimeCam                                      |
| 484     | flux         | (2)         | 343-349       | F7.3  0.3631uJy e_FIA484 [0.07/8]?=-99.999 FIA484 uncertainty               |
| 351-358 | F8.3         | 0.3631uJy   | FIA527        | [-316/3211]?=-99.999 Subaru/SuprimeCam                                      |
| 527     | flux         | (2)         | 360-366       | F7.3  0.3631uJy e_FIA527 [0.07/9]?=-99.999 FIA527 uncertainty               |
| 368-375 | F8.3         | 0.3631uJy   | FIA624        | [-412/3666]?=-99.999 Subaru/SuprimeCam                                      |
| 624     | flux         | (2)         | 377-383       | F7.3  0.3631uJy e_FIA624 [0.09/8]?=-99.999 FIA624 uncertainty               |
| 385-392 | F8.3         | 0.3631uJy   | FIA679        | [-582/5602]?=-99.999 Subaru/SuprimeCam                                      |
| 679     | flux         | (2)         | 394-400       | F7.3  0.3631uJy e_FIA679 [0.1/8]?=-99.999 FIA679 uncertainty                |
| 402-409 | F8.3         | 0.3631uJy   | FIA738        | [-206/3984]?=-99.999 Subaru/SuprimeCam                                      |
| 738     | flux         | (2)         | 411-417       | F7.3  0.3631uJy e_FIA738 [0.1/9]?=-99.999 FIA738 uncertainty                |
| 419-427 | F9.3         | 0.3631uJy   | FIA767        | [-1449/5859]?=-99.999 Subaru/SuprimeCam                                     |
| 767     | flux         | (2)         | 429-435       | F7.3  0.3631uJy e_FIA767 [0.1/10]?=-99.999 FIA767 uncertainty               |
| 437-444 | F8.3         | 0.3631uJy   | FIB427        | [-871/7199]?=-99.999 Subaru/SuprimeCam                                      |
| 427     | flux         | (2)         | 446-452       | F7.3  0.3631uJy e_FIB427 [0.07/17]?=-99.999 FIB427 uncertainty              |
| 454-462 | F9.3         | 0.3631uJy   | FIB464        | [-1043/8397]?=-99.999 Subaru/SuprimeCam                                     |
| 464     | flux         | (2)         | 464-470       | F7.3  0.3631uJy e_FIB464 [0.1/17]?=-99.999 FIB464 uncertainty               |
| 472-480 | F9.3         | 0.3631uJy   | FIB505        | [-1476/7743]?=-99.999 Subaru/SuprimeCam                                     |
| 505     | flux         | (2)         | 482-488       | F7.3  0.3631uJy e_FIB505 [0.09/15]?=-99.999 FIB505 uncertainty              |
| 490-497 | F8.3         | 0.3631uJy   | FIB574        | [-566/7152]?=-99.999 Subaru/SuprimeCam                                      |
| 574     | flux         | (2)         | 499-505       | F7.3  0.3631uJy e_FIB574 [0.1/13]?=-99.999 FIB574 uncertainty               |
| 507-514 | F8.3         | 0.3631uJy   | FIB709        | [-645/5095]?=-99.999 Subaru/SuprimeCam                                      |
| 709     | flux         | (2)         | 516-522       | F7.3  0.3631uJy e_FIB709 [0.1/9]?=-99.999 FIB709 uncertainty                |
| 524-532 | F9.3         | 0.3631uJy   | FIB827        | [-1449/4860]?=-99.999 Subaru/SuprimeCam                                     |
| 827     | flux         | (2)         | 534-540       | F7.3  0.3631uJy e_FIB827 [0.1/10]?=-99.999 FIB827 uncertainty               |
| 542-550 | F9.3         | 0.3631uJy   | FFUV          | [-1482/7734]?=-99.9 GALEX FUV flux (2)                                      |
| 552-558 | F7.3         | 0.3631uJy   | e_FFUV        | [0.06/946]?=-99.9 FFUV uncertainty                                          |
| 560-568 | F9.3         | 0.3631uJy   | FNUV          | [-6098/5495]?=-99.9 GALEX NUV flux (2)                                      |
| 570-576 | F7.3         | 0.3631uJy   | e_FNUV        | [0.04/452]?=-99.9 FNUV uncertainty                                          |
| 578-586 | F9.3         | 0.3631uJy   | F24           | [0.1/33412]?=-99.9 Spitzer/MIPS 24um flux (2)                               |
| 588-594 | F7.3         | 0.3631uJy   | e_F24         | [0.1/14]?=-99.9 F24 uncertainty                                             |
| 596-600 | F5.3         | ---         | Kflag         | [0/6] SExtractor's FLAG output for the                                      |
| 602-606 | F5.3         | ---         | S/G           | [0/1] SExtractor's CLASS_STAR output from the                               |
| 608-615 | F8.5         | ---         | KKron         | [3/50] SExtractor's Kron radius in Ks-band                                  |
| 617-623 | F7.5         | ---         | apcor         | [1/1.2] Aperture correction that has been                                   |
| 625-632 | F8.5         | ---         | zsp           | [0.01/2.1]?=-1 zCOSMOS spectroscopic redshift                               |
| 634-641 | F8.5         | ---         | CC            | [3/5]?=-1 Spectroscopic redshift quality flag                               |
| 643-648 | I6           | ---         | zCOSMOS       | [7447/950074]?=-1 ID of the spectroscopic                                   |
| 650     | I1           | ---         | Star          | [0/1] Star/galaxy indicator determined from                                 |
| 652     | I1           | ---         | Cont          | [0/1] Contamination: proximity to a bright                                  |
| 654-655 | I2           | ---         | nCont         | [0/21] Number of filters where object lies                                  |
| 0       | (nan_contam) | (5)         | 657-661       | I5    ---         Ori    [230/82870] ID number in the original              |
| 9       | COSMOS       | subfields   | (orig_cat_id) | 663  I1    ---         Field  [1/9] Subfield of the object (orig_cat_field) |
| 665     | I1           | ---         | USE           | [0/1] Indicates galaxies with uncontaminated                                |
| 5       | (6)          | Note        | (1):          | Total Ks flux and error determined using Sextractor's flux_auto. An         |
| 5       | times        | the         | Kron          | radius.                                                                     |
| 3       | as           | these       | are           | probably contaminated by a nearby object or are near saturated pixels.      |
| 99      | so           | are         | ignored       | by EAZY and FAST. Objects with 0<value<5 are probably                       |
| 3       | should       | probably    | be            | excluded as many filters of data are                                        |
| 1       | have,        | K(ap)<24.44 | (i.e.,        | 3-sigma detection), star =0,                                                |
| 4       | so           | for         | truly         | complete sample that selection                                              |

**Note**: Total Ks flux and error determined using Sextractor's flux_auto. An
          additional aperture correction has also been applied to correct for
          flux outside 2.5 times the Kron radius.
Note (2): Flux and error in filter X measured in a 2.1" aperture from
          PSF-matched images.
          Total magnitudes in any band can be calculated via
          flux_X(total)_=flux_X(aperture)_*(FKstot/FKs), where X is the band
          of interest.
Note (3): One should be cautious using objects with Kflag>3 as these are
          probably contaminated by a nearby object or are near saturated pixels.
Note (4): See "Confidence Class" in Lilly et al. (2007, J/ApJS/172/70) for full
          definition of these flags.
Note (5): If this object is near an object that is saturated and the flux is
          contaminated by PSF convolution of the saturated object this value =1.
          The value is the TOTAL number of filters that have this type of
          contamination. The fluxes of these filters have been set to -99 so are
          ignored by EAZY and FAST. Objects with 0<value<5 are probably
          acceptable as are only missing a few filters of data. Objects with
          value >3 should probably be excluded as many filters of data are
          contaminated and missing.
Note (6): A simple switch for choosing galaxies with good photometry. Objects
          with USE =1 have, K(ap)<24.44 (i.e., 3-sigma detection), star =0,
          contamination =0, and nan_contam <3. Be aware that this includes
          objects with Ks_tot>23.4 so for truly complete sample that selection
          should also be done.

</details>

<details>
<summary>zout.dat</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                       |
|:--------|:---------|:--------|:--------|:---------------------------------------------------|
| 1- 6    | I6       | ---     | Seq     | [1/262615] Running sequence number                 |
| 8- 14   | F7.4     | ---     | zsp     | [0.01/2.1]?=-1 Spectroscopic redshift from zCOSMOS |
| 16- 22  | F7.3     | ---     | za      | [0.01/6]?=-99 Redshift where {chi}^2^ is minimized |
| 24- 30  | F7.3     | ---     | zm1     | [0.01/6]?=-99 Redshift marginalized over           |
| 32- 43  | E12.7    | ---     | chia    | [1.4/3759]?=-99 {chi}^2^ value at z=za             |
| 45- 51  | F7.3     | ---     | zp      | [0.01/6]?=-99 Redshift where likelihood is         |
| 53- 64  | E12.7    | ---     | chip    | [1.4/3759]?=-99 Original {chi}^2^ at z=zp          |
| 66- 72  | F7.3     | ---     | zm2     | [0.01/6]?=-99 Redshift marginalized over           |
| 74- 80  | F7.3     | ---     | odds    | [-99/1] Redshift quality parameter (1)             |
| 82- 88  | F7.3     | ---     | l68     | [0.01/6]?=-99 Lower 68% confidence interval on zpk |
| 90- 96  | F7.3     | ---     | u68     | [0.02/6]?=-99 Upper 68% confidence interval on zpk |
| 98-104  | F7.3     | ---     | l95     | [0.01/6]?=-99 Lower 95% confidence interval on zpk |
| 106-112 | F7.3     | ---     | u95     | [0.02/6]?=-99 Upper 95% confidence interval on zpk |
| 114-120 | F7.3     | ---     | l99     | [0.01/6]?=-99 Lower 99% confidence interval on zpk |
| 122-128 | F7.3     | ---     | u99     | [0.02/6]?=-99 Upper 68% confidence interval on zpk |
| 130-132 | I3       | ---     | Nf      | [8/29]?=-99 Number of filters used to determine    |
| 134-146 | E13.7    | ---     | q_z     | [-99/3.26455e+212] z quality                       |
| 148-155 | F8.4     | ---     | zpk     | [0.01/6]?=-99 Photometric redshift from the peak   |
| 157-163 | F7.3     | ---     | Probpk  | [-99/1] Peak probability                           |
| 165-172 | F8.4     | ---     | zmc     | [0.01/6]?=-99 zmc value (1)                        |

**Note**: Photometric redshift information from EASY code
          (Brammer et al. 2008ApJ...686.1503B).
          See http://www.astro.yale.edu/eazy/?node17 for more details.

</details>

<details>
<summary>bc03.dat</summary>

| Bytes   | Format   | Units     | Label   | Explanations                                |
|:--------|:---------|:----------|:--------|:--------------------------------------------|
| 1- 6    | I6       | ---       | Seq     | [1/262615] Running sequence number          |
| 8- 14   | F7.4     | ---       | z       | [0.01/6]?=-1 Photometric redshift from EASY |
| 16- 20  | F5.2     | [yr]      | ltau    | [7/10]?=-1 Best-fit value of log({tau}) (1) |
| 22- 27  | F6.3     | ---       | metal   | [0.02]?=-1 Metallicity (fixed at 0.020)     |
| 29- 33  | F5.2     | [yr]      | lage    | [7/10.1]?=-1 Best-fit value of log(t) (1)   |
| 35- 39  | F5.2     | ---       | Av      | [0/4]?=-1 Best-fit value of A_v_            |
| 41- 46  | F6.2     | [Msun]    | lmass   | [-1/14.3]?=-99 Best-fit value of            |
| 48- 53  | F6.2     | [Msun/yr] | lsfr    | [-36/4.8]?=-99 Best-fit value of log(sfr)   |
| 55- 60  | F6.2     | [yr-1]    | lssfr   | [-43/-1]?=-99 Best-fit value of log(ssfr)   |
| 62- 66  | F5.2     | ---       | la2t    | [-3/3.1] la2t value                         |
| 68- 75  | E8.3     | ---       | chi2    | [-1/189] {chi}^2^ of best-fitting model     |

**Note**: We assume galaxies have exponentially declining star formation
          histories (SFHs) of the form SFR{propto}exp(-t/{tau}), where t is the
          time since the onset of star formation and {tau} is the e-folding star
          formation timescale in units of yr. See section 5.1.

</details>

<details>
<summary>153-155.dat</summary>

| Bytes   | Format   | Units                                    | Label       | Explanations                                                                  |
|:--------|:---------|:-----------------------------------------|:------------|:------------------------------------------------------------------------------|
| 1- 6    | I6       | ---                                      | Seq         | [1/262615] Running sequence number                                            |
| 8- 15   | F8.5     | ---                                      | zpk         | [/6]?=-1 Photometric redshift from the peak of                                |
| 17- 22  | F6.2     | ---                                      | DM          | [/47]?=-99 Distance modulus                                                   |
| 24- 26  | I3       | ---                                      | Nf          | [/20]?=-99 Number of filters used for the fit                                 |
| 28- 39  | E12.6    | ---                                      | chi2        | [/2009]?=-99 Best-fit {chi}^2^                                                |
| 41- 52  | E12.6    | ---                                      | L153        | [/826698]?=-99 EAZY-interpolated U-V color index (1)                          |
| 54- 65  | E12.6    | ---                                      | L155        | [/5.59709e+06]?=-99 EAZY-interpolated U-V                                     |
| 03      | 155:     | REST_FRAME/maiz-apellaniz_Johnson_V.res, | 5.49056e+03 | Rest-frame colors computed using templates in tweak_UVISTA_v4.1/spectra.param |

**Note**: 153: REST_FRAME/maiz-apellaniz_Johnson_U.res, 3.59854e+03
   155: REST_FRAME/maiz-apellaniz_Johnson_V.res, 5.49056e+03
   Rest-frame colors computed using templates in tweak_UVISTA_v4.1/spectra.param

</details>

<details>
<summary>155-161.dat</summary>

| Bytes   | Format   | Units        | Label       | Explanations                                                                   |
|:--------|:---------|:-------------|:------------|:-------------------------------------------------------------------------------|
| 1- 6    | I6       | ---          | Seq         | [1/262615] Running sequence number                                             |
| 8- 15   | F8.5     | ---          | zpk         | [/6]?=-1 Photometric redshift from the peak of                                 |
| 17- 22  | F6.2     | ---          | DM          | [/47]?=-99 Distance modulus                                                    |
| 24- 26  | I3       | ---          | Nf          | [/20]?=-99 Number of filters used for the fit                                  |
| 28- 39  | E12.6    | ---          | chi2        | [/1730]?=-99 Best-fit {chi}^2^                                                 |
| 41- 52  | E12.6    | ---          | L155        | [/261250]?=-99 EAZY-interpolated V-J color index (1)                           |
| 54- 65  | E12.6    | ---          | L161        | [/1.06681e+06]?=-99 EAZY-interpolated V-J                                      |
| 03      | 161:     | 2MASS/J.res, | 1.23751e+04 | Rest-frame colors computed using templates in tweak_UVISTA_v3.24/spectra.param |

**Note**: 155: REST_FRAME/maiz-apellaniz_Johnson_V.res, 5.49056e+03
  161: 2MASS/J.res, 1.23751e+04
  Rest-frame colors computed using templates in tweak_UVISTA_v3.24/spectra.param

</details>
