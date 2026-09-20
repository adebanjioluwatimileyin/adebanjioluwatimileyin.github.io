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

## Claims NOT changed (verified already accurate, no action needed)

`boiling-phasefield-3d`'s existing Problem/Approach/Validation copy, all of
`neural-surrogate-burgers`'s and `photoacoustic-reconstruction`'s existing figures and stat rows,
`diff-pbr`, `nerf-tensorf`, `pinn-advection-diffusion`, `abdominal-ct-segmentation`, and the entire
Experience page and Applied ML/Engineering project entries were re-read in full during this audit
and found to already match their respective authoritative sources exactly; none were altered.
