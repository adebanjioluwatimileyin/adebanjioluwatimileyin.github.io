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

def card(p, featured=False):
    illustration = image(p['image'], 'Research figure: '+p['title']) if featured and p['image'] else ''
    return f'''<article class="project-card{' featured-card' if featured else ''}" id="{p['slug']}">
    {illustration}<div class="card-body"><p class="eyebrow">{escape(p['category'])}</p>
    <h3><a href="./projects/{p['slug']}.html">{escape(p['title'])}</a></h3>
    <p>{escape(p['result'])}</p><a class="section-link" href="./projects/{p['slug']}.html" aria-label="Read case study: {escape(p['title'])}">Read case study →</a></div></article>'''

def home():
    selected=''.join(card(BY_SLUG[s],True) for s in ['navier-stokes','darcy','topology-optimization'])
    return f'''<p class="hero-role">Applied Mathematician &amp; Scientific Machine Learning Researcher</p>
<p class="lede">I develop and verify numerical methods for PDEs, fluid dynamics, and inverse problems, with a focus on reduced-order modelling and scientific machine learning.</p>
<p class="availability">Open to PhD and research opportunities, and ML engineering roles combining mathematical depth with practical software development.</p>
<div class="cta-row hero-actions"><a href="./research.html" class="btn btn-primary">Explore research</a><a href="./cv.pdf" class="btn btn-outline" download>Download CV ↓</a></div>
<section class="home-section" aria-labelledby="selected-work"><div class="section-heading"><h2 id="selected-work">Selected work</h2><a href="./projects.html">All projects →</a></div><div class="featured-grid">{selected}</div></section>
<section class="home-section" aria-labelledby="research-themes"><h2 id="research-themes">Research themes</h2><div class="theme-list">
<div><h3><a href="./research.html#numerical-pdes">Numerical simulation</a></h3><p>Spectral and finite-element methods for flow, transport, and mechanics, checked through convergence studies and reference solutions.</p></div>
<div><h3><a href="./research.html#inverse-problems">Inference &amp; uncertainty</a></h3><p>PDE-constrained inversion, Bayesian inference, optimisation, and ensemble data assimilation.</p></div>
<div><h3><a href="./research.html#reduced-order-sciml">Scientific machine learning</a></h3><p>Reduced models and learned surrogates, with attention to computational cost and generalisation beyond training data.</p></div></div></section>
<section class="home-section" aria-labelledby="industry"><h2 id="industry">From mathematical models to working systems</h2><p>My industry experience spans aviation analytics, predictive modelling, and engineering software. At Intuos Srl, I developed a dashboard serving flight-phase classifiers over recorded telemetry. Its classifier achieved <strong>0.999 weighted F1 in five-fold cross-validation</strong>.</p><p><a href="./projects/intuos.html">Aviation dashboard case study →</a> <span class="link-separator">·</span> <a href="./experience.html">Professional experience →</a></p></section>
<section class="home-section" aria-labelledby="background"><h2 id="background">Background</h2><p>I hold an M.Sc. in Mathematical Engineering from the University of L’Aquila (2021) and a B.Sc. in Mathematics from Obafemi Awolowo University (2018). My Master’s thesis investigated mixing-rate bounds for passive scalars in incompressible flow.</p><p><a href="./research-outputs.html">Thesis &amp; research software →</a> <span class="link-separator">·</span> <a href="./education.html">Education →</a></p></section>
<section class="contact-panel" aria-labelledby="collaboration"><h2 id="collaboration">Let’s discuss research &amp; collaboration</h2><p>I am based in L’Aquila, Italy. Get in touch about research, scientific computing, or applied machine learning.</p><a class="btn btn-primary" href="./contact.html">Get in touch →</a></section>'''

def project_index():
    groups=[('numerical','Numerical simulation'),('inverse','Inference & uncertainty'),('learning','Scientific ML & imaging'),('applied','Applied ML & engineering')]
    sections=[]
    for group,label in groups:
        anchor='applied-projects' if group=='applied' else group
        cards=''.join(card(p) for p in PROJECTS if p['group']==group)
        sections.append(f'<section class="project-group" aria-labelledby="{anchor}"><h2 id="{anchor}">{escape(label)}</h2><div class="project-grid">{cards}</div></section>')
    return '''<p class="lede">Computational studies and engineering systems, with methods, results, evaluation settings, and limitations in each case study.</p>
<nav class="section-nav" aria-label="Project categories"><a href="#numerical">Numerical simulation</a><a href="#inverse">Inference &amp; uncertainty</a><a href="#learning">Scientific ML &amp; imaging</a><a href="#applied-projects">Engineering</a><a href="#additional">More work</a></nav><span id="research-projects" class="anchor-alias"></span>'''+''.join(sections)+(ROOT/'content/additional.html').read_text()

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
<p class="case-result">{escape(p['result'])}</p>
<div class="cta-row"><a class="btn btn-primary" href="{escape(p['code'])}">View source code ↗</a><a class="btn btn-outline" href="./projects.html#{p['slug']}">All projects</a></div>'''
    return prefix+detail+f'<p class="back-link"><a href="./projects.html#{p["slug"]}">← Back to project index</a></p>'

PAGES={
 'index':('Adebanji Adelowo','Applied mathematician and scientific machine learning researcher working on numerical PDEs, inverse problems, and reduced-order models.'),
 'projects':('Projects','Numerical simulation, inverse problems, scientific ML, and engineering case studies with evaluation settings and limitations.'),
 'research':('Research','Research in numerical PDEs, inverse problems, uncertainty quantification, reduced-order modelling, and scientific machine learning.'),
 'experience':('Experience','Professional experience in data science, machine learning, aviation analytics, and engineering software.'),
 'education':('Education','Mathematics and mathematical engineering education, thesis work, academic awards, and mentorship.'),
 'skills':('Skills','Mathematical methods, scientific computing, machine learning, and software engineering skills.'),
 'contact':('Contact','Contact Adebanji Adelowo about research, PhD opportunities, scientific computing, and machine learning roles.'),
 'research-outputs':('Research Outputs','Theses and open-source research software in applied mathematics, numerical simulation, and scientific ML.'),
}

def render(filename,heading,description,content,active='',home_page=False):
    nested='/' in filename
    root='../' if nested else './'
    links=[]
    for slug,label in [('index','Home'),('research','Research'),('projects','Projects'),('experience','Experience'),('cv','CV'),('contact','Contact')]:
        href=root+('cv.pdf' if slug=='cv' else slug+'.html')
        attrs=' aria-current="page"' if active==slug else ''
        if slug=='cv':attrs+=' download'
        links.append(f'<li><a href="{href}"{attrs}>{label}</a></li>')
    # Replace legacy project anchors with direct case-study routes, preserving index anchors externally.
    for slug in BY_SLUG:
        content=content.replace(f'href="./projects.html#{slug}"',f'href="./projects/{slug}.html"') if not nested else content
    if nested:
        content=re.sub(r'(href|src)="\./',r'\1="../',content)
    title='Adebanji Adelowo | Applied Mathematics & Scientific ML' if home_page else heading+' | Adebanji Adelowo'
    before_title=f'<a class="breadcrumb" href="{root}projects.html">← Projects</a>' if nested else ''
    if home_page:
        before_title=image('images/profile/adebanji_profile.jpg','Portrait of Adebanji Adelowo','home-avatar',False)
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
