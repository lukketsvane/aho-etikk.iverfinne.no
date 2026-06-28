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

## Status etter runde 1 (28.06.2026)

- **Skuleliste:** 70 nordiske design-/arkitektureiningar kartlagde (Noreg, Sverige,
  Danmark, Finland, Island) → [`data/benchmark/nordiske-skular.csv`](../../data/benchmark/nordiske-skular.csv).
- **Koda så langt:** 19 skular (6 NO, 7 SE, 5 FI, 1 IS) →
  [`data/benchmark/etikk-benchmark.csv`](../../data/benchmark/etikk-benchmark.csv).
- **Står att:** Danmark (14), Finland (resten), full koding av alle 70.

### Nivåfordeling (koda, n=19)

| Nivå | Tal | Døme |
| --- | --- | --- |
| 1 – berre nasjonalt rammeverk | 2 | BAS, Beckmans |
| 2 – eigen generell etikkode | 12 | **AHO**, Konstfack, KTH, Tampere, Oulu, LHÍ … |
| 3 – kriterium for eksternsamarbeid | 3 | KHiO, Høyskolen Kristiania, Aalto ARTS |
| 4 – partnar-vurdering / reservasjonsrett | 2 | NTNU (ansatt), NMBU (inkl. student) |

### Kritisk funn for A11 (nøytralitet)

Påstanden «AHO er **éin av berre to av 78**» utan offentleg prosedyre/krav for
etisk vurdering av eksterne samarbeid **held ikkje mot utvalet**:

- Med **streng** definisjon (ekte prosedyre for eksterne, nivå ≥ 3): **dei fleste**
  skulane manglar det — AHO er typisk, ikkje unik. Berre Aalto ARTS, KHiO,
  Kristiania, NTNU og NMBU har noko i den retninga.
- Med **laus** definisjon (har skulen *noko* etisk kode/krav?): AHO **har** ein
  eigen etisk kode (nivå 2), og er då heller ikkje blant dei svakaste «to».

Det som **held**: AHO er blant dei **svakaste** (nivå 2; berre BAS lågare i Noreg),
har **inga** publisert prosedyre for etisk vurdering av eksterne samarbeid og
**ingen reservasjonsrett** for studentar. Den presise «2 av 78»-formuleringa bør
**ikkje** brukast offentleg før alle 70+ skular er koda med fast definisjon og
kjelde per skule.

> Eksporter / synk med Notion-databasen ved behov:
> ```bash
> export NOTION_TOKEN=ntn_...
> python3 scripts/notion_export.py bca7224e13a047b894e99ac9497d7830 \
>         data/notion-export/etikk-benchmark.csv
> ```
