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

## Tabell (utdrag — full liste i Notion)

| Institusjon | Land | By | Etiske retningslinjer | Nivå | Prosedyre for eksterne | Direkte URL |
| --- | --- | --- | --- | --- | --- | --- |
| Arkitektur- og designhøgskolen i Oslo (AHO) | Noreg | Oslo | (fyll inn) | (fyll inn) | (påstått: ingen offentleg prosedyre) | aho.no |
| … | … | … | … | … | … | … |

> Eksporter den fulle, ajourførte tabellen frå Notion:
> ```bash
> export NOTION_TOKEN=ntn_...
> python3 scripts/notion_export.py bca7224e13a047b894e99ac9497d7830 \
>         data/notion-export/etikk-benchmark.csv
> ```
> Atterhald: «78 skular» og «2 av 78» må kunne dokumenterast med kjelde per skule
> før talet brukast offentleg.
