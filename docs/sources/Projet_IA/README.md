# Projet fil rouge — Comprendre la consommation électrique

## Objectif

Faire évoluer le même projet pendant les six chapitres avancés : comparer des journées, prévoir leur consommation, explorer les directions des données, vérifier les gradients et entraîner des modèles.

Ce projet prolonge [le TP de modélisation de la consommation](../Slides/02_modelisation.md). Les 30 valeurs de ce TP restent dans leur source. Pour expérimenter avec plusieurs variables et un test réservé, on utilise ici une **nouvelle table de 240 journées entièrement simulées**. Les variables ajoutées ne sont pas des mesures reconstituées des 30 journées initiales.

## Contexte et utilisateurs

Une équipe de gestion énergétique souhaite estimer la consommation d'une journée et repérer à l'avance les journées de forte demande. Les résultats doivent être compréhensibles pour l'équipe technique.

## Problème à résoudre

Une simple tendance en fonction du jour ne décrit pas l'effet combiné de la température, de l'occupation et des équipements. Nous comparons plusieurs représentations et modèles en gardant les mêmes partitions.

Les données sont pédagogiques : aucune conclusion opérationnelle sur un bâtiment réel ne peut être tirée de leurs performances.

## Fonctionnalités cibles

1. Rechercher des profils comparables sans connaître leur consommation future.
2. Ajuster et contrôler une régression multivariée.
3. Analyser la possibilité d'une réduction de dimension.
4. Calculer puis vérifier la perte et les gradients.
5. Comparer résolution directe, descente et pénalité L2.
6. Comparer une classification logistique et un petit réseau.

Deux ateliers transversaux complètent les six jalons : vérifier la cohérence d'un réordonnement des journées et regrouper des profils sans utiliser leur consommation.

## Modèle de données ou objets principaux

Le fichier [consommation.csv](data/consommation.csv) contient :

| Colonne | Sens | Utilisation |
|---|---|---|
| `jour` | Ordre chronologique, de 1 à 240 | Partitionnement ; pas une caractéristique du modèle avancé |
| `temperature` | Température simulée, en °C | Caractéristique connue ou prévue avant la journée |
| `occupation` | Nombre d'occupants simulé, de 1 à 5 | Caractéristique |
| `equipements` | Indice d'intensité d'utilisation simulé, entre 1 et 5 | Caractéristique sans unité physique |
| `consommation` | Consommation simulée, en kWh | Cible de régression puis construction de l'étiquette |

La simulation inclut une composante non linéaire liée au chauffage et un bruit aléatoire. Cela ne garantit pas qu'un réseau soit meilleur que la logistique sur la tâche de classification choisie.

Partitions fixées : jours 1–144 pour l'apprentissage, 145–192 pour la validation, 193–240 pour le test. Leur ordre chronologique est conservé. La saisonnalité simulée crée des distributions différentes : commenter cette limite.

## Architecture attendue

Faire évoluer [depart.py](depart.py), ou le [notebook de départ](depart.ipynb), sans créer six projets indépendants.

Séparer progressivement les fonctions de chargement, transformation, prédiction, perte, gradient, apprentissage et évaluation. Sauvegarder la moyenne, l'écart-type et les paramètres avec le modèle : les poids seuls ne suffisent pas à reproduire les prédictions.

Le calcul obligatoire utilise seulement NumPy. Les visualisations et la comparaison PyTorch sont des extensions facultatives.

## Installation et exécution

Depuis le dossier `Projet_IA` :

```sh
python3 -m pip install -r requirements.txt
python3 depart.py
python3 correction.py --verifier
```

Le programme de correction utilise toujours les mêmes données et graines. Il écrit `resultats/bilan.json` et `resultats/modeles.npz` à côté du script, quel que soit le dossier depuis lequel il est lancé.

Pour télécharger le projet complet : [archive du fil rouge](projet_ia.zip). Décompresser l'archive avant d'exécuter le script, afin de conserver `data/consommation.csv` à sa place.

