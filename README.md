# Marco Giovanni Ferrari

Sito personale: didattica e fotografia. Destinazione: https://mgferrari.github.io/

## Aggiornamenti con ChatGPT

- Struttura, testi e generazione delle pagine principali: `scripts/build_site.py`.
- Stile del sito: `assets/site.css`.
- Cartesian Lab: `didattica/matematica/cartesian-lab/` (HTML, CSS e JavaScript).
- Letture di Economia: modificare `sorgenti/economia/content/` e, per la grafica, `sorgenti/economia/web/`.
- Rigenerare tutto con `python3 scripts/build_site.py`, controllare i collegamenti e pubblicare i file aggiornati.
- Foto: usare esclusivamente immagini selezionate dal proprietario, ottimizzate per il web. La sezione iniziale rimanda a Instagram.

Non modificare solo gli HTML generati: il successivo build li sovrascrive.

## Pubblicazione

GitHub Settings → Pages → Deploy from a branch → `main` → `/ (root)`.
Il sito è statico e non richiede installazione di dipendenze. `.nojekyll` evita elaborazioni aggiuntive.

## Provenienza

Contenuti importati il 4 ottobre 2026 da:
- `mgferrari/cartesian_lab`, commit `02d0d0622ad1d8394218a274384155398e02be32` (tree).
- `mgferrari/economia-don-bosco`, tree `ee0e29c14d5febb0dad2041501b391d16c654061`.

I repository originali non sono stati modificati o cancellati. Da questa integrazione gli aggiornamenti destinati al sito personale vanno effettuati qui. Per Economia sono stati rigenerati i sorgenti correnti: stampa della singola lettura, senza stampa integrale del libretto.
