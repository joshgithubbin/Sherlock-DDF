## Summary

Abstract section not found.

## Catalogue Schema

<details>
<summary>table3.dat catalogue schema</summary>

| Bytes   | Format   | Units       | Label     | Explanations                               |
|:--------|:---------|:------------|:----------|:-------------------------------------------|
| 1- 5    | I5       | ---         | Seq       | Sequential number (unique object ID)       |
| 7- 8    | I2       | h           | RAh       | Right ascension (J2000)                    |
| 10- 11  | I2       | min         | RAm       | Right ascension (J2000)                    |
| 13- 18  | F6.3     | s           | RAs       | Right ascension (J2000) (1)                |
| 20      | A1       | ---         | DE-       | Declination sign (J2000)                   |
| 21- 22  | I2       | deg         | DEd       | Declination (J2000)                        |
| 24- 25  | I2       | arcmin      | DEm       | Declination (J2000)                        |
| 27- 31  | F5.2     | arcsec      | DEs       | Declination (J2000) (1)                    |
| 33- 39  | F7.2     | pix         | Xpos      | x-coordinate on image cdfs_r.fit           |
| 41- 47  | F7.2     | pix         | Ypos      | y-coordinate on image cdfs_r.fit           |
| 49- 54  | F6.3     | mag         | Rmag      | Total magnitude in R                       |
| 56- 60  | F5.3     | mag         | e_Rmag    | Mean error (1-{sigma}) of Rmag             |
| 62- 67  | F6.3     | mag         | ApRmag    | ? Aperture magnitude in R                  |
| 69- 75  | F7.3     | mag         | ApDRmag   | ? Aperture difference of Rmag (2)          |
| 77- 82  | F6.3     | mag/arcsec2 | mumax     | Central surface brightness in Rmag         |
| 84- 89  | F6.2     | arcsec      | MajAxis   | ? Major axis (3)                           |
| 91- 96  | F6.2     | arcsec      | MinAxis   | ? Minor axis (3)                           |
| 98-102  | F5.3     | deg         | PA        | ? Position angle, measured West to North   |
| 104-107 | I4       | ---         | Phot      | Flags on photometry (4)                    |
| 109     | I1       | ---         | Var       | Variability flag (0=not variable)(5)       |
| 111-115 | F5.3     | ---         | Stel      | ? Stellarity index from SExtractor         |
| 0       | for      | galaxy,     | 1         | for star)                                  |
| 117-131 | A15      | ---         | MCclass   | Multi-colour class (6)                     |
| 133-137 | F5.3     | ---         | MCz       | ? Mean redshift in distribution of p(z)    |
| 139-143 | F5.3     | ---         | e_MCz     | ? Mean error (1-{sigma}) of MCz            |
| 145-149 | F5.3     | ---         | MCz2      | ? Alternative redshift if p(z) bimodal     |
| 151-155 | F5.3     | ---         | e_MCz2    | ? Mean error (1-{sigma}) of MCz2           |
| 157-161 | F5.3     | ---         | MCzml     | ? Peak of redshift distribution p(z)       |
| 163-169 | F7.1     | Mpc         | dl        | ? Luminosity distance of MCz (7)           |
| 171-177 | F7.2     | ---         | chi2red   | Reduced Chi^2 of best-fitting template     |
| 179-184 | F6.2     | mag         | UjMAG     | ? Absolute Magnitude in Johnson U (8)      |
| 186-192 | F7.2     | mag         | e_UjMAG   | ? Mean error (1-{sigma}) of UjMag          |
| 194-199 | F6.2     | mag         | BjMAG     | ? Absolute Magnitude in Johnson B (8)      |
| 201-207 | F7.2     | mag         | e_BjMAG   | ? Mean error (1-{sigma}) of BjMag          |
| 209-214 | F6.2     | mag         | VjMAG     | ? Absolute Magnitude in Johnson V (8)      |
| 216-222 | F7.2     | mag         | e_VjMAG   | ? Mean error (1-{sigma}) of VjMag          |
| 224-229 | F6.2     | mag         | usMAG     | ? Absolute Magnitude in SDSS u (8)         |
| 231-237 | F7.2     | mag         | e_usMAG   | ? Mean error (1-{sigma}) of usMag          |
| 239-244 | F6.2     | mag         | gsMAG     | ? Absolute Magnitude in SDSS g (8)         |
| 246-252 | F7.2     | mag         | e_gsMAG   | ? Mean error (1-{sigma}) of gsMag          |
| 254-259 | F6.2     | mag         | rsMAG     | ? Absolute Magnitude in SDSS r (8)         |
| 261-267 | F7.2     | mag         | e_rsMAG   | ? Mean error (1-{sigma}) of rsMag          |
| 269-274 | F6.2     | mag         | UbMAG     | ? Absolute Magnitude in Bessell U (8)      |
| 276-280 | F5.2     | mag         | e_UbMAG   | ? Mean error (1-{sigma}) of UbMag          |
| 282-287 | F6.2     | mag         | BbMAG     | ? Absolute Magnitude in Bessell B (8)      |
| 289-295 | F7.2     | mag         | e_BbMAG   | ? Mean error (1-{sigma}) of BbMag          |
| 297-302 | F6.2     | mag         | VbMAG     | ? Absolute Magnitude in Bessell V (8)      |
| 304-310 | F7.2     | mag         | e_VbMAG   | ? Mean error (1-{sigma}) of VbMag          |
| 312-317 | F6.2     | mag         | S280MAG   | ? Absolute Magnitue in 280/40nm (8)(9)     |
| 319-325 | F7.2     | mag         | e_S280MAG | ? Mean error (1-{sigma}) of S280Mag        |
| 327-332 | F6.2     | mag         | S145MAG   | ? Absolute Magnitude in 145/10nm (10)      |
| 334-337 | F4.2     | mag         | e_S145MAG | ? Mean error (1-{sigma}) of S145Mag        |
| 339-348 | E10.4    | ct/m+2/s/nm | W420FE    | ? Flux in filter 420/30nm in run E (11)    |
| 350-359 | E10.4    | ct/m+2/s/nm | e_W420FE  | ? Mean error (1-{sigma}) of W420FE         |
| 361-370 | E10.4    | ct/m+2/s/nm | W462FE    | ? Flux in filter 462/14nm in run E (11)    |
| 372-381 | E10.4    | ct/m+2/s/nm | e_W462FE  | ? Mean error (1-{sigma}) of W462FE         |
| 383-392 | E10.4    | ct/m+2/s/nm | W485FD    | ? Flux in filter 485/31nm in run D (11)    |
| 394-403 | E10.4    | ct/m+2/s/nm | e_W485FD  | ? Mean error (1-{sigma}) of W485FD         |
| 405-414 | E10.4    | ct/m+2/s/nm | W518FE    | ? Flux in filter 518/16nm in run E (11)    |
| 416-425 | E10.4    | ct/m+2/s/nm | e_W518FE  | ? Mean error (1-{sigma}) of W518FE         |
| 427-436 | E10.4    | ct/m+2/s/nm | W571FD    | ? Flux in filter 571/25nm in run D (11)    |
| 438-447 | E10.4    | ct/m+2/s/nm | e_W571FD  | ? Mean error (1-{sigma}) of W571FD         |
| 449-458 | E10.4    | ct/m+2/s/nm | W571FE    | ? Flux in filter 571/25nm in run E (11)    |
| 460-469 | E10.4    | ct/m+2/s/nm | e_W571FE  | ? Mean error (1-{sigma}) of W571FE         |
| 471-480 | E10.4    | ct/m+2/s/nm | W571FS    | ? Combined flux in filter 571/25nm(11)(12) |
| 482-491 | E10.4    | ct/m+2/s/nm | e_W571FS  | ? Mean error (1-{sigma}) of W571FS         |
| 493-502 | E10.4    | ct/m+2/s/nm | W604FE    | ? Flux in filter 604/21nm in run E (11)    |
| 504-513 | E10.4    | ct/m+2/s/nm | e_W604FE  | ? Mean error (1-{sigma}) of W604FE         |
| 515-524 | E10.4    | ct/m+2/s/nm | W646FD    | ? Flux in filter 646/27nm in run D (11)    |
| 526-535 | E10.4    | ct/m+2/s/nm | e_W646FD  | ? Mean error (1-{sigma}) of W646FD         |
| 537-546 | E10.4    | ct/m+2/s/nm | W696FE    | ? Flux in filter 696/20nm in run E (11)    |
| 548-557 | E10.4    | ct/m+2/s/nm | e_W696FE  | ? Mean error (1-{sigma}) of W696FE         |
| 559-568 | E10.4    | ct/m+2/s/nm | W753FE    | ? Flux in filter 753/18nm in run E (11)    |
| 570-579 | E10.4    | ct/m+2/s/nm | e_W753FE  | ? Mean error (1-{sigma}) of W753FE         |
| 581-590 | E10.4    | ct/m+2/s/nm | W815FE    | ? Flux in filter 815/20nm in run E (11)    |
| 592-601 | E10.4    | ct/m+2/s/nm | e_W815FE  | ? Mean error (1-{sigma}) of W815FE         |
| 603-612 | E10.4    | ct/m+2/s/nm | W815FG    | ? Flux in filter 815/20nm in run G (11)    |
| 614-623 | E10.4    | ct/m+2/s/nm | e_W815FG  | ? Mean error (1-{sigma}) of W815FG         |
| 625-634 | E10.4    | ct/m+2/s/nm | W815FS    | ? Combined flux in filter 815/20nm(11)(12) |
| 636-645 | E10.4    | ct/m+2/s/nm | e_W815FS  | ? Mean error (1-{sigma}) of W815FS         |
| 647-656 | E10.4    | ct/m+2/s/nm | W856FD    | ? Flux in filter 856/14nm in run D (11)    |
| 658-667 | E10.4    | ct/m+2/s/nm | e_W856FD  | ? Mean error (1-{sigma}) of W856FD         |
| 669-678 | E10.4    | ct/m+2/s/nm | W914FD    | ? Flux in filter 914/27nm in run D (11)    |
| 680-689 | E10.4    | ct/m+2/s/nm | e_W914FD  | ? Mean error (1-{sigma}) of W914FD         |
| 691-700 | E10.4    | ct/m+2/s/nm | W914FE    | ? Flux in filter 914/27nm in run E (11)    |
| 702-711 | E10.4    | ct/m+2/s/nm | e_W914FE  | ? Mean error (1-{sigma}) of W914FE         |
| 713-722 | E10.4    | ct/m+2/s/nm | UFF       | ? Flux in filter U in run F (11)           |
| 724-733 | E10.4    | ct/m+2/s/nm | e_UFF     | ? Mean error (1-{sigma}) of UFF            |
| 735-744 | E10.4    | ct/m+2/s/nm | UFG       | ? Flux in filter U in run G (11)           |
| 746-755 | E10.4    | ct/m+2/s/nm | e_UFG     | ? Mean error (1-{sigma}) of UFG            |
| 757-766 | E10.4    | ct/m+2/s/nm | UFS       | ? Combined flux in filter U (11)(12)       |
| 768-777 | E10.4    | ct/m+2/s/nm | e_UFS     | ? Mean error (1-{sigma}) of UFS            |
| 779-788 | E10.4    | ct/m+2/s/nm | BFD       | ? Flux in filter B in run D (11)           |
| 790-799 | E10.4    | ct/m+2/s/nm | e_BFD     | ? Mean error (1-{sigma}) of BFD            |
| 801-810 | E10.4    | ct/m+2/s/nm | BFF       | ? Flux in filter B in run F (11)           |
| 812-821 | E10.4    | ct/m+2/s/nm | e_BFF     | ? Mean error (1-{sigma}) of BFF            |
| 823-832 | E10.4    | ct/m+2/s/nm | BFS       | ? Combined flux in filter B (11)(12)       |
| 834-843 | E10.4    | ct/m+2/s/nm | e_BFS     | ? Mean error (1-{sigma}) of BFS            |
| 845-854 | E10.4    | ct/m+2/s/nm | VFD       | ? Flux in filter V in run D (11)           |
| 856-865 | E10.4    | ct/m+2/s/nm | e_VFD     | ? Mean error (1-{sigma}) of VFD            |
| 867-876 | E10.4    | ct/m+2/s/nm | RFD       | ? Flux in filter R in run D (11)           |
| 878-887 | E10.4    | ct/m+2/s/nm | e_RFD     | ? Mean error (1-{sigma}) of RFD            |
| 889-898 | E10.4    | ct/m+2/s/nm | RFE       | ? Flux in filter R in run E (11)           |
| 900-909 | E10.4    | ct/m+2/s/nm | e_RFE     | ? Mean error (1-{sigma}) of RFE            |
| 911-920 | E10.4    | ct/m+2/s/nm | RFF       | ? Flux in filter R in run F (11)           |
| 922-931 | E10.4    | ct/m+2/s/nm | e_RFF     | ? Mean error (1-{sigma}) of RFF            |
| 933-942 | E10.4    | ct/m+2/s/nm | RFG       | ? Flux in filter R in run G (11)           |
| 944-953 | E10.4    | ct/m+2/s/nm | e_RFG     | ? Mean error (1-{sigma}) of RFG            |
| 955-964 | E10.4    | ct/m+2/s/nm | RFS       | ? Combined flux in filter R (11)(12)       |
| 966-975 | E10.4    | ct/m+2/s/nm | e_RFS     | ? Mean error (1-{sigma}) of RFS            |
| 977-986 | E10.4    | ct/m+2/s/nm | IFD       | ? Flux in filter I in run D (11)           |
| 988-997 | E10.4    | ct/m+2/s/nm | e_IFD     | ? Mean error (1-{sigma}) of IFD            |

**Note**: Internal accuracy 0.15"

</details>