---

## Jalons reliés aux séances

### Jalon 1 — Géométrie des données

Après [Géométrie des données](../Slides/avance/01_geometrie_donnees.md).

**Notions mobilisées :** normes, distances, cosinus et échelles. **Fonctionnalité à produire :** chercher trois journées d'apprentissage proches de la première journée de validation, sans utiliser la consommation comme variable.

**Consigne :** fixer des échelles métier simples, annoncer la mesure et expliquer le premier résultat. Ne pas comparer une requête à elle-même dans l'ensemble des candidats.

**Résultat vérifiable :** trois identifiants distincts et des scores ordonnés. **Erreurs à observer :** confusion entre direction et valeur, absence de contrôle des vecteurs nuls.

**Livrable :** une fonction de voisinage et un tableau commenté. Revenir sur ce choix après l'introduction de la standardisation au jalon 3.

### Jalon 2 — Moindres carrés

Après [Régression multivariée](../Slides/avance/02_moindres_carres.md).

**Notions mobilisées :** matrice de conception, rang et orthogonalité des résidus. **Fonctionnalité :** ajuster trois poids et une constante sur l'apprentissage avec `lstsq`.

**Consigne :** vérifier les dimensions, calculer les résidus, puis comparer la RMSE de validation avec une référence prédisant la moyenne d'apprentissage. Aucun choix ne doit utiliser le test.

**Résultat vérifiable :** rang 4 et `A.T @ r` proche de zéro pour la solution non pénalisée. Ajouter temporairement une colonne dupliquée pour examiner la perte de rang.

**Livrable :** paramètres et diagnostic. **Erreurs à observer :** inverse explicite et interprétation causale des coefficients.

### Jalon 3 — SVD après les statistiques et l'ACP

Après [centrage-réduction](../Slides/stat/03_centrage_reduction.md), [ACP](../Slides/stat/04_acp_intro.md) et [SVD](../Slides/avance/03_svd_acp.md).

**Notions mobilisées :** standardisation, covariance, valeurs singulières et projection. **Fonctionnalité :** proposer une représentation à 95 % de variance et reconstruire les observations.

**Consigne :** apprendre moyenne et écart-type sur les 144 premières lignes ; appliquer les mêmes paramètres partout ; calculer les axes sur l'apprentissage. Recalculer les voisins du jalon 1 avec cette nouvelle géométrie.

**Résultat vérifiable :** les parts de variance sont environ 40,24 %, 33,96 % et 25,80 %. Trois axes restent nécessaires au seuil de 95 %. Le résultat « pas de compression » est correct.

**Livrable :** spectre, nombre d'axes, reconstruction et explication. **Erreurs à observer :** forcer deux axes, ajuster la moyenne sur toutes les lignes.

### Jalon 4 — Calcul différentiel

Après [gradient et Hessienne](../Slides/gradient.md), puis [Calcul différentiel matriciel](../Slides/avance/04_calcul_differentiel.md).

**Notions mobilisées :** perte moyenne, transposée et règle de chaîne. **Fonctionnalité :** calculer la perte quadratique et ses quatre dérivées.

**Consigne :** écrire une seule fonction renvoyant perte et gradient ; comparer avec des différences finies centrées sur chaque paramètre.

**Résultat vérifiable :** gradient `(4,)`, écart inférieur à `1e-7` au point de contrôle fourni, en précision double.

**Livrable :** code et explication des dimensions. **Erreurs à observer :** résidu de signe contraire, moyenne absente et diffusion automatique.

### Jalon 5 — Optimisation et régularisation

Après [Optimisation](../Slides/avance/05_optimisation.md).

**Notions mobilisées :** pas, courbure, L2 et sélection sur validation. **Fonctionnalité :** entraîner le modèle par descente et comparer à une solution directe.

**Consigne :** conserver le biais non pénalisé ; comparer `lambda` dans `[0, .001, .01, .1, 1]` ; choisir la RMSE de validation minimale. Figer les paramètres avant le test.

