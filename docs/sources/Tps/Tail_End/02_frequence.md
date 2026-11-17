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
  <p class="interactive-demo-readout" data-cumul-readout aria-live="polite">À 0 h : rythme de 0 visiteurs/h ; cumul exact de 0 visiteur ; cumul au rythme moyen de 0 visiteur.</p>
  <svg class="interactive-demo-svg cumul-demo-svg" viewBox="0 0 1200 390" role="img" aria-label="Deux graphiques synchronisés : à gauche le rythme f(t)=2t et son aire cumulée ; à droite le cumul exact C(t)=t² comparé au cumul linéaire du rythme moyen 2t.">
    <text x="600" y="28" text-anchor="middle" class="demo-title">Du rythme au cumul : deux lectures du même temps</text>
    <text x="315" y="58" text-anchor="middle" class="demo-title">1. Le rythme et son aire</text>
    <line x1="90" y1="310" x2="540" y2="310" class="demo-axis"/>
    <line x1="90" y1="310" x2="90" y2="90" class="demo-axis"/>
    <path d="M90 255H540M90 200H540M90 145H540M90 90H540M202.5 90V310M315 90V310M427.5 90V310M540 90V310" class="demo-grid"/>
    <path d="M90 310L540 90" class="demo-wave"/>
    <path d="M90 310L90 310L90 310Z" class="cumul-area" data-cumul-area/>
    <line x1="90" y1="310" x2="90" y2="310" class="demo-cursor" data-cumul-cursor/>
    <circle cx="90" cy="310" r="7" class="demo-point" data-cumul-point/>
    <text x="90" y="334" text-anchor="middle" class="demo-caption">0</text>
    <text x="202.5" y="334" text-anchor="middle" class="demo-caption">0,5</text>
    <text x="315" y="334" text-anchor="middle" class="demo-caption">1</text>
    <text x="427.5" y="334" text-anchor="middle" class="demo-caption">1,5</text>
    <text x="540" y="334" text-anchor="middle" class="demo-caption">2 h</text>
    <text x="80" y="94" text-anchor="end" class="demo-caption">4</text>
    <text x="80" y="204" text-anchor="end" class="demo-caption">2</text>
    <text x="80" y="314" text-anchor="end" class="demo-caption">0</text>
    <text x="90" y="80" class="demo-caption">Visiteurs/h</text>
    <text x="315" y="365" text-anchor="middle" class="demo-caption">Aire colorée = cumul exact</text>
    <text x="885" y="58" text-anchor="middle" class="demo-title">2. Le cumul et son approximation moyenne</text>
    <line x1="660" y1="310" x2="1110" y2="310" class="demo-axis"/>
    <line x1="660" y1="310" x2="660" y2="90" class="demo-axis"/>
    <path d="M660 255H1110M660 200H1110M660 145H1110M660 90H1110M772.5 90V310M885 90V310M997.5 90V310M1110 90V310" class="demo-grid"/>
    <path d="M660 310C810 310 960 236.67 1110 90" class="demo-wave"/>
    <path d="M660 310L1110 90" class="cumul-average-line"/>
    <line x1="660" y1="310" x2="660" y2="310" class="demo-cursor" data-cumul-right-cursor/>
    <circle cx="660" cy="310" r="7" class="demo-point" data-cumul-exact-point/>
    <circle cx="660" cy="310" r="6" class="cumul-average-point" data-cumul-average-point/>
    <text x="660" y="334" text-anchor="middle" class="demo-caption">0</text>
    <text x="772.5" y="334" text-anchor="middle" class="demo-caption">0,5</text>
    <text x="885" y="334" text-anchor="middle" class="demo-caption">1</text>
    <text x="997.5" y="334" text-anchor="middle" class="demo-caption">1,5</text>
    <text x="1110" y="334" text-anchor="middle" class="demo-caption">2 h</text>
    <text x="650" y="94" text-anchor="end" class="demo-caption">4</text>
    <text x="650" y="204" text-anchor="end" class="demo-caption">2</text>
    <text x="650" y="314" text-anchor="end" class="demo-caption">0</text>
    <text x="660" y="80" class="demo-caption">Visiteurs cumulés</text>
    <text x="755" y="120" class="demo-caption">C(t)=t²</text>
    <text x="955" y="245" class="demo-caption">C_moy(t) = 2t</text>
    <text x="885" y="365" text-anchor="middle" class="demo-caption">Vert : cumul exact · pointillé : cumul au rythme moyen</text>
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

## Discussion — Un modèle peut changer la décision

Avant d'utiliser la formule, Sam devrait examiner si la fréquence diminue réellement, si elle comporte des ruptures et si un changement d'organisation peut la modifier.

**Lien data :** une extrapolation sur 30 ans à partir d'une fréquence actuelle contient une hypothèse forte. Dessiner plusieurs scénarios rend cette hypothèse visible ; cela ne valide pas le scénario le plus spectaculaire.

[Retour aux quatre problèmes](README.md). Point de départ conceptuel : [*The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html) ; modèle et données créés pour ce problème.
