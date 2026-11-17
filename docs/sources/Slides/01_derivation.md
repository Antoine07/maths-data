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

Le point $A$ glisse sur la courbe $f(x)=\frac{x^2}{2}$. À gauche, on voit le point et sa tangente sur la courbe. À droite, la même tangente est isolée : on voit sa direction changer et son équation $y=ax+b$ se met à jour.

<div class="interactive-math-demo" data-derivative-demo>
  <div class="interactive-demo-controls derivative-demo-controls">
    <label>Position du point <output data-derivative-position-label>x₀ = −1,50</output>
      <input data-derivative-position type="range" min="-2" max="2" step="0.01" value="-1.5" aria-label="Position du point sur la courbe">
    </label>
    <div class="interactive-demo-buttons">
      <button class="button primary" type="button" data-derivative-toggle aria-pressed="false">▶ Animer</button>
      <button class="button" type="button" data-derivative-reset>Repartir du début</button>
    </div>
  </div>
  <p class="interactive-demo-readout" data-derivative-readout aria-live="polite">Au point x₀ = −1,50 : a = f′(x₀) = −1,50 et b = −1,13. Tangente : y = −1,50x − 1,13.</p>
  <svg class="interactive-demo-svg derivative-demo-svg" viewBox="0 0 1000 390" role="img" aria-label="À gauche, une parabole et sa tangente mobile. À droite, la même droite tangente isolée, qui pivote et change d'ordonnée à l'origine.">
    <text x="270" y="30" text-anchor="middle" class="demo-title">Courbe et tangente</text>
    <line x1="90" y1="280" x2="450" y2="280" class="demo-axis"/>
    <line x1="270" y1="145" x2="270" y2="290" class="demo-axis"/>
    <path d="M90 215H450M90 150H450" class="demo-grid"/>
    <path d="" class="demo-derivative-curve" data-derivative-curve/>
    <line x1="0" y1="0" x2="0" y2="0" class="demo-tangent-line" data-derivative-tangent/>
    <circle cx="0" cy="0" r="8" class="demo-point" data-derivative-point/>
    <text x="455" y="286" class="demo-caption">x</text>
    <text x="278" y="150" class="demo-caption">f(x)</text>
    <text x="90" y="307" text-anchor="middle" class="demo-caption">−2</text>
    <text x="180" y="307" text-anchor="middle" class="demo-caption">−1</text>
    <text x="360" y="307" text-anchor="middle" class="demo-caption">1</text>
    <text x="450" y="307" text-anchor="middle" class="demo-caption">2</text>
    <text x="90" y="65" class="demo-equation">f(x) = x² / 2</text>
    <text x="780" y="30" text-anchor="middle" class="demo-title">La droite tangente pivote</text>
    <line x1="600" y1="280" x2="960" y2="280" class="demo-axis"/>
    <line x1="780" y1="175" x2="780" y2="375" class="demo-axis"/>
    <path d="M600 230H960M600 330H960" class="demo-grid"/>
    <line x1="600" y1="0" x2="960" y2="0" class="demo-tangent-line" data-derivative-isolated-line/>
    <circle cx="0" cy="0" r="8" class="demo-point" data-derivative-isolated-point/>
    <text x="965" y="286" class="demo-caption">x</text>
    <text x="790" y="180" class="demo-caption">y</text>
    <text x="600" y="307" text-anchor="middle" class="demo-caption">−2</text>
    <text x="690" y="307" text-anchor="middle" class="demo-caption">−1</text>
    <text x="870" y="307" text-anchor="middle" class="demo-caption">1</text>
    <text x="960" y="307" text-anchor="middle" class="demo-caption">2</text>
    <text x="600" y="65" class="demo-equation" data-tangent-equation>y = −1,50x − 1,13</text>
  </svg>
</div>

Pour la tangente au point d’abscisse $x_0$, $a=f'(x_0)$ est sa pente et $b=f(x_0)-a x_0$ son ordonnée à l’origine. La valeur $f(x_0)$ donne la hauteur du point sur la courbe ; elle n’est pas forcément égale à $b$.

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

## Problème — Combien de tee-shirts produire pour maximiser le bénéfice ?

Une entreprise prépare des tee-shirts pour un festival. Elle peut en produire jusqu’à 1 000 et suppose qu’elle vendra tous ceux qu’elle fabrique.

On note $x$ le nombre de centaines de tee-shirts produits. Dans ce modèle, le bénéfice $B(x)$, exprimé en centaines d’euros, est donné par la fonction du second degré :

$$
B(x)=-x^2+10x-16,\qquad x\in[0;10].
$$

### Énoncé

1. Calcule $B(0)$. Que représente cette valeur pour l’entreprise ?
2. Calcule $B'(x)$ et résous $B'(x)=0$.
3. Dresse le tableau de signes de $B'(x)$, puis le tableau de variations de $B$.
4. Combien de tee-shirts l’entreprise doit-elle produire pour maximiser son bénéfice ? Quel est ce bénéfice en euros ?

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

## Exercice — Une affiche qui utilise moins de papier

