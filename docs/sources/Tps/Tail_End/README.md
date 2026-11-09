# Quatre problèmes — Compter les occasions

## Une autre façon de regarder le temps

Dans [*The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html), Tim Urban propose de compter les activités et les rencontres plutôt que les seules années. Ces quatre problèmes originaux reprennent cette idée comme point de départ mathématique. Leurs personnages, données, modèles et dessins sont créés pour le cours.

Les horizons sont des hypothèses de scénario. Ils ne sont ni des prévisions individuelles de durée de vie, ni une manière d'attribuer une valeur aux personnes ou aux relations. Les élèves peuvent remplacer les situations par des activités fictives équivalentes.

## Où les placer dans le parcours ?

| Problème | Après quel cours ? | Question mathématique |
|---|---|---|
| [1 — La moitié des années, combien de rencontres ?](01_rencontres.md) | Révisions d'algèbre | Produits, pourcentages, unités et changement de dénominateur |
| [2 — Et si les occasions devenaient moins fréquentes ?](02_frequence.md) | Dérivation | Exponentielle, fréquence, cumul et dérivée |
| [3 — Une rencontre peut-elle disparaître dans 99 % de variance ?](03_evenement_rare.md) | SVD, après statistiques et ACP | Centrage, projection, reconstruction et choix de métrique |
| [4 — Vingt-quatre demi-journées à répartir](04_planning.md) | Optimisation et régularisation | Contrainte linéaire, concavité et optimum entier |

## Méthode commune

Écrire les hypothèses, nommer les unités, prédire l'allure du résultat, puis calculer. Lire le graphique avant de conclure. Distinguer enfin ce qui découle du calcul et ce qui dépend du scénario choisi.

Chaque problème fournit un énoncé, des indices gradués, des critères de réussite et une correction dépliable. Le code commun [tail_end.py](../../Projet_IA/tail_end.py) vérifie les résultats numériques des quatre problèmes. Il est également inclus dans l'archive du [projet fil rouge](../../Projet_IA/README.md).

## Lien avec la data et l'IA

Le premier problème travaille la définition des indicateurs. Le deuxième montre qu'extrapoler une fréquence exige un modèle. Le troisième sépare fidélité statistique et information utile. Le dernier rend visibles un objectif, ses contraintes et ses hypothèses de préférence.

Dans les quatre cas, un résultat numérique ne suffit pas : il faut expliquer ce qui a été mesuré et ce qui n'a pas été modélisé.

Les six problèmes « Penser autrement » complètent cette série : minutes cumulées, Simpson, attente du bus, dîner à dix, Braess et fausses alertes. [Ouvrir le catalogue des dix problèmes](../../docs/problemes.html).
