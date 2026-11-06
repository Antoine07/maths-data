# I. Corrections — Multiplication de matrices

---

## **Exercice 1 — Produit matrice–vecteur**

$$
A=\begin{pmatrix}
2 & -1\
4 & 3
\end{pmatrix},
\quad
x=\begin{pmatrix}
3\
1
\end{pmatrix}.
$$

Calcul :

$$
Ax =
\begin{pmatrix}
2\cdot 3 + (-1)\cdot 1 \
4\cdot 3 + 3\cdot 1
\end{pmatrix}
=

\begin{pmatrix}
6 - 1 \
12 + 3
\end{pmatrix}
=

\begin{pmatrix}
5\
15
\end{pmatrix}.
$$

---

## **Exercice 2 — Produit de deux matrices**

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

$$
AB =
\begin{pmatrix}
1\cdot 3 + 2\cdot 4 & 1\cdot 1 + 2\cdot 2\
0\cdot 3 + 1\cdot 4 & 0\cdot 1 + 1\cdot 2
\end{pmatrix}
=

\begin{pmatrix}
3 + 8 & 1 + 4\
4 & 2
\end{pmatrix}
=

\begin{pmatrix}
11 & 5\
4 & 2
\end{pmatrix}.
$$

---

## **Exercice 3 — Produit non commutatif**

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

Calcul de (AB) :

$$
AB =
\begin{pmatrix}
1\cdot 0 + 1\cdot 1 & 1\cdot 2 + 1\cdot 0\
0\cdot 0 + 1\cdot 1 & 0\cdot 2 + 1\cdot 0
\end{pmatrix}
=

\begin{pmatrix}
1 & 2\
1 & 0
\end{pmatrix}.
$$

Calcul de (BA) :

$$
BA =
\begin{pmatrix}
0\cdot 1 + 2\cdot 0 & 0\cdot 1 + 2\cdot 1\
1\cdot 1 + 0\cdot 0 & 1\cdot 1 + 0\cdot 1
\end{pmatrix}
=

\begin{pmatrix}
0 & 2\
1 & 1
\end{pmatrix}.
$$

$$
AB \neq BA.
$$

---

## **Exercice 4 — Interprétation géométrique**

$$
A=
\begin{pmatrix}
-2 & 0\
0 & 1
\end{pmatrix}.
$$

Effet :

* le facteur (-2) → étirement par 2 **et inversion** sur l’axe (x),
* le facteur (1) → aucune modification sur (y).

Transformation = **symétrie par rapport à l’axe (y)** + **étirement**.

---

# II. Corrections — Diagonalisation

---

## **Exercice 5 — Valeurs propres**

$$
A=
\begin{pmatrix}
4 & 0\
0 & 1
\end{pmatrix}.
$$

Les valeurs propres sont les éléments diagonaux :

$$
\lambda_1 = 4,\quad \lambda_2 = 1.
$$

---

## **Exercice 6 — Vecteur propre simple**

$$
A=
\begin{pmatrix}
2 & 1\
0 & 2
\end{pmatrix}.
$$

Valeur propre :

$$
\det(A - \lambda I) = 0
\quad\Rightarrow\quad
\begin{vmatrix}
2-\lambda & 1\
0 & 2-\lambda
\end{vmatrix}
= (2-\lambda)^2 = 0.
$$

$$
\lambda = 2 \quad (\text{multiplicité algébrique } = 2)
$$

Résolution de :
$$
(A - 2I)v = 0
\quad\Rightarrow\quad
\begin{pmatrix}
0 & 1\
0 & 0
\end{pmatrix}
\begin{pmatrix}
x\y
\end{pmatrix}
= 0.
$$

Système :
$$
y = 0,
\quad x \text{ libre}.
$$

Vecteur propre :
$$
v = \begin{pmatrix}1\0\end{pmatrix}.
$$

Comme il n’y a qu’un seul vecteur propre → matrice non diagonalisable.

---

## **Exercice 7 — Matrice diagonalisable**

$$
A=
\begin{pmatrix}
3 & 1\
0 & 2
\end{pmatrix}.
$$

### 1. Valeurs propres

