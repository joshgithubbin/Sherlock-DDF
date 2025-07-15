![Visualised Catalogue Ranking.](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/Catalogue%20Plotting/Code/wikipages/images/Catalogue%20Ranking.png?raw=true)


***


Within the wiki we are able to sort and rank each dataset based on the quality and depth of information contained within. In an ideal scenario we have time and resources to implement each and every catalogue within the deep drilling fields; however, many of these will be redundant or irrelevant for cross-matching. In ranking them we are able to prioritise catalogues for implementation and identify low-quality datasets not worth the expense to store and implement within a system. 


**A+:** Spectroscopic redshift catalogues with additional contextual information. Spectroscopic redshifts provide the most reliable estimation of host-transient separation and are a priority for implementation within cross-matching pipelines. Also of value is the contextual information regarding host morphology or the type of galaxy (or any other object) the transient has been cross-matched with.

**A:** Spectroscopic redshift catalogues with no additional contextual information. While not as suited to our morphology-based approach, the spectroscopic redshifts still provide the most value to the majority of cross-matching studies.

**B+:** Photometric redshift catalogues with additional contextual information. While not as reliable for cross-matching photometric redshifts still provide useful context both individually and when used in tandem with non-physical approaches. 

**B:** Photometric redshift catalogues with no additional contextual information. In these cases a cross-match using photometric redshifts may be less reliable and would be improved by utilising the additional contextual data from another catalogue.

**C+/C:** Photometric catalogues with/without additional contextual information. Such catalogues are less valuable than any containing redshift information and so are the lowest priority for implementation.


Lestrade takes the above ranking criteria into consideration when generating and organising both the Catalogue Wiki and the Auto-Wiki. This ranking is not exhaustive and exists only to provide a broad overview of considerations regarding catalogue implementation, which increase in complexity when discussing the implementation of multiple catalogues. A significant omittance is that of catalogue size and coverage. A catalogue containing one hundred spectroscopic redshifts will be outclassed by a catalogue containing ten thousand spectroscopic redshifts. When we discuss coverage, we also discuss depth - how wide an area within a given deep drilling field does the catalogue cover; how much coverage existed there previously; and to what redshift does this coverage extend to? A related consideration is the trade-off between spectroscopic and photometric redshifts. While catalogue size and quality matters, how do we rank the relative qualities of a catalogue containing one hundred spectroscopic redshift versus a catalogue with ten thousand photometric redshifts? We should also take care to consider catalogues that cover multiple fields. While they may be of lower quality compared to others, the extended coverage for the same level of manpower during implementation yields a good return on investment. Likewise we should be wary of redundant data and seek to avoid catalogues with many duplicate entries or less 'unique' coverage. These considerations, as with the ones in our ranking, cannot be taken in isolation and must be assessed on a case-by-case basis for more in-depth prioritisation. 
