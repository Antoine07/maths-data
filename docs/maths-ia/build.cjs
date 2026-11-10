/* Builder propre à la branche maths-ia. Les supports Markdown font référence. */
const fs = require('node:fs');
const path = require('node:path');
const { execFileSync } = require('node:child_process');
const { createRequire } = require('node:module');
let dependencies = require;
try { dependencies.resolve('@marp-team/marp-core'); }
catch {
  dependencies = createRequire(path.join(execFileSync('npm', ['root', '-g'], {encoding:'utf8'}).trim(), '@marp-team/marp-cli/package.json'));
}
const { Marp } = dependencies('@marp-team/marp-core');
const marp = new Marp({html:true, inlineSVG:false, math:'katex'});
const base = __dirname, docs = path.dirname(base);
const config = JSON.parse(fs.readFileSync(path.join(base, 'parcours.json'), 'utf8'));
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const plain = s => s.replace(/<[^>]+>/g,'').replace(/&amp;/g,'&');
const relative = (from, to) => path.relative(path.dirname(from), to).split(path.sep).join('/');
const targets = new Map(config.modules.map(m => [path.join(base, 'supports', m.id+'.md'), path.join(base, m.id+'.html')]));
targets.set(path.join(base, 'supports/programme.md'), path.join(base, 'programme.html'));
targets.set(path.join(base, 'evaluation/sujet.md'), path.join(base, 'examen.html'));

function head(title, extra='') {
  return `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#f7f8f2"><title>${esc(title)} · Maths & IA</title><link rel="stylesheet" href="../assets/site.css"><link rel="stylesheet" href="../assets/slides.css"><link rel="stylesheet" href="../assets/katex/katex.min.css">${extra}<noscript><style>.slide-card[hidden]{display:block!important}.slide-card{margin-bottom:24px}.card-controls,.deck-toolbar{display:none!important}</style></noscript></head>`;
}
function header() {
  return '<a class="skip-link" href="#contenu">Aller au contenu</a><header class="site-header"><a class="brand" href="../index.html"><span class="brand-icon" aria-hidden="true">m.</span> Le labo maths <span class="brand-course">/ CODA</span></a><nav class="header-actions" aria-label="Navigation principale"><a class="back-link" href="index.html">Les deux semaines</a><a class="back-link" href="programme.html">Programme</a><a class="back-link" href="examen.html">Examen</a></nav></header>';
}
function footer() { return '<footer class="site-footer"><span>Le labo maths / CODA · Maths & IA</span><a href="index.html">Comprendre, construire et évaluer.</a></footer>'; }
function render(source, output) {
  const result = marp.render(fs.readFileSync(source, 'utf8'));
  return [...result.html.matchAll(/<section\b[^>]*>([\s\S]*?)<\/section>/g)].map(m => m[1]).filter(s => s.trim()).map(html => html
    .replace(/\b(href|src)="([^"]+)"/g, (all, attr, url) => {
      if (/^(?:https?:|data:|mailto:|#)/.test(url)) return all;
      const [file, fragment] = url.split('#');
      const target = path.resolve(path.dirname(source), decodeURI(file));
      return `${attr}="${relative(output, targets.get(target) || target)}${fragment ? '#'+fragment : ''}"`;
    })
    .replace(/<pre>/g, '<pre tabindex="0">').replace(/<table>/g, '<div class="table-wrap" tabindex="0"><table>').replace(/<\/table>/g, '</table></div>')
    .replace(/<p>(<img\b[^>]*src="([^"]+)"[^>]*>)<\/p>/g, (_,img,src) => `<figure class="math-figure lesson-illustration"><a href="${src}" target="_blank" rel="noopener" aria-label="Ouvrir la figure en grand">${img}</a><figcaption>Ouvrir en grand ↗</figcaption></figure>`));
}

