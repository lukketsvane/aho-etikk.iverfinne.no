# AHO-etikk - juridisk og faktadatabase

> Strukturert faktagrunnlag for saka om Arkitektur- og designhøgskolen i Oslo (AHO) og det forfattaren kallar **lovbrot** (brot på rettsleg bindande krav) og **løftebrot** (brot på skulens eigne ord og marknadsføring), overfor studentane og Kunnskapsdepartementet.

Repo: `github.com/lukketsvane/aho-etikk.iverfinne.no`

## Kva dette er

Ein database, ikkje eit brev. Kvar påstand i grunnlagsdokumenta er kopla til (1) ein paragraf, (2) ei primærkjelde, (3) ein arkivlenke og (4) ein **verifiseringsstatus** - slik at det rettslege skiljet mellom provbart lovbrot og retorisk skarpt løftebrot held heile vegen.

## Kjernetesen i éi setning

AHO listar eit **lovpålagt** etikk-læringsutbytte (NKR nivå 7: *«kan analysere relevante fag-, yrkes- og forskningsetiske problemstillinger»*) men underviser det aldri som krav, prøver det aldri, og knyter ingen karakter eller sanksjon til det - i strid med kravet i **universitets- og høyskoleforskriften § 1-11** om at vurderingsforma skal vere tilpassa læringsutbyttet, og at informasjonen om studietilbodet skal vere korrekt.

## Mappestruktur

```
.
├── README.md                       ← denne fila
├── kunnskap/
│   ├── SENTRALE_FORESEGNER.md       ← START HER: nøkkelparagrafane med AHO-merknader
│   ├── INDEKS.md                    ← indeks over alle rettskjelder
│   ├── lover/                       ← fulltekst lover (verbatim, Lovdata)
│   ├── forskrifter/                 ← fulltekst forskrifter (verbatim, Lovdata)
│   └── nkr/                         ← NKR-forskrifta
├── database/
│   ├── AHO-etikk_database.xlsx      ← heile databasen, 6 ark + forklaring, fargekoda
│   ├── 1_Lovforesegner.csv
│   ├── 2_Faktapaastandar.csv
│   ├── 3_AHO_ord_vs_royndom.csv
│   ├── 4_Palantir_menneskerett.csv
│   ├── 5_Krav_tiltak.csv
│   └── 6_Kjelder_arkiv.csv
└── docs/
    ├── GIT_PUSH.md                  ← korleis pushe dette til repoet
    └── NOTION_IMPORT.md             ← korleis importere CSV-ane til Notion
```

## Verifiseringsstatus (gjennomgåande)

| Kode | Tyder | Farge i XLSX |
|------|-------|--------------|
| **A** | Verifisert via offentleg primærkjelde | Grøn |
| **B** | Forfattardokumentert - treng offentleg korroborering | Gul |
| **C** | Lovføresegn (eksakt sitert) | Blå |
| **LOVBROT** | Brot på rettsleg bindande krav | Raud |
| **LØFTEBROT** | Brot på AHOs eigne ord - ingen statutt bak | Oransje |

## Dei fem viktigaste rettslege funna

1. **Rettsgrunnlaget har skifta paragraf.** Studietilsynsforskrifta § 2-2 vart **oppheva 1.8.2025**. Kravet er vidareført i **UH-forskrifta § 1-11** (FOR-2024-06-28-1392). Alle referansar bør peike dit no.
2. **§ 1-11 gir to lovbrot-grunnlag i éin paragraf:** (a) vurderingsform tilpassa læringsutbyttet (samstemt vurdering), og (b) *«Informasjonen om studietilbudet skal være korrekt»* - det sistnemnde løftar «uærleg framstilling» frå løftebrot mot mogleg lovbrot.
3. **Berekraft er eit lovfesta formål.** UH-loven § 1-1: institusjonen skal *«bidra til en miljømessig, sosialt og økonomisk bærekraftig utvikling»*.
4. **NKR-samsvar er eit akkrediteringsvilkår.** UH-loven § 3-2: *«Akkrediterte studier skal være i samsvar med det nasjonale kvalifikasjonsrammeverket.»*
5. **NOKUT-tilsynet treffer berre systemet.** UH-loven § 16-2: tilsyn med *«systematiske kvalitetsarbeid»* - ikkje med om kvart utbytte faktisk blir levert. «Krinsen som skulle fange brotet, er huset sjølv.»

## Lovtekst-kjelde

All verbatim lovtekst er ekstrahert frå **Lovdata sitt opne API** under **NLOD 2.0**-lisens (fri bruk):
- `api.lovdata.no/v1/publicData/get/gjeldende-lover.tar.bz2`
- `api.lovdata.no/v1/publicData/get/gjeldende-sentrale-forskrifter.tar.bz2`

Nedlasta og ekstrahert 28. juni 2026. Dette er den autoritative, konsoliderte versjonen av gjeldande rett.

## Åtvaringar

- **B-merkte påstandar** (Amsterdam-turen, GK4-ordlyden, signaturlista, Minab-åtaket, dei nordiske skulane) er **ikkje** offentleg korroborerte og må ikkje presenterast som fastslått faktum før verifisering. Sjå ark 2 og 6.
- **Talsprik:** dei nordiske skulane er oppgjevne som ~47 i eitt dokument og ~78 i eit anna. Avklar før publisering.
- **markedsføringsloven** mot offentleg utdanningsinstitusjon er juridisk usikkert - UH-forskrifta § 1-11 (korrekt informasjon) er eit tryggare grunnlag.
- **GDPR/AI Act** rammar ikkje nødvendigvis AHO direkte ved eit observasjonsbesøk - hald Palantir-vinkelen som **etisk** (løftebrot), ikkje AHO-lovbrot.
