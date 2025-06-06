**Authors:** Impey C.D., McCarthy P.J., Elvis M., Huchra J.P., Brusa M.,, Hasinger G., Schinnerer E., Capak P., Lilly S.J., Scoville N.Z., <Astrophys. J. Suppl. Ser., 172, 383-395 (2007)>, =2007ApJS..172..383T

## Summary: AGN candidates in the COSMOS field 

We present spectroscopic redshifts for the first 466 X-ray and radio-selected AGN targets in the 2deg^2^ COSMOS field. Spectra were obtained with the IMACS instrument on the Magellan (Baade) telescope, using the nod-and-shuffle technique. We identify a variety of type 1 and type 2 AGNs, as well as red galaxies with no emission lines. Our redshift yield is 72% down to i_AB_=24, although the yield is >90% for i_AB_<22. We expect the completeness to increase as the survey continues. When our survey is complete and additional redshifts from the zCOSMOS project are included, we anticipate ~1100 AGNs with redshifts over the entire COSMOS field. Our redshift survey is consistent with an obscured AGN population that peaks at z~0.7, although further work is necessary to disentangle the selection effects.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJS-172-383/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**z:** ?=-1.00000 Redshift 
 

## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units    | Label     | Explanations                                   |
|:--------|:---------|:---------|:----------|:-----------------------------------------------|
| 1- 6    | A6       | ---      | ---       | [COSMOS]                                       |
| 8- 26   | A19      | ---      | [TIM2007] | Object name (JHHMMSS.ss+DDMMSS.s),             |
| 28- 38  | F11.7    | deg      | RAdeg     | Right Ascension in decimal degrees (J2000)     |
| 40- 48  | F9.7     | deg      | DEdeg     | Declination in decimal degrees (J2000)         |
| 50- 54  | F5.2     | ---      | imag      | HST/ACS i band AB magnitude                    |
| 56- 61  | F6.2     | ---      | S/N       | Signal-to-noise                                |
| 63- 67  | I5       | ---      | Texp      | Exposure time                                  |
| 69- 73  | A5       | ---      | Type      | Source classification (1)                      |
| 75- 82  | F8.5     | ---      | z         | ?=-1.00000 Redshift                            |
| 84      | A1       | ---      | n_z       | [c] Manually assigned z (2)                    |
| 86- 93  | F8.5     | ---      | e_z       | ?=-1.00000 The 1{sigma} error in z             |
| 95      | A1       | ---      | n_e_z     | [b] Manually assigned e_z (3)                  |
| 97      | A1       | ---      | zconf     | Confidence note on z (4)                       |
| 1       | =        | Type     | 1         | AGN                                            |
| 2       | =        | Type     | 2         | AGN                                            |
| 2       | AGN      | and      | red       | galaxy hybrid                                  |
| 2       | Type     | 1        | AGN       | had their  redshifts                           |
| 1       | =        | redshift | is        | considered unambiguous                         |
| 2       | =        | only     | one       | line fit or the redshift comes strictly from a |

**Note**: Source type as follows:
     q1 = Type 1 AGN
     q2 = Type 2 AGN
      e = red galaxy
    q2e = Type 2 AGN and red galaxy hybrid
  mstar = M-type stars
      ? = questionable classification
     q? = blue continua but no obvious emission lines
     e? = red  continua and no emission or absorption lines
Note (2): 'c' indicates that these zconf=2 Type 1 AGN had their  redshifts
     manually adjusted to be more consistent with  their u*(CFHT)-B(Subaru)
     and V(Subaru)-r(Subaru) colors.
Note (3): 'b' indicates objects with a manually assigned redshift error
     derived from the 5-pixel spectral resolution.
Note (4): Note on zconf as follows:
      1 = redshift is considered unambiguous 
      2 = only one line fit or the redshift comes strictly from a 
          well-fit continuum shape over the entire spectral range 
      ? = signal-to-noise of the object spectrum was too low for 
          a redshift to be determined

</details>
