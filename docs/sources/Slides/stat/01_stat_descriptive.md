---
marp: true
theme: default
paginate: true
class: lead
html: true
---

# Statistiques descriptives avec NumPy

## Cours + corrections detaillees

![Les valeurs 2, 3, 3, 4 et 8 sur une ligne, avec leur médiane 3 et leur moyenne 4.](../images/couverture-statistiques.svg)

---

## Objectifs

1. Savoir pourquoi et quand observer un échantillon
2. Distinguer décrire les données et estimer une population
3. Comprendre techniquement pourquoi les écarts à la moyenne ont `n−1` degrés de liberté
4. Choisir `ddof` à partir de la question, puis utiliser les fonctions NumPy
5. Repérer un biais de sélection et interpréter moyenne, dispersion et quartiles

---

## Pourquoi utilise-t-on un échantillon ?

On veut souvent connaître une caractéristique d'un ensemble trop grand, trop coûteux à observer intégralement ou qui contient encore des événements futurs.

Exemples : interroger une partie des utilisateurs d'une application, contrôler quelques pièces lorsque le contrôle les détruit, ou observer des journées de consommation pour préparer un modèle sur de nouvelles journées.

On recueille alors un **échantillon** : une partie des observations possibles. L'objectif peut être d'estimer une moyenne ou une dispersion inconnue de la population cible.

Échantillonner économise des mesures, mais introduit une incertitude. Il faut expliquer comment les observations ont été choisies.

---

## Population cible, observation et question posée

La **population cible** est l'ensemble sur lequel porte notre question. Une **observation** correspond à une unité de cet ensemble : personne, pièce, requête ou journée, selon le problème.

Exemple fictif : on veut connaître les heures d'étude hebdomadaires des 100 étudiants d'une promotion. On interroge 20 étudiants : ces 20 réponses constituent l'échantillon.

La moyenne des 20 réponses est connue une fois les données recueillies. La moyenne des 100 étudiants reste à **estimer** si l'on n'a pas observé les autres.

Même fichier, deux questions : « Que décrivent ces 20 réponses ? » et « Que peut-on en déduire sur toute la promotion ? »

---

## Comment sélectionner les observations ?

Un tirage aléatoire simple donne aux observations de la population une chance annoncée d'être retenues. Une sélection par groupes peut aussi être organisée, mais le calcul doit tenir compte du plan retenu.

Prendre les 20 premiers volontaires ou interroger uniquement les participants à un atelier est un autre procédé : certaines situations peuvent être exclues ou surreprésentées.

Dans le projet consommation, les journées sont chronologiques. On ne suppose pas automatiquement qu'elles sont indépendantes ni qu'elles ont toutes la même distribution : saison et usage peuvent changer.

Pour expliquer la correction `n−1`, nous utiliserons ensuite un modèle simple d'observations indépendantes de même distribution, de variance finie. Cette hypothèse sera annoncée.

---

## Qu'est-ce qu'un biais d'échantillonnage ?

Un biais de sélection apparaît lorsque la manière de recueillir les données favorise certaines situations et peut déformer systématiquement la conclusion sur la population cible.

Dans un exemple fictif, 50 étudiants suivent un atelier et étudient chacun 4 h par semaine ; les 50 autres étudient chacun 2 h. La moyenne de la promotion vaut $(50\times4+50\times2)/100=3$ h.

Interroger uniquement les participants à l'atelier donne 4 h. Passer de 10 à 50 réponses de ce même groupe ne répare pas l'exclusion des autres étudiants.

Ce qui constitue un biais dépend aussi de la question : 4 h décrit correctement le groupe de l'atelier, mais pas l'ensemble de la promotion.

---

## Fluctuation : même méthode, résultats différents

Deux tirages aléatoires peuvent donner deux moyennes différentes. Cette variation due au hasard est la **fluctuation d'échantillonnage**. Un échantillon n'a pas à reproduire exactement la population à chaque essai.

