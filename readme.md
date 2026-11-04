# Personal website

Source of [wang-zhiping.github.io](https://wang-zhiping.github.io), built with [Jekyll](https://jekyllrb.com/) on GitHub Pages. Every push to `main` is published automatically within a minute or two.

## Where things live

| What | File |
| --- | --- |
| Name, tagline, email, short bio, sidebar buttons | `_config.yml` |
| Sidebar navigation | `_data/nav.yml` |
| Home page (about, news, education, honors, teaching, contact) | `index.md` |
| Research experience | `research.md` |
| Publications | `publications/publication.md` (images live next to it) |
| CV PDFs | `CV/` (update the `CV` link in `_config.yml` and `index.md` when adding a new one) |
| Layout and styles | `_layouts/default.html`, `_includes/sidebar.html`, `_sass/site.scss` |

## Preview locally

With Ruby installed (the faithful way, same build as GitHub Pages):

```bash
bundle install
bundle exec jekyll serve --livereload
```

Without Ruby, a quick layout/CSS preview with Python:

```bash
pip install libsass python-liquid pyyaml markdown
python3 _preview/render.py . _preview/out
python3 -m http.server 4000 --directory _preview/out
```

Then open <http://localhost:4000>.
