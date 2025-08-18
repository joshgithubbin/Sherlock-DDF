

**Authors:** Bock J., Altieri B., Amblard A., Arumugam V., Aussel H.,, Babbedge T., Beelen A., Bethermin M., Blain A., Boselli A., Bridge C.,, Brisbin D., Buat V., Burgarella D., Castro-Rodriguez N., Cava A.,, Chanial P., Cirasuolo M., Clements D.L., Conley A., Conversi L., Cooray A.,, Dowell C.D., Dubois E.N., Dwek E., Dye S., Eales S., Elbaz D., Farrah D.,, Feltre A., Ferrero P., Fiolet N., Fox M., Franceschini A., Gear W.,, Giovannoli E., Glenn J., Gong Y., Gonzalez Solares E.A., Griffin M.,, Halpern M., Harwit M., Hatziminaoglou E., Heinis S., Hurley P., Hwang H.S.,, Hyde A., Ibar E., Ilbert O., Isaak K., Ivison R.J., Lagache G.,, Le Floc'h E., Levenson L., Faro B.L., Lu N., Madden S., Maffei B.,, Magdis G., Mainetti G., Marchetti L., Marsden G., Marshall J.,, Mortier A.M.J., Nguyen H.T., O'Halloran B., Omont A., Page M.J.,, Panuzzo P., Papageorgiou A., Patel H., Pearson C.P., Perez-Fournon I.,, Pohlen M., Rawlings J.I., Raymond G., Rigopoulou D., Riguccini L.,, Rizzo D., Rodighiero G., Roseboom I.G., Rowan-Robinson M.,, Sanchez Portal M., Schulz B., Scott D., Seymour N., Shupe D.L.,, Smith A.J., Stevens J.A., Symeonidis M., Trichas M., Tugwell K.E.,, Vaccari M., Valtchanov I., Vieira J.D., Viero M., Vigroux L., Wang L.,, Ward R., Wardlow J., Wright G., Xu C.K., Zemcov M., <Mon. Not. R. Astron. Soc. 424, 1614-1635 (2012)>, =2012MNRAS.424.1614O, +2012MNRAS.419..377S, =2014yCat.8095....0O

## Summary: Herschel Multi-tiered Extragalactic Survey

The Herschel Multi-tiered Extragalactic Survey (HerMES) is a legacy programme designed to map a set of nested fields totalling ~380deg^2^. Fields range in size from 0.01 to ~20deg^2^, using the Herschel-Spectral and Photometric Imaging Receiver (SPIRE) (at 250, 350 and 500um) and the Herschel-Photodetector Array Camera and Spectrometer (PACS) (at 100 and 160um), with an additional wider component of 270deg^2^ with SPIRE alone. These bands cover the peak of the redshifted thermal spectral energy distribution from interstellar dust and thus capture the reprocessed optical and ultraviolet radiation from star formation that has been absorbed by dust, and are critical for forming a complete multiwavelength understanding of galaxy formation and evolution.

## Coverage 

 

 
![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/VIII_95/im/coverage.png?raw=true)

## Spectroscopic Redshift 



**None:** None 




<details><summary>See Figure . . .</summary>

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/VIII_95/im/ZSP.png?raw=true)

</details>

## Photometric Redshift 



**None:** None 




<details><summary>See Figure . . .</summary>

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/VIII_95/im//ZPH.png?raw=true)

</details>

## Morphology 



**None:** None 

**None:** None 

**None:** None 




<details><summary>See Figure . . .</summary>

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/pages/VIII_95/im//morphology.png?raw=true)

</details>
                      
## Type Flags 





## Catalogue Schema 



