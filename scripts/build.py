"""Render the static portfolio from shared templates and editable content.

Run `python3 scripts/build.py` after editing content or templates.
Run `python3 scripts/build.py --check` to verify generated files are current.
No third-party dependencies are required. GitHub Pages serves the generated HTML.
"""
from pathlib import Path
from html import escape
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://adebanjioluwatimileyin.github.io/'
PROJECTS = json.loads((ROOT/'content/projects.json').read_text())
BY_SLUG = {p['slug']: p for p in PROJECTS}
SIZES = json.loads((ROOT/'content/image-sizes.json').read_text())
TEMPLATE = (ROOT/'templates/base.html').read_text()

def image(path, alt, cls='', lazy=True):
    dimensions = SIZES.get(path)
    size = f' width="{dimensions[0]}" height="{dimensions[1]}"' if dimensions else ''
    loading = ' loading="lazy"' if lazy else ''
    return f'<img src="./{path}" alt="{escape(alt)}" class="{cls}"{size}{loading} decoding="async">'

def status_line(p):
    badge = p.get('badge')
    label = f'<span class="status-badge status-{badge.lower().replace(" ", "-")}">{escape(badge)}</span>' if badge else ''
    return f'<p class="project-status">{label}{escape(p["status"])}</p>'

def card(p, featured=False):
    illustration = ''
    if featured and p['image']:
        label = {'navier-stokes': 'Full-order vorticity at t = 3', 'darcy': 'Reconstructed log permeability', 'topology-optimization': 'Optimised material layout'}.get(p['slug'], p['image_caption'])
        illustration = f'<div class="card-visual"><div class="thumbnail thumbnail-{p["slug"]}">{image(p["image"], label)}</div><p class="thumbnail-caption">{label}</p></div>'
    elif p['image']:
        illustration = f'<a class="project-preview" href="./projects/{p["slug"]}.html">{image(p["image"], p["image_alt"])}<span>{escape(p["image_caption"])}</span></a>'
    return f'''<article class="project-card{' featured-card' if featured else ''}" id="{p['slug']}" data-group="{p['group']}">
    {illustration}<div class="card-body"><p class="eyebrow">{escape(p['category'])}</p>
    <h3><a href="./projects/{p['slug']}.html">{escape(p['title'])}</a></h3>
    <p class="card-purpose">{escape(p['purpose'])}</p><p>{escape(p.get('summary', p['result']))}</p><a class="section-link" href="./projects/{p['slug']}.html" aria-label="Read case study: {escape(p['title'])}">Read case study →</a></div></article>'''

def order_project_lists(content):
    ranks = {p['slug']: i for i, p in enumerate(PROJECTS)}
    urls = {p['code'].rstrip('/'): p['slug'] for p in PROJECTS}
    def reorder(match):
        items = re.findall(r'<li\b[^>]*>.*?</li>', match.group(2), re.S)
        def priority(item):
            local = re.search(r'href="\./projects/([^"/]+)\.html"', item)
            if local:
                return ranks.get(local.group(1), len(ranks))
            external = re.search(r'href="([^"]+)"', item)
            return ranks.get(urls.get(external.group(1).rstrip('/'), ''), len(ranks)) if external else len(ranks)
        return match.group(1) + '\n' + '\n'.join(sorted(items, key=priority)) + '\n</ul>'
    return re.sub(r'(<ul[^>]*class="[^"]*\bproject-order\b[^"]*"[^>]*>)(.*?)</ul>', reorder, content, flags=re.S)

def visual_gallery(slugs):
    items=[]
    for p in PROJECTS:
        if p['slug'] not in slugs:
            continue
        slug=p['slug']
        items.append(f'<a class="gallery-item" href="./projects/{slug}.html">{image(p["image"], p["image_alt"])}<span>{escape(p["title"])}</span></a>')
    return '<div class="visual-gallery">'+''.join(items)+'</div>'

