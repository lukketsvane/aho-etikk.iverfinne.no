# AHO-spesifikke primærkjelder

Konkrete oppslag for granskinga. Tilgangsnivå: A = open · B = API-nøkkel ·
C = søknad/heimel · D = nettside. Kontroller alltid mot originaldokument.

## Eining

| Felt | Verdi |
| --- | --- |
| Namn | Arkitektur- og designhøgskolen i Oslo (AHO) |
| Org.nr. | **971 526 378** (organisasjonsform ORGL - statleg organisasjonsledd) |
| Sektor | Statleg vitskapleg høgskule under **Kunnskapsdepartementet** |
| Nettstad | aho.no |
| Relatert | Klimaforeningen for AHOs studenter, org.nr. 930 461 199 |

## Oppslag (kopier og køyr)

| Kva | Tilgang | URL / endepunkt |
| --- | --- | --- |
| Enhetsregisteret (roller, signatur) | A | `https://data.brreg.no/enhetsregisteret/api/enheter/971526378` |
| Rekneskap (statleg - avgrensa) | A | `https://data.brreg.no/regnskapsregisteret/api/regnskap/971526378` |
| eInnsyn - offentleg journal | A | einnsyn.no → søk verksemd «Arkitektur- og designhøgskolen» |
| Cristin/NVA - publikasjonar/prosjekt | A | `https://api.cristin.no/v2/institutions?name=AHO` |
| DBH / HK-dir - studieprogram, tilsette, økonomi | A | `https://dbh.hkdir.no` (vel institusjon AHO) |
| AHO Open (Brage) | A | `https://aho.brage.unit.no` |
| Riksrevisjonen - forvaltningsrevisjon UH-sektor | D | riksrevisjonen.no |
| NOKUT - tilsyn/akkreditering | D | nokut.no |
| Sivilombodet - klager på innsyn/forvaltning | D | sivilombudet.no |
| Regjeringen.no - tildelingsbrev/etatsstyring KD→AHO | A/D | regjeringen.no → Kunnskapsdepartementet |
| Stortinget opne data - løyvingar, spørsmål | A | `https://data.stortinget.no` |

## Regelverk AHO er bunden av (slå opp i Lovdata-indeksen)

Som statleg høgskule er AHO m.a. bunden av:

- **Universitets- og høgskulelova** (krav til utdanningskvalitet, læringsutbyte)
- **Offentleglova** (innsyn, journalføring)
- **Forvaltningslova** (saksbehandling, habilitet, partsrettar)
- **Statstilsettelova** og **arbeidsmiljølova**
- **Anskaffingsregelverket** (LOA/FOA) ved innkjøp/eksterne samarbeid
- **Økonomireglementet for staten** / økonomistyring
- **Studietilsynsforskrifta** (NOKUT) - krav til studieprogram

Bruk indeksen til å finne gjeldande versjon og ikrafttreding:

```bash
grep -iE "universiteter og høyskoler|offentleglov|forvaltningslov|offentlige anskaffelser" \
     data/index/lover.csv | cut -d, -f3,5,11,17
```

Sjekk kunngjering/endringshistorikk i Norsk Lovtidend avd. I
(`scripts/fetch_lovdata.sh`).

## Kopling regel → moglege funn

| Regel/lovnad | Kva å sjekke | Kjelde |
| --- | --- | --- |
| UH-lova: læringsutbyte skal vurderast | Vert etikk-læringsutbyte faktisk prøvd/vurdert? | Studieplan, emneskildring, sensurordning |
| Offentleglova: journalføring/innsyn | Vert dokument journalførte og utlevert i tide? | eInnsyn, innsynskrav (sjå maler/) |
| Studieplan/marknadsføring | Samsvar mellom det som lovast og det som leverast | aho.no, studiekatalog, vitnemål |
| Anskaffingsregelverk | Eksterne samarbeid - open konkurranse, habilitet | eInnsyn, kontraktar, Doffin |

> Alt over er **kontrollpunkt**, ikkje konstaterte brot. Fyll funn inn i
> [`funn.md`](funn.md) med kjelde og styrkegrad.
