## Summary

Single-dish far-infrared (far-IR) and sub-millimetre (sub-mm) point source catalogues and their connections with galaxy catalogues at other wavelengths are of paramount importance to studying galaxy evolution. However, due to the large mismatch in spatial resolution, cross-matching galaxies detected at different wavelengths is not straightforward. This work aims to develop the next-generation deblended far-IR and sub-mm catalogues in deep extragalactic survey fields, by extracting photometry at the positions of known sources. We present the first application of our methodology in the COSMOS field. Our progressive deblending used the Monte Carlo Markov Chain (MCMC)-based Bayesian probabilistic framework known as XID+. The deblending process started from the Spitzer/MIPS 24um data, using an initial prior list composed of sources selected from the COSMOS2020 catalogue and radio catalogues from the VLA and the MeerKAT surveys, based on spectral energy distribution (SED) modelling which predicts fluxes of the known sources at the deblending wavelength. To speed up flux prediction, we made use of a neural network-based emulator. After deblending the 24um data, we proceeded to the Herschel PACS (100 & 160um) and SPIRE wavebands (250, 350 & 500um). Each time we constructed a tailor-made prior list based on the predicted fluxes of the known sources, taking into account the deblended photometry from the previous steps. Using simulated far-IR and sub-mm sky, we detailed the performance of our deblending pipeline. After validation with simulations, we then deblended the real observations from 24 to 500um and compared with blindly extracted catalogues and previous versions of deblended catalogues. As an additional test, we deblended the SCUBA-2 850um map and compared our deblended fluxes with ALMA measurements, demonstrating a higher level of flux accuracy compared to previous results. We publicly release our XID+ deblended point source catalogues, including best estimates and posterior probability distribution functions. These deblended long-wavelength data, which are cross-matched with multi-band photometry by construction, are crucial for studies such as deriving the fraction of dust-obscured star formation and better separation of quiescent galaxies from dusty star-forming galaxies.

## Catalogue Schema

<details>
<summary>master.dat catalogue schema</summary>

| Bytes   | Format   | Units    | Label      | Explanations                            |
|:--------|:---------|:---------|:-----------|:----------------------------------------|
| 1- 7    | I7       | ---      | ID         | COSMOS2020 ID                           |
| 9- 23   | F15.11   | deg      | RAdeg      | Right Ascension (J2000) from COSMOS2020 |
| 25- 39  | F15.11   | deg      | DEdeg      | Declination (J2000) from COSMOS2020     |
| 41- 49  | F9.6     | mJy      | F24        | 24um flux density (median) (F_24)       |
| 51- 58  | F8.6     | mJy/beam | Sigconf24  | Fitted Background of 24um map (median)  |
| 60- 67  | F8.6     | mJy      | s_F24      | Maximum of sigma+ and sigma- for        |
| 69- 76  | F8.6     | mJy/beam | e_F24      | Total error for 24um flux density       |
| 78- 87  | F10.6    | mJy      | F100       | ?=- 100um flux density (median) (F_100) |
| 89- 98  | F10.6    | mJy      | F160       | ?=- 160um flux density (median) (F_160) |
| 100-108 | F9.6     | mJy/beam | Sigconf100 | ?=- Fitted Background of 100um map      |
| 110-118 | F9.6     | mJy/beam | Sigconf160 | ?=- Fitted Background of 160um map      |
| 120-127 | F8.6     | mJy      | s_F100     | ?=- Maximum of sigma+ and sigma- for    |
| 129-137 | F9.6     | mJy/beam | e_F100     | ?=- Total error for 100um flux density  |
| 139-147 | F9.6     | mJy      | s_F160     | ?=- Maximum of sigma+ and sigma- for    |
| 149-157 | F9.6     | mJy/beam | e_F160     | ?=- Total error for 160um flux density  |
| 159-169 | F11.6    | mJy      | F250       | ?=- 250um flux density (median) (F_250) |
| 171-180 | F10.6    | mJy      | F350       | ?=- 350um flux density (median) (F_350) |
| 182-191 | F10.6    | mJy      | F500       | ?=- 500um flux density (median) (F_500) |
| 193-200 | F8.5     | mJy/beam | Sigconf250 | ?=- Fitted Background of 250um map      |
| 202-209 | F8.5     | mJy/beam | Sigconf350 | ?=- Fitted Background of 350um map      |
| 211-219 | F9.6     | mJy/beam | Sigconf500 | ?=- Fitted Background of 500um map      |
| 221-229 | F9.6     | mJy      | s_F250     | ?=- Maximum of sigma+ and sigma- for    |
| 231-239 | F9.6     | mJy/beam | e_F250     | ?=- Total error for 250um flux density  |
| 241-249 | F9.6     | mJy      | s_F350     | ?=- Maximum of sigma+ and sigma- for    |
| 251-259 | F9.6     | mJy/beam | e_F350     | ?=- Total error for 350um flux density  |
| 261-269 | F9.6     | mJy      | s_F500     | ?=- Maximum of sigma+ and sigma- for    |
| 271-279 | F9.6     | mJy/beam | e_F500     | ?=- Total error for 500um flux density  |
| 281-289 | F9.6     | mJy      | F850       | ?=- 850um flux density (median) (F_850) |
| 291-301 | F11.6    | mJy/beam | Sigconf850 | ?=- Fitted Background of 850um map      |
| 303-310 | F8.6     | mJy      | s_F850     | ?=- Maximum of sigma+ and sigma- for    |
| 312-322 | F11.6    | mJy/beam | e_F850     | ?=- Total error for 850um flux density  |
</details>
