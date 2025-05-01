**Authors:** Aussel H., Ajiki M., McCracken H.J., Mobasher B., Scoville N.,, Shopbell P., Taniguchi Y., Thompson D., Tribiano S., Sasaki S., Blain A.W.,, Brusa M., Carilli C., Comastri A., Carollo C.M., Cassata P., Colbert J.,, Ellis R.S., Elvis M., Giavalisco M., Green W., Guzzo L., Hasinger G.,, Ilbert O., Impey C., Jahnke K., Kartaltepe J., Kneib J.-P., Koda J.,, Koekemoer A., Komiyama Y., Leauthaud A., Lefevre O., Lilly S., Liu C.,, Massey R., Miyazaki S., Murayama T., Nagao T., Peacock J.A., Pickles A.,, Porciani C., Renzini A., Rhodes J., Rich M., Salvato M., Sanders D.B.,, Scarlata C., Schiminovich D., Schinnerer E., Scodeggio M., Sheth K.,, Shioya Y., Tasca L.A.M., Taylor J.E., Yan L., Zamorani G., <Astrophys. J. Suppl. Ser., 172, 99-116 (2007)>, =2007ApJS..172...99C

## Summary: COSMOS Multi-Wavelength Photometry Catalog 

We present imaging data and photometry for the COSMOS survey in 15 photometric bands between 0.3 and 2.4m. These include data taken on the Subaru 8.3m telescope, the KPNO and CTIO 4m telescopes, and the CFHT 3.6m telescope. Special techniques are used to ensure that the relative photometric calibration is better than 1% across the field of view. The absolute photometric accuracy from standard-star measurements is found to be 6%. The absolute calibration is corrected using galaxy spectra, providing colors accurate to 2% or better. Stellar and galaxy colors and counts agree well with the expected values. Finally, as the first step in the scientific analysis of these data we construct panchromatic number counts which confirm that both the geometry of the universe and the galaxy population are evolving.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/II-284/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Photometric Redshift 
 
**zphot:** Photometric Redshift from Mobasher et al. 
 

## Catalogue Schema

<details>
<summary>cosmos.dat</summary>