const manifest = [];
function deck(meta, reading=false) {
  const source = path.join(base, 'supports', meta.id+'.md'), output = path.join(base, meta.id+'.html');
  const sections = render(source, output), total = sections.length;
  const titles = sections.map((s,i) => plain(s.match(/<h[1-6][^>]*>([\s\S]*?)<\/h[1-6]>/)?.[1] || `${meta.titre} — ${i+1}`));
  const list = titles.map((title,i) => `<a class="slide-link" href="#${i+1}" data-slide-link="${i+1}"${i===0?' aria-current="step"':''}><small>${String(i+1).padStart(2,'0')}</small><span>${title}</span></a>`).join('');
  const position = config.modules.findIndex(m=>m.id===meta.id), next = config.modules[position+1];
  const articles = sections.map((body,i) => `<article class="slide-card${/exercice|à vous/i.test(titles[i])?' exercise':''}" id="slide-${i+1}" aria-labelledby="slide-label-${i+1}"${!reading&&i>0?' hidden':''}><p class="question-kicker" id="slide-label-${i+1}">${esc(meta.repere)} <span class="pill">${i+1} / ${total}</span></p><div class="prose">${body}</div>${i===total-1?`<div class="chapter-end"><p>Contrôler les acquis avant de continuer.</p><a class="button primary" href="${next?next.id+'.html':'index.html'}">${next?esc(next.titre)+' →':'Revenir aux deux semaines →'}</a></div>`:''}</article>`).join('\n');
  fs.writeFileSync(output, `${head(meta.titre)}<body class="deck-page${reading?' reading-mode':''}" data-deck="maths-ia/${meta.id}">${header()}<main class="learning-main" id="contenu"><div class="page-heading"><div><p class="eyebrow">${esc(meta.repere)}</p><h1>${esc(meta.titre)}</h1><p>${esc(meta.objectif)}</p></div><span class="chapter-count">${total} slides</span></div><div class="deck-toolbar"><div class="mode-switch" role="group" aria-label="Mode d'affichage"><button id="mode-slides" aria-pressed="${!reading}">Slides</button><button id="mode-reading" aria-pressed="${reading}">Lecture continue</button></div><div class="toolbar-actions"><button class="text-button mobile-only" id="toggle-outline" aria-expanded="false" aria-controls="outline">Sommaire</button><button class="text-button" id="fullscreen">Plein écran</button><button class="text-button" id="print">Imprimer / PDF</button></div></div><div class="progress-line"><span id="position" role="status" aria-live="polite">Slide 1 sur ${total}</span><span id="progress-label">${Math.round(100/total)} %</span></div><progress id="progress" max="${total}" value="1" aria-label="Progression du chapitre"></progress><div class="learning-layout"><aside class="sidebar" id="outline"><p class="sidebar-title">DANS CETTE SÉANCE</p><nav class="slide-list" aria-label="Sommaire des slides">${list}</nav><p><a href="supports/${meta.id}.md" download>Support Markdown ↓</a></p><p><a href="pratique.zip" download>Projet et notebooks ↓</a></p></aside><div class="content-column"><div id="slides">${articles}</div><nav class="card-controls" aria-label="Navigation des slides"><button class="button" id="previous" disabled>← Précédente</button><span class="page-number" id="page-number" aria-hidden="true">01 / ${total}</span><button class="button primary" id="next">Suivante →</button></nav><p class="neutral-note">Les corrections des exercices s'ouvrent au clic. Le corrigé de l'examen est remis séparément.</p></div></div></main>${footer()}<script src="../assets/slides.js" defer></script></body></html>\n`);
  manifest.push({...meta, file:meta.id+'.html', slides:total});
}
for (const m of config.modules) deck(m);
deck({id:'programme', titre:'Le programme sur deux semaines', repere:'Organisation · Antoine et Michel', objectif:'Séances, jalons, examen et livrables.'}, true);

function card(m, output=path.join(base,'index.html')) {
  return `<a class="path-card course-card" data-course="maths-ia/${m.id}" href="${relative(output,path.join(base,m.id+'.html'))}"><span class="card-top"><span class="step-number">${String(config.modules.findIndex(x=>x.id===m.id)+1).padStart(2,'0')}</span><span class="pill">${esc(m.repere)}</span></span><h3>${esc(m.titre)}</h3><p>${esc(m.objectif)}</p><span class="card-bottom">${manifest.find(x=>x.id===m.id).slides} slides <span aria-hidden="true">Ouvrir →</span></span></a>`;
}
const sections = [1,2].map(semaine => `<section class="home-path-section"><div class="section-heading"><div><p class="eyebrow">Semaine ${semaine}</p><h2>${semaine===1?'Comprendre avant d’apprendre':'Apprendre, contrôler et évaluer'}</h2></div><p>${semaine===1?'Deux séances de maths, une introduction au réseau, puis le devoir.':'Trois séances de maths, puis entraînement et évaluation avec Michel.'}</p></div><nav class="path-grid" aria-label="Séances de semaine ${semaine}">${config.modules.filter(m=>m.semaine===semaine).map(m=>card(m)).join('')}</nav></section>`).join('');
fs.writeFileSync(path.join(base,'index.html'), `${head(config.titre)}<body>${header()}<main class="home" id="contenu"><div class="course-intro"><p class="eyebrow">Deux semaines · Antoine et Michel</p><h1>Comprendre.<br>Construire.<br>Évaluer.</h1><p>Des calculs d'un modèle linéaire au bilan d'un petit réseau, avec le même projet de consommation simulée.</p><div class="actions"><a class="button primary" href="01_representer.html">Commencer le parcours →</a><a class="button" href="programme.html">Voir l'organisation</a><a class="button" href="pratique.zip" download>Projet et notebooks ↓</a></div></div>${sections}<aside class="project-banner"><div><p class="eyebrow">Après l'introduction de Michel · Semaine 1</p><h2>Un examen individuel de 3 h.</h2><p>1 h 30 de mathématiques, 30 min d'IA et 1 h de pratique Python. Le sujet porte sur les trois premières séances ; le corrigé est remis séparément.</p></div><div class="project-actions"><a class="button primary" href="examen.html">Lire le sujet →</a><a href="examen-etudiant.zip" download>Fichiers étudiants ↓</a></div></aside></main>${footer()}</body></html>\n`);

