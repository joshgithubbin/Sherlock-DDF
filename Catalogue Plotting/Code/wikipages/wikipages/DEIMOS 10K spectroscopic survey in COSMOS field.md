**Authors:** Capak P., Salvato M., Barger A.J., Cowie L.L., Faisst A.,, Hemmati S., Kakazu Y., Kartaltepe J., Masters D., Mobasher B., Nayyeri H.,, Sanders D., Scoville N.Z., Suh H., Steinhardt C., Yang F., <Astrophys. J., 858, 77 (2018)>, =2018ApJ...858...77H

## Summary: DEIMOS 10K spectroscopic survey in COSMOS field 

We present a catalog of 10718 objects in the COSMOS field, observed through multi-slit spectroscopy with the Deep Imaging Multi-Object Spectrograph (DEIMOS) on the Keck II telescope in the wavelength range ~5500-9800{AA}. The catalog contains 6617 objects with high-quality spectra (two or more spectral features), and 1798 objects with a single spectroscopic feature confirmed by the photometric redshift. For 2024 typically faint objects, we could not obtain reliable redshifts. The objects have been selected from a variety of input catalogs based on multi-wavelength observations in the field, and thus have a diverse selection function, which enables the study of the diversity in the galaxy population. The magnitude distribution of our objects is peaked at I_AB_~23 and K_AB_~21, with a secondary peak at K_AB_~24. We sample a broad redshift distribution in the range 0<z<6, with one peak at z~1, and another one around z~4. We have identified 13 redshift spikes at z>0.65 with chance probabilities <4x10^-4^, some of which are clearly related to protocluster structures of sizes >10Mpc. An object-to-object comparison with a multitude of other spectroscopic samples in the same field shows that our DEIMOS sample is among the best in terms of fraction of spectroscopic failures and relative redshift accuracy. We have determined the fraction of spectroscopic blends to about 0.8% in our sample. This is likely a lower limit and at any rate well below the most pessimistic expectations. Interestingly, we find evidence for strong lensing of Ly{alpha} background emitters within the slits of 12 of our target galaxies, increasing their apparent density by about a factor of 4.
## Coverage
![image](https://raw.githubusercontent.com/joshgithubbin/Sherlock-DDF/refs/heads/main/Catalogue%20Plotting/Catalogues/J-ApJ-858-77/Subcatalogues/COSMOS/Plots/fieldcover.png)
## Spectroscopic Redshift 
 
**zspec:** [0/6.7]? Spectroscopic redshift 
 

## Catalogue Schema

<details>
<summary>table2.dat</summary>

| Bytes   | Format   | Units   | Label    | Explanations                              |
|:--------|:---------|:--------|:---------|:------------------------------------------|
| 1- 9    | A9       | ---     | Mask     | Mask                                      |
| 11- 12  | I2       | h       | RAh      | [9/10] Hour of Right Ascension (J2000)    |
| 14- 15  | I2       | min     | RAm      | Minute of Right Ascension (J2000)         |
| 17- 18  | I2       | s       | RAs      | Second of Right Ascension (J2000)         |
| 20- 20  | A1       | ---     | DE-      | [+] Sign of the Declination (J2000)       |
| 21- 22  | I2       | deg     | DEd      | [1/2] Degree of Declination (J2000)       |
| 24- 25  | I2       | arcmin  | DEm      | Arcminute of Declination (J2000)          |
| 27- 30  | F4.1     | arcsec  | DEs      | Arcsecond of Declination (J2000)          |
| 32- 36  | F5.1     | deg     | PA       | [-98/303.2] Position angle, east of north |
| 38- 47  | A10      | "D/M/Y" | obs.date | UTC observation date                      |
| 49- 56  | A8       | "h:m:s" | obs.time | UTC observation time                      |
| 58- 60  | F3.1     | h       | Exp      | [0.3/2] Exposure time, hours              |
| 62- 65  | F4.2     | ---     | Airmass  | [1/3] Airmass                             |
| 67- 71  | A5       | ---     | Grating  | Grating (1)                               |
| 73- 77  | A5       | ---     | Filter   | Filter (GG455, GG495 or OG550)            |
| 79- 81  | I3       | ---     | Nsl      | [43/123] Number of slits assigned         |
| 83- 84  | I2       | ---     | Nz       | [30/96] Number of high-quality redshifts  |
| 86- 87  | I2       | ---     | Nsep     | [0/20] Number of serendipitous sources    |

**Note**: The 600ZD grating yields a wavelength coverage of ~4800-10000{AA}
    with a dispersion of 0.65{AA}/pixel and a spectral resolution of R~2000.
    The 830G grating yields a wavelength coverage of ~6700-10500{AA} with
    a dispersion of 0.47{AA}/pixel and a spectral resolution of R~2700.

</details>

<details>
<summary>table3.dat</summary>

| Bytes   | Format   | Units       | Label         | Explanations                                                         |
|:--------|:---------|:------------|:--------------|:---------------------------------------------------------------------|
| 1- 8    | A8       | ---         | ID            | Identifier (1)                                                       |
| 10- 20  | F11.7    | deg         | RAdeg         | [149.3/151] Right Ascension (J2000)                                  |
| 22- 31  | F10.8    | deg         | DEdeg         | [1.4/3] Declination (J2000)                                          |
| 33- 35  | I3       | ---         | sel           | [1/960] Subsample identifier (2)                                     |
| 37- 41  | F5.2     | mag         | imag          | [8/31.5]? I bandpass AB magnitude (3)                                |
| 43- 47  | F5.2     | mag         | Kmag          | [12/30.4]? K bandpass AB magnitude (3)                               |
| 49- 54  | F6.4     | ---         | zspec         | [0/6.7]? Spectroscopic redshift                                      |
| 56- 57  | I2       | ---         | Qf            | [0/19] Original spectroscopic quality flag                           |
| 59- 61  | F3.1     | ---         | Q             | [0/2] Comprehensive spectral quality flag                            |
| 63-132  | A70      | ---         | Remarks       | Remarks (6)                                                          |
| 24      | ;        | <COSMOS2015 | NNNNNNN>      | in Simbad).                                                          |
| 284     | ;        | <COSMOS     | NNNNNNN>      | in Simbad) and                                                       |
| 1236    | ;        | <[ICS2009]  | NNNNNNN>      | in Simbad).                                                          |
| 4       | and      | figure      | 1:            | sel=512*X+256*hiz+128*M+64*VLA+32*H+16*OVV+8*OII+4*PL+2*Fil+1*ser    |
| 2       | for      | further     | explanations. | Note (3): Magnitudes based on the ultradeep Subaru Hyper Suprime-Cam |
| 11-19   | indicate | broad       | emission      | lines.                                                               |
| 24      | are      | given       | the           | value Q=2, signaling reliable spectroscopic identification. The      |
| 29      | are      | given       | the           | value Q=1 for                                                        |
| 1       | source   | is          | matching      | with the uncertain                                                   |

