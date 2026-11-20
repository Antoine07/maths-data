# TP – Le modèle prévoit-il une saturation ?

**TP facultatif.** Ce prolongement permet d’approfondir l’étude des variations, des limites et des asymptotes.

Une startup modélise le nombre d’utilisateurs actifs, en milliers, par la fonction suivante. Le temps $t$ est mesuré en mois depuis le lancement.

$$
U(t) = 5 + t\ln(t+2) - 2t, \qquad t\ge 0.
$$

Le modèle combine une base initiale de 5 000 utilisateurs, une contribution positive $t\ln(t+2)$ pour $t>0$ et une perte modélisée par $-2t$.

On parle ici de **saturation** lorsque le nombre d’utilisateurs actifs tend vers un plafond fini.

---

## Calcul de la dérivée

Calculer et simplifier $U'(t)$ en utilisant la règle de dérivation d’un produit.

Quelle est l’unité de $U'(t)$ ?

---

## Signe de la dérivée et variations

On pose $f(t)=U'(t)$.

1. Calculer $f'(t)$ et justifier que $f$ est strictement croissante sur $[0,+\infty[$.
2. Calculer $f(0)$ et la limite de $f(t)$ lorsque $t$ tend vers $+\infty$.
3. À l’aide de la continuité de $f$, justifier l’existence et l’unicité d’un instant $t_0$ tel que $f(t_0)=0$. Dresser le tableau de signe de $f$.
4. Vérifier que $f(2)<0<f(3)$. Approcher $t_0$ par dichotomie en Python sur $[2,3]$ jusqu’à obtenir un intervalle de largeur au plus $10^{-6}$ mois.
5. En déduire les variations de $U$ et estimer le nombre d’utilisateurs au minimum.

---

## Dérivée seconde et dynamique

1. Justifier que $U$ est strictement convexe et décrire comment $U''(t)$ évolue avec le temps.
2. Interpréter les signes de $U'(t)$ et de $U''(t)$ de part et d’autre de $t_0$. Que représente $t_0$ pour l’équipe produit ?

---

## Limite à long terme

Calculer la limite de $U(t)$ quand $t$ tend vers $+\infty$.

D’après cette limite, le modèle prévoit-il une saturation du nombre d’utilisateurs actifs ?

---

## Asymptotes

Pour $t>0$, on a

$$
\frac{U(t)}{t} = \ln(t+2)-2 + \frac{5}{t}.
$$

1. Calculer la limite de ce quotient quand $t$ tend vers $+\infty$.
2. En déduire si la courbe de $U$ admet une asymptote horizontale ou oblique en $+\infty$.

---

## Seuil de croissance

L’équipe produit fixe un seuil de croissance de $0{,}2$ millier d’utilisateurs actifs par mois, soit 200 utilisateurs actifs par mois.

1. Montrer qu’il existe un unique instant $t_s$ tel que $U'(t_s)=0{,}2$. L’estimer par dichotomie avec la même précision que pour $t_0$.
2. Donner l’intervalle où $U'(t)<0{,}2$, puis celui où la croissance atteint ou dépasse le seuil.
3. Sur quel intervalle le nombre d’utilisateurs actifs augmente-t-il à un taux strictement inférieur au seuil ?
