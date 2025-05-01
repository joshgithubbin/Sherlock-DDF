**Authors:** Trump J.R., Impey C.D., Elvis M., McCarthy P.J., Huchra J.P., Brusa M.,, Salvato M., Capak P., Cappelluti N., Civano F., Comastri A., Gabor J.,, Hao H., Hasinger G., Jahnke K., Kelly B.C., Lilly S.J., Schinnerer E.,, Scoville N.Z., Smolcic V., <Astrophys. J., 696, 1195-1212 (2009)>, =2009ApJ...696.1195T

## Summary: COSMOS AGN spectroscopic survey. I. 

We present optical spectroscopy for an X-ray and optical flux-limited sample of 677 XMM-Newton selected targets covering the 2deg^2^ Cosmic Evolution Survey field, with a yield of 485 high-confidence redshifts. The majority of the spectra were obtained over three seasons (2005-2007) with the Inamori Magellan Areal Camera and Spectrograph instrument on the Magellan (Baade) telescope. We also include in the sample previously published Sloan Digital Sky Survey spectra and supplemental observations with MMT/Hectospec. We detail the observations and classification analyses. The survey is 90% complete to flux limits of f_0.5-10keV_>8x10^-16-^erg/cm^2^/s and i^+^_AB_<22, where over 90% of targets have high-confidence redshifts. Making simple corrections for incompleteness due to redshift and spectral type allows for a description of the complete population to i^+^_AB_<23. The corrected sample includes a 57% broad emission line (Type 1, unobscured) active galactic nucleus (AGN) at 0.13<z<4.26, 25% narrow emission line (Type 2, obscured) AGN at 0.07<z<1.29, and 18% absorption line (host-dominated, obscured) AGN at 0<z<1.22 (excluding the stars that made up 4% of the X-ray targets). We show that the survey's limits in X-ray and optical fluxes include nearly all X-ray AGNs (defined by L_0.5-10keV_>3x10^42^erg/s) to z<1, of both optically obscured and unobscured types.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-696-1195/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**z:** ?=-1 Spectroscopic redshift 
 

## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units           | Label    | Explanations                                                |
|:--------|:---------|:----------------|:---------|:------------------------------------------------------------|
| 1- 7    | A7       | ---             | Sample   | SDSS/COSMOS                                                 |
| 8- 26   | A19      | ---             | Name     | SDSS or COSMOS object name (JHHMMSS.ss+DDMMSS.s)            |
| 28- 38  | F11.7    | deg             | RAdeg    | Right Ascension in decimal degrees (J2000)                  |
| 40- 48  | F9.7     | deg             | DEdeg    | Declination in decimal degrees (J2000)                      |
| 50- 54  | F5.2     | ---             | imag     | HST/ACS i band AB magnitude from COSMOS                     |
| 56- 61  | F6.2     | ---             | S/N      | Signal-to-noise                                             |
| 63- 67  | I5       | s               | ExpT     | Exposure time                                               |
| 69- 73  | A5       | ---             | Type     | Source type (1)                                             |
| 75- 81  | F7.4     | ---             | z        | ?=-1 Spectroscopic redshift                                 |
| 83- 89  | F7.4     | ---             | e_z      | ?=-1 The 1{sigma} error in z                                |
| 91- 92  | I2       | ---             | q_z      | Confidence note on z (2)                                    |
| 1       | AGN);    | nl              | =        | narrow emission line (Type 2 AGN or starburst galaxy);      |
| 2       | AGN/red  | galaxy          | hybrid); | star = star;                                                |
| 4       | =        | redshift        | is       | considered unambiguous, empirically estimated               |
| 3       | =        | one             | strong   | feature and one weak feature used in fitting, ~90% correct; |
| 2       | =        | degenerate      | redshift | solution from only one feature, ~75% correct;               |
| 1       | =        | purely          | a        | guess, redshift may come from only noise, ~33% correct;     |
| 0       | =        | signal-to-noise | of       | the object spectrum was too low for a redshift              |
| 1       | =        | "broken"        | slits,   | with severe neighboring slit contamination or mask          |

**Note**: Source type as follows:
    bl = broad emission line (Type 1 AGN);
    nl = narrow emission line (Type 2 AGN or starburst galaxy);
     a = absorption line (red galaxy or optically dull AGN);
   nla = both narrow emission and absorption lines
         (Type 2 AGN/red galaxy hybrid);
  star = star;
     ? = questionable classification
Note (2): Confidence on redshift as follows:
    4 = redshift is considered unambiguous, empirically estimated
        as ~97% correct;
    3 = one strong feature and one weak feature used in fitting, ~90% correct;
    2 = degenerate redshift solution from only one feature, ~75% correct;
    1 = purely a guess, redshift may come from only noise, ~33% correct;
    0 = signal-to-noise of the object spectrum was too low for a redshift
        to be determined;
   -1 = "broken" slits, with severe neighboring slit contamination or mask
        cutting errors.

</details>
