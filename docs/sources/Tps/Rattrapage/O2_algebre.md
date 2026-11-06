### Exercice — Algèbre linéaire et calcul numérique 

On considère la matrice réelle 

$$
A \in \mathbb{R}^{3\times 3}
$$

définie par :

$$
A =
\begin{pmatrix}
2 & 1 & 0 \\
1 & 2 & 1 \\
0 & 1 & 2
\end{pmatrix}
$$

---

## 1. Valeurs propres (approche théorique)

1. Écrire le polynôme caractéristique de la matrice (A).
2. Montrer que ce polynôme est de degré 3 et admet trois racines réelles.
3. Sans chercher à factoriser explicitement le polynôme, expliquer pourquoi une méthode numérique est pertinente pour déterminer les valeurs propres.

---

## 2. Valeurs propres par calcul numérique Numpy

On souhaite déterminer numériquement les valeurs propres de (A).

1. Écrire un script Python utilisant **NumPy** permettant de calculer les racines du polynôme caractéristique de (A).
2. Donner les valeurs propres approchées au millième près.
3. Vérifier le résultat à l'aide de la fonction `numpy.linalg.eig`.

*(Le code devra être commenté de manière concise.)*

---

## 3. Recherche des vecteurs propres

Pour chacune des valeurs propres (\lambda) trouvées :

1. Résoudre le système linéaire :

   $$
   (A-\lambda I_3),x = 0
   $$

2. Déterminer un **vecteur propre associé** (normalisation non exigée).
3. Vérifier numériquement que

$$
A x \approx \lambda x
$$

---

## 4. Comportement asymptotique d'une suite vectorielle

On considère la suite définie par :

$$
X_{n+1} = A X_n, \qquad X_0 =
\begin{pmatrix}
1\\
0\\
0
\end{pmatrix}
$$

1. Exprimer `Xn` en fonction de `A^n` et `X0`.
2. En utilisant la valeur propre dominante de  `A`, conjecturer le comportement de la suite `Xn` lorsque `quand n tend vers l'infini`.
3. Vérifier numériquement cette conjecture à l'aide d'un script Python (calcul de `Xn` pour `n` grand).

---

## 5. Calcul de limite et interprétation

On définit la suite normalisée :

$$
Y_n = \frac{X_n}{|X_n|}
$$

1. Montrer que la limite de (Y_n) existe.
2. Identifier cette limite à l'aide des vecteurs propres de (A).
3. Interpréter ce résultat du point de vue :

   * de l'algèbre linéaire,
   * d'un système dynamique discret.

---

## Conclusion attendue

La conclusion devra mettre en évidence :

* le rôle des **valeurs propres** dans la dynamique du système,
* l'intérêt du **calcul numérique Numpy** pour résoudre des équations polynomiales non triviales,
* le lien entre **limite**, **vecteur propre dominant** et stabilité asymptotique.
