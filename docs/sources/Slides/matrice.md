---
marp: true
theme: default
paginate: true
class: lead
---

## **Matrices, vecteurs, transformations et vecteurs propres**

![Un triangle avant et après une transformation matricielle.](images/couverture-matrices.svg)

---

## Introduction 

D'où viennent les équations ou matrices

## **Dimension 1 : décroissance simple**

On modélise une quantité qui diminue de 20 % à chaque période
(population, prix, signal…).

Relation réelle :

$$
x_{\text{nouveau}} = 0.8 , x_{\text{ancien}}
$$

---

Ici :

1. le coefficient **0.8** exprime une perte de 20 %,
1. la « transformation » est simplement **une matrice 1×1** :
  $$
  [0.8]
  $$

Ce modèle dit juste : *chaque période, on garde 80 % de la valeur précédente*.

---

# Dimension 2 : industrie et services

Deux secteurs se stimulent mutuellement :

1. l'industrie génère +0.7 de nouvelle industrie et +0.1 de services,
1. les services génèrent +0.2 d'industrie et +0.8 de services.

Alors :

$$
\begin{pmatrix}
\text{Ind}*{n+1} \\
\text{Serv}*{n+1}
\end{pmatrix}
=

\begin{pmatrix}
0.7 & 0.1 \\
0.2 & 0.8
\end{pmatrix}
\begin{pmatrix}
\text{Ind}_n \\
\text{Serv}_n
\end{pmatrix}
$$

La matrice traduit simplement :

1. comment **chaque secteur influence l'autre**,
1. et comment chacun **s'auto-alimente**.

---

## I. Vecteurs et matrices

### 1. Vecteurs

Un vecteur est un ensemble ordonné de nombres.

$$
x =
\begin{pmatrix}
2 \\
-1
\end{pmatrix}
$$

Il représente une direction et une intensité dans l'espace.

---

### 2. Matrices

Une matrice est un tableau de nombres.

$$
A=
\begin{pmatrix}
1 & 3 \\
2 & -1
\end{pmatrix}
$$

Elle représente une transformation linéaire : elle prend un vecteur en entrée et produit un nouveau vecteur.

---

## II.1 Multiplication matrice–vecteur

Pour une matrice (A) et un vecteur (x), le produit (Ax) est défini par :

$$
Ax=
\begin{pmatrix}
a_{11}x_1 + a_{12}x_2 \\
a_{21}x_1 + a_{22}x_2
\end{pmatrix}
$$

Exemple :

$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 1
\end{pmatrix},
\quad
x=
\begin{pmatrix}
2\\
1
\end{pmatrix}
$$

d'où :

$$
Ax=
\begin{pmatrix}
1\cdot 2 + 2\cdot 1 \\
3\cdot 2 + 1\cdot 1
\end{pmatrix}
=
\begin{pmatrix}
4 \\
7
\end{pmatrix}
$$

Interprétation : la matrice transforme le vecteur en l'étirant, le tournant ou le comprimant.

---

## II.2 Multiplication matrice–matrice

Voici la **règle** pour multiplier deux matrices **2×2** :

$$
A =
\begin{pmatrix}
a & b \\
c&d
\end{pmatrix}
\qquad
B =
\begin{pmatrix}
e & f\\
g & h
\end{pmatrix}
$$

Le produit se calcule ligne par colonne :

$$
AB =
\begin{pmatrix}
ae + bg & af + bh \\
ce + dg & cf + dh
\end{pmatrix}.
$$

👉 **Ligne × Colonne** pour chaque élément.

---
Voici la **règle très** pour multiplier deux matrices **3×3** :

$$
C = A \times B,\quad C_{ij} = \text{somme des produits }(\text{ligne } i \text{ de } A)\times(\text{colonne } j \text{ de } B).
$$

Autrement dit :

> **Chaque élément = ligne de A × colonne de B.**


---

Pour multiplier :

$$
A_{n \times p} \quad \text{et} \quad B_{p \times m},
$$

il faut :

