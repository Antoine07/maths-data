
# **TP – Modéliser la saturation d'un marché numérique**

Une startup lance une application mobile. Le nombre d'utilisateurs actifs (en milliers) au mois (t) est modélisé par :

$$
U(t) = 5 + t\ln(t+2) - 2t, \qquad t\ge 0
$$

où

* (t) : temps en mois,
* (U(t)) : utilisateurs actifs (en milliers).

Le modèle reflète :

1. une croissance initiale : 

$$
t \ln(t+2)
$$

1. une perte naturelle d'utilisateurs : (-2t)
1. une base stable d'utilisateurs fidèles : (+5)

---

#  **Dérivée et signe de la dérivée**

## **Calculer la dérivée `U'(t)`**

En déduire une expression simple de `U'(t)`.

---

## **Étudier rigoureusement le signe de `U'(t)`**

On pose :

$$
f(t)=U'(t)
$$

1. Calculer `f'(t)`.
2. Montrer que `f'(t) > 0` pour tout (t > 0).
3. Conclure que `f(t)` est strictement croissante.
4. Calculer :

1. f(0)
1. la limite de f(t) lorsque (t tend vers  + l'infini)
5. En déduire l'existence d'un **unique** point (t_0) tel que (U'(t_0)=0).
6. Dresser le tableau de signe de (U'(t)).
7. Trouvez ce point par dicothomie avec Python.
8. En conclure les **variations de U(t)**.

---

#  **Dérivée seconde et dynamique**

Expliquer, dans le contexte d'un marché :

1. pourquoi une fonction d'utilisateurs peut d'abord décroître,
1. puis repartir,
1. et pourquoi une convexité constante est réaliste.

---

# **Limite et asymptote**

Calculez la limite en + l'infini de la fonction `U`.

---

## **Y-a-t-il des asymptotes**

Étudier :

$$
\frac{U(t)}{t} = \ln(t+2)-2 + \frac{5}{t}
$$

1. Calculer sa limite.
2. Conclure s'il existe une asymptote horizontale ou oblique.

À partir du signe de U'(t), expliquer :

1. quand l'application perd des utilisateurs,
1. quand elle en regagne,
1. ce que signifie le point (t_0) pour une équipe produit.

---

## **Analyse de la faiblesse de la croissance**

On fixe un seuil minimal de croissance égal à :

$$
U'(t) < 0.2.
$$

On dit que la croissance est trop faible lorsque la dérivée U'(t) est strictement inférieure à ce seuil.
Déterminer, à l’aide d’un raisonnement analytique ou d’un calcul numérique, l’instant à partir duquel cette situation cesse d’être vérifiée.

