---
marp: true
theme: default
paginate: true
class: lead
---

# Dérivation

## 1. Définition intuitive de la dérivée

La dérivée d'une fonction (f) en un point (x) mesure **la pente de la courbe** de (f) à ce point.
On l'interprète comme la vitesse de variation :

$$
f'(x) = \text{pente de la tangente au point } x.
$$

Si :

1. (f'(x) > 0) : la fonction **augmente** (pente positive).
1. (f'(x) < 0) : la fonction **diminue** (pente négative).
1. (f'(x) = 0) : la courbe a une **tangente horizontale** (candidats aux extremums).

---

## Lire une tangente et sa pente

![À gauche, f(x)=x carré et sa tangente en x=1 ; à droite, la dérivée 2x. La valeur en 1 vaut 1 et la pente vaut 2.](figures/derivee-tangente.svg)

La valeur de la fonction et la valeur de sa dérivée ne désignent pas la même quantité.

---

## 2. Fonction dérivable

Une fonction est dérivable sur un intervalle si sa pente existe en tout point.
Notation :

$$
f : I \to \mathbb{R}, \quad f'(x) \text{ existe pour tout } x \in I.
$$

---

# 3. Règles de dérivation

### 3.1. Dérivées usuelles

$$
(x^n)' = nx^{n-1}
$$

$$
(\sqrt{x})' = \frac{1}{2\sqrt{x}}
$$

$$
(e^x)' = e^x
$$

$$
(\ln(x))' = \frac{1}{x}
$$

### Fonctions trigonométriques

Le chapitre [Fonctions périodiques](fonctions_periodiques.md) présente les courbes du sinus et du cosinus ainsi que les notions de période et de fréquence.

$$
(\sin x)' = \cos x
$$

$$
(\cos x)' = -\sin x
$$

---

### 3.2. Règles de calcul

1. **Somme**

$$
(f+g)' = f' + g'
$$

2. **Produit**

$$
(fg)' = f'g + fg'
$$

3. **Quotient**

$$
\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2} \qquad (g \neq 0)
$$

4. **Composition** (chaîne)

$$
f(g(x))' = f'(g(x)) \cdot g'(x)
$$

---

# 4. Dérivée et sens de variation

Pour étudier une fonction, on :

1. calcule sa dérivée (f'),
2. étudie le signe de (f'),
3. remplit un tableau de variation.

Règle fondamentale :

1. (f'(x) > 0) : (f) **croît**,
1. (f'(x) < 0) : (f) **décroît**,
1. (f'(x) = 0) : points critiques (minima, maxima possibles).

---

# 5. Dérivée seconde et courbure (rappel utile)

La dérivée seconde est la dérivée de la dérivée :

$$
f''(x) = (f'(x))'.
$$

Elle indique la **courbure** :

1. (f''(x) > 0) : la courbe est **convexe** (pente augmente),
1. (f''(x) < 0) : la courbe est **concave** (pente diminue).

---

# 6. Exemples corrigés

## Exemple 1 : Extrema locaux

Étudions $f(x)=x^3-3x$, définie sur $\mathbb{R}$.

$$
f'(x)=3x^2-3=3(x-1)(x+1).
$$

La dérivée s'annule en $-1$ et $1$. Elle est positive pour $x<-1$ et $x>1$, négative pour $-1<x<1$.

- En $x=-1$, le signe passe de $+$ à $-$ : **maximum local**, de valeur $f(-1)=2$.
- En $x=1$, le signe passe de $-$ à $+$ : **minimum local**, de valeur $f(1)=-2$.

« Local » signifie que l'on compare aux points voisins. Cette cubique n'a pas de maximum ni de minimum global sur $\mathbb{R}$ : ses limites sont $-\infty$ et $+\infty$.

---

## Exemple 1 — Lire la correction sur les courbes

![À gauche, x cube moins 3x : maximum local en (-1,2) et minimum local en (1,-2). À droite, sa dérivée, négative entre -1 et 1 et positive ailleurs.](images/fonctions-extrema.svg)

À gauche, on lit les **valeurs** de $f$. À droite, on lit les **pentes**. Une dérivée nulle est un candidat ; le changement de signe permet ici de conclure.

---

## Exemple 2 : Fonction avec quotient

$$f(x)=\frac{x^2-1}{x}=x-\frac1x,\qquad x\in\mathbb{R}\setminus\{0\}.$$

$$
f'(x)=\frac{2x^2 - (x^2 - 1)}{x^2} = \frac{x^2 + 1}{x^2}.
$$

Comme $$x^2+1>0$$, on obtient :

$$
f'(x) > 0 \quad \text{pour tout } x\neq 0.
$$

La fonction est **strictement croissante** sur chacun des intervalles $]-\infty,0[$ et $]0,+\infty[$. On ne traverse pas le point interdit 0.

![Deux branches séparées en zéro pour x moins 1 sur x ; la dérivée 1 plus 1 sur x carré reste positive sur chaque intervalle.](images/fonctions-quotient.svg)

---

## Exemple 3 : Composition

$$f(x) = e^{3x}$$

$$
f'(x) = 3 e^{3x}.
$$

La dérivée est toujours positive : la fonction est strictement croissante sur $\mathbb{R}$. En 0, $f(0)=1$ mais $f'(0)=3$ : valeur et pente sont différentes.

![Exponentielle exp(3x), tangente de pente 3 en zéro, et dérivée 3 exp(3x) positive.](images/fonctions-composition.svg)

---

# 7. Exercices d'entraînement

## Exercice 1

Dériver :

a) 

$$
f(x)=x^4 - 2x^2 + 1
$$

b) 

$$
g(x)=\sqrt{x}(x^2+3)
$$

c) 

$$
h(x)=\frac{3x+1}{x-2}
$$

---

## Exercice 2

Étudier les variations de :

a) 

$$
f(x)=x^3+3x^2
$$

b) 

$$
g(x)=\ln(x) - x
$$

c) 

$$
h(x)=e^{-x}
$$

---

## Exercice 3

Trouver les maxima/minima de :

a) 

$$
f(x)=x^2 - 4x +1
$$

b) 