def home():
    selected=''.join(card(BY_SLUG[s]) for s in ['intuos','photoacoustic','navier-stokes','burgers-rom','lorenz96','mixing'])
    return f'''<p class="hero-role">Applied Mathematician &amp; Machine Learning Engineer</p>
<p class="lede">I build machine-learning applications, data workflows, and numerical models. My industry experience spans aviation analytics, predictive modelling, APIs, and engineering software; my research focuses on scientific machine learning, numerical PDEs, and inverse problems.</p>
<p class="availability">Open to machine learning, data science, software engineering, research, and PhD opportunities.</p>
<div class="cta-row hero-actions"><a href="./projects.html#applied-projects" class="btn btn-primary">ML &amp; software engineering</a><a href="./research.html" class="btn btn-outline">Explore research</a></div>
<p class="hero-secondary"><a href="./experience.html">Professional experience →</a> <a href="./cv.html">View CV →</a></p>
<section class="home-section" aria-labelledby="selected-work"><div class="section-heading"><h2 id="selected-work">Selected work</h2><a href="./projects.html">All projects →</a></div><div class="project-grid">{selected}</div></section>
<section class="home-section" aria-labelledby="engineering-work"><h2 id="engineering-work">ML systems &amp; engineering</h2><div class="theme-list"><div><h3><a href="https://github.com/AdebanjiAdelowo/prediction-api">Prediction API</a></h3><p>FastAPI model serving with PostgreSQL prediction logging, Docker Compose, automated tests, and Terraform deployment configuration.</p></div><div><h3><a href="https://github.com/AdebanjiAdelowo/Vendingmachine">Vending-machine failure prediction</a></h3><p>Predictive modelling and operational analysis of telemetry and transaction logs across roughly 150 machines.</p></div></div></section>
<section class="home-section" aria-labelledby="more-work"><div class="section-heading"><h2 id="more-work">Scientific machine learning</h2><a href="./projects.html#learning">All scientific ML →</a></div><p>Learned surrogates and physics-informed models evaluated against numerical references through controlled experiments.</p><ul class="work-links">
<li><a href="./projects/burgers-rom.html">Reduced models and neural operators for Burgers’ equation →</a></li>
<li><a href="./projects/pinn.html">Physics-informed advection–diffusion: boundary constraints versus global accuracy →</a></li>
<li><a href="./projects/s4d.html">State-space model versus Transformer across context lengths →</a></li>
<li><a href="./projects.html#physicsnemo">NVIDIA PhysicsNeMo studies: neural operators, graph networks and physics-informed training (in progress) →</a></li>
</ul></section>
<section class="home-section" aria-labelledby="research-themes"><h2 id="research-themes">Research themes</h2><div class="theme-list">
<div><h3><a href="./research.html#reduced-order-sciml">Scientific machine learning</a></h3><p>Reduced models and learned surrogates, with attention to computational cost and generalisation beyond training data.</p></div><div><h3><a href="./research.html#inverse-problems">Inference &amp; uncertainty</a></h3><p>PDE-constrained inversion, Bayesian inference, optimisation, and ensemble data assimilation.</p></div><div><h3><a href="./research.html#numerical-pdes">Numerical simulation</a></h3><p>Spectral and finite-element methods for flow, transport, and mechanics, checked through convergence studies and reference solutions.</p></div></div></section>
<section class="home-section" aria-labelledby="industry"><h2 id="industry">From mathematical models to working systems</h2><a class="industry-visual" href="./projects/intuos.html">{image(BY_SLUG['intuos']['image'], BY_SLUG['intuos']['image_alt'])}<span>Aviation analytics architecture · explore the case study →</span></a><p>My industry experience spans aviation analytics, predictive modelling, and engineering software. At Intuos Srl, I developed a dashboard serving flight-phase classifiers over recorded telemetry. The system combines a FastAPI and IBM DB2 backend, a React frontend, Docker packaging, and deterministic safety alarms. My Intuos work also includes audio-based engine monitoring using Raspberry Pi and ESP32.</p><p><a href="./projects/intuos.html">Aviation dashboard case study →</a> <span class="link-separator">·</span> <a href="./experience.html">Professional experience →</a></p></section>
<section class="home-section" aria-labelledby="background"><h2 id="background">Background</h2><p>I hold an M.Sc. in Mathematical Engineering from the University of L’Aquila (2021) and a B.Sc. in Mathematics from Obafemi Awolowo University (2018). My Master’s thesis investigated mixing-rate bounds for passive scalars in incompressible flow.</p><p><a href="./research-outputs.html">Thesis &amp; research software →</a> <span class="link-separator">·</span> <a href="./education.html">Education →</a></p></section>
<section class="contact-panel" aria-labelledby="collaboration"><h2 id="collaboration">Let’s discuss research &amp; collaboration</h2><p>I am based in L’Aquila, Italy. Get in touch about research, scientific computing, or applied machine learning.</p><a class="btn btn-primary" href="./contact.html">Get in touch →</a></section>'''