Une association prépare une affiche pour annoncer un concert. Le texte et les illustrations occupent un bloc rectangulaire de $600\,\text{cm}^2$. Le graphiste peut modifier les proportions du bloc tout en gardant la même aire.

L’imprimeur demande de laisser 2 cm de marge à gauche et à droite, et 3 cm en haut et en bas. Pour que l’affiche reste lisible, la largeur du bloc imprimé doit être comprise entre 15 et 30 cm.

Quelles dimensions de feuille faut-il choisir pour utiliser le moins de papier possible ?

On note $x$ la largeur du bloc imprimé, en centimètres, et $A(x)$ l’aire de la feuille entière, en centimètres carrés.

1. Fais un croquis de l’affiche. Exprime en fonction de $x$ la hauteur du bloc imprimé, puis la largeur et la hauteur de la feuille.
2. Montre que, pour $x\in[15;30]$,

   $$
   A(x)=\frac{6x^2+624x+2400}{x}.
   $$

3. Calcule $A'(x)$, puis dresse son tableau de signes et le tableau de variations de $A$.

   **Indice —** avant de dériver, divise chaque terme du numérateur par $x$.

4. Donne les dimensions du bloc imprimé, puis celles de la feuille qui minimise l’aire de papier utilisée. Calcule cette aire minimale.

---

## TP — Combien de plats un restaurant doit-il proposer ?

Un restaurateur envisage d'élargir sa carte. Chaque paire de plats peut demander du matériel, des ingrédients ou du temps de préparation en commun. Nous modélisons ce travail de coordination par une relation entre chaque paire.

<svg class="interactive-demo-svg restaurant-pairs-svg" viewBox="0 0 400 250" role="img" aria-label="Quatre plats reliés deux à deux ; chaque trait représente une paire à coordonner.">
  <text x="200" y="26" text-anchor="middle" class="demo-title">Les paires de plats à coordonner</text>
  <g class="restaurant-pair-lines" stroke="#7b9a83" stroke-width="3">
    <line x1="125" y1="85" x2="275" y2="85"/><line x1="125" y1="85" x2="125" y2="185"/><line x1="125" y1="85" x2="275" y2="185"/>
    <line x1="275" y1="85" x2="125" y2="185"/><line x1="275" y1="85" x2="275" y2="185"/><line x1="125" y1="185" x2="275" y2="185"/>
  </g>
  <g fill="#fff" stroke="#245c46" stroke-width="3"><circle cx="125" cy="85" r="24"/><circle cx="275" cy="85" r="24"/><circle cx="125" cy="185" r="24"/><circle cx="275" cy="185" r="24"/></g>
  <g text-anchor="middle" dominant-baseline="central" class="demo-caption" fill="#183d2e"><text x="125" y="85">A</text><text x="275" y="85">B</text><text x="125" y="185">C</text><text x="275" y="185">D</text></g>
</svg>

### Partie 1 — Compter les relations

1. Combien de paires de plats apparaissent sur le dessin ?
2. Si l'on ajoute un cinquième plat, combien de nouvelles relations apparaît-il ?
3. Avec $x$ plats, combien chaque plat possède-t-il de relations potentielles ?
4. En déduire le nombre total de paires $R(x)$. Justifier pourquoi une division par 2 est nécessaire.

### Partie 2 — Traduire les relations en coût

On suppose que chaque paire entraîne un coût moyen de 6 unités.

5. Écrire le coût total $C(x)$ en fonction du nombre de paires.
6. Développer et réduire l'expression obtenue.
7. Calculer le coût associé à 5, 10 et 15 plats.

---

## TP — Mesurer le coût d'un plat supplémentaire

Le restaurateur demande : *« Si j'ajoute un plat, de combien augmente le coût de coordination ? »* On commence par un changement fini, avec un nombre entier de plats.

### Partie 3 — De la différence à la dérivée

8. Calculer $C(6)-C(5)$ puis $C(11)-C(10)$.
9. Le coût supplémentaire est-il identique dans les deux cas ? Que suggèrent ces calculs sur l'évolution du coût ?
10. Développer et réduire $C(x+1)-C(x)$. Calculer aussi $C'(x)$, puis comparer ces deux mesures de variation.

<div class="interactive-math-demo restaurant-cost-demo" data-restaurant-cost>
  <div class="interactive-demo-controls">
    <label>Nombre de plats au départ <output data-restaurant-cost-x-label>8</output>
      <input type="range" min="1" max="20" step="1" value="8" data-restaurant-cost-x aria-label="Nombre de plats au départ, de 1 à 20">
    </label>
  </div>
  <div class="restaurant-readouts" aria-live="polite">
    <div><span>Coût actuel</span><strong data-restaurant-cost-now>168</strong></div>
    <div><span>Coût avec un plat de plus</span><strong data-restaurant-cost-next>216</strong></div>
    <div><span>Coût supplémentaire</span><strong data-restaurant-cost-delta>48</strong></div>
  </div>
  <p class="demo-caption">Déplace le curseur et compare les deux coûts. Vérifie tes calculs avant de poursuivre.</p>
</div>

Pour étudier une variation très petite, on regarde le taux :

