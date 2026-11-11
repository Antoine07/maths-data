---
marp: true
html: true
paginate: true
---

# Fonctions périodiques

Sinus, cosinus, période et fréquence.

![À gauche, un profil de consommation électrique simulé qui se répète sur deux jours. À droite, les heures 23 h et 0 h sont voisines sur le cercle et se codent avec sinus et cosinus.](images/fonctions-ia-cyclique.svg)

En IA, on peut encoder l'heure du jour par une paire sinus/cosinus pour aider un modèle à reconnaître les cycles d'une série temporelle, par exemple pour prévoir la consommation électrique. Ce codage représente la périodicité des horaires ; il ne suppose pas que la consommation réelle soit un sinus parfait.

---

## Objectif

Reconnaître un phénomène périodique, lire une période sur un graphique et passer d'une période à une fréquence. Relier le coefficient du sinus ou du cosinus au nombre de cycles observés.

Les prérequis sont les fractions, les unités et la lecture d'une courbe. Un tour complet correspond à $360^\circ=2\pi$ radians.

Dans ce chapitre, on part d'un angle, puis on décrit un signal qui évolue au cours du temps. Les unités de la variable accompagnent chaque calcul.

---

## Sinus et cosinus

Sur le cercle de rayon 1, le point associé à l'angle $x$ a pour coordonnées $(\cos x,\sin x)$. Les deux fonctions prennent leurs valeurs entre -1 et 1.

| Angle $x$ en radians | $0$ | $\pi/2$ | $\pi$ | $3\pi/2$ | $2\pi$ |
|---|---:|---:|---:|---:|---:|
| $\sin x$ | 0 | 1 | 0 | -1 | 0 |
| $\cos x$ | 1 | 0 | -1 | 0 | 1 |

Le sinus vaut 0 à l'origine et le cosinus vaut 1. Un décalage d'un quart de tour relie les deux fonctions.

$$
\cos x=\sin\left(x+\frac\pi2\right).
$$

---

## Qu'est-ce qu'une période ?

Une fonction est **périodique** lorsqu'il existe un nombre $T>0$ tel que, pour tout $x$ de son domaine,

$$
h(x+T)=h(x).
$$

La courbe se reproduit après une translation horizontale de longueur $T$. La plus petite période strictement positive, lorsqu'elle existe, est appelée **période fondamentale**. C'est celle que nous cherchons dans les exercices.

Pour le sinus et le cosinus usuels,

$$
\boxed{T=2\pi\text{ radians}=360^\circ}.
$$

$$
\sin(x+2\pi)=\sin x,\qquad \cos(x+2\pi)=\cos x.
$$

Les décalages $4\pi$ et $6\pi$ reproduisent également ces courbes. Leur plus petit cycle complet mesure $2\pi$.

---

## Lire une période sur les courbes

![Courbes du sinus et du cosinus entre 0 et 4 pi radians. Une flèche de 0 à 2 pi indique un cycle complet commun aux deux fonctions.](images/fonctions-sinus-cosinus.svg)

Pour lire la période, mesurer l'écart horizontal entre deux maxima consécutifs d'une même courbe. Deux minima consécutifs donnent le même résultat.

Un cycle complet retrouve la même valeur et le même sens de variation. Pour le sinus, les passages par zéro en 0 et en $\pi$ sont espacés d'une demi-période. En $2\pi$, on retrouve le passage croissant de l'origine.

---

## Période et fréquence d'un signal temporel

La **période** est la durée d'un cycle. La **fréquence** est le nombre de cycles par unité de temps.

$$
\boxed{f=\frac1T},\qquad \boxed{T=\frac1f}.
$$

| Grandeur | Symbole | Unité si le temps est en secondes |
|---|---|---|
| Période | $T$ | seconde, s |
| Fréquence | $f$ | hertz, Hz, soit un cycle par seconde |

Un signal qui effectue 5 oscillations par seconde a une fréquence de 5 Hz. Sa période vaut $T=1/5=0{,}2$ s.

Pour un cycle toutes les 2 secondes, $T=2$ s et $f=1/2=0{,}5$ Hz. Plus la période est courte, plus le nombre de cycles par seconde augmente.

---

## Garder les unités du temps

Lorsque la variable $x$ représente un angle, la période de $\sin x$ s'exprime en **radians**. Pour un signal dépendant du temps $t$, elle s'exprime dans l'unité de ce temps.

| Signal temporel | Période | Fréquence |
|---|---:|---:|
| Un cycle toutes les 2 secondes | 2 s | 0,5 Hz |
| Un cycle toutes les 24 heures | 24 h | $1/24$ cycle/h |
| Un cycle par jour | 1 jour | 1 cycle/jour |

Les deux dernières lignes décrivent la même fréquence. Pour l'exprimer en hertz, convertir la journée en secondes.

$$
24\text{ h}=86\,400\text{ s},\qquad
f=\frac1{86\,400}\text{ Hz}.
$$