def project_index():
    # PROJECTS puts stronger demonstrated evidence and fewer unresolved
    # validation gaps first. Categories filter without reordering it.
    cards=''.join(card(p) for p in PROJECTS)
    return '''<p class="lede">Machine-learning applications, engineering systems, and computational research, with source code, methods, and evaluation in each case study.</p>
<p class="status-key">Featured projects below demonstrate implemented systems and evaluated computational studies. Ongoing PhysicsNeMo research is listed separately.</p>
<nav class="section-nav project-filters" aria-label="Filter projects by field"><a href="#all-projects" data-filter="all">All projects</a><a href="#numerical" data-filter="numerical">Numerical simulation</a><a href="#inverse" data-filter="inverse">Inference &amp; uncertainty</a><a href="#learning" data-filter="learning">Scientific ML &amp; imaging</a><a href="#applied-projects" data-filter="applied">Engineering</a><a href="#physicsnemo">PhysicsNeMo studies</a><a href="#additional">More work</a></nav>
<span id="research-projects" class="anchor-alias"></span><span id="numerical" class="anchor-alias"></span><span id="inverse" class="anchor-alias"></span><span id="learning" class="anchor-alias"></span><span id="applied-projects" class="anchor-alias"></span>
<section class="project-group" aria-labelledby="all-projects"><h2 id="all-projects">Project portfolio</h2><p class="project-count" role="status" aria-live="polite">'''+str(len(PROJECTS))+''' projects</p><div class="project-grid">'''+cards+'</div></section>'+(ROOT/'content/physicsnemo.html').read_text()+(ROOT/'content/additional.html').read_text()+'<script src="./assets/js/projects.js" defer></script>'

def case_study(p):
    detail=(ROOT/f"content/projects/{p['slug']}.html").read_text()
    # Supply dimensions and a direct full-resolution view for existing figures.
    def figure(match):
        attrs=match.group(1)
        src=re.search(r'src="([^"]+)"',attrs).group(1)
        local=src.removeprefix('./')
        if local in SIZES:
            w,h=SIZES[local]
            attrs+=f' width="{w}" height="{h}"'
        else:
            attrs+=' class="external-figure"'
        attrs+=' decoding="async"'
        return f'<a class="figure-link" href="{src}" aria-label="Open figure at full resolution"><img {attrs}></a>'
    detail=re.sub(r'<img\s+([^>]*?)/?>',figure,detail)
    detail=detail.replace('</figcaption>',' <span class="figure-hint">Select figure to enlarge.</span></figcaption>')
    prefix=f'''<p class="eyebrow case-category">{escape(p['category'])}</p>
<div class="contribution"><h2>My contribution</h2><p>{escape(p['contribution'])}</p></div>
{status_line(p)}
<p class="case-result">{escape(p['result'])}</p>
<div class="cta-row"><a class="btn btn-primary" href="{escape(p['code'])}">View source code ↗</a><a class="btn btn-outline" href="./projects.html#{p['slug']}">All projects</a></div>'''
    return prefix+detail+f'<p class="back-link"><a href="./projects.html#{p["slug"]}">← Back to project index</a></p>'

