_Lestrade_ is a Python package designed for non-real-time transient-host matching in the Legacy Survey of Space and Time ([LSST](https://rubinobservatory.org/explore/lsst)) Deep Drilling Fields. Designed as a companion to the real-time contextual classification software _Sherlock_, it allows for the downloading, analysis and use of Vizier Deep Drilling Field catalogues in transient science.

Lestrade is divided into two parts. The Lestrade Autowiki provides automated summaries of identified Deep Drilling Field catalogues and their ranked usefulness in transient-host matching, with figures detailing field coverage, redshift distribution and quality among other metrics. Schemas and abstracts for each catalogue are also provided. The Lestrade software allows users to build their own Autowikis with custom data and utilise any combination of this data in a Deep Drilling Field to carry out cross-matching. A machine learning element can assess the confidence of this matching and identify potential catalogue contaminants.

[The Vera C. Rubin Observatory](https://rubinobservatory.org/about) is a brand new astronomical facility on top of Cerro Pachón, a mountain in Northern Chile. Rubin Observatory will conduct a 10-year survey of the Southern Hemisphere sky (referred to as the Legacy Survey of Space and Time, or [LSST](https://rubinobservatory.org/explore/lsst)) with the goal of answering some of astronomers' biggest questions about the Universe.

Every night for a decade, Rubin Observatory will take images of the sky using a 3200 megapixel camera and six different optical filters. Each image covers an area as big as 40 full moons, and the giant 8.4-meter telescope can move between different positions in less than five seconds. In this way, the telescope will image the entire visible sky every 3-4 nights. This makes Rubin Observatory particularly good at detecting objects that have changed in brightness, like supernovae, or in position, like asteroids. Additionally, Rubin Observatory’s light-collecting power and sensitive camera will help us discover ~17 billion stars and ~20 billion galaxies we’ve never seen before.

In addition to the main wide-fast-deep survey (roughly 18,000 deg2), 10-20% of observing time will be dedicated to other programs, including mini-surveys and intensive observation of a set of Deep Drilling Fields. Deeper coverage and more frequent temporal sampling (in at least some of the ugrizy filters) will be obtained for the Deep Drilling Fields than for typical points on the sky. The full Deep Drilling Field program will address a broad range of science topics, including Solar System, Galactic, and extragalactic studies.


***

<img align="right" width="250" src="https://rubinobservatory.org/_next/image?url=https%3A%2F%2FRubin.canto.com%2Fdirect%2Fimage%2F3a4p6ip07138j1p7jt27e4es4t%2F5rWJEW6LnUsKPyEKMsTd080XNGs%2Fm3000%2F800&w=1920&q=75" />
<br/>

### Automated Catalogue Summarisation

- Use the wiki to identify relevant Deep Drilling Field catalogues.

- Construct automated summarisation and analysis of Vizier catalogues for your own wikis. 

- Assess catalogue utility and prioritise data for your science needs.  


<br/>

<img align="left" width="290" src="https://github.com/joshgithubbin/Sherlock-DDF/blob/main/Catalogue%20Plotting/Code/wikipages/images/1246549.png?raw=true" />
<br/>

### Transient-Host Matching

- Match Deep Drilling Field transients to the likeliest host via a morphology-based approach.

- Combine any number of catalogues for a given deep drilling field to carry out offline host matching.

- Assess catalogue usefulness by testing against known transient/galaxy matches.  

<br/>

<img align="right" width="250" src="https://rubinobservatory.org/_next/image?url=https%3A%2F%2FRubin.canto.com%2Fdirect%2Fimage%2F3a4p6ip07138j1p7jt27e4es4t%2F5rWJEW6LnUsKPyEKMsTd080XNGs%2Fm3000%2F800&w=1920&q=75" />
<br/>

### Assess Transient Matches

- Identify high and low-quality matches via a machine learning approach.

- Catch diffraction spikes and identify blended hosts via ML and human-rule techniques.

- Use annotated matches to train error-spotting algorithms.
<br/>
<br/>

***

## Other useful links

More information on Sherlock can be found in [documentation](https://lasair.readthedocs.io/en/develop/core_functions/sherlock.html) for the Lasair Transient Science Platform. 
