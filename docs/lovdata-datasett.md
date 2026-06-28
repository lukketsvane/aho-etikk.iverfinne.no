# Lovdata-datasett

Prosjektet brukar Lovdata sine **opne data** som juridisk grunnlag — for å kunne
sjekke kva lover, forskrifter og kunngjeringar som faktisk gjeld, og kva AHO som
statleg høgskule er bunden av.

## Kjelde og lisens

- Utgjevar: **Stiftelsen Lovdata**
- API: `https://api.lovdata.no/v1/publicData` (sjå
  `https://api.lovdata.no/v1/publicData/list`)
- Datasettside: data.norge.no → «Norsk Lovtidend, Avdeling I»
  (`c0c6a87c-f597-3735-965f-650be23426a0`)
- Lisens: **NLOD 2.0** (Norsk lisens for offentlege data) — fri vidarebruk med
  kreditering «Lovdata».
- Ratelimit: ~200 kall per vindauge (`X-RateLimit-*` i responsen).

## Datasett

| Fil | Innhald | Storleik (bz2) | I repoet? |
| --- | --- | --- | --- |
| `gjeldende-lover.tar.bz2` | 788 gjeldande lover, ajourførte | ~5,9 MB | ✅ `data/raw/` |
| `gjeldende-sentrale-forskrifter.tar.bz2` | 3 487 gjeldande forskrifter | ~20 MB | ✅ `data/raw/` |
| `lovtidend-avd1-2001-2025.tar.bz2` | Norsk Lovtidend avd. I 2001–2025 | ~69 MB | ⬇️ via fetch-skript |
| `lovtidend-avd1-2026.tar.bz2` | Norsk Lovtidend avd. I, i år | ~1 MB | ⬇️ via fetch-skript |

Dei to «gjeldande»-sett er committa (ein lov-/forskrift-snapshot). Dei store
Lovtidend-arkiva (kunngjeringshistorikk) hentast ved behov med
`scripts/fetch_lovdata.sh` for å halde repoet lett.

## Filformat

Kvart dokument er ei `.xml`-fil som faktisk inneheld **HTML**. Metadata ligg i ei
`<dl class="data-document-key-info">`-blokk øvst (DokumentID, datokode, tittel,
departement, ikrafttreding, sist endra, rettsområde m.m.), følgt av sjølve
lov-/forskriftsteksten.

## Metadata-indeks

`scripts/build_index.py` strøymer tarballane og hentar ut metadatablokka til:

- `data/index/lover.csv` — 788 rader
- `data/index/forskrifter.csv` — 3 487 rader
- `data/index/lovdata-index.jsonl` — 4 275 dokument

Feltforklaring i [`data/index/SCHEMA.md`](../data/index/SCHEMA.md).

## Korleis dette brukast i saka

- Slå opp **kva regelverk AHO er bunden av** som statleg universitet/høgskule:
  universitets- og høgskulelova, forvaltningslova, offentleglova,
  statstilsettelova, økonomireglementet, anskaffingsregelverket m.m.
- Verifiser **gjeldande versjon og ikrafttreding** før du siterer ein paragraf.
- Bruk Norsk Lovtidend til å stadfeste **kunngjering** (kva som vart vedteke når).
- Søk i indeksen, t.d.:

  ```bash
  # alle lover under Kunnskapsdepartementet
  awk -F, 'NR==1 || $7 ~ /Kunnskaps/' data/index/lover.csv

  # finn universitets- og høgskulelova
  grep -i "universiteter og høyskoler" data/index/lover.csv
  ```

Kontroller alltid funn mot originaldokumentet (lenkje i `url`-kolonnen) før sitat.
