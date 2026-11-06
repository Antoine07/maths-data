# Problème 4 — Vingt-quatre demi-journées à répartir

## Le point de départ

Après avoir compté les occasions, Inès préfère construire un calendrier. Elle dispose de 24 demi-journées libres sur un horizon fixé et veut les répartir entre visites à un proche et sorties avec des amis.

Une visite consomme deux demi-journées, une sortie en consomme une. Ce sont des hypothèses logistiques du scénario, pas des règles générales sur les relations.

---

## Objectif et prérequis

**Objectif pédagogique :** rendre explicites une contrainte, un objectif et le passage d'une solution continue à un calendrier entier.

**Prérequis :** équations linéaires, dérivée du logarithme, dérivées composées et [optimisation](../../Slides/avance/05_optimisation.md).

**Durée indicative :** 75 minutes. Le score proposé sert à travailler les mathématiques ; il ne mesure pas le bonheur.

---

## Modèle et unités

$x$ est le nombre de visites ; $y$ le nombre de sorties. Le budget s'écrit :

$$
2x+y\le24,\qquad x\ge0,\quad y\ge0.
$$

Le score de préférence, exprimé en unités arbitraires, est :

$$
U(x,y)=3\ln(1+x)+2\ln(1+y).
$$

Les coefficients 3 et 2 sont des préférences posées par l'énoncé. Le logarithme représente une satisfaction marginale décroissante. Les nombres d'activités sont considérés comme des comptes sans dimension dans ce score.

---

## Énoncé

1. Dessiner les calendriers admissibles dans le plan $(x,y)$. Pourquoi un optimum de ce score utilise-t-il tout le budget ?
2. Sur la frontière, remplacer $y$ par $24-2x$. Donner l'intervalle admissible de $x$ et écrire la fonction d'une seule variable $F(x)$.
3. Calculer $F'(x)$ puis $F''(x)$. Résoudre l'équation stationnaire et justifier qu'elle donne le maximum continu.
4. Les activités doivent être entières. Comparer les calendriers admissibles entiers et proposer le meilleur selon ce score.
5. Remplacer les coefficients 3 et 2 par 2 et 3. Le meilleur calendrier doit-il rester identique ? Qu'est-ce que cette sensibilité apprend sur le modèle ?

---

## Contraintes, livrables et critères de réussite

**Contraintes :** ne pas arrondir les deux coordonnées indépendamment ; conserver le budget ; présenter le score comme un choix de préférence.

**Livrables :** région admissible, calcul de dérivée, optimum continu, calendrier entier et discussion de sensibilité.

**Critères de réussite :** vérifier `2*x + y <= 24`, justifier le maximum par la concavité et reconnaître la dépendance de la solution aux coefficients choisis.

<details><summary>Indices gradués</summary>

1. Les deux dérivées partielles de $U$ sont strictement positives sur le domaine : un budget inutilisé permet encore une amélioration continue.
2. $F(x)=3\ln(1+x)+2\ln(25-2x)$ pour $0\le x\le12$.
3. La dérivée du second logarithme contient le facteur -2. Vérifier les 13 valeurs entières possibles de $x$ est simple.
</details>

---

## Correction — Du plan au maximum continu

<details><summary>Afficher la correction</summary>

L'ensemble admissible est le triangle sous la droite $2x+y=24$, dans le quadrant positif. Sur le bord supérieur :

$$
F'(x)=\frac3{1+x}-\frac4{25-2x},
\qquad
F''(x)=-\frac3{(1+x)^2}-\frac8{(25-2x)^2}<0.
$$

La stricte concavité donne au plus un maximum. L'équation stationnaire donne $3(25-2x)=4(1+x)$, donc $x_*=7{,}1$ et $y_*=9{,}8$, tous deux admissibles.

![À gauche, les calendriers admissibles sous la contrainte 2x+y=24 ; à droite, le score concave atteint son maximum continu vers x=7,1.](../../Slides/figures/tail-04-planning.svg)

L'optimum continu sert de repère : il ne constitue pas un calendrier de 7,1 visites.
</details>

---

## Correction — Choisir un calendrier entier

<details><summary>Afficher la correction</summary>

Pour chaque entier $x$ entre 0 et 12, le meilleur $y$ entier est $24-2x$, car le score croît avec $y$.

La comparaison donne **7 visites et 10 sorties**, soit $2\times7+10=24$ demi-journées et un score d'environ 11,034.

Arrondir $x_*$ à 7 et $y_*$ à 10 fonctionne ici, mais ce n'est pas une méthode générale : il faut vérifier la contrainte et comparer les choix admissibles.

Avec les coefficients inversés, le maximum continu devient $(4{,}4,15{,}2)$ et le meilleur calendrier entier devient $(4,16)$. Changer les préférences change la réponse ; les mathématiques rendent ce choix explicite, elles ne le décident pas à notre place.
</details>

---

## Correction — Contrôle avec Python

<details><summary>Afficher la correction</summary>

```python
import numpy as np
x = np.arange(13)
y = 24 - 2*x
for a, b in [(3, 2), (2, 3)]:
    valeurs = a*np.log1p(x) + b*np.log1p(y)
    i = np.argmax(valeurs)
    print(int(x[i]), int(y[i]), round(float(valeurs[i]), 3))
```

**Lecture :** les tableaux énumèrent les 13 plans entiers sur la frontière. Le score est calculé avec deux systèmes de préférences ; `argmax` renvoie le meilleur indice. Sorties : `7 10 11.034`, puis `4 16 11.718` environ.

**Erreur fréquente :** comparer les valeurs de scores de deux préférences différentes comme si elles appartenaient à une même échelle objective.
</details>

---

## Discussion — Optimiser ne suffit pas à définir le bon objectif

Le résultat suppose des coûts fixes, des activités interchangeables et un score additif. Il ignore disponibilités des autres personnes, déplacements variables, fatigue et qualité du temps partagé.

**Lien data / IA :** optimiser une métrique ne valide pas cette métrique. En planification comme en apprentissage, un objectif doit correspondre à l'usage et ses limites doivent rester visibles.

[Retour aux quatre problèmes](README.md). Inspiration : [*The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html) ; problème d'optimisation original.
