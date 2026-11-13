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

### Animation — suivre la phase

Modifiez la période ou la phase initiale, puis lancez l'animation. L'aiguille tourne sur le cercle ; le point correspondant parcourt la sinusoïde.

<div class="interactive-math-demo" data-wave-demo>
  <div class="interactive-demo-controls">
    <label>Période <output data-wave-period-label>24 h</output>
      <input data-wave-period type="range" min="6" max="24" step="1" value="24" aria-label="Période du signal, en heures">
    </label>
    <label>Phase initiale <output data-wave-phase-label>0°</output>
      <input data-wave-phase type="range" min="-180" max="180" step="15" value="0" aria-label="Phase initiale, en degrés">
    </label>
    <div class="interactive-demo-buttons">
      <button class="button primary" type="button" data-wave-toggle aria-pressed="false">▶ Démarrer</button>
      <button class="button" type="button" data-wave-reset>Repartir de t = 0</button>
    </div>
  </div>
  <p class="interactive-demo-readout" data-wave-readout aria-live="polite">Temps : 0 h · phase : 0° · sinusoïde : 0,00</p>
  <svg class="interactive-demo-svg" viewBox="0 0 1000 320" role="img" aria-label="À gauche, une aiguille tourne sur le cercle. À droite, le point correspondant se déplace sur la courbe du sinus.">
    <text x="125" y="36" text-anchor="middle" class="demo-title">Position sur le cercle</text>
    <circle cx="125" cy="166" r="78" class="demo-circle"/>
    <line x1="42" y1="166" x2="208" y2="166" class="demo-axis"/>
    <line x1="125" y1="83" x2="125" y2="249" class="demo-axis"/>
    <line x1="125" y1="166" x2="203" y2="166" class="demo-hand" data-wave-hand/>
    <circle cx="203" cy="166" r="7" class="demo-point" data-wave-circle-point/>
    <text x="125" y="276" text-anchor="middle" class="demo-caption">La phase donne l'angle de l'aiguille.</text>
    <text x="610" y="36" text-anchor="middle" class="demo-title">Valeur du sinus entre 0 h et 48 h</text>
    <line x1="270" y1="166" x2="950" y2="166" class="demo-axis"/>
    <line x1="270" y1="70" x2="270" y2="262" class="demo-axis"/>
    <path d="M270 166H950" class="demo-grid"/>
    <path d="M270 86H950M270 246H950" class="demo-grid"/>
    <path d="" class="demo-wave" data-wave-path/>
    <line x1="270" y1="86" x2="270" y2="246" class="demo-cursor" data-wave-cursor/>
    <circle cx="270" cy="166" r="7" class="demo-point" data-wave-graph-point/>
    <text x="270" y="292" text-anchor="middle" class="demo-caption">0 h</text>
    <text x="610" y="292" text-anchor="middle" class="demo-caption">24 h</text>
    <text x="950" y="292" text-anchor="middle" class="demo-caption">48 h</text>
  </svg>
</div>

---

## Application · Coder l'heure dans une série de données

Une heure se répète toutes les 24 heures. Les valeurs brutes créent pourtant une fausse distance : $|23-0|=23$, alors que 23 h et minuit sont séparés d'une heure.

On place l'heure $h$ sur un cercle. Un tour complet vaut $2\pi$ radians, donc l'angle associé est :

$$
\theta=\frac{2\pi h}{24}.
$$

Le cosinus et le sinus donnent les deux coordonnées du point :

$$
\left(\cos\theta,\;\sin\theta\right).
$$

| Heure | Encodage $(\cos\theta,\sin\theta)$ |
|---:|---:|
| 0 h | $(1,0)$ |
| 6 h | $(0,1)$ |
| 12 h | $(-1,0)$ |
| 18 h | $(0,-1)$ |
| 23 h | $(0{,}966,-0{,}259)$ |

![Sur le cercle, les encodages de 23 h et de 0 h sont voisins.](images/fonctions-ia-cyclique.svg)

Cette représentation, appelée **encodage cyclique**, aide un modèle à exploiter l'heure pour prévoir une série temporelle, par exemple la consommation électrique. Elle ne suppose pas que la consommation suive elle-même un sinus. On utilise les deux coordonnées, car le cosinus seul ne distingue pas 6 h et 18 h.

---

## Petit exercice · Comparer deux heures

On donne :

```python
import numpy as np

heures = np.array([0, 6, 18, 23])
angle = 2 * np.pi * heures / 24
encodage = np.column_stack((np.cos(angle), np.sin(angle)))
```

1. Donner l'encodage de 6 h et de 18 h. Pourquoi le cosinus seul ne suffit-il pas ?
2. Les encodages de 23 h et de 0 h sont-ils proches ? Justifier à l'aide du tableau.

<details><summary>Afficher une correction possible</summary>

À 6 h, $\theta=\pi/2$ et l'encodage vaut $(0,1)$. À 18 h, $\theta=3\pi/2$ et il vaut $(0,-1)$. Le cosinus vaut 0 dans les deux cas ; le sinus permet de distinguer ces heures.

À 23 h, l'encodage est environ $(0{,}966,-0{,}259)$, proche de $(1,0)$ à 0 h. Le changement de 23 h à minuit est donc continu sur le cercle.

</details>
