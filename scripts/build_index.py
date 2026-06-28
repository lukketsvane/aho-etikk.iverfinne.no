#!/usr/bin/env python3
"""Bygg ein søkbar metadata-indeks over Lovdata-korpuset.

Les dei komprimerte tarballane under data/raw/ (gjeldende-lover.tar.bz2 og
gjeldende-sentrale-forskrifter.tar.bz2) direkte som straum - utan å pakke ut
~270 MB HTML til disk - og hentar ut metadatablokka
``<dl class="data-document-key-info">`` frå kvart dokument.

Skriv:
  data/index/lover.csv          (ei rad per lov)
  data/index/forskrifter.csv    (ei rad per forskrift)
  data/index/lovdata-index.jsonl (alle dokument, eitt JSON-objekt per linje)

Rein standardbibliotek - ingen avhengnader. Køyr frå repo-rota:
  python3 scripts/build_index.py

Kjelde: Lovdata opne data (api.lovdata.no), lisens NLOD 2.0.
"""

from __future__ import annotations

import bz2
import csv
import html
import json
import re
import sys
import tarfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "raw"
OUT = REPO / "data" / "index"

# tarball -> dokumenttype
SOURCES = {
    "gjeldende-lover.tar.bz2": "lov",
    "gjeldende-sentrale-forskrifter.tar.bz2": "forskrift",
}

# dt class="x" -> kolonnenamn i indeksen
FIELDS = {
    "legacyID": "datokode",
    "dokid": "dokid",
    "ministry": "departement",
    "subunit": "etat",
    "publishedIn": "publisert_i",
    "dateInForce": "i_kraft",
    "lastChangeInForce": "siste_endring_i_kraft",
    "lastChangedBy": "sist_endret_ved",
    "legalArea": "rettsomraade",
    "appliesTo": "gjelder_for",
    "titleShort": "korttittel",
    "title": "tittel",
    "lastupdated": "siste_rettelse",
    "refid": "refid",
}

# Rekkjefølgje på kolonnar i CSV/JSONL
COLUMNS = [
    "type", "filename", "dokid", "datokode", "tittel", "korttittel",
    "departement", "etat", "rettsomraade", "i_kraft", "siste_endring_i_kraft",
    "sist_endret_ved", "publisert_i", "gjelder_for", "siste_rettelse",
    "refid", "url",
]

# Hent ut heile <dl class="data-document-key-info"> ... </dl>-blokka
DL_RE = re.compile(
    r'<dl class="data-document-key-info">(.*?)</dl>', re.DOTALL,
)
# Par av <dt class="X">...</dt> <dd class="X"> innhald </dd>
PAIR_RE = re.compile(
    r'<dt class="([^"]+)">.*?</dt>\s*<dd class="\1">(.*?)</dd>', re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def clean(value: str) -> str:
    """Strip HTML-taggar, samanstill whitespace, dekod entitetar."""
    text = TAG_RE.sub(" ", value)
    text = html.unescape(text)
    # Lister (departement, rettsområde, gjelder for) -> separer med "; "
    text = WS_RE.sub(" ", text).strip()
    return text


def parse_document(raw: bytes, filename: str, doctype: str) -> dict:
    text = raw.decode("utf-8", errors="replace")
    record = {c: "" for c in COLUMNS}
    record["type"] = doctype
    record["filename"] = filename

    dl = DL_RE.search(text)
    block = dl.group(1) if dl else text
    for cls, value in PAIR_RE.findall(block):
        col = FIELDS.get(cls)
        if col:
            record[col] = clean(value)

    if record["refid"]:
        record["url"] = "https://lovdata.no/" + record["refid"].lstrip("/")
    return record


def iter_records():
    for fname, doctype in SOURCES.items():
        path = RAW / fname
        if not path.exists():
            print(f"  ! manglar {path} - hopp over "
                  f"(køyr scripts/fetch_lovdata.sh)", file=sys.stderr)
            continue
        print(f"  Les {fname} ...", file=sys.stderr)
        with bz2.open(path, "rb") as fh, tarfile.open(fileobj=fh, mode="r|") as tar:
            count = 0
            for member in tar:
                if not member.isfile() or not member.name.endswith(".xml"):
                    continue
                data = tar.extractfile(member).read()
                yield parse_document(data, Path(member.name).name, doctype)
                count += 1
            print(f"    {count} dokument", file=sys.stderr)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    lover, forskrifter = [], []
    jsonl_path = OUT / "lovdata-index.jsonl"

    with jsonl_path.open("w", encoding="utf-8") as jf:
        for rec in iter_records():
            jf.write(json.dumps(rec, ensure_ascii=False) + "\n")
            (lover if rec["type"] == "lov" else forskrifter).append(rec)

    for rows, name in ((lover, "lover.csv"), (forskrifter, "forskrifter.csv")):
        rows.sort(key=lambda r: r["datokode"])
        with (OUT / name).open("w", encoding="utf-8", newline="") as cf:
            w = csv.DictWriter(cf, fieldnames=COLUMNS)
            w.writeheader()
            w.writerows(rows)
        print(f"  Skreiv {name}: {len(rows)} rader", file=sys.stderr)

    total = len(lover) + len(forskrifter)
    print(f"  Skreiv lovdata-index.jsonl: {total} dokument", file=sys.stderr)
    if total == 0:
        print("Ingen dokument - ligg tarballane i data/raw/?", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
