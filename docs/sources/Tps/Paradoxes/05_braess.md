# Ajouter une route peut-il ralentir tout le monde ?

## Objectif et prérequis

**Après :** [optimisation](../../Slides/avance/05_optimisation.md). **Approfondissement facultatif.**

**Objectif :** distinguer un équilibre de choix individuels et un objectif collectif. Les graphes nécessaires sont introduits dans l'énoncé.

## La situation

Une ville fictive ouvre une nouvelle liaison gratuite. Aucun trajet existant ne disparaît. Pourtant, lorsque chacun choisit son trajet le plus rapide, tout le monde peut mettre plus de temps qu'avant.

Un **graphe orienté** représente les croisements par des sommets et les routes par des flèches. Ici, 4 000 conducteurs vont de S à T ; les deux sommets intermédiaires sont A et B.

---

## Données du réseau

| Route orientée | Temps en minutes |
|---|---:|
| S → A | nombre de conducteurs sur cette route / 100 |
| A → T | 45 |
| S → B | 45 |
| B → T | nombre de conducteurs sur cette route / 100 |
| Nouvelle liaison A → B | 0 dans ce modèle idéalisé |

Les temps d'un trajet s'additionnent. Seules S → A et B → T dépendent de la congestion. Les conducteurs ont tous le même point de départ, la même destination et accès aux mêmes informations.

---

## Énoncé

1. Dessiner le réseau sans la liaison A → B. Si 2 000 conducteurs choisissent chaque trajet, calculer les temps de parcours.
2. Si un trajet accueille davantage de conducteurs que l'autre, pourquoi certains ont-ils intérêt à changer ?
3. Ajouter A → B, puis supposer que les 4 000 conducteurs empruntent S → A → B → T. Calculer leur temps et celui d'un conducteur qui dévierait seul par l'un des anciens trajets.
4. Un état est un **équilibre individuel** si aucun conducteur ne peut réduire son temps en changeant seul. L'état précédent possède-t-il cette propriété ? Comparer son temps à celui d'avant l'ouverture.
5. Un planificateur pourrait-il conserver une répartition réalisable à 65 minutes après l'ouverture ? Pourquoi cela ne contredit-il pas le résultat individuel ?

## Contraintes, livrables et critères de réussite

**Contraintes :** recalculer les flux sur les routes partagées ; conserver la demande totale de 4 000 ; ne pas interpréter cet exemple comme une règle sur toutes les routes.

**Livrables :** graphe annoté, tableau des flux, temps et conclusion.

**Critères :** distinguer trajet et route ; vérifier les déviations individuelles ; expliquer la différence entre ensemble des choix possibles et choix effectivement réalisés.

<details><summary>Indices gradués</summary>

1. Sans liaison, chaque conducteur utilise une route congestionnée et une route à temps constant.
2. Avec tous les conducteurs au milieu, les deux routes congestionnées portent chacune 4 000 conducteurs.
3. Le conducteur qui dévie vers A → T économise un tronçon de 40 min mais le remplace par un de 45 min.
</details>

---

## Correction — Avant et après l'ouverture

<details><summary>Afficher la correction</summary>

Sans liaison, une répartition 2 000 / 2 000 donne $2\,000/100+45=65$ minutes sur chaque trajet. Une répartition déséquilibrée rend le trajet le plus chargé moins attractif.

Avec tous les conducteurs sur le trajet central, le temps vaut $4\,000/100+0+4\,000/100=80$ minutes.

Dévier seul sur un ancien trajet donnerait $40+45=85$ minutes. Personne ne gagne donc à changer seul : c'est un équilibre individuel, mais tous mettent 15 minutes de plus qu'avant, soit environ 23,08 %.

![Le réseau sans liaison répartit les trajets à 65 minutes ; avec la liaison centrale, un équilibre où tous l'empruntent donne 80 minutes et une déviation individuelle coûterait 85 minutes.](../../Slides/figures/paradoxe-braess.svg)
</details>

---

## Correction — Une ressource supplémentaire ne supprime pas les anciens plans

<details><summary>Afficher la correction</summary>

Le planificateur peut conserver l'ancienne répartition et laisser la nouvelle liaison inutilisée : 65 minutes reste un plan réalisable. Nous n'avons pas besoin de calculer ici l'optimum collectif exact pour constater qu'il fait mieux que 80 minutes.

L'ajout d'une possibilité ne dégrade pas le meilleur plan collectif réalisable dans ce modèle. Il peut cependant changer l'équilibre produit par les décisions individuelles.

C'est cette différence entre objectifs et modes de décision qui crée le paradoxe, pas une disparition mathématique des anciens trajets.
</details>

---

## Correction — Contrôle Python

<details><summary>Afficher la correction</summary>

```python
demande = 4000
avant = (demande/2)/100 + 45
apres = demande/100 + demande/100
deviation = demande/100 + 45
print(avant, apres, deviation)
print(round(100*(apres-avant)/avant, 2))
```

**Lecture :** les valeurs représentent les temps des états décrits, pas une simulation de trafic réel. Les sorties sont `65.0 80.0 85.0`, puis `23.08`.

**Erreur fréquente :** conserver un flux de 2 000 sur une route qui en porte maintenant 4 000, ou appeler l'équilibre individuel « optimum collectif ».
</details>

## Discussion — Optimiser quoi, et pour qui ?

Dans un système partagé, un choix modifie parfois le coût subi par les autres. Des recommandations individuelles peuvent déplacer les congestions plutôt que les supprimer.

**Lien data / IA :** un système de recommandation de trajets doit distinguer le coût d'un utilisateur et celui du réseau. La population, les règles de décision et les contraintes appartiennent au modèle.

Référence : [Braess et sa traduction présentés par l'UMass Amherst](https://supernet.isenberg.umass.edu/braess/braess-new.html). Le réseau chiffré ci-dessus est un exemple pédagogique idéalisé.

[Tous les problèmes du parcours](../../docs/problemes.html).