$$
g(x)=x + \frac{1}{x}
$$

Cette fonction n'est pas définie en 0.

c) 

$$
h(x)=\sin x + x
$$

<details><summary>Afficher la correction et les graphiques</summary>

**a)** $f(x)=(x-2)^2-3$ et $f'(x)=2x-4$. La dérivée passe de négative à positive en 2. Le **minimum global** vaut $-3$, atteint en 2 ; aucun maximum sur $\mathbb{R}$.

**b)** $g'(x)=1-1/x^2=(x^2-1)/x^2$. Sur $]-\infty,-1[$, le signe est positif, puis négatif sur $]-1,0[$ : **maximum local** $g(-1)=-2$. Sur $]0,1[$, le signe est négatif, puis positif sur $]1,+\infty[$ : **minimum local** $g(1)=2$. Aucun extremum global sur tout $\mathbb{R}\setminus\{0\}$ : la fonction y est non bornée dans les deux sens.

**c)** $h'(x)=1+\cos x\geq0$. Les zéros $x=(2k+1)\pi$, $k\in\mathbb{Z}$, sont isolés et la dérivée reste positive entre eux. La fonction est strictement croissante : **aucun extremum**, malgré ces tangentes horizontales.

![Une parabole avec minimum global, x plus 1 sur x avec deux extrema locaux, et sinus de x plus x avec tangente horizontale sans extremum.](images/fonctions-exercice-extremums.svg)

Un dessin aide à interpréter le calcul. Sa fenêtre finie ne suffit pas à démontrer un extremum global.

</details>

---

## Exercice 4

Étudier la convexité de :

a) 

$$
f(x)=x^4
$$

b) 

$$
g(x)=x e^x
$$

c) 

$$
h(x)=\ln(x)
$$

---

## Exercice 5 — Simuler une température

Préparez l'environnement Python des TP avec NumPy, Pandas, Matplotlib et FastAPI : [installation](https://github.com/Antoine07/maths/blob/main/installation.md). Le calcul ci-dessous utilise seulement NumPy ; l'API sera construite dans le TP suivant.

Testez ce programme complet. `t` contient 48 instants, de 0 h à 47 h ; l'unité du temps est l'heure et les températures sont exprimées en °C.

```python
import numpy as np

t = np.arange(0., 48., 1.)
np.random.seed(7)  # Reproduire les mêmes tirages pour comparer les essais.
noise = np.random.normal(loc=0.0, scale=0.5, size=t.size)
T_raw = 10 + 5 * np.sin((2*np.pi/24)*t) + noise
```

**Travail attendu :** un graphique légendé et des réponses justifiées. Distinguez le signal sans bruit, le bruit et la série obtenue.

---

## Exercice 5 — Questions à explorer

