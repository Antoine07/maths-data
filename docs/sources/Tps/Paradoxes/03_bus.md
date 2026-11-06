# Pourquoi j'attends toujours le bus ?

## Objectif et prérequis

**Après :** [statistiques descriptives](../../Slides/stat/01_stat_descriptive.md) et [probabilités essentielles](../../Slides/stat/probabilites.md). **Durée :** 45 min.

**Objectif :** distinguer une moyenne calculée par intervalle d'une moyenne observée à un instant choisi au hasard.

## La situation

Le réseau annonce un intervalle moyen de dix minutes. Noé pense donc attendre cinq minutes en moyenne. Pourtant, il tombe souvent dans une longue période sans bus.

Comparer deux lignes fictives. La première passe exactement toutes les dix minutes. Sur la seconde, les intervalles alternent indéfiniment : **2 minutes, puis 18 minutes**.

Les voyageurs arrivent à un instant uniforme dans le temps, sans regarder l'horaire. Il n'y a ni trajet manqué ni limitation de capacité.

---

## Énoncé

1. Calculer l'intervalle moyen sur chaque ligne. Calculer la variance des deux types d'intervalle sur la seconde ligne, en les pondérant chacun par 1/2.
2. Sur un cycle de vingt minutes de la seconde ligne, quelle est la probabilité d'arriver dans l'intervalle court ? Dans l'intervalle long ?
3. À l'intérieur d'un intervalle de longueur $L$, choisi à un instant uniforme, justifier une attente moyenne de $L/2$.
4. Calculer l'attente moyenne sur chaque ligne. Pourquoi la moyenne $(1+9)/2$ est-elle incorrecte pour le voyageur de la seconde ligne ?
5. Simuler 200 000 arrivées sur le cycle de vingt minutes et comparer la moyenne observée au calcul.

## Contraintes, livrables et critères de réussite

**Contraintes :** respecter le mode de sélection des voyageurs ; exprimer les temps en minutes. **Livrables :** pondérations, calcul, simulation et conclusion.

**Critères :** mêmes intervalles moyens mais attentes différentes ; pondérations temporelles correctes ; simulation proche du résultat théorique.

<details><summary>Indices gradués</summary>

1. L'intervalle long occupe 18 des 20 minutes du cycle.
2. La moyenne d'attente conditionnelle est 1 minute dans le petit intervalle et 9 dans le grand.
3. Dans la simulation, le prochain bus passe à la minute 2 ou à la minute 20, selon l'instant d'arrivée.
</details>

---

## Correction — Le voyageur ne tire pas un intervalle au hasard

<details><summary>Afficher la correction</summary>

Les deux intervalles moyens valent 10 minutes. La variance des intervalles de la seconde ligne vaut $((2-10)^2+(18-10)^2)/2=64$ minutes carrées.

Un voyageur arrivant au hasard tombe dans le petit intervalle avec probabilité $2/20=0{,}1$ et dans le grand avec probabilité $18/20=0{,}9$.

La première ligne donne une attente moyenne de 5 minutes. La seconde donne :

$$
0{,}1\times1+0{,}9\times9=8{,}2\text{ minutes}.
$$

![Un instant choisi au hasard tombe plus souvent dans l'intervalle de 18 minutes que dans celui de 2 minutes. Les attentes moyennes sont 5 et 8,2 minutes.](../../Slides/figures/paradoxe-bus.svg)

La moyenne $(1+9)/2$ correspondrait à un autre protocole : tirer l'un des deux intervalles avec chances égales, puis un instant dans cet intervalle. Ce n'est pas l'arrivée uniforme dans le temps annoncée.
</details>

---

## Correction — Contrôle Python

<details><summary>Afficher la correction</summary>

```python
import numpy as np
rng = np.random.default_rng(42)
arrivees = rng.uniform(0, 20, 200000)
attentes = np.where(arrivees < 2, 2-arrivees, 20-arrivees)
print(round(float(attentes.mean()), 2))
print(0.1*1 + 0.9*9)
```

**Lecture :** les entrées simulées sont des instants sur un cycle complet. La condition choisit le prochain passage ; les sorties sont environ `8.21` et `8.2`. Un petit écart est normal pour une simulation finie.

**Erreur fréquente :** tirer directement `2` ou `18` avec probabilités égales pour représenter l'intervalle rencontré par un voyageur.
</details>

## Discussion — La manière d'observer change les poids

Les longs intervalles ont davantage de chances d'être observés à un instant pris au hasard. C'est une forme de biais de longueur, apparentée au paradoxe de l'inspection.

**Lien data :** un échantillon de sessions actives observées à midi surreprésente les longues sessions par rapport à un échantillon de sessions démarrées dans la journée. Avant de généraliser une moyenne, décrire le protocole d'observation.

Référence : [MIT — paradoxe d'incidence aléatoire](https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/332143a27afa79791971c948f82b032a_sG3_Bveu_cA.pdf). Le scénario périodique 2/18 est créé pour cet exercice ; ce n'est pas le processus de Poisson du cours cité.

[Tous les problèmes du parcours](../../docs/problemes.html).
