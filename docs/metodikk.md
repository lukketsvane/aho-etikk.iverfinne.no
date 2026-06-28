# Metodikk - kjeldekritisk gravejournalistikk

Arbeidsmetoden for dette prosjektet, avleidd frå rolla i
[`research-agent.md`](research-agent.md). Kort sagt: **primærkjelde først,
verifiser før påstand, dokumenter alt, dataminimer.**

## 1. Frå spørsmål til søk

1. Omformuler researchspørsmålet til 3-7 presise søkestrengar (nynorsk, bokmål,
   engelsk; ta med eldre rettskriving og alternative namn).
2. Identifiser entitetar: person, organisasjon (org.nr.), stad, tidsrom,
   sak-/dokumentnummer, lov/forskrift, arkivsignatur.
3. Finn autoritativ primærkjelde før du går til omtale.
4. Hent metadata før fulltekst.

## 2. Kjeldeorden (autoritet først)

Følg fasane i [`research-agent.md`](research-agent.md): Nasjonalbiblioteket →
NRK → lov/rett/innsyn → arkiv/kulturarv → bibliotek/forsking → presse →
kart/eigedom → register/økonomi. Tilgangsnivå og endepunkt står i
[`kjelderegister.md`](kjelderegister.md).

For denne saka er tyngdepunktet **Fase 3** (Lovdata, Stortinget, eInnsyn,
regjeringen.no), **Fase 5** (Cristin/NVA, AHO Open, DBH/HK-dir) og **Fase 8**
(Brønnøysund, SSB) - sjå [`aho-sak/kjelder-aho.md`](aho-sak/kjelder-aho.md).

## 3. Verifisering

Kryssjekk med minst éi uavhengig kjelde dersom funnet er:
- OCR-basert, eller frå ufullstendig kjelde
- politisk/juridisk
- om person, eigedom, økonomi eller skuldingar.

Gradér styrken på kvart funn (jf. Notion-databasen «AHOs lumskheit»):

| Styrke | Krav |
| --- | --- |
| **Sterk** | Primærdokument + uavhengig stadfesting; tåler offentleggjering og tilsvar |
| **Medium** | Éi god primærkjelde, men manglar uavhengig stadfesting |
| **Svak** | Indikasjon / sekundærkjelde / udokumentert; må styrkast før bruk |

## 4. Skilje påstand / bevis

Skriv aldri ein påstand som faktum før den er verifisert. Bruk fast struktur:

> **Regel eller lovnad** (kva som var lova / kravd) → **Røyndom / brot** (kva som
> faktisk skjedde) → **Kjelde** (primærdokument) → **Merknad og atterhald**.

Dette speglar feltstrukturen i Notion-funndatabasen, slik at funn kan flyttast
1:1 mellom repo og Notion.

## 5. Logging

Logg kvart søk i [`sokelogg.md`](sokelogg.md): dato/tid, søkestreng, kjelde/API,
endepunkt/URL, parameter, treff, feilkjelder, vidare steg. Reproduserbarheit er
ein del av kjeldekritikken.

## 6. Personvern og lov (bindande)

- Hent ikkje sensitive persondata utan rettsleg grunnlag og relevant formål.
- Ikkje samanstill data om privatpersonar berre fordi teknisk tilgang finst.
- Skil **offentleg journalmetadata** (kan delast) frå **sjølve dokumentet** (be
  om innsyn). Sjå [`maler/`](../maler/).
- Personregisteret «personar av interesse» blir i Notion (tilgangsstyrt) - det
  blir **ikkje** eksportert til dette repoet. Sjå [`notion.md`](notion.md).
- Følg lisenskrav og kreditering (Lovdata = NLOD 2.0).

## 7. Presseetikk

Saka gjeld ein offentleg institusjon (AHO) og personar i offentlege roller.
Hald deg til Ver Varsam-plakaten: rett til samtidig imøtegåing (VVP 4.14),
kjeldekritikk og kontroll av opplysningar (3.2), og skilje mellom fakta og
kommentar. Gi den/dei det vedkjem høve til tilsvar før publisering.
