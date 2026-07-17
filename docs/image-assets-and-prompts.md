# Image Assets: SHIPPED illustration system + the one remaining drop-in

## Status: 13 of 14 images are DONE and included
The site now ships with a complete custom illustration system ("Warm Cartography," see illustration-philosophy.md): layered landscape scenes in the exact brand palette, one per content block, each composition designed for its section's meaning.

| File (in site/) | Where | Composition and why it fits the block |
|---|---|---|
| images/generated/home-hero.jpg | Home hero | A path winding through calm hills toward a low rust sun, small home mid-journey. The block invites visitors to "start here": the image is literally the road ahead. |
| images/generated/ltc-hero.jpg | LTC page hero | A deep-rooted tree with three canopy circles (three generations) sheltering a home. LTC planning as multigenerational shelter. |
| images/generated/annuities-hero.jpg | Annuities hero | Evenly repeated wave bands and a small boat riding them. Income that arrives like the tide: regular, dependable. |
| images/generated/life-hero.jpg | Life hero | Concentric protective arcs over a family of three homes. The canopy of protection the block describes. |
| images/generated/medicare-hero.jpg | Medicare hero | A lighthouse on a calm coast. Navigation and guidance through complex waters, matching the referral positioning. |
| images/generated/disability-hero.jpg | Disability hero | A rust-arched bridge carrying a household across a river gap. Income protection bridging the period when work stops. |
| images/blog/ltc-covers-thumb.jpg | "What LTC covers" | A large rust umbrella over homes: coverage, literally. |
| images/blog/medicare-vs-ltc-thumb.jpg | "Medicare vs LTC" | Two summits, navy vs rust, echoing the article's two-color comparison table. |
| images/blog/when-to-buy-thumb.jpg | "When to buy" | The sun's arc across the sky with the present moment in rust: the planning window. |
| images/blog/cost-thumb.jpg | "How much it costs" | Five geological strata (the five cost factors) with one embedded rust coin (the premium). |
| images/blog/traditional-vs-hybrid-thumb.jpg | "Traditional vs hybrid" | Three paths converging on one horizon: three designs, one goal. |
| images/og-image.jpg | Social sharing (all pages) | Brand lockup over the landscape system. 1200x630. |
| favicon.svg + images/favicon-512.png | Browser tab / home screen | The system's horizon-in-circle mark with rust sun. |

All are lightweight (18-53KB), dimensioned in markup (no layout shift), and regenerable from build/imagegen.py (edit the SVG scene functions and re-run).

## The ONE manual drop-in: the real headshot
- Target path: images/headshot/mischa-wright-headshot.jpg
- Source: "Head shot Mischa Wright.jpg" in the Drive Head Shots folder
- Crop: 4:5 portrait (roughly 960x1200), face in upper third
- Until dropped in, the slot shows a clean warm gradient inside the rust offset frame; nothing looks broken.

## Optional future upgrade
If you later commission lifestyle photography, shoot to the compositions above (same subjects, same warmth) and swap files 1:1; the markup needs no changes. Keep the illustration set for blog thumbs and social; consistency there is worth more than photorealism.
