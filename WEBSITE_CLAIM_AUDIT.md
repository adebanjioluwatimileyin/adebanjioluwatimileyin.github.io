# Website Claim Audit

Every quantitative research claim newly added to the website is traced to the authoritative
Selected Projects source. No number was independently derived; all were copied from, or are a
direct restatement of, the audited source.

| Website claim | Project | Authoritative Selected Projects source | Verified |
|---|---|---|---|
| 38.5x online speed-up at <0.1% state error, rank 16 | navier-stokes-2d | `Adebanji_Adelowo_Selected_Projects_LaTeX.tex`, navier-stokes-2d entry, Results field | Yes |
| ~99% error on unseen flow realisation, all ranks | navier-stokes-2d | Same entry, Results/Limitations fields | Yes |
| O(h^3) velocity-L2 / O(h^2) velocity-H1 and pressure-L2 convergence | fem-cylinder-flow | fem-cylinder-flow entry, Verification field | Yes |
| 3/4 2D-1/2D-2 quantities inside reference interval; -0.19%/-0.64% near-misses | fem-cylinder-flow | Same entry, Results/Limitations fields | Yes |
| 0.59% sampler validation error (linear-Gaussian case) | darcy-inverse-problem | darcy-inverse-problem entry, Verification field | Yes |
| 0.849 structured-truth relative error (H1 regularisation mismatch) | darcy-inverse-problem | Same entry, Limitations field | Yes |
| 617.86 -> 101.39 canonical-cantilever compliance | fem-topology-optimization | fem-topology-optimization entry, Results field (source states 617.855262 -> 101.391807; website rounds to 2 d.p., matching the CV/brief convention) | Yes |
| ~14% compliance gap between two finest meshes (not mesh-converged) | fem-topology-optimization | Same entry, Limitations field | Yes |
| >11x RMSE reduction from Gaspari-Cohn localisation | lorenz96-data-assimilation | lorenz96-data-assimilation entry, Results field | Yes |
| Largest Lyapunov exponent lambda_1 ~ 1.69 | lorenz96-data-assimilation | Same entry, Verification field | Yes |
| Conservative Allen-Cahn/NS/energy phase-field solver; 2D bubble-growth 2nd-order convergence; Stefan-problem failure; 3D not yet validated | boiling-phasefield-3d | boiling-phasefield-3d entry (unchanged content, only reordered on the page) | Yes (pre-existing, not re-derived) |
| Formal M.Sc. thesis title, supervisor, final grade | Master-Thesis / Education | Master CV `MASTER_CV_FINAL_CONSISTENCY_REPORT.md` / verified directly against the submitted thesis PDF title page | Yes |
| M.Sc. 106/110, B.Sc. First Class Honours | Education page | Master CV (`adebanji_cv_master.tex`), itself verified against multiple authoritative application CVs | Yes |
| POD-ROM/DEIM/FNO Burgers comparison numbers (0.152%, 1.7%/3.1%, 23.4%, ~2x speed-up) | neural-surrogate-burgers | Unchanged from the pre-existing site content; not modified this pass | Yes (pre-existing) |
| Photoacoustic PSNR/SSIM numbers (+11.8 dB, +10.6 dB, 0.936 vs 0.188) | photoacoustic-reconstruction | Unchanged from the pre-existing site content; not modified this pass | Yes (pre-existing) |
| diff-pbr, nerf-tensorf, pinn-advection-diffusion, abdominal-ct-segmentation figures | (respective projects) | Unchanged from the pre-existing site content; not modified this pass | Yes (pre-existing) |
| INTUOS dashboard F1=0.999; LLM portfolio 96.9%/88M | Applied ML/Engineering section | Unchanged from the pre-existing site content; not modified this pass | Yes (pre-existing) |

## Stale claims found and corrected

- **M.Sc. thesis title**, previously shown on the homepage, Education page, and Research page as
  "Lower Bounds on the Mix Norm of Passive Scalars Advected by Incompressible
  Enstrophy-Constrained Flows" (a paraphrase, not the formal title) -- corrected everywhere to
  either link to the Research Outputs page (which now states the exact formal title in quotes) or,
  on `research-outputs.html` and `projects.html#mixing` directly, to state the formal title
  verbatim alongside the existing descriptive project heading.
- **Thesis-work terminology** (`index.html` About paragraph, `education.html` thesis line): "derived
  and numerically validated ... mixing-rate bounds" corrected to "derived and numerically
  investigated ... mixing-rate bounds." Reviewed the thesis's own Numerical Discussion section
  directly (`thesis1.tex`): the cited theorem (Iyer-Kiselev-Xu 2014, Theorem 1.1) predicts the
  fitted exponential decay rate should scale as $b^{-1}$ with the initial-data support size $b$; the
  thesis's own numerical fit gives $b^{-1.78}$, which the thesis itself describes as a deviation from
  the prediction ("consistent with the known gap between the greedy LTD strategy and the global
  optimum ... higher resolution would be needed to access the true asymptotic regime"). Since the
  numerical work did not confirm quantitative agreement with the theoretical bound, "validated" was
  not an accurate term under this project's own verification/validation taxonomy (validation implies
  confirmed agreement with independent reference evidence); "investigated" -- numerical exploration
  of the theorem's predicted behaviour, honestly reporting the resulting discrepancy -- is accurate.
  "Mixing-rate bounds" itself was checked against the thesis and found accurate (the thesis's own
  Section 3, "Lower Bounds on the mix norm," proves/cites exactly this) and was not changed.
- **Missing M.Sc. grade (106/110)** and **missing supervisor (Prof. Stefano Spirito)** -- added to
  `index.html` (About section), `education.html`, and `research-outputs.html`.
- **Missing B.Sc. "First Class Honours"** -- added to `index.html` and `education.html`
  (`education.html` previously omitted classification entirely).
