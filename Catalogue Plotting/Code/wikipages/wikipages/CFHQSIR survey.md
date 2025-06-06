**Authors:** Basa S., Cuby J.-G., Cuillandre J.-C.,, Willott C., Moutard T., Chatron J., Arnouts S., Hudelot P., <Astron. Astrophys. 616, A55 (2018)>, =2018A&A...616A..55P (SIMBAD/NED BibCode)

## Summary: CFHQSIR survey 

The Canada-France-Hawaii Telescope Legacy Survey (CFHTLS) has been conducted over a five-year period at the CFHT with the MegaCam instrument, totaling 450 nights of observations. The Wide Synoptic Survey is one component of the CFHTLS, covering 155 square degrees in four patches of 23 to 65 square degrees through the whole MegaCam filter set (u*, g', r', i', z') down to i'_{AB} = 24.5. With the motivation of searching for high-redshift quasars at redshifts above 6.5, we extend the multi-wavelength CFHTLS-Wide data in the Y-band down to magnitudes of {sim} 22.5 for point sources (5{sigma}). We observed the four CFHTLS-Wide fields (except one quarter of the W3 field) in the Y-band with the WIRCam instrument (Wide-field InfraRed Camera) at the CFHT. Each field was visited twice, at least three weeks apart. Each visit consisted of two dithered exposures. The images are reduced with the Elixir software used for the CFHTLS and modified to account for the properties of near-InfraRed (IR) data. Two series of image stacks are subsequently produced: four-image stacks for each WIRCam pointing, and one-square- degree tiles matched to the format of the CFHTLS data release. Photometric calibration is performed on stars by fitting stellar spectra to their CFHTLS photometric data and extrapolating their Y-band magnitudes. After corrections accounting for correlated noise, we measure a limiting magnitude of Y_{AB}~=22.4 for point sources (5{sigma}) in an aperture diameter of 0.93 arcsecs, over 130 square degrees. We produce a multi-wavelength catalogue combining the CFHTLS-Wide optical data with our CFHQSIR (Canada-France High-z quasar survey in the near-InfraRed) Y-band data. We derive the Y-band number counts and compare them to the Vista Deep Extragalactic Observations survey (VIDEO). We find that the addition of the CFHQSIR Y-band data to the CFHTLS optical data increases the accuracy of photometric redshifts and reduces the outlier rate from 13.8% to 8.8% in the redshift range 1.05<~z<~1.2. The images and the catalogue for 8.6 million sources down to [(z'>=23.5) {lor} (Y>=23.0)] are released and available at the following URL: http://apps.canfar.net/storage/list/cjw/cfhqsir
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-A+A-616-A55/Subcatalogues/XMM-LSS/Plots/fieldcover.png)
## Catalogue Schema

<details>
<summary>cfhqsir.dat</summary>

