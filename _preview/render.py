"""Quick local preview without Ruby/Jekyll (layout and CSS check only).

GitHub Pages builds the real site with Jekyll; this script only mimics it closely
enough to check the design. Requires: pip install libsass python-liquid pyyaml markdown

Usage (from the repository root):
    python3 _preview/render.py . _preview/out
    python3 -m http.server 4000 --directory _preview/out
Then open http://localhost:4000
"""
import re, shutil, sys, datetime, pathlib
import yaml, sass, markdown
from liquid import Environment, FileSystemLoader

repo = pathlib.Path(sys.argv[1]).resolve()
out = pathlib.Path(sys.argv[2]).resolve()
if out.exists():
    shutil.rmtree(out)
out.mkdir(parents=True)

site = yaml.safe_load((repo / "_config.yml").read_text())
site["data"] = {"nav": yaml.safe_load((repo / "_data/nav.yml").read_text())}
site["time"] = datetime.datetime.now()
site["github"] = {}

def quote_includes(text):
    return re.sub(r"{%\s*include\s+([^\s'\"%]+)\s*%}", r'{% include "\1" %}', text)

inc_dir = out.parent / "preview-includes"
if inc_dir.exists():
    shutil.rmtree(inc_dir)
inc_dir.mkdir()
for p in (repo / "_includes").glob("*.html"):
    (inc_dir / p.name).write_text(quote_includes(p.read_text()))
env = Environment(loader=FileSystemLoader(str(inc_dir)))

def relative_url(v):
    return v
env.add_filter("relative_url", relative_url)

def absolute_url(v):
    return site["url"] + v
env.add_filter("absolute_url", absolute_url)

def date_filter(v, fmt):
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.strftime(fmt)
    return str(v)
env.add_filter("date", date_filter)

def front_matter(text):
    m = re.match(r"^---\n(.*?)---\n(.*)$", text, re.S)
    if not m:
        return {}, text
    return (yaml.safe_load(m.group(1)) or {}), m.group(2)

# CSS
_, scss = front_matter((repo / "assets/css/style.scss").read_text())
css = sass.compile(string=scss, include_paths=[str(repo / "_sass")], output_style="expanded")
(out / "assets/css").mkdir(parents=True)
(out / "assets/css/style.css").write_text(css)

# static assets
for d in ["assets/img", "assets/fonts", "assets/video", "CV", "publications", "hiking&photos"]:
    src = repo / d
    for p in src.rglob("*"):
        if p.is_file() and p.suffix.lower() not in (".md", ".scss"):
            dest = out / p.relative_to(repo)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dest)

layout_src = (repo / "_layouts/default.html").read_text()
layout_src = quote_includes(layout_src).replace("{% seo %}", "<title>{{ page.title }} | {{ site.title }}</title>")
layout = env.from_string(layout_src)

md = markdown.Markdown(extensions=["extra", "attr_list", "sane_lists"])

pages = ["index.md", "research.md", "publications/publication.md", "hiking&photos/readme2.md", "404.md"]
for rel in pages:
    fm, body = front_matter((repo / rel).read_text())
    md.reset()
    html = md.convert(body)
    url = "/" + rel.replace("index.md", "").replace(".md", ".html")
    page = dict(fm)
    page["url"] = url
    rendered = layout.render(site=site, page=page, content=html)
    dest = out / rel.replace(".md", ".html")
    if rel == "index.md":
        dest = out / "index.html"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(rendered)
    print("rendered", dest.relative_to(out))
