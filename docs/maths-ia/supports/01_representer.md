---
marp: true
html: true
---

# Représenter et calculer

S1 · Maths A · Antoine

Algèbre, fonctions, vecteurs, matrices et prédiction linéaire.

---

## Objectif

Représenter une journée par un vecteur, choisir les dimensions d'un modèle et calculer des prédictions. Justifier les transformations algébriques utilisées.

**Prérequis :** Bases de Python : variables, fonctions, tableaux et lecture d'une boucle. Les calculs algébriques sont repris dans la séance.

---

## Résumé général

Une fonction associe une sortie à une entrée. Un modèle linéaire combine plusieurs caractéristiques avec des poids et un biais. Une matrice rassemble les observations ; le produit matrice-vecteur réalise toutes les prédictions avec la même règle.

---

## Concepts essentiels — Réécrire pour calculer

La commutativité des nombres permet d'échanger les facteurs : $3\times50=50\times3=150$. L'associativité permet de regrouper : $25\times12=(25\times4)\times3=300$.

La distributivité relie multiplication et addition : $3(x+2)=3x+6$. Elle servira à développer une erreur de prédiction.

Une réécriture doit garder la même valeur pour toutes les entrées autorisées. Par exemple, $(a+b)^2=a^2+2ab+b^2$ ; oublier le terme croisé modifie la fonction.

---

## Concepts essentiels — Fonction, variable et paramètre

Dans $f(x)=wx+b$, $x$ est l'entrée ; $w$ et $b$ sont les paramètres qui définissent la règle.

Avec $w=2$ et $b=1$, l'entrée 3 donne $2\times3+1=7$. Changer $x$ évalue la même fonction ailleurs ; changer $w$ modifie la fonction elle-même.

Dans le projet, la température est une entrée. Un poids peut être ajusté à partir des journées connues ; ce n'est pas une propriété physique universelle du bâtiment.

---

## Concepts essentiels — Une observation, un vecteur

Une journée est représentée par trois coordonnées, dans un ordre fixé : température, occupation et équipements.

Le vecteur $(12,3,4)$ signifie 12 °C, 3 occupants et un indice d'équipements de 4. L'indice est simulé et sans unité physique.

Des coordonnées de même position doivent toujours décrire la même variable. Une permutation accidentelle des colonnes change les calculs et leur sens.

---

## Lecture des formules — Combiner des caractéristiques

$$
\widehat y_i=\sum_{j=1}^{p}x_{ij}w_j+b.
$$

$i$ repère une journée ; $j$ une caractéristique ; $p$ est le nombre de caractéristiques. $w_j$ est le poids de la colonne $j$, $b$ le biais et $\widehat y_i$ la prédiction.

Exemple illustratif : pour $x=(2,1)$, $w=(3,-1)$ et $b=2$, la prédiction vaut $2\times3+1\times(-1)+2=7$.

Le biais décale toutes les prédictions. Un poids négatif fait diminuer la prédiction lorsque l'entrée correspondante augmente, les autres entrées restant fixées.

---

## Explication détaillée — Du tableau aux dimensions

Pour $n$ observations et $p$ caractéristiques, $X$ est de taille $n\times p$. Un vecteur de poids $w$ contient $p$ nombres.

Le produit $Xw$ produit une valeur par observation. Avec les tableaux NumPy utilisés ici, `X.shape == (n, p)` et `w.shape == (p,)` donnent des prédictions de forme `(n,)`.

Un produit matriciel exige que les dimensions intérieures correspondent. On ne peut pas échanger arbitrairement les matrices : leur produit n'est généralement pas commutatif.

---

## Exemple concret — Deux journées

$$
X=\begin{pmatrix}1&2\\3&4\end{pmatrix},\quad
w=\begin{pmatrix}2\\1\end{pmatrix},\quad b=1.
$$

La première journée donne $1\times2+2\times1+1=5$. La seconde donne $3\times2+4\times1+1=11$.

Si les valeurs observées sont 6 et 10, les erreurs « prédit moins observé » valent -1 et 1. Leur moyenne est nulle, alors que les deux prédictions sont imparfaites.

---

## Lecture du code — Une prédiction par ligne

```python
import numpy as np
X = np.array([[1., 2.], [3., 4.]])
w, b = np.array([2., 1.]), 1.
predictions = X @ w + b
print(predictions, predictions.shape)
```

**Fonctionnement :** `X` contient les observations et `w` les poids ; `@` réalise le produit matriciel. NumPy ajoute le même scalaire `b` à chaque résultat.