$$
\boxed{\text{colonnes de A} = \text{lignes de B}}.
$$

Donc **p = p**


---

**Magie de Numpy**

Pour multiplier deux matrices il suffit d'utiliser l'opérateur `@` comme suit dans Numpy

`C = A @ B`

A et B sont deux matrices Numpy `np.array`, l'opérateur ne marche que sur les array `numpy`

---

**Qu'est ce que ces dimensions peuvent représenter ?**

n = le nombre d'individus / situations / observations

p = le nombre de variables / paramètres / données par individu

---

## III. Transformations linéaires

Une matrice carrée représente une transformation linéaire de l'espace vers lui-même.

Voici les transformations fondamentales.

### 1. Étirement

$$
A=
\begin{pmatrix}
3 & 0 \\
0 & 1
\end{pmatrix}
$$

Multiplie la coordonnée (x) par 3, laisse (y) inchangé.

---

## Voir une transformation matricielle

![Le cercle unité devient une ellipse après multiplication par la matrice diagonale de coefficients 2 et 0,5 ; les deux directions de base sont transformées avec lui.](figures/matrice-transformation.svg)

La matrice s'applique à chaque vecteur du plan. Les deux axes ont la même échelle graphique.

---

### 2. Compression

$$
A=
\begin{pmatrix}
0.5 & 0\\
0 & 0.5
\end{pmatrix}
$$

Réduit toutes les directions d'un facteur 2.

![Le même triangle avant et après la compression de facteur 0,5 sur les deux axes, avec les mêmes unités graphiques.](images/transformation-compression.svg)

---

### 3. Réflexion (symétrie)

$$
A=
\begin{pmatrix}
1 & 0\\
0 & -1
\end{pmatrix}
$$

Symétrie par rapport à l'axe (x).

![Une réflexion conserve les abscisses du triangle et change le signe de ses ordonnées.](images/transformation-reflexion.svg)

---

### 4. Rotation

$$
A=
\begin{pmatrix}
\cos\theta & -\sin\theta\\
\sin\theta & \cos\theta
\end{pmatrix}
$$

Rotation de tout l'espace d'un angle (\theta).

