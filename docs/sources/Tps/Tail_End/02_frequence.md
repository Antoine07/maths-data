# Problème 2 — Et si les occasions devenaient moins fréquentes ?

## Objectif et prérequis

**Objectif pédagogique :** distinguer une fréquence et un cumul, relier leurs variations et tester une extrapolation.

**Prérequis :** [dérivation](../../Slides/01_derivation.md), exponentielle, logarithme et dérivée d'une fonction composée.

Les notions nécessaires sur le cumul sont introduites ci-dessous.

---

## Activité d'introduction — Additionner une fréquence

Avant d'aborder le scénario de Sam, cette activité montre comment un rythme produit un cumul.

Un compteur suit les visiteurs pendant deux heures. On compare deux scénarios.

- **Scénario A :** le rythme est constant à 2 visiteurs par heure pendant la première heure, puis à 4 visiteurs par heure pendant la deuxième heure.
- **Scénario B :** le rythme augmente continûment selon $f(t)=2t$ visiteurs par heure, où $t$ est le temps écoulé en heures.

Pour le scénario B, on garde la même idée : **la hauteur de la courbe indique le rythme à cet instant ; l'aire sous la courbe indique le cumul depuis le départ.**

<div class="interactive-math-demo" data-cumulative-demo>
  <div class="interactive-demo-controls cumul-controls">
    <label>Temps écoulé <output data-cumul-time-label>0,00 h</output>
      <input data-cumul-time type="range" min="0" max="2" step="0.01" value="0" aria-label="Temps écoulé, de zéro à deux heures">
    </label>
    <div class="interactive-demo-buttons">
      <button class="button primary" type="button" data-cumul-toggle aria-pressed="false">▶ Animer</button>
      <button class="button" type="button" data-cumul-reset>Repartir de 0 h</button>
    </div>
  </div>
  <p class="interactive-demo-readout" data-cumul-readout aria-live="polite">À 0 h : rythme de 0 visiteurs/h ; cumul de 0 visiteurs.</p>
  <svg class="interactive-demo-svg cumul-demo-svg" viewBox="0 0 1000 380" role="img" aria-label="La droite du rythme f(t)=2t et le triangle coloré représentant le cumul jusqu'au temps choisi.">
    <text x="500" y="28" text-anchor="middle" class="demo-title">Rythme instantané et cumul par l'aire</text>
    <line x1="120" y1="300" x2="900" y2="300" class="demo-axis"/>
    <line x1="120" y1="300" x2="120" y2="60" class="demo-axis"/>
    <path d="M120 240H900M120 180H900M120 120H900M120 60H900M315 60V300M510 60V300M705 60V300M900 60V300" class="demo-grid"/>
    <text x="105" y="304" text-anchor="end" class="demo-caption">0</text>
    <text x="105" y="244" text-anchor="end" class="demo-caption">1</text>
    <text x="105" y="184" text-anchor="end" class="demo-caption">2</text>
    <text x="105" y="124" text-anchor="end" class="demo-caption">3</text>
    <text x="105" y="64" text-anchor="end" class="demo-caption">4</text>
    <text x="120" y="324" text-anchor="middle" class="demo-caption">0</text>
    <text x="315" y="324" text-anchor="middle" class="demo-caption">0,5</text>
    <text x="510" y="324" text-anchor="middle" class="demo-caption">1</text>
    <text x="705" y="324" text-anchor="middle" class="demo-caption">1,5</text>
    <text x="900" y="324" text-anchor="middle" class="demo-caption">2 h</text>
    <text x="30" y="75" class="demo-caption">Visiteurs/h</text>
    <text x="510" y="354" text-anchor="middle" class="demo-caption">Temps écoulé</text>
    <path d="M120 300L900 60" class="demo-wave"/>
    <path d="M120 300L510 300L510 180Z" class="cumul-area" data-cumul-area/>
    <line x1="510" y1="300" x2="510" y2="180" class="demo-cursor" data-cumul-cursor/>
    <circle cx="510" cy="180" r="8" class="demo-point" data-cumul-point/>
    <text x="680" y="92" class="demo-caption">Hauteur = rythme f(t)=2t</text>
    <text x="675" y="274" class="demo-caption">Aire colorée = cumul C(t)=t²</text>
  </svg>
</div>

Quelques valeurs permettent de vérifier la lecture de l'animation :

