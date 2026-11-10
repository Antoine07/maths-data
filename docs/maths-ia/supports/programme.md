---
marp: true
html: true
---

# Des mathématiques aux réseaux de neurones

Deux semaines · Antoine et Michel · un projet de consommation simulée.

Les réseaux sont introduits **après « 03 / Décrire et interpréter »**, puis leur apprentissage est approfondi après le gradient et l'optimisation.

---

## Objectif du parcours

Comprendre les calculs d'un modèle, préparer les données, expliquer l'apprentissage et produire un bilan argumenté d'un petit réseau.

Le public doit connaître les bases de Python. Un diagnostic initial porte sur variables, fonctions, tableaux et lecture de code. La sandbox prépare l'environnement ; l'évaluation ne mesure pas la capacité à installer les outils.

Les supports détaillés du catalogue général restent disponibles pour approfondir. Il n'est pas demandé de parcourir intégralement tous les chapitres avancés pendant ces deux semaines.

---

## Organisation et volume

| Intervention | Semaine 1 | Semaine 2 | Total |
|---|---|---|---|
| Antoine — mathématiques et devoir | 1,5 jour | 1,5 jour | 21 h |
| Michel — réseaux de neurones | 0,5 jour | 1 jour | 10 h 30 |
| Ensemble | 14 h | 17 h 30 | 31 h 30 |

Le devoir de 3 h et son retour de 30 minutes sont inclus dans les 21 h d'Antoine. Il reste cinq séances de mathématiques de 3 h 30. Si l'on souhaite 21 h d'enseignement en plus du devoir, il faut ajouter 3 h à ce calendrier.

Les durées figurent ici pour organiser l'intervention ; les chapitres ne présentent pas d'estimation de temps pour chaque activité.

---

## Semaine 1 — Représenter, comprendre et vérifier

| Créneau | Intervenant | Séance | Production |
|---|---|---|---|
| Jour 1 matin | Antoine | [Représenter et calculer](01_representer.md) | Prédictions matricielles et dimensions |
| Jour 1 après-midi | Antoine | [Décrire et dériver](02_decrire_deriver.md) | Statistiques, perte et premier pas |
| Jour 2 matin | Michel | [Comprendre le réseau](03_comprendre_reseau.md) | Propagation avant NumPy |
| Jour 2 après-midi | Antoine | Examen de 3 h, puis retour de 30 min | Travail individuel et diagnostic |

L'introduction de Michel précède l'examen pour que la partie IA porte sur un contenu effectivement enseigné. Aucun entraînement PyTorch ni calcul complet de rétropropagation n'est demandé dans ce devoir.

---

## Semaine 2 — Apprendre et évaluer

| Créneau | Intervenant | Séance | Production |
|---|---|---|---|
| Jour 1 matin | Antoine | [Préparer les données](04_preparer_donnees.md) | Partitions, échelles et cible |
| Jour 1 après-midi | Antoine | [Gradient et chaîne](05_gradient_chaine.md) | Gradient vérifié numériquement |
| Jour 2 matin | Antoine | [Optimiser](06_optimiser.md) | Descente, pénalité et protocole |
| Jour 2 après-midi | Michel | [Entraîner avec PyTorch](07_entrainer_pytorch.md) | Courbes et meilleur état |
| Jour 3 matin | Michel | [Évaluer et argumenter](08_evaluer.md) | Bilan comparatif et explication |

La dernière séance inclut la finalisation du livrable et son explication. Elle n'ajoute pas une nouvelle demi-journée d'évaluation.

---

## Ce qu'Antoine transmet à Michel

Après la première semaine : formes de X et des poids, calcul d'une fonction affine, statistiques descriptives, perte et notion de dérivée.

Après la reprise de semaine 2 : partitions fixées, paramètres de standardisation, cible de classification, convention de perte et de pénalité, gradient et règle de mise à jour.

Michel reprend ces objets pour construire puis entraîner le même modèle. Il n'a pas à refaire un cours complet de dérivation ; il fait expliquer ce que les opérations PyTorch automatisent.

---

## Déroulé de la séance Maths A

Commencer par le diagnostic et les deux paniers 3×50 et 50×3. Relier les propriétés de calcul à une fonction affine, puis à plusieurs caractéristiques.

Passer des observations au tableau X. Lire les dimensions avant de calculer. Faire une prédiction à la main, puis vérifier avec NumPy.

Les trois exercices font lire une forme, interpréter poids et biais, puis corriger un produit élément par élément. Le notebook du fil rouge reçoit sa première fonction de prédiction.

---

## Déroulé de la séance Maths B

Décrire quelques valeurs à la main avant d'utiliser moyenne et écart-type. Distinguer la description du groupe observé et les conclusions sur des journées futures.

Construire une perte à partir de résidus qui s'annulent en moyenne. Dériver une petite perte à un paramètre et vérifier l'effet d'une mise à jour.

Faire expliciter le signe de la dérivée et le sens de déplacement. L'exercice de débogage prépare les erreurs de formes et de perte du devoir.

---

## Déroulé de la séance Michel 1

Reprendre les entrées et les poids sous forme matricielle. Introduire biais et activation, puis composer deux couches et suivre les formes.

