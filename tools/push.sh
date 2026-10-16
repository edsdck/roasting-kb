#!/usr/bin/env bash
# Push main to GitHub using the repo-scoped token in local.settings.json ("githubPat"; gitignored).
# The token is passed as a one-off HTTP header: never written to .git/config or printed.
set -euo pipefail
cd "$(dirname "$0")/.."
TOKEN_FILE="local.settings.json"
if ! git check-ignore -q "$TOKEN_FILE"; then echo "ERROR: $TOKEN_FILE is not gitignored; refusing to push."; exit 1; fi
TOKEN="$(python3 -c 'import json,sys;print(json.load(open(sys.argv[1])).get("githubPat","").strip())' "$TOKEN_FILE" 2>/dev/null || true)"
if [ -z "$TOKEN" ]; then echo "NO TOKEN: add {\"githubPat\": \"...\"} to $TOKEN_FILE (see README) — skipping push."; exit 2; fi
if ! git remote get-url origin >/dev/null 2>&1; then echo "NO REMOTE: run 'git remote add origin https://github.com/<user>/<repo>.git' — skipping push."; exit 2; fi
AUTH="$(printf 'x-access-token:%s' "$TOKEN" | base64 | tr -d '\n')"
if git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $AUTH" push origin main 2>&1 | sed "s/$TOKEN/***/g"; then
  echo "Pushed. GitHub Actions will build and publish the site."
else
  echo "PUSH FAILED (token expired, wrong repo, or missing permissions)."; exit 1
fi