**Résultat vérifiable :** accord à `1e-6` entre descente complète et résolution directe du même objectif ; choix de `lambda=0.1` sur le fichier fourni. Une expérimentation à mini-lots doit commenter les oscillations.

**Livrable :** historique, tableau de sélection et paramètres sauvegardés. **Erreurs à observer :** comparaison de deux normalisations différentes et réglages sur le test.

### Jalon 6 — Classification et réseau

Après [Classification et rétropropagation](../Slides/avance/06_retropropagation.md).

**Notions mobilisées :** sigmoïde, perte binaire stable et chaîne de dérivation. **Fonctionnalité :** prévoir les journées dépassant la médiane de consommation d'apprentissage, sans fournir la consommation en entrée.

**Consigne :** comparer classe majoritaire, logistique et réseau à quatre neurones ; sélectionner les itérations sur la perte de validation et garder un seuil de probabilité fixé à 0,5. Contrôler numériquement les quatre tableaux de gradients.

**Résultat vérifiable :** gradients corrects à `1e-8` sur le petit exemple ; paramètres figés avant l'évaluation finale. La correction obtient 48/48 décisions correctes pour la logistique et 47/48 pour le réseau sur le petit test simulé.

**Livrable :** pertes de validation, matrices de confusion, fréquences des classes et commentaire des erreurs. **Erreurs à observer :** fuite de la cible, surinterprétation de 48 exemples et affirmation systématique que le réseau est meilleur.

---

## Ateliers transversaux

### Atelier A — Groupes, symétries et cohérence des lignes

Après [Groupes, symétries et données](../Slides/avance/07_groupes_symetries.md), puis en reprise après le réseau du jalon 6.

**Notions mobilisées :** composition, identité, inverse, invariance et équivariance. **Fonctionnalité à produire :** contrôler qu'une prédiction indépendante par ligne suit la permutation de cette ligne et que l'erreur moyenne ne change pas si les cibles suivent aussi.

**Consigne :** vérifier les quatre rotations de $C_4$ sur des coordonnées du plan, puis revenir à la table énergétique. Fixer les partitions chronologiques avant de permuter les seules lignes d'apprentissage. Réutiliser les mêmes colonnes dans le même ordre. Ne pas appliquer une rotation arbitraire aux colonnes température, occupation et équipements : elle ne conserve pas leur sens métier.

**Résultat vérifiable :** identité après quatre quarts de tour ; compositions et inverses corrects ; prédictions initiales retrouvées par la permutation inverse ; erreur identique avec les cibles alignées. **Erreurs à observer :** puissance coefficient par coefficient, cibles désalignées, confusion entre changement de représentation et changement de tâche.

**Livrable :** contrôles NumPy et deux exemples de transformations admissibles ou interdites. La [correction exécutable](groupes_symetries.py) utilise des poids fixés pour isoler le contrôle de cohérence : elle ne prétend pas ajuster un modèle prédictif.

### Atelier B — Clustering des journées après le jalon 3

Après [Clustering et profils de consommation](../Slides/avance/08_clustering.md).

**Notions mobilisées :** distance euclidienne, standardisation, centroïdes, inertie et alternance de Lloyd. **Fonctionnalité à produire :** apprendre des profils sur les jours 1–144 et affecter les jours 145–192 à ces profils.

**Consigne :** continuer `depart.py` en réutilisant son chargement et ses partitions. Choisir les seules colonnes température, occupation et équipements. Ajuster les échelles uniquement sur l'apprentissage ; traiter les colonnes constantes. Comparer $k=2,3,4$, plusieurs initialisations et des graines documentées. Garder le centre précédent en cas de cluster vide et signaler cette limite. Sur validation, appliquer les échelles et les centres figés, sans les réapprendre ; ne pas consulter le test pour régler l'atelier.

