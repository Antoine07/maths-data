# Meilleure dans chaque groupe… moins bonne au total ?

## Objectif et prérequis

**Après :** [statistiques descriptives](../../Slides/stat/01_stat_descriptive.md). **Durée :** 45 min.

**Objectif :** calculer des taux pondérés et identifier un changement de composition. Aucune probabilité avancée n'est nécessaire.

## La situation

Deux formations fictives, A et B, publient leurs résultats. A revendique de meilleurs résultats chez les débutants et les confirmés. B annonce pourtant un meilleur taux global.

Les inscriptions n'ont pas été réparties au hasard entre les formations. Il faut commencer par examiner les effectifs.

---

## Données et énoncé

| Formation | Débutants : réussites / inscrits | Confirmés : réussites / inscrits |
|---|---:|---:|
| A | 18 / 30 | 9 / 10 |
| B | 5 / 10 | 24 / 30 |

1. Calculer les quatre taux par groupe. Qui obtient le meilleur taux dans chaque groupe ?
2. Calculer les deux taux globaux à partir des nombres de réussites et d'inscrits. Le classement est-il conservé ?
3. Écrire chaque taux global comme une moyenne pondérée des taux de ses groupes.
4. Comparer les formations avec une population de référence composée de 50 % de débutants et 50 % de confirmés.
5. Peut-on conclure, à partir de ces seuls chiffres, que suivre A plutôt que B cause une meilleure réussite ?

## Contraintes, livrables et critères de réussite

**Contraintes :** conserver les effectifs ; distinguer taux observé et taux sur une population de référence. **Livrables :** tableau des taux, graphique et interprétation.

**Critères :** retrouver l'inversion du classement ; expliquer le rôle des poids sans déclarer l'un des calculs faux ; ne pas conclure à un effet causal.

<details><summary>Indices gradués</summary>

1. Un taux global utilise le total des réussites divisé par le total des inscrits.
2. A accueille surtout des débutants ; B accueille surtout des confirmés.
3. La moyenne simple des deux taux répond à une question différente si les groupes n'ont pas les mêmes tailles.
</details>

---

## Correction — Deux classements, deux compositions

<details><summary>Afficher la correction</summary>

A : 60 % chez les débutants et 90 % chez les confirmés. B : 50 % et 80 %. A est donc devant dans chacun des deux groupes.

Mais les taux globaux sont $27/40=67{,}5\%$ pour A et $29/40=72{,}5\%$ pour B.

$$
\text{A global}=0{,}75\times0{,}60+0{,}25\times0{,}90=0{,}675,
$$

$$
\text{B global}=0{,}25\times0{,}50+0{,}75\times0{,}80=0{,}725.
$$

![A dépasse B dans chacun des deux groupes, mais le classement global s'inverse parce que les proportions de débutants et de confirmés diffèrent.](../../Slides/figures/paradoxe-simpson.svg)

Avec les mêmes poids 50/50, les taux deviennent 75 % pour A et 65 % pour B. Ce sont des taux standardisés pour cette population de référence, pas les taux globaux initialement observés.
</details>

---

## Correction — Contrôle Python

<details><summary>Afficher la correction</summary>

```python
import numpy as np
reussites = np.array([[18, 9], [5, 24]])
effectifs = np.array([[30, 10], [10, 30]])
taux = reussites / effectifs
print(taux)
print(reussites.sum(axis=1) / effectifs.sum(axis=1))
print(taux @ np.array([0.5, 0.5]))
```

**Lecture :** chaque ligne représente une formation et chaque colonne un niveau. Les sorties sont les taux par groupe, `[0.675, 0.725]`, puis `[0.75, 0.65]`.

**Erreur fréquente :** utiliser directement `taux.mean(axis=1)` pour retrouver les taux globaux malgré des groupes de tailles différentes.
</details>

## Discussion — Une agrégation peut changer la question

Cette inversion illustre le paradoxe de Simpson. Comparer des populations de compositions différentes peut masquer ce qui se passe dans les groupes.

Les chiffres ne révèlent pas les autres facteurs influençant les inscriptions et les réussites. Choisir une stratification pertinente demande du contexte ; regrouper ou séparer les données ne suffit pas à démontrer une causalité.

**Lien data / IA :** examiner les performances par sous-groupes et annoncer la population de référence.

Référence : [Bickel, Hammel et O'Connell, analyse des admissions de Berkeley](https://pubmed.ncbi.nlm.nih.gov/17835295/). Les données de formation utilisées ici sont entièrement fictives.

[Tous les problèmes du parcours](../../docs/problemes.html).
