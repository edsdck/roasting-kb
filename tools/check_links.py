#!/usr/bin/env python3
"""Fallback link checker for docs/ when mkdocs isn't installed. Exit 1 on broken relative links."""
import os, re, sys
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs")
bad = 0
for d, _, fs in os.walk(ROOT):
    for f in fs:
        if not f.endswith(".md") or f.startswith("_"):
            continue
        p = os.path.join(d, f)
        txt = open(p, encoding="utf-8").read()
        txt = re.sub(r"```.*?```", "", txt, flags=re.S)
        for link in re.findall(r"\]\(([^)\s]+)\)", txt):
            if re.match(r"^(https?:|mailto:|#)", link):
                continue
            target = os.path.normpath(os.path.join(d, link.split("#")[0]))
            if not os.path.exists(target) or not target.startswith(ROOT + os.sep):
                # mkdocs only knows files inside docs/, so a link that leaves docs/ is broken too
                print(f"BROKEN {os.path.relpath(p, ROOT)} -> {link}")
                bad += 1
print("ok" if not bad else f"{bad} broken links")
sys.exit(1 if bad else 0)
