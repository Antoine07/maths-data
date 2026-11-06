> Qu’est-ce que signifie exactement " approximation au point (x, y) " avec le gradient, et comment cela se traduit dans le TP ?

Je vais donc :

1. Rappeler le TP en une phrase.
2. Expliquer l’approximation linéaire **mathématiquement** au point ((x_0,y_0)).
3. Faire un exemple numérique détaillé.
4. Montrer comment cela correspond exactement à ce que fait l’endpoint `/variation` dans le code.

---

## 1. Rappel du cadre du TP

Fonction choisie dans le TP :

$$
T(x,y) = x^2 + 2y
$$

Gradient :

$$
\nabla T(x,y) = \left( \frac{\partial T}{\partial x}, \frac{\partial T}{\partial y} \right) = (2x,; 2)
$$

Le but du TP :

* calculer (T(x,y)) et (\nabla T(x,y)),
* comparer la variation **approximée** de (T) avec la variation **réelle** quand on passe de ((x,y)) à ((x+dx,y+dy)).

L’endpoint `/variation` est justement là pour cela.

---

## 2. L’idée de l’approximation au point ((x_0,y_0))

On fixe un point ((x_0,y_0)).
On considère une petite variation :

$$
\Delta x = dx, \quad \Delta y = dy
$$

On passe donc du point ((x_0,y_0)) au point ((x_0+dx,; y_0+dy)).

Deux manières de regarder la variation de (T) :

### 2.1. Variation réelle

C’est la vraie différence :

$$
\Delta T_{\text{réel}}
= T(x_0+dx, y_0+dy) - T(x_0, y_0)
$$

On la calcule en remplaçant directement dans la formule de (T).

---

### 2.2. Variation approximée (linéaire)

La formule d’approximation (développement limité d’ordre 1) dit que pour des petites variations ((dx,dy)) :

$$
\Delta T \approx \nabla T(x_0,y_0) \cdot
\begin{pmatrix}
dx\
dy
\end{pmatrix}
$$

Autrement dit :

$$
\Delta T_{\text{approx}} \approx
\frac{\partial T}{\partial x}(x_0,y_0),dx
+
\frac{\partial T}{\partial y}(x_0,y_0),dy
$$

Dans notre cas :

$$
\frac{\partial T}{\partial x}(x,y) = 2x
\quad\text{et}\quad
\frac{\partial T}{\partial y}(x,y) = 2
$$

Donc, au point ((x_0,y_0)) :

$$
\Delta T_{\text{approx}} \approx 2x_0,dx + 2,dy
$$

Cette formule ne vient pas du code, elle vient des maths.
Le code ne fait que l’évaluer numériquement.

---

## 3. Exemple numérique détaillé

Prenons un exemple concret, très proche de ce que fait l’endpoint `/variation`.

Choix du point :

$$
x_0 = 1,\quad y_0 = 2
$$

Choix des petites variations :

$$
dx = 0.1,\quad dy = -0.05
$$

### 3.1. Calcul de la variation approximée

Au point ((1,2)), le gradient vaut :

$$
\nabla T(1,2) = (2 \cdot 1,; 2) = (2,; 2)
$$

On considère le vecteur variation :

$$
\Delta x =
\begin{pmatrix}
dx\
dy
\end{pmatrix}
=============

\begin{pmatrix}
0.1\
-0.05
\end{pmatrix}
$$

Produit scalaire :

$$
\Delta T_{\text{approx}}
= (2,2) \cdot (0.1,; -0.05)
= 2 \cdot 0.1 + 2 \cdot (-0.05)
= 0.2 - 0.1
= 0.1
$$

Donc, l’approximation linéaire prédit :

> Quand on passe de (1,2) à (1.1, 1.95), la température augmente d’environ 0.1.

---

### 3.2. Calcul de la variation réelle

On calcule maintenant :

$$
T(x,y) = x^2 + 2y
$$

D’abord la valeur au point initial :

$$
T(1,2) = 1^2 + 2 \cdot 2 = 1 + 4 = 5
$$

Ensuite au point déplacé :

$$
T(1.1, 1.95)
= (1.1)^2 + 2 \cdot 1.95
= 1.21 + 3.9
= 5.11
$$

Variation réelle :

$$
\Delta T_{\text{réel}} = 5.11 - 5 = 0.11
$$

Comparaison :

* approximation : 0.10
* réel : 0.11

Les deux sont très proches. L’écart de 0.01 vient des termes d’ordre supérieur (l’approximation est linéaire, la fonction est quadratique).

C’est exactement cela que le TP veut faire comprendre :
localement, pour de petites variations, la variation réelle est bien approximée par le produit du gradient au point par le vecteur de variation.

---

## 4. Comment cela se traduit dans l’endpoint `/variation`

Dans la correction que j’ai donnée, l’endpoint `/variation` fait exactement ces calculs.

Conceptuellement, il exécute :

1. Calcul du gradient en ((x,y)) :

```python
g = grad_T(x, y)  # renvoie $$2*x, 2$$
```

2. Construction du vecteur variation :

```python
delta_vec = np.array($$dx, dy$$)
```

3. Variation approximée :

```python
delta_T_approx = float(g @ delta_vec)
# c'est ∇T(x,y) · (dx, dy)
```

4. Variation réelle :

```python
T_old = T(x, y)
T_new = T(x + dx, y + dy)
delta_T_real = T_new - T_old
```

5. Comparaison des deux :

```python
difference = delta_T_real - delta_T_approx
```

Et tout cela est renvoyé dans un JSON pour lisibilité.

---

## 5. Résumé en une phrase pour vos étudiants

Vous pouvez formuler ainsi dans le cours ou l’énoncé :

> Au point ((x_0,y_0)), le gradient (\nabla T(x_0,y_0)) donne la meilleure approximation linéaire de la variation de (T) pour de petites perturbations ((dx,dy)).
> Plutôt que de recalculer exactement (T(x_0+dx,y_0+dy)), on peut approcher la variation par
> (\Delta T \approx \nabla T(x_0,y_0)\cdot(dx,dy)).
