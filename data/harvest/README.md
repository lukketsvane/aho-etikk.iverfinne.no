# data/harvest/ - arkivhausting (15 år)

Råmateriale frå systematisk hausting av AHO-relatert dokumentasjon, med vekt på
kva AHO har **hevda / lova / avtalt** og styringa bakover i tid.

## `wayback-aho-index.csv`

Indeks over **2 068 Wayback Machine-snapshots** av aho.no (2000-2026), henta via
Internet Archive CDX API (`https://web.archive.org/cdx/search/cdx`), kategorisert:

| Kategori | Snapshots | Kva det dekkjer |
| --- | --- | --- |
| studieplan/master design | 1050 | Studieplan/programsider - etikk-læringsutbyte over tid |
| etikk/retningslinjer | 367 | Etiske retningslinjer, reglement, vedtekter |
| styre/sakspapir | 296 | Styremøte, sakspapir, protokollar |
| strategi | 195 | Strategidokument |
| aarsrapport/meldingar | 160 | Årsrapportar, planar og meldingar, kvalitetsmeldingar |

Kolonnar: `kategori, dato (YYYYMMDD), timestamp, original_url, statuscode, wayback_url`.
Kvar `wayback_url` opnar det arkiverte dokumentet direkte.

### Bruk

```bash
# alle styre-snapshots frå 2015
awk -F, '$1=="styre/sakspapir" && $2 ~ /^2015/' data/harvest/wayback-aho-index.csv
# eldste studieplan-snapshot
awk -F, '$1=="studieplan/master design"' data/harvest/wayback-aho-index.csv | sort -t, -k2 | head
```

### Reproduser / utvid

CDX-spørjing (bruk **https** - http er blokkert av egress):
```
https://web.archive.org/cdx/search/cdx?url=aho.no&matchType=domain&output=json
  &collapse=digest&fl=timestamp,original,statuscode,mimetype
  &filter=urlkey:.*<mønster>.*&limit=4000
```

## `dbh-aho-design-tidsserie.csv`

Tidsseriedata frå **DBH/HK-dir** (open API, `dbh-data.dataporten-api.no`) for AHO
(instkode 1220), 2011-2025. Kvantifiserer design-nedbygginga:
- **MASTERID kull (møtt studiestart):** ~30 (2017-19) → **59/59/60 (2020-22)** →
  **31/40/35 (2023-25)** - stadfestar opptrapping (korona-plassar) og reduksjon.
- **MASTERDES (2-årig): 0 møtt 2024-25** - i praksis under utfasing.
- AHO totalt veks 565 (2011) → 892 (2025) → design-kuttet er **relativ intern
  omfordeling**, ikkje institusjonsvid nedgang.

⚠️ AHO rapporterer all studentdata til DBH under avdelingskode `000000` - det finst
**inga institutt-/avdelingsnedbryting**; design er rekonstruert via studieprogram-
kode (MASTERID/MASTERDES/MASTERSOD). MASTERSOD er ofte GDPR-skjerma (<3).

## Atterhald

- Snapshots er **arkivkopiar** - kontroller mot original der det er viktig; OCR/
  rendering kan vere ufullstendig.
- `collapse=digest` fjernar identiske kopiar, men same dokument kan finnast under
  fleire URL-ar (omstrukturering av aho.no over tid).
- Dokument bak innlogging (Feide, intranett) er **ikkje** fanga - krev innsynskrav.
- Tildelingsbrev/utviklingsavtale frå KD ligg på regjeringen.no (eige spor).
