# Website Deployment Report

## Thesis wording

**Previous sentence** (`index.html` About paragraph and `education.html` thesis line):
> "... derived and numerically validated mixing-rate bounds for a passive scalar advected by
> incompressible, enstrophy-constrained flow."

**Evidence reviewed**: the actual submitted thesis source,
`/Users/adebanjiadelowo/Documents/Academic_Career/05_Research/Research_Projects/Lower_Bounds_Mix_Norm/thesis1.tex`,
specifically its "Numerical Discussion" section. The cited theorem the thesis works from
(Iyer-Kiselev-Xu 2014, Theorem 1.1) predicts that the fitted exponential mix-norm decay rate
$\lambda(b)$ should scale as $b^{-1}$ with the initial-data support-size parameter $b$. The thesis's
own numerical fit gives $\lambda \sim b^{-1.78}$ instead, and the thesis's own text describes this as
a deviation: *"This deviation is consistent with the known gap between the greedy LTD strategy and
the global optimum; higher resolution (larger N) would be needed to access the true asymptotic
regime."* The thesis explicitly reports a qualitative match (the decay rate increases as $b$
decreases, as predicted) alongside a quantitative mismatch (the exponent itself does not match).

**Final sentence**:
> "... derived and numerically investigated mixing-rate bounds for a passive scalar advected by
> incompressible, enstrophy-constrained flow."

**Reason for terminology choice**: under this project's own verification/validation taxonomy
(exact/manufactured solutions and convergence studies -> verification; independent physical/
reference evidence confirming agreement -> validation; numerical exploration of theoretical
behaviour -> investigation/evaluation), "validated" is not accurate here -- the numerical work did
not confirm quantitative agreement with the theorem it was testing, it found and reported a
discrepancy. "Investigated" is the precise term: it describes numerically exploring the theorem's
predicted behaviour and reporting what was actually found, including the mismatch, without implying
a confirmation that did not occur. The phrase "mixing-rate bounds" was independently checked against
the thesis and found accurate (the thesis's own Section 3, "Lower Bounds on the mix norm," is
exactly this) and was left unchanged.

Also applied, as approved: "scientific-ML models" -> "scientific machine-learning models" in the
hero paragraph (`index.html`).

## Responsive verification

**Widths checked**: 1440px (desktop), 1024px (tablet), 768px (tablet, adjacent to the site's own
~766px CSS breakpoint), 430px (mobile), 390px (mobile).

**Mechanism used**: Chrome DevTools Protocol (`Emulation.setDeviceMetricsOverride` +
`Page.captureScreenshot`), driven directly via a local Python script against headless Chrome
(`Google Chrome.app`) with `--remote-debugging-port` and `--remote-allow-origins=*`. This is genuine
browser responsive emulation (the same mechanism Chrome DevTools' own device toolbar and tools like
Puppeteer/Playwright use), not a real physical device and not the naive `--window-size` CLI flag
used in the previous task (which was diagnosed as unreliable and is not repeated here). Full-page
screenshots were captured and cropped for close inspection of specific regions (CTA row, flagship
card tags/stat rows/figures, sidebar).

**Issues found**: none. All five widths rendered without horizontal overflow, without clipped text,
with correct card/tag/stat wrapping, correct figure scaling, and correct behaviour crossing the
~766px breakpoint (768px width uses the desktop two-column layout with wrapped CTA pills; narrower
widths use the single-column layout with the stacked CTA buttons and the corrected sidebar grid).
This also serves as independent confirmation that the sidebar grid-column fix made in the previous
task was correct and effective.

**Fixes made this pass**: none required -- the previous task's CSS was confirmed correct via this
more reliable method. No new CSS changes were made in this task.

**`.cta-row` decision**: **kept**. Inspected directly via the CDP screenshots at 390px and 430px:
five full-width stacked buttons (Research / Projects / Download CV / GitHub / Contact), clearly
readable, sensibly spaced, no crowding. Meets all three "keep" criteria from the brief. Not reverted.

