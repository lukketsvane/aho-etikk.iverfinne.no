# scripts/

Verktøy for å hente og indeksere data. Alle skripta køyrer frå repo-rota og
brukar berre standardbibliotek (Python 3) / `curl` + `bash`.

| Skript | Gjer | Køyr |
| --- | --- | --- |
| `fetch_lovdata.sh` | Lastar ned Lovdata-datasett frå `api.lovdata.no` | `bash scripts/fetch_lovdata.sh --list` |
| `build_index.py` | Byggjer metadata-indeks (CSV/JSONL) frå tarballane | `python3 scripts/build_index.py` |
| `notion_export.py` | Tek snapshot av ein Notion-database til CSV | `python3 scripts/notion_export.py <db-id>` |

## Typisk arbeidsflyt

```bash
# 1. (valfritt) hent ferske data – dei to gjeldande sett ligg alt i data/raw/
bash scripts/fetch_lovdata.sh

# 2. bygg søkbar indeks
python3 scripts/build_index.py
#   -> data/index/lover.csv, forskrifter.csv, lovdata-index.jsonl

# 3. (valfritt) snapshot av kjeldeførte funn frå Notion
export NOTION_TOKEN=ntn_...          # integrasjonen «aho-etikk», sjå .env.example
python3 scripts/notion_export.py baaf3e0b70b648f5a260c45347a267e6 \
        data/notion-export/funn.csv
```

## Personvern og hemmelegheiter

- `NOTION_TOKEN` skal aldri committast. `.env` og `data/notion-export/` er i
  `.gitignore`.
- Ikkje eksporter databasen **«personar av interesse»** til repoet — den
  inneheld personopplysningar og skal bli verande i Notion (tilgangsstyrt).
  Dataminimer: eksporter berre kjeldeførte funn/benchmark med ålment formål.
- Lovdata-data er NLOD 2.0 — krediter «Lovdata» ved vidarebruk.
