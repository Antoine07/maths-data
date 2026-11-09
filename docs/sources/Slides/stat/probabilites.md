---
marp: true
html: true
---

# Probabilités essentielles

## Des fréquences aux situations aléatoires

![Dix cases dont huit colorées représentent une fréquence observée de 8 sur 10.](../images/couverture-probabilites.svg)

Après les [statistiques descriptives](01_stat_descriptive.md), un court bloc pour comprendre les problèmes du bus, du dîner et, plus tard, des fausses alertes.

---

## Objectif

Décrire un événement, calculer une probabilité simple, distinguer conditionnement et indépendance, puis vérifier un modèle par simulation.

Prérequis : fractions, pourcentages et moyenne. Les hypothèses de hasard seront toujours explicites.

---

## Résumé général

Une probabilité décrit les chances d'un événement dans un modèle annoncé. Une fréquence décrit ce qui a été observé sur un nombre fini d'essais.

Conditionner signifie restreindre les situations considérées. L'indépendance signifie que connaître un événement ne modifie pas la probabilité de l'autre.

La simulation illustre les conséquences des hypothèses ; elle ne prouve pas que ces hypothèses décrivent le monde réel.

---

## Concepts essentiels — Issues et événements

Une expérience produit une **issue**. Un **événement** est un ensemble d'issues.

Pour un dé équilibré à six faces, les issues sont 1 à 6 et l'événement A « résultat pair » contient 2, 4 et 6.

Si les issues sont équiprobables :

$$
P(A)=\frac{\text{nombre d'issues dans A}}{\text{nombre d'issues possibles}}=\frac36=\frac12.
$$

La formule de comptage suppose l'équiprobabilité. Elle n'est pas valable simplement parce qu'une liste d'issues a été écrite.

---

## Concepts essentiels — Complément et intersection

Le complément $A^c$ signifie « A ne se produit pas ». L'intersection $A\cap B$ signifie « A et B se produisent ».

$$
P(A^c)=1-P(A).
$$

Si une réussite a une probabilité de 0,8, son échec a une probabilité de 0,2. Ces nombres sont sans unité et appartiennent à l'intervalle de 0 à 1.

Pour obtenir « au moins un succès », il est souvent plus facile de calculer le complément de « aucun succès ».

---

## Concepts essentiels — Probabilité conditionnelle

Si $P(B)>0$ :

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}.
$$

On ne regarde que les cas où B se produit, puis on cherche parmi eux ceux où A se produit aussi.

Avec le dé, A = pair et B = supérieur à 3. Les issues restantes sont 4, 5 et 6, dont deux paires : $P(A\mid B)=2/3$, alors que $P(A)=1/2$.

Le dénominateur représente la population sur laquelle porte la question.

---

## Concepts essentiels — Indépendance

Deux événements sont indépendants si :

$$
P(A\cap B)=P(A)P(B).
$$

Deux lancers indépendants d'une pièce équilibrée donnent une probabilité $1/2\times1/2=1/4$ pour deux piles.

L'indépendance est une propriété du modèle, pas une conséquence du fait qu'il y a deux colonnes ou deux personnes. Si A et B désignent exactement le même événement de probabilité 0,8, leur intersection a une probabilité 0,8, pas 0,64.

---

## Explication détaillée — Un instant uniforme

Choisir un instant uniformément dans une période signifie que les intervalles de même durée ont la même probabilité.

Reprendre la notion de [biais de sélection](01_stat_descriptive.md) : une observation à un instant au hasard ne sélectionne pas nécessairement les mêmes situations qu'un tirage d'objets avec chances égales.

Sur un cycle de vingt minutes, un intervalle de deux minutes occupe $2/20=10\%$ du temps ; un intervalle de dix-huit minutes en occupe 90 %.

Tirer un intervalle avec chances égales puis un instant à l'intérieur ne décrit pas la même expérience.

Cette distinction sera la clé du problème du bus : il faut préciser ce qui est tiré au hasard.

---

## Lecture des formules — Nombre moyen et probabilité

Pour $n$ personnes disponibles chacune avec probabilité $p$, le nombre moyen de personnes disponibles est $np$.

Avec dix personnes et $p=0{,}8$, cela donne huit personnes en moyenne. Cette formule d'espérance ne nécessite pas l'indépendance.

En revanche, pour calculer la probabilité qu'elles soient **toutes** disponibles par $p^n$, on suppose ici leur indépendance.

