#!/usr/bin/env bash
# Last ned Lovdata opne data frå api.lovdata.no/v1/publicData.
#
# Datasett (sjå https://data.norge.no/datasets - "Norsk Lovtidend, Avdeling I"):
#   gjeldende-lover.tar.bz2                 gjeldande lover (committa i data/raw/)
#   gjeldende-sentrale-forskrifter.tar.bz2  gjeldande forskrifter (committa)
#   lovtidend-avd1-2001-2025.tar.bz2        Norsk Lovtidend avd. I 2001-2025 (~69 MB, IKKJE committa)
#   lovtidend-avd1-2026.tar.bz2             Norsk Lovtidend avd. I inneverande år
#
# Lisens: NLOD 2.0 (Norsk lisens for offentlege data). Krediter "Lovdata".
# Ratelimit: ~200 kall/vindauge (sjå X-RateLimit-* i responsen).
#
# Bruk:
#   scripts/fetch_lovdata.sh --list      # vis tilgjengelege filer (tørrkøyring)
#   scripts/fetch_lovdata.sh             # last ned alle fire til data/raw/
#   scripts/fetch_lovdata.sh <fil> ...   # last ned spesifikke filer
set -euo pipefail

API="https://api.lovdata.no/v1/publicData"
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$REPO/data/raw"

ALL=(
  gjeldende-lover.tar.bz2
  gjeldende-sentrale-forskrifter.tar.bz2
  lovtidend-avd1-2001-2025.tar.bz2
  lovtidend-avd1-2026.tar.bz2
)

if [[ "${1:-}" == "--list" ]]; then
  echo "Tilgjengelege datasett frå $API/list:"
  curl -fsSL "$API/list"
  echo
  exit 0
fi

mkdir -p "$DEST"
files=("$@")
[[ ${#files[@]} -eq 0 ]] && files=("${ALL[@]}")

for f in "${files[@]}"; do
  echo "==> $f"
  curl -fL --retry 4 --retry-delay 2 --retry-all-errors \
    -o "$DEST/$f" "$API/get/$f"
  echo "    -> data/raw/$f  ($(du -h "$DEST/$f" | cut -f1))"
done

echo "Ferdig. Bygg indeks på nytt med: python3 scripts/build_index.py"