**Exécution et résultat :** chaque ligne est combinée avec les poids ; l'affichage est `[5. 11.] (2,)`.

**Erreur fréquente :** `X * w` conserve une valeur par case au lieu de sommer les contributions d'une ligne.

---

## Algorithme expliqué — Prédire sans apprendre

**Objectif :** calculer les sorties d'un modèle déjà défini. **Entrées :** une table, des poids et un biais.

**Traitement :** vérifier les colonnes et les dimensions ; multiplier chaque caractéristique par son poids ; sommer par observation ; ajouter le biais.

**Sortie :** un vecteur de prédictions. Sur l'exemple précédent, les deux sorties sont 5 et 11.

Ces opérations ne choisissent pas les poids. L'apprentissage cherchera des paramètres qui réduisent une perte sur des observations réservées à cet usage.

---

## Erreurs fréquentes

- Confondre une ligne et une colonne.
- Permuter les colonnes sans permuter les poids.
- Utiliser la consommation à prédire comme entrée.
- Présenter des poids choisis arbitrairement comme des paramètres appris.

---

## Exercice 1 — Prédire les dimensions et les valeurs

**Objectif pédagogique :** Lire une représentation matricielle. **Prérequis :** Produit matrice-vecteur.

**Énoncé :** Pour $X=((1,2),(2,0),(0,3))$, $w=(2,1)$ et $b=1$, donner les dimensions et les trois prédictions.

**Contraintes :** Calculer à la main avant NumPy.

**Livrable attendu :** Trois valeurs et les formes de X, w et du résultat.

**Critères de réussite :** Une prédiction par ligne, sans changer l'ordre des colonnes.

<details><summary>Indices gradués</summary>

1. Chaque ligne contient deux caractéristiques.
2. Multiplier chaque coordonnée par son poids avant de sommer.

</details>

---

## Correction — Prédire les dimensions et les valeurs

<details><summary>Afficher la correction</summary>

Les formes sont `(3, 2)`, `(2,)` et `(3,)`. Les valeurs sont 5, 5 et 4.

```python
import numpy as np
X, w = np.array([[1., 2.], [2., 0.], [0., 3.]]), np.array([2., 1.])
print(X @ w + 1)
```

Le produit combine les lignes et le biais ajoute 1 à chaque sortie. L'affichage confirme `[5. 5. 4.]`.

</details>


---

## Exercice 2 — Lire le rôle des paramètres

**Objectif pédagogique :** Distinguer entrées et paramètres. **Prérequis :** Fonction affine.

**Énoncé :** Le modèle est $f(x)=2x+1$. Calculer $f(3)$, puis comparer avec $g(x)=3x+1$ et $h(x)=2x+4$ pour cette même entrée.

**Contraintes :** Justifier ce qui change : poids ou biais.

**Livrable attendu :** Trois résultats et une interprétation.

**Critères de réussite :** Distinguer une pente et un décalage.

<details><summary>Indices gradués</summary>

1. Garder x égal à 3.
2. Comparer séparément le coefficient de x et le terme constant.

</details>

---

## Correction — Lire le rôle des paramètres

<details><summary>Afficher la correction</summary>

On obtient $f(3)=7$, $g(3)=10$ et $h(3)=10$. Dans g, le poids a changé ; dans h, c'est le biais. Une seule entrée peut donner la même sortie avec deux règles différentes : elle ne suffit pas à identifier les paramètres.

</details>


---

## Exercice 3 — Corriger un produit NumPy

**Objectif pédagogique :** Déboguer un calcul de prédiction. **Prérequis :** Formes et opérateurs NumPy.

**Énoncé :** Un programme utilise `predictions = X * w + b` avec X de forme (2, 2) et w de forme (2,). Pourquoi n'obtient-il pas une prédiction par observation ? Corriger et contrôler.

**Contraintes :** Utiliser les deux journées de l'exemple et justifier l'opérateur.

**Livrable attendu :** Une correction exécutable et un contrôle de forme.

**Critères de réussite :** Sortie (2,) avec les valeurs 5 et 11.

<details><summary>Indices gradués</summary>

1. Observer la forme du produit élément par élément.
2. Chercher l'opérateur qui somme les contributions de chaque ligne.

</details>

---

## Correction — Corriger un produit NumPy

<details><summary>Afficher la correction</summary>

Il faut utiliser `@`, puis vérifier le contrat de sortie.