Faire calculer un neurone et un petit réseau à la main. Visualiser l'effet d'une activation et utiliser XOR comme illustration, sans lancer un deuxième projet complet.

Écrire la propagation avant NumPy et distinguer logit, probabilité et décision. La question « comment choisir les poids ? » ouvre la semaine suivante.

---

## Déroulé des trois séances Maths de semaine 2

**Préparer :** partir des erreurs du devoir, fixer les rôles des partitions, apprendre les échelles sur train et contrôler une nouvelle journée. Séparer le seuil de consommation du seuil de probabilité.

**Différencier :** passer d'une dérivée à deux paramètres, suivre la chaîne dans un réseau scalaire et comparer avec des différences finies. Chaque formule est rattachée à ses dimensions et à sa convention de perte.

**Optimiser :** comparer plusieurs pas sur une parabole, ajouter une contribution L2 et définir à l'avance la sélection sur validation. Remettre à Michel un protocole écrit, pas seulement un jeu de poids.

---

## Déroulé des deux séances Michel de semaine 2

**Entraîner :** retrouver les calculs NumPy dans les tenseurs ; expliquer `Linear`, la perte sur logits et l'ordre `zero_grad → backward → step`. Tracer apprentissage et validation, puis restaurer le meilleur état.

**Évaluer :** figer les réglages, produire les métriques et comparer majorité, logistique et réseau. Faire commenter les faux positifs, les faux négatifs et la saisonnalité simulée.

Chaque groupe doit pouvoir expliquer une ligne de code, un choix de protocole et une limite de sa conclusion.

---

## Projet fil rouge — Contexte et données

Une équipe énergétique veut représenter les journées, prévoir une consommation puis classifier une forte demande. Les 240 journées sont entièrement simulées.

Entrées : température, occupation, équipements. Consommation : cible de régression puis construction de la classe ; jamais une entrée du classificateur.

Partitions chronologiques : 144 journées d'apprentissage, 48 de validation et 48 de test. La variation saisonnière limite l'interprétation et fait partie du bilan.

L'architecture attendue reste un même notebook avec des fonctions de chargement, préparation, prédiction, perte, entraînement et évaluation. Le fichier `depart.py` évolue ; on ne redémarre pas huit projets.

---

## Projet fil rouge — Jalons et critères

| Séance | Fonctionnalité | Résultat vérifiable | Erreur à observer |
|---|---|---|---|
| Maths A | Prédire avec Xw+b | Une sortie par ligne | Produit élément par élément |
| Maths B | Décrire et calculer une perte | Moyennes, MSE et pas commentés | Erreurs signées qui s'annulent |
| Michel 1 | Propagation avant | Logits et probabilités de bonnes formes | Activation réduite en scalaire |
| Maths C | Préparer sans fuite | Paramètres appris sur 144 lignes | Échelles apprises sur test |
| Maths D | Vérifier un gradient | Accord numérique sur un petit cas | Convention de perte oubliée |
| Maths E | Définir l'optimisation | Grille et règle d'arrêt annoncées | Réglage choisi sur test |
| Michel 2 | Entraîner et conserver | Courbes et meilleur état | Gradients accumulés par erreur |
| Michel 3 | Évaluer et expliquer | Bilan comparatif relançable | Réseau déclaré meilleur par principe |

---

## Évaluation de première semaine

Le [sujet](../evaluation/sujet.md) est individuel et porte uniquement sur les trois premières séances.

Répartition retenue pour les 3 h : **1 h 30 de mathématiques, 30 min d'IA et 1 h de pratique Python et interprétation**. L'heure de pratique complète les deux durées disciplinaires, qui totalisent 2 h.

Barème : 10 points de mathématiques, 4 d'IA et 6 de pratique, soit 20 points. Les calculs justifiés et l'interprétation comptent autant que l'exécution.

Le sujet et les fichiers de départ sont distribuables. La correction et la grille détaillée sont conservées dans le dossier local non versionné `sandbox_jupyter/correction/maths-ia/`.

---

## Livrable de fin de semaine 2

Le notebook doit se relancer dans l'ordre et produire : dimensions, unités et partitions ; contrôle d'une dérivée ; transformations apprises sur train ; courbes train/validation ; choix de réglages ; comparaison majorité/logistique/réseau ; matrices de confusion et limites.

Critères : exactitude des calculs, protocole sans fuite, traçabilité des choix, lisibilité du code et qualité de l'explication. Aucune supériorité du réseau n'est exigée.

Les extensions facultatives sont les mini-lots, d'autres graines et une visualisation ACP. Groupes, crible, Lean, SVD et clustering restent accessibles depuis le catalogue général et ne sont pas évalués dans ce devoir.

---

## Fiche de liaison et bilan

Avant l'examen, chacun doit pouvoir calculer une prédiction, une moyenne, une perte, une dérivée simple et une propagation avant.

Avant l'entraînement PyTorch, chacun doit pouvoir expliquer les partitions, le gradient, la chaîne et la mise à jour.

Au bilan, chacun doit distinguer un calcul correct, un réglage sélectionné et une conclusion soutenue par l'évaluation.

[Commencer la première séance](01_representer.md).
