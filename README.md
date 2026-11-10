# Le labo maths — CODA

Cette branche **`maths-ia`** affiche les huit chapitres du [cours détaillé directement après « 02 / Représenter et ajuster »](docs/index.html#decouvrir-reseaux). Le [parcours maths et IA](docs/maths-ia/index.html) regroupe aussi les supports, les travaux pratiques et un [examen individuel de 3 h](docs/maths-ia/examen.html). Les fichiers étudiants sont distribuables ; le corrigé d'examen reste dans le dossier local non versionné de la sandbox.

Le cours antérieur est conservé sur `main`. Le repère local `cours-avant-maths-ia` inclut aussi les dernières corrections de révision présentes au début de cette mise à jour. Les fichiers propres au nouveau parcours sont contenus dans `docs/maths-ia/` et versionnés sur cette branche.

Un parcours de mathématiques pour comprendre les données et l'IA : révisions d'algèbre, fonctions, dérivation, matrices, statistiques, probabilités, ACP, optimisation et réseaux de neurones.

Le catalogue initial comprend 27 présentations, des figures, dix problèmes et un projet fil rouge avec données simulées, code Python et notebooks. Deux ateliers complètent ses six jalons : groupes et symétries, puis clustering des journées avec k-means. La branche maths-ia y ajoute huit chapitres sur les mathématiques et les réseaux de neurones.

## Consulter les cours

Ouvrir [le parcours](docs/index.html), [les problèmes](docs/problemes.html) ou [les exercices et ressources](docs/ressources.html).

Le dossier `docs/` est autonome : les styles, les figures et les polices mathématiques sont inclus. Les présentations fonctionnent sans installation, y compris hors ligne. Les liens vers des références externes nécessitent une connexion.

## Consultation en local

Ouvrir `docs/index.html` dans un navigateur.

Pour servir les pages localement, depuis le dossier qui contient `docs/` :

```sh
python3 -m http.server 8080 --directory docs
```

Puis ouvrir <http://localhost:8080>.

## Publier avec GitHub Pages

Ce dépôt de publication contient uniquement `README.md` et le dossier `docs/` complet. Les fichiers de travail restent dans le projet local.

Après avoir envoyé la branche `main` sur GitHub, ouvrir **Settings → Pages**, choisir **Deploy from a branch**, puis la branche **main** et le dossier **/docs**. Enregistrer pour lancer la publication, puis reprendre l'adresse affichée par GitHub Pages.

Le fichier `docs/.nojekyll` permet de publier directement les fichiers HTML déjà générés. Aucune compilation n'est nécessaire sur GitHub.

Voir la [documentation GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Utiliser les présentations

- Flèches gauche et droite : changer de slide.
- Sommaire : accéder à une slide et partager son lien.
- Lecture continue : afficher tout le chapitre.
- Imprimer / PDF : exporter le chapitre ; les corrections sont dépliées pour l'impression.
- Source Markdown : récupérer le contenu du support.

Les détails du parcours et des supports sont dans [docs/README.md](docs/README.md). La charte graphique est adaptée du [labo Matplotlib](https://antoine07.github.io/Matplotlib/).

## Reconstruire la variante maths-ia

Dans le projet de travail complet, reconstruire le catalogue historique, puis appliquer l'extension propre à cette branche :

```sh
npm run build
node docs/maths-ia/build.cjs
npm run check
```

Le second programme génère les nouveaux supports, les archives étudiants et l'insertion des huit séances après le bloc 02 de l'accueil. Il est réexécutable sans dupliquer les cartes. `python docs/maths-ia/verifier.py` contrôle les exemples, l'examen et la progression ; l'exécuter dans la sandbox équipée de PyTorch.