Le biais de sélection concerne le procédé d'observation. La fluctuation concerne les différences entre tirages obtenus avec un même procédé.

Un troisième sujet arrive maintenant : quand on utilise un échantillon pour estimer une variance, le calcul lui-même peut être biaisé. C'est ce que la correction `n−1` va traiter ; elle ne répare pas la sélection des observations.

---

## Avant la variance : calculer le centre

Avec $n$ observations $x_1,\ldots,x_n$, leur moyenne est :

$$
\bar{x}=\frac1n\sum_{i=1}^{n}x_i.
$$

L'écart de la valeur $x_i$ à ce centre est $e_i=x_i-\bar{x}$. Une variance décrit la taille des écarts en utilisant leurs carrés : leur signe ne peut plus les annuler.

Exemple : pour $x=(2,4,6)$, la moyenne vaut 4 et les écarts valent $(-2,0,2)$. Leur somme est nulle, mais la somme de leurs carrés vaut $4+0+4=8$.

---

## Le calcul qui fait apparaître une contrainte

Lorsque le centre est la moyenne **calculée sur ces mêmes données** :

$$
\sum_{i=1}^{n}e_i=\sum_{i=1}^{n}(x_i-\bar{x})
=\sum_{i=1}^{n}x_i-n\bar{x}=0.
$$

La dernière égalité vient directement de la définition de la moyenne : $n\bar{x}=\sum_i x_i$.

Les écarts ne sont donc pas $n$ nombres pouvant varier librement : ils doivent respecter une équation. Ce n'est pas une hypothèse statistique ; c'est une identité algébrique.

---

## Techniquement, pourquoi n−1 degrés de liberté ?

Un **degré de liberté** est ici une coordonnée que l'on peut choisir sans violer les contraintes.

Pour les $n$ écarts centrés, une fois les $n-1$ premiers fixés, le dernier est imposé :

$$
e_n=-\sum_{i=1}^{n-1}e_i.
$$

Avec trois valeurs, si les deux premiers écarts sont -2 et 0, le troisième vaut nécessairement +2. Il reste **deux** degrés de liberté.

![Les écarts -2 et 0 imposent le troisième écart +2, car leur somme doit être nulle. Trois écarts centrés ont donc deux degrés de liberté.](../images/statistiques-degres-liberte.svg)

Les trois observations restent utilisées. C'est la représentation de leurs écarts à leur propre moyenne qui comporte une contrainte ; on ne supprime aucune ligne.

---

## Pourquoi cela affecte-t-il la variance estimée ?

La moyenne de l'échantillon est choisie à partir des observations. Elle minimise la somme des carrés des distances à un centre.

Si $\mu$ désigne la vraie moyenne de la population, inconnue en pratique :

$$
\sum_i(x_i-\bar{x})^2
=\sum_i(x_i-\mu)^2-n(\bar{x}-\mu)^2.
$$

On retire donc une quantité positive ou nulle en recentrant autour de la moyenne calculée. Les écarts paraissent plus petits qu'autour du centre réel.

Exemple : pour $(2,4,6)$ et une vraie moyenne $\mu=5$, les carrés des écarts au centre réel totalisent 11 ; au centre calculé 4, ils totalisent $11-3(4-5)^2=8$.

---

## Le n−1 corrige quoi exactement ?

Sous le modèle annoncé — observations indépendantes de même distribution, moyenne $\mu$ et variance $\sigma^2$ finie — la somme des carrés autour de la moyenne calculée vaut **en moyenne sur les échantillons** $(n-1)\sigma^2$.

On estime donc la variance de population avec :

$$
s^2=\frac{\sum_i(x_i-\bar{x})^2}{n-1},\qquad n>1.
$$

Le comptage des degrés de liberté explique le $n-1$ ; le calcul en moyenne ci-dessous justifie la correction de biais. Il ne garantit pas une meilleure estimation pour chaque échantillon pris isolément.

<details><summary>Voir la justification technique complète</summary>

