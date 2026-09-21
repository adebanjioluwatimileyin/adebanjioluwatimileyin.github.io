"""Check public HTML structure, local links, images, metadata, and sitemap."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path=path
        self.ids=[]
        self.refs=[]
        self.images=[]
        self.headings=[]
        self.main=0
        self.canonical=[]
        self.metadata={}
        self.stack=[]
        self.errors=[]
        self.feed(path.read_text())
        if self.stack:self.errors.append('Unclosed elements: '+str(self.stack))

    def handle_starttag(self, tag, attrs):
        attrs=dict(attrs)
        if 'id' in attrs:self.ids.append(attrs['id'])
        for key in ['href','src']:
            if key in attrs:self.refs.append(attrs[key])
        if tag=='img':self.images.append(attrs)
        if tag in ['h1','h2','h3','h4','h5','h6']:self.headings.append(int(tag[1]))
        if tag=='main':self.main+=1
        if tag=='link' and attrs.get('rel')=='canonical':self.canonical.append(attrs.get('href'))
        if tag=='meta':self.metadata[attrs.get('name',attrs.get('property'))]=attrs.get('content')
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}:
            self.stack.append(tag)

    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if self.stack and self.stack[-1]==tag:self.stack.pop()

    def handle_endtag(self,tag):
        if not self.stack or self.stack[-1]!=tag:self.errors.append('Unbalanced closing tag: '+tag)
        else:self.stack.pop()

def check():
    paths=sorted(list(ROOT.glob('*.html'))+list((ROOT/'projects').glob('*.html')))
    pages={path.resolve():Page(path) for path in paths}
    errors=[]
    for path,p in pages.items():
        issues=list(p.errors)
        if p.main!=1:issues.append('Expected one main landmark')
        if p.headings.count(1)!=1:issues.append('Expected one h1')
        for prev,level in zip(p.headings,p.headings[1:]):
            if level>prev+1:issues.append(f'Heading level jumps from h{prev} to h{level}')
        duplicates=[name for name,count in Counter(p.ids).items() if count>1]
        if duplicates:issues.append('Duplicate IDs: '+str(duplicates))
        if len(p.canonical)!=1:issues.append('Expected one canonical URL')
        for field in ['description','og:title','og:description','og:image','twitter:card']:
            if not p.metadata.get(field):issues.append('Missing metadata: '+field)
        for img in p.images:
            if not img.get('alt'):issues.append('Image lacks descriptive alt text')
            if not img.get('width') or not img.get('height'):issues.append('Image lacks intrinsic dimensions: '+img.get('src',''))
        for ref in p.refs:
            url=urlsplit(ref)
            if url.scheme or url.netloc:continue
            target=(path.parent/unquote(url.path)).resolve() if url.path else path
            if not target.exists():issues.append('Missing local target: '+ref)
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:issues.append('Missing anchor: '+ref)
        if '{{' in path.read_text():issues.append('Unrendered template placeholder')
        errors.extend(f'{path.relative_to(ROOT)}: {issue}' for issue in issues)
    sitemap=ET.parse(ROOT/'sitemap.xml')
    urls=[n.text for n in sitemap.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    canonicals=[p.canonical[0] for p in pages.values() if p.canonical]
    if len(set(canonicals))!=len(canonicals):errors.append('Duplicate canonical URLs')
    if set(urls)!=set(canonicals):errors.append('Sitemap does not match public pages')
    if errors:raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(pages)} pages; local links, anchors, HTML nesting, headings, image dimensions, metadata, and sitemap.')

if __name__=='__main__':check()