| Bytes   | Format   | Units     | Label   | Explanations                                    |
|:--------|:---------|:----------|:--------|:------------------------------------------------|
| 1- 7    | I7       | ---       | COSMOS  | Unique identification number of each source     |
| 9- 11   | I3       | ---       | Image   | [1/144] Which of the 144 sub-image tiles        |
| 13- 21  | F9.5     | deg       | RAdeg   | Right Ascension in decimal degrees (J2000.0)    |
| 22- 30  | F9.5     | deg       | DEdeg   | Declination in decimal degrees (J2000.0)        |
| 32- 39  | F8.3     | pix       | Xpix    | X pixel position on the sub-image tile          |
| 41- 48  | F8.3     | pix       | Ypix    | Y pixel position on the sub-image tile          |
| 50- 55  | F6.2     | pix       | ifwhm   | ?=-99 FWHM measured on the detection image      |
| 57- 68  | F12.6    | uJy       | imax    | ?=-99 Peak flux measured on the detection       |
| 70- 75  | F6.2     | ---       | istar   | ?=-99 SExtractor stellarity parameter measured  |
| 77- 84  | F8.4     | mag       | imagA   | ?=-99 Total i-band magnitude measured on the    |
| 86- 93  | F8.4     | mag       | dmag3   | ?=-99 Offset between 3" aperture magnitudes     |
| 95- 96  | I2       | ---       | n_imagA | [-1/2] Flag indicating which image the total    |
| 98-105  | F8.4     | mag       | umag    | ?=-99. CFHT u* AB magnitude (8)                 |
| 107-114 | F8.4     | mag       | e_umag  | ?=-99. 1 Sigma error on CFHT umag (9)           |
| 116-123 | F8.4     | mag       | Bmag    | ?=-99. Subaru Bj AB magnitude (8)               |
| 125-132 | F8.4     | mag       | e_Bmag  | ?=-99. 1 Sigma error on Subaru Bmag (9)         |
| 134-141 | F8.4     | mag       | Vmag    | ?=-99. Subaru Vj AB magnitude (8)               |
| 143-150 | F8.4     | mag       | e_Vmag  | ?=-99. 1 Sigma error on Subaru Vmag (9)         |
| 152-159 | F8.4     | mag       | gmag    | ?=-99. Subaru g+ AB magnitude (8)               |
| 161-168 | F8.4     | mag       | e_gmag  | ?=-99. 1 Sigma error on Subaru gmag (9)         |
| 170-177 | F8.4     | mag       | rmag    | ?=-99. Subaru r+ AB magnitude (8)               |
| 179-186 | F8.4     | mag       | e_rmag  | ?=-99. 1 Sigma error on Subaru rmag (9)         |
| 188-195 | F8.4     | mag       | imag    | ?=-99. Subaru i+ AB magnitude (8)               |
| 197-204 | F8.4     | mag       | e_imag  | ?=-99. 1 Sigma error on Subaru imag (9)         |
| 206-213 | F8.4     | mag       | zmag    | ?=-99. Subaru z+ AB magnitude (8)               |
| 215-222 | F8.4     | mag       | e_zmag  | ?=-99. 1 Sigma error on Subaru zmag (9)         |
| 224-231 | F8.4     | mag       | Kmag    | ?=-99. CTIO/KPNO Ks AB magnitude (8)            |
| 233-240 | F8.4     | mag       | e_Kmag  | ?=-99. 1 Sigma error on CTIO/KPNO Kmag (9)      |
| 242-249 | F8.4     | mag       | iCFHT   | ?=-99. CFHT i* AB magnitude (8)                 |
| 251-258 | F8.4     | mag       | e_iCFHT | ?=-99. 1 Sigma error on CFHT imag (9)           |
| 260-267 | F8.4     | mag       | uSDSS   | ?=-99. SDSS u AB magnitude (8)                  |
| 269-276 | F8.4     | mag       | e_uSDSS | ?=-99. 1 Sigma error on SDSS umag (9)           |
| 278-285 | F8.4     | mag       | gSDSS   | ?=-99. SDSS g AB magnitude (8)                  |
| 287-294 | F8.4     | mag       | e_gSDSS | ?=-99. 1 Sigma error on SDSS gmag (9)           |
| 296-303 | F8.4     | mag       | rSDSS   | ?=-99. SDSS r AB magnitude (8)                  |
| 305-312 | F8.4     | mag       | e_rSDSS | ?=-99. 1 Sigma error on SDSS rmag (9)           |
| 314-321 | F8.4     | mag       | iSDSS   | ?=-99. SDSS i AB magnitude (8)                  |
| 323-330 | F8.4     | mag       | e_iSDSS | ?=-99. 1 Sigma error on SDSS imag (9)           |
| 332-339 | F8.4     | mag       | zSDSS   | ?=-99. SDSS z AB magnitude (8)                  |
| 341-348 | F8.4     | mag       | e_zSDSS | ?=-99. 1 Sigma error on SDSS zmag (9)           |
| 350-357 | F8.4     | mag       | F814W   | ?=-99. HST F814W magnitude (8)                  |
| 359-366 | F8.4     | mag       | e_F814W | ?=-99. 1 Sigma error on HST F814W mag (9)       |
| 368-375 | F8.4     | mag       | NB816   | ?=-99. Subaru NB816 magnitude (8)               |
| 377-384 | F8.4     | mag       | e_NB816 | ?=-99. 1 Sigma error on Subaru NB816 mag (9)    |
| 386-393 | F8.6     | mag       | E(B-V)  | E(B-V) for this object position from            |
| 395-398 | F4.2     | ---       | zphot   | Photometric Redshift from Mobasher et al.       |
| 400-403 | F4.2     | ---       | z68min  | Minimum photometric redshift at 68% probability |
| 405-408 | F4.2     | ---       | z68max  | Maximum photometric redshift at 68% probability |
| 410-413 | F4.2     | ---       | z95min  | Minimum photometric redshift at 95% probability |
| 415-418 | F4.2     | ---       | z95max  | Maximum photometric redshift at 95% probability |
| 420-423 | F4.2     | ---       | Tphot   | [1/6] Photometric type of the object (2)        |
| 425-428 | F4.2     | mag       | Rphot   | ?=0 Intrinsic e(B-V) of the object estimated    |
| 430-435 | F6.2     | ---       | Chi2    | Chi-square of best fit redshift and             |
| 437-438 | I2       | ---       | Nf      | Number of filters used for in the               |
| 440-447 | F8.3     | mag       | VMAG    | Absolute V band AB magnitude                    |
| 449-453 | F5.3     | ---       | D95     | D95 parameter (4)                               |
| 455-461 | F7.3     | [solMass] | logMass | Log base 10 of the stellar mass (3)             |
| 463     | I1       | ---       | Star    | [0/1] Star flag based on color and              |
| 465     | I1       | ---       | BMask   | Bj image mask (6)                               |
| 467     | I1       | ---       | VMask   | Vj image mask (6)                               |
| 469     | I1       | ---       | iMask   | i+ image mask (6)                               |
| 471     | I1       | ---       | zMask   | z+ image mask (6)                               |
| 473     | I1       | ---       | blFlag  | [0/1] de-blended or false detection (7)         |
| 1       | =        | Subaru    | i+      | 2 = CFHT i*                                     |
| 1       | =        | No        | valid   | total magnitude                                 |

**Note**: Flag for the total magnitude measurement as follows:
      1 = Subaru i+
      2 = CFHT i*
     -1 = No valid total magnitude

</details>
