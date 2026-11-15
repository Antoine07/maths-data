# Parcours de la branche maths-ia

Ouvrir `index.html` ou `examen.html`. Les pages sont autonomes avec les styles et polices du dossier parent.

## Contenu

- Huit chapitres : des bases mathématiques à l’entraînement et à l’évaluation des réseaux de neurones.
- Trois exercices progressifs corrigés, cinq questions de révision et cinq QCM par chapitre.
- Propagation avant introduite après les statistiques, avant l'étude approfondie du gradient.
- Un notebook et le même jeu de 240 journées simulées pour le projet fil rouge.
- Un devoir individuel portant sur les trois premiers chapitres : 90 minutes de maths, 30 minutes d'IA et 60 minutes de pratique Python.
- Sujet, données, script et notebook de départ dans l'archive `examen-etudiant.zip`.

Les corrigés du cours sont dépliables. Le corrigé de l'examen et son barème détaillé ne sont pas publiés ; ils sont conservés localement dans `sandbox_jupyter/correction/maths-ia/`.

## Modifier et reconstruire

Les Markdown de `supports/` font référence ; `parcours.json` définit la progression. Le sujet est `evaluation/sujet.md`. Exécuter `node docs/maths-ia/build.cjs` depuis la racine du dépôt après une modification.

Après `npm run build`, relancer ce générateur pour réappliquer l'insertion des nouvelles cartes sur l'accueil et la page statistiques. Le catalogue historique et son générateur restent utilisables sur l'ancienne branche.

## Vérifier

Dans la sandbox équipée de PyTorch, lancer `python /workspace/docs/maths-ia/verifier.py`. Les snippets sont exécutés, les conventions de perte et les formes sont contrôlées, ainsi que les partitions, les archives et le barème global.

Les figures sont calculées avec `python docs/maths-ia/figures.py` dans ce même environnement. Les SVG pédagogiques de réseau et de partitions sont des dessins vectoriels décrits dans leurs textes alternatifs.

Quatre graphiques supplémentaires accompagnent les questions d’observation : activations, effet du poids et du biais, frontières sur XOR et choix d’un état sur validation. Les réponses sont dépliables. Ils se régénèrent avec `python docs/maths-ia/graphiques_reseaux.py` (NumPy et Matplotlib). L’exemple XOR utilise des paramètres fournis ; l’arrêt sur validation est illustré par une descente calculée sur quatre observations, distinctes du fil rouge. Les courbes binaires du projet proviennent de `figures.py`.
