#!/usr/bin/env python3
"""Build public pages without external dependencies. Run from any directory."""
from pathlib import Path
import subprocess, shutil
R=Path(__file__).resolve().parents[1]

def page(path,title,body,active=''):
 depth=len(Path(path).parts)-1
 prefix='/' if path=='404.html' else '../'*depth
 nav=''.join(f'<a href="{prefix}{url}"'+(' aria-current="page"' if label==active else '')+f'>{label}</a>' for label,url in [('Didattica','didattica/'),('Fotografia','fotografia/'),('Chi sono','chi-sono/')])
 doc=f'''<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} · Marco Giovanni Ferrari</title><meta name="description" content="Materiali didattici di matematica ed economia, laboratori interattivi e fotografia. Il sito personale di Marco Giovanni Ferrari."><meta name="theme-color" content="#f6f4ee"><link rel="stylesheet" href="{prefix}assets/site.css"></head>
<body><a class="skip" href="#contenuto">Vai al contenuto</a><div class="wrap"><header class="header"><a class="brand" href="{prefix}index.html">Marco Giovanni Ferrari<span>Didattica &amp; fotografia</span></a><nav aria-label="Navigazione principale">{nav}</nav></header><main id="contenuto">{body}</main><footer class="footer"><span>© Marco Giovanni Ferrari</span><span><a href="{prefix}didattica/">Didattica</a> &nbsp; / &nbsp; <a href="https://www.instagram.com/mgferrari_photo/">Instagram ↗</a></span></footer></div></body></html>'''
 target=R/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(doc)

def card(number,title,text,url,label,warm=False):
 return f'<a class="card{" warm" if warm else ""}" href="{url}"><span class="number">{number}</span><h2>{title}</h2><p>{text}</p><span class="arrow">{label}<b aria-hidden="true">↗</b></span></a>'

page('index.html','Home','''<section class="hero"><p class="eyebrow">Lo spazio di Marco Giovanni Ferrari</p><h1>Insegnare, esplorare.<br><em>Osservare.</em></h1><p class="lead">Materiali per imparare, strumenti per capire e uno spazio per la fotografia.</p></section><div class="section-head"><h2>Due percorsi, uno spazio</h2><span>Esplora il sito</span></div><section class="grid" aria-label="Esplora il sito">'''+card('01 / IMPARARE','Didattica','Matematica ed economia: letture, strumenti e laboratori da usare in classe e nello studio.','didattica/','Esplora i materiali')+card('02 / OSSERVARE','Fotografia','Uno spazio dedicato alle immagini e ai progetti fotografici.','fotografia/','Scopri lo spazio fotografico',True)+'''</section><section class="note"><h2>Da una domanda<br>a un altro sguardo.</h2><div><p>Sono Marco, insegnante di matematica ed economia. Qui raccolgo il mio lavoro didattico e la mia passione per la fotografia.</p><a href="chi-sono/">Qualcosa su di me →</a></div></section>''')
page('didattica/index.html','Didattica','''<section class="hero compact"><p class="eyebrow">01 / Imparare</p><h1>Didattica</h1><p class="lead">Materiali per accompagnare lo studio: dalle formule ai grafici, dalle parole dell’economia al mondo che descrivono.</p></section><section class="grid" aria-label="Materie">'''+card('MATEMATICA','Vedere le formule','Un laboratorio interattivo per esplorare il piano cartesiano e il ruolo dei parametri.','matematica/','Vai a matematica')+card('ECONOMIA','Leggere e capire','Quattordici letture progressive, con lessico, esempi e stampa della singola lettura.','economia/','Apri le letture',True)+'''</section>''','Didattica')
page('didattica/matematica/index.html','Matematica','''<p class="crumb"><a href="../">Didattica</a> / Matematica</p><section class="hero compact"><p class="eyebrow">Matematica</p><h1>Dalla formula<br><em>al grafico.</em></h1><p class="lead">Esplora le funzioni, modifica i parametri e osserva che cosa cambia nel piano cartesiano.</p></section>'''+card('LABORATORIO INTERATTIVO · IN INGLESE','Cartesian Lab','Retta, parabola, circonferenza, radice, valore assoluto, esponenziale ed ellisse. Con slider, brevi spiegazioni e sfide.','cartesian-lab/','Entra nel laboratorio'),'Didattica')
page('fotografia/index.html','Fotografia','''<section class="hero compact"><p class="eyebrow">02 / Osservare</p><h1>Uno spazio<br>per le <em>immagini.</em></h1><p class="lead">La sezione fotografica del mio sito personale.</p></section><section class="photo-block"><h2>Le fotografie,<br>per ora su Instagram.</h2><div><p>Le gallerie di questo sito sono in preparazione. Nel frattempo puoi trovare i miei scatti su @mgferrari_photo.</p><a class="button" href="https://www.instagram.com/mgferrari_photo/">Guarda le fotografie ↗</a></div></section>''','Fotografia')
page('chi-sono/index.html','Chi sono','''<section class="hero compact"><p class="eyebrow">Chi sono</p><h1>Marco Giovanni<br><em>Ferrari</em></h1></section><div class="prose"><p>Insegno matematica ed economia e coltivo una passione per la fotografia.</p><p>Questo sito riunisce materiali per le lezioni, strumenti interattivi per lo studio e uno spazio dedicato alle immagini.</p><p>La sezione didattica è pensata per trovare e utilizzare facilmente le risorse, in classe o in autonomia.</p><a class="text-link" href="../didattica/">Esplora la didattica →</a></div>''','Chi sono')
page('404.html','Pagina non trovata','''<section class="hero"><p class="eyebrow">Errore 404</p><h1>Ci siamo persi<br>una pagina.</h1><p class="lead">Il collegamento potrebbe essere cambiato.</p><a class="button text-link" href="/">Torna alla home →</a></section>''')
subprocess.run(['python3',str(R/'sorgenti/economia/scripts/build_site.py')],check=True)
out=R/'didattica/economia'
shutil.copytree(R/'sorgenti/economia/docs',out,dirs_exist_ok=True)
for directory in [out,R/'didattica/matematica/cartesian-lab']:
 for p in directory.glob('*.html'):
  text=p.read_text()
  if 'class="project-return"' not in text:
   relative='../../' if directory==out else '../../../'
   bar=f'<a class="project-return" href="{relative}didattica/">← Marco Giovanni Ferrari · Didattica</a>'
   style='<style>.project-return{display:block;padding:10px 24px;background:#f6f4ee;color:#253a32;border-bottom:1px solid #ccd1c6;font:13px/1.5 system-ui} @media print{.project-return{display:none}}</style>'
   text=text.replace('</head>',style+'</head>')
   text=text.replace('<aside>','<aside>'+bar) if directory==out else text.replace('<body>','<body>'+bar)
   p.write_text(text)
(R/'.nojekyll').touch()
print('Personal site built.')