- **Five newly published repositories entirely absent** from Projects, Research, and Research
  Outputs pages -- added throughout (see `WEBSITE_OVERHAUL_REPORT.md` for the full list of pages
  touched).
- **Identity/positioning language**: sidebar tagline and hero role across all 8 pages read "Applied
  Mathematician · Machine Learning Researcher" (missing "Scientific"); corrected to "Applied
  Mathematician · Scientific Machine Learning Researcher" to match the finalized master CV exactly.
- **`cv.pdf`** (the site's only downloadable CV link, referenced from every page's nav/sidebar/hero)
  was a distinct, older "industry" CV variant (confirmed by content hash: did not match the
  finalized master CV). Replaced with the finalized `adebanji_cv_master.pdf` byte-for-byte (hash
  verified identical after copy). `industry_cv.pdf` and `adebanji_academic_cv.pdf` also exist in
  the repository but are not linked from any page and were left untouched.

## Industry-facing refinement pass (2026-09-20, second pass)

| Website claim | Project | Authoritative source | Type | Notes |
|---|---|---|---|---|
| "Full-stack aviation analytics platform integrating ML flight-phase classification, IBM DB2 telemetry, FastAPI services, and a React/Vite frontend, deployed via Docker for operational flight-performance analysis." (new homepage card, `#intuos`) | intuos-fdm-dashboard | `projects.html`'s own existing `#intuos` article (System field: "A full-stack platform (FastAPI + IBM DB2 backend, React/Vite frontend, Dockerised deployment)...") | Application result | Homepage-only addition; no new claim, condensed from the already-verified `projects.html` entry. Not present in Selected Projects (this repository is in the "Additional Applied ML & Engineering" tier there, not a Selected-Projects flagship entry) -- traced instead to the website's own already-audited `projects.html` content, which is itself traced to the repository. |
| "F1 = 0.999 (flight-phase classifier)" (new homepage stat) | intuos-fdm-dashboard | Same `#intuos` article ("5-fold cross-validated weighted F1 = 0.999 on the flight-phase classifier, trained on 278,571 real DB2 rows") | Application result | Same source as above; number unchanged, not re-derived. |
| "0.59% linear-Gaussian validation error" (homepage Darcy card, was "0.59% sampler validation error") | darcy-inverse-problem | `Adebanji_Adelowo_Selected_Projects_LaTeX.tex`, darcy-inverse-problem entry, Verification field: "the pCN sampler independently validated against an analytically tractable linear-Gaussian problem (0.59% posterior-mean error vs. the analytical result...)" | Validation (independent reference: the closed-form linear-Gaussian posterior) | Wording clarified, not re-derived: the previous homepage phrasing risked being read as the nonlinear PDE inverse problem's own reconstruction accuracy. The clarified wording makes explicit that 0.59% is the sampler-validation figure from the linear-Gaussian test case, not a reconstruction-error claim about the Darcy PDE posterior. `projects.html`'s own stat label already said "(Linear-Gaussian)"; the homepage now matches. |
| "extending a validated 2D prototype toward 3D" (homepage + research.html phase-field cards) | boiling-phasefield-3d | Same document, boiling-phasefield-3d entry, Status field: "Validated: the 2D bubble-growth benchmark (prescribed vaporisation rate) matches the analytical growth rate with demonstrated second-order convergence... Exploratory: the 3D solver is implemented but has not yet been run or validated." | Validation (2D only) | **Checked, not changed.** The authoritative Selected Projects entry itself uses "Validated" for the 2D bubble-growth benchmark. The homepage sentence already correctly scopes "validated" to the 2D prototype only and does not extend that claim to the 3D work (which is described only as something being "extended toward," never itself called validated) -- matching the source exactly. |

## Claims NOT changed (verified already accurate, no action needed)

`boiling-phasefield-3d`'s existing Problem/Approach/Validation copy, all of
`neural-surrogate-burgers`'s and `photoacoustic-reconstruction`'s existing figures and stat rows,
`diff-pbr`, `nerf-tensorf`, `pinn-advection-diffusion`, `abdominal-ct-segmentation`, and the entire
Experience page and Applied ML/Engineering project entries were re-read in full during this audit
and found to already match their respective authoritative sources exactly; none were altered.

## Update 2026-09-21: liver project synchronised with the repository audit

The statement above that the `abdominal-ct-segmentation` entry and figure were unchanged is superseded.

- The liver card now reads "0.9886 Dice on the 26-volume 128³ centre-cropped validation split used for model
  selection" and has a short Limitations facet: not an independent or full-volume test result, no boundary-distance
  metric reported, a leakage-controlled full-volume evaluation pipeline implemented but not yet run on a newly
  trained model.
- The learning-curve figure was regenerated from the project's own `metrics.csv` without its Validation HD95
  panel. The previous figure plotted the invalid historical HD95 on a "(mm)" axis.
- `industry_cv.pdf` and `adebanji_academic_cv.pdf` were removed because they are superseded website artifacts.
  Evidence: neither has been linked since the download link moved to another file (`industry_cv.pdf` on 2026-06-03,
  `adebanji_academic_cv.pdf` on 2026-08-30) and both were replaced by `cv.pdf`, which continued through the 2026-09-16
  and 2026-09-20 updates; neither was edited after 2026-07-31; no page, sitemap or workspace document references
  them; no maintained source exists (they match no version in the workspace CV history, and the only trace of their
  origin is a stale `~/Documents/CVs/` path in an unrelated tool's config); and their content is stale (B.Sc. dates
  shown as 2014 - 2018, corrected in the authoritative CV records on 2026-09-08, and an older headline). Incidentally,
  both also contain an invalid numerical HD95 claim. The linked `cv.pdf` has no liver entry.