$\mathbb{E}$ désigne ici la moyenne théorique sur les échantillons possibles. L'identité précédente donne :

$$
\mathbb{E}\!\left[\sum_i(X_i-\bar{X})^2\right]
=n\sigma^2-n\mathbb{E}[(\bar{X}-\mu)^2].
$$

La moyenne de l'échantillon est centrée sur $\mu$ et sa variance vaut $\sigma^2/n$ : l'indépendance permet d'additionner les variances des observations avant de diviser par $n^2$.

$$
\mathbb{E}\!\left[\sum_i(X_i-\bar{X})^2\right]
=n\sigma^2-n\frac{\sigma^2}{n}=(n-1)\sigma^2.
$$

Diviser par $n-1$ donne donc $\mathbb{E}[s^2]=\sigma^2$. C'est le sens précis de « sans biais » pour cet estimateur de variance, sous ces hypothèses.

Si l'on prélève sans remise une fraction importante d'une population finie, on doit tenir compte du plan de sondage et de la convention de variance de cette population. Le calcul ci-dessus correspond au modèle indépendant annoncé.
</details>

---

## Le même exemple, deux questions différentes

Pour les valeurs observées $(2,4,6)$, la somme des carrés des écarts vaut 8.

**Décrire ces trois valeurs :** la moyenne de leurs écarts au carré vaut $8/3\approx2{,}67$. Ce calcul est correct pour décrire ce tableau, même s'il ne contient qu'une partie d'une population plus large.

**Estimer la variance d'une population à partir d'un échantillon indépendant :** la correction précédente donne $8/(3-1)=4$.

Les deux nombres utilisent les mêmes données mais répondent à deux questions. Le choix ne dépend pas seulement du fait que le fichier s'appelle « échantillon ».

---

## Maintenant, traduire avec NumPy : ddof

Dans `np.var`, `ddof` signifie **Delta Degrees of Freedom** : le dénominateur est `n - ddof`.

| Objectif | Dénominateur | NumPy |
|---|---:|---|
| Décrire la dispersion des valeurs observées | $n$ | `np.var(x, ddof=0)` |
| Estimer la variance de population, sous le modèle précédent | $n-1$ | `np.var(x, ddof=1)` |

`ddof=1` ne signifie pas « il reste un degré de liberté ». Il signifie qu'on retire 1 à $n$ : avec trois valeurs, il reste deux degrés de liberté pour les écarts centrés.

Pour `np.std`, le résultat est la racine de la variance avec le même dénominateur. La racine de la variance corrigée n'est pas, en général, un estimateur sans biais de l'écart-type.

---

## Lecture du code — Aucun point n'a disparu

```python
import numpy as np
x = np.array([2., 4., 6.])
ecarts = x - x.mean()
carres = np.sum(ecarts**2)
print(ecarts, ecarts.sum())        # [-2.  0.  2.] 0.0
print(len(x), len(x) - 1)         # 3 observations, 2 degrés de liberté
print(carres / len(x))            # 2.666666...
print(carres / (len(x) - 1))      # 4.0
print(np.var(x, ddof=0), np.var(x, ddof=1))
```

**Fonctionnement :** les trois valeurs servent à calculer la moyenne, les trois écarts et leurs trois carrés. Seul le dénominateur change selon l'objectif.

**Erreur fréquente :** retirer une observation, ou croire que `ddof=1` modifie les écarts. Il ne change ici ni le centre ni la somme des carrés.

---

## Et si la vraie moyenne était déjà connue ?

Lorsque la vraie moyenne $\mu$ est connue indépendamment des données, on peut estimer la variance par la moyenne des $(x_i-\mu)^2$, avec un dénominateur $n$.

On n'a alors pas estimé ce centre sur le même échantillon et les écarts à $\mu$ ne sont pas contraints de totaliser zéro.

Dans notre exemple avec $\mu=5$, ils valent $(-3,-1,1)$, de somme -3. La moyenne des carrés vaut $11/3$.