---

## Modifier le coefficient du sinus ou du cosinus

Pour un signal temporel de la forme

$$
y(t)=\sin(\omega t+\phi_0),
$$

la **phase** à l'instant $t$ est l'angle $\phi(t)=\omega t+\phi_0$. C'est l'angle où se trouve l'aiguille sur le cercle. La **pulsation** $\omega$ indique à quelle vitesse cet angle change.

![Sur le cercle, la phase est l'angle de l'aiguille. Quand le temps avance, la pulsation détermine la vitesse de rotation ; le sinus suit la projection verticale de l'aiguille.](images/fonctions-phase-pulsation.svg)

Le cosinus correspond au même mouvement avec un décalage de phase de $\pi/2$, car $\cos x=\sin(x+\pi/2)$.

La pulsation s'exprime en radians par unité de temps. Pour $\omega>0$, l'aiguille tourne dans le sens trigonométrique ; pour $\omega<0$, elle tourne dans l'autre sens. On suppose $\omega\ne0$.

Un cycle complet correspond à une variation de $2\pi$ de l'angle. On obtient donc $|\omega|T=2\pi$, puis

$$
\boxed{T=\frac{2\pi}{|\omega|}},\qquad
\boxed{f=\frac{|\omega|}{2\pi}}.
$$

Si $t$ est en secondes, $\omega$ est en rad/s, $T$ en secondes et $f$ en hertz. Si $t$ est en heures, on utilise rad/h, heures et cycles/h.

---

## Quatre exemples avec un angle

Dans ce tableau, $x$ est exprimé en radians.

| Fonction | Coefficient de $x$ | Période fondamentale |
|---|---:|---:|
| $\sin(x)$ | $1$ | $2\pi$ radians |
| $\sin(2x)$ | $2$ | $\pi$ radians |
| $\sin(4x)$ | $4$ | $\pi/2$ radians |
| $\cos(x/2)$ | $1/2$ | $4\pi$ radians |

Pour $\sin(4x)$, l'angle intérieur avance de $2\pi$ lorsque $x$ avance de $\pi/2$.

Pour $\cos(x/2)$, il faut avancer $x$ de $4\pi$ pour que l'angle intérieur avance de $2\pi$.

Plus le coefficient est grand en valeur absolue, plus la période est courte. Un coefficient négatif change le sens de parcours de l'angle tout en conservant la période associée à sa valeur absolue.

---

## Comparer des périodes sur les mêmes axes

![Sur la même fenêtre de 0 à 4 pi radians, sinus de x effectue deux cycles, sinus de 2x quatre, sinus de 4x huit et cosinus de x sur 2 un seul. Une zone colorée représente une période de chaque fonction.](images/fonctions-periodes.svg)

L'axe horizontal couvre le même intervalle sur les quatre graphiques. Les zones colorées marquent chacune un cycle complet.

La hauteur des oscillations vaut toujours 1 de part et d'autre de zéro. Le changement du coefficient agit sur l'espacement horizontal des cycles.

---

## Retrouver le cycle de température

Le signal idéal de l'exercice de température s'écrit, avec $t$ en heures,

$$
T_{ideal}(t)=10+5\sin\left(\frac{2\pi}{24}t\right).
$$

La lettre $T_{ideal}$ désigne ici la température. Appelons $P$ sa période temporelle pour garder les deux grandeurs distinctes.

$$
\omega=\frac{2\pi}{24}\text{ rad/h},\quad
P=24\text{ h},\quad f=\frac1{24}\text{ cycle/h}.
$$

Le nombre 10 fixe le niveau central, et 5 l'amplitude des oscillations en degrés Celsius. Ces deux paramètres conservent la période de 24 h.

Le sinus décrit un cycle quotidien idéal. Le TP ajoute des fluctuations aléatoires à ce signal. Les calculs de période portent ici sur sa composante sinusoïdale.

[Continuer avec l'exercice de température](01_derivation.md).

---

## Exercice 1 — Compter des cycles

Un signal réalise 4 cycles complets en 2 secondes.

1. Déterminer sa fréquence en hertz.
2. Calculer sa période en secondes.
3. Pour les courbes classiques du sinus et du cosinus, donner la période en radians et expliquer le décalage entre elles.

<details><summary>Indice</summary>

Diviser le nombre de cycles par la durée totale, puis utiliser la relation entre période et fréquence.

</details>

<details><summary>Afficher la correction</summary>

La fréquence vaut $f=4/2=2$ Hz. La période vaut $T=1/2=0{,}5$ s. Le contrôle donne bien $4\times0{,}5=2$ secondes.

Le sinus et le cosinus classiques ont une période de $2\pi$ radians. Le cosinus est le sinus décalé de $\pi/2$ vers la gauche, soit un quart de période.

</details>

---

## Exercice 2 — Calculer une période et une fréquence

Le temps $t$ est exprimé en secondes. Pour chaque signal, identifier la pulsation, puis calculer la période et la fréquence avec leurs unités.

$$
a(t)=\sin(3t),\qquad b(t)=\cos\left(\frac t4\right),\qquad
c(t)=\sin(-2\pi t).
$$

<details><summary>Indice</summary>

Dans $b(t)$, la pulsation vaut $1/4$ rad/s. Utiliser la valeur absolue de la pulsation dans les formules de période et de fréquence.

</details>

<details><summary>Afficher la correction</summary>

| Signal | Pulsation en rad/s | Période en s | Fréquence en Hz |
|---|---:|---:|---:|
| $a(t)$ | $3$ | $2\pi/3$ | $3/(2\pi)$ |
| $b(t)$ | $1/4$ | $8\pi$ | $1/(8\pi)$ |
| $c(t)$ | $-2\pi$ | $1$ | $1$ |

Pour le dernier signal, la valeur absolue de la pulsation vaut $2\pi$. La période est positive et vaut une seconde.

</details>

---

## Exercice 3 — Changer le rythme quotidien

On conserve le niveau central de 10 °C et l'amplitude de 5 °C du signal de température.

1. Écrire une formule dont la période serait de 12 h.
2. Combien de cycles les modèles de périodes 24 h et 12 h réalisent-ils sur 48 h ?
3. Un étudiant annonce « période de 12 h, donc fréquence de 12 Hz ». Corriger son calcul en explicitant les unités.

<details><summary>Indice</summary>

Écrire la pulsation sous la forme $2\pi/P$, avec $P$ en heures. Pour compter les cycles, diviser la durée d'observation par la période.

</details>

<details><summary>Afficher la correction</summary>

La formule devient $10+5\sin((2\pi/12)t)$, avec $t$ en heures. Sur 48 h, le premier modèle réalise $48/24=2$ cycles et le second $48/12=4$ cycles.

Pour une période de 12 h, la fréquence vaut $1/12$ cycle/h. En secondes, $12\text{ h}=43\,200\text{ s}$, donc $f=1/43\,200$ Hz. La fréquence double lorsque la période passe de 24 h à 12 h.

</details>

---

## Questions de révision

1. Comment reconnaître un cycle complet sur une courbe ?
2. Quelle est la période fondamentale du sinus et du cosinus usuels ?
3. Dans quelles unités s'exprime une fréquence lorsque le temps est en heures ?
4. Quel effet produit le passage de $\sin(x)$ à $\sin(4x)$ ?
5. Pourquoi utilise-t-on la valeur absolue de la pulsation ?

---

## QCM — Questions 1 à 3

**1. La période fondamentale de $\cos x$, pour $x$ en radians, vaut**

A. $\pi/2$ · B. $\pi$ · C. $2\pi$ · D. $4\pi$.

**2. Une période de 0,2 s correspond à une fréquence de**

A. 0,2 Hz · B. 2 Hz · C. 5 Hz · D. 20 Hz.

**3. La période de $\sin(4x)$ vaut**

A. $8\pi$ · B. $2\pi$ · C. $\pi$ · D. $\pi/2$.

<details><summary>Afficher la correction</summary>

1. **C**. La courbe du cosinus se reproduit après un angle de $2\pi$.
2. **C**. On calcule $f=1/0{,}2=5$ Hz.
3. **D**. On calcule $T=2\pi/4=\pi/2$.

</details>

---

## QCM — Questions 4 et 5

**4. Un phénomène sinusoïdal possède une période de 24 heures. Si on multiplie sa pulsation par 2, quelle sera sa nouvelle période ?**

A. 48 heures · B. 24 heures · C. 12 heures · D. 6 heures.

**5. De façon générale, pour $y(t)=\sin(\omega t)$, si la valeur absolue de la pulsation est multipliée par 2, la période**

A. double · B. reste la même · C. est divisée par deux · D. devient négative.

<details><summary>Afficher la correction</summary>

4. **C**. La période est inversement proportionnelle à la valeur absolue de la pulsation : $T=2\pi/|\omega|$. La doubler divise la période par deux : $24/2=12$ heures.
5. **C**. Plus généralement, si $|\omega|$ devient $2|\omega|$, alors $T'=2\pi/(2|\omega|)=T/2$. La fréquence double.

</details>

---

## Fiche de révision

- Le sinus et le cosinus usuels se répètent tous les $2\pi$ radians.
- La période est la longueur ou la durée d'un cycle complet.
- La fréquence compte les cycles par unité de temps et vérifie $f=1/T$.
- Pour $\sin(\omega t)$ et $\cos(\omega t)$, avec $\omega\ne0$, $T=2\pi/|\omega|$ et $f=|\omega|/(2\pi)$.
- Les unités de la variable déterminent celles de la période et de la fréquence.

[Continuer avec la dérivation](01_derivation.md).
