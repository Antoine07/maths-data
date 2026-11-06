
# **Correction détaillée et interprétée**

(C'est la même correction que précédemment mais **toujours replacée dans le contexte du système dynamique**.)

---

# 1. Valeurs propres

[
\det(A - \lambda I)
===================

\lambda^2 - 7\lambda + 10
= (\lambda - 5)(\lambda - 2).
]

[
\boxed{\lambda_1 = 5,\qquad \lambda_2 = 2.}
]

**Interprétation :**

* un mode d'évolution grandit d'un facteur **5** par unité de temps,
* l'autre grandit d'un facteur **2**.

---

# 2. Vecteurs propres

## Pour (\lambda = 5)

Système : (x = 2y).
Je prends (y=1).

[
v_1 =
\begin{pmatrix}
2\
1
\end{pmatrix}.
]

**Interprétation :**
Il existe une combinaison (2x + y) qui se dilate exactement par un facteur 5 à chaque période.

---

## Pour (\lambda = 2)

Système : (x = -y).
Je prends (y=1).

[
v_2 =
\begin{pmatrix}
-1\
1
\end{pmatrix}.
]

**Interprétation :**
Il existe une direction du système où l'évolution est plus lente (facteur 2).

---

# 3. Matrice (P)

[
P =
\begin{pmatrix}
2 & -1\
1 & 1
\end{pmatrix}.
]

**Interprétation :**
Passer de la base standard à la base des vecteurs propres = regarder le système dans ses **axes naturels d'évolution**.

---

# 4. Inverse de (P)

[
P^{-1}
======

\frac{1}{3}
\begin{pmatrix}
1 & 1\
-1 & 2
\end{pmatrix}.
]

---

# 5. Matrice diagonale (D)

[
D =
\begin{pmatrix}
5 & 0\
0 & 2
\end{pmatrix}.
]

**Interprétation :**
Dans la base des vecteurs propres, le système devient :

[
z_{t+1} =
\begin{pmatrix}
5 & 0\
0 & 2
\end{pmatrix}
z_t.
]

C'est **le modèle le plus simple possible** :
les deux composantes évoluent **indépendamment**.

---

# 6. Vérification

[
A = P D P^{-1}.
]

(Les calculs vérifient parfaitement.)

---

# 🔵 **Résumé interprétatif**

* Les **vecteurs propres** donnent les axes dans lesquels le système évolue naturellement.
* Les **valeurs propres** donnent la vitesse d'évolution dans ces axes.
* La diagonalisation permet d'écrire le système dans une forme où l'évolution est **découplée**, ce qui simplifie l'analyse, la simulation et la prédiction.

---