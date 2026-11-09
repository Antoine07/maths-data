---
marp: true
html: true
---

# Clustering et profils de consommation

## Regrouper sans étiquettes connues

Après la [SVD et l'ACP](03_svd_acp.md), utilisons la géométrie des données pour rechercher des journées qui se ressemblent.

Notre question : quels profils peut-on décrire sans connaître à l'avance une catégorie pour chaque journée ?

---

## Objectif

Expliquer et programmer les deux étapes de k-means, puis interpréter ses résultats avec prudence.

Prérequis : moyenne, distance euclidienne, centrage-réduction, indexation NumPy ; ACP pour la visualisation.

Le calcul obligatoire utilise uniquement NumPy.

---

## Résumé général

Le **clustering**, ou regroupement non supervisé, construit des groupes d'observations à partir de leurs caractéristiques, sans étiquette cible fournie pour apprendre ces groupes.

K-means alterne deux opérations : affecter chaque observation au centre le plus proche, puis recalculer les centres par des moyennes.

Le résultat dépend des variables, de leurs échelles, du nombre de centres et du départ choisi. Il décrit une partition ; il ne démontre ni des catégories naturelles ni une causalité.

---

## Concepts essentiels — Cluster et classe

Une **classe** est une catégorie définie dans une tâche supervisée : par exemple dépasser ou non un seuil de consommation connu sur l'apprentissage.

Un **cluster** rassemble ici des journées proches selon température, occupation et équipements, sans utiliser leur consommation.

Les numéros des clusters sont arbitraires : le cluster 0 n'est ni « faible » ni « meilleur ». Deux exécutions peuvent échanger les numéros tout en conservant la même partition.

Ces groupes d'observations ne sont pas les groupes algébriques du chapitre sur les symétries.

---

## Concepts essentiels — Matrice et centroïdes

$Z$ est la matrice des caractéristiques après standardisation : $n$ lignes et $p$ colonnes.

On choisit un entier $k$, le nombre de clusters. Chaque centre $c_j$ contient $p$ coordonnées.

Le **centroïde** est la moyenne des observations affectées à un cluster non vide. Il n'est pas nécessairement une observation réelle.

Exemple : les points $(0,0)$ et $(0,2)$ ont pour centroïde $(0,1)$. Une occupation moyenne de 2,4 personnes décrit un profil moyen, pas une journée individuelle.

---

## Lecture des formules — L'affectation

$$
a_i=\operatorname*{argmin}_{j\in\{0,\ldots,k-1\}}\|z_i-c_j\|_2^2.
$$

$z_i$ est la ligne $i$ ; $c_j$ le centre $j$ ; $a_i$ le numéro du centre le plus proche. `argmin` renvoie un indice, pas une distance.

Pour le point $(0,2)$ et les centres $c_0=(0,0)$, $c_1=(8,0)$, les distances au carré valent $4$ et $68$. On choisit donc $a_i=0$.

À égalité, notre code choisira le premier centre. Prendre les carrés évite les racines sans changer ce classement.

---

## Lecture des formules — Recalculer les centres

$$
c_j=\frac{1}{n_j}\sum_{i:a_i=j}z_i.
$$

$n_j$ est le nombre d'observations du cluster $j$ ; la somme ne porte que sur ses membres et s'effectue coordonnée par coordonnée.

Avec $(0,0)$ et $(0,2)$ : $n_0=2$ et $c_0=((0+0)/2,(0+2)/2)=(0,1)$.

**Intuition :** déplacer le centre au milieu de ses membres réduit leur somme de distances au carré. Si $n_j=0$, la formule ne s'applique pas : notre code conserve l'ancien centre.

---

## Concepts essentiels — L'inertie

$$
J=\sum_{i=1}^{n}\|z_i-c_{a_i}\|_2^2.
$$

$J$ additionne les distances au carré entre chaque observation et son centre affecté. C'est la quantité minimisée par k-means sur l'apprentissage.

Pour $(0,0)$ et $(0,2)$ autour de $(0,1)$, la contribution vaut $1+1=2$.

L'inertie n'est ni une exactitude de classification ni une erreur de prévision en kWh. Elle dépend de l'échelle et du nombre d'observations.

---

## Exemple concret — Un tour de k-means à la main

Points : A=$(0,0)$, B=$(0,2)$, C=$(8,0)$, D=$(8,2)$. Centres de départ : A et C.

**Affectation :** A et B choisissent le premier centre ; C et D le second. L'inertie initiale vaut $0+4+0+4=8$.

**Moyennes :** les nouveaux centres sont $(0,1)$ et $(8,1)$.

**Nouvelle affectation :** les groupes restent identiques. L'inertie vaut $1+1+1+1=4$.

Nous avons atteint un point fixe pour ce départ. Cela ne prouve pas qu'un départ quelconque conduit au meilleur minimum global.

---

## Voir l'affectation et la mise à jour

![Quatre points illustratifs : avant la mise à jour, les centres sont (0,0) et (8,0), inertie 8 ; après mise à jour, ils sont (0,1) et (8,1), inertie 4.](../figures/clustering-lloyd.svg)

---

## Algorithme expliqué — K-means de Lloyd

**Objectif :** diminuer l'inertie pour un nombre $k$ fixé.

**Entrées :** une table numérique, $k$, des centres initiaux et une limite d'itérations.

**Traitement :** affecter les lignes ; recalculer les moyennes des groupes non vides ; réaffecter ; répéter jusqu'à stabilité des affectations ou limite d'itérations.

**Sortie :** centres, affectations, inertie et indicateur de convergence.

**Exemple pas à pas :** sur les quatre points précédents, un cycle suffit. Pour limiter les mauvais départs, répéter depuis plusieurs initialisations et retenir la plus faible inertie.

---

## Lecture du code — Affecter les observations

```python
import numpy as np
Z = np.array([[0., 0.], [0., 2.], [8., 0.], [8., 2.]])
centres = np.array([[0., 0.], [8., 0.]])
distances2 = np.sum((Z[:, None, :] - centres[None, :, :]) ** 2, axis=2)
labels = np.argmin(distances2, axis=1)
print(distances2)
print(labels)
```

**Fonctionnement :** les axes ajoutés construisent un tableau de différences de taille `(n, k, p)`. La somme sur les coordonnées donne une matrice `(n, k)`.

**Exécution et résultat attendu :** distances `[[0, 64], [4, 68], [64, 0], [68, 4]]`, puis `[0, 0, 1, 1]`.

**Erreur fréquente :** utiliser `axis=0` dans `argmin`, ce qui renvoie une ligne par centre au lieu d'un centre par ligne.

---

## Lecture du code — Mettre à jour un centre

```python
import numpy as np
Z = np.array([[0., 0.], [0., 2.], [8., 0.], [8., 2.]])
labels = np.array([0, 0, 1, 1])
centres = np.array([[0., 0.], [8., 0.]])
for j in range(len(centres)):
    membres = Z[labels == j]
    if len(membres):
        centres[j] = membres.mean(axis=0)
print(centres)
```

**Fonctionnement et exécution :** la boucle sélectionne chaque groupe, puis calcule sa moyenne par colonne. Sortie : `[[0, 1], [8, 1]]`.

**Erreur fréquente :** `mean()` sans axe donne une moyenne de tous les coefficients. Le contrôle `if` évite la moyenne d'un groupe vide.

---

## Explication détaillée — Pourquoi standardiser ?

La température, l'occupation et l'indice d'équipements n'ont ni les mêmes unités ni les mêmes amplitudes numériques.

On retire la moyenne d'apprentissage puis on divise par l'écart-type d'apprentissage, comme dans le cours de centrage-réduction.

Une température de 14 °C, avec moyenne 10 et écart-type 2, devient $(14-10)/2=2$. Si une colonne est constante, notre convention lui donne une échelle de 1 pour éviter une division par zéro.

La standardisation donne une géométrie explicite ; elle ne prouve pas que toutes les variables ont la même pertinence métier.

---

## Explication détaillée — Apprendre et affecter ensuite

Dans notre atelier, l'objectif est de construire des profils sur les jours 1–144, puis d'affecter de nouvelles journées à ces profils.

Les moyennes, écarts-types et centres sont donc appris **uniquement sur l'apprentissage**. Sur validation, on applique ces transformations et on prend le centre le plus proche, sans réajustement.

On peut utiliser la validation pour discuter des réglages. Le test reste réservé au bilan final du projet et ne choisit aucun réglage.

Le clustering purement descriptif d'une table entière serait un autre protocole : ici nous voulons aussi affecter des journées futures.

---

## Explication détaillée — Choisir k sans fausse certitude

Le meilleur objectif théorique ne peut qu'être aussi bon ou meilleur quand on autorise plus de centres. Des exécutions locales imparfaites peuvent néanmoins donner une courbe irrégulière.

Une baisse de l'inertie ne suffit donc pas à choisir $k$. Examiner un éventuel coude, les effectifs, les centres et la stabilité entre plusieurs graines.

Sur validation, comparer des **distances au carré moyennes**, dans la même représentation. Cette quantité ne pénalise pas à elle seule la complexité ; son minimum ne garantit pas le bon nombre de profils.

Dans le projet, comparer $k=2,3,4$ et justifier une description utile. Aucun « vrai k » n'est fourni.

---

## Explication détaillée — ACP et limites de k-means

L'ACP construit des axes ; k-means affecte des observations à des centres. Ce sont deux opérations différentes.

Pour visualiser une partition calculée avec toutes les variables standardisées, on peut projeter les points et colorer leurs clusters. Les distances projetées peuvent masquer des écarts présents dans les dimensions retirées.

K-means convient surtout à des groupes compacts dans la géométrie euclidienne retenue. Les valeurs extrêmes, les formes courbes et les densités très différentes peuvent rendre ses partitions peu pertinentes.

DBSCAN et le regroupement hiérarchique sont des pistes complémentaires, hors du calcul obligatoire de cet atelier.

---

## Exemple concret — Lire les journées du projet

![À gauche, journées d'apprentissage simulées colorées selon trois clusters calculés sur trois variables standardisées, vues en température et occupation. À droite, inerties d'apprentissage pour deux, trois et quatre centres.](../figures/clustering-journees.svg)

La couleur vient d'un calcul sur **trois variables**. Le dessin n'en montre que deux : un chevauchement visible n'est pas une erreur d'affectation.

---

## Erreurs fréquentes

- Inclure la consommation cible dans les caractéristiques du regroupement.
- Ajuster les échelles ou les centres sur validation ou test dans ce protocole.
- Donner un sens ordonné aux numéros des clusters.
- Diviser par zéro sur une colonne constante ou calculer la moyenne d'un cluster vide.
- Assimiler minimum local, stabilité numérique et preuve de catégories naturelles.
- Choisir le plus grand $k$ uniquement parce que son inertie est plus faible.

---

## Exercice 1 — Prédire un cycle de Lloyd

**Objectif pédagogique :** relier affectation et mise à jour. **Prérequis :** distances au carré et moyenne.

**Énoncé :** reprendre A=$(0,0)$, B=$(0,2)$, C=$(8,0)$, D=$(8,2)$, avec centres A et C. Prédire les affectations, les nouveaux centres et les deux inerties avant d'exécuter le code.

**Contraintes :** calculs à la main puis NumPy. **Livrable attendu :** tableau de distances et résultats commentés.

**Critères de réussite :** une étiquette par point, deux centres et une inertie décroissante.

<details><summary>Indices gradués</summary>

1. La distance au carré de B à C vaut $8^2+2^2$.
2. Le nouveau centre du premier groupe est la moyenne de A et B.
</details>

---

## Correction — Prédire un cycle de Lloyd

<details><summary>Afficher la correction</summary>

```python
import numpy as np
Z = np.array([[0., 0.], [0., 2.], [8., 0.], [8., 2.]])
centres = np.array([[0., 0.], [8., 0.]])
labels = np.argmin(np.sum((Z[:, None] - centres[None]) ** 2, axis=2), axis=1)
print(labels, np.sum((Z - centres[labels]) ** 2))
nouveaux = np.array([Z[labels == j].mean(0) for j in range(2)])
print(nouveaux, np.sum((Z - nouveaux[labels]) ** 2))
```

**Lecture et exécution :** affectation `[0, 0, 1, 1]`, inertie 8, centres `[[0, 1], [8, 1]]`, inertie 4. Les groupes sont non vides dans cet exemple ; cette dernière ligne de moyennes exige un contrôle supplémentaire dans le cas général.
</details>

---

## Exercice 2 — Affecter une nouvelle journée

**Objectif pédagogique :** appliquer une transformation déjà ajustée. **Prérequis :** standardisation et affectation.

**Énoncé :** moyenne d'apprentissage `(10, 2)`, écarts-types `(2, 1)`, centres standardisés `(-1, 0)` et `(1, 0)`. Affecter une nouvelle journée `(14, 2)`, puis reconvertir les centres dans les unités de départ.

**Contraintes :** ne recalculer aucune moyenne avec la nouvelle journée. **Livrable attendu :** coordonnées standardisées, distances et centres dans les unités initiales.

**Critères de réussite :** cluster d'indice 1, échelles inchangées et justification du choix.

<details><summary>Indices gradués</summary>

1. Soustraire la moyenne puis diviser coordonnée par coordonnée.
2. La transformation inverse multiplie par l'écart-type puis ajoute la moyenne.
</details>

---

## Correction — Affecter une nouvelle journée

<details><summary>Afficher la correction</summary>

```python
import numpy as np
moyenne, echelle = np.array([10., 2.]), np.array([2., 1.])
centres = np.array([[-1., 0.], [1., 0.]])
z = (np.array([14., 2.]) - moyenne) / echelle
d2 = np.sum((centres - z) ** 2, axis=1)
print(z, d2, np.argmin(d2))
print(centres * echelle + moyenne)
```

**Lecture et exécution :** `z = [2, 0]`, distances au carré `[9, 1]`, indice `1`. Les centres initiaux correspondent à `(8, 2)` et `(12, 2)`.

On applique les paramètres connus. Les réapprendre sur une seule journée donnerait des écarts-types nuls et changerait le système de coordonnées.
</details>

---

## Exercice 3 — Réparer une mise à jour fragile

**Objectif pédagogique :** déboguer puis vérifier un algorithme. **Prérequis :** masques NumPy, moyenne et inertie.

**Énoncé :** le code utilise `centres[j] = Z[labels == j].mean()` sans contrôler les effectifs. Corriger les deux erreurs et intégrer le calcul dans une boucle de Lloyd.

**Données :** points `(0,0)`, `(0,2)`, `(8,0)`, `(8,2)` ; centres `(0,0)`, `(8,0)`, `(100,100)`.

**Contraintes :** conserver un centre vide, limiter les itérations, retourner des labels correspondant aux centres finaux. **Livrable attendu :** fonction, historique d'inertie et justification.

**Critères de réussite :** aucune valeur non finie, inertie non croissante, troisième cluster vide explicitement signalé.

<details><summary>Indices gradués</summary>

1. Calculer `mean(axis=0)` uniquement s'il existe des membres.
2. Réaffecter après chaque mise à jour et comparer les labels.
</details>

---

## Correction — Réparer la boucle

<details><summary>Afficher la correction</summary>

La [correction complète](../../Projet_IA/clustering.py) contient `lloyd` et `kmeans`. Dans le dossier du projet :

```python
import numpy as np
from clustering import lloyd, affecter
Z = np.array([[0., 0.], [0., 2.], [8., 0.], [8., 2.]])
resultat = lloyd(Z, np.array([[0., 0.], [8., 0.], [100., 100.]]))
assert np.isfinite(resultat['centres']).all()
assert np.all(np.diff(resultat['historique']) <= 1e-10)
assert np.array_equal(resultat['labels'], affecter(Z, resultat['centres']))
print(np.bincount(resultat['labels'], minlength=3), resultat['inertie'])
```

**Lecture et exécution :** `lloyd` conserve le centre sans membre ; les contrôles vérifient finitude, décroissance et cohérence. Sortie : `[2, 2, 0] 4.0`.

Une limite d'itérations peut arrêter avant convergence : lire aussi `resultat['converge']`. Un cluster vide reste une limite de ce départ, pas un profil interprétable.
</details>

---

## Projet fil rouge — Atelier après le jalon 3

### Contexte et utilisateurs / Problème à résoudre

L'équipe énergétique veut décrire des profils de journées avant d'examiner leur consommation. Continuer le [même projet](../../Projet_IA/README.md), sans créer un nouveau jeu de données.

### Fonctionnalités cibles / Modèle de données

Regrouper les 144 journées d'apprentissage avec température, occupation et équipements ; affecter les 48 journées de validation. Exclure `jour` et `consommation` des caractéristiques.

### Architecture attendue

Réutiliser chargement et partitions de `depart.py`. Ajouter standardisation, `affecter`, `lloyd` et plusieurs départs. La correction [clustering.py](../../Projet_IA/clustering.py) utilise NumPy et se lance dans l'archive téléchargée.

---

## Projet fil rouge — Jalons, livrables et validation

### Jalons reliés aux séances

**Représenter et regrouper :** réutiliser le centrage-réduction du jalon 3, comparer $k=2,3,4$ et plusieurs départs. **Résultat vérifiable :** inerties, effectifs et centres dans les unités initiales. **À observer :** cible utilisée ou lecture ordonnée des étiquettes.

**Affecter et interpréter :** appliquer le modèle figé à la validation. **Résultat vérifiable :** une étiquette par journée, sans nouvel ajustement. **À observer :** nouvelles échelles ou centres recalculés sur validation.

### Livrables / Critères de validation

Code relançable, tableau comparatif, historique non croissant, centres et commentaire sur les changements de distribution. Justifier un choix de description sans prétendre découvrir des catégories vraies.

### Extensions facultatives

Visualiser avec l'ACP apprise sur l'apprentissage ; étudier des valeurs extrêmes ou comparer avec un regroupement hiérarchique. Ces extensions ne remplacent pas les contrôles de base.

---

## Cas d'usage réels

**Entreprise :** gestionnaire de bâtiments, scénario pédagogique.

**Problème :** résumer de nombreuses situations de température, occupation et utilisation des équipements.

**Solution :** construire quelques centres représentatifs et examiner les effectifs ainsi que les variables qui les distinguent.

**Bénéfice attendu :** faciliter la description et la comparaison des journées. Un cluster peu fréquent n'est pas automatiquement une anomalie ; les données simulées ne prouvent aucune économie d'énergie réelle.

---

## Fiche de révision

- K-means apprend une partition sans étiquettes cibles fournies.
- Affectation : centre le plus proche ; mise à jour : moyenne des membres.
- Inertie : somme des distances au carré dans la représentation choisie.
- Fixer les échelles et le protocole avant d'interpréter les profils.
- Essayer plusieurs départs et expliciter les clusters vides.
- Les numéros sont arbitraires ; aucune catégorie naturelle n'est garantie.

---

## Questions de révision

1. Pourquoi une occupation moyenne de 2,4 est-elle possible pour un centroïde ?
2. Quelle différence existe entre le numéro d'un cluster et une classe supervisée ?
3. Pourquoi l'inertie seule ne suffit-elle pas à choisir $k$ ?
4. Que devient la mise à jour lorsqu'un cluster est vide ?
5. Pourquoi faut-il garder les échelles d'apprentissage sur validation ?
6. Que peut masquer une projection sur deux axes d'une partition calculée en trois dimensions ?

---

## QCM — Questions 1 et 2

**1. K-means apprend ses groupes à partir :** A. d'étiquettes obligatoires ; B. des caractéristiques et d'une distance ; C. de la seule consommation cible ; D. d'une preuve de causalité.

**2. Le centre d'un groupe non vide est mis à jour avec :** A. le maximum par colonne ; B. une ligne toujours réelle ; C. la moyenne par colonne ; D. la somme des numéros de lignes.

<details><summary>Afficher la correction</summary>

1. **B** : le regroupement enseigné est non supervisé.
2. **C** : le centroïde minimise la somme des distances au carré pour les membres fixés.
</details>

---

## QCM — Questions 3 à 5

**3. Pour affecter la validation, il faut :** A. recalculer les centres ; B. recalculer son écart-type ; C. ajouter la cible ; D. appliquer les échelles et centres appris.

**4. Deux exécutions échangent les numéros 0 et 1 sans changer les membres. Les partitions sont :** A. équivalentes ; B. nécessairement opposées ; C. inexploitables ; D. supervisées.

**5. Une faible inertie prouve :** A. une causalité ; B. une faible somme de distances au carré pour le modèle retenu ; C. l'existence de classes naturelles ; D. une bonne prévision en kWh.

<details><summary>Afficher la correction</summary>

3. **D** : le protocole affecte de nouvelles journées à des profils déjà appris.
4. **A** : les numéros sont des noms arbitraires.
5. **B** : l'inertie mesure cet objectif géométrique, pas les autres affirmations.
</details>

---

## Résumé final

Nous pouvons décrire des profils sans étiquettes préalables.
K-means alterne affectation et moyenne dans une géométrie explicite.
Les échelles, le départ et le nombre de centres influencent la partition.
Le fil rouge conserve ses données et ajoute une description des journées.

[Reprendre le parcours : gradient et Hessienne](../gradient.md).

Références : [scikit-learn — k-means et ses limites](https://scikit-learn.org/stable/modules/clustering.html#k-means), [NumPy — argmin](https://numpy.org/doc/stable/reference/generated/numpy.argmin.html).
