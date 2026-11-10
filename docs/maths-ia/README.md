# Parcours de la branche maths-ia

Ouvrir `index.html`, `programme.html` ou `examen.html`. Les pages sont autonomes avec les styles et polices du dossier parent.

## Contenu

- Huit séances : cinq de mathématiques avec Antoine, trois de réseaux avec Michel.
- Trois exercices progressifs corrigés, cinq questions de révision et cinq QCM par séance.
- Propagation avant introduite après les statistiques, avant l'étude approfondie du gradient.
- Un notebook et le même jeu de 240 journées simulées pendant les deux semaines.
- Un devoir individuel après l'introduction de Michel, en première semaine : 90 minutes de maths, 30 minutes d'IA et 60 minutes de pratique Python.
- Sujet, données, script et notebook de départ dans l'archive `examen-etudiant.zip`.

Les corrigés du cours sont dépliables. Le corrigé de l'examen et son barème détaillé ne sont pas publiés ; ils sont conservés localement dans `sandbox_jupyter/correction/maths-ia/`.

## Modifier et reconstruire

Les Markdown de `supports/` font référence ; `parcours.json` définit la progression. Le sujet est `evaluation/sujet.md`. Exécuter `node docs/maths-ia/build.cjs` depuis la racine du dépôt après une modification.

Après `npm run build`, relancer ce générateur pour réappliquer l'insertion des nouvelles cartes sur l'accueil et la page statistiques. Le catalogue historique et son générateur restent utilisables sur l'ancienne branche.

## Vérifier

Dans la sandbox équipée de PyTorch, lancer `python /workspace/docs/maths-ia/verifier.py`. Les snippets sont exécutés, les conventions de perte et les formes sont contrôlées, ainsi que les partitions, les archives et le barème global.

Les figures sont calculées avec `python docs/maths-ia/figures.py` dans ce même environnement. Les SVG pédagogiques de réseau et de partitions sont des dessins vectoriels décrits dans leurs textes alternatifs.

Le programme compte l'examen de 3 h et son retour de 30 minutes dans les 21 h d'Antoine. Michel intervient 3 h 30 en semaine 1 puis 7 h en semaine 2. Le détail des créneaux est dans `programme.html`.
