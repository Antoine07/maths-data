# I. Exercices — Multiplication de matrices

# **Exercice : Analyse d'un système économique à deux secteurs**

Une petite économie possède deux secteurs productifs :

* (x_t) = production du secteur **industrie**,
* (y_t) = production du secteur **services**.

Chaque période, leurs productions évoluent selon le modèle linéaire :

$$
\begin{pmatrix}
x_{t+1}\\
y_{t+1}
\end{pmatrix}
=

A
\begin{pmatrix}
x_t\\
y_t
\end{pmatrix},
\qquad
A =
\begin{pmatrix}
4 & 2\\
1 & 3
\end{pmatrix}.
$$

Ce modèle signifie :

* l'industrie dépend fortement de sa propre production et un peu de celle des services,
* les services dépendent faiblement de l'industrie et fortement d'eux-mêmes.

On cherche à comprendre :

1. **les directions d'évolution naturelles** du système,
2. **la vitesse de croissance** dans ces directions,
3. quel secteur domine à long terme,
4. comment simplifier le modèle grâce à la diagonalisation.

---

# **Questions**

### **1. Calculez les valeurs propres de (A).**

Interprétation attendue :
→ ce sont les **taux de croissance fondamentaux** de l'économie.

---

### **2. Calculez les vecteurs propres.**

Interprétation attendue :
→ chaque vecteur propre représente une **combinaison stable des deux secteurs**,
c'est-à-dire une direction où le système évolue **sans changer sa structure interne**.

---

### **3. Construisez la matrice (P) des vecteurs propres et son inverse $$(P^{-1})$$** (méthode de la matrice augmentée).

Interprétation attendue :
→ changement de base : passage de la base "secteurs industriels/services" à la base des "directions fondamentales"

---

### **4. Construisez la matrice diagonale (D).**

Interprétation attendue :
→ dans cette nouvelle base, les deux composantes du système **évoluent indépendamment**.

---

### **5. Vérifiez que $$(A = P D P^{-1})$$**

---

### **6. Interprétez économiquement les résultats suivants :**

#### a. La plus grande valeur propre $$(\lambda_1)$$ représente quoi ?

#### b. Le vecteur propre associé ((2,1)) indique quelle structure économique ?

#### c. Si la croissance dominante suit ce vecteur propre, quel secteur prendra la majorité à long terme ?

#### d. Pourquoi le modèle est plus simple dans la base diagonale ?


# **Conclusion pédagogique pour tes étudiants**

Cet exercice montre que :

* Les **vecteurs propres** décrivent les **structures naturelles et stables** d'un système.
* Les **valeurs propres** décrivent la **vitesse de croissance** de ces structures.
* La **diagonalisation** permet de transformer un système couplé en un système indépendant.
* En économie, data, IA ou dynamique, cela permet :

  * de prédire le long terme,
  * de simplifier les modèles,
  * d'identifier les modes essentiels.


## **Exercice 1 — Produit matrice–vecteur**

Calculer (Ax) :

$$
A=
\begin{pmatrix}
2 & -1\
4 & 3
\end{pmatrix},
\quad
x=
\begin{pmatrix}
3\
1
\end{pmatrix}.
$$

---

## **Exercice 2 — Produit de deux matrices**

Calculer (AB) :

$$
A=
\begin{pmatrix}
1 & 2\
0 & 1
\end{pmatrix},
\quad
B=
\begin{pmatrix}
3 & 1\
4 & 2
\end{pmatrix}.
$$

---

## **Exercice 3 — Produit non commutatif**

Vérifier que (AB \neq BA) :

$$
A=
\begin{pmatrix}
1 & 1\
0 & 1
\end{pmatrix},
\quad
B=
\begin{pmatrix}
0 & 2\
1 & 0
\end{pmatrix}.
$$

---

## **Exercice 4 — Interprétation géométrique**

Déterminer si (A) représente un étirement, une compression ou une symétrie :

$$
A=
\begin{pmatrix}
-2 & 0\
0 & 1
\end{pmatrix}.
$$

---

---

# II. Exercices — Diagonalisation

## **Exercice 5 — Valeurs propres**

Trouver les valeurs propres de :

$$
A=
\begin{pmatrix}
4 & 0\
0 & 1
\end{pmatrix}.
$$

*(Très simple : sert d'échauffement.)*

---

## **Exercice 6 — Vecteurs propres**

Trouver un vecteur propre de :

$$
A=
\begin{pmatrix}
2 & 1\
0 & 2
\end{pmatrix}.
$$

*(Attention : cette matrice n'a qu'une direction propre.)*

---

## **Exercice 7 — Matrice diagonalisable**

Diagonaliser complètement :

$$
A=
\begin{pmatrix}
3 & 1\
0 & 2
\end{pmatrix}.
$$

Questions :

1. Trouver les valeurs propres
2. Trouver les vecteurs propres
3. Former la matrice (P) des vecteurs propres
4. Former la matrice diagonale (D)
5. Vérifier que (A = P D P^{-1})

---

## **Exercice 8 — Matrice symétrique**

Diagonaliser :

$$
A=
\begin{pmatrix}
2 & 1\
1 & 2
\end{pmatrix}.
$$

*(Très important : les vecteurs propres seront orthogonaux.)*

---

## **Exercice 9 — Détection**

Dire si (A) est diagonalisable :

$$
A=
\begin{pmatrix}
1 & 1\
0 & 1
\end{pmatrix}.
$$

*(Matrice non diagonalisable classique.)*

---

## **Exercice 10 — Application directe**

Soit un vecteur initial :
$$
x_0 = \begin{pmatrix}1\1\end{pmatrix}
$$
et la matrice :
$$
A=
\begin{pmatrix}
3 & 0\
0 & 2
\end{pmatrix}.
$$

1. Calculer (A^5 x_0).
2. Interpréter le résultat à l'aide des valeurs propres.