| Bytes   | Format   | Units            | Label       | Explanations                                                     |
|:--------|:---------|:-----------------|:------------|:-----------------------------------------------------------------|
| 1- 16   | A16      | ---              | Tile        | CFHTLS T0007 tile (tile) (5)                                     |
| 18- 27  | E10.6    | deg              | RAdeg       | Right ascension (J2000.0) (RAJ2000)                              |
| 29- 38  | E10.6    | deg              | DEdeg       | Declination (J2000.0) (DECJ2000)                                 |
| 40- 47  | F8.4     | mag              | umag        | ?=-99 CFHTLS u total magnitude (AB)                              |
| 49- 56  | E8.4     | mag              | e_umag      | ?=-99 rms uncertainty on umag (err_umag)                         |
| 58- 65  | F8.4     | mag              | gmag        | ?=-99 CFHTLS g total magnitude (AB)                              |
| 67- 74  | F8.4     | mag              | e_gmag      | ?=-99 rms uncertainty on gmag (err_gmag)                         |
| 76- 83  | F8.4     | mag              | rmag        | ?=-99 CFHTLS r total magnitude (AB)                              |
| 85- 92  | F8.4     | mag              | e_rmag      | ?=-99 rms uncertainty on rmag (err_rmag)                         |
| 94-101  | F8.4     | mag              | imag        | ?=-99 CFHTLS i total magnitude (AB)                              |
| 103-110 | F8.4     | mag              | e_imag      | ?=-99 rms uncertainty on imag (err_imag)                         |
| 112-119 | F8.4     | mag              | ymag        | ?=-99 CFHTLS y total magnitude (AB)                              |
| 121-128 | E8.4     | mag              | e_ymag      | ?=-99 rms uncertainty on zmag (err_zmag)                         |
| 130-137 | F8.4     | mag              | zmag        | ?=-99 CFHTLS y total magnitude (AB)                              |
| 139-146 | E8.4     | mag              | e_zmag      | ?=-99 rms uncertainty on zmag (err_zmag)                         |
| 148-155 | F8.4     | mag              | YWmag       | ?=-99 WIRCam Y total magnitude (AB)                              |
| 157-164 | E8.4     | mag              | e_YWmag     | ?=-99 rms uncertainty on Ywirmag                                 |
| 166-174 | E9.5     | mag              | deltamag    | Weighted mean rescaling factor                                   |
| 176-183 | F8.4     | mag              | umagISO     | ?=-99 CFHTLS u isophotal magnitude (AB)                          |
| 185-192 | E8.4     | mag              | e_umagISO   | ?=-99 rms uncertainty on MAG_ISO_u                               |
| 194-201 | F8.4     | mag              | gmagISO     | ?=-99 CFHTLS g isophotal magnitude (AB)                          |
| 203-210 | F8.4     | mag              | e_gmagISO   | ?=-99 rms uncertainty on MAG_ISO_g                               |
| 212-219 | F8.4     | mag              | rmagISO     | ?=-99 CFHTLS r isophotal magnitude (AB)                          |
| 221-228 | F8.4     | mag              | e_rmagISO   | ?=-99 rms uncertainty on MAG_ISO_r                               |
| 230-237 | F8.4     | mag              | imagISO     | ?=-99 CFHTLS i isophotal magnitude (AB)                          |
| 239-246 | F8.4     | mag              | e_imagISO   | ?=-99 rms uncertainty on MAG_ISO_i                               |
| 248-255 | F8.4     | mag              | ymagISO     | ?=-99 CFHTLS y isophotal magnitude (AB)                          |
| 257-264 | E8.4     | mag              | e_ymagISO   | ?=-99 rms uncertainty on MAG_ISO_y                               |
| 266-273 | F8.4     | mag              | zmagISO     | ?=-99 CFHTLS z isophotal magnitude (AB)                          |
| 275-282 | E8.4     | mag              | e_zmagISO   | ?=-99 rms uncertainty on MAG_ISO_z (AB)                          |
| 284-291 | F8.4     | mag              | umagAUTO    | ?=-99 CFHTLS u Kron-like elliptical                              |
| 293-300 | E8.4     | mag              | e_umagAUTO  | ?=-99 rms uncertainty on MAG_AUTO_u                              |
| 302-309 | F8.4     | mag              | gmagAUTO    | ?=-99 CFHTLS g Kron-like elliptical                              |
| 311-318 | E8.4     | mag              | e_gmagAUTO  | ?=-99 rms uncertainty on MAG_AUTO_g                              |
| 320-327 | F8.4     | mag              | rmagAUTO    | ?=-99 CFHTLS r Kron-like elliptical                              |
| 329-336 | E8.4     | mag              | e_rmagAUTO  | ?=-99 rms uncertainty on MAG_AUTO_r                              |
| 338-345 | F8.4     | mag              | imagAUTO    | ?=-99 CFHTLS i Kron-like elliptical                              |
| 347-354 | E8.4     | mag              | e_imagAUTO  | ?=-99 rms uncertainty on MAG_AUTO_i                              |
| 356-363 | F8.4     | mag              | ymagAUTO    | ?=-99 CFHTLS y Kron-like elliptical                              |
| 365-372 | E8.4     | mag              | e_ymagAUTO  | ?=-99 rms uncertainty on MAG_AUTO_y                              |
| 374-381 | F8.4     | mag              | zmagAUTO    | ?=-99 CFHTLS z Kron-like elliptical                              |
| 383-390 | E8.4     | mag              | e_zmagAUTO  | ?=-99 rms uncertainty on MAG_AUTO_z                              |
| 392-399 | F8.4     | mag              | umagAPER    | ?=-99 CFHTLS u circular aperture                                 |
| 401-408 | E8.4     | mag              | e_umagAPER  | ?=-99 rms uncertainty on MAG_APER_u                              |
| 410-417 | F8.4     | mag              | gmagAPER    | ?=-99 CFHTLS g circular aperture                                 |
| 419-426 | E8.4     | mag              | e_gmagAPER  | ?=-99 rms uncertainty on MAG_APER_g                              |
| 428-435 | F8.4     | mag              | rmagAPER    | ?=-99 CFHTLS r circular aperture                                 |
| 437-444 | E8.4     | mag              | e_rmagAPER  | ?=-99 rms uncertainty on MAG_APER_r                              |
| 446-453 | F8.4     | mag              | imagAPER    | ?=-99 CFHTLS i circular aperture                                 |
| 455-462 | E8.4     | mag              | e_imagAPER  | ?=-99 rms uncertainty on MAG_APER_i                              |
| 464-471 | F8.4     | mag              | ymagAPER    | ?=-99 CFHTLS y circular aperture                                 |
| 473-480 | E8.4     | mag              | e_ymagAPER  | ?=-99 rms uncertainty on MAG_APER_y                              |
| 482-489 | F8.4     | mag              | zmagAPER    | ?=-99 CFHTLS z circular aperture                                 |
| 491-498 | E8.4     | mag              | e_zmagAPER  | ?=-99 rms uncertainty on MAG_APER_z                              |
| 500-504 | F5.3     | mag              | E(B-V)      | CFHTLS E(B-V) extinction (EB_V) (4)                              |
| 506-513 | F8.4     | mag              | YWmagISO    | ?=-99 WIRCam Y isophotal magnitude (AB)                          |
| 515-522 | E8.4     | mag              | e_YWmagISO  | ?=-99 rms uncertainty on MAG_APER_z                              |
| 524-531 | F8.4     | mag              | YWmagAPER   | ?=-99 WIRCam Y isophotal magnitude (AB)                          |
| 533-540 | E8.4     | mag              | e_YWmagAPER | ?=-99 WIRCam Y circular aperture                                 |
| 542-549 | F8.4     | mag              | YWmagAUTO   | ?=-99 WIRCam Y Kron-like elliptical                              |
| 551-558 | E8.4     | mag              | e_YWmagAUTO | ?=-99 rms uncertainty on MAG_AUTO_Ywir                           |
| 560-565 | I6       | pix+2            | AreaY       | Isophotal area above analysis threshold                          |
| 567-572 | I6       | pix+2            | AreaFY      | Isophotal area (filtered) above analysis                         |
| 574-581 | F8.2     | pix              | Xpos        | Object position along the x-axis                                 |
| 583-590 | F8.2     | pix              | Ypos        | Object position along the y-axis                                 |
| 592-603 | E12.10   | deg              | AaxisY      | Profile RMS along major axis                                     |
| 605-616 | E12.10   | deg              | BaxisY      | ? Profile RMS along minor axis                                   |
| 618-622 | F5.1     | deg              | thetaY      | Position angle (THETA_WORLD_Ywir) (2)                            |
| 624-629 | F6.3     | mag/arcsec+2     | muMaxY      | Peak Surface brightness above background                         |
| 631-633 | I3       | ---              | FlagsY      | Extraction flags (FLAGS_Ywir)                                    |
| 635-641 | F7.2     | pix              | FWHMImgY    | FWHM assuming a gaussian core                                    |
| 643-646 | F4.2     | ---              | ClassStarY  | Star/Galaxy classifier output                                    |
| 10      | pixels   | diameter.        | Note        | (4): E(B-V) extinction from Schlegelet al. (1998ApJ...500..525S) |
| 1       | field,   | W1_022929-070000 | and         | W1_023319-07000.                                                 |
| 2       | at       | CFHT.            | Not         | to be                                                            |
| 0       | =        | extended         | /           | galaxy / non-star                                                |
| 1       | =        | point-like       | source      | / star                                                           |

**Note**: All magnitudes are given in th AB system.
Note (2): The subscript "Ywir" refers to measurements performed on the
 WIRCam Y-band images.
Note (3): All aperture magnitude (MAG_APE) are given for an aperture
 of 10 pixels diameter.
Note (4): E(B-V) extinction from Schlegelet al. (1998ApJ...500..525S)
Note (5): Due to a miss-matchingbetween he CFHTLS catalogues,
 two CFHTLS tiles are missing in the W1 field,
 W1_022929-070000 and W1_023319-07000.
Note (6): the subscript "y" in the label of the magnitudes
 is the Terapix designation for the emplacement MegaCam
 i-band filter, also known as i2 at CFHT. Not to be
 confused with the subscript "Ywir" which refers to
 the WIRCam Y-band at CFHT.
Note (7): Star/Galaxy flag as follows:
  0 = extended / galaxy / non-star
  1 = point-like source / star

</details>
