#!/bin/sh
# Deploy ONLY what is committed (agents may be editing the working tree). Usage: tools/deploy-clean.sh
# After a successful deploy it ALWAYS announces the changed pages to every search + AI engine
# (contentcam-hub/marketing/tools/announce.py --deployed: IndexNow, Bing URLs + sitemap, Google sitemap,
# Brave + Google hand queues). Never deploy another way, or the announce is skipped until the daily catch-up.
set -e
cd "$(dirname "$0")/.."
REV=$(git rev-parse HEAD)
D=$(mktemp -d)
git archive HEAD | tar -x -C "$D"
cp -r .vercel "$D/"
(cd "$D" && vercel --prod --yes)
rm -rf "$D"
echo "Deployed $REV. Announcing to search + AI engines..."
sleep 20   # let the new sitemap.xml go live before reading it
python3 "$HOME/contentcam-hub/marketing/tools/announce.py" --deployed "$REV"
# Fail loudly if the announce didn't record this rev (a silent no-op hid for one deploy on 14 Nov).
grep -q "\"last_rev\": \"$REV\"" "$HOME/contentcam-hub/marketing/announce-state.json" \
  || { echo "ANNOUNCE FAILED: announce-state.json doesn't show $REV. Run announce.py --deployed $REV by hand."; exit 1; }
echo "Announce recorded for $REV."
