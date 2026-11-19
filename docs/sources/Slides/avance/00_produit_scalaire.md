---
marp: true
html: true
---

# Produit scalaire pour les données

## Du panier au score d’un perceptron

Un produit scalaire associe deux listes de nombres de même longueur. Il multiplie les valeurs qui se correspondent, puis additionne les produits.

Nous partons d’un panier de courses pour comprendre cette opération avant de l’utiliser avec des données et des poids.

---

## Exemple — Calculer le prix d’un panier

Gardons le même ordre dans les deux listes : pommes, lait, pain.

| Produit | Prix unitaire (€) | Quantité |
|:---|---:|---:|
| Pommes | 2 | 2 |
| Lait | 1 | 1 |
| Pain | 3 | 1 |

Les quantités sont $q=(2,1,1)$ et les prix sont $p=(2,1,3)$. Le prix total vaut :

$$
2\times2+1\times1+1\times3=8\text{ euros}.
$$

On multiplie chaque quantité par le prix correspondant, puis on additionne. Garder le même ordre dans les deux listes est essentiel.

---

## Écriture générale

Pour deux vecteurs de même longueur, le produit scalaire se note :

$$
q^Tp=q_1p_1+q_2p_2+\cdots+q_np_n.
$$

Le résultat est un nombre. Dans l’exemple du panier, c’est le prix total.

**À vous de jouer.** Avec l’ordre pommes, lait, pain, calculez le prix de ces paniers :

1. $(1,2,1)$.
2. $(0,3,2)$.
3. $(3,0,2)$. Un budget de 10 € suffit-il ?

---

## Des produits aux caractéristiques

Dans une donnée, les nombres décrivent des caractéristiques. Un modèle leur associe des poids :

$$
z=x^Tw+b.
$$

Le produit scalaire $x^Tw$ combine les caractéristiques avec les poids. Le biais $b$ décale le score $z$.

Pour un perceptron, une règle de seuil transforme ensuite ce score en classe : par exemple, classe 1 si $z\geq0$, classe 0 sinon.

---

## Avec NumPy : l’opérateur `@`

Quand `x` et `poids` sont deux vecteurs de même longueur, `x @ poids` calcule leur produit scalaire.

```python
import numpy as np

x = np.array([2, 1, 1])
poids = np.array([2, 1, 3])

score = x @ poids
print(score)
```

L’opérateur `@` multiplie les coordonnées qui se correspondent et additionne les résultats. Ici, il reprend le calcul du panier.

---

## Exercices préparatoires — Du produit scalaire au perceptron

Ces exercices préparent au calcul d’un score et à la décision d’un perceptron. Faites les calculs à la main avant de les vérifier avec NumPy.

### 1. Calculer un score et décider

$$
X=\begin{bmatrix}2&1\\0&2\\3&0\end{bmatrix},\qquad
w=\begin{bmatrix}1\\-1\end{bmatrix},\qquad b=0{,}5.
$$

Pour chaque ligne $x_i$ de $X$ :

1. Calculez le produit scalaire $x_i^Tw$.
2. Ajoutez le biais pour obtenir le score $z_i=x_i^Tw+b$.
3. Attribuez la classe 1 si $z_i\geq0$, et la classe 0 sinon.

---

## Comparer une prédiction à la classe attendue

Les classes réelles sont $y=(1,1,0)$. On note $\widehat y_i$ la classe prédite à l’exercice précédent.

1. Pour chaque observation, dites si la prédiction est correcte.
2. Calculez $y_i-\widehat y_i$ pour les trois observations.
3. Que signifie une différence égale à 0, à 1 ou à $-1$ ?

---

## Refaire les calculs avec NumPy

Complétez les lignes pour calculer les scores de toutes les observations, puis leurs classes prédites. `np.where(condition, valeur_si_vrai, valeur_si_faux)` applique une règle à tout un tableau.

```python
import numpy as np

X = np.array([[2, 1], [0, 2], [3, 0]])
poids = np.array([1, -1])
biais = 0.5

scores = ...  # Indice : X @ poids calcule un produit scalaire par ligne.
classes_predites = ...
```

**À retenir :** un produit scalaire combine les caractéristiques et les poids pour produire un score. Le biais décale ce score ; une règle de seuil le transforme en classe.
