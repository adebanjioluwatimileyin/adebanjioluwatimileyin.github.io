#!/usr/bin/env bash
# Mirror adebanjiadelowo.github.io into this repository, keeping this
# site's own hostname in canonical links and metadata.
# Usage: .github/sync-from-main-site.sh <path to a clone of the main site>
set -euo pipefail
src=$1
main_host=adebanjiadelowo.github.io
own_host=adebanjioluwatimileyin.github.io

# Workflow files are not mirrored: GITHUB_TOKEN may not push changes to
# .github/workflows/, so mirroring them would block every sync after a
# workflow edit. Copy workflow changes here by hand when needed; the checks
# below gate every sync either way.
rsync -a --delete \
  --exclude .git \
  --exclude .github/workflows/ \
  --exclude .github/sync-from-main-site.sh \
  --exclude .github/workflows/sync-from-main-site.yml \
  "$src"/ ./

sed -i.bak "s/${main_host//./\\.}/$own_host/g" scripts/build.py templates/base.html robots.txt README.md
sed -i.bak "s/assert \"$own_host\" not in page/assert \"$main_host\" not in page/" .github/workflows/site-checks.yml
find . -name '*.bak' -not -path './.git/*' -delete

python3 scripts/build.py
python3 scripts/build.py --check
python3 scripts/check_site.py
python3 scripts/test_check_links.py
python3 scripts/check_links.py

if grep -l "$main_host" ./*.html projects/*.html sitemap.xml robots.txt; then
  echo "Main-site hostname left in published pages" >&2
  exit 1
fi
grep -q "assert \"$main_host\" not in page" .github/workflows/site-checks.yml