**Note**: Object identifier from the major two photometric catalogues. An
    "L" in front of the number refers to the red multiband-band selected
    catalogue of Laigle+ (2016, J/ApJS/224/24 ; <COSMOS2015 NNNNNNN> in Simbad).
    A "C" in front of the number refers to the i-band selected catalogue of
    Capak+ (2007, II/284 ; <COSMOS NNNNNNN> in Simbad) and
    Ilbert+ (2009, J/ApJ/690/1236 ; <[ICS2009] NNNNNNN> in Simbad).
    If an object is not present in either of these catalogs it does not have an
    identifier (the value is blank).
Note (2): The subsample identifier, sel, is a decimal representation of a
    binary flag containing the X-ray, high-z, MIPS, VLA, Herschel,
    optically variable sources ("OVV", Salvato+, 2009ApJ...690.1250S),
    OII, PL AGN, Filler and Serendipitous flag following the order in
    table 4 and figure 1:
    sel=512*X+256*hiz+128*M+64*VLA+32*H+16*OVV+8*OII+4*PL+2*Fil+1*ser
    See section 2 for further explanations.
Note (3): Magnitudes based on the ultradeep Subaru Hyper Suprime-Cam
    (Tanaka et al. 2017arXiv170600566T) and UltraVista (Laigle+
    2016, J/ApJS/224/24), the Subaru Suprime-Cam (Ilbert+
    2009, J/ApJ/690/1236), and the Hubble ACS (Koekemoer+
    2007ApJS..172..196K) photometric catalogs. Because of field-coverage,
    bright star cut-outs, blending or other confusion issues not all objects
    in the spectroscopic catalogue are covered by a single photometric
    catalogue, and we thus have to refer to various different imaging
    datasets.
Note (4): Spectroscopic quality flag, Qf, following the original zCOSMOS
    scheme (Lilly+ 2009, J/ApJS/184/218, aka the column CClass),
    where values 11-19 indicate broad emission lines.
Note (5): Comprehensive quality flag Q combining spectroscopic and
    photometric redshift information, following Zheng et al.
    (2004, J/ApJS/155/73). The Qf flags 3, 4, 13, 14, 23, 24 are given
    the value Q=2, signaling reliable spectroscopic identification. The
    Qf flags 1, 2, 9, 11, 12, 19, 21, 22, 29 are given the value Q=1 for
    an uncertain spectroscopic identification. However, if the photometric
    redshift value for a Q=1 source is matching with the uncertain
    spectroscopic redshift within an interval dz/(1+z)<0.1, where
    dz=|z_spec_-z_phot_|, we raise the quality flag to Q=1.5. An
    unsuccessful redshift measurement yields Q=0.
Note (6): Remarks for most objects, in particular indicating the spectral
    features detected, e.g. the Ly{alpha} and Balmer lines (H{alpha},
    H{beta}, H{gamma}, ...) of hydrogen, or the MgII line, as well as the
    [CIV], CIII], CII], [OII], [OIII], NII, and [SII] emission lines.
    A "d" behind an emission line designation indicates a detected line
    doublet.
    A "br" behind an emission line refers to a broad emission line
    profile.
    An "abs" behind a line indicates its appearance in absorption rather
    than emission.
    "H&K" and "G" correspond to the Ca-H 3940{AA} and Ca-K 3960{AA}
    absorption lines and the G 4304{AA} absorption band, respectively.
    Other prominent absorption lines are MgI 5175{AA} and NaI 5892{AA}.
    Finally, "E+A" features indicate the forest of spectral emission and
    absorption features ("ringing") between the [OII] line and Ca-H & K,
    characteristic of post-starburst (E+A) galaxies.

</details>