Attention : `np.var(x, ddof=0)` recentre par défaut sur la moyenne du tableau, pas sur cette moyenne externe. Pour ce cas, écrire explicitement `np.mean((x - mu)**2)`.

---

## Vérifier sur tous les petits échantillons possibles

Prenons une population pédagogique $(2,4,6,8)$, dont la variance vaut 5. Former tous les échantillons de trois tirages **indépendants avec remise** donne $4^3=64$ suites équiprobables.

La moyenne des 64 variances divisées par $n$ vaut environ 3,33. La moyenne des 64 variances divisées par $n-1$ vaut exactement 5 à l'arrondi numérique près.

<details><summary>Afficher le code de vérification</summary>

```python
from itertools import product
import numpy as np
population = np.array([2., 4., 6., 8.])
echantillons = np.array(list(product(population, repeat=3)))
print(population.var())
print(np.var(echantillons, axis=1, ddof=0).mean())
print(np.var(echantillons, axis=1, ddof=1).mean())
```

**Lecture :** chaque ligne est l'une des 64 suites de tirages. On calcule une variance par ligne, puis leur moyenne. Les sorties sont `5.0`, environ `3.333333`, puis `5.0`.

Cette expérience illustre la correction **en moyenne** sur les échantillons. Elle ne dit pas que chaque variance corrigée est égale à 5.
</details>

---

## À vous — Retrouver le dernier écart

La moyenne vient d'être calculée sur quatre observations. Leurs trois premiers écarts à cette moyenne valent -3, +1 et 0.

1. Déterminer le quatrième écart.
2. Donner le nombre de degrés de liberté des écarts centrés.
3. Calculer la variance descriptive, puis la variance corrigée utilisée pour l'estimation sous le modèle annoncé.

<details><summary>Afficher la correction</summary>

Le quatrième écart vaut +2, pour que la somme soit nulle. Les quatre écarts ont trois degrés de liberté.

La somme des carrés vaut $9+1+0+4=14$. La variance descriptive vaut $14/4=3{,}5$ ; la variance corrigée vaut $14/3\approx4{,}67$.
</details>

---

## Choisir avant de lancer la fonction

1. Quelle population veut-on décrire ou étudier ?
2. A-t-on toutes ses valeurs, un échantillon choisi selon un protocole, ou seulement des observations de convenance ?
3. Veut-on décrire ce tableau ou estimer une variance au-delà de ce tableau ?
4. Les hypothèses de l'estimation sont-elles défendables ?

Le `n−1` ne répare ni un biais de sélection, ni une dépendance temporelle, ni une population cible mal définie.

