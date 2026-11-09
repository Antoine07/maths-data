---
marp: true
html: true
---

# Groupes, symétries et données

## Ce qui change et ce qui se conserve

Déplacer un objet dans une image change ses coordonnées. Doit-il changer de catégorie ? Tout dépend de la question posée au modèle.

Après les [matrices](../matrice.md), découvrons comment décrire et composer des transformations.

---

## Objectif

Reconnaître un groupe de transformations sur un exemple simple et distinguer **invariance** et **équivariance**.

Prérequis : produit matrice-vecteur, produit de matrices, identité et coordonnées du plan. Aucune connaissance préalable des groupes n'est nécessaire.

Durée indicative : 2 h, dont trois exercices et un atelier sur les données du fil rouge.

---

## Résumé général

Un groupe réunit des transformations que l'on peut composer et inverser, avec des règles précises.

Les rotations d'un carré fournissent un exemple fini que l'on peut calculer avec des matrices.

Pour les données, on demande ensuite ce qu'une transformation doit préserver : une statistique globale, une décision ou la correspondance entre entrées et sorties.

Un groupe algébrique et un groupe d'observations obtenu par clustering sont deux notions différentes.

---

## Concepts essentiels — Composer des transformations

Une transformation $g$ envoie une observation $x$ vers une autre représentation $g(x)$.

Composer $g$ et $h$, c'est appliquer $h$ puis $g$ : $(g\circ h)(x)=g(h(x))$.

Avec des vecteurs colonnes et des matrices, la composition s'écrit $GHx$ : la matrice de droite agit d'abord.

Exemple : deux rotations successives de 90° produisent une rotation de 180°.

---

## Concepts essentiels — Les quatre règles d'un groupe

Pour un ensemble de transformations muni de la composition :

1. **Stabilité** : composer deux transformations de l'ensemble reste dans l'ensemble.
2. **Associativité** : regrouper les compositions différemment ne change pas le résultat.
3. **Identité** : une transformation ne change rien et appartient à l'ensemble.
4. **Inverse** : chaque transformation peut être annulée par une transformation de l'ensemble.

La composition des fonctions est associative. Il reste à vérifier les trois autres règles pour l'ensemble choisi.

---

## Exemple concret — Les rotations d'un carré

Plaçons le carré aux sommets $(1,1)$, $(-1,1)$, $(-1,-1)$ et $(1,-1)$.

Une rotation de 90° autour de l'origine envoie chaque sommet sur un autre sommet. Le carré est conservé comme ensemble de points.

Les rotations de 0°, 90°, 180° et 270° constituent le groupe **cyclique à quatre éléments**, noté $C_4$.

Ce groupe contient les rotations du carré ; ses réflexions formeraient un ensemble plus grand.

---

## Lecture des formules — Un quart de tour

$$
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
R\begin{pmatrix}a\\b\end{pmatrix}=\begin{pmatrix}-b\\a\end{pmatrix}.
$$

$R$ désigne une rotation de 90° dans le sens inverse des aiguilles d'une montre ; $a$ et $b$ sont les coordonnées du point.

Pour $(a,b)=(3,4)$, la nouvelle abscisse vaut $0\times3-1\times4=-4$ et l'ordonnée vaut $1\times3+0\times4=3$.

On obtient $(-4,3)$ : le point se déplace, sa distance à l'origine reste 5.

---

## Explication détaillée — Quatre tours et un inverse

On écrit $I$ pour la matrice identité et $R^k$ pour $k$ compositions de $R$.

Pour le point $(1,0)$ : $(1,0)\to(0,1)\to(-1,0)\to(0,-1)\to(1,0)$.

Ainsi $R^4=I$ et $R^{-1}=R^3$ : trois quarts de tour annulent un quart de tour.

La règle $R^aR^b=R^{(a+b)\bmod4}$ décrit la composition : on additionne les nombres de quarts de tour et on conserve le reste après division par 4. Par exemple, $R^3R^2=R^1$.

