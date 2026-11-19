# Corrections — Des bases à la modélisation

Ce document rassemble les réponses des notions et exercices déjà travaillés dans le parcours **Des bases à la modélisation**. Il suit l'ordre du cours. La partie **Étude de fonction** n'est pas incluse.

Pour les corrections détaillées avec les scripts ou les graphiques, voir aussi les fichiers liés à la fin des sections.

## 1. Révisions d'algèbre

### Calculs et expressions

- $3\times50=50\times3=150$. La commutativité permet de choisir l'écriture la plus commode ; additionner 3 cinquante fois n'est pas nécessaire.
- $5x-3+2x+8=7x+5$.
- $3(2x-5)-2(x+1)=6x-15-2x-2=4x-17$.
- $6x^2+9x=3x(2x+3)$.
- $\dfrac{x^2-9}{x-3}=x+3$, avec $x\ne3$.

### Racines

- $\displaystyle A=\left(\frac{\sqrt6}{\sqrt3+\sqrt2}\right)^2=\frac6{5+2\sqrt6}=30-12\sqrt6$.
- $\displaystyle B=\left(\frac{\sqrt2}{\sqrt3+1}\right)^2=\frac1{2+\sqrt3}=2-\sqrt3$.
- $\displaystyle C=\left(\frac{\sqrt{12}}{\sqrt8-\sqrt2}\right)^2=\left(\frac{2\sqrt3}{\sqrt2}\right)^2=6$.
- $\displaystyle D=\left(\frac{\sqrt3}{\sqrt5-\sqrt2}\right)^2=\frac3{7-2\sqrt{10}}=\frac{7+2\sqrt{10}}3$.

### Sommes et produits

Pour $n\geq1$ :

- $\displaystyle\sum_{k=1}^n\frac1{k(k+1)}=\sum_{k=1}^n\left(\frac1k-\frac1{k+1}\right)=\frac n{n+1}$.
- $\displaystyle\sum_{k=1}^n k\,k!=\sum_{k=1}^n((k+1)!-k!)=(n+1)!-1$.
- $\displaystyle\sum_{k=1}^n((k+1)-k)=n$.
- $\displaystyle\sum_{k=1}^4((k+1)^2-k^2)=5^2-1^2=24$.
- Facultatif : $\displaystyle\sum_{k=1}^n\frac1{k(k+2)}=\frac12\left(1+\frac12-\frac1{n+1}-\frac1{n+2}\right)$.
- $\displaystyle\prod_{k=1}^4(k+1)=2\times3\times4\times5=5!=120$.
- Fiabilité des trois mesures : $0{,}9\times0{,}8\times0{,}95=0{,}684$ (soit $68{,}4\%$). NumPy : `np.prod([0.9, 0.8, 0.95])`.

### Équations et intervalles

- $3x+5=20$ donne $x=5$.
- $2x-3<5$ donne $x<4$, soit l'intervalle $]-\infty;4[$.
- $3(x-2)+4=2x+7$ donne $x=9$.
- $x^2-4=0$ se factorise en $(x-2)(x+2)=0$ : $x=-2$ ou $x=2$.

### Logarithmes — calculs de révision

- $\ln(8x)=\ln 8+\ln x$ pour $x>0$.
- $\ln(x^3)=3\ln x$ pour $x>0$.
- $(\ln x)^2-3\ln x+2=0$ : poser $u=\ln x$. Alors $(u-1)(u-2)=0$, donc $x=e$ ou $x=e^2$.

Pour l'application qui double ses utilisateurs, $N(t)=100\times2^t$ et $\ln N(t)=\ln100+t\ln2$. La pente vaut $\ln2\approx0{,}6931$ et le temps de doublement est $\ln2/\ln2=1$ mois.

Pour $N(t)=100e^{0{,}2t}$ : $N(0)=100$, $N(5)=100e\approx271{,}83$ et $N(t)=500$ lorsque $t=\ln(5)/0{,}2\approx8{,}05$ heures.

Correction détaillée : [logarithmes](10_logarithmes.md).

### Problème des rencontres

Dans l'exemple sur 60 ans, les 18 premières années à 300 journées par an donnent 5 400 journées ; les 12 années suivantes à 12 par an en donnent 144. Le passé représente donc **5 544 journées**. Les 30 années restantes à 12 par an représentent **360 journées** ; total : **5 904**. Il reste 50 % des années de l'horizon, mais seulement $360/5904\approx6{,}10\%$ des journées de rencontre selon ces hypothèses. En doublant les rencontres futures à 24 par an, leur part devient $720/(5544+720)\approx11{,}49\%$.

## 2. Produit scalaire et données

Le prix du panier initial vaut $2\times2+1\times1+1\times3=8$ euros. Pour les trois paniers proposés :