$$
\det(A-\lambda I)=
\begin{vmatrix}
3-\lambda & 1\
0 & 2-\lambda
\end{vmatrix}
= (3-\lambda)(2-\lambda).
$$

$$
\lambda_1 = 3,\quad \lambda_2 = 2.
$$

### 2. Vecteurs propres

Pour (\lambda = 3) :
$$
(A-3I)v =
\begin{pmatrix}
0 & 1\
0 & -1
\end{pmatrix}
\begin{pmatrix}
x\y
\end{pmatrix}
= 0.
$$

$$
y = 0, \quad x \text{ libre}.
$$
$$
v_1 = \begin{pmatrix}1\0\end{pmatrix}.
$$

Pour (\lambda = 2) :
$$
(A-2I)v =
\begin{pmatrix}
1 & 1\
0 & 0
\end{pmatrix}
\begin{pmatrix}
x\y
\end{pmatrix}
= 0.
$$

$$
x + y = 0 \Rightarrow x = -y.
$$

Vecteur propre :
$$
v_2 = \begin{pmatrix}1\-1\end{pmatrix}.
$$

### 3. Matrice (P)

$$
P = \begin{pmatrix}1 & 1\ 0 & -1\end{pmatrix}.
$$

### 4. Matrice (D)

$$
D=
\begin{pmatrix}
3 & 0\
0 & 2
\end{pmatrix}.
$$

---

## **Exercice 8 — Matrice symétrique**

$$
A=
\begin{pmatrix}
2 & 1\
1 & 2
\end{pmatrix}.
$$

### 1. Valeurs propres

$$
\det(A-\lambda I)
=====

\begin{vmatrix}
2-\lambda & 1\
1 & 2-\lambda
\end{vmatrix}
= (2-\lambda)^2 - 1.
$$

$$
\lambda^2 - 4\lambda + 3 = 0.
$$

$$
\lambda_1 = 1,\quad \lambda_2 = 3.
$$

### 2. Vecteurs propres

Pour (\lambda = 1) :
$$
(A - I)v =
\begin{pmatrix}
1 & 1\
1 & 1
\end{pmatrix}
\begin{pmatrix}
x\y
\end{pmatrix}
= 0.
$$

$$
x + y = 0.
$$
$$
v_1 = \begin{pmatrix}1\-1\end{pmatrix}.
$$

Pour (\lambda = 3) :
$$
(A - 3I)v =
\begin{pmatrix}
-1 & 1\
1 & -1
\end{pmatrix}
\begin{pmatrix}
x\y
\end{pmatrix}
= 0.
$$

$$
-x + y = 0.
$$
$$
v_2 = \begin{pmatrix}1\1\end{pmatrix}.
$$

### 3. Orthogonalité

$$
v_1 \cdot v_2 = 1\cdot 1 + (-1)\cdot 1 = 0.
$$

Les vecteurs propres sont bien orthogonaux → normal pour une matrice symétrique.

### 4. Matrice (D)

$$
D =
\begin{pmatrix}
1 & 0\
0 & 3
\end{pmatrix}.
$$

---

## **Exercice 9 — Détection**

$$
A=
\begin{pmatrix}
1 & 1\
0 & 1
\end{pmatrix}.
$$

Valeur propre unique : (\lambda = 1).
Un seul vecteur propre indépendant.

Conclusion : **A n’est pas diagonalisable.**

---

## **Exercice 10 — Application directe**

$$
A=
\begin{pmatrix}
3 & 0\
0 & 2
\end{pmatrix},
\quad x_0 = \begin{pmatrix}1\1\end{pmatrix}.
$$

On calcule :

$$
A^5 x_0 =
\begin{pmatrix}
3^5 & 0\
0 & 2^5
\end{pmatrix}
\begin{pmatrix}
1\1
\end{pmatrix}
=

\begin{pmatrix}
243\
32
\end{pmatrix}.
$$

### Interprétation

* la composante associée à (\lambda = 3) croît beaucoup plus vite,
* la composante associée à (\lambda = 2) croît plus lentement.

**Le vecteur finit par pointer presque entièrement dans la direction du vecteur propre dominant.**
