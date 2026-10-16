#!/usr/bin/env bash
# Push main to GitHub using a repo-scoped token stored in .github-token (gitignored).
# The token is passed as a one-off HTTP header: never written to .git/config or printed.
set -euo pipefail
cd "$(dirname "$0")/.."
TOKEN_FILE=".github-token"
if ! git check-ignore -q "$TOKEN_FILE"; then echo "ERROR: $TOKEN_FILE is not gitignored; refusing to push."; exit 1; fi
if [ ! -s "$TOKEN_FILE" ]; then echo "NO TOKEN: create $TOKEN_FILE (see README) — skipping push."; exit 2; fi
if ! git remote get-url origin >/dev/null 2>&1; then echo "NO REMOTE: run 'git remote add origin https://github.com/<user>/<repo>.git' — skipping push."; exit 2; fi
TOKEN="$(tr -d '[:space:]' < "$TOKEN_FILE")"
AUTH="$(printf 'x-access-token:%s' "$TOKEN" | base64 | tr -d '\n')"
if git -c credential.helper= -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $AUTH" push origin main 2>&1 | sed "s/$TOKEN/***/g"; then
  echo "Pushed. GitHub Actions will build and publish the site."
else
  echo "PUSH FAILED (token expired, wrong repo, or missing permissions)."; exit 1
fi
