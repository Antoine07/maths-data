# **Modéliser l'évolution de la température moyenne d'un mois**  page 1/6

On s'intéresse à l'évolution de la **température moyenne quotidienne** dans une ville pendant un mois (par exemple en avril).

On étudie ici la tendance d'un mois à l'autre des jours, pas les oscillations de température au cours d'une journée. Une droite peut servir de premier modèle pour cette évolution.

Voici des valeurs observées (en °C) :

```python
T = np.array([
    8.0, 8.2, 8.5, 9.0, 9.3, 9.5, 10.1, 10.4, 
    10.6, 11.0, 11.2, 11.4, 11.7, 12.0, 12.1, 
    12.5, 12.6, 12.9, 13.0, 13.1, 13.4, 13.5, 
    13.7, 14.0, 14.2, 14.3, 14.5, 14.8, 15.0, 15.2
])
```

On suppose que la température augmente **presque linéairement** au cours du mois.

On associe chaque valeur à un jour `t = 1, 2, ..., 30`.

---

### **Tracer les données** page 2/6

Utilisez la fonction `plot.scatter`

---

### **Trouver un modèle linéaire** page 3/6

On cherche une fonction affine qui approche au mieux les mesures :

$$
T(t) = a t + b
$$

La fonction **`np.polyfit(x, y, degré)`** calcule les coefficients du polynôme qui ajuste au mieux les points $(x_i,y_i)$, au sens des moindres carrés : elle minimise la somme des carrés des écarts verticaux entre les mesures et le modèle.

Dans cet exemple :

```python
t = np.arange(1, 31)       # les jours : variable x
a, b = np.polyfit(t, T, 1) # les températures : variable y
```

Le dernier argument, **`1`**, est le degré du polynôme demandé. Un polynôme de degré 1 s'écrit $a t+b$ : c'est une droite. `np.polyfit` renvoie ses coefficients dans l'ordre des puissances décroissantes, donc ici `[a, b]` : d'abord la pente, puis l'ordonnée à l'origine.

On peut ensuite calculer les températures prédites par cette droite :

```python
T_modele = a * t + b
```

Ainsi, `1` ne désigne ni le nombre de données ni le nombre de variables : il demande simplement un modèle de degré 1. Avec `2`, NumPy ajusterait une parabole de la forme $c t^2+a t+b$.

---

### **Tracer la droite obtenue sur le même graphique.** page 4/6

---
 
## Lire un ajustement et ses résidus

![Les 30 températures du support sont ajustées par une droite ; un second panneau montre les résidus observé moins prédit, exprimés en degrés Celsius.](figures/modele-temperature.svg)

Les écarts ne se résument pas à leur moyenne : chercher aussi une structure dans les résidus.

---

### **4. Interpréter les paramètres** page 5/6

1. Que signifie (a) ?
1. Que signifie (b) ?
1. Le modèle semble-t-il cohérent ?

---

### **Prédire la température au jour 35.** page 6/6

---

## **Exercice 2 — Une boisson qui refroidit**

Le modèle affine précédent décrit une tendance sur un mois. Une tasse de café qui refroidit suit une évolution différente : la température baisse rapidement au début, puis ralentit en se rapprochant de celle de la pièce.

On mesure la température d'une boisson dans une pièce à **20 °C** :

| Temps $t$ (min) | 0 | 2 | 4 | 6 | 8 | 10 | 15 | 20 | 30 | 40 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Température $T$ (°C) | 80,0 | 71,1 | 63,6 | 57,1 | 51,6 | 46,9 | 38,1 | 32,1 | 25,4 | 22,4 |

**Question :** une droite peut-elle bien représenter cette baisse jusqu'à ce que la boisson atteigne la température de la pièce ?

---

## **Un modèle exponentiel**

La température ne descend pas indéfiniment : elle se rapproche de la température ambiante $T_{\mathrm{amb}}$.

On propose le modèle, où $T_{\mathrm{amb}}$ désigne la température ambiante de la pièce :

$$
T(t)=T_{\mathrm{amb}}+(T_0-T_{\mathrm{amb}})e^{-kt}.
$$

- $T_0$ est la température initiale ;
- $T_{\mathrm{amb}}=20$ °C est la température ambiante ;
- $k>0$ règle la vitesse de refroidissement.

À $t=0$, le modèle donne $T(0)=T_0$. Quand le temps augmente, le terme exponentiel diminue et $T(t)$ se rapproche de 20 °C.

---

## **À vous — Transformer le modèle pour l'ajuster**

À partir du modèle exponentiel proposé juste avant, trouvez une transformation qui permet d'utiliser `np.polyfit(t, y, 1)`.

1. Tracez les mesures avec `plt.scatter`.
2. Déterminez quelle transformation appliquer aux températures pour obtenir une relation affine en fonction du temps. Vérifiez que les opérations choisies sont possibles pour toutes les mesures.
3. Ajustez la relation obtenue avec `np.polyfit(t, y, 1)`.
4. À partir de la pente et de l'ordonnée à l'origine, retrouvez les paramètres du modèle exponentiel.
5. Représentez les mesures et le modèle exponentiel sur le même graphique avec `plt.plot`.

---

## **Correction — Afficher la solution**

<details>
<summary>Afficher une correction possible</summary>

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.array([0, 2, 4, 6, 8, 10, 15, 20, 30, 40], dtype=float)
T = np.array([80.0, 71.1, 63.6, 57.1, 51.6, 46.9, 38.1, 32.1, 25.4, 22.4])
T_piece = 20.0

# Après soustraction de la température ambiante, le modèle devient exponentiel.
y = np.log(T - T_piece)
pente, intercept = np.polyfit(t, y, 1)

k = -pente
T0 = T_piece + np.exp(intercept)
print(f"Pente transformée : {pente:.4f} par minute")
print(f"k : {k:.4f} par minute")
print(f"Température initiale estimée : {T0:.1f} °C")

t_modele = np.linspace(0, 45, 200)
T_modele = T_piece + (T0 - T_piece) * np.exp(-k * t_modele)

plt.scatter(t, T, color="steelblue", label="Mesures")
plt.plot(t_modele, T_modele, color="tomato", label="Modèle exponentiel")
plt.axhline(T_piece, color="gray", linestyle="--", label="Température de la pièce")
plt.xlabel("Temps (min)")
plt.ylabel("Température (°C)")
plt.title("Refroidissement d'une boisson")
plt.legend()
plt.show()
```

On obtient environ $k=0{,}080$ par minute et $T_0\approx80$ °C. La pente négative de la droite transformée donne $-k$ ; l'exponentielle de son ordonnée à l'origine donne $T_0-20$.

Ce modèle simplifie la réalité : il suppose une température ambiante stable et un refroidissement de même nature pendant toute l'expérience. L'ajustement logarithmique sert ici à apprendre la méthode ; avec des mesures très bruitées, il faudra discuter la méthode d'ajustement.

</details>

