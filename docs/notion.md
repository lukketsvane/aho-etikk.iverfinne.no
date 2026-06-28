# Notion - arbeidsnav

Den løpande granskinga blir driven i **Notion**. Notion er arbeidsnavet (notatar,
utkast, levande databasar); dette git-repoet er **data- og metodelaget**
(Lovdata-korpus, indeks, skript, malar, metode) som Notion-arbeidet hentar
grunnlag frå og kan ta snapshot inn i.

- Hovudside: **«AHO etikkrådet»** - 
  <https://app.notion.com/p/tingogtang/AHO-etikkr-det-38d1c6815f7880e5bad8ef59b1f76595>
- Integrasjon: intern connection **`aho-etikk`** (workspace JifUniversal's Notion).
  Tilgang: lese, oppdatere, setje inn innhald.
- Token: miljøvariabel `NOTION_TOKEN` (sjå [`.env.example`](../.env.example)).
  **Aldri** committa - `.env` er i `.gitignore`.

## Struktur i Notion

| Element | Type | Innhald |
| --- | --- | --- |
| AHO etikkrådet | side | Rota |
| brev til killi | side | Brev til Steinar Killi + kjernekrav (designskule treng eit «nei») |
| Funn: regelbrot og løftebrot («AHOs lumskheit») | database | Kjeldeførte funn - sjå skjema under |
| etiske retningslinjer | database | Benchmark av etikk-policy ved nordiske design-/arkitektskular |
| personar av interesse | database | **Personopplysningar - blir i Notion, ikkje eksportert hit** |
| AHO mot resten (søyle) | database/visning | Samanlikning |
| Innsynskrav til AHO (utkast) | side | Innsynskrav under arbeid |
| Tidslinje: AHO og krinsen (kjeldeført) | side | Tidslinje 1945-2026 |

## Skjema som speglar repoet

**Funndatabasen** («AHOs lumskheit») har felt som matchar
[`aho-sak/funn.md`](aho-sak/funn.md):
`Funn` · `Type` (Regelbrot / Løftebrot / Ansvarsglipe / Faktasjekk /
Styringssvikt / Interessekonflikt / Historisk forelegg / Alumni-fagleg /
Alumni-personleg) · `Regel eller lovnad` · `Røyndom / brot` · `Styrke`
(Sterk/Medium/Svak) · `Kjelde` · `Kjelde 2` · `Merknad og atterhald` · `Date` ·
`Årstal`.

**Etikk-benchmark** matchar [`aho-sak/etikk-benchmark.md`](aho-sak/etikk-benchmark.md):
`Institusjon` · `Land` · `By` · `Etiske retningslinjer` (Ja/Delvis/Uklart/Ikkje
funne/Nei) · `Nivå` (0-4) · `Prosedyre for etisk vurdering av eksterne` ·
`Direkte URL` · `Merknader og atterhald`.

## Snapshot frå Notion til repo

```bash
export NOTION_TOKEN=ntn_...
# Funndatabasen -> CSV (kan committast; sjå personvern under)
python3 scripts/notion_export.py baaf3e0b70b648f5a260c45347a267e6 \
        data/notion-export/funn.csv
# Etikk-benchmark -> CSV
python3 scripts/notion_export.py bca7224e13a047b894e99ac9497d7830 \
        data/notion-export/etikk-benchmark.csv
```

`data/notion-export/` er som standard i `.gitignore`. Vurder kvart snapshot mot
personvern før du eventuelt committar det - funn-/benchmark-data med ålment
formål kan delast, men ikkje personregisteret.

## Personvern

Databasen «personar av interesse» (namn, rolle, haldning, kontakt) er
personopplysningar. Den blir verande i Notion under tilgangsstyring og blir
**ikkje** lasta ned eller committa. Dataminimer: berre kjeldeførte funn med
offentleg interesse hører heime i versjonert form.