---

## Voir le groupe cyclique

![Le vecteur (1,0) devient (0,1), puis (-1,0), puis (0,-1) sous quatre rotations successives de 90 degrés. Les quatre points restent à distance 1 de l'origine.](../figures/groupes-rotations.svg)

---

## Lecture du code — Vérifier la composition

```python
import numpy as np
R = np.array([[0, -1], [1, 0]])
x = np.array([3, 4])
print(R @ x)
print(np.linalg.matrix_power(R, 4))
```

**Fonctionnement :** `R` transforme le vecteur `x` ; `@` effectue un produit matriciel. `matrix_power` compose la matrice quatre fois.

**Exécution et résultat attendu :** affichage de `[-4  3]`, puis de l'identité `[[1, 0], [0, 1]]` sur deux lignes.

**Erreur fréquente :** `R ** 4` élève chaque coefficient à la puissance 4 et ne calcule pas quatre rotations.

---

## Algorithme expliqué — Vérifier un groupe fini

**Objectif :** vérifier les règles sur les quatre rotations.

**Entrées :** les matrices $I$, $R$, $R^2$, $R^3$.

**Traitement :** calculer les 16 produits, vérifier qu'ils restent dans la liste, identifier l'identité puis chercher l'inverse de chaque élément. L'associativité vient du produit matriciel.

**Sortie :** une table de composition et un inverse pour chaque rotation.

**Exemple pas à pas :** 90° puis 270° donnent 360°, donc 0°. Dans la table, la case correspondante contient $I$.

---

## Concepts essentiels — L'ordre peut compter

Un groupe n'impose pas que deux transformations commutent : leur ordre peut changer le résultat.

La réflexion horizontale $S$ transforme $(a,b)$ en $(a,-b)$.

Sur $(1,0)$, appliquer $S$ puis $R$ donne $(0,1)$. Appliquer $R$ puis $S$ donne $(0,-1)$.

Les rotations de $C_4$ commutent entre elles. Si l'on ajoute les réflexions du carré, ce n'est plus toujours le cas.

---

## Concepts essentiels — Une action sur les données

Une **action** indique comment chaque élément du groupe transforme les données, en respectant l'identité et la composition.

Exemple : chaque rotation de $C_4$ agit sur les coordonnées des points du plan.

Autre exemple : une permutation réordonne les lignes d'une table. Son inverse remet les lignes à leur place.

Réordonner la représentation d'un ensemble d'observations ne change pas cet ensemble. Cela peut toutefois changer une procédure qui exploite l'ordre temporel.

---

## Concepts essentiels — Invariance

$$
f(gx)=f(x).
$$

$x$ est l'entrée, $g$ une transformation autorisée et $f$ la fonction étudiée. L'écriture $gx$ désigne l'action de $g$ sur $x$.

**Intuition :** la sortie ne change pas.

Exemple : $f(x)$ est la distance à l'origine. Pour $x=(3,4)$ et $Rx=(-4,3)$, elle vaut dans les deux cas $\sqrt{25}=5$.

Une moyenne de valeurs est aussi invariante à leur réordonnement : la moyenne de $(2,4,6)$ et de $(6,2,4)$ vaut 4.

---

## Concepts essentiels — Équivariance

$$
f(gx)=\rho(g)f(x).
$$

$\rho(g)$ décrit la transformation correspondante sur les sorties. Elle peut agir sur un espace différent de celui des entrées.

**Intuition :** la sortie suit la transformation de l'entrée.

Exemple : $f(x)=2x$ et $x=(1,0)$. Alors $f(Rx)=f(0,1)=(0,2)$ et $Rf(x)=R(2,0)=(0,2)$.

Sur une table, une prédiction calculée indépendamment pour chaque ligne doit suivre la permutation des lignes.

---

## Explication détaillée — Les liens avec l'IA

Pour classer une image, on peut souhaiter que déplacer l'objet préserve sa catégorie : c'est une invariance souhaitée.

Pour localiser ou segmenter cet objet, la position ou le masque doit suivre le déplacement : c'est une équivariance souhaitée.

Pour un graphe, renuméroter les sommets doit déplacer les sorties associées aux sommets de manière correspondante.

Ce sont des propriétés à construire ou à vérifier. Un réseau quelconque ne les satisfait pas automatiquement. Nous les retrouverons après la [rétropropagation](06_retropropagation.md).

---

## Explication détaillée — Choisir les bonnes symétries

Une rotation géométrique conserve les distances entre des points du plan. Elle ne conserve pas automatiquement le sens de toutes les données.

Tourner un chiffre 6 peut le faire ressembler à un 9. Permuter les mots d'une phrase peut changer son sens.

Dans le fil rouge, température et occupation n'ont pas le même sens : les permuter ou les mélanger par une rotation ne préserve pas le problème de consommation.

Nous testerons plutôt le réordonnement de lignes **au sein de l'apprentissage**, avec leurs cibles alignées. Les partitions temporelles restent fixées avant cette opération.

---

## Erreurs fréquentes

- Confondre groupe algébrique et cluster d'observations.
- Oublier l'identité ou l'inverse dans un ensemble de transformations.
- Supposer que toutes les matrices sont inversibles ou que tous les groupes commutent.
- Calculer une puissance coefficient par coefficient au lieu de composer.
- Exiger une invariance lorsque la sortie doit suivre le mouvement.
- Appliquer une transformation qui détruit le sens des données.

---

## Exercice 1 — Prédire quatre rotations

**Objectif pédagogique :** lire un produit et identifier un inverse. **Prérequis :** matrice $R$ et composition.

**Énoncé :** pour $x=(2,1)$, prédire $Rx$, $R^2x$, $R^3x$ et $R^4x$. Quel inverse annule $R$ ? Que fait `R ** 2` ?

**Contraintes :** répondre à la main avant d'exécuter. **Livrable attendu :** quatre vecteurs et une vérification NumPy.

**Critères de réussite :** retour à $x$, inverse correct et distinction entre produit matriciel et produit coefficient par coefficient.

<details><summary>Indices gradués</summary>

1. Un quart de tour transforme $(a,b)$ en $(-b,a)$.
2. Pour annuler 90°, compléter le tour de 360°.
</details>

---

## Correction — Prédire quatre rotations

<details><summary>Afficher la correction</summary>

Les vecteurs sont $(-1,2)$, $(-2,-1)$, $(1,-2)$ et $(2,1)$. L'inverse est $R^3$.

```python
import numpy as np
R = np.array([[0, -1], [1, 0]])
x = np.array([2, 1])
for k in range(1, 5):
    print(np.linalg.matrix_power(R, k) @ x)
assert np.array_equal(np.linalg.matrix_power(R, 3) @ R, np.eye(2))
```

**Lecture et exécution :** la boucle parcourt quatre puissances et affiche les vecteurs annoncés. `R ** 2` donne `[[0, 1], [1, 0]]`, alors que `R @ R` donne `-I`. Les confondre modifie la transformation.
</details>

---

## Exercice 2 — Tester une invariance et une équivariance

**Objectif pédagogique :** comparer deux propriétés. **Prérequis :** distance euclidienne, rotation et projection matricielle.

**Énoncé :** pour $x=(3,4)$ et $z=(1,0)$, vérifier que la distance entre $Rx$ et $Rz$ égale celle entre $x$ et $z$. Le projecteur horizontal $P=\operatorname{diag}(1,0)$ vérifie-t-il $P(Rx)=R(Px)$ ?

**Contraintes :** donner les valeurs et les vecteurs. **Livrable attendu :** calculs puis contrôle NumPy.

**Critères de réussite :** distinguer la conservation d'une distance et l'équivariance du projecteur.

<details><summary>Indices gradués</summary>

1. Comparer les carrés des distances avant de prendre la racine.
2. Calculer séparément $PRx$ et $RPx$.
</details>

---

## Correction — Tester les deux propriétés

<details><summary>Afficher la correction</summary>

La distance vaut $\sqrt{2^2+4^2}=\sqrt{20}$, avant comme après la rotation. Mais $PRx=(-4,0)$ et $RPx=(0,3)$ : le projecteur ne commute pas avec $R$.

```python
import numpy as np
R, P = np.array([[0., -1.], [1., 0.]]), np.diag([1., 0.])
x, z = np.array([3., 4.]), np.array([1., 0.])
print(np.linalg.norm(x - z), np.linalg.norm(R @ x - R @ z))
print(P @ R @ x, R @ P @ x)
```

**Lecture et exécution :** deux normes affichent environ `4.4721`, puis les vecteurs `[-4, 0]` et `[0, 3]`. Conserver les distances ne rend pas toute fonction équivariante.
</details>

---

## Exercice 3 — Corriger des cibles désalignées

**Objectif pédagogique :** déboguer un réordonnement et le justifier. **Prérequis :** indexation NumPy, moyenne et équivariance.

**Énoncé :** un programme calcule `pred_perm = predictions[ordre]`, puis `np.mean((pred_perm - y)**2)`. Corriger l'erreur et retrouver les prédictions dans l'ordre initial.

**Données :** `predictions = [10., 20., 30.]`, `y = [11., 18., 32.]` et `ordre = [2, 0, 1]`.

**Contraintes :** conserver l'association journée-cible. **Livrable attendu :** code et justification.

**Critères de réussite :** même erreur moyenne avant et après permutation ; récupération exacte de l'ordre initial.

<details><summary>Indices gradués</summary>

1. Les cibles doivent suivre les mêmes indices.
2. `np.argsort(ordre)` donne la permutation inverse.
</details>

---

## Correction — Réaligner les sorties

<details><summary>Afficher la correction</summary>

```python
import numpy as np
predictions, y = np.array([10., 20., 30.]), np.array([11., 18., 32.])
ordre = np.array([2, 0, 1])
pred_perm = predictions[ordre]
print(np.mean((pred_perm - y[ordre]) ** 2))
print(pred_perm[np.argsort(ordre)])
```

**Lecture et exécution :** la même permutation agit sur les prédictions et les cibles ; l'erreur moyenne vaut $(1+4+4)/3=3$. La permutation inverse redonne `[10, 20, 30]`.

L'erreur moyenne est invariante au réordonnement des paires. Les prédictions par ligne sont équivariantes. Permuter uniquement les prédictions détruit les paires.
</details>

---

## Projet fil rouge — Atelier de cohérence

### Contexte et utilisateurs / Problème à résoudre

Dans le [projet consommation](../../Projet_IA/README.md), l'équipe énergétique doit conserver la correspondance entre chaque journée et sa prédiction, même si l'affichage change d'ordre.

### Fonctionnalités cibles / Modèle de données

Ajouter un contrôle de permutation des lignes d'apprentissage avec les colonnes température, occupation et équipements. Conserver les identifiants et les cibles correspondantes.

### Architecture attendue

Faire évoluer `depart.py` ; utiliser [groupes_symetries.py](../../Projet_IA/groupes_symetries.py) comme correction exécutable. Aucun modèle appris n'est nécessaire : des poids fixés suffisent au contrôle.

---

## Projet fil rouge — Livrables et validation

### Jalons reliés aux séances

**Après les matrices :** vérifier $C_4$, l'identité et les inverses ; produire la table des compositions. **À observer :** confusion entre `**` et `@`.

**Atelier sur la table :** permuter les lignes à partitions fixées, puis annuler la permutation. **Résultat vérifiable :** mêmes prédictions dans l'ordre initial et même erreur si les cibles suivent. **À observer :** cibles désalignées ou mélange du test.

### Livrables / Critères de validation

Table des compositions, contrôles NumPy, deux exemples métier de symétries autorisées ou interdites. Les comparaisons de nombres flottants utilisent `np.allclose`.

### Extensions facultatives

Après les réseaux : comparer une décision de classification et un masque de segmentation sous translation. Voir l'ouverture du chapitre de rétropropagation.

---

## Cas d'usage réels

**Entreprise :** fabricant de pièces, scénario pédagogique d'inspection visuelle.

**Problème :** reconnaître un défaut malgré une position différente de la pièce sur le convoyeur.

**Solution :** identifier les transformations qui préservent la tâche ; concevoir des traitements adaptés ou augmenter les données d'apprentissage avec ces transformations.

**Bénéfice attendu :** réduire la dépendance à une position arbitraire. L'augmentation des données ne garantit pas à elle seule une invariance exacte, et toutes les orientations ne sont pas forcément admissibles.

---

## Fiche de révision

- Groupe : stabilité, associativité, identité, inverse.
- La matrice de droite agit d'abord sur un vecteur colonne.
- Dans $C_4$, quatre quarts de tour donnent l'identité.
- Invariance : la sortie reste la même.
- Équivariance : la sortie suit une transformation correspondante.
- Une symétrie doit être pertinente pour les données et la tâche.

---

## Questions de révision

1. Pourquoi les seules rotations de 90° et 180° ne forment-elles pas un groupe ?
2. Quel élément annule une rotation de 270° dans $C_4$ ?
3. En quoi `R ** 2` diffère-t-il de `R @ R` ?
4. Pourquoi un masque de segmentation doit-il suivre le déplacement de l'image ?
5. Pourquoi ne faut-il pas mélanger température et occupation par une rotation arbitraire ?
6. Quelles transformations faut-il appliquer aux cibles lorsque les lignes sont permutées ?

---

## QCM — Questions 1 et 2

**1. Dans $C_4$, $R^3R^2$ vaut :** A. $R^2$ ; B. $R$ ; C. $I$ ; D. la matrice nulle.

**2. Quelle propriété n'est pas imposée à tout groupe ?** A. l'associativité ; B. l'identité ; C. la commutativité ; D. l'existence des inverses.

<details><summary>Afficher la correction</summary>

1. **B** : cinq quarts de tour équivalent à un seul.
2. **C** : l'ordre de composition peut compter.
</details>

---

## QCM — Questions 3 à 5

**3. La norme d'un vecteur après rotation orthogonale est :** A. invariante ; B. toujours nulle ; C. doublée ; D. indéfinie.

**4. Si l'on permute les lignes, les prédictions indépendantes par ligne doivent :** A. toutes devenir égales ; B. rester aux anciennes positions ; C. disparaître ; D. suivre la permutation.

**5. Une augmentation par rotation convient :** A. à toute table numérique ; B. si elle préserve le sens de la tâche ; C. à toutes les images de chiffres sans exception ; D. uniquement sans identité.

<details><summary>Afficher la correction</summary>

3. **A** : une rotation orthogonale conserve les longueurs.
4. **D** : c'est l'équivariance des sorties par ligne.
5. **B** : il faut justifier les transformations retenues.
</details>

---

## Résumé final

Les groupes permettent de raisonner sur les transformations réversibles.
Les rotations du carré rendent les règles concrètes et calculables.
L'invariance conserve une réponse ; l'équivariance la transforme de manière cohérente.
Pour les données, le sens métier détermine les transformations admissibles.

[Continuer : géométrie des données](01_geometrie_donnees.md).

Référence : [Geometric Deep Learning — groupes, actions, invariance et équivariance](https://geometricdeeplearning.com/book/algebraicpriors.html).
