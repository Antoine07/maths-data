---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# Centrage et reduction

## Cours

![Les valeurs 8 et 12 deviennent -2 et +2 après centrage, puis -1 et +1 après réduction.](../images/couverture-centrage.svg)

---

## Jeu de donnees 1 - Temperatures

```python
temps = np.array([
    15.2, 15.5, 15.1, 15.3, 15.4,
    25.8, 26.1, 25.9,
    15.2, 15.3, 15.1
])
```

---

## Centrage

Formule :

$$
x_c = x - \bar{x}
$$

Consigne :

1. Calculez $\bar{x}$
2. Construisez `temps_centered = temps - np.mean(temps)`
3. Interpretez les signes (positif/negatif)

<details>
<summary>Afficher la correction</summary>

$$
\bar{x}\approx 18.173
$$

`temps_centered` (arrondi) :
`[-2.973, -2.673, -3.073, -2.873, -2.773, 7.627, 7.927, 7.727, -2.973, -2.873, -3.073]`

Valeur negative : en dessous de la moyenne.
Valeur positive : au dessus de la moyenne.
</details>

---

## Detection simple des jours froids / chauds

Avec un seuil `threshold = 2` :

```python
cold_idx = np.where(temps_centered < -2)[0]
hot_idx  = np.where(temps_centered >  2)[0]
```

Consigne :

1. Trouvez `cold_idx`
2. Trouvez `hot_idx`
3. Comparez avec les temperatures d'origine

<details>
<summary>Afficher la correction</summary>

`cold_idx = [0, 1, 2, 3, 4, 8, 9, 10]`

`hot_idx = [5, 6, 7]`
</details>

---

## Jeu de donnees 2 - Temperature et frequence cardiaque

```python
temperature = np.array([36.8, 37.1, 36.9, 37.5, 38.2, 36.7, 37.0])
heart_rate  = np.array([62, 70, 65, 74, 90, 60, 68])
```

---

## Centrage des deux variables

```python
temp_centered  = temperature - np.mean(temperature)
heart_centered = heart_rate  - np.mean(heart_rate)
```

Consigne :

1. Calculez `temp_centered`
2. Calculez `heart_centered`
3. Comparez les amplitudes des deux variables

<details>
<summary>Afficher la correction</summary>

`temp_centered = [-0.371, -0.071, -0.271, 0.329, 1.029, -0.471, -0.171]`

`heart_centered = [-7.857, 0.143, -4.857, 4.143, 20.143, -9.857, -1.857]`

Amplitude plus forte pour la frequence cardiaque avant reduction.
</details>

---

## Reduction (standardisation)

```python
temp_scaled  = temp_centered  / np.std(temp_centered)
heart_scaled = heart_centered / np.std(heart_centered)
```

Consigne :

1. Calculez `temp_scaled`
2. Calculez `heart_scaled`
3. Relevez les valeurs proches de 0, > +1 et < -1

<details>
<summary>Afficher la correction</summary>

`temp_scaled = [-0.769, -0.148, -0.562, 0.680, 2.129, -0.976, -0.355]`

`heart_scaled = [-0.842, 0.015, -0.521, 0.444, 2.160, -1.057, -0.199]`

Valeurs > +1 : individu 4 sur les deux variables.
Valeur < -1 : individu 5 sur la frequence cardiaque.
</details>

---

## Interpretation

1. Valeur > `+1` : atypiquement elevee
2. Valeur < `-1` : atypiquement faible
3. Valeur proche de `0` : proche de la moyenne

---

## Resume

1. Centrer : retirer la moyenne
2. Reduire : diviser par l'ecart-type
3. Apres centrage-reduction : moyenne = 0, ecart-type = 1
4. On peut comparer des variables sur des echelles differentes
