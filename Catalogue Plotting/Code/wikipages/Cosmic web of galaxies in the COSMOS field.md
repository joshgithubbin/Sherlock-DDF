**Authors:** Mobasher B., Martin D.C., Sobral D., Scoville N., Stroe A.,, Hemmati S., Kartaltepe J., <Astrophys. J., 837, 16-16 (2017)>, =2017ApJ...837...16D (SIMBAD/NED BibCode)

## Summary: Cosmic web of galaxies in the COSMOS field 

We use a mass complete (log(M/M_{sun}_)>=9.6) sample of galaxies with accurate photometric redshifts in the COSMOS field to construct the density field and the cosmic web to z=1.2. The comic web extraction relies on the density field Hessian matrix and breaks the density field into clusters, filaments, and the field. We provide the density field and cosmic web measures to the community. We show that at z<~0.8, the median star formation rate (SFR) in the cosmic web gradually declines from the field to clusters and this decline is especially sharp for satellites (~1dex versus ~0.5dex for centrals). However, at z>~0.8, the trend flattens out for the overall galaxy population and satellites. For star-forming (SF) galaxies only, the median SFR is constant at z>~0.5 but declines by ~0.3-0.4dex from the field to clusters for satellites and centrals at z<~0.5. We argue that for satellites, the main role of the cosmic web environment is to control their SF fraction, whereas for centrals, it is mainly to control their overall SFR at z<~0.5 and to set their fraction at z>~0.5. We suggest that most satellites experience a rapid quenching mechanism as they fall from the field into clusters through filaments, whereas centrals mostly undergo a slow environmental quenching at z<~0.5 and a fast mechanism at higher redshifts. Our preliminary results highlight the importance of the large-scale cosmic web on galaxy evolution.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-837-16/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Photometric Redshift 
 
**zph:** [0.1/1.2] Photometric redshift 
 

## Catalogue Schema

<details>
<summary>table1.dat</summary>

| Bytes   | Format         | Units      | Label      | Explanations                                                              |
|:--------|:---------------|:-----------|:-----------|:--------------------------------------------------------------------------|
| 1- 6    | I6             | ---        | COSMOS2015 | Original sequence number in Laigle+ 2016,                                 |
| 24      | 8-             | 17         | F10.6      | deg   RAdeg      Right Ascension in decimal degrees (J2000)               |
| 19- 26  | F8.6           | deg        | DEdeg      | Declination in decimal degrees (J2000)                                    |
| 28- 33  | F6.4           | ---        | zph        | [0.1/1.2] Photometric redshift                                            |
| 35- 39  | F5.2           | Mpc-2      | Den        | [0.01/93] Density                                                         |
| 41- 45  | F5.2           | ---        | Oden       | [0/37.3] Density divided by the median density                            |
| 47- 54  | F8.6           | ---        | SCl        | [0/0.9] Cluster signal, resemblance of the                                |
| 56- 63  | F8.6           | ---        | SFil       | [0/0.9] Filament signal, resemblance of the                               |
| 65- 72  | A8             | ---        | CWE        | Cosmic Web Environment (1)                                                |
| 74- 77  | I4             | ---        | Group      | [1/7231]?=-99 Group ID (2)                                                |
| 79- 81  | I3             | ---        | Ngroup     | [2/377]?=-99 Number of members in Group                                   |
| 83- 91  | A9             | ---        | Type       | Galaxy type ("satellite" (21316 occurrences),                             |
| 16874   | occurrences)   | or         | "central") | 93- 93 I1     ---   Flag       Flag (1=Objects that are close to the edge |
| 4926    | occurrences),  | "filament" | (17902     | occurrences) or                                                           |
| 22593   | occurrences)); | see        | Section    | 3.4.                                                                      |

**Note**: "cluster" (4926 occurrences), "filament" (17902 occurrences) or
          "field" (22593 occurrences)); see Section 3.4.
          The median density of our sample galaxies in clusters, filaments, and
          the field is 8.61, 3.09, and 1.53Mpc^-2^, respectively.
Note (2): We select the most massive galaxy in each group as a central and the
          rest as satellites. Galaxies that are not associated with any galaxy
          group (isolated) are either centrals whose satellites, in principle,
          are too faint to be detected in our volume-limited sample or they are
          ejected satellites orbiting beyond their halo's virial radius. We rely
          on our sample galaxies (our volume-limited-like sample) to identify
          groups. See section 3.5.

</details>
