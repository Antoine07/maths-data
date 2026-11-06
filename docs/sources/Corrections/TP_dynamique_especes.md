
#  **Correction — Modèle de compétition entre deux espèces**

La matrice du modèle est :

$$
M=
\begin{pmatrix}
1.2 & -0.3 \\
-0.2 & 1.1
\end{pmatrix}.
\qquad
X_0 =
\begin{pmatrix}
100 \\
80
\end{pmatrix}.
$$

---

#  **Calculs itératifs**

## a) Calcul de `X1 = M.X0`

$$
X_1=
\begin{pmatrix}
1.2 & -0.3 \\
-0.2 & 1.1
\end{pmatrix}
\begin{pmatrix}
100 \\
80
\end{pmatrix}
$$

Composante par composante :

* première ligne :

$$
1.2 \cdot 100 - 0.3 \cdot 80
=120 - 24 = 96
$$

* deuxième ligne :

$$
-0.2 \cdot 100 + 1.1 \cdot 80
=-20 + 88 = 68
$$

$$
\boxed{
X_1 = \begin{pmatrix} 
96 \\ 
68 \end{pmatrix}
}
$$

---

## b) Calcul de `X2 = M.X1`

$$
X_2=
\begin{pmatrix}
1.2 & -0.3 \\
-0.2 & 1.1
\end{pmatrix}
\begin{pmatrix}
96 \\
68
\end{pmatrix}
$$

* première ligne :

$$
1.2\cdot96 - 0.3\cdot68 = 115.2 - 20.4 = 94.8
$$

* deuxième ligne :

$$
-0.2\cdot96 + 1.1\cdot68 = -19.2 + 74.8 = 55.6
$$

$$
\boxed{
X_2 = \begin{pmatrix} 
94.8 \\ 
55.6 \end{pmatrix}
}
$$

## Interprétation immédiate

* Les deux populations **diminuent**.
* L'espèce B `68 → 55.6` décroît **plus vite** que l'espèce A.
* Les interactions négatives ralentissent fortement la croissance.

---

#  **Valeurs propres**

On calcule le polynôme caractéristique :

$$
\det(M - \lambda I)
=

\begin{vmatrix}
1.2-\lambda & -0.3 \\
-0.2 & 1.1-\lambda
\end{vmatrix}
$$

$$
= (1.2-\lambda)(1.1-\lambda) - (0.06)
$$

Développement :

$$
= \lambda^2 - 2.3\lambda + (1.32 - 0.06)
$$

$$
= \lambda^2 - 2.3\lambda + 1.26
$$

Résolution :

$$
\lambda =
\frac{2.3 \pm \sqrt{2.3^2 - 4\times1.26}}{2}
$$

$$
\Delta = 5.29 - 5.04 = 0.25
$$

$$
\boxed{
\lambda_1 = \frac{2.3 + 0.5}{2} = 1.4
}
$$

$$
\boxed{
\lambda_2 = \frac{2.3 - 0.5}{2} = 0.9
}
$$


##  **Vecteurs propres**

### Pour `lambda1 = 1.4`

On résout :

$$
(M - 1.4I)v = 0
$$

$$
\begin{pmatrix}
-0.2 & -0.3 \\
-0.2 & -0.3
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
=0
$$

Système :

$$
-0.2x - 0.3y = 0 \quad \Rightarrow \quad x = -1.5 y
$$

Un vecteur propre est :

$$
\boxed{
v_1 = \begin{pmatrix}
 -3 \\ 
 2 
 \end{pmatrix}
}
$$

---

### Pour `lambda2 = 0.9`

$$
M - 0.9I=
\begin{pmatrix}
0.3 & -0.3 \\
-0.2 & 0.2
\end{pmatrix}
$$

Système :

$$
0.3x - 0.3y = 0 \quad \Rightarrow \quad x = y
$$

$$
\boxed{
v_2 = \begin{pmatrix} 
1 \\ 
1 
\end{pmatrix}
}
$$

---

##  **Interprétation biologique**

### Valeur propre dominante : `lambda1 = 1.4`

C'est celle qui commande l'évolution à long terme.

Le vecteur propre associé :

$$
v_1 = (-3, 2)
$$

signifie :

* les populations évoluent **en opposition** : quand l'une augmente, l'autre diminue,
* la composante négative `–3` indique que l'espèce A souffre beaucoup plus de la concurrence.

> À long terme, la dynamique tend vers un antagonisme fort entre les espèces.


##  La seconde valeur propre : `lambda2 = 0.9 < 1`

Cela veut dire :

* la composante proportionnelle au vecteur `(1,1)` **disparaît progressivement**,
* autrement dit, la coexistence harmonieuse n'est pas stable.


## **Comportement asymptotique**

$$
X_0 = c_1 v_1 + c_2 v_2
$$

où :

* `v1` et `v2` = vecteurs propres de la matrice,
* `(c1, c2)` = coefficients de la *décomposition* du vecteur initial dans cette base.

Pourquoi c'est possible ?
Parce que une matrice 2x2 qui a 2 vecteurs propres **forme une base** de R2.


Ensuite, comme :

$$
A v_1 = \lambda_1 v_1
\quad
\text{et}
\quad
A v_2 = \lambda_2 v_2,
$$

on obtient :

$$
X_n = A^n X_0 = c_1 \lambda_1^n v_1 + c_2 \lambda_2^n v_2.
$$


$$
\lambda_1 = 1, \quad \lambda_2 = 0.5
$$

Donc :

$$
A^n X_0 = c_1 1^n v_1 + c_2 0.5^n v_2.
$$

Quand `n tend vers l'inifi`

$$
(0.5)^n \to 0
$$

* seule la partie **en direction du vecteur propre dominant** `V1` reste.

Donc :

$$
X_n \longrightarrow C, v_1
\quad\text{avec}\quad C=c_1.
$$

**proportion interne du vecteur propre**

$$
x : y = -3 : 2.
$$

Mais comme 

$$
(\lambda_2^n \to 0),
$$

cette proportion **disparaît** à long terme.

Le vecteur propre dominant impose la **tendance finale**.

$$
X_n \to C, v_1
\quad (\text{car }\lambda_1 \text{ est le plus grand})
$$

> Le vecteur propre secondaire ne sert qu'à décrire l'évolution **à court terme**.

Sa proportion interne est :

$$
x : y = -3 : 2
$$

S'éteint quand `n tend vers l'infini` car 

$$
\lambda2^n \to 0
$$

Cela signifie biologiquement :

> L'interaction nuit tellement à l'espèce A qu'elle s'effondre, tandis que l'espèce B se maintient mieux.


##  **Vérification avec Python (optionnelle)**

```python
import numpy as np

M = np.array([[1.2, -0.3],
              [-0.2, 1.1]])

X = np.array([100, 80], dtype=float)

for n in range(6):
    print(n, X)
    X = M @ X

# Valeurs propres :
vals, vecs = np.linalg.eig(M)
print(vals)
print(vecs)
```

##  **Conclusion générale**

* La dynamique matricielle révèle la tendance profonde du système.
* La valeur propre dominante décrit le comportement à long terme.
* Le vecteur propre dominant montre la **proportion dans laquelle les espèces s'organisent**.
* Ici, la compétition extrême pousse le système vers une **relation défavorable**, où l'espèce A est fortement pénalisée.
