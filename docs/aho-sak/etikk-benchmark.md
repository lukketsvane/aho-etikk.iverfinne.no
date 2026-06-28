# Etikk-benchmark — design-/arkitekturskular i Norden

Speglar Notion-databasen **«etiske retningslinjer»**. Grunnlag for påstand A11:
*AHO er éin av berre to av 78 nordiske design-/arkitekturskular utan offentleg
prosedyre eller uttala krav om etisk vurdering av eksterne samarbeid.*

## Felt (same som Notion)

- **Institusjon** · **Land** (Noreg/Sverige/Danmark/Finland/Island) · **By**
- **Etiske retningslinjer**: Ja · Delvis · Uklart · Ikkje funne · Nei
- **Nivå**:
  - `0` Ikkje funne
  - `1` Berre nasjonalt rammeverk
  - `2` Eigen generell etikkode
  - `3` Eigne kriterium for eksternsamarbeid
  - `4` Partnar-etisk vurdering / reservasjonsrett
- **Prosedyre for etisk vurdering av eksterne** (fritekst)
- **Direkte URL** · **Merknader og atterhald**

## Metode

For kvar av dei 78 skulane: søk etter (a) offentleg etisk kode, (b) prosedyre for
etisk vurdering av eksterne samarbeid, (c) reservasjonsrett for studentar. Kjelde
= direkte URL til institusjonen si side. Marker «Ikkje funne» ≠ «finst ikkje».
Definer kriteria for nivå 3–4 eksplisitt, sidan A11 heng på definisjonen.

## Status etter runde 2 (28.06.2026)

- **Skuleliste:** 70 nordiske design-/arkitektureiningar →
  [`data/benchmark/nordiske-skular.csv`](../../data/benchmark/nordiske-skular.csv).
- **Koda:** **47 skular** (11 NO, 14 SE, 14 DK, 7 FI, 1 IS) →
  [`data/benchmark/etikk-benchmark.csv`](../../data/benchmark/etikk-benchmark.csv).
- **Står att:** ~23 (mest mindre yrkeshøgskular, truleg nivå 1–2).

### Nivåfordeling (koda, n=47)

| Nivå | Tal | Døme |
| --- | --- | --- |
| 1 – berre nasjonalt rammeverk | 8 | BAS, Beckmans, Det Kongelige Akademi, KEA |
| 2 – eigen generell etikkode | 26 | **AHO**, Konstfack, KTH, DTU, KU, Oulu, LHÍ … |
| 3 – kriterium for eksternsamarbeid | 7 | KHiO, Kristiania, OsloMet, UiS, Aalto ARTS, Aarhus Univ., Borås |
| 4 – partnar-vurdering / reservasjonsrett | 6 | NTNU, NMBU, UiT, RUC, Berghs, SU-DSV |

**13 skular (nivå 3–4) har ein eksternsamarbeid-/partnarvurdering AHO manglar.**

### Konklusjon A11 — omformulert og forsvarleg

Den opphavlege påstanden «AHO er **éin av berre to av 78**» utan etisk
eksternprosedyre er **FALSK** og må ikkje brukast: 25 av 47 koda skular manglar
ein slik prosedyre — AHO er i fleirtalet, ikkje unik.

**Det som derimot held** (og er sterkare som poeng): AHO ligg på **nivå 2** og har
**inga** publisert prosedyre for etisk vurdering av eksterne samarbeid og **ingen
reservasjonsrett**, medan ein klar minoritet av nordiske skular — inkludert **7 av
11 koda norske** (KHiO, Kristiania, NTNU, NMBU, OsloMet, UiT, UiS) — **har** ein
slik prosedyre. I Noreg er det berre **BAS og Volda** som ligg likt med eller under
AHO. Forsvarleg formulering:

> «Fleire norske institusjonar — m.a. UiT, NTNU, NMBU, OsloMet, KHiO og UiS — har
> innført etiske kriterium eller prosedyrar for eksterne samarbeid. AHO har det
> ikkje, og er blant dei svakaste i Noreg på dette punktet.»

> Eksporter / synk med Notion-databasen ved behov:
> ```bash
> export NOTION_TOKEN=ntn_...
> python3 scripts/notion_export.py bca7224e13a047b894e99ac9497d7830 \
>         data/notion-export/etikk-benchmark.csv
> ```
