# Problème 2 — Et si les occasions devenaient moins fréquentes ?

## Le point de départ

Sam retrouve actuellement son groupe d'amis environ deux fois par mois. Il projette 30 années supplémentaires et annonce : « Cela fait 720 occasions. »

Mais un déménagement et des emplois du temps différents pourraient rendre les rencontres moins fréquentes. Nous comparons deux scénarios, sans prétendre prédire la vie de Sam.

---

## Objectif et prérequis

**Objectif pédagogique :** distinguer une fréquence et un cumul, relier leurs variations et tester une extrapolation.

**Prérequis :** [dérivation](../../Slides/01_derivation.md), exponentielle, logarithme et dérivée d'une fonction composée.

**Durée indicative :** 60 à 75 minutes. Les notions nécessaires sur le cumul sont introduites ci-dessous.

---

## Du rythme au cumul

Le temps $t$ est mesuré en années après aujourd'hui. Le modèle de fréquence est :

$$
r(t)=24e^{-0{,}05t},\qquad t\ge0.
$$

$r(t)$ s'exprime en occasions par an. Le nombre 0,05 a l'unité inverse d'une année, afin que l'exposant soit sans unité.

On propose le cumul $C(t)=480(1-e^{-0{,}05t})$, exprimé en occasions équivalentes. Pour justifier ce cumul, vérifier $C(0)=0$ et $C'(t)=r(t)$.

Cette relation introduit l'idée de primitive : le cumul est l'aire sous une fréquence. Le modèle continu peut produire un nombre non entier ; il décrit un volume moyen modélisé.

---

## Énoncé

1. Calculer $r(0)$ et $r(30)$. Dériver $r$ et expliquer son évolution.
2. Vérifier que la fonction $C$ proposée possède la bonne valeur initiale et la bonne dérivée. Pourquoi $24t$ serait-il le cumul d'une fréquence constante ?
3. Calculer $C(30)$ et comparer à 720. Exprimer la diminution relative **par rapport au scénario constant**.
4. Trouver le temps $t_*$ tel que $C(t_*)=C(30)/2$. Est-ce 15 ans ? Expliquer la réponse avec les courbes.
5. Calculer la limite de $C(t)$ lorsque $t$ tend vers l'infini. Quelle hypothèse du modèle explique ce résultat ?

---

## Contraintes, livrables et critères de réussite

**Contraintes :** différencier occasions/an et occasions ; conserver des valeurs non arrondies pendant les calculs ; annoncer que la loi exponentielle est une hypothèse.

**Livrables :** dérivées, calcul du cumul, résolution logarithmique, deux courbes et conclusion.

**Critères de réussite :** unités cohérentes, cumul croissant malgré une fréquence décroissante et moitié du cumul située avant 15 ans.

<details><summary>Indices gradués</summary>

1. La dérivée de $e^{-0{,}05t}$ vaut $-0{,}05e^{-0{,}05t}$.
2. Résoudre d'abord l'équation pour $e^{-0{,}05t_*}$, puis appliquer le logarithme.
3. Le pourcentage demandé utilise 720 au dénominateur, car c'est la référence annoncée.
</details>

---

## Correction — Fréquence et cumul

<details><summary>Afficher la correction</summary>

$r(0)=24$ occasions/an et $r(30)=24e^{-1{,}5}\approx5{,}36$ occasions/an.

La dérivée $r'(t)=-1{,}2e^{-0{,}05t}$ est négative : le rythme baisse. Mais $C'(t)=24e^{-0{,}05t}>0$ : le cumul continue d'augmenter, de plus en plus lentement. Sa valeur initiale est nulle.

$$
C(30)=480(1-e^{-1{,}5})\approx372{,}90.
$$

Le scénario décroissant donne environ 347,10 occasions équivalentes de moins que la référence de 720, soit une diminution de $347{,}10/720\approx48{,}21\%$ par rapport à cette référence.

![À gauche, la fréquence descend de 24 à environ 5,36 par an ; à droite, le cumul croît plus lentement que le scénario constant.](../../Slides/figures/tail-02-frequence.svg)
</details>

---

## Correction — La moitié avant la mi-temps

<details><summary>Afficher la correction</summary>

L'équation $C(t_*)=C(30)/2$ conduit à :

$$
e^{-0{,}05t_*}=\frac{1+e^{-1{,}5}}2,
\qquad
t_*=-\frac{\ln((1+e^{-1{,}5})/2)}{0{,}05}\approx9{,}83\text{ ans}.
$$

La moitié du cumul prévu sur les 30 années apparaît avant le tiers de l'horizon, car les rencontres sont plus fréquentes au début.

La limite à l'infini vaut 480. Elle découle de la décroissance exponentielle supposée de la fréquence. Ce n'est pas une limite naturelle au nombre de rencontres d'une personne : modifier la loi change la conclusion.
</details>

---

## Correction — Contrôle avec Python

<details><summary>Afficher la correction</summary>

```python
import numpy as np
horizon = 30.0
cumul = 480 * (1 - np.exp(-0.05*horizon))
moitie = -np.log((1 + np.exp(-0.05*horizon))/2) / 0.05
print(round(cumul, 2), round(moitie, 2))
print(round(100*(720-cumul)/720, 2))
```

**Lecture :** l'entrée est un horizon de 30 ans ; le code évalue l'exponentielle, résout la moitié par logarithme et compare à la référence. Sorties : `372.9 9.83`, puis `48.21`.

**Erreur fréquente :** résoudre $r(t)=r(30)/2$, ce qui porte sur une fréquence et non sur la moitié des occasions cumulées.
</details>

---

## Discussion — Un modèle peut changer la décision

Avant d'utiliser la formule, Sam devrait examiner si la fréquence diminue réellement, si elle comporte des ruptures et si un changement d'organisation peut la modifier.

**Lien data :** une extrapolation sur 30 ans à partir d'une fréquence actuelle contient une hypothèse forte. Dessiner plusieurs scénarios rend cette hypothèse visible ; cela ne valide pas le scénario le plus spectaculaire.

[Retour aux quatre problèmes](README.md). Point de départ conceptuel : [*The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html) ; modèle et données créés pour ce problème.
