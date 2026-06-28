# Importere til Notion

> Eg har ikkje skrivetilgang til Notion-sida. Slik får du databasen inn sjølv - kvar CSV blir ein eigen Notion-database du kan filtrere og sortere.

## Steg

1. Opne Notion-sida `AHO-etikk` (lenka du gav).
2. Lag ein ny underside per ark, eller bruk `/database` ▸ **Import**.
3. **Import** ▸ **CSV** ▸ vel fila frå `database/`-mappa.
4. Gjenta for kvar av dei seks CSV-ane:
   - `1_Lovforesegner.csv`
   - `2_Faktapaastandar.csv`
   - `3_AHO_ord_vs_royndom.csv`
   - `4_Palantir_menneskerett.csv`
   - `5_Krav_tiltak.csv`
   - `6_Kjelder_arkiv.csv`

## Tilrådde Notion-eigenskapar etter import

For **2_Faktapaastandar** og **1_Lovforesegner**:
- Gjer `Status`-kolonnen om til ein **Select** med fargar: A = grøn, B = gul, C = blå.
- Lag ein **filtrert visning** «Treng verifisering» = `Status` inneheld `B`.

For **3_AHO_ord_vs_royndom**:
- Gjer `Type` om til **Select**: LOVBROT = raud, LØFTEBROT = oransje.

For **6_Kjelder_arkiv**:
- Gjer `Wayback-status` om til **Select**: `TODO` = raud, `Nedlasta…` = grøn.
- Dette blir di arbeidsliste for arkivering.

## Lovtekst-sidene

Markdown-filene i `kunnskap/` kan limast rett inn som Notion-sider (Notion les markdown ved innliming). Lag ei mor-side «Rettskjelder» og legg `SENTRALE_FORESEGNER.md` øvst.

## Synk-tips

Notion-import er ein **eingongs-snapshot** - den synkar ikkje automatisk med GitHub. Når du oppdaterer ein CSV i repoet, re-importer for å oppdatere Notion, eller hald GitHub som «source of truth» og Notion som lesevisning.
