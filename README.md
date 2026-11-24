# MUNT Hypotheken – Hypotheekberekening

Nabouw van de *Aanvraagstraat* van munt.hypotheekbond.nl als één standalone HTML-bestand (`index.html`), zonder externe API's of build-stap.

**Live:** https://jeroen-o.github.io/munt-hypotheken-berekening/

## Stappen
0. Start
1. Vraagprijs (ook via `?vraagprijs=350000` in de URL)
2. Mijn totale kosten: hoofdsom, verbouwing (70% waardestijging), eigen geld, energielabel, NHG
3. Kan ik dit bedrag lenen?: max. hypotheek (Nibud 2026-tabellen, ook AOW), rentevaste periode, maandlast en JKP
4. Overzicht + rapport (opent in nieuw venster om af te drukken of als PDF op te slaan)
5. Hoe nu verder? (adviseurszoeker)

## Rekenregels
Gekalibreerd tegen de live rekentool (23-11-2026). Uitkomsten zijn op ~3.000 testpunten tot op de cent gelijk.
- Overdrachtsbelasting 2%. Notaris leveringsakte en hypotheekakte € 650 elk, taxatie € 500, advies € 2.500
- NHG: 0,4% van de hoofdsom, kostengrens € 470.000
- Rente per risicoklasse (NHG, ≤60, ≤80, ≤90, >90% LTV). Bij aflossing zakt de rente automatisch naar een lagere klasse en wordt de annuïteit herberekend
- Toetsrente bij een rentevaste periode korter dan 10 jaar: minimaal 5%
- Alleenstaande: + € 17.000 (vanaf de eerste tabelrij). Krediet: 2% per maand. Studieschuld: factor 1,05 tot 1,40. Erfpachtcanon: per maand
- Energielabel: extra leenruimte en EBV-ruimte volgens de tabellen in `CONFIG`

**Tarieven bijwerken:** pas `CONFIG.rentes` en `CONFIG.tariefDatum` aan, bovenaan het script in `index.html`.

## Toegankelijkheid (WCAG 2.1 AA)
- Alles bedienbaar met het toetsenbord: echte radio-knoppen, `<details>` in plaats van tooltips, geen enkelcijferige datumvakjes
- Focus springt naar de kop van de stap. De voortgang staat in een `<ol>` met `aria-current`
- Contrast AA: merkgroen alleen als vlak met donkere tekst, groene tekst in `#006b4c`
- Foutmeldingen zijn gekoppeld via `aria-describedby`/`aria-invalid`, met herstelknop
- Responsive vanaf 320px, doelgrootte ≥ 44px, ondersteunt `prefers-reduced-motion`

## Rapport (PDF)
"Download rapport" opent een A4-document van 19 pagina's in een nieuw venster: het opent automatisch het printvenster, waar je "Opslaan als PDF" kiest. Het ontwerp en de teksten zijn één-op-één overgenomen van het MUNT-rapport:
- Voorblad en pagina 1–5, 7 en 8 worden opgebouwd met de berekende waarden.
- Pagina 6 (rekenvoorbeeld € 250.000) en het voorbeeld-renteaanbod (10 pagina's) zijn vaste afbeeldingen uit het origineel (`assets/rapport/`).
- Lettertypen: Open Sans (zoals het origineel) en Roboto Slab als vervanger van Serifa BT, beide OFL, in `assets/fonts/`.

## Standalone-versie bouwen
`python3 tools/bouw-standalone.py` maakt `munt-hypotheekberekening-standalone.html`: één bestand van ca. 2 MB, met alle afbeeldingen en lettertypen ingebakken. Draai dit na elke wijziging in `index.html`.
