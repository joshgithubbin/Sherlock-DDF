**Authors:** Cavuoti S., Brescia M., Riccio G., Salvato M., Longo G., <Mon. Not. R. Astron. Soc. 507, 5034-5052 (2021)>, =2021MNRAS.507.5034R (SIMBAD/NED BibCode)

## Summary: COSMOS2015 dataset machine learning photo-z 

In order to answer the open questions of modern cosmology and galaxy evolution theory, robust algorithms for calculating photometric redshifts (photo-z) for very large samples of galaxies are needed. Correct estimation of the various photo-z algorithms' performance requires attention to both the performance metrics and the data used for the estimation. In this work, we use the supervised machine learning algorithm MLPQNA (Multi-Layer Perceptron with Quasi-Newton Algorithm) to calculate photometric redshifts for the galaxies in the COSMOS2015 catalogue and the unsupervised Self-Organizing Maps (SOM) to determine the reliability of the resulting estimates. We find that for z_spec_<1.2, MLPQNA photo-z predictions are on the same level of quality as spectral energy distribution fitting photo-z. We show that the SOM successfully detects unreliable zspec that cause biases in the estimation of the photo-z algorithms' performance. Additionally, we use SOM to select the objects with reliable photo-z predictions. Our cleaning procedures allow us to extract the subset of objects for which the quality of the final photo-z catalogues is improved by a factor of 2, compared to the overall statistics.

## Catalogue Schema


## Spectroscopic Redshift 
 
*:*  
 

## Photometric Redshift 
 
*zphMl:* [0.02/1.47] Photometric redshift obtained 
 
<details>
<summary>mlphotoz.dat</summary>

| Bytes   | Format       | Units   | Label      | Explanations                                                     |
|:--------|:-------------|:--------|:-----------|:-----------------------------------------------------------------|
| 1- 18   | F18.14       | deg     | RAdeg      | [149.41/150.79] Right ascension (J2000)                          |
| 20- 37  | F18.16       | deg     | DEdeg      | [1.61/2.82] Declination (J2000)                                  |
| 39- 44  | I6           | ---     | Seq        | Object ID in the original COSMOS2015                             |
| 46- 50  | A5           | ---     | dataset    | [Run Test Train] A flag indicating whether                       |
| 52- 71  | F20.18       | ---     | zphMl      | [0.02/1.47] Photometric redshift obtained                        |
| 73- 95  | E23.17       | ---     | zphMlCoeff | ?=-99.99 In-cell outlier coefficient for                         |
| 97-116  | F20.18       | ---     | zphSED     | [0.0/4.72] SED fitting photometric redshift                      |
| 2015    | (photoZ_SED) | 118-140 | E23.17     | ---     zphSEDCoeff ?=-99.99 In-cell outlier coefficient for SED |
| 142-164 | E23.17       | ---     | resML-SED  | [-1.11/0.75] Residuals between ML and SED                        |
| 166-188 | E23.17       | ---     | zspCoeff   | ?=-99.99 In-cell outlier coefficient for                         |
| 190-194 | F5.1         | ---     | tMO        | Occupation of the SOM cell, to which this                        |

**Note**: objects are considered to be outliers if |*Coeff|>3.

</details>