<details>
<summary>merge.dat catalogue schema</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                                                   |
|:--------|:---------|:--------|:--------|:-------------------------------------------------------------------------------|
| 1- 22   | A22      | ---     | Field   | Field designation                                                              |
| 24- 40  | A17      | ---     | ---     | [2HERMES S250 SF D]                                                            |
| 42- 57  | A16      | ---     | 2HERMES | HerMES ID, JHHMMSS.s+DDMMSS (G1)                                               |
| 61- 69  | F9.5     | deg     | RAdeg   | Right Ascension (J2000)                                                        |
| 71- 79  | F9.5     | deg     | DEdeg   | Declination (J2000)                                                            |
| 81- 96  | E16.11   | mJy     | F250    | Herschel/SPIRE flux density at 250um                                           |
| 98-113  | E16.11   | mJy     | e_F250  | Instrumental error in flux 250um density                                       |
| 115-130 | E16.11   | mJy     | F350    | Herschel/SPIRE flux density at 350um                                           |
| 132-147 | E16.11   | mJy     | e_F350  | Instrumental error in flux 350um density                                       |
| 149-164 | E16.11   | mJy     | F500    | Herschel/SPIRE flux density at 500um                                           |
| 166-181 | E16.11   | mJy     | e_F500  | Instrumental error in flux 500um density                                       |
| 183-198 | E16.11   | mJy     | E_F250  | Total error (instrumental + confusion) in 250um flux density                   |
| 200-215 | E16.11   | ---     | chi250  | Local reduced {chi}^2^ statistic of 250um photometry fit in 11x11 pixel window |
| 217-232 | E16.11   | mJy     | E_F350  | Total error (instrumental + confusion) in 350um flux density                   |
| 234-249 | E16.11   | ---     | chi350  | Local reduced {chi}^2^ statistic of 350um photometry fit in 11x11 pixel window |
| 251-266 | E16.11   | mJy     | E_F500  | Total error (instrumental + confusion) in 500um flux density                   |
| 268-283 | E16.11   | ---     | chi500  | Local reduced {chi}^2^ statistic of 500um photometry fit in 11x11 pixel window |
| 285-290 | I6       | ---     | gID     | ID of the segment  where the source is                                         |
| 292-295 | I4       | ---     | Ng      | Number of sources in the segment gid                                           |
| 297-304 | F8.5     | mJy     | bg250   | Background subtracted from 250um map (G2)                                      |
| 306-313 | F8.5     | mJy     | bg350   | Background subtracted from 350um map (G2)                                      |
| 315-322 | F8.5     | mJy     | bg500   | Background subtracted from 550um map (G2)                                      |
| 324-330 | A7       | ---     | Com     | Comment                                                                        |
</details>

<details>
<summary>sf???.dat catalogue schema</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                                                          |
|:--------|:---------|:--------|:--------|:--------------------------------------------------------------------------------------|
| 1- 22   | A22      | ---     | Field   | Field designation                                                                     |
| 24- 32  | A9       | ---     | ---     | [2HERMES S]                                                                           |
| 33- 35  | I3       | um      | lam     | Herschel filter (250, 300 or 500)                                                     |
| 37- 40  | A4       | ---     | ---     | [SF D]                                                                                |
| 42- 57  | A16      | ---     | 2HERMES | HerMES ID, JHHMMSS.s+DDMMSS (G1)                                                      |
| 61- 69  | F9.5     | deg     | RAdeg   | Right ascension (J2000)                                                               |
| 71- 79  | F9.5     | deg     | DEdeg   | Declination (J2000)                                                                   |
| 81- 96  | E16.11   | mJy     | Flux    | Source flux density                                                                   |
| 98-113  | E16.11   | mJy     | e_Flux  | Source flux density formal uncertainty (instrumental noise)                           |
| 115-130 | E16.11   | mJy     | E_Flux  | Total uncertainty in the source flux density, due to confusion and instrumental noise |
| 132-147 | E16.11   | ---     | chi2    | Local reduced {chi}^2^ statistic of photometry fit in 11x11 pixel window              |
| 149-154 | I6       | ---     | gID     | ID of the segment  where the source is                                                |
| 156-159 | I4       | ---     | Ng      | Number of sources in the segment gid                                                  |
| 161-169 | F9.6     | mJy     | bg      | Background subtracted from map in observed band (mJy/beam) (G2)                       |
| 171-177 | A7       | ---     | Com     | Comments                                                                              |
</details>

