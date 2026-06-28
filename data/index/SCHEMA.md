# Datakatalog - Lovdata metadata-indeks

Generert av [`scripts/build_index.py`](../../scripts/build_index.py) frå dei
komprimerte tarballane i [`data/raw/`](../raw/). Kjelde: **Lovdata opne data**
(`api.lovdata.no`), lisens **NLOD 2.0**. Snapshot-dato står i git-historikken.

## Filer

| Fil | Innhald | Rader |
| --- | --- | --- |
| `lover.csv` | Gjeldande lover, sortert på datokode | 788 |
| `forskrifter.csv` | Gjeldande sentrale forskrifter, sortert på datokode | 3 487 |
| `lovdata-index.jsonl` | Alle dokument, eitt JSON-objekt per linje | 4 275 |

## Kolonnar

| Kolonne | Døme | Skildring |
| --- | --- | --- |
| `type` | `lov` / `forskrift` | Dokumenttype, avleidd frå kjeldetarball |
| `filename` | `nl-18140517-000.xml` | Filnamn i tarballen |
| `dokid` | `NL/lov/1814-05-17` | Lovdata DokumentID (stabil nøkkel) |
| `datokode` | `LOV-1814-05-17` | Datokode / legacy-ID |
| `tittel` | `Kongeriket Norges Grunnlov` | Fullt namn |
| `korttittel` | `Grunnloven (bokmål) - Grl.` | Korttittel der oppgitt |
| `departement` | `Justis- og beredskapsdepartementet` | Ansvarleg departement (kan vere fleire, skilde med mellomrom) |
| `etat` | `Protokollavd.` | Underordna etat/avdeling der oppgitt |
| `rettsomraade` | `Stats- ... > Grunnloven` | Rettsområde (oftast tomt for forskrifter) |
| `i_kraft` | `1905-11-15` | I kraft frå |
| `siste_endring_i_kraft` | `2024-05-21` | Ikraftsetjing av siste endring |
| `sist_endret_ved` | `forskrift/2024-06-07-928 fra 2024-05-21` | Kva som sist endra dokumentet |
| `publisert_i` | `II 1905 s 507` | Kunngjering i Norsk Lovtidend |
| `gjelder_for` | `Norge` | Geografisk verkeområde der oppgitt |
| `siste_rettelse` | `2021-07-01 (...)` | Siste redaksjonelle rettelse |
| `refid` | `lov/1814-05-17` | Relativ referanse-ID |
| `url` | `https://lovdata.no/lov/1814-05-17` | Direkte lenkje til Lovdata |

## Atterhald

- Felt manglar der Lovdata ikkje har fylt dei ut. T.d. har **3 462 av 3 487
  forskrifter** ikkje `rettsomraade` i kjelda - tom verdi tyder *ikkje oppgitt*,
  ikkje *finst ikkje*.
- Tekstfelt er reinska for HTML-taggar; lister er flata ut til éin streng.
- Indeksen er **metadata**, ikkje fulltekst. Sjølve lovteksten ligg i HTML-fila i
  tarballen (`data/raw/`). Kontroller alltid mot originaldokumentet før sitat.
- For kunngjeringshistorikk (kva som vart kunngjort når) - sjå Norsk Lovtidend
  Avdeling I via `scripts/fetch_lovdata.sh` (ikkje committa pga. storleik).
