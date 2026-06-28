#!/usr/bin/env python3
"""Eksporter ein Notion-database (data source) til CSV - lesetilgang berre.

Arbeidsnavet for AHO-granskinga er Notion-sida «AHO etikkrådet». Dette skriptet
tek eit snapshot av ein strukturert database derifrå slik at funn kan
versjonerast og kryssjekkast mot Lovdata-indeksen i dette repoet.

Autentisering: set miljøvariabelen NOTION_TOKEN (intern integrasjon «aho-etikk»).
  export NOTION_TOKEN=ntn_...
Token skal ALDRI committast - sjå .gitignore / .env.example.

Bruk:
  python3 scripts/notion_export.py <database-id> [ut.csv]

Kjende database-id-ar (sjå docs/notion.md):
  baaf3e0b70b648f5a260c45347a267e6   Funn: regelbrot og løftebrot (AHOs lumskheit)
  bca7224e13a047b894e99ac9497d7830   Etiske retningslinjer (benchmark)

PERSONVERN: ikkje eksporter databasen «personar av interesse» til dette repoet.
Den inneheld personopplysningar og skal bli verande i Notion (tilgangsstyrt).
Dataminimer - eksporter berre kjeldeførte funn/benchmark med ålment formål.
"""

from __future__ import annotations

import csv
import json
import os
import sys
import urllib.request

API = "https://api.notion.com/v1"
VERSION = "2022-06-28"


def _post(path: str, token: str, body: dict) -> dict:
    req = urllib.request.Request(
        API + path,
        data=json.dumps(body).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {token}",
            "Notion-Version": VERSION,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def flatten(prop: dict) -> str:
    """Reduser ein Notion-property til ein lesbar streng."""
    t = prop.get("type")
    v = prop.get(t)
    if v is None:
        return ""
    if t == "title" or t == "rich_text":
        return "".join(x.get("plain_text", "") for x in v)
    if t == "select":
        return v.get("name", "") if v else ""
    if t == "multi_select":
        return "; ".join(o.get("name", "") for o in v)
    if t in ("url", "email", "phone_number"):
        return v or ""
    if t == "number":
        return "" if v is None else str(v)
    if t == "date":
        return (v.get("start", "") or "") + (f"-{v['end']}" if v.get("end") else "")
    if t == "checkbox":
        return "ja" if v else "nei"
    return json.dumps(v, ensure_ascii=False)


def query_all(db_id: str, token: str) -> list[dict]:
    rows, cursor = [], None
    while True:
        body = {"page_size": 100}
        if cursor:
            body["start_cursor"] = cursor
        data = _post(f"/databases/{db_id}/query", token, body)
        rows.extend(data["results"])
        if not data.get("has_more"):
            return rows
        cursor = data["next_cursor"]


def main(argv: list[str]) -> int:
    token = os.environ.get("NOTION_TOKEN")
    if not token:
        print("Set NOTION_TOKEN i miljøet først.", file=sys.stderr)
        return 2
    if len(argv) < 2:
        print(__doc__)
        return 2
    db_id = argv[1].replace("-", "")
    out = argv[2] if len(argv) > 2 else f"data/notion-export/{db_id}.csv"

    results = query_all(db_id, token)
    if not results:
        print("Ingen rader.", file=sys.stderr)
        return 1

    cols: list[str] = []
    for r in results:
        for k in r["properties"]:
            if k not in cols:
                cols.append(k)

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["url"] + cols)
        for r in results:
            props = r["properties"]
            w.writerow([r.get("url", "")] + [flatten(props.get(c, {})) for c in cols])
    print(f"Skreiv {out}: {len(results)} rader, {len(cols)} kolonnar", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