Un nombre moyen de personnes et une probabilité de réunion ne répondent donc pas à la même question.

---

## Exemple concret — Fréquence et fluctuation

Un événement a une probabilité de 0,2 dans notre modèle. Sur 100 essais, on ne doit pas exiger exactement 20 réussites.

Une fréquence est le nombre de réussites divisé par le nombre d'essais. Elle varie d'une expérience à l'autre.

Multiplier le nombre d'essais indépendants rend généralement la fréquence plus stable autour de la probabilité ; cela ne garantit pas qu'elle s'en rapproche à chaque nouvel essai.

---

## Lecture du code — Simuler des essais

```python
import numpy as np
rng = np.random.default_rng(42)
tirages = rng.random(100000)
succes = tirages < 0.2
print(round(float(succes.mean()), 3))
```

**Fonctionnement :** le générateur produit des valeurs uniformes entre 0 et 1 ; le seuil 0,2 transforme chaque valeur en succès ou échec.

**Exécution et résultat attendu :** une fréquence proche de 0,2. La graine rend cet exemple reproductible.

**Erreur fréquente :** croire qu'une graine fixée supprime la variabilité du phénomène modélisé. Elle fixe seulement les nombres de cette exécution.

---

## Algorithme expliqué — Du scénario à la simulation

**Entrées :** une expérience clairement décrite, ses probabilités, ses dépendances et un nombre d'essais.

**Traitement :** générer les issues, repérer l'événement, compter les succès et calculer leur fréquence.

**Sortie :** fréquence simulée et comparaison au calcul théorique.

**Exemple :** tirer deux pièces indépendantes, conserver l'essai uniquement si les deux résultats sont pile ; la fréquence doit être proche de 1/4 sur beaucoup d'essais.

Changer la façon de tirer les issues peut changer entièrement le problème simulé.

---

## Erreurs fréquentes

- Multiplier des probabilités sans justifier l'indépendance.
- Confondre $P(A\mid B)$ et $P(B\mid A)$.
- Exiger que le nombre de succès égale son espérance sur un petit échantillon.
- Confondre observation uniforme dans le temps et choix uniforme d'un intervalle.
- Interpréter une simulation correcte comme une validation empirique du modèle.

---

## Exercice 1 — Changer la population de référence

**Objectif :** calculer un conditionnement. **Prérequis :** issues du dé équilibré.

**Énoncé :** A signifie « pair » et B « supérieur à 3 ». Calculer $P(A)$, $P(B)$, $P(A\cap B)$ puis $P(A\mid B)$.

**Contraintes :** lister les issues avant les fractions. **Livrable :** quatre valeurs avec leur dénominateur. **Critère :** reconnaître les issues 4 et 6 dans l'intersection.

<details><summary>Indices gradués</summary>

1. B contient trois issues.
2. Le conditionnement retire les issues qui ne sont pas dans B.
</details>

<details><summary>Afficher la correction</summary>

$P(A)=1/2$, $P(B)=1/2$, $P(A\cap B)=2/6=1/3$ et $P(A\mid B)=2/3$. Le dénominateur de la dernière fraction est la probabilité de B, pas celle de A.
</details>

---

## Exercice 2 — Vérifier une intersection par simulation

**Objectif :** écrire une simulation autonome. **Prérequis :** tirages uniformes NumPy.

**Énoncé :** simuler 100 000 lancers de deux pièces indépendantes ; estimer la probabilité de deux piles.

**Contraintes :** deux colonnes distinctes, graine fixée. **Livrable :** code et fréquence. **Critère :** résultat proche de 0,25, avec une tolérance de 0,01.

<details><summary>Indices gradués</summary>

1. Générer un tableau `(100000, 2)`.
2. Exiger que les deux colonnes remplissent la condition avec `all(axis=1)`.
</details>

<details><summary>Afficher la correction</summary>

```python
import numpy as np
rng = np.random.default_rng(42)
piles = rng.random((100000, 2)) < 0.5
print(float(piles.all(axis=1).mean()))
```

**Lecture :** chaque ligne est une expérience à deux pièces. La sortie est proche de 0,25. Utiliser `any` répondrait à « au moins une pile ».
</details>

---

## Exercice 3 — Déboguer une indépendance inventée

**Objectif :** discuter les hypothèses. **Prérequis :** indépendance.