```python
import numpy as np
X, w, b = np.array([[1., 2.], [3., 4.]]), np.array([2., 1.]), 1.
predictions = X @ w + b
assert predictions.shape == (len(X),)
print(predictions)
```

La sortie est `[5. 11.]`. Le produit `*` n'est pas incorrect en soi : il effectue une autre opération.

</details>


---

## Projet fil rouge

### Contexte et utilisateurs

Une équipe de gestion énergétique souhaite comprendre des profils de journées et préparer une prévision. Les 240 journées sont entièrement simulées ; les résultats ne constituent pas une étude de bâtiment réel.

### Problème à résoudre et fonctionnalités cibles

Représenter les journées et calculer des prédictions illustratives avec trois poids fixés, sans présenter ces poids comme un modèle ajusté.

### Modèle de données et architecture attendue

Réutiliser `pratique/depart.py`, `pratique/parcours.py` et le même notebook. Les entrées sont température, occupation et équipements. La consommation est la cible, jamais une entrée du classificateur. Les jours 1–144 servent à apprendre, 145–192 à valider, 193–240 au bilan final.

---

## Projet fil rouge — Livrables et validation

### Jalon relié à la séance

Charger les 240 lignes, documenter les trois colonnes et produire un vecteur de 240 prédictions. Contrôler une journée à la main. À observer : unités mélangées, cible ajoutée dans X et produit élément par élément.

### Livrables

Ajouter le code et son commentaire au notebook existant. Conserver les dimensions, les unités, la partition utilisée et les contrôles effectués.

### Critères de validation

Le notebook se relance dans l'ordre. Les calculs manuels concordent avec le code. Les transformations et réglages ne sont jamais appris sur le test. Expliquer les erreurs plutôt que supprimer les observations gênantes.

### Extensions facultatives

Reprendre les supports du [catalogue général](../../index.html) pour approfondir une notion. Les groupes, l'ACP, la SVD et le clustering sont des compléments ; leur étude complète n'est pas nécessaire pour ce parcours court.

---

## Cas d'usage réels

**Organisation :** service de gestion énergétique, scénario pédagogique.

**Problème :** transformer des mesures hétérogènes en une décision interprétable.

**Solution étudiée :** Algèbre, fonctions, vecteurs, matrices et prédiction linéaire.

**Bénéfice attendu :** comprendre les hypothèses et contrôler les résultats avant une utilisation sur des données réelles. Une amélioration numérique ne démontre pas une économie d'énergie ni une causalité.

---

## Fiche de révision

- Une observation devient un vecteur de caractéristiques.
- Le modèle combine des poids et un biais.
- Les dimensions donnent un premier contrôle de cohérence.
- Prédire avec des paramètres fournis n'est pas encore apprendre.

---

## Questions de révision

1. Que distingue une entrée d'un paramètre ?
2. Que représente le biais ?
3. Pourquoi les dimensions intérieures doivent-elles correspondre ?
4. Que produit X * w dans l'exemple ?
5. Pourquoi une erreur moyenne nulle ne garantit-elle pas de bonnes prédictions ?

---

## QCM — Questions 1 à 2

**1. Une ligne de X représente**

A. une observation ; B. un poids ; C. un biais ; D. une époque.

**2. Avec X de forme (5, 3), w doit contenir**

A. 5 valeurs ; B. 15 valeurs ; C. 3 valeurs ; D. aucune valeur.

<details><summary>Afficher la correction</summary>

1. **A** : chaque ligne décrit une journée

2. **C** : il faut un poids par caractéristique

</details>

---

## QCM — Questions 3 à 5

**3. Le produit matriciel NumPy s'écrit**

A. X * w ; B. X @ w ; C. X + w ; D. X / w.

**4. Changer le biais modifie**

A. le nombre de colonnes ; B. la partition ; C. la température ; D. le décalage des prédictions.

**5. Un calcul de prédiction apprend-il les poids ?**

A. toujours ; B. si X est grand ; C. non, les poids sont ici fournis ; D. si le biais vaut 0.

<details><summary>Afficher la correction</summary>

3. **B** : @ combine les lignes par produit matriciel

4. **D** : le biais ajoute une constante

5. **C** : calculer une sortie et ajuster des paramètres sont deux opérations distinctes

</details>

---

## Résumé final

Une observation devient un vecteur de caractéristiques.
Le modèle combine des poids et un biais.
Les dimensions donnent un premier contrôle de cohérence.
Prédire avec des paramètres fournis n'est pas encore apprendre.

[Continuer le parcours](02_decrire_deriver.md) · [Programme et livrables](programme.md).
