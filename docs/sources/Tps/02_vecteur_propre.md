
## **Modèle de diffusion d'un produit sur deux marchés**

On étudie la manière dont la notoriété d'un nouveau produit se propage sur deux marchés, notés A et B.
On note :

$$
X_n =
\begin{pmatrix}
a_n \\
b_n
\end{pmatrix}
\quad\text{le niveau de notoriété au bout de n mois}.
$$

Le modèle retenu est :

$$
X_{n+1} = M X_n,
\qquad
M=
\begin{pmatrix}
1.15 & -0.4 \\
0.3 & 0.85
\end{pmatrix},
\qquad
X_0=
\begin{pmatrix}
120 \\
60
\end{pmatrix}.
$$

1. Calculer explicitement `X1 = M.X0`.
2. Calculer ensuite `X2 = M.X1`.
3. Interpréter brièvement l'évolution observée entre `n=0`, `n=1`, `n=2`.

---

## **Valeurs propres et vecteurs propres**

1. Calculer les valeurs propres de la matrice `M`.
2. Déterminer un vecteur propre pour chacune d'elles.
3. Justifier que la matrice est diagonalisable.
4. Expliquer pourquoi on peut écrire :

$$
X_0 = \alpha v_1 + \beta v_2.
$$

## **Expression générale de `Xn`**

1. En utilisant les résultats précédents, établir que :

$$
X_n = \alpha, \lambda_1^n v_1 + \beta, \lambda_2^n v_2.
$$

2. En déduire quels comportements apparaissent pour :

- la norme `|Xn|`,
- la proportion `an / bn`,

lorsque `n tend vers l'infini`.

## Interprétation économique

Rédigez une analyse de vos résultats.

## Partie facultative

On s'intéresse maintenant à la suite transformée suivante :

$$
Y_n = \frac{X_{n+1} - 0.5 X_n}{n}.
$$

1. Montrer que :

$$
Y_n
= \alpha, \left(\lambda_1 - \tfrac12\right)\frac{\lambda_1^n}{n} v_1

+ \beta, \left(\lambda_2 - \tfrac12\right)\frac{\lambda_2^n}{n} v_2.
$$

2. Déterminer le signe et le module de
   $$
   \lambda_1 - \tfrac12, \qquad \lambda_2 - \tfrac12.
   $$

3. Justifier que **la limite de `Yn`** lorsque `n tend vers l'infini` :

**n'est pas contrôlée** par la valeur propre dominante, **mais dépend de la valeur propre qui maximise**
  $$
  \frac{|\lambda_i|}{n} \quad\text{après renormalisation}.
  $$

4. Montrer que la limite finale est **nulle**, mais que :

$$
\lim_{n\to\infty} Y_n
$$

existe et **pointe dans la direction du vecteur propre associé à la valeur propre `lambda2`**
(et non `lambda1`.