PAGES={
 'index':('Adebanji Adelowo','Machine learning engineer and applied mathematician building data systems, ML applications, and scientific computing software.'),
 'cv':('CV','Download my industry CV for machine learning, data science, and engineering roles.'),
 'projects':('Projects','Numerical simulation, inverse problems, scientific ML, and engineering case studies with evaluation settings and limitations.'),
 'research':('Research','Research in numerical PDEs, inverse problems, uncertainty quantification, reduced-order modelling, and scientific machine learning.'),
 'experience':('Experience','Professional experience in data science, machine learning, aviation analytics, and engineering software.'),
 'education':('Education','Mathematics and mathematical engineering education, thesis work, academic awards, and mentorship.'),
 'skills':('Skills','Mathematical methods, scientific computing, machine learning, and software engineering skills.'),
 'contact':('Contact','Contact Adebanji Adelowo about research, PhD opportunities, scientific computing, and machine learning roles.'),
 'research-outputs':('Research Outputs','Theses and open-source research software in applied mathematics, numerical simulation, and scientific ML.'),
}

def render(filename,heading,description,content,active='',home_page=False):
    content=order_project_lists(content)
    nested='/' in filename
    root='../' if nested else './'
    links=[]
    for slug,label in [('index','Home'),('research','Research'),('projects','Projects'),('experience','Experience'),('cv','CV'),('contact','Contact')]:
        href=root+(slug+'.html')
        attrs=' aria-current="page"' if active==slug else ''
        links.append(f'<li><a href="{href}"{attrs}>{label}</a></li>')
    # Replace legacy project anchors with direct case-study routes, preserving index anchors externally.
    for slug in BY_SLUG:
        content=content.replace(f'href="./projects.html#{slug}"',f'href="./projects/{slug}.html"') if not nested else content
    if nested:
        content=re.sub(r'(href|src)="\./',r'\1="../',content)
    title='Adebanji Adelowo | Machine Learning & Applied Mathematics' if home_page else heading+' | Adebanji Adelowo'
    before_title=f'<a class="breadcrumb" href="{root}projects.html">← Projects</a>' if nested else ''
    if home_page:
        before_title=''
        aliases={'selected-work':['research-projects-h'], 'research-themes':['areas-h','interests-h'], 'industry':['applied-projects-h'], 'background':['about-h','profile-h'], 'collaboration':['contact-h']}
        for target,old_ids in aliases.items():
            marker=''.join(f'<span id="{old}" class="anchor-alias"></span>' for old in old_ids)
            content=re.sub(r'(<section[^>]+aria-labelledby="'+target+r'">)',lambda m: marker+m.group(1),content)
    values=dict(title=escape(title),description=escape(description),canonical=BASE+('' if home_page else filename),root=root,navigation=''.join(links),body_class='home' if home_page else ('case-study' if nested else ''),heading=escape(heading),before_title=before_title,content=content)
    result=TEMPLATE
    for key,value in values.items():result=result.replace('{{'+key+'}}',value)
    return "\n".join(line.rstrip() for line in result.splitlines())+"\n"

def outputs():
    result={}
    for slug,(heading,description) in PAGES.items():
        content=home() if slug=='index' else project_index() if slug=='projects' else (ROOT/f'content/{slug}.html').read_text()
        result[slug+'.html']=render(slug+'.html',heading,description,content,slug,slug=='index')
    for p in PROJECTS:
        name='projects/'+p['slug']+'.html'
        result[name]=render(name,p['title'],p['result'],case_study(p),'projects')
    urls=[BASE+('' if name=='index.html' else name) for name in result]
    result['sitemap.xml']='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{url}</loc></url>\n' for url in urls)+'</urlset>\n'
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    stale=[]
    rendered=outputs()
    for filename,text in rendered.items():
        path=ROOT/filename
        if args.check:
            if not path.exists() or path.read_text()!=text:stale.append(filename)
        else:
            path.parent.mkdir(parents=True,exist_ok=True)
            path.write_text(text)
    if stale:raise SystemExit('Generated files are stale: '+', '.join(stale))
    print(('Checked' if args.check else 'Rendered')+f' {len(rendered)-1} HTML pages and sitemap.')