const examSource=path.join(base,'evaluation/sujet.md'), examFile=path.join(base,'examen.html');
const examBody=render(examSource,examFile).map(s=>`<section class="exam-part">${s}</section>`).join('\n');
fs.writeFileSync(examFile, `${head('Examen individuel · 3 h', '<style>.exam-page{max-width:960px;margin:auto;padding:30px 5%}.exam-part{margin-bottom:48px}.exam-part h1,.exam-part h2{line-height:1.25}@media print{.site-header,.site-footer,.exam-actions{display:none}.exam-page{max-width:none;padding:0}.exam-part{break-before:page}.exam-part:first-child{break-before:auto}}</style>')}<body>${header()}<main class="exam-page" id="contenu"><div class="actions exam-actions"><button class="button primary" onclick="window.print()">Imprimer le sujet</button><a class="button" href="examen-etudiant.zip" download>Fichiers étudiants ↓</a><a href="evaluation/sujet.md" download>Sujet Markdown ↓</a></div><article class="prose">${examBody}</article></main>${footer()}</body></html>\n`);

for (const [fileName, targetDir] of [['pratique.zip','pratique'],['examen-etudiant.zip','evaluation']]) {
  execFileSync('python3',['-c',`from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import sys
source=Path(sys.argv[1])
with ZipFile(sys.argv[2], 'w', ZIP_DEFLATED) as z:
 for p in sorted(source.rglob('*')):
  if p.is_file() and not any(part in ('__pycache__','.ipynb_checkpoints') for part in p.parts):
   z.write(p, source.name+'/'+p.relative_to(source).as_posix())
`,path.join(base,targetDir),path.join(base,fileName)]);
}

for (const name of ['index.html','stat/index.html']) {
  const output = path.join(docs,name);
  let html=fs.readFileSync(output,'utf8')
    .replace(/<!-- maths-ia intro start -->[\s\S]*?<!-- maths-ia intro end -->/g,'')
    .replace(/<!-- maths-ia practice start -->[\s\S]*?<!-- maths-ia practice end -->/g,'')
    .replace(/<a class="button maths-ia-link"[^>]*>[\s\S]*?<\/a>/g,'')
    .replace(/<a href="#decouvrir-reseaux">[\s\S]*?<\/a>/g,'');
  const programmeHref=relative(output,path.join(base,'index.html'));
  const semaines=[1,2].map(semaine => {
    const cours=config.modules.filter(m=>m.semaine===semaine).map(m=>card(m,output)).join('');
    const examen=semaine===1?`<div class="project-banner"><div><p class="eyebrow">Fin de semaine 1</p><h3>Examen individuel de 3 h</h3><p>1 h 30 de mathématiques, 30 min d'IA et 1 h de pratique Python.</p></div><div class="project-actions"><a class="button" href="${relative(output,path.join(base,'examen.html'))}">Ouvrir le sujet →</a><a href="${relative(output,path.join(base,'examen-etudiant.zip'))}" download>Fichiers étudiants ↓</a></div></div>`:'';
    return `<h3>Semaine ${semaine} · ${semaine===1?'Comprendre et construire':'Entraîner et évaluer'}</h3><nav class="path-grid" aria-label="Cours maths et IA de semaine ${semaine}">${cours}</nav>${examen}`;
  }).join('');
  const intro=`<!-- maths-ia intro start --><section class="home-path-section" id="decouvrir-reseaux"><div class="section-heading"><div><p class="eyebrow">02 bis / Le cours maths et IA</p><h2>Des mathématiques aux réseaux de neurones</h2></div><p>Le cours détaillé sur deux semaines, avec Antoine et Michel. Décrire les données et dériver une erreur avant le premier réseau, puis étudier le gradient avant son entraînement.</p></div><div class="actions"><a class="button" href="${relative(output,path.join(base,'programme.html'))}">Programme et répartition des séances →</a><a class="button" href="${relative(output,path.join(base,'pratique.zip'))}" download>Projet et notebooks ↓</a></div>${semaines}</section><!-- maths-ia intro end -->`;
  // Le catalogue complet contient le bloc 02 ; la page de statistiques commence au bloc 03.
  const apres=name==='index.html'?'algebre':'statistiques';
  const ancre=new RegExp('(<section class="home-path-section" id="'+apres+'">[\\s\\S]*?<\\/section>)');
  if (!ancre.test(html)) throw new Error(`Section ${apres} absente de ${name}`);
  html=html.replace(ancre, '$1'+intro);
  const lien=new RegExp('(<a href="#'+apres+'">[\\s\\S]*?<\\/a>)');
  html=html.replace(lien, '$1<a href="#decouvrir-reseaux">Maths et IA</a>');
  html=html.replace('<div class="actions">', `<div class="actions"><a class="button maths-ia-link" href="${programmeHref}">Le parcours sur deux semaines →</a>`);
  fs.writeFileSync(output,html);
}
fs.writeFileSync(path.join(base,'manifest.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(`Maths & IA : ${config.modules.length} séances détaillées, ${manifest.reduce((a,m)=>a+m.slides,0)} slides, programme, examen et deux archives étudiants.`);
