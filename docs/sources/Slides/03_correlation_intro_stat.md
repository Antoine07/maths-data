---
marp: true
theme: default
paginate: true
class: lead
---

# Corrélation et Régression linéaire

![Trois nuages de points donnent des exemples de relations croissante, décroissante et non linéaire.](images/couverture-correlation.svg)

---

## Objectif du chapitre

1. Comprendre le **lien entre deux variables quantitatives**
2. Mesurer ce lien avec la **corrélation**
3. Modéliser ce lien avec une **droite de régression**
4. Interpréter correctement les résultats

---

## Exemple de données

```python
import numpy as np

# Temps d'entraînement (heures/semaine)
x = np.array([1, 2, 3, 4, 5, 6, 7])

# Performance (score)
y = np.array([10, 12, 15, 18, 19, 22, 24])
```

---

## Visualisation du lien

```python
import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.xlabel("Temps d'entraînement")
plt.ylabel("Performance")
plt.title("Nuage de points")
plt.show()
```

---

## Question

1. Le lien semble-t-il **croissant** ou **décroissant** ?
2. Le lien semble-t-il **fort** ou **faible** ?
3. Peut-on prédire `y` à partir de `x` ?

---

## Corrélation : idée intuitive

> La corrélation mesure **à quel point deux variables évoluent ensemble**.

* positive → quand x augmente, y augmente
* négative → quand x augmente, y diminue
* proche de 0 → pas de lien linéaire clair

---

## Coefficient de corrélation de Pearson

Valeur comprise entre **–1 et +1**

```python
r = np.corrcoef(x, y)[0, 1]
r
```

---

## Interprétation de r

| Valeur de r  | Interprétation             |
| ------------ | -------------------------- |
| proche de 1  | lien linéaire fort positif |
| proche de –1 | lien linéaire fort négatif |
| proche de 0  | pas de lien linéaire       |

---

## Exercice 1 – Corrélation

On donne :

```python
a = np.array([2, 4, 6, 8, 10])
b = np.array([9, 7, 5, 3, 1])
```

1. Calculez la corrélation
2. Interprétez le résultat

```python
# TODO
```

---

## Attention : corrélation ≠ causalité

Exemples classiques :

* température et ventes de glaces
* nombre de pompiers et dégâts

> La corrélation décrit un lien, **pas une cause**.

---

# Régression linéaire

---

## Objectif de la régression

> Trouver la **meilleure droite** qui approxime la relation entre `x` et `y`.

Forme :

$$
y = ax + b
$$

* `a` : pente
* `b` : ordonnée à l’origine

---

## Calcul de la droite avec Numpy

```python
a, b = np.polyfit(x, y, 1)
a, b
```

---

## Visualisation de la droite

```python
y_pred = a * x + b

plt.scatter(x, y)
plt.plot(x, y_pred)
plt.show()
```

---

## Interprétation de la pente

> `a` représente la variation moyenne de `y` lorsque `x` augmente de 1.

Exemple :

* `a = 2.1` → +1 heure d’entraînement ≈ +2.1 points

---

## Exercice 2 – Régression

```python
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 4, 7, 9])
```

1. Calculez `a` et `b`
2. Tracez la droite
3. Interprétez la pente

```python
# TODO
```

---

## Résidus

Les **résidus** mesurent l’erreur du modèle :

$$
\text{résidu}_i = y_i - \hat{y}_i
$$

```python
residus = y - y_pred
residus
```

---

## Graphique des résidus

```python
plt.scatter(x, residus)
plt.axhline(0)
plt.xlabel("x")
plt.ylabel("Résidu")
plt.show()
```

---

## Interprétation des résidus

- résidus centrés autour de 0 → bon modèle
- structure visible → modèle inadapté
- résidus très grands → valeurs atypiques

---

## Lien entre corrélation et régression

1. Corrélation forte → droite pertinente
2. Corrélation faible → droite peu informative
3. Corrélation mesure **l’intensité**
4. Régression fournit un **modèle prédictif**

---

## Exercice 3 – Interprétation

1. Une corrélation de **0.95** implique-t-elle une causalité ?
2. Peut-on avoir une corrélation faible mais une relation non linéaire forte ?
3. Pourquoi toujours tracer un nuage de points avant de calculer `r` ?
