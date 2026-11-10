# Le labo maths — CODA

Sur la branche **maths-ia**, les huit séances du cours sont visibles directement dans [l'accueil, après « 02 / Représenter et ajuster »](index.html#decouvrir-reseaux), dans le bloc « 02 bis / Le cours maths et IA ». Elles suivent l'ordre des deux semaines, avec le programme Antoine/Michel, le notebook fil rouge et l'examen de première semaine. Le [parcours sur deux semaines](maths-ia/index.html) reste aussi accessible en page dédiée. Les statistiques précèdent le premier réseau ; le gradient et l'optimisation précèdent son entraînement.

La répartition de l'examen est 90 minutes de mathématiques, 30 minutes d'IA et 60 minutes de pratique Python, sur 20 points. L'épreuve précède les contenus avancés de semaine 2 et ne les évalue pas. Le corrigé reste local dans `sandbox_jupyter/correction/maths-ia/`, absent de cette distribution et des archives étudiants.

Ouvrir `index.html` dans un navigateur. Le dossier `docs/` peut aussi être publié tel quel avec GitHub Pages.

Ce dossier est la distribution autonome des supports. Les instructions de génération ci-dessous concernent le projet de travail complet : les scripts de construction et les originaux ne sont pas inclus dans le dépôt de publication. Les copies Markdown consultables sont livrées dans `sources/`.

Les 27 présentations du catalogue initial reprennent les sources de `Slides/` et les supports HTML historiques. Huit chapitres avancés relient l'algèbre et l'analyse à l'apprentissage automatique ; un court support de probabilités prépare les nouveaux problèmes. Les TP et corrections sont accessibles depuis « Exercices & ressources ».

Les nouveaux contenus sont intercalés dans le parcours : géométrie et moindres carrés après les matrices ; SVD après les statistiques et l'ACP ; calcul différentiel, optimisation et rétropropagation après le gradient. Le projet de consommation électrique se télécharge avec son CSV, son code et ses notebooks depuis la page des ressources.

« Groupes, symétries et données » s'insère après le calcul matriciel : rotations du carré, composition, inverses, invariance et équivariance, puis contrôle du réordonnement des lignes du projet. Une ouverture reprend ces notions après la rétropropagation. « Clustering et profils de consommation » suit la SVD : k-means en NumPy, mise à l'échelle, inertie, plusieurs départs et interprétation prudente. Chaque chapitre comprend trois exercices corrigés et cinq QCM. Les scripts `projet-ia/groupes_symetries.py` et `projet-ia/clustering.py` sont inclus dans l'archive ; les six jalons du projet restent complétés par ces deux ateliers. Le fil rouge reste en fin de page d'accueil.

Les révisions commencent par deux paniers : trois produits à 50 € et cinquante produits à 3 €. La comparaison introduit la commutativité et l'idée de choisir une écriture qui simplifie le calcul. L'associativité et la distributivité prolongent cette ouverture avec trois calculs à expliquer et une correction dépliable.

Les révisions comprennent aussi deux démonstrations guidées : le crible d'Ératosthène après les priorités de calcul, puis la somme de deux entiers pairs après la factorisation. Chaque activité propose des indices et une correction dépliable. Le programme Python du crible et la preuve Lean 4 avec Mathlib sont disponibles dans `exemples/revision/`. La grille du crible reste compacte et peut s'ouvrir en grand.

La partie sur les nombres premiers distingue les diviseurs premiers des diviseurs premiers stricts : pour 7, les ensembles sont respectivement `{7}` et l'ensemble vide. Une preuve par contradiction relie ce critère au contrôle jusqu'à la racine carrée. Le script `exemples/revision/primalite.py` teste un entier, compte les divisions et permet d'observer la complexité en `O(racine(N))` tests dans le pire cas. Les exemples incluent 1, 2 et les carrés 49 et 121.

Les supports incluent 28 figures SVG générées avec Matplotlib : tangentes, limites, transformations, résidus, ACP, courbure, optimisation, classification, rotations, clustering et problèmes. Cliquer sur une figure permet de l'ouvrir en grand.

Cinq graphiques supplémentaires accompagnent les exemples corrigés de fonctions : extrema locaux, quotient, composition, exercices d'extremums et température simulée. L'exercice de température relie période et fréquence, distingue écart-type et variance, et explicite les limites du modèle. Les scripts reproductibles et leur vérification sont dans [exemples/fonctions](exemples/fonctions/).

Huit illustrations compactes accompagnent les couvertures Matrices, Gradient, Statistiques, Corrélation, Centrage-réduction, ACP, Probabilités et Réseau. Sept dessins complètent les transformations, les limites, l'histogramme, la boîte à moustaches et les degrés de liberté. Leur hauteur est plafonnée dans la page : 220 px pour les couvertures et 250 px pour ces dessins de cours, puis 150 et 190 px sur mobile. Les SVG restent accessibles en grand au clic.

Le chapitre de statistiques descriptives part du besoin d'échantillonner et distingue description, estimation, sélection et fluctuation. Il explique ensuite la contrainte de somme nulle des écarts centrés, les `n−1` degrés de liberté et la correction d'estimation de variance. Une démonstration et l'énumération de 64 échantillons indépendants avec remise justifient la correction avant l'introduction de `ddof`. Le cas d'une vraie moyenne connue est distingué du centrage sur une moyenne estimée.

Les dix problèmes sont accessibles par des cartes lavande insérées après leur cours associé, avec question, notions, prérequis et bouton d'accès. `problemes.html` les regroupe ; les liens depuis les slides permettent de les retrouver au moment utile. Les quatre problèmes « Compter les occasions » sont complétés par six situations : minutes cumulées, Simpson, bus, dîner, Braess et fausses alertes. La configuration éditoriale des cartes se trouve dans `../scripts/data/problems.json`.

## Utilisation

- Flèches gauche et droite : changer de slide.
- Sommaire : accéder directement à une slide ; son numéro est conservé dans l’URL.
- Lecture continue : afficher tout le chapitre.
- F : passer en plein écran lorsque le navigateur le permet ; Échap pour quitter.
- Imprimer / PDF : exporter toutes les slides du chapitre, avec les corrections dépliées.
- Source Markdown : télécharger le fichier original.

Sur mobile, ouvrir le bouton « Sommaire » pour consulter la liste des slides. Sans JavaScript, toutes les slides restent visibles.

## Génération

Depuis la racine du projet :

```sh
npm install
npm run build
node docs/maths-ia/build.cjs
npm run check
npm run check:ia
npm run check:figures
npm run check:problemes
npm run check:statistiques
```

La génération fonctionne aussi avec une installation globale de Marp CLI fournissant `@marp-team/marp-core`. Les fichiers générés s’ouvrent directement, sans installation.

La commande `node docs/maths-ia/build.cjs` concerne cette branche uniquement. Elle s'exécute après le générateur historique. Les supports Markdown modifiables de cette extension sont dans `maths-ia/supports/` ; son manifeste et son générateur sont versionnés avec elle. Un retour à l'ancienne branche restaure les anciennes pages, sans dépendre d'une modification des scripts de travail locaux.

Pour régénérer les courbes et illustrations, installer `../scripts/requirements-figures.txt` avec pip puis lancer `npm run figures` et `npm run illustrations` depuis la racine, avant `npm run build`. Matplotlib n'est pas nécessaire pour consulter les figures livrées ni pour reconstruire le HTML à partir des SVG existants.

Pour un aperçu avec un serveur local :

```sh
npm run preview
```

Puis ouvrir `http://localhost:8080`.

## Sources et style

La charte est adaptée du [labo Matplotlib](https://antoine07.github.io/Matplotlib/) : fond crème, verts foncés, accents citron, cartes arrondies et code sur fond sombre. Le fichier `assets/site.css` provient de la copie locale du projet de référence ; `assets/slides.css` adapte cette charte aux présentations de mathématiques.

Les fichiers Markdown font référence pour les contenus ; leurs copies sous `sources/` sont identiques aux fichiers du projet au moment de la génération. Modifier le Markdown puis reconstruire permet de conserver les pages HTML à jour. Les délimiteurs mathématiques anciens sont normalisés uniquement au moment du rendu. Les supports historiques sans source Markdown correspondante, `calcul_matriciel.html` et `modelisation.html`, sont conservés dans `../scripts/data/legacy-slides.json` pour permettre une reconstruction complète.

Les formules, les polices KaTeX, les figures et les styles sont locaux. Les illustrations web du chapitre covariance/ANOVA/ACP ont été remplacées par des figures originales calculées, dont les légendes distinguent les données du projet et les exemples illustratifs.

`npm run check` vérifie les liens locaux, les ancres, les formules, les fichiers de style, la structure de navigation, la syntaxe JavaScript, l'ordre des prérequis et l'intégrité des copies des sources. `npm run check:ia` exécute les exemples NumPy des huit chapitres, les ateliers, le notebook corrigé et les contrôles numériques du projet, y compris depuis l'archive téléchargée. Ces contrôles ne remplacent pas une vérification visuelle dans un navigateur.
