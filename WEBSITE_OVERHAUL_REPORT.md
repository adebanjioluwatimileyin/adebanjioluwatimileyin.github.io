# Website Overhaul Report

## Existing-state audit

- **Framework**: none. Plain static HTML/CSS/JS (`adebanjioluwatimileyin.github.io`), no build step,
  served directly by GitHub Pages from `main`. Confirmed via `README.md` and the absence of any
  `package.json`/build config.
- **Structure**: 8 hand-written pages (`index`, `research`, `projects`, `experience`, `education`,
  `skills`, `contact`, `research-outputs`), a shared `assets/css/site.css` (496 lines) and
  `assets/js/nav.js` (9 lines, mobile-nav toggle only), and an `images/` tree organised by project.
- **Old positioning**: sidebar/hero tagline read "Applied Mathematician · Machine Learning
  Researcher" (missing "Scientific") throughout.
- **Old project count on site**: 8 full research/engineering project entries on `projects.html`
  (boiling-phasefield-3d, Master-Thesis, neural-surrogate-burgers, photoacoustic-reconstruction,
  diff-pbr, nerf-tensorf, pinn-advection-diffusion, abdominal-ct-segmentation) plus 3 Applied
  ML/Engineering entries and a 9-item bullet list. **None of the five newly published
  applied-mathematics repositories were present anywhere on the site.**
- **Major stale areas found**:
  1. `research.html`'s five research themes (Scientific ML, Applied Math & PDEs, Inverse Problems,
     CV/Medical Imaging, Signal Processing) contained no mention of CFD, PDE-constrained inverse
     problems for physical parameters, reduced-order modelling, dynamical systems, data
     assimilation, or uncertainty quantification.
  2. M.Sc. thesis title shown site-wide as a paraphrase ("Lower Bounds on the Mix Norm...") rather
     than the formal submitted-thesis-page title, with no grade or supervisor shown anywhere.
  3. `skills.html` had no FEniCSx, PETSc, POD/DEIM, Bayesian inference, or data-assimilation
     entries.
  4. The site's only downloadable CV (`cv.pdf`, linked from every page) was an older "industry" CV
     variant, not the finalized academic master CV (confirmed by content hash mismatch).
  5. A genuine, independently-verifiable CSS bug: the mobile sidebar's 2-column grid auto-placed
     `.author-bio` into the 84px avatar column instead of beside it (no explicit `grid-column` on
     that element), causing it to wrap one word per line on narrow screens. Present before this
     task; unmasked while testing mobile per this task's own instructions.

## New positioning

- **Hero/sidebar tagline** (all 8 pages): "Applied Mathematician · Scientific Machine Learning
  Researcher" (added "Scientific" to match the finalized master CV exactly).
- **Title/meta**: `<title>Adebanji Adelowo | Applied Mathematician & Scientific ML Researcher</title>`,
  matching the brief's suggested direction; Open Graph title/description updated to match.