![Le même triangle avant et après une rotation de 45 degrés autour de l'origine.](images/transformation-rotation.svg)

Exemple illustré : $\theta=45^\circ$ ; les deux repères ont la même échelle.

---

## IV. Matrices particulières : matrices symétriques

Une matrice est symétrique si :

$$
A = A^T,
$$
c'est-à-dire :
$$
a_{ij} = a_{ji}
$$

Exemple :

$$
S=
\begin{pmatrix}
2 & 1\\
1 & 3
\end{pmatrix}
$$

Les matrices symétriques possèdent des propriétés géométriques fortes, notamment l'existence de vecteurs propres orthogonaux.

---

## V. Vecteurs propres et valeurs propres

### 1. Définition

Pour une matrice carrée (A), un vecteur non nul (v) est un vecteur propre s'il existe un réel `lambda` tel que :

$$
A v = \lambda v
$$

1. (v) est une direction préservée,


$$
\lambda
$$ 

est le facteur d'étirement dans cette direction.

---

### 2. Exemple

$$
A=
\begin{pmatrix}
3 & 0\\
0 & 2
\end{pmatrix}.
$$

Alors :

$$
A
\begin{pmatrix}
1\\
0
\end{pmatrix}
=
\begin{pmatrix}
3\\
0
\end{pmatrix}
= 3
\begin{pmatrix}
1\\
0
\end{pmatrix}
$$

Donc `(1,0)^T` est un vecteur propre, valeur propre `lambda = 3`. 

De même :

$$
A
\begin{pmatrix}
0\\
1
\end{pmatrix}
=
2
\begin{pmatrix}
0\\
1
\end{pmatrix}
$$

---

### 3. Interprétation géométrique

Une matrice possède généralement plusieurs directions privilégiées : ses vecteurs propres.
Ce sont les directions où la transformation agit de manière la plus simple.

Si l'on observe deux données comme la taille et le poids, les vecteurs propres indiquent les directions dans lesquelles ces données varient le plus ensemble. Par exemple, on peut découvrir qu'une augmentation de taille s'accompagne souvent d'une augmentation de poids : cette relation correspond à une direction propre. Les vecteurs propres servent donc à repérer les tendances naturelles dans les données.

---

Cette notion sont essentielles dans:

1. analyser les directions principales d'une fonction (via une Hessienne),
1. comprendre des données (ACP),
1. étudier la stabilité de systèmes,
1. optimiser des critères.

---

#  Comment obtenir

$$
A = P D P^{-1}
$$

La diagonalisation consiste à **réécrire la matrice A dans une base formée de ses vecteurs propres**.

Voici les étapes exactes.

---

# 1. Trouver les valeurs propres

On résout :

$$
\det(A - \lambda I) = 0
$$

Les solutions 

$$
\lambda_1, \lambda_2, \dots
$$ 

sont les **valeurs propres**.

---

# 2. Trouver les vecteurs propres

Pour chaque valeur propre  `lambda`, on résout :

$$
(A - \lambda I)v = 0.
$$

Les solutions non nulles sont les **vecteurs propres**.

---

# 3. Construire la matrice (P)

On met **chaque vecteur propre comme colonne** :

$$
P = [v_1 ; v_2 ; \dots ; v_n].
$$

Si la matrice est diagonalisable, (P) est **inversible**.

---

# 4. Construire la matrice diagonale (D)

On place les valeurs propres **dans le même ordre que les vecteurs propres de (P)** :

$$
D =
\begin{pmatrix}
\lambda_1 & 0 & \cdots \\
0 & \lambda_2 & \cdots \\
\vdots & & \ddots
\end{pmatrix}.
$$

---

# 5. Alors on obtient automatiquement :

$$
A P = P D
$$

Pourquoi ?

Parce que :

$$
A v_i = \lambda_i v_i
\quad\text{pour chaque vecteur propre } v_i.
$$

Écrit sous forme matricielle :

$$
A[v_1 ; v_2 ;\dots; v_n]
=

[v_1 ; v_2 ;\dots; v_n]
\begin{pmatrix}
\lambda_1 & 0 & \dots \\
0 & \lambda_2 & \dots \\
\vdots & & \ddots
\end{pmatrix}.
$$

---

Donc :

$$
A P = P D.
$$

Et comme (P) est inversible :

$$
A = P D P^{-1}
$$

---

# Résumé

> On diagonalise une matrice en construisant la base de ses vecteurs propres : dans cette base, la matrice devient diagonale, ce qui donne


$$
A = P D P^{-1}
$$


---

### 4. Théorèmes importants

**Matrices symétriques réelles.**
Toute matrice symétrique réelle admet une famille complète de vecteurs propres réels, mutuellement orthogonaux, qui forment une base de l'espace.

**Matrices diagonalisables.**
Toute matrice diagonalisable possède suffisamment de vecteurs propres pour former une base.
Ces vecteurs propres ne sont pas nécessairement orthogonaux.

**Autres matrices.**
Une matrice qui n'est pas diagonalisable ne possède pas assez de vecteurs propres pour former une base (et peut même ne pas en posséder du tout).


---

## VI. Combinaison linéaire et base de vecteurs propres

De nombreuses matrices, notamment les matrices symétriques, peuvent être diagonalisées :

$$
A = P D P^{-1},
$$

où (D) est diagonale, formée des valeurs propres.

Cette idée servira plus tard pour :

1. lire facilement la structure d'une transformation,
2. identifier les directions principales d'un problème.

Diagonaliser, c'est trouver les axes naturels du problème.

---

## Remarque en statistiques

La covariance mesure comment deux variables varient ensemble : positive si elles montent ou descendent ensemble, négative si l'une monte quand l'autre descend.

La matrice de covariance est diagonalisée :
→ Les vecteurs propres = axes principaux
→ Les valeurs propres = variances importantes


> **(A) et (D) font la même chose : (A) le fait dans la base normale, (D) le fait dans la base des vecteurs propres où tout est plus simple.**

---


# Inverse d'une matrice : méthode de la matrice augmentée

Une matrice (A) est inversible s'il existe `InvA` tel que :

$$
A A^{-1} = I.
$$

Pour trouver `InvA`, on utilise **la matrice augmentée** :

$$
(A \mid I),
$$

et on applique des opérations élémentaires pour transformer :

$$
(A \mid I) ;\longrightarrow; (I \mid A^{-1}).
$$

---

## Exemple 

Soit

$$
A=
\begin{pmatrix}
2 & 1\\
1 & 1
\end{pmatrix}.
$$

On forme :

$$
\left(
\begin{array}{cc|cc}
2 & 1 & 1 & 0\\
1 & 1 & 0 & 1
\end{array}
\right).
$$

Étape 1 : rendre le pivot en haut à gauche égal à 1 (on échange les lignes) :

$$
\left(
\begin{array}{cc|cc}
1 & 1 & 0 & 1\\
2 & 1 & 1 & 0
\end{array}
\right).
$$

---

Étape 2 : annuler la deuxième ligne, première colonne :

L2 ← L2 – 2 L1

$$
\left(
\begin{array}{cc|cc}
1 & 1 & 0 & 1\\
0 & -1 & 1 & -2
\end{array}
\right).
$$

---

Étape 3 : normaliser la deuxième ligne

L2 ← –L2

$$
\left(
\begin{array}{cc|cc}
1 & 1 & 0 & 1\\
0 & 1 & -1 & 2
\end{array}
\right).
$$

---

Étape 4 : annuler le 1 au-dessus (colonne 2)

L1 ← L1 – L2

$$
\left(
\begin{array}{cc|cc}
1 & 0 & 1 & -1\\
0 & 1 & -1 & 2
\end{array}
\right).
$$

Résultat :

$$
A^{-1}=
\begin{pmatrix}
1 & -1\\
-1 & 2
\end{pmatrix}.
$$

---

# Vérification

$$
A A^{-1} =
\begin{pmatrix}
2 & 1\\
1 & 1
\end{pmatrix}
\begin{pmatrix}
1 & -1\\
-1 & 2
\end{pmatrix}
=

\begin{pmatrix}
1 & 0\\
0 & 1
\end{pmatrix}.
$$

L'inverse est correctement trouvé.

---

# Résolution d'un système linéaire `2x2`

Un système de deux équations à deux inconnues s'écrit :

$$
\begin{cases}
a_{11} x + a_{12} y = b_1 \\
a_{21} x + a_{22} y = b_2
\end{cases}
$$

---

# Forme matricielle

$$
A x = b,
\quad
A =
\begin{pmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}
\end{pmatrix},
\quad
x =
\begin{pmatrix}
x \\ y
\end{pmatrix},
\quad
b =
\begin{pmatrix}
b_1 \\ b_2
\end{pmatrix}.
$$

Le but est de trouver le vecteur `x`

---

# Condition d'existence d'une solution unique

Une unique solution existe **si et seulement si** :

$$
\det(A) \neq 0.
$$

Pour une matrice 2×2 :

$$
\det(A) = a_{11} a_{22} - a_{12} a_{21}.
$$

---


## Exercice 1

Résoudre à l'aide de la matrice augmentée, puis vérifiez à l'aide `np.linalg.inv(A)` avec Numpy que vous avez bien la matrice inversée.

$$
\begin{cases}
3x + 2y = 7 \\
x - y = 1
\end{cases}
$$

---

## Exercice 2
Résoudre par la matrice augmentée :

$$
\begin{cases}
4x - y = 10 \\
2x + y = 8
\end{cases}
$$

---

## Exercice 3
Déterminer si le système possède une solution unique :

$$
\begin{cases}
2x + 4y = 8 \\
x + 2y = 4
\end{cases}
$$

---

# Résolution d'un système linéaire `3x3` avec NumPy

Un système linéaire s'écrit sous forme matricielle :

$$
A x = b
$$

où `A` est une matrice 3x3, `x` le vecteur des inconnues, et `b` le vecteur des résultats.

NumPy permet de résoudre directement ce type de système.

---

## Méthode

Pour une unique solution, il faut que :

$$
\det(A) \neq 0.
$$

NumPy vérifie cette condition automatiquement.

La résolution se fait avec :

```python
x = np.linalg.solve(A, b)
```

---

## Exemple

Résoudre :

$$
\begin{cases}
x + y + z = 6\\
2x - y + 3z = 14\\
-x + 4y + z = 2
\end{cases}
$$

---

```python
import numpy as np

A = np.array([
    [1, 1, 1],
    [2, -1, 3],
    [-1, 4, 1]
])

b = np.array([6, 14, 2])

x = np.linalg.solve(A, b)
print(x)
```

Résultat :

$$
x=3,\quad y=1,\quad z=2.
$$

---

## Vérification

```python
A @ x    # doit être égal à b
```

---

## Remarque

> Audelas de la dimension 3x3 on utilise d'autres méthodes.
> Pour des systèmes de taille supérieure à `3x3` on utilise des méthodes numériques robustes comme la décomposition LU ou QR. 
> NumPy applique automatiquement ces méthodes via `np.linalg.solve`

---

# Méthode stable

```python
import numpy as np

A = np.array([
    [2, 1, 0, 3],
    [1, 4, 2, 1],
    [0, 2, 5, 2],
    [3, 1, 2, 6]
], dtype=float)

b = np.array([7, 12, 15, 20], dtype=float)

x = np.linalg.solve(A, b)
print("Solution :", x)

```

Si ça échoue : `LinAlgError: Singular matrix`

---

## Application - Trouvez les vecteurs propres

Utilisez Python pour trouver les vecteurs propres de la matrice suivante:

$$
A=
\begin{pmatrix}
4 & 1 & 2\\
0 & 3 & 5\\
1 & 0 & 2\\
\end{pmatrix}.
$$

---

Testez le programme suivant

```python
import numpy as np

A = np.array([
    [4, 1, 2],
    [0, 3, 5],
    [1, 0, 2]
])

# Calcul des valeurs propres et vecteurs propres
valeurs_propres, vecteurs_propres = np.linalg.eig(A)
print(valeurs_propres)
print(vecteurs_propres)
```

---

## Exercice **Interaction entre deux types de cellules**

Deux types de cellules interagissent :

1. (x) : cellules immunitaires
1. (y) : cellules tumorales

On modélise leurs influences respectives par :

$$
A=
\begin{pmatrix}
4 & 2\\
2 & 4
\end{pmatrix}.
$$

Cette matrice décrit comment les deux populations agissent l'une sur l'autre dans un modèle simplifié.

---
Sans utilisez Python répondez aux questions suivantes:

1. Calculez les valeurs propres de (A).
2. Trouvez les vecteurs propres associés.
3. Construisez les matrices (P) et (D).
4. Interprétez biologiquement les deux vecteurs propres.


Vérifiez l'ensemble de vos calcules à l'aide de Python.

---

##  **Interprétation biologique**

$$
(1,1)
\quad\text{avec}\quad
\lambda_1 = 6
$$

Cela décrit **une évolution conjointe** où les deux populations cellulaires augmentent ou diminuent *ensemble*.

→ **Comportement dominant**, coopération forte.

---

###  Deuxième vecteur propre

$$
(1,-1)
\quad\text{avec}\quad
\lambda_2 = 2
$$

Cela décrit une **relation opposée** :

1. si les cellules immunitaires augmentent,
1. les cellules tumorales diminuent (et inversement).

→ **Comportement secondaire**, opposé des dynamiques.

---

# TP dynamique économique

[Dynamique des espèces](https://github.com/Antoine07/maths/blob/main/Matrice/TPs/TP_dynamique_especes.md)

---

## [Retour au plan](https://antoine07.github.io/maths/)