<details>
<summary>sx???.dat catalogue schema</summary>

| Bytes   | Format   | Units   | Label   | Explanations                                                                                       |
|:--------|:---------|:--------|:--------|:---------------------------------------------------------------------------------------------------|
| 1- 22   | A22      | ---     | Field   | Field designation                                                                                  |
| 24- 32  | A9       | ---     | ---     | [2HERMES S]                                                                                        |
| 33- 35  | I3       | um      | lam     | Herschel filter (250, 300 or 500)                                                                  |
| 37- 40  | A4       | ---     | ---     | [SX D]                                                                                             |
| 42- 59  | A18      | ---     | 2HERMES | HerMES ID, JHHMMSS.s+DDMMSS, or JHHMMSS.s+DDNNNSS or JHHMMSS.s+DDNNNNSS (G1)                       |
| 61- 69  | F9.5     | deg     | RAdeg   | Right ascension (J2000)                                                                            |
| 71- 79  | F9.5     | deg     | DEdeg   | Declination (J2000)                                                                                |
| 81- 90  | F10.5    | mJy     | Flux    | Source flux density                                                                                |
| 92-100  | F9.5     | mJy     | e_Flux  | Source flux density formal uncertainty (instrumental noise)                                        |
| 102-113 | F12.5    | ---     | S/N     | Signal to instrumental noise: Flux/e_Flux                                                          |
| 115-123 | F9.5     | deg     | e_RAdeg | Right ascension uncertainty                                                                        |
| 125-133 | F9.5     | deg     | e_DEdeg | Declination uncertainty                                                                            |
| 135-143 | F9.5     | mJy     | E_Flux  | ?=-99.99999 Total uncertainty in the source flux density, due to confusion and instrumental noise  |
| 145-154 | F10.5    | ---     | SNR     | ?=-99.999 Signal to total noise: Flux/E_Flux                                                       |
| 156-177 | E22.15   | mJy     | F1      | ?=1E+20 Source flux density, as measured using a map based on the first half of the data           |
| 178-200 | E23.15   | ---     | SN1     | ?=1E+20 Signal to instrumental noise, as measured using a map based on the first half of the data  |
| 202-223 | E22.15   | mJy     | F2      | ?=1E+20 Source flux density, as measured using a map based on the second half of the data          |
| 224-246 | E23.15   | ---     | SN2     | ?=1E+20 Signal to instrumental noise, as measured using a map based on the second half of the data |
| 248     | A1       | ---     | fc      | [1T] source lies within a well-defined central region of the map                                   |
| 250-256 | A7       | ---     | Com     | Comment                                                                                            |
</details>

<details>
<summary>img.dat catalogue schema</summary>

| Bytes   | Format   | Units      | Label    | Explanations                          |
|:--------|:---------|:-----------|:---------|:--------------------------------------|
| 1- 17   | A17      | ---        | Field    | Field designation                     |
| 19- 27  | F9.5     | deg        | RAdeg    | Right Ascension of center (J2000)     |
| 28- 36  | F9.5     | deg        | DEdeg    | Declination of center (J2000)         |
| 38- 42  | F5.2     | arcsec/pix | Scale    | Scale of the image                    |
| 44- 47  | I4       | pix        | Nx       | Number of pixels along X-axis         |
| 48      | A1       | ---        | ---      | [x]                                   |
| 49- 52  | I4       | pix        | Ny       | Number of pixels along Y-axis         |
| 54- 56  | I3       | um         | lam      | Wavelength (250, 350 or 500)          |
| 58-108  | A51      | ---        | FileName | Name of FITS file in subdirectory img |
| 109-156 | A48      | ---        | Title    | Title and comments                    |
</details>

        
        