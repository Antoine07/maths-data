---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# ACP - Introduction

## Cours

![Un nuage de points et ses projections orthogonales sur son premier axe principal.](../images/couverture-acp.svg)

---

## Objectif

L'ACP (Analyse en Composantes Principales) sert a :

1. reduire la dimension
2. garder un maximum d'information (variance)
3. faciliter la visualisation des individus

---

## Donnees exemple

```python
X = np.array([
    [160, 55],
    [170, 65],
    [172, 68],
    [180, 80],
    [175, 75],
    [158, 50]
], dtype=float)
```

Variables : taille et poids.

---

## Etape 1 - Centrage

```python
mean = np.mean(X, axis=0)
X_centered = X - mean
```

Pourquoi : supprimer l'effet du niveau moyen avant l'analyse.

<details>
<summary>Afficher la correction</summary>

Moyennes :

`mean = [169.167, 65.500]`

Donnees centrees (arrondi) :

```text
[-9.167, -10.500]
[ 0.833,  -0.500]
[ 2.833,   2.500]
[10.833,  14.500]
[ 5.833,   9.500]
[-11.167, -15.500]
```
</details>

---

## Etape 2 - Matrice de covariance

```python
C = np.cov(X_centered, rowvar=False)
```

Interpretation :

1. diagonale : variances de chaque variable
2. hors diagonale : covariance entre variables

<details>
<summary>Afficher la correction</summary>

```text
C = [[ 73.767,  97.700],
     [ 97.700, 131.500]]
```

La covariance positive indique que taille et poids augmentent ensemble.
</details>

---

## Etape 3 - Valeurs propres et vecteurs propres

```python
eigenvalues, eigenvectors = np.linalg.eigh(C)
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
eigenvectors = eigenvectors[:, order]
# Convention de signe pour reproduire les tableaux ci-dessous :
for j in range(eigenvectors.shape[1]):
    i = np.argmax(np.abs(eigenvectors[:, j]))
    if eigenvectors[i, j] < 0:
        eigenvectors[:, j] *= -1
```

1. valeur propre = variance expliquee par l'axe
2. vecteur propre = direction de l'axe principal

<details>
<summary>Afficher la correction</summary>

Valeurs propres (ordre decroissant) :

`[204.509, 0.758]`

Part de variance expliquee :

`[99.63%, 0.37%]`

Vecteurs propres (a un signe pres) :

```text
PC1 ~ [ 0.599, 0.801]
PC2 ~ [0.801, -0.599]
```
</details>

---

## Etape 4 - Projection

```python
X_projected = X_centered @ eigenvectors
```

Les individus sont exprimes dans la nouvelle base (PC1, PC2).

<details>
<summary>Afficher la correction</summary>

Projection `X_projected` (arrondie) :

```text
[-13.898, -1.058]
[  0.098,  0.967]
[  3.699,  0.773]
[ 18.100, -0.002]
[ 11.102, -1.014]
[-19.101,  0.333]
```
</details>

---

## Pistes d'interpretation

Le signe d'un axe est conventionnel. Changer son signe change celui des coordonnees projetees, mais ne change ni les distances, ni la variance expliquee, ni la reconstruction. Les valeurs propres et les colonnes de vecteurs propres doivent toujours etre triees ensemble.

1. Observez le signe de la covariance taille-poids
2. Comparez la part de variance expliquee par PC1 et PC2
3. Proposez une interpretation de PC1
4. Proposez une interpretation de PC2

<details>
<summary>Afficher la correction</summary>

1. Covariance positive.
2. PC1 explique presque toute la variance.
3. PC1 peut etre interpretee comme un axe de gabarit global.
4. PC2 capte un contraste residuel taille/poids.
</details>

---

## Resume

1. Centrer les donnees
2. Calculer covariance
3. Extraire valeurs/vecteurs propres
4. Projeter sur les composantes principales
5. Interpreter la variance expliquee
