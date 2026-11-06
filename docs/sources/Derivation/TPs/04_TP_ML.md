
# entraînement d'un modèle avec une fonction de perte pathologique

Une équipe de data scientists conçoit un mini-modèle interne pour prédire le taux d'engagement d'un utilisateur en fonction de deux paramètres ajustables (x) et (y).

Pour tester la robustesse de leur algorithme de descente de gradient, ils utilisent une **fonction de perte artificielle** présentant un comportement non convexe typique des réseaux neuronaux :

$$
L(x,y) = x^4 - 2x^2 + y^2 - 3xy.
$$

Cette fonction a été construite pour **imiter** :

* des vallées étroites (termes en (x^4)),
* des dépendances croisées (terme en (-3xy)),
* une géométrie instable proche d'un **point-selle**,
* un paysage d'optimisation difficile, comme en deep learning.

---

##  **Calculer les dérivées partielles** de (L).

On demande `(L_x)` et `(L_y)`.

---

##  **Déterminer les points critiques** en résolvant

$$
\nabla L = (0,0).
$$

---

##  **Calculer les dérivées secondes** et établir la **matrice Hessienne** de (L).

---

##  **Évaluer la Hessienne en chaque point critique** identifié.

---

##  **Classifier les points critiques** (min local, max local, point-selle) en utilisant :

$$
\det(H), \quad L_{xx},
$$

et le test standard du Hessien.

---

##  **Interprétation machine learning :**

a) Pourquoi un point-selle peut-il **ralentir fortement** la descente de gradient ?

b) Pourquoi un minimum **non strict** ou mal conditionné rend-il l'apprentissage instable ?

c) Dans cet exemple, quelles régions du plan ((x,y)) seraient **dangereuses** pour un optimiseur naïf comme SGD ?

---

## **Utilisation pratique :**

Implémenter la descente de gradient sur (L(x,y)) à partir de plusieurs points initiaux, et observer :

* convergence lente,
* oscillations,
* stagnation autour des points-selles,
* sensibilité au taux d'apprentissage.
