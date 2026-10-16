# Roasting Knowledge Base

Source for the wiki. Maintained by two agents (see `GATHERER.md`, `BUILDER.md`).

- `docs/` — the published wiki (MkDocs Material → GitHub Pages)
- `registry.csv` — every URL the Gatherer has seen
- `gaps.md` — what the Gatherer should look for next
- `tools/` — `registry.py` (dedupe/status/index), `roastlog.py` (Artisan parser), `check_links.py`
- `roasts/` — Artisan `.alog` files (not published) + cupping notes `<roast>.md`
- `runs/` — Gatherer run logs

Local preview: `pip install -r requirements.txt && mkdocs serve`

## Publishing
Pushing `main` triggers `.github/workflows/deploy.yml`, which builds the site with MkDocs in GitHub
Actions and deploys it to GitHub Pages. The Builder pushes with `tools/push.sh`, using a
fine-grained token in `.github-token` (gitignored, never committed) limited to this repo with
**Contents: read & write** and **Workflows: read & write**.
