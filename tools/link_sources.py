#!/usr/bin/env python3
"""Expand bare source refs like [S0003] into links to the source file, in all docs/ pages
(except docs/sources/). Idempotent: already-linked refs are left alone."""
import glob, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
files = {os.path.basename(p)[:5]: p for p in glob.glob(os.path.join(DOCS, "sources", "S[0-9][0-9][0-9][0-9]-*.md"))}
n = 0
for p in glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True):
    if os.sep + "sources" + os.sep in p or os.path.basename(p).startswith("_"):
        continue
    txt = open(p, encoding="utf-8").read()
    def rep(m):
        global n
        sid = m.group(1)
        if sid not in files:
            return m.group(0)
        n += 1
        return f"[{sid}]({os.path.relpath(files[sid], os.path.dirname(p))})"
    new = re.sub(r"\[(S\d{4})\](?!\()", rep, txt)
    if new != txt:
        open(p, "w", encoding="utf-8").write(new)
print(f"linked {n} refs")
