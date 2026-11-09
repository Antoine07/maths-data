# Le labo maths — CODA

Un parcours de mathématiques pour comprendre les données et l'IA : révisions d'algèbre, fonctions, dérivation, matrices, statistiques, probabilités, ACP, optimisation et réseaux de neurones.

Le support comprend 27 présentations, des figures, dix problèmes et un projet fil rouge avec données simulées, code Python et notebooks. Deux ateliers complètent ses six jalons : groupes et symétries, puis clustering des journées avec k-means.

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
