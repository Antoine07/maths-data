# Problème 1 — La moitié des années, combien de rencontres ?

## Le point de départ

Léa a 30 ans. Elle pense : « Si je regarde jusqu'à mes 60 ans, il reste autant de temps qu'il en est passé. »

Ce raisonnement compte des années. Mais Léa veut maintenant compter les journées où elle voit un proche. Elle n'a pas toujours vécu au même endroit.

Le scénario est fictif ; l'horizon de 60 ans est fixé pour l'exercice et n'est pas une prévision de durée de vie.

---

## Objectif et prérequis

**Objectif pédagogique :** définir un indicateur, vérifier ses unités et comprendre le rôle du dénominateur.

**Prérequis :** [révisions d'algèbre](../../Slides/revision.md), multiplication et pourcentages. Aucune probabilité n'est nécessaire.

**Travail attendu :** calcul manuel puis contrôle numérique.

---

## Données et unités

| Période | Durée | Journées de rencontre par an |
|---|---:|---:|
| De 0 à 18 ans | 18 ans | 300 |
| De 18 à 30 ans | 12 ans | 12 |
| De 30 à 60 ans, scénario de base | 30 ans | 12 |

Une journée où plusieurs rencontres ont lieu ne compte qu'une fois. Les journées ne sont pas des durées de 24 h passées ensemble : c'est notre unité de comptage.

Les fréquences sont supposées constantes à l'intérieur de chaque période. Le modèle ne pondère ni la durée ni la qualité des rencontres.

---

## Énoncé

1. Calculer le nombre de journées de rencontre de chaque période, puis les totaux passé et futur.
2. Calculer la fraction d'années restantes dans l'horizon, puis la fraction de journées de rencontre restantes. Comparer les deux résultats.
3. Dessiner une grille où chaque point représente **12 journées de rencontre**, en distinguant passé et futur. Combien de points faut-il ?
4. Léa passe désormais à 24 journées de rencontre par an. Recalculer le futur, le total et la fraction future. Le passé change-t-il ? La fraction future est-elle exactement doublée ?
5. Formuler une conclusion conditionnelle : qu'affirme le calcul et qu'ignore-t-il ?

---

## Contraintes, livrables et critères de réussite

**Contraintes :** annoncer toutes les unités ; conserver les jours passés lorsque le futur change ; ne pas transformer un horizon fixé en certitude.

**Livrables :** tableau de calcul, grille de points, deux pourcentages comparés et conclusion de cinq lignes.

**Critères de réussite :** nombres cohérents avec les trois périodes, dénominateur recomputé dans le second scénario et représentation dont la légende indique l'unité de chaque point.

<details><summary>Indices gradués</summary>

1. Pour chaque période : années × journées par an = journées.
2. La part future est `futur / (passé + futur)`.
3. En doublant la fréquence future, le numérateur **et** le dénominateur changent.
</details>

---

## Correction — Calculs et représentation

<details><summary>Afficher la correction</summary>

Enfance : $18\times300=5\,400$ journées. Vie adulte passée : $12\times12=144$ journées. Le passé total vaut donc $5\,544$ journées.

Le futur du scénario de base vaut $30\times12=360$ journées. Le total de l'horizon vaut $5\,904$ journées.

La moitié des années de l'horizon restent, mais la part des journées futures vaut :

$$
\frac{360}{5\,544+360}\approx0{,}06098=6{,}10\%.
$$

![492 points, dont 462 pour le passé et 30 pour le futur ; chaque point représente 12 journées de rencontre.](../../Slides/figures/tail-01-rencontres.svg)

La grille contient $5\,904/12=492$ points : 462 pour le passé et 30 pour le futur. Les points représentent des journées de rencontre, pas des années de vie.
</details>

---

## Correction — Changer le futur sans réécrire le passé

<details><summary>Afficher la correction</summary>

Avec 24 journées par an, le futur vaut 720 journées et le total vaut $5\,544+720=6\,264$ journées.

$$
\text{Nouvelle part future}=\frac{720}{6\,264}\approx11{,}49\%.
$$

Le nombre futur double, mais le pourcentage ne double pas exactement : le total change aussi. Le passé reste à 5 544 journées.

Conclusion possible : **si** les fréquences et l'horizon fixés se réalisent, le modèle compte 360 journées futures dans le scénario de base. Il ne mesure ni la qualité des relations, ni la durée des visites, ni les événements qui pourraient modifier les fréquences.
</details>

---

## Correction — Contrôle avec Python

<details><summary>Afficher la correction</summary>

```python
passe = 18 * 300 + 12 * 12
for frequence in (12, 24):
    futur = 30 * frequence
    total = passe + futur
    print(futur, total, round(100*futur/total, 2))
```

**Lecture du code :** `passe` est fixé une fois ; la boucle compare deux hypothèses de fréquence future. Les sorties sont `360 5904 6.1` et `720 6264 11.49`.

**Erreur fréquente :** conserver le total 5 904 dans les deux scénarios. On comparerait alors des quantités définies sur des horizons d'événements différents.
</details>

---

## Discussion — Ce que cet indicateur raconte

Les années et les rencontres ne sont pas réparties de la même façon. Pour rendre l'indicateur utile, il faut expliciter son unité, ses périodes et ses hypothèses.

Une grille peut rendre un ordre de grandeur visible tout en donnant une impression de certitude. La légende et la conclusion conditionnelle font partie de la réponse mathématique.

**Lien data :** avant de construire un tableau de bord, définir précisément ce que représente une ligne, un point et un pourcentage.

[Retour aux quatre problèmes](README.md). Idée de départ : [Tim Urban, *The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html) ; scénario et calculs originaux.
