
# **Calcul des valeurs propres**

On part de la matrice :

$$
A=
\begin{pmatrix}
4 & 2\\
2 & 4
\end{pmatrix}.
$$

Les valeurs propres sont les solutions de :

$$
\det(A - \lambda I)=0.
$$

Calcul :

$$
A - \lambda I =
\begin{pmatrix}
4-\lambda & 2\
2 & 4-\lambda
\end{pmatrix}.
$$

Déterminant :

$$
\det(A - \lambda I)
= (4-\lambda)(4-\lambda) - 2\cdot 2.
$$

$$
= (4-\lambda)^2 - 4.
$$

Développons :

$$
(4-\lambda)^2 = 16 - 8\lambda + \lambda^2.
$$

Donc :

$$
\det(A - \lambda I)
= \lambda^2 - 8\lambda + 16 - 4
= \lambda^2 - 8\lambda + 12.
$$

Résolvons :

$$
\lambda^2 - 8\lambda + 12 = 0.
$$

Discriminant :

$$
\Delta = (-8)^2 - 4\times 1\times 12 = 64 - 48 = 16.
$$

Donc :

$$
\lambda = \frac{8 \pm \sqrt{16}}{2} = \frac{8 \pm 4}{2}.
$$

$$
\lambda_1 = 6,
\qquad
\lambda_2 = 2.
$$

**Deux valeurs propres réelles distinctes**, la matrice est donc diagonalisable.

---

# **Vecteurs propres**

`lambda=6`

On résout :

$$
(A - 6 I)v = 0.
$$

$$
A - 6I =
\begin{pmatrix}
4-6 & 2 \\
2 & 4-6
\end{pmatrix}
=
\begin{pmatrix}
-2 & 2\\
2 & -2
\end{pmatrix}.
$$

Système :

$$
-2x + 2y = 0 \quad \Longrightarrow \quad x = y.
$$

Un vecteur propre est donc :

$$
v_1 = (1,1).
$$

---

`lambda=2`, valeur propre moins dominante.

$$
A - 2I =
\begin{pmatrix}
4-2 & 2\\
2 & 4-2
\end{pmatrix}
=

\begin{pmatrix}
2 & 2\\
2 & 2
\end{pmatrix}
$$

Système :

$$
2x + 2y = 0 \quad \Longrightarrow \quad x = -y
$$

Un vecteur propre est donc :

$$
v_2 = (1,-1)
$$

---

#  **3. Construction des matrices (P) et (D)**

La matrice des vecteurs propres (colonnes) :

$$
P =
\begin{pmatrix}
1 & 1 \\
1 & -1
\end{pmatrix}.
$$

La matrice diagonale associée :

$$
D =
\begin{pmatrix}
6 & 0  \\
0 & 2
\end{pmatrix}.
$$

La relation vérifiée est :

$$
A P = P D.
$$

---

# **Interprétation biologique**

Premier vecteur propre : `v_1 = (1,1)` avec `lambda_1 = 6`

Direction :
$$
(x, y) \ \text{augmente ensemble}.
$$

Interprétation :

* Les cellules immunitaires et tumorales **évoluent conjointement**.
* Leur croissance est **synchronisée**, dans la même proportion.
* Dynamique **dominante**, car `lambda_1 = 6` est la plus grande valeur propre.
* À long terme, **tout système converge vers cette direction**, indépendamment des valeurs initiales.

**Coopération forte.**

---

Deuxième vecteur propre : `v_2 = (1,-1)` avec `lambda_2 = 2`

Direction :

$$
x \uparrow,\ y \downarrow
\quad\text{ou l'inverse}.
$$

Interprétation :

* Relation **opposée / compétitive**.
* Si les immunitaires augmentent, les tumorales diminuent.
* Si les tumorales augmentent, les immunitaires diminuent.
* Dynamique **secondaire**, car `lambda_2 < \lambda_1`.

Ce mode **disparaît à long terme** car il est moins puissant.

---

# **Conclusion biologique générale**

* Le système possède deux modes fondamentaux :

  1. **Coopération** (dominant)
  2. **Opposition** (faible)

* À long terme, la dynamique converge **vers le mode coopératif** ((1,1)).

> **Indépendamment du nombre initial de cellules immunitaires ou tumorales, le système évolue vers une proportion stable où les deux populations progressent ensemble.**

---

# Vérification avec Python

```python
import numpy as np

A = np.array([[4, 2],
              [2, 4]])

vals, vecs = np.linalg.eig(A)

print("Valeurs propres :", vals)
print("Vecteurs propres :\n", vecs)
```

Résultat attendu :

* valeurs propres : `[6. 2.]`
* vecteurs propres : colonnes proportional to `(1,1)` et `(1,-1)`
