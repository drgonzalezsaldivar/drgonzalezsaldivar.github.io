#!/usr/bin/env python3
"""Revisa enlaces internos e imágenes locales. Sale con error si hay rotos.
Entiende URLs sin .html (como las sirve GitHub Pages)."""
import re, sys, glob, os
from urllib.parse import urlparse, unquote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = {"www.drgonzalezsaldivar.com", "drgonzalezsaldivar.com"}
pages = [p for p in glob.glob(ROOT + "/**/*.html", recursive=True)
         if "/assets/" not in p and "/.git/" not in p]

def exists(path):
    c = [path, path + ".html", os.path.join(path, "index.html")]
    return any(os.path.isfile(x) for x in c)

bad = []
for page in pages:
    html = open(page, encoding="utf-8").read()
    html = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    for attr, url in re.findall(r'\b(href|src)="([^"]+)"', html):
        u = urlparse(url)
        if u.scheme in ("mailto", "tel", "javascript", "data", "whatsapp") or url.startswith("#"):
            continue
        if u.scheme in ("http", "https"):
            if u.netloc not in SITE:
                continue
            path = u.path
        else:
            path = u.path
            if not path:
                continue
        path = unquote(path)
        base = ROOT if path.startswith("/") else os.path.dirname(page)
        target = os.path.normpath(os.path.join(base, path.lstrip("/")))
        if path in ("", "/"):
            continue
        if not exists(target):
            bad.append((os.path.relpath(page, ROOT), url))

for p, u in sorted(set(bad)):
    print(f"ROTO  {p}  ->  {u}")
print(f"{len(pages)} páginas revisadas, {len(set(bad))} enlaces rotos")
sys.exit(1 if bad else 0)
