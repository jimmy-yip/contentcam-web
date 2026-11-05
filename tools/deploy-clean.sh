#!/bin/sh
# Deploy ONLY what is committed (agents may be editing the working tree). Usage: tools/deploy-clean.sh
set -e
cd "$(dirname "$0")/.."
D=$(mktemp -d)
git archive HEAD | tar -x -C "$D"
cp -r .vercel "$D/"
(cd "$D" && vercel --prod --yes)
rm -rf "$D"