**Remaining verification limitation**: this is real browser rendering via genuine responsive
emulation, not physical-device testing. No actual phone or tablet was used. I recommend a quick
manual check on an actual phone before treating mobile as unconditionally verified, though I have
materially higher confidence after this pass than after the previous (unreliable) one.

## Pre-push state

- Branch: `main`
- Remote: `origin` -> `https://github.com/adebanjioluwatimileyin/adebanjioluwatimileyin.github.io.git`
- HEAD before push: `08efd68` ("Finalize website content and responsive checks")
- Status: working tree clean, 4 commits ahead of `origin/main` (`79f891e`, `25c456d`, `b4a0e98`,
  `08efd68`)
- `git fetch origin` immediately before push confirmed `origin/main` was still at `c46f6c3` (its
  state at the start of this task) -- no unexpected remote changes, no divergence.

## Push

- Command: `git push origin main`
- First attempt failed: `403` -- the active local `gh`/git credential was `AdebanjiAdelowo` (the
  research-repositories account, set active during the earlier publication task), not
  `adebanjioluwatimileyin` (this site's actual owner). Switched with `gh auth switch --hostname
  github.com --user adebanjioluwatimileyin`, then retried.
- Result: `c46f6c3..08efd68  main -> main` -- succeeded. No force push, no rebase, no history
  rewrite.

## Deployment

- Live URL: `https://adebanjioluwatimileyin.github.io/`
- GitHub Pages build for commit `08efd68` polled via the Pages Builds API: `building` ->
  `built` (confirmed complete before any live verification below).
- Live pages checked (all returned HTTP 200): `/`, `research.html`, `projects.html`,
  `experience.html`, `education.html`, `skills.html`, `contact.html`, `research-outputs.html`,
  `cv.pdf`, `assets/css/site.css`.

## Live assets

- **Figures**: all five new project figures (`images/navier-stokes-2d/...`,
  `images/fem-cylinder-flow/...`, `images/darcy-inverse-problem/...`,
  `images/fem-topology-optimization/...`, `images/lorenz96-data-assimilation/...`) fetched live and
  returned HTTP 200.
- **CV**: fetched `https://adebanjioluwatimileyin.github.io/cv.pdf` live and compared its MD5 hash
  against the finalized `adebanji_cv_master.pdf` -- **identical** (`359221002bc07625a455aab373f80519`).
- **Repository links**: live homepage confirmed to contain all six flagship project anchors
  (`#navier-stokes`, `#cylinder-flow`, `#darcy`, `#boiling`, `#topology-optimization`, `#lorenz96`).
  Live `projects.html` confirmed to contain exactly 6 "Flagship" tier labels and the exact formal
  thesis title verbatim. Spot-checked 6 representative repository links
  (`navier-stokes-2d`, `darcy-inverse-problem`, `lorenz96-data-assimilation`, `Master-Thesis`,
  `boiling-phasefield-3d`, `neural-surrogate-burgers`) directly against `github.com` -- all HTTP 200,
  all under `AdebanjiAdelowo`. GitHub-profile and LinkedIn links on the live homepage confirmed to
  point to `github.com/AdebanjiAdelowo` and `linkedin.com/in/adebanjioluwatimileyin` respectively
  (the site's own domain correctly remains under the `adebanjioluwatimileyin` account, unchanged).
- **Navigation**: internal anchors and page links validated locally before push (see previous
  report and this task's re-run); live page fetches for all 8 pages returned 200, consistent with
  navigation working end to end.

## Live metadata

- Title (live, verified): `Adebanji Adelowo | Applied Mathematician & Scientific ML Researcher` --
  matches exactly.
- Open Graph (live, verified): `og:type=website`, `og:site_name=Adebanji Adelowo`,
  `og:title=Adebanji Adelowo | Applied Mathematician & Scientific ML Researcher`. No new SEO
  framework introduced; existing meta tags only.

## Final status

**DEPLOYED WITH MINOR CAVEAT**

The only caveat is the one disclosed above: responsive verification used genuine browser emulation
via the Chrome DevTools Protocol (a reliable, standard technique), not an actual physical device.
Nothing else is outstanding.
