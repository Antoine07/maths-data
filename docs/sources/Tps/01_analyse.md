# Examen M1 Data

On modélise la température interne (en °C) d'un drone en fonctionnement par :

$$
T(t) = 20 + 4t e^{-0.3t}, \qquad t \ge 0.
$$

### **Domaine et limites**

1. Identifier le domaine de définition de `T`.
1. Calculer les limites de `T(t)` lorsque `t tend vers l'infini`
1. Interpréter physiquement ces résultats.

1. Dérivée `T(t)`
1. Résoudre l'équation `T'(t)=0`.
1. Déterminer les variations de (T).
1. En déduire à quel instant la température atteint un **maximum**.

## Analyse de la forme de la courbe `T(t)`

La forme de la courbe `T(t)` permet de mieux comprendre la manière dont la température interne du drone évolue : accélération du chauffage, ralentissement, puis entrée dans une phase de refroidissement régulier.

**Analysez ce comportement**

## **Analyse de la vitesse de refroidissement**

On définit la vitesse de refroidissement après le pic thermique :

$$
R(t)= -T'(t)= 4 e^{-0.3t}(0.3t - 1).
$$

On cherche quand la vitesse devient inférieure à **0.1°C/min** :

$$
R(t)=0.1
$$

 Montrer que l'équation admet une unique solution dans l'intervalle `[5,15]`. Donner une valeur approchée au millième près.

## **Conclusion**

Rédiger une conclusion claire décrivant :

1. quand le drone atteint son **maximum thermique**,
1. quand le **refroidissement devient lent**,
1. les implications pratiques pour son utilisation.
