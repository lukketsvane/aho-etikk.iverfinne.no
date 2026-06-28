# Pushe til repoet

> Eg (assistenten) har ikkje skrivetilgang til GitHub. Desse stega gjer du sjølv. Innhaldet er ferdig - du berre legg det inn og pushar.

## Alternativ A - du har repoet klona lokalt

```bash
# frå rota av aho-etikk.iverfinne.no
# kopier inn dei genererte mappene (juster sti til der du pakka ut zip-en)
cp -r ~/Downloads/aho-etikk-build/kunnskap ./
cp -r ~/Downloads/aho-etikk-build/database ./
cp -r ~/Downloads/aho-etikk-build/docs ./
cp    ~/Downloads/aho-etikk-build/README.md ./

git add kunnskap database docs README.md
git commit -m "Legg til juridisk kunnskapsbase: verbatim lovtekst (Lovdata NLOD 2.0) + 6-arks faktadatabase

- kunnskap/SENTRALE_FORESEGNER.md: nøkkelparagrafar med AHO-merknader
- UH-loven (LOV-2024-03-08-9), UH-forskrifta (FOR-2024-06-28-1392 § 1-11), NKR (FOR-2017-11-08-1846)
- database/AHO-etikk_database.xlsx + CSV-ar: lovføresegner, faktapåstandar, AHOs ord vs røyndom, Palantir/menneskerett, krav, kjelder
- Skil LOVBROT frå LØFTEBROT; verifiseringsstatus A/B/C gjennomgåande
- Sentralt funn: studietilsynsforskrifta § 2-2 oppheva 1.8.2025 -> krav vidareført i UH-forskrifta § 1-11"
git push origin main
```

## Alternativ B - nytt repo / første gong

```bash
git clone https://github.com/lukketsvane/aho-etikk.iverfinne.no.git
cd aho-etikk.iverfinne.no
# kopier inn som over, så:
git add -A && git commit -m "Initial: juridisk kunnskapsbase og faktadatabase" && git push
```

## Alternativ C - berre dra-og-slepp i nettlesaren

GitHub → repoet → **Add file ▸ Upload files** → dra inn mappene `kunnskap/`, `database/`, `docs/` og `README.md` → skriv commit-melding → **Commit changes**.

## Forslag til repo-struktur etterpå

```
aho-etikk.iverfinne.no/
├── README.md
├── kunnskap/
├── database/
├── docs/
└── (eksisterande brev/kronikkar du alt har)
```
