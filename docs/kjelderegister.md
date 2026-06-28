# Kjelderegister — API-ar og databasar

Startregister for research. **Tilgang**: A = open maskinlesbar · B = API-nøkkel ·
C = søknad/heimel/avtale · D = nettside utan offentleg API. Utvid via
[data.norge.no](https://data.norge.no) sin API-katalog.

## Lov, rett, politikk og innsyn (Fase 3 — kjernen for denne saka)

| Kjelde | Tilgang | Endepunkt / URL | Beviser |
| --- | --- | --- | --- |
| Lovdata opne data | A (NLOD 2.0) | `https://api.lovdata.no/v1/publicData/list` | Gjeldande lover, forskrifter, Norsk Lovtidend avd. I |
| Lovdata Pro | C | lovdata.no/pro | Dommar, forarbeid, historikk (lisens) |
| Stortinget opne data | A | `https://data.stortinget.no` | Saker, voteringar, spørsmål, høyringar |
| eInnsyn | A (metadata) | `https://www.einnsyn.no` / api.einnsyn.no | Offentleg journal, møte; dokument via innsynskrav |
| Regjeringen.no | D/A | regjeringen.no | NOU, prop., høyringar, tildelingsbrev |
| Domstol.no | D | domstol.no | Domstolsinfo; full rettspraksis ofte ikkje ope |

## Forsking, utdanning og register (Fase 5 + 8)

| Kjelde | Tilgang | Endepunkt / URL | Beviser |
| --- | --- | --- | --- |
| Enhetsregisteret | A | `https://data.brreg.no/enhetsregisteret/api` | Org.nr., roller, verksemder |
| Regnskapsregisteret | A | `https://data.brreg.no/regnskapsregisteret/api` | Rekneskapstal |
| Cristin / NVA | A | `https://api.cristin.no` / nva.sikt.no | Vitskapleg produksjon, prosjekt |
| DBH / HK-dir | A | `https://dbh.hkdir.no` | Sektordata: studieprogram, tilsette, økonomi |
| AHO Open (Brage) | A | `https://aho.brage.unit.no` | AHO sine publikasjonar, avhandlingar |
| SSB | A | `https://data.ssb.no/api/v0` | Statistikk, klassifikasjonar |
| NSD/Sikt | C | sikt.no | Forskingsdata, surveydata |

## Nasjonalbiblioteket og presse (Fase 1 + 6)

| Kjelde | Tilgang | Endepunkt / URL | Beviser |
| --- | --- | --- | --- |
| NB API | A | `https://api.nb.no` | Katalogmetadata, digitalisert innhald |
| NB DH-LAB | A | `https://api.nb.no/dhlab` | Korpus, n-gram, fulltekstanalyse |
| Nettbiblioteket | A/norsk-IP | nb.no | Bøker, aviser, tidsskrift, bilete |
| Retriever/Atekst | C | retriever.no | Mediearkiv (lisens) |

## Kart, stad, eigedom (Fase 7)

| Kjelde | Tilgang | Endepunkt / URL | Beviser |
| --- | --- | --- | --- |
| Geonorge | A | `https://www.geonorge.no` | Kartkatalog, WMS/WFS |
| Kartverket stedsnavn | A | ws.geonorge.no/stedsnavn | Stadnamn |
| Kartverket adresse | A | ws.geonorge.no/adresser | Adresser, geokoding |
| Matrikkel / Grunnbok | C | kartverket.no | Eigedom (heimel/avtale) |

## Arbeidsdata i dette repoet

| Datasett | Tilgang | Sti |
| --- | --- | --- |
| Lovdata-indeks (metadata) | A | [`data/index/`](../data/index/) |
| Lovdata råkorpus (tarballs) | A | [`data/raw/`](../data/raw/) |
| Norsk Lovtidend avd. I | A | `scripts/fetch_lovdata.sh` (ikkje committa) |
| Notion-arbeidsnav | B (`NOTION_TOKEN`) | sjå [`notion.md`](notion.md) |
