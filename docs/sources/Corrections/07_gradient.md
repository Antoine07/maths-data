#  **Correction – Approximation locale avec le gradient**

On veut montrer que pour de petits déplacements `(Delta x, Delta y)` :

$$
f(x+\Delta x, y+\Delta y)\approx f(x,y) + \nabla f(x,y)\cdot (\Delta x,\Delta y)
$$

C'est la **formule de linéarisation** : on approche la fonction par son plan tangent.

---

# **Calcul du gradient**

Pour

$$
f(x,y)= x^2 + 2y,
$$

on calcule les dérivées partielles :

$$
\frac{\partial f}{\partial x} = 2x,
\qquad
\frac{\partial f}{\partial y} = 2.
$$

Donc :

$$
\nabla f(x,y) = (2x, 2).
$$

---

# **2. Gradient au point ((1,1))**

$$
\nabla f(1,1) = (2\cdot 1, 2) = (2,2).
$$

---

# **3. Produit scalaire avec ((\Delta x,\Delta y))**

On prend :

$$
(\Delta x,\Delta y) = (0.1, -0.2).
$$

Produit scalaire :

$$
\nabla f(1,1)\cdot (\Delta x,\Delta y)
= 2(0.1) + 2(-0.2)
= 0.2 - 0.4
= -0.2.
$$

---

# **4. Valeur approximée**

$$
f(1,1) = 1^2 + 2\cdot 1 = 3.
$$

Approximation linéaire :

$$
f(1+\Delta x,1+\Delta y)
\approx 3 + (-0.2)
= 2.8.
$$

---

# **5. Vérification exacte**

Calculons exactement :

$$
f(1.1, 0.8) = (1.1)^2 + 2(0.8)
$$

$$
= 1.21 + 1.6 = 2.81.
$$

---

# **Conclusion**

L'approximation locale donne :

$$
\boxed{2.8}
$$

La valeur exacte est :

$$
\boxed{2.81}
$$

L'erreur est très petite :
**la linéarisation fonctionne très bien pour de petits déplacements.**


---

## Exercice Hessienne

```
Comme toutes les valeurs propres de la Hessienne sont positives, la matrice est définie positive : le point étudié est un minimum local strict et la fonction est localement convexe dans toutes les directions.
```