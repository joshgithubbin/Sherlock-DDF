**Authors:** Sevilla-Noarbe I., Fernandez E., Carretero J., Eriksen M.,, Serrano S., Alarcon A., Amara A., Casas R., Castander F.J., de Vicente J.,, Folger M., Garcia-Bellido J., Gaztanaga E., Hoekstra H., Miquel R.,, Padilla C., Sanchez E., Stothert L., Tallada P., Tortorelli L., <Mon. Not. R. Astron. Soc., 483, 529-539 (2019)>, =2019MNRAS.483..529C (SIMBAD/NED BibCode)

## Summary: Star-galaxy multi narrow-band classification 

Classification of stars and galaxies is a well-known astronomical problem that has been treated using different approaches, most of them relying on morphological information. In this paper, we tackle this issue using the low-resolution spectra from narrow-band photometry, provided by the Physics of the Accelerating Universe survey. We find that, with the photometric fluxes from the 40 narrow-band filters and without including morphological information, it is possible to separate stars and galaxies to very high precision, 98.4 per cent purity with a completeness of 98.8 per cent for objects brighter than I=22.5. This precision is obtained with a convolutional neural network as a classification algorithm, applied to the objects' spectra. We have also applied the method to the ALHAMBRA photometric survey and we provide an updated classification for its Gold sample.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-MNRAS-483-529/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>tablea1.dat</summary>

| Bytes   | Format   | Units   | Label      | Explanations                              |
|:--------|:---------|:--------|:-----------|:------------------------------------------|
| 1- 11   | I11      | ---     | ID         | ALHAMBRA's unique object identifier       |
| 13- 20  | F8.4     | deg     | RAdeg      | Right ascension (J2000)                   |
| 22- 28  | F7.4     | deg     | DEdeg      | Declination (J2000)                       |
| 30- 33  | F4.2     | ---     | Starflag   | ALHAMBRA's Statistical STAR/GALAXY        |
| 35- 52  | F18.15   | mag     | F814Wmag   | Isophotal magnitude (AB)                  |
| 54- 75  | F22.18   | mag     | e_F814Wmag | [] Error on F814Wmag                      |
| 77- 98  | E22.19   | ---     | cnn        | CNN star/galaxy discriminator probability |
| 20      | optical, | three   | NIR,       | and F814W). For those without, the        |

**Note**: We only provide a classification for those objects with all bands
          measured (20 optical, three NIR, and F814W). For those without, the
          class is set to a 'sentinel' value of -1.

</details>
