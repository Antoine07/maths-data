# **TP – Analyse d'une fonction multivariée avec FastAPI, NumPy et Matplotlib**

Pour des fonctions multivariées comme (T(x,y)), on ne peut pas toujours calculer exactement la variation de la fonction lorsqu'on déplace légèrement les variables.
On utilise alors une **approximation linéaire**, issue du développement limité d'ordre 1 :

$$
T(x+dx, y+dy)
\approx
T(x,y)
+
\nabla T(x,y) \cdot
\begin{pmatrix}
dx \
dy
\end{pmatrix}.
$$

Cette formule repose sur une idée simple :

**près d'un point, toute fonction suffisamment régulière ressemble à un plan**
(son plan tangent).

Ainsi, la variation réelle :

$$
\Delta T_{\text{réel}} = T(x+dx,y+dy) - T(x,y)
$$

est souvent **très proche** de la variation prédite par le gradient :

$$
\Delta T_{\text{approx}} ;=;
\nabla T(x,y) \cdot (dx,dy).
$$

L'endpoint `/variation` du TP vous permet justement **de comparer** la variation réelle avec cette approximation mathématique.

> **Approximation linéaire :**
> Si une fonction multivariée est régulière, alors pour de petites variations ((dx,dy)),
$$
T(x+dx, y+dy) \approx T(x,y)+\nabla T(x,y)\cdot(dx,dy).
$$
> Le gradient donne donc la **meilleure approximation locale** de la variation de la fonction.
> Le TP vous fait comparer cette approximation avec la variation réelle.

---

Dans ce TP, vous allez :

1. Implémenter une fonction de deux variables (T(x,y)).
2. Calculer son **gradient**.
3. Créer **trois endpoints REST** avec **FastAPI** :

   * un endpoint qui renvoie la valeur de la fonction et son gradient,
   * un endpoint qui calcule une **variation locale** à l'aide de l'approximation linéaire,
   * un endpoint qui renvoie un **graphique PNG généré par Matplotlib**.
4. Tester l'API depuis un navigateur ou un client HTTP.
5. Comprendre comment les maths (gradient, variation locale) s'appliquent à un service RESTful.

---

# **Fonction étudiée**

Dans ce TP, on étudie la fonction :

$$
T(x,y) = x^2 + 2y
$$

Et son gradient :

$$
\nabla T(x,y) = (2x,; 2)
$$

Vous devrez :

* coder cette fonction,
* coder le gradient correspondant,
* utiliser NumPy pour effectuer les calculs.

---

# 📌 **2. Travail demandé : création d'une API FastAPI**

Créez un fichier `main.py` et construisez une API avec **FastAPI** contenant les **trois endpoints suivants :**

---

## **Endpoint 1 : /temperature**

**Entrées :** `x` et `y` (paramètres float dans l'URL)
**Rôle :**

* calculer la valeur (T(x,y)),
* calculer le gradient (\nabla T(x,y)),
* renvoyer un **JSON** contenant :

  * les entrées,
  * la valeur de la température,
  * les deux composantes du gradient,
  * une phrase d'interprétation simple.

**Exemple attendu :**

```
GET /temperature?x=1&y=2
```

---

## **Endpoint 2 : /variation**

Cet endpoint doit estimer la variation locale de la fonction.

On rappelle l'approximation linéaire :

$$
\Delta T \approx \nabla T(x,y) \cdot
\begin{pmatrix}
dx\
dy
\end{pmatrix}
$$

**Entrées :** `x`, `y`, `dx`, `dy`

**Travail demandé :**

1. calculer l'approximation linéaire
   $$
   \nabla T(x,y) \cdot (\Delta x, \Delta y)
   $$
2. calculer la variation réelle
   $$
   T(x+dx, y+dy) - T(x,y)
   $$
3. envoyer un JSON contenant :

   * $\Delta T$ approximé
   * $\Delta T$ réel
   * l'erreur entre les deux

---

## **Endpoint 3 : /plot**

Cet endpoint doit générer une **image PNG** d'une carte de chaleur montrant la fonction (T(x,y)).

**Travail demandé :**

1. Créer une grille (meshgrid) avec NumPy.
2. Calculer (T(x,y)) sur cette grille.
3. Créer un graphique Matplotlib avec `contourf`.
4. Retourner l'image en PNG via un `StreamingResponse`.

**Résultat attendu :**

Au navigateur : un **graphique** montrant la fonction.

---

#  **Lancement de l'API**

Demander aux étudiants de lancer le serveur :

```
uvicorn main:app --reload
```

Puis tester :

* [http://localhost:8001/temperature?x=1&y=2](http://localhost:8001/temperature?x=1&y=2)
* [http://localhost:8001/variation?x=1&y=2&dx=0.1&dy=-0.05](http://localhost:8001/variation?x=1&y=2&dx=0.1&dy=-0.05)
* [http://localhost:8001/plot](http://localhost:8001/plot)

---

# **Questions à traiter dans le rapport**

1. Que représente le gradient $\nabla T(x,y)$ dans ce contexte ?
2. Pourquoi la variation locale prédite est-elle parfois très proche de la variation réelle ?
3. Comment interpréter le signe de $\Delta T$ ?
4. Si $\Delta T \approx 0$, que peut-on dire des variations locales ?
5. Comment l'API pourrait être modifiée pour analyser d'autres fonctions ?

