# aho-etikk.iverfinne.no

Kjeldekritisk, gravejournalistisk dokumentasjon av etiske og juridiske
**tillitsbrot** og **løftebrot** ved **Arkitektur- og designhøgskolen i Oslo
(AHO)** - bygd på primærkjelder, norsk lovverk og opne data.

> **Hypotese (ikkje konklusjon):** ein designskule må ha eit «nei». AHO lærer
> studentane å be om å sjå overvakingssystem, men ikkje å seie nei til dei; eit
> lovpålagt etikk-læringsutbyte står i studieplanen, men vert aldri prøvd.
> Dette skal **provast eller avkreftast** med kjelder. Sjå
> [`docs/aho-sak/`](docs/aho-sak/).

## 🧭 Arbeidsnav: Notion

Den løpande granskinga blir driven i **Notion** - sida **«AHO etikkrådet»**:
<https://app.notion.com/p/tingogtang/AHO-etikkr-det-38d1c6815f7880e5bad8ef59b1f76595>

Notion held levande notatar, brevutkast og databasar (funn, etikk-benchmark,
personar av interesse). **Dette git-repoet er data- og metodelaget** som Notion
hentar grunnlag frå og kan ta snapshot inn i. Integrasjon: `aho-etikk`
(`NOTION_TOKEN`). Skjema og synk: [`docs/notion.md`](docs/notion.md).

## Innhald

| Mappe | Innhald |
| --- | --- |
| [`data/raw/`](data/raw/) | Lovdata-korpus: 788 gjeldande lover + 3 487 forskrifter (.tar.bz2, NLOD 2.0) |
| [`data/index/`](data/index/) | Søkbar metadata-indeks: `lover.csv`, `forskrifter.csv`, `lovdata-index.jsonl` ([SCHEMA](data/index/SCHEMA.md)) |
| [`scripts/`](scripts/) | `fetch_lovdata.sh`, `build_index.py`, `notion_export.py` |
| [`docs/`](docs/) | [Rolle](docs/research-agent.md) · [Metode](docs/metodikk.md) · [Kjelderegister](docs/kjelderegister.md) · [Lovdata-datasett](docs/lovdata-datasett.md) · [Søkelogg](docs/sokelogg.md) · [Notion](docs/notion.md) |
| [`docs/aho-sak/`](docs/aho-sak/) | Dossier: [påstandar](docs/aho-sak/paastandar.md) · [funn](docs/aho-sak/funn.md) · [tidslinje](docs/aho-sak/tidslinje.md) · [etikk-benchmark](docs/aho-sak/etikk-benchmark.md) · [AHO-kjelder](docs/aho-sak/kjelder-aho.md) · [brev til Killi](docs/aho-sak/kjelder/brev-killi/) |
| [`maler/`](maler/) | Innsynskrav (offentleglova, eInnsyn) + e-post til arkiv |
| [`docs/tekstar/`](docs/tekstar/) | Kontekst-/essaytekstar (t.d. *stirps / ONEIDA*) |

## Hurtigstart

```bash
# Bygg den søkbare Lovdata-indeksen frå tarballane i data/raw/
python3 scripts/build_index.py

# (valfritt) hent ferske data + Norsk Lovtidend avd. I
bash scripts/fetch_lovdata.sh --list
bash scripts/fetch_lovdata.sh

# (valfritt) snapshot av kjeldeførte funn frå Notion
cp .env.example .env   # fyll inn NOTION_TOKEN
export $(grep -v '^#' .env | xargs)
python3 scripts/notion_export.py baaf3e0b70b648f5a260c45347a267e6 data/notion-export/funn.csv
```

## Datakjelder

- **Lovdata opne data** (`api.lovdata.no`) - lover, forskrifter, Norsk Lovtidend
  avd. I. Lisens **NLOD 2.0**, krediter «Lovdata». Datasett:
  [data.norge.no → Norsk Lovtidend, Avdeling I](https://data.norge.no/nb/datasets/c0c6a87c-f597-3735-965f-650be23426a0/norsk-lovtidend-avdeling-i).
  Sjå [`docs/lovdata-datasett.md`](docs/lovdata-datasett.md).
- **Notion** - arbeidsnav (over).
- Vidare register: [`docs/kjelderegister.md`](docs/kjelderegister.md).

## Prinsipp

Nøytralt og bevisbasert · primærkjelde først · verifiser før påstand ·
dataminimer (persondata blir i Notion) · presseetikk (samtidig imøtegåing) ·
følg lisens. Rolle: [`AGENTS.md`](AGENTS.md) / [`docs/research-agent.md`](docs/research-agent.md).
