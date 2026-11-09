# Pourquoi notre dîner à dix n'arrive jamais ?

## Objectif et prérequis

**Après :** [probabilités essentielles](../../Slides/stat/probabilites.md).

**Objectif :** distinguer disponibilité individuelle, nombre moyen de personnes présentes et disponibilité simultanée du groupe.

## La situation

Dix amis cherchent une date pour dîner. Chacun est disponible avec une probabilité de 80 % sur une date proposée. Cela semble généreux : pourquoi trouver une date commune reste-t-il difficile ?

Nous posons un modèle fictif : les disponibilités des personnes sont indépendantes pour une date. Pour comparer plusieurs dates, on les suppose également indépendantes d'une date à l'autre. Ce sont des hypothèses à discuter, pas des propriétés garanties d'un agenda réel.

---

## Énoncé

1. Calculer la probabilité que les dix personnes soient disponibles pour une date.
2. Quel est le nombre moyen de personnes disponibles à une date ? Est-ce contradictoire avec la première réponse ?
3. Refaire le calcul pour cinq personnes. Tracer la probabilité d'une disponibilité commune pour des groupes de 1 à 15 personnes.
4. Avec quatre dates indépendantes proposées, calculer la probabilité d'en trouver au moins une où les dix personnes sont libres. Pourquoi n'est-ce pas exactement quatre fois la probabilité d'une date ?
5. Simuler 100 000 dates, puis expliquer ce qui changerait si les amis partageaient les mêmes contraintes professionnelles ou les mêmes vacances.

## Contraintes, livrables et critères de réussite

**Contraintes :** annoncer à chaque multiplication l'hypothèse d'indépendance ; ne pas confondre « au moins une date » et « nombre moyen de dates favorables ».

**Livrables :** calculs, courbe, simulation et discussion des hypothèses.

**Critères :** distinguer une moyenne de personnes et une probabilité de groupe ; utiliser l'événement complémentaire pour plusieurs dates.

<details><summary>Indices gradués</summary>

1. « Tous disponibles » est l'intersection de dix événements indépendants.
2. « Au moins une date favorable » est le complément de « aucune date favorable ».
3. Des contraintes communes peuvent rendre les disponibilités dépendantes.
</details>

---

## Correction — Souvent libre, rarement tous libres

<details><summary>Afficher la correction</summary>

Pour dix personnes : $p=0{,}8^{10}\approx0{,}1074$, soit **10,74 %**. Le nombre moyen de personnes libres vaut pourtant $10\times0{,}8=8$.

Ce sont deux questions différentes : il peut souvent manquer une ou deux personnes. Avec cinq personnes, la probabilité commune vaut $0{,}8^5\approx32{,}77\%$.

Sur quatre dates indépendantes :

$$
P(\text{au moins une date})=1-(1-0{,}8^{10})^4\approx36{,}51\%.
$$

![La probabilité de disponibilité commune diminue avec la taille du groupe ; proposer plusieurs dates augmente la chance d'un succès sans les additionner directement.](../../Slides/figures/paradoxe-diner.svg)

La valeur $4p\approx0{,}4295$ est le nombre moyen de dates favorables parmi les quatre. Ce n'est pas la probabilité d'en avoir au moins une, car plusieurs dates favorables peuvent survenir dans le même essai.
</details>

---

## Correction — Contrôle Python

<details><summary>Afficher la correction</summary>

```python
import numpy as np
p = 0.8**10
print(round(100*p, 2), round(100*(1-(1-p)**4), 2))
rng = np.random.default_rng(42)
disponibles = rng.random((100000, 10)) < 0.8
print(round(float(disponibles.sum(axis=1).mean()), 2))
print(round(float(disponibles.all(axis=1).mean()), 3))
```

**Lecture :** chaque ligne représente une date et les dix colonnes les personnes. La somme compte les présents ; `all` exige leur présence simultanée. Les résultats sont proches de 8 personnes et d'une fréquence de succès 0,107.

**Erreur fréquente :** lire une moyenne de huit personnes comme une probabilité de 80 % pour réunir tout le groupe.
</details>

## Discussion — Les agendas ne sont pas toujours indépendants

Si tous les amis partagent exactement les mêmes disponibilités, la probabilité commune pourrait être de 80 % plutôt que de 10,74 %, malgré les mêmes probabilités individuelles. D'autres dépendances peuvent avoir un autre effet.

Il faut donc observer les agendas ou simuler un modèle de dépendance explicite avant de transformer la formule en conseil d'organisation.

**Lien avec l'optimisation :** reprendre ce problème lorsque le parcours aborde le [calendrier sous contrainte](../Tail_End/04_planning.md). La possibilité d'une date commune et l'allocation d'un budget de temps sont deux contraintes différentes.

[Tous les problèmes du parcours](../../docs/problemes.html).