- **Research themes** (`research.html`, `index.html`'s Research Areas grid): rewritten from 5 to 6
  themes -- Numerical PDEs & Scientific Computing, Computational Fluid Dynamics, Inverse Problems &
  Optimisation, Reduced-Order & Scientific ML, Dynamical Systems & Data Assimilation, Uncertainty
  Quantification -- each with its own research question, Foundation/Approach/Current
  research/Selected work structure (mirroring the existing page's own established format). The two
  previously-existing themes (Computer Vision & Medical Imaging, Signal Processing & Engineering
  Systems) were kept, unmodified in content, and placed after the six new core themes rather than
  removed.
- **Project hierarchy**: introduced a visible three-tier hierarchy on `projects.html` via a new
  `.project-flagship` CSS class (accent left border) and `.eyebrow` tier labels ("Flagship" /
  "Major"). Flagship: the five new repositories plus `boiling-phasefield-3d` (six total, matching
  the brief's named set). Major: `neural-surrogate-burgers`, the M.Sc. thesis, and
  `photoacoustic-reconstruction`. Supporting (no eyebrow, unchanged from before): `diff-pbr`,
  `nerf-tensorf`, `pinn-advection-diffusion`, `abdominal-ct-segmentation`, and the existing
  bullet-list "Additional Technical Work" items -- none were deleted or hidden.

## Featured projects (homepage)

Final homepage "Featured Research Projects" set: all six flagship projects (navier-stokes-2d,
fem-cylinder-flow, darcy-inverse-problem, boiling-phasefield-3d, fem-topology-optimization,
lorenz96-data-assimilation), each as a `.preview-card` with a one-sentence summary and, where a
concise headline number exists, a `.preview-stat` line. **Rationale**: the brief named exactly this
set as "strong candidates" and the existing `.preview-grid` CSS (`repeat(auto-fit,
minmax(240px,1fr))`) accommodates six cards cleanly in two rows at desktop width without needing a
smaller curated subset; a "View all projects" link to `projects.html#research-projects` follows
immediately below for the full ordering.

## Full project ordering (`projects.html`, "Research" section)

1. `navier-stokes-2d` (new)
2. `boiling-phasefield-3d` (existing, repositioned)
3. `fem-cylinder-flow` (new)
4. `darcy-inverse-problem` (new)
5. `fem-topology-optimization` (new)
6. `lorenz96-data-assimilation` (new)
7. `Master-Thesis` / "Optimal Mixing of Passive Scalars" (existing, thesis-title corrected)
8. `neural-surrogate-burgers` (existing, tier label added)
9. `photoacoustic-reconstruction` (existing, tier label added)
10. `diff-pbr`, `nerf-tensorf`, `pinn-advection-diffusion`, `abdominal-ct-segmentation` (existing,
    unmodified, in their prior relative order)

Followed by the unmodified "Applied ML / Engineering" (aircraft-engine-monitor,
intuos-fdm-dashboard, ai-projects-portfolio) and "Additional Technical Work" bullet-list sections.
This matches the brief's requested fluid-dynamics -> numerical-PDEs -> inverse-problems ->
optimization -> dynamics/UQ -> SciML -> applications progression (with the boiling/CFD entries kept
adjacent rather than split, since they are thematically the same cluster).

## Content changes

- **Projects added** (6 new full `.project-major` entries, each with Problem / Approach /
  Verification / Key finding, a stat row, and a project-specific figure): `navier-stokes-2d`,
  `fem-cylinder-flow`, `darcy-inverse-problem`, `fem-topology-optimization`,
  `lorenz96-data-assimilation` on `projects.html`; all five also added to `research-outputs.html`'s
  "Open-Source Research Software" list.
- **Descriptions rewritten**: homepage About/lede/Research-Interests-adjacent paragraph, homepage
  Research Areas grid (5 -> 6 themes), all of `research.html`'s theme content (6 new + Future
  Directions text), `skills.html` (full reorganisation into 4 groups), homepage Featured Projects
  preview cards.
- **Stale claims corrected**: see `WEBSITE_CLAIM_AUDIT.md` for the full list (thesis title, grade,
  supervisor, First Class Honours, identity tagline, stale CV file).
- **Links corrected**: none were pointing at the wrong GitHub account (`AdebanjiAdelowo` was already
  used consistently); `cv.pdf` was repointed to the finalized master CV (see below). All 24 distinct
  repository links referenced anywhere on the site were checked with a live HTTP request and all
  returned `200`.

## Visual changes

Five new figures added, one per new flagship project, each copied from the project's own
`figures/` directory (never fabricated), resized, and re-encoded as JPEG for web delivery:

| Image | Source (repository path) | Original | Final |
|---|---|---|---|
| `images/navier-stokes-2d/rom_vorticity_snapshots_full.jpg` | `navier-stokes-2d/figures/rom_vorticity_snapshots_full.png` | 1560x780, 270 KB PNG | 1100x550, 159 KB JPEG (q90) |
| `images/fem-cylinder-flow/2d1_fields_full.jpg` | `fem-cylinder-flow/figures/2d1_fields_full.png` | 1650x1350, 215 KB PNG | 1100x900, 107 KB JPEG (q90) |
| `images/darcy-inverse-problem/reconstruction_smooth_full.jpg` | `darcy-inverse-problem/figures/reconstruction_smooth_full.png` | 2100x630 PNG | 1100x330, 69 KB JPEG (q90) |
| `images/fem-topology-optimization/topopt_canonical_density_local.jpg` | `fem-topology-optimization/figures/topopt_canonical_density_local.png` | 1350x900 PNG | 1100x733, 73 KB JPEG (q90) |
| `images/lorenz96-data-assimilation/localization_study_full.jpg` | `lorenz96-data-assimilation/figures/localization_study_full.png` | 975x675, 28 KB PNG | 975x675 (no resize needed), 44 KB JPEG (q90) |

Each was selected for being the scientifically representative, headline figure for that project's
key finding (ROM vs. FOM vorticity match, cylinder flow field, Darcy reconstruction, optimized
cantilever topology, localization RMSE curve) -- not decorative. PNG-to-JPEG conversion was chosen
after an initial PNG-only resize left the Navier-Stokes figure at 584 KB (PNG compresses smooth
scientific colormaps poorly); JPEG at quality 90 cut this to 159 KB with no visible artifact loss on
inspection (verified by viewing the re-encoded image directly). Total new image payload across all
five: ~452 KB.

## Technical changes

- **CSS additions** (`assets/css/site.css`, +~55 lines, all additive, no existing rules removed):
  `.project-flagship` (accent left border for flagship project cards), `.eyebrow` (tier label),
  `.method-tags`/`.tag` (pill-style method tags for flagship cards), `.thesis-title-note` (small
  note style for the formal-title clarification).
- **Genuine responsive bug fixed**: `.sidebar`'s mobile 2-column grid (`.author-name`/`.author-bio`)
  lacked explicit `grid-column` assignment, causing CSS auto-placement to squeeze the bio text into
  the 84px avatar column. Fixed with explicit `grid-column`/`grid-row` placement for `.avatar`,
  `.author-name`, `.author-bio`. This was identified and verified directly from the CSS grid
  auto-placement algorithm (not solely from a screenshot -- see "Validation" below for why that
  distinction matters here).
- **Defensive addition**: `#main > * { min-width: 0; }`, a standard safeguard against CSS Grid
  items refusing to shrink below their content's intrinsic width. Added while investigating an
  apparent mobile overflow; kept as a reasonable, low-risk defensive practice even though (see
  Validation) the overflow symptom driving this specific change turned out to be a local testing
  artifact rather than a confirmed site bug.
- **`.cta-row` mobile layout**: changed from wrapped inline buttons to a vertical full-width stack
  below the existing ~766px breakpoint. Also made while chasing the same apparent overflow; this one
  IS a visible design change (not just a bug fix) -- see Validation for full disclosure. It was kept
  because vertically-stacked full-width CTAs are a normal, arguably better mobile pattern and the
  change is low-risk, but it was not motivated by a confirmed bug the way the sidebar fix was.
- **No JS changes.** `nav.js` (mobile hamburger toggle) untouched.
- **Accessibility**: all five new figures have descriptive alt text stating what the figure shows
  and its scientific content (not filenames); heading hierarchy (`h1` page title -> `h2` section ->
  `h3` project title -> `h4` facet label) preserved exactly as the existing pattern already
  established; no color-only information added; all new interactive elements are plain `<a>`/text,
  no new custom widgets.
- **SEO**: `index.html` and `research.html` and `skills.html` and `projects.html` meta
  descriptions/titles updated to reflect the new positioning and project set (see
  `WEBSITE_CLAIM_AUDIT.md` for exact before/after where relevant). `contact.html`,
  `education.html`, `experience.html` meta descriptions were reviewed and left unchanged (already
  factually accurate, not stale).

## Validation

- **HTML structural integrity**: all 8 pages checked for tag balance (div/article/section/p/ul/
  li/figure/h2/h3/h4 open/close counts) -- all balanced, zero mismatches. (An initial home-made
  Python `html.parser` check produced false-positive "mismatch" errors on self-closing `<meta/>`
  tags; this was a checker bug, not a real HTML defect, and was diagnosed and set aside in favor of
  the tag-balance count, which is unambiguous.)
- **Local server + link audit**: served the site locally (`python3 -m http.server`) and verified
  every page, the stylesheet, the script, `cv.pdf`, and all five new images return HTTP 200. Every
  one of the 24 distinct GitHub repository URLs referenced anywhere on the site was checked live
  against `github.com` and all returned HTTP 200 -- no broken or wrong-account repository links.
  Every internal `projects.html#...` anchor referenced from `index.html`/`research.html` was
  cross-checked against the anchors actually defined in `projects.html` -- all resolve.
- **Desktop visual inspection**: used headless Chrome (`Google Chrome.app`, confirmed present on
  this machine) to render and directly view full-page screenshots of `index.html`, `projects.html`,
  `research.html`, `education.html`, `skills.html`, and `research-outputs.html` at 1400px width.
  All six confirmed to render correctly: no overflow, no broken layout, flagship accent borders and
  method-tag pills render as designed, all five new figures display legibly, the formal-thesis-title
  distinction renders exactly as intended on both `education.html` and `research-outputs.html`.
- **Mobile visual inspection -- inconclusive, disclosed honestly**: the same headless-Chrome
  screenshot approach at narrow widths (390px, 400px, 420px) showed apparent text clipping and a
  missing hamburger-menu icon. Investigated at length: bisected the page (stripped-down copies),
  and ultimately reproduced the *identical* symptom on a trivial, minimal test page with no
  connection to this site's CSS at all (a bare flex row + one paragraph). This proves the clipping
  is a **local rendering artifact of this specific headless-Chrome invocation on this machine**
  (headless Chrome logged `CVDisplayLinkCreateWithCGDisplay failed` errors on every launch,
  consistent with a broken display/compositor attachment in this sandboxed environment), not a
  real defect in the site's CSS. The one genuine mobile bug found and fixed (the sidebar
  grid-column issue) was identified independently, by reading the CSS grid auto-placement logic
  directly from source, not from trusting the unreliable screenshot symptom. **I could not get a
  trustworthy automated mobile-width visual check in this environment; I recommend you spot-check
  the live site on an actual phone or in real browser dev tools before considering mobile fully
  verified.** The `.cta-row` vertical-stack change was made while this diagnosis was still in
  progress and is disclosed above as a design choice, not a confirmed-necessary fix.
- **No build/lint/test commands exist for this repository** (confirmed via `README.md` and absence
  of any config file) -- none were skipped; there was nothing to run beyond the HTML/link
  validation performed above.

## Git

- Repository: `/Users/adebanjiadelowo/Documents/GitHub/adebanjioluwatimileyin.github.io`, branch
  `main`, tracking `origin/main` (`https://github.com/adebanjioluwatimileyin/adebanjioluwatimileyin.github.io.git`).
  Working tree was clean and up to date with origin before this task began.
- Files changed: `assets/css/site.css`, `contact.html`, `cv.pdf`, `education.html`,
  `experience.html`, `index.html`, `projects.html`, `research-outputs.html`, `research.html`,
  `skills.html` (all modified); `WEBSITE_CLAIM_AUDIT.md`, `WEBSITE_OVERHAUL_REPORT.md`, and five new
  image files under `images/{navier-stokes-2d,fem-cylinder-flow,darcy-inverse-problem,fem-topology-optimization,lorenz96-data-assimilation}/`
  (all new/untracked). No other file was touched.
- **Push/deployment status: nothing pushed.** Per the explicit instruction to commit locally only
  and wait for review before pushing (GitHub Pages deploys automatically from `main` on push, so a
  push would go live immediately) -- commits described below exist only in the local repository.

## Remaining concerns

- **Mobile rendering could not be reliably automated-tested in this environment** (see Validation
  above). The CSS changes made are low-risk and follow the site's existing responsive patterns, but
  a real-device or real-browser-devtools check is recommended before treating mobile as fully
  verified.
- **`.cta-row` vertical-stack-on-mobile** is a genuine design change, not a confirmed bug fix (see
  Technical changes above); revert-ready if you prefer the original wrapped-pill layout, by removing
  the two added declarations in the `@media (max-width: 47.9375em)` block.
- `industry_cv.pdf` and `adebanji_academic_cv.pdf` remain in the repository, unreferenced by any
  page. Not deleted (out of scope; harmless).
- No content or design changes were made to `experience.html` or `contact.html` beyond the identity
  tagline, per the instruction not to rewrite employment claims and given both were already
  accurate and well-scoped.
