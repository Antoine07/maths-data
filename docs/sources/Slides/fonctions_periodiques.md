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

## Pourquoi ces fonctions en IA ?

L'heure est cyclique : 23 h est proche de 0 h, même si les nombres 23 et 0 semblent éloignés. On peut encoder une heure $h$ par deux coordonnées sur le cercle :

$$
\left(\cos\left(\frac{2\pi h}{24}\right),\;\sin\left(\frac{2\pi h}{24}\right)\right).
$$

Un modèle peut ainsi apprendre les régularités liées à l'heure pour prévoir une série temporelle, comme la consommation électrique. Le codage représente le cycle des heures ; il ne suppose pas que la consommation soit elle-même sinusoïdale.

![Les heures 23 h et 0 h sont voisines sur un cercle ; leur encodage sinus-cosinus rend visible cette proximité.](images/fonctions-ia-cyclique.svg)

### Animation — passer minuit

Déplacez le curseur ou lancez le parcours : l'heure avance sur le cercle, et ses deux coordonnées sinus-cosinus s'actualisent. Le passage de 23 h à 0 h est continu.

<div class="interactive-math-demo" data-clock-demo>
  <div class="interactive-demo-controls clock-controls">
    <label>Heure <output data-clock-hour-label>23 h</output>
      <input data-clock-hour type="range" min="0" max="24" step="0.25" value="23" aria-label="Heure de la journée">
    </label>
    <div class="interactive-demo-buttons">
      <button class="button primary" type="button" data-clock-toggle aria-pressed="false">▶ Faire avancer l'heure</button>
      <button class="button" type="button" data-clock-reset>Replacer à 23 h</button>
    </div>
  </div>
  <p class="interactive-demo-readout" data-clock-readout aria-live="polite">Encodage : (0,966 ; −0,259) · distance à minuit : 0,261</p>
  <svg class="interactive-demo-svg clock-demo-svg" viewBox="0 0 1000 330" role="img" aria-label="Une horloge circulaire avec un point mobile, et les coordonnées cosinus et sinus de l'heure.">
    <text x="230" y="34" text-anchor="middle" class="demo-title">Heure sur un cercle de 24 h</text>
    <circle cx="230" cy="170" r="112" class="demo-circle"/>
    <line x1="106" y1="170" x2="354" y2="170" class="demo-axis"/>
    <line x1="230" y1="46" x2="230" y2="294" class="demo-axis"/>
    <text x="350" y="176" text-anchor="middle" class="demo-caption">0 h</text>
    <text x="230" y="52" text-anchor="middle" class="demo-caption">6 h</text>
    <text x="110" y="176" text-anchor="middle" class="demo-caption">12 h</text>
    <text x="230" y="310" text-anchor="middle" class="demo-caption">18 h</text>
    <line x1="230" y1="170" x2="340" y2="140" class="demo-hand" data-clock-hand/>
    <circle cx="340" cy="140" r="9" class="demo-point" data-clock-point/>
    <text x="610" y="115" class="demo-title">Coordonnées données au modèle</text>
    <text x="610" y="170" class="demo-equation">cos(2πh / 24) = <tspan data-clock-cos>0,966</tspan></text>
    <text x="610" y="220" class="demo-equation">sin(2πh / 24) = <tspan data-clock-sin>−0,259</tspan></text>
    <text x="610" y="274" class="demo-caption">À minuit, l'encodage revient près de celui de 23 h.</text>
  </svg>
</div>

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
