# adebanjioluwatimileyin.github.io

Source for my personal website, published via GitHub Pages at
[adebanjioluwatimileyin.github.io](https://adebanjioluwatimileyin.github.io/).

The site presents my work as an applied mathematician and machine learning
researcher, covering PDEs, numerical methods, inverse problems, and
scientific/engineering ML systems.

## Structure

```
adebanjioluwatimileyin.github.io/
├── index.html              Landing page
├── projects.html           Project portfolio
├── research.html           Research interests
├── research-outputs.html   Papers, reports, and thesis writeups
├── experience.html         Professional experience
├── education.html          Education
├── skills.html             Technical skills
├── contact.html            Contact page
├── assets/
│   ├── css/site.css        Site styling
│   └── js/nav.js           Navigation behaviour
└── images/                 Project and profile images, by project
```

No build step: plain HTML, CSS, and JavaScript, served directly by GitHub
Pages.

## Local preview

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000` in a browser.

## License

Site content and code are personal work; not licensed for reuse.