**Énoncé :** deux collègues partagent toujours la même disponibilité. Chacun est disponible 80 % du temps. Un programme calcule `0.8 * 0.8` pour leur disponibilité commune. Corriger le raisonnement.

**Contraintes :** garder la dépendance annoncée. **Livrable :** probabilité et explication. **Critère :** identifier que les deux événements sont identiques.

<details><summary>Indices gradués</summary>

1. Lorsque l'un est disponible, que sait-on de l'autre ?
2. L'intersection d'un événement avec lui-même est cet événement.
</details>

<details><summary>Afficher la correction</summary>

La disponibilité commune vaut 0,8. On peut simuler une seule disponibilité puis la recopier pour les deux collègues. La multiplication donnerait 0,64 dans un autre modèle où leurs disponibilités seraient indépendantes.
</details>

---

## Projet fil rouge — Décrire une fréquence

Dans le [projet consommation](../../Projet_IA/README.md), distinguer une fréquence observée de journées à forte consommation et une hypothèse probabiliste sur les prochaines journées.

**Notions mobilisées :** événement et population de référence. **Fonctionnalité :** annoncer les effectifs et les fréquences d'un événement sur chaque partition.

**Résultat vérifiable :** les fréquences proviennent des effectifs annoncés. **Livrable :** tableau et limites. **Erreur à observer :** supposer les journées indépendantes ou les distributions identiques sans examen.

Nous utiliserons plus tard ces distinctions pour interpréter les alertes d'un classifieur.

---

## Cas d'usage réels

**Entreprise :** équipe exploitant un service en ligne, scénario pédagogique.

**Problème :** comparer des incidents observés à des instants choisis au hasard et des incidents enregistrés au démarrage de chaque session.

**Solution :** définir l'expérience et les événements avant de calculer les fréquences.

**Bénéfice attendu :** éviter de comparer deux indicateurs dont les populations de référence diffèrent.

---

## Fiche de révision

- Une probabilité appartient à un modèle ; une fréquence résume des observations.
- Un conditionnement change la population de référence.
- L'indépendance autorise certains produits ; elle doit être justifiée.
- Une moyenne de comptes ne suffit pas à déterminer une probabilité d'événement.
- Une simulation teste le calcul et illustre le modèle.

---

## Questions de révision

1. Quand la formule « cas favorables / cas possibles » est-elle valable ?
2. Pourquoi le complément facilite-t-il un calcul « au moins un » ?
3. Quelle information change entre $P(A\mid B)$ et $P(B\mid A)$ ?
4. Deux personnes différentes sont-elles nécessairement indépendantes ?
5. Pourquoi deux protocoles d'observation peuvent-ils produire des moyennes différentes ?

---

## QCM

**1. Une fréquence est :** A. toujours la probabilité exacte ; B. un rapport observé sur des essais ; C. une durée ; D. une hypothèse de causalité.

**2. Pour des événements indépendants, leur intersection a pour probabilité :** A. la somme ; B. le maximum ; C. le produit ; D. toujours 0.

**3. Si $P(A)=0{,}8$, $P(A^c)$ vaut :** A. 0,2 ; B. 0,8 ; C. 1,8 ; D. 0,64.

**4. Conditionner sur B signifie :** A. supprimer B ; B. imposer l'indépendance ; C. doubler les observations ; D. considérer les cas où B se produit.

**5. Une simulation réussie prouve-t-elle que le modèle représente le réel ?** A. toujours ; B. non ; C. avec 100 000 essais ; D. avec une graine fixée.

<details><summary>Afficher la correction</summary>

1. **B** : la fréquence décrit l'échantillon observé.
2. **C** : sous l'hypothèse d'indépendance.
3. **A** : les probabilités complémentaires totalisent 1.
4. **D** : B devient la référence.
5. **B** : il faut aussi confronter les hypothèses à des observations.
</details>

---

## Résumé final

Nous savons définir ce qui est tiré au hasard, ce qui est compté et les dépendances supposées.
Ces précautions expliquent pourquoi des situations familières peuvent produire des résultats surprenants.

Explorer [le bus](../../Tps/Paradoxes/03_bus.md) et [le dîner à dix](../../Tps/Paradoxes/04_diner.md), puis continuer vers [covariance et corrélation](02_covariance_correlation.md).

Référence : [MIT — probabilités, indépendance et conditionnement](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf).