$$
\frac{C(x+h)-C(x)}{h}.
$$

Quand $h$ tend vers zéro, ce taux devient la dérivée $C'(x)$. Elle décrit la pente du modèle continu à cet endroit. Pour l'ajout exact d'un plat, qui est entier, on utilise la différence $C(x+1)-C(x)$.

---

## TP — Rechercher un nombre de plats avantageux

Proposer davantage de plats peut aussi attirer des clients. On suppose que chaque plat apporte un bénéfice de diversité de 60 unités.

### Parties 4 et 5 — Construire le bénéfice net

11. Écrire la fonction $B(x)$ qui modélise ce bénéfice de diversité.
12. Calculer $B'(x)$. Que représente cette dérivée ?
13. Le bénéfice net $A(x)$ est le bénéfice de diversité moins le coût de coordination. Écrire $A(x)$ en fonction de $B(x)$ et $C(x)$.
14. Développer et réduire pour obtenir une expression polynomiale de $A(x)$.
15. Calculer $A'(x)$.
16. Résoudre $A'(x)=0$. Que peut indiquer cette valeur sur le bénéfice net ?

<div class="interactive-math-demo restaurant-opt-demo" data-restaurant-opt>
  <div class="interactive-demo-controls">
    <label>Nombre de plats dans le modèle continu <output data-restaurant-opt-x-label>8</output>
      <input type="range" min="0" max="21" step="0.1" value="8" data-restaurant-opt-x aria-label="Nombre continu de plats, de zéro à vingt et un">
    </label>
  </div>
  <svg class="interactive-demo-svg restaurant-opt-svg" viewBox="0 0 800 370" role="img" aria-label="Courbe du bénéfice net selon le nombre de plats ; le point suit le curseur.">
    <text x="400" y="25" text-anchor="middle" class="demo-title">Bénéfice net du modèle continu</text>
    <path d="M100 300H700M100 60V300" class="demo-axis"/>
    <path d="M100 300H700M100 240H700M100 180H700M100 120H700M100 60H700M200 60V300M300 60V300M400 60V300M500 60V300M600 60V300M700 60V300" class="demo-grid"/>
    <path d="" fill="none" stroke="#245c46" stroke-width="4" data-restaurant-opt-curve/>
    <line x1="328.6" y1="60" x2="328.6" y2="300" stroke="#d8894a" stroke-dasharray="6 6" data-restaurant-opt-guide/>
    <circle cx="328.6" cy="80" r="8" fill="#e66f51" data-restaurant-opt-point/>
    <text x="100" y="325" text-anchor="middle" class="demo-caption">0</text><text x="300" y="325" text-anchor="middle" class="demo-caption">7</text><text x="500" y="325" text-anchor="middle" class="demo-caption">14</text><text x="700" y="325" text-anchor="middle" class="demo-caption">21 plats</text>
    <text x="90" y="304" text-anchor="end" class="demo-caption">0</text><text x="90" y="64" text-anchor="end" class="demo-caption">330</text>
    <text x="400" y="355" text-anchor="middle" class="demo-caption">Bénéfice net (unités)</text>
  </svg>
  <p class="interactive-demo-readout" data-restaurant-opt-readout aria-live="polite">À 8 plats : bénéfice net 312 unités ; dérivée +15. Le bénéfice net augmente localement.</p>
</div>

---

## TP — Interpréter et discuter le modèle

Le modèle continu donne une valeur de $x$ qui peut ne pas être entière. Dans la réalité, le restaurant doit proposer un nombre entier de plats.

### Partie 6 — Revenir à la situation réelle

17. Calculer $A(10)$ et $A(11)$.
18. Quel(s) nombre(s) entier(s) de plats donne(nt) le bénéfice net le plus élevé ? Comparer ce résultat à l’optimum du modèle continu.
19. Citer au moins deux hypothèses simplificatrices du modèle. Quelles données réelles faudrait-il recueillir pour aider le restaurateur à décider ?

**Conclusion attendue :** distinguer le résultat du modèle continu, la contrainte de nombre entier et la décision réelle. La dérivée aide à repérer une zone favorable ; elle ne remplace pas la vérification des valeurs entières ni les données du restaurant.

**Lien avec la data science :** on construit une fonction de coût et un bénéfice, puis on étudie la dérivée pour rechercher un choix favorable. La même démarche prépare à l'optimisation d'une fonction de perte et à la lecture d'un gradient.

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

## Problème — Un rythme et son cumul

Un groupe se retrouve aujourd'hui deux fois par mois. Peut-on simplement multiplier cette fréquence par 30 ans ?

Comparer une fréquence constante à une fréquence décroissante et vérifier le cumul en le dérivant. Le problème introduit la relation entre une fréquence et son cumul.

[Problème 2 : et si les occasions devenaient moins fréquentes ?](../Tps/Tail_End/02_frequence.md)

---

## TP optimisation 

[TP Optimisation](https://github.com/Antoine07/maths/blob/main/Derivation/TPs/00_TP_optimisation.md)

---

## [Retour au plan](https://antoine07.github.io/maths/)
