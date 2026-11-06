# Examen M1 Data — Sujet 2

On modélise la **température interne** (en °C) d'un module de calcul embarqué (drone) soumis à une charge de calcul variable par :

$$
T(t)=25+6,(t+1),e^{-0.25t},\qquad t\ge 0.
$$

---

## Domaine et limites

1. Identifier le domaine de définition de `T`.
2. Calculer 

$$
\displaystyle \lim_{t\to +\infty} T(t)).
$$

3. Interpréter physiquement ces résultats (avec `t` en secondes).

---

## Dérivée et extrema

1. Calculer `T'(t)`.
2. Résoudre l'équation `T'(t)=0`.

   * Donner une valeur approchée (au millième) de la (des) solution(s) pertinente(s) sur 

   $$
   0,+\infty
   $$)

3. Étudier le signe de  `T'(t)` et déterminer les variations de  `T`.
4. En déduire l'instant auquel la température atteint un **maximum** et la valeur 

$$
T_{\max} 
$$

correspondante (au millième).

---

## Analyse de la forme de la courbe (T(t))

La courbe de (T(t)) présente typiquement :

* une phase de montée (chauffage) liée à la montée en charge,
* un ralentissement,
* puis une baisse due à la dissipation thermique.

1. Calculer  `T''(t)`.
2. Étudier la convexité/concavité de  `T` et déterminer s'il existe un **point d'inflexion** (donner l'instant associé au millième si applicable).
3. Interpréter le lien entre convexité/concavité et **accélération/décélération** du chauffage.

---

## Analyse de la vitesse de refroidissement

Après le pic thermique, on définit la **vitesse de refroidissement** :

$$
R(t)=-T'(t).
$$

1. Exprimer (R(t)) sous forme factorisée.
2. On cherche l'instant où la vitesse devient inférieure à **0,1 °C/min**.
   Convertir ce seuil en **°C/s**, puis résoudre :

$$
R(t)=\frac{0.1}{60}.
$$

3. Montrer que l'équation admet une **unique solution** dans l'intervalle ($$6,18$$).
   Donner une valeur approchée au **millième** près (méthode numérique au choix : dichotomie, Newton, etc., avec justification brève).

---

## Conclusion

Rédiger une conclusion claire décrivant :

1. quand le drone atteint son **maximum thermique** (instant et température),
2. quand le **refroidissement devient lent** (instant),
3. les implications pratiques pour l'utilisation (fenêtre de fonctionnement sûre, précautions, stratégies de charge/pauses).