1. Que représentent `t`, `t.size`, `loc`, `noise` et `T_raw` ? Quels sont leurs types ou leurs dimensions ?
2. Pourquoi utilise-t-on $2\pi/24$ dans le sinus ? Reliez **période**, **fréquence** et angle en radians. Que se passe-t-il si l'on remplace 24 par 12 ?
3. Que représentent 10 et 5 ? Le changement de période les modifie-t-il ? Comparez les deux signaux sans bruit sur 48 h, puis utilisez **le même bruit** pour comparer les séries bruitées.
4. Pourquoi `scale=0.5` est-il l'**écart-type** du bruit et non sa variance ? Donnez les deux valeurs théoriques, avec leurs unités. `noise.std()` est-il nécessairement égal à 0,5 sur 48 tirages ?
5. Le bruit est-il toujours entre -0,5 et 0,5 ? La série bruitée reste-t-elle nécessairement entre 5 et 15 °C ?
6. Quelles hypothèses simplifient la température réelle ? Cette simulation constitue-t-elle déjà une prédiction météo ?

**Indice :** un sinus retrouve sa valeur après une augmentation de $2\pi$ de son argument. Pour les statistiques, séparez les paramètres de la loi et les valeurs observées sur un échantillon.

---

## Exercice 5 — Correction expliquée

<details><summary>Afficher la correction et le graphique</summary>

**Lecture du code.** `t`, `noise` et `T_raw` sont des tableaux NumPy de forme `(48,)`. `t.size` vaut 48. `loc=0.0` fixe la moyenne théorique du bruit à 0 ; chaque mesure reçoit un tirage gaussien. La graine rend l'expérience reproductible.

**Période et fréquence.** Pour une période $P$ en heures, la fréquence vaut $\nu=1/P$ cycle/h et la pulsation $\omega=2\pi/P$ rad/h. Ainsi, $\omega(t+P)=\omega t+2\pi$ : le signal se répète après $P$ heures. Avec 24, il accomplit deux cycles en 48 h ; avec 12, quatre cycles. La période est divisée par deux et la fréquence est doublée. [NumPy : sinus et radians](https://numpy.org/doc/stable/reference/generated/numpy.sin.html).

**Niveau et amplitude.** 10 °C est le niveau central du signal idéal et 5 °C son amplitude. Sans bruit, il oscille entre 5 et 15 °C, quelle que soit la période. Le bruit de moyenne théorique nulle préserve ce signal en espérance, mais sa moyenne observée n'est pas exactement nulle.

**Dispersion.** L'API `np.random.normal` définit `scale` comme l'écart-type $\sigma$, ici 0,5 °C. La variance vaut donc $\sigma^2=0{,}25$ °C². Si l'on voulait une **variance de 0,5 °C²**, on utiliserait `scale=np.sqrt(0.5)`. [NumPy : paramètres de la loi normale](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html).

Sur 48 tirages, `noise.std()` et `noise.var()` donnent des statistiques descriptives de l'échantillon, généralement différentes des paramètres théoriques. Le bruit gaussien n'est pas borné par $\pm\sigma$ : des écarts plus grands sont possibles. La température bruitée peut donc sortir de [5,15].

![Comparaison de périodes 24 et 12 heures, observations simulées sur 48 heures et bruit avec écart-type 0,5 degré, soit une variance de 0,25 degré carré.](images/fonctions-temperature.svg)

**À reproduire :** [script Python de comparaison](../docs/exemples/fonctions/temperature_simulee.py). Il utilise un générateur local pour retrouver les mêmes tirages sans modifier les autres expériences.

**Limites scientifiques.** Il s'agit d'un **modèle simplifié** : le sinus représente une variation quotidienne idéale et le bruit gaussien simule des fluctuations aléatoires. Le cycle thermique réel n'est pas parfaitement sinusoïdal ; les fluctuations peuvent aussi dépendre des heures précédentes. La formule donnée culmine à 6 h (modulo 24), ce qui ne représente pas automatiquement une journée météo réelle. Un décalage $t-8$ déplacerait ce maximum à 14 h, sans changer la période.

**Vers la data et l'IA.** Ces données constituent une série temporelle simulée. Simuler consiste à produire des observations selon une règle choisie ; prédire consiste à estimer des valeurs inconnues. Pour une future prévision, conserver l'ordre chronologique apprentissage/validation/test et comparer le modèle à une référence saisonnière. Un bon résultat sur cette simulation ne suffit pas à valider un modèle météo réel.

</details>

---

## Problème — Un rythme et son cumul

Un groupe se retrouve aujourd'hui deux fois par mois. Peut-on simplement multiplier cette fréquence par 30 ans ?

Comparer une fréquence constante à une fréquence décroissante et vérifier le cumul en le dérivant. Le problème introduit la relation entre une fréquence et son cumul.

[Problème 2 : et si les occasions devenaient moins fréquentes ?](../Tps/Tail_End/02_frequence.md)

---

## TP optimisation 

[TP Optimisation](https://github.com/Antoine07/maths/blob/main/Derivation/TPs/00_TP_optimisation.md)

---

## [Retour au plan](https://antoine07.github.io/maths/)