| Temps écoulé | Rythme à cet instant | Cumul depuis le départ |
|---|---:|---:|
| 0 h 30 | 1 visiteur/h | 0,25 visiteur |
| 1 h | 2 visiteurs/h | **1 visiteur** |
| 1 h 30 | 3 visiteurs/h | 2,25 visiteurs |
| 2 h | 4 visiteurs/h | **4 visiteurs** |

1. Pour le scénario A, calculer le nombre total de visiteurs sur les deux heures. Représenter le rythme sur un graphique et repérer les aires qui correspondent aux deux périodes.
2. Pour le scénario B, arrêtez l'animation à 1 h puis à 2 h. À chaque fois, distinguez la hauteur (le rythme) de l'aire colorée (le cumul). Vérifiez les valeurs avec le tableau.
3. Les deux scénarios ont-ils le même rythme au cours du temps ? Pourquoi leurs cumuls sont-ils différents ?
4. Si le rythme reste constant à 2 visiteurs par heure pendant 3 heures, combien de visiteurs sont comptés ?
5. Pour chaque scénario, calculer le rythme moyen sur les deux heures. En supposant ce rythme moyen constant, écrire le cumul linéaire correspondant. Comparer cette droite au cumul réel à $t=1$ h et à $t=2$ h.

![En haut, les deux rythmes et les aires sous leurs courbes. En bas, les cumuls exacts et les droites obtenues en appliquant le rythme moyen pendant deux heures. Les droites moyennes atteignent le même total final que leur scénario, mais ne décrivent pas la même répartition dans le temps.](../../Slides/figures/tail-02-cumul-intro.svg)

<details><summary>Afficher la correction</summary>

Dans le scénario A, chaque palier forme un rectangle : $2\times1=2$ visiteurs, puis $4\times1=4$. Le cumul est donc $2+4=6$ visiteurs.

Dans le scénario B, la courbe est une droite qui part de 0 et atteint 4 visiteurs par heure à $t=2$. L'aire sous la droite est un triangle de base 2 heures et de hauteur 4 visiteurs par heure :

$$
\frac{2\times4}{2}=4\text{ visiteurs}.
$$

À 1 h, le triangle a une largeur de 1 h et une hauteur de 2 visiteurs/h : son aire vaut $1\times2\div2=1$ visiteur. À 2 h, sa largeur vaut 2 h et sa hauteur 4 visiteurs/h : son aire vaut $2\times4\div2=4$ visiteurs. Le 4 visiteurs/h se lit au sommet ; les 4 visiteurs cumulés correspondent à toute l'aire du triangle.

Cela explique le carré : quand le temps double, la largeur et la hauteur doublent toutes les deux, donc l'aire est multipliée par quatre. En général, jusqu'au temps $t$, $C(t)=\frac{t\times2t}{2}=t^2$ visiteurs.

Les scénarios n'ont pas le même rythme : le premier change brusquement à une heure, tandis que le second augmente continûment. Leurs aires, donc leurs cumuls, diffèrent. Un rythme constant de 2 visiteurs par heure pendant 3 heures donne $2\times3=6$ visiteurs.

Dans le scénario A, le rythme moyen est $(2+4)/2=3$ visiteurs par heure. Le cumul linéaire associé est $C_{A,\mathrm{moy}}(t)=3t$. Il donne 3 visiteurs à $t=1$ h, alors que le cumul par paliers en donne 2. À $t=2$ h, les deux valent 6.

Dans le scénario B, le rythme moyen est $(0+4)/2=2$ visiteurs par heure. Le cumul linéaire moyen est $C_{B,\mathrm{moy}}(t)=2t$. À $t=1$ h, il donne 2 visiteurs, alors que le cumul exact $C_B(t)=t^2$ en donne 1. À $t=2$ h, les deux valent 4. Le calcul avec le rythme moyen retrouve le total final, mais il masque le moment où les visiteurs arrivent.

**À retenir :** le cumul additionne les quantités apportées au fil du temps. Sur un graphique du rythme, il correspond à l'aire sous la courbe. Pour un rythme constant par paliers, on additionne les aires des rectangles ; pour un rythme qui varie continûment, on calcule l'aire sous la courbe.
</details>

---

## Le point de départ

Sam retrouve actuellement son groupe d'amis environ deux fois par mois. Il projette 30 années supplémentaires et annonce : « Cela fait 720 occasions. »

Mais un déménagement et des emplois du temps différents pourraient rendre les rencontres moins fréquentes. Nous comparons deux scénarios, sans prétendre prédire la vie de Sam.

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
