**Authors:** Cappelluti N., Brusa M., Hasinger G., Comastri A., Zamorani G.,, Finoguenov A., Gilli R., Puccetti S., Miyaji T., Salvato M., Vignali C.,, Aldcroft T., Boehringer H., Brunner H., Civano F., Elvis M., Fiore F.,, Fruscione A., Griffiths R.E., Guzzo L., Iovino A., Koekemoer A.M.,, Mainieri V., Scoville N.Z., Shopbell P., Silverman J., Urry C.M., <Astron. Astrophys. 497, 635 (2009)>, =2009A&A...497..635C

## Summary: XMM-Newton wide-field survey in COSMOS field 

The COSMOS survey is a multiwavelength survey aimed to study the evolution of galaxies, AGN and large scale structures. Within this survey XMM-COSMOS a powerful tool to detect AGN and galaxy clusters. The XMM-COSMOS is a deep X-ray survey over the full 2deg^2^ of the COSMOS area. It consists of 55 XMM-Newton pointings for a total exposure of ~1.5Ms with an average vignetting-corrected depth of 40ks across the field of view and a sky coverage of 2.13deg^2^. The analysis was performed using the XMM-SAS data analysis package in the 0.5-2keV, 2-10keV and 5-10keV energy bands. Source detection has been performed using a maximum likelihood technique especially designed for raster scan surveys. The completeness of the catalogue as well as logN-logS and source density maps have been calibrated using Monte Carlo simulations.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-A+A-497-635/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>catalog.dat</summary>

| Bytes   | Format   | Units     | Label    | Explanations                               |
|:--------|:---------|:----------|:---------|:-------------------------------------------|
| 1- 7    | I7       | ---       | XID      | XID sequential number (1)                  |
| 9- 12   | A4       | --        | ---      | [XMMU]                                     |
| 14- 29  | A16      | ---       | XMMU     | IAU Name (JHHMMSS.s+DDMMSS)                |
| 31- 40  | F10.6    | deg       | RAdeg    | Right Ascension J2000 (degrees)            |
| 43- 50  | F8.6     | deg       | DEdeg    | Declination J2000 (degrees)                |
| 52- 55  | F4.2     | arcsec    | ePos     | Positional error (arcsec)                  |
| 57- 62  | F6.2     | 10-17W/m2 | S.5-2    | ?=-1.00 Flux in 0.5-2keV band (3)          |
| 64- 67  | F4.2     | 10-17W/m2 | e_S.5-2  | rms uncertainty on S.5-2 (3)               |
| 68      | A1       | ---       | n_S.5-2  | [*] * for negative flux value (2)          |
| 69- 72  | I4       | ct        | Ct.5-2   | Counts in 0.5-2keV band                    |
| 74- 77  | I4       | ct        | e_Ct.5-2 | rms uncertainty on Ct.5-2                  |
| 79- 86  | F8.2     | ---       | L.5-2    | ?=-1.00 0.5-2keV band detection likelihood |
| 88- 92  | F5.2     | ct/pix    | bg.5-2   | ?=-1.00 0.5-2keV band background counts    |
| 94- 98  | F5.2     | ks        | Exp.5-2  | 0.5-2keV band vignetting corrected         |
| 100-105 | F6.2     | 10-17W/m2 | S2-10    | ?=-1.00 Flux in 2-10keV band (3)           |
| 107-110 | F4.2     | 10-17W/m2 | e_S2-10  | ?=0.00 rms uncertainty on S2-10 (3)        |
| 111     | A1       | ---       | n_S2-10  | [*] * for negative flux value (2)          |
| 112-115 | I4       | ct        | Ct2-10   | Counts in 2-10keV band                     |
| 117-120 | I4       | ct        | e_Ct2-10 | rms uncertainty on Ct2-10                  |
| 122-129 | F8.2     | ---       | L2-10    | ?=-1.00 2-10keV band detection likelihood  |
| 131-136 | F6.2     | ct/pix    | bg2-10   | ?=-1.00 2-10keV band background counts     |
| 138-142 | F5.2     | ks        | Exp2-10  | 2-10keV band vignetting corrected exposure |
| 144-149 | F6.2     | 10-17W/m2 | S5-10    | ?=-1.00 Flux in 5-10keV band  (3)          |
| 151-154 | F4.2     | 10-17W/m2 | e_S5-10  | ?=0.00 rms uncertainty on S5-10 (3)        |
| 155     | A1       | ---       | n_S5-10  | [*] * for negative flux value (2)          |
| 156-159 | I4       | ct        | Ct5-10   | Counts in 5-10keV band                     |
| 161-164 | I4       | ct        | e_Ct5-10 | rms uncertainty on Ct5-10                  |
| 166-173 | F8.2     | ---       | L5-10    | ?=-1.00 5-10keV band detection likelihood  |
| 175-179 | F5.2     | ct/pix    | bg5-10   | ?=-1.00 5-10keV band background counts     |
| 181-185 | F5.2     | ks        | Exp5-10  | 5-10keV band vignetting corrected exposure |

**Note**: Internal reference number, from Hasinger et al.,
     Cat. J/ApJS/172/29, XMMC NNNNN in Simbad
Note (2): Negative flux values are upper-limits.
Note (3): or 10^-14^erg/cm^2^/s

</details>