1. $(1,2,1)\cdot(2,1,3)=7$ €.
2. $(0,3,2)\cdot(2,1,3)=9$ €.
3. $(3,0,2)\cdot(2,1,3)=12$ € : le budget de 10 € ne suffit pas.

Les deux listes doivent garder le même ordre de produits. En NumPy, `quantites @ prix` effectue les produits terme à terme et en additionne les résultats.

Correction et explication : [produit scalaire du panier](05b_produit_scalaire.md).

## 3. Fonctions périodiques — encoder l'heure

L'angle d'une heure $h$ dans la journée est $\theta=2\pi h/24$. L'encodage est $(\cos\theta,\sin\theta)$ :

| Heure | Encodage approximatif |
|---:|:---|
| 0 h | $(1,0)$ |
| 6 h | $(0,1)$ |
| 12 h | $(-1,0)$ |
| 18 h | $(0,-1)$ |
| 23 h | $(0{,}966,-0{,}259)$ |

Le cosinus seul ne suffit pas : il vaut 0 à 6 h comme à 18 h. Les deux coordonnées permettent aussi de placer 23 h près de minuit sur le cercle. `np.column_stack((cos_heures, sin_heures))` place ces deux tableaux comme colonnes.

Correction et code : [support sur les fonctions périodiques](../docs/sources/Slides/fonctions_periodiques.md).

## 4. Modéliser des données

### Ajustement affine des températures

`np.polyfit(t, T, 1)` ajuste une droite $T(t)=at+b$ aux mesures par la méthode des moindres carrés. Le `1` demande un polynôme de degré 1. Le résultat est renvoyé dans l'ordre `[a, b]` : pente, puis ordonnée à l'origine. Une prédiction au jour 35 se calcule par `a * 35 + b`.

Le script complet et commenté est dans [le modèle affine de température](04_modele_temperature.py).

### Refroidissement d'une boisson

Avec $T_{\mathrm{pièce}}=20$ °C, on pose l'écart `ecart = T - 20`, puis `y = np.log(ecart)`. Le modèle devient une droite :

$$\ln(T(t)-20)=\ln(T_0-20)-kt.$$

Ainsi `pente, intercept = np.polyfit(t, y, 1)` donne $k=-\text{pente}$ et $T_0=20+e^{\text{intercept}}$. Les mesures étant toutes supérieures à 20 °C, le logarithme de l'écart est défini.

## 5. Dérivation — jusqu'au point d'arrêt

La dérivée en un point donne la pente de la tangente. Pour $f(x)=x^2/2$, on a $f'(x)=x$. Au point d'abscisse $x_0$, la pente vaut $a=f'(x_0)=x_0$ et l'ordonnée à l'origine est $b=f(x_0)-ax_0=-x_0^2/2$. La tangente est donc $y=x_0x-x_0^2/2$.

Règles travaillées : $(x^n)'=nx^{n-1}$, $(f+g)'=f'+g'$, $(fg)'=f'g+fg'$. Le signe de la dérivée indique si la fonction augmente ou diminue.

### Problème des tee-shirts

Pour $B(x)=-x^2+10x-16$ sur $[0;10]$, $B(0)=-16$, soit une perte de 1 600 € dans les unités du modèle. On a $B'(x)=-2x+10$, qui s'annule en $x=5$. La dérivée est positive avant 5 puis négative après 5 : le bénéfice maximal est $B(5)=9$, soit **900 €**, pour **500 tee-shirts**.

### Exercice de l'affiche

À partir de $A(x)=6x+624+2400/x$, on obtient $A'(x)=6-2400/x^2$. Sur $[15;30]$, la dérivée s'annule en $x=20$, est négative avant et positive après : l'aire minimale est atteinte pour un bloc de 20 cm de large. Sa hauteur vaut $600/20=30$ cm. Avec les marges, la feuille mesure **24 cm × 36 cm**, soit une aire minimale de **864 cm²**.

### Problème du restaurant

Le nombre de paires de plats est $R(x)=x(x-1)/2$. Le coût vaut $C(x)=6R(x)=3x^2-3x$. Avec un bénéfice de diversité $B(x)=60x$, le bénéfice net est $A(x)=-3x^2+63x$. Son maximum continu se situe en $x=10{,}5$ ; comme le nombre de plats doit être entier, **10 ou 11 plats** donnent le même maximum, 330 unités.

**Le chapitre suivant, Étude de fonction (limites et asymptotes), n'est pas inclus dans ce document.**

Pour le problème du restaurant, voir aussi le [corrigé détaillé](11_restaurant.md). Pour le problème du cumul, consulter la [correction de fréquence et cumul](09_frequence.md).

---

*Document de correction interne : il ne fait pas partie des pages du cours publiées dans `docs/`.*
