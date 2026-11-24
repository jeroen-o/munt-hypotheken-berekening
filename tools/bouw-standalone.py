#!/usr/bin/env python3
"""Bouwt munt-hypotheekberekening-standalone.html: index.html met alle assets/… als data-URI ingebakken.
Gebruik (vanuit de repo-map):  python3 tools/bouw-standalone.py
"""
import base64, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".svg": "image/svg+xml",
        ".webp": "image/webp", ".woff2": "font/woff2"}

html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

def data_uri(pad):
    vol = os.path.join(ROOT, pad)
    ext = os.path.splitext(pad)[1].lower()
    with open(vol, "rb") as f:
        return f"data:{MIME[ext]};base64," + base64.b64encode(f.read()).decode()

paden = sorted(set(re.findall(r'assets/[A-Za-z0-9_./-]+\.(?:png|jpe?g|svg|webp|woff2)', html)))
for p in paden:
    html = html.replace(p, data_uri(p))

rest = re.findall(r'assets/[A-Za-z0-9_./-]+', html)
if rest:
    sys.exit(f"Niet-ingebakken verwijzingen: {rest}")

uit = os.path.join(ROOT, "munt-hypotheekberekening-standalone.html")
open(uit, "w", encoding="utf-8").write(html)
print(f"{len(paden)} bestanden ingebakken -> {uit} ({len(html)/1024/1024:.2f} MB)")
