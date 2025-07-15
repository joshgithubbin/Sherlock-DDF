Several approaches exist for catalogue-based transient-host cross-matching. Currently Lestrade utilises two morphology-based approaches; the 'A-Value' Method and the 'Directional Light Radius' Method, both of which we detail below.

## The A-Value Approach

The A-Value method is to treat the elliptical shape of the galaxy as being strictly circular; i.e., the galaxy is equally extended in all directions (either at radius \texttt{A} or \texttt{B}, an average of the two, or a mean half-light radius). We calculate the angular separation between the transient and the galactic centre and express it in units of this extension to give a dimensionless distance - the A-Value.

## The Directional Light Radius Approach

Here we begin by normalizing the separation by calculating it in units of the elliptical radius R along the line connecting the transient position to the given host centre. Here then R is provided by:

![](https://github.com/joshgithubbin/Sherlock-DDF/blob/main/Catalogue%20Plotting/Code/wikipages/images/DLR%20Formulae.png?raw=true)

where θ is analogous to THETA. Calculating this radius in units of arcseconds, and also having the angular separation in units of arcseconds, we can calculate the dimensionless ratio d_DLR as the transient-host separation over the Directional Light Radius (R, as defined above).
