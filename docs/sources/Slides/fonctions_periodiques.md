---
marp: true
html: true
paginate: true
---

# Fonctions périodiques

Un cycle, une période, un rythme : sinus et cosinus servent à décrire des phénomènes qui se répètent.

![Courbes du sinus et du cosinus : un cycle complet se répète tous les 2 pi radians.](images/fonctions-sinus-cosinus.svg)

---

## Un cycle qui se répète

Une fonction est **périodique** lorsqu'elle reprend les mêmes valeurs après un intervalle fixe $T$ :

$$
h(t+T)=h(t).
$$

Cet intervalle est la **période**. Sur un graphique, on la lit entre deux points identiques consécutifs, par exemple deux maxima.

Le sinus et le cosinus ont chacun une période fondamentale de $2\pi$ radians :

$$
\sin(t+2\pi)=\sin(t),\qquad \cos(t+2\pi)=\cos(t).
$$

Ils décrivent le même cycle, décalé d'un quart de tour : $\cos(t)=\sin(t+\pi/2)$.

![Un cycle complet du sinus et du cosinus, de 0 à 2 pi radians.](images/fonctions-sinus-cosinus.svg)

---

## Période et fréquence

La **période** $T$ est la durée d'un cycle. La **fréquence** $f$ compte le nombre de cycles par unité de temps :

$$
\boxed{f=\frac1T}\qquad\text{et}\qquad\boxed{T=\frac1f}.
$$

Si un cycle dure 2 secondes, $T=2\,\mathrm{s}$ et $f=0{,}5\,\mathrm{Hz}$. Si un cycle dure 24 heures, $f=1/24$ cycle par heure. On parle en hertz seulement quand le temps est exprimé en secondes.

Une période plus courte correspond à une fréquence plus grande : le phénomène recommence plus souvent.

![Comparaison de sinusoïdes de périodes différentes sur les mêmes axes.](images/fonctions-periodes.svg)

---

## Pulsation et phase

Un signal sinusoïdal s'écrit :

$$
y(t)=\sin(\omega t+\varphi_0).
$$

La **phase** est l'angle $\varphi(t)=\omega t+\varphi_0$ : c'est la position de l'aiguille sur le cercle. La **pulsation** $\omega$ indique à quelle vitesse l'aiguille tourne. $\varphi_0$ donne sa position au départ.

Un cycle correspond à un tour de $2\pi$ radians. Si $\omega\ne0$ :

$$
\boxed{T=\frac{2\pi}{|\omega|}},\qquad
\boxed{f=\frac{|\omega|}{2\pi}}.
$$

![La phase est l'angle de l'aiguille ; la pulsation est sa vitesse de rotation.](images/fonctions-phase-pulsation.svg)

---

## Pourquoi ces fonctions en IA ?

L'heure est cyclique : 23 h est proche de 0 h, même si les nombres 23 et 0 semblent éloignés. On peut encoder une heure $h$ par deux coordonnées sur le cercle :

$$
\left(\cos\left(\frac{2\pi h}{24}\right),\;\sin\left(\frac{2\pi h}{24}\right)\right).
$$

Un modèle peut ainsi apprendre les régularités liées à l'heure pour prévoir une série temporelle, comme la consommation électrique. Le codage représente le cycle des heures ; il ne suppose pas que la consommation soit elle-même sinusoïdale.

![Les heures 23 h et 0 h sont voisines sur un cercle ; leur encodage sinus-cosinus rend visible cette proximité.](images/fonctions-ia-cyclique.svg)

---

## TP — Comparer deux rythmes quotidiens

Exécutez le code, puis répondez aux questions.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 48, 481)  # temps en heures

signal_24h = 10 + 5 * np.sin((2 * np.pi / 24) * t)
signal_12h = 10 + 5 * np.sin((2 * np.pi / 12) * t)

plt.plot(t, signal_24h, label="Période : 24 h")
plt.plot(t, signal_12h, label="Période : 12 h")
plt.xlabel("Temps (heures)")
plt.ylabel("Valeur du signal")
plt.title("Deux rythmes sinusoïdaux")
plt.grid(alpha=0.3)
plt.legend()
plt.show()

heures = np.array([23, 0])
angle = 2 * np.pi * heures / 24
encodage = np.column_stack((np.cos(angle), np.sin(angle)))
print("Encodage de 23 h et 0 h :", encodage)
print("Distance entre les deux encodages :",
      np.linalg.norm(encodage[0] - encodage[1]))
```

1. Quelle est la période de chaque signal ? Combien de cycles chacun réalise-t-il en 48 h ?
2. Pourquoi le coefficient $2\pi/24$ donne-t-il un cycle en 24 h ? Que se passe-t-il quand on remplace 24 par 12 ?
3. Les heures 23 et 0 sont-elles proches dans l'encodage ? Expliquez pourquoi cette représentation convient à une heure de la journée.

<details><summary>Afficher une correction possible</summary>

Le premier signal a pour période 24 h et réalise deux cycles en 48 h. Le second a pour période 12 h et réalise quatre cycles. Dans $\sin((2\pi/P)t)$, le coefficient $2\pi/P$ fait avancer l'angle de $2\pi$ lorsque $t$ augmente de $P$ heures : remplacer 24 par 12 divise la période par deux.

Les angles associés à 23 h et 0 h ne diffèrent que d'un douzième de tour, donc leurs encodages sont voisins. Leur distance vaut environ $0{,}26$, alors que les valeurs brutes 23 et 0 paraissent éloignées.

</details>
