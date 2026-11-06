# **Modéliser l'évolution de la température moyenne d'un mois**  page 1/6

On s'intéresse à l'évolution de la **température moyenne quotidienne** dans une ville pendant un mois (par exemple en avril).

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

On cherche une fonction :

$$
T(t) = a t + b
$$

Utiliser **NumPy `np.polyfit`** pour estimer (a) et (b), droite de régression linéaire.

`np.polyfit(x, y, 1)` où 1 est le degré du pôlynome.

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