**Résultat vérifiable :** une étiquette par ligne, centres finis, historique d'inertie non croissant et affectations cohérentes avec les centres retournés. Examiner l'indicateur de convergence si la limite d'itérations est atteinte. Reconvertir les centres en °C, occupation et indice d'équipements pour les commenter. Comparer aussi les effectifs d'apprentissage et de validation : la saisonnalité simulée peut changer leur répartition.

**Livrable :** tableau pour les trois valeurs de $k$, effectifs, centres en unités initiales, graines et justification d'une description utile. **Erreurs à observer :** consommation incluse dans les distances, validation utilisée pour réajuster, numéros pris pour des niveaux ordonnés et plus grand $k$ choisi uniquement grâce à l'inertie. Il n'existe pas de « vrai k » imposé pour ces données.

La [correction exécutable](clustering.py) fournit `affecter`, `lloyd`, `kmeans` et un bilan des trois valeurs de $k$. Elle ne lit pas la consommation pour construire les groupes et ne consulte pas les journées de test.

Depuis le dossier décompressé `Projet_IA` :

```sh
python3 groupes_symetries.py
python3 clustering.py
```

**Extensions facultatives :** projeter les clusters avec l'ACP apprise au jalon 3 ; comparer les partitions à permutation de numéros près ; discuter les symétries du réseau après le jalon 6. L'ajout de ces ateliers conserve les six étapes du projet initial.

## Livrables

- Le même script ou notebook enrichi pendant les six étapes.
- Un tableau des transformations apprises et de leurs dimensions.
- Les résultats de contrôle des gradients et de reconstruction.
- Les erreurs de validation utilisées pour les choix.
- Les modèles figés et un compte rendu de l'évaluation finale.
- Une conclusion distinguant qualité numérique, qualité prédictive et limites des données simulées.

## Critères de validation

La solution doit se relancer avec le CSV fourni. Les partitions, graines, unités et conventions de perte sont explicites. Les transformations sont ajustées uniquement sur l'apprentissage ; le test ne sélectionne aucun réglage.

Les gradients analytiques et numériques concordent. Les résultats de régression sont comparés à une référence constante ; la classification est comparée à la classe majoritaire et à la logistique. Aucune amélioration du réseau n'est exigée.

## Correction expliquée

La [correction exécutable](correction.py) regroupe les six jalons dans l'ordre. Le [notebook de correction](correction.ipynb) permet d'examiner chaque étape séparément.

Lecture du code : `charger` fixe les partitions ; `ajuster_echelle` apprend les transformations ; `cout_gradient` implémente la perte du chapitre de calcul différentiel ; `descente` et `ridge` résolvent le même objectif ; `reseau_cout_gradients` applique la chaîne de dérivation. `main` assemble les jalons et consulte le test après la sélection.

Le fichier [bilan de référence](resultats/bilan.json) contient les valeurs obtenues sur le CSV fourni. De petits écarts d'arrondi sont possibles selon la bibliothèque numérique ; le signe des axes SVD peut aussi changer.

## Extensions facultatives

- Les [quatre problèmes Compter les occasions](../Tps/Tail_End/README.md) prolongent le cours avec d'autres situations. Le fichier [tail_end.py](tail_end.py), inclus dans l'archive, vérifie leurs résultats : `python3 tail_end.py`.

- Les six problèmes supplémentaires se trouvent dans le [catalogue du parcours](../docs/problemes.html). Le fichier [paradoxes.py](paradoxes.py), inclus dans l'archive, vérifie les minutes cumulées, Simpson, le bus, le dîner, Braess et les fausses alertes : `python3 paradoxes.py`.

- [Comparer les gradients NumPy et PyTorch](verification_pytorch.py), après installation des dépendances optionnelles : `python3 verification_pytorch.py`.
- Compresser une image par SVD et tracer erreur contre rang ; cela complète le jalon 3 sans remplacer les données du projet.
- Étudier les mini-lots, plusieurs graines d'initialisation et le coût des faux négatifs.
- Définir un protocole temporel avec plusieurs fenêtres de validation, avant de réutiliser ces idées sur de vraies données.