Référence pour le calcul de `ddof` : [documentation officielle de NumPy](https://numpy.org/doc/stable/reference/generated/numpy.var.html).

---

## Exercice 1 - Ages

Donnees :

```python
import numpy as np
ages = np.array([12, 15, 14, 13, 16, 15], dtype=float)
```

---

## Exercice 1 - Moyenne et mediane

Consigne :

1. Calculez la moyenne avec NumPy
2. Calculez la mediane avec NumPy
3. Interpretez les 2 valeurs

<details>
<summary>Afficher la correction</summary>

```python
mean_age = np.mean(ages)
median_age = np.median(ages)

print(mean_age)    # 14.166666666666666
print(median_age)  # 14.5
```

$$
\bar{x}=\frac{85}{6}\approx 14.17,\qquad \text{Mediane}=14.5
$$

Interpretation : l'age central (mediane) est legerement au-dessus de la moyenne.
</details>

---

## Exercice 1 — Décrire ou estimer avec les mêmes âges

Consigne :

1. Pour décrire uniquement les six âges du tableau, calculer variance et écart-type avec `ddof=0`.
2. Supposer ensuite que ces six âges proviennent d'observations indépendantes de même distribution dans une population plus large : calculer la variance corrigée avec `ddof=1` et sa racine.
3. Expliquer la question associée à chaque calcul et les cinq degrés de liberté des écarts centrés.

<details>
<summary>Afficher la correction</summary>

```python
var_pop = np.var(ages, ddof=0)
std_pop = np.std(ages, ddof=0)

var_sample = np.var(ages, ddof=1)
std_sample = np.std(ages, ddof=1)

print(var_pop, std_pop)        # 1.805555... 1.343709...
print(var_sample, std_sample)  # 2.166666... 1.471960...
```

Description des six valeurs observées :

$$
\text{Var}=\frac{1}{n}\sum (x_i-\bar{x})^2\approx 1.81,\qquad
\sigma\approx 1.34
$$

`ddof=1` donne une variance un peu plus grande en remplaçant le dénominateur `n` par `n-1`. Cette correction du biais d'estimation de la variance ne rend pas un échantillon mal sélectionné représentatif.

Les six écarts à la moyenne totalisent zéro : une fois cinq écarts fixés, le sixième est imposé. Les six âges contribuent pourtant tous à la somme des carrés.
</details>

---

## Exercice 3 - Tailles

Donnees :

```python
tailles = np.array([160, 170, 175, 150, 165], dtype=float)
```

Tableau d'effectifs :

| Taille   | 150 | 160 | 165 | 170 | 175 |
| -------- | --- | --- | --- | --- | --- |
| Effectif | 1   | 1   | 1   | 1   | 1   |

---

## Exercice 3 - Moyenne et dispersion (NumPy)

Consigne :

1. Décrire uniquement ces cinq tailles : calculer moyenne, variance et écart-type avec `ddof=0`.
2. Donnez les interpretations

<details>
<summary>Afficher la correction</summary>

```python
m = np.mean(tailles)
v = np.var(tailles, ddof=0)
s = np.std(tailles, ddof=0)

print(m, v, s)  # 164.0 74.0 8.602325267...
```

$$
\bar{x}=164,\qquad \text{Var}=74,\qquad \sigma\approx 8.60
$$

Interprétation : l'écart-type vaut environ 8,6 cm autour de la moyenne de 164 cm. Il repose sur les carrés des écarts ; ce n'est pas la moyenne des distances absolues à la moyenne.
</details>

---

## Exercice 3 - Quartiles avec NumPy

Consigne :

1. Triez la serie
2. Calculez `Q1` avec la methode du cours (rang `(n+1)/4`)
3. Comparez avec la methode par defaut de NumPy

<details>
<summary>Afficher la correction</summary>

```python
x = np.sort(tailles)
q1_weibull = np.percentile(x, 25, method="weibull")  # methode (n+1)/4
q1_linear  = np.percentile(x, 25, method="linear")   # defaut NumPy

print(q1_weibull)  # 155.0
print(q1_linear)   # 160.0
```

Avec la methode du cours :

$$
r=\frac{n+1}{4}=\frac{6}{4}=1.5,
\qquad
Q_1=150+0.5(160-150)=155
$$

Point cle : pour etre coherent avec la correction du cours, utiliser `method="weibull"`.
</details>

---

## Resume des fonctions NumPy

1. `np.mean(x)` : moyenne
2. `np.median(x)` : mediane
3. `np.var(x, ddof=0)` : variance population
4. `np.std(x, ddof=0)` : ecart-type population
5. `np.percentile(x, 25, method="weibull")` : `Q1` version cours

Pour **estimer** une variance de population avec une moyenne estimée sur un échantillon indépendant, utiliser `np.var(x, ddof=1)` ; le dénominateur devient `n−1`. Pour décrire les valeurs présentes, `ddof=0` reste correct.

---

## Problème — Quand le classement change avec les poids

Une formation réussit mieux chez les débutants et chez les confirmés, mais obtient un taux global inférieur. Est-ce contradictoire ?

[Explorer le paradoxe de Simpson](../../Tps/Paradoxes/02_simpson.md).

Puis suivre les [probabilités essentielles](probabilites.md) pour préparer les problèmes du bus et du dîner à dix.
