---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# Covariance et correlation avec NumPy

## Cours + corrections detaillees

![Trois petits nuages illustrent une relation croissante, une relation décroissante et une relation non linéaire.](../images/couverture-correlation.svg)

---

## Objectifs

1. Calculer covariance et correlation en Python
2. Expliquer les fonctions `np.cov` et `np.corrcoef`
3. Maitriser la convention population (`ddof=0`)

---

## Convention sur la covariance

On reprend la distinction du [chapitre descriptif](01_stat_descriptive.md) : décrire les couples observés ou estimer la covariance d'une population plus large.

Pour décrire les couples observés, on divise par $n$ :

$$
\mathrm{Cov}(X,Y)=\frac{1}{n}\sum (x_i-\bar{x})(y_i-\bar{y})
$$

En NumPy :

1. `np.mean((x-x.mean())*(y-y.mean()))`
2. `np.cov(x, y, bias=True)[0, 1]`

Pour l'estimation usuelle à partir de couples indépendants de même distribution, avec moyennes estimées sur ces couples, on divise par `n−1` : `np.cov(x, y, bias=False)[0, 1]`.

Les vecteurs d'écarts sont centrés sur les mêmes $n$ observations. La correction n'est pas `n−2` parce qu'il y a deux variables. Contrairement à `np.var`, `np.cov` utilise par défaut le dénominateur `n−1`.

---

## Exercice 2 - Donnees

```python
import numpy as np

x = np.array([1, 2, 3], dtype=float)
y = np.array([2, 4, 5], dtype=float)
```

---

## Exercice 2 - Moyennes

Consigne :

1. Calculez $\bar{x}$ et $\bar{y}$
2. Ecrivez les vecteurs centres

<details>
<summary>Afficher la correction</summary>

```python
mx = np.mean(x)
my = np.mean(y)

xc = x - mx
yc = y - my

print(mx, my)  # 2.0 3.6666666666666665
print(xc)      # [-1.  0.  1.]
print(yc)      # [-1.66666667  0.33333333  1.33333333]
```
</details>

---

## Exercice 2 - Covariance (population)

Consigne :

1. Calculez la covariance manuellement
2. Verifiez avec NumPy (`ddof=0`)
3. Comparez avec la version echantillon (`ddof=1`)

<details>
<summary>Afficher la correction</summary>

```python
cov_pop_manual = np.mean((x - mx) * (y - my))
cov_pop_numpy  = np.cov(x, y, bias=True)[0, 1]
cov_sample     = np.cov(x, y, bias=False)[0, 1]

print(cov_pop_manual)  # 1.0
print(cov_pop_numpy)   # 1.0
print(cov_sample)      # 1.5
```

Population :

$$
\mathrm{Cov}=1
$$

Point cle : `np.cov` est en `n-1` par defaut (`bias=False`).
</details>

---

## Exercice 2 - Correlation

Consigne :

1. Calculez $\sigma_X$ et $\sigma_Y$ avec `ddof=0`
2. Calculez $\rho$
3. Interpretez

<details>
<summary>Afficher la correction</summary>

```python
sx = np.std(x, ddof=0)
sy = np.std(y, ddof=0)

rho_formula = cov_pop_manual / (sx * sy)
rho_numpy   = np.corrcoef(x, y)[0, 1]

print(sx, sy)       # 0.816496... 1.247219...
print(rho_formula)  # 0.981980...
print(rho_numpy)    # 0.981980...
```

$$
\rho\approx 0.98
$$

Interpretation : tres forte correlation lineaire positive.
</details>

---

## Exercice 4 - Lire un coefficient de correlation

Interpretez :

1. $\rho = 0.92$
2. $\rho = -0.45$
3. $\rho = 0$

<details>
<summary>Afficher la correction</summary>

1. $\rho = 0.92$ : lien lineaire tres fort positif
2. $\rho = -0.45$ : lien lineaire negatif modere
3. $\rho = 0$ : pas de lien lineaire detectable
</details>

---

## Lire un nuage avant son coefficient

![Quatre nuages : relation croissante, décroissante, relation quadratique de corrélation linéaire nulle et tirages indépendants. Les coefficients sont calculés sur chaque nuage.](../figures/correlations.svg)

La corrélation de Pearson décrit une relation linéaire. Une valeur proche de zéro n'exclut pas une dépendance non linéaire.

---

## Rappel important

Correlation forte ne veut pas dire causalite.

Toujours verifier :

1. le nuage de points
2. le contexte metier
3. la plausibilite causale

---

## Resume des fonctions NumPy

1. `np.mean(x)` : moyenne
2. `np.std(x, ddof=0)` : ecart-type population
3. `np.cov(x, y, bias=True)` : covariance population
4. `np.cov(x, y, bias=False)` : covariance echantillon
5. `np.corrcoef(x, y)` : coefficient de correlation de Pearson
