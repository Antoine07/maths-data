---
marp: true
theme: default
paginate: true
class: lead
---

# Révision d’algèbre : calculs essentiels

![Un rectangle découpé en quatre aires illustre le passage entre (x + 2)(x + 3) et x² + 5x + 6, en développant ou en factorisant.](images/revision-algebre.svg)

---

# Pourquoi faire des maths ? Calculer plus simplement

Dans une boutique, comparons deux paniers :

| Panier | Nombre de produits | Prix par produit | Total à calculer |
|---|---|---|---|
| A | 3 | 50 € | $3 \times 50$ |
| B | 50 | 3 € | $50 \times 3$ |

Pour le panier A, on peut additionner $50 + 50 + 50$.

Pour le panier B, on pourrait additionner 3 cinquante fois. Mais est-il nécessaire de faire toutes ces additions ?

**Avant de calculer :** quelle écriture vous permet de trouver le total le plus facilement ?

---

# Trois fois 50 ou cinquante fois 3 ?

$$
\underbrace{50+50+50}_{3\text{ fois}}=150
\qquad
\underbrace{3+3+\cdots+3}_{50\text{ fois}}=150.
$$

La **commutativité de la multiplication des nombres** permet d'échanger les facteurs :

$$
3\times50=50\times3=150.
$$

Les deux paniers contiennent des quantités différentes, mais coûtent chacun **150 €**.

Si l'on procède par additions successives, la première écriture demande 2 additions ; la seconde, 49. Reconnaître l'égalité évite ce travail répétitif.

**Les maths aident aussi à choisir un chemin de calcul plus court, tout en gardant un résultat exact.**

---

# Changer l'écriture pour alléger le calcul

Trois propriétés permettent de remplacer un calcul par un calcul égal, plus commode.

**Échanger les facteurs — commutativité :**

$$
50\times3=3\times50=150.
$$

**Regrouper les facteurs — associativité :**

$$
25\times12=25\times(4\times3)=(25\times4)\times3=100\times3=300.
$$

**Décomposer un facteur — distributivité :**

$$
7\times99=7\times(100-1)=700-7=693.
$$

Chaque transformation repose sur une propriété. Nous retrouverons la distributivité pour développer et factoriser des expressions.

---

# À vous · Trouver un chemin plus court

**Objectif :** choisir et expliquer une simplification. **Prérequis :** les trois propriétés précédentes.

Sans calculatrice :

1. **Échanger :** calculer $50\times6$ en choisissant une addition courte.
2. **Regrouper :** calculer $4\times17\times25$ en faisant apparaître 100.
3. **Décomposer :** calculer $3\times49$ en utilisant 50.

**Livrable :** une chaîne d'égalités par calcul et le nom de la propriété utilisée. **Réussite :** résultat exact et réécriture justifiée.

<details><summary>Indices gradués</summary>

1. Cinquante fois 6 et six fois 50 donnent le même total.
2. Échanger les facteurs pour rapprocher 4 et 25, puis les regrouper.
3. Écrire $49=50-1$, puis distribuer la multiplication.

</details>

<details><summary>Correction · Calculer moins, expliquer le choix</summary>

1. $50\times6=6\times50=300$ : **commutativité**. Six termes de 50 sont plus commodes à additionner que cinquante termes de 6.
2. $4\times17\times25=(4\times25)\times17=100\times17=1700$ : **commutativité et associativité**.
3. $3\times49=3\times(50-1)=3\times50-3\times1=150-3=147$ : **distributivité**.

Un même résultat peut être obtenu par plusieurs chemins corrects. Chercher une écriture adaptée fait partie du raisonnement mathématique.

</details>

---

# 1. Priorités de calcul

Ordre des opérations (toujours dans cet ordre) :

1. Parenthèses
2. Puissances et racines
3. Multiplications et divisions
4. Additions et soustractions

Exemple :

$$
3 + 2 \cdot 5^2 = 3 + 2 \cdot 25 = 3 + 50 = 53.
$$

---

# À vous · Quatre calculs algébriques

Sans calculatrice, simplifiez chaque expression et justifiez les transformations.

1. **Réduire :** $5x-3+2x+8$.
2. **Développer et réduire :** $3(2x-5)-2(x+1)$.
3. **Factoriser :** $6x^2+9x$.
4. **Simplifier :** $\dfrac{x^2-9}{x-3}$, en précisant la valeur interdite.

<details><summary>Afficher la correction</summary>

1. $5x-3+2x+8=7x+5$.
2. $3(2x-5)-2(x+1)=6x-15-2x-2=4x-17$.
3. $6x^2+9x=3x(2x+3)$.
4. $\dfrac{x^2-9}{x-3}=\dfrac{(x-3)(x+3)}{x-3}=x+3$, pour $x\ne3$. La simplification ne rend pas l'expression initiale définie en $x=3$.

</details>

---

# 2. Développer

Règle de base :

$$
(a+b)(c+d)=ac + ad + bc + bd.
$$

Cas particuliers importants :

### Cas 1 : carré d’une somme

$$
(a+b)^2 = a^2 + 2ab + b^2.
$$

### Cas 2 : carré d’une différence

$$
(a-b)^2 = a^2 - 2ab + b^2.
$$

---

### Cas 3 : produit conjugué

$$
(a-b)(a+b)=a^2 - b^2.
$$

Exemple :

$$
(3x - 2)(x + 5) = 3x^2 + 15x - 2x - 10.
$$

$$
= 3x^2 + 13x - 10.
$$

---

# 3. Factoriser

Objectif : réécrire un terme sous forme de produit.

Méthodes principales :

### 1. Mise en évidence

$$
3x^2 - 6x = 3x(x - 2).
$$

### 2. Identités remarquables

$$
x^2 - 4 = (x-2)(x+2).
$$

$$
9x^2 - 6x + 1 = (3x - 1)^2.
$$

---

### 3. Factorisation par regroupement

$$
x^3 + x^2 + x + 1 = (x^2 + 1)(x + 1).
$$

---

# Démo 2 · La somme de deux entiers pairs est paire

**Objectif :** utiliser la factorisation pour passer des exemples à une preuve générale, puis traduire cette preuve dans Lean.

Un entier $a \in \mathbb{Z}$ est **pair** s'il existe un entier $k$ tel que $a = 2k$. Cela inclut 0 et les entiers négatifs.

Exemple : $14 + 22 = 36 = 2 \times 18$.

Cet exemple vérifie un cas. Pour démontrer l'énoncé, il faut raisonner sur **deux entiers pairs quelconques**, sans leur attribuer des valeurs particulières.

**Prérequis :** mise en facteur commun et sens du mot « entier ».

---

# À faire · Construire la preuve sur papier

On suppose $a = 2k$ et $b = 2\ell$, avec $k,\ell \in \mathbb{Z}$.

1. Remplacer $a$ et $b$ dans $a+b$.
2. Mettre 2 en facteur.
3. Quel entier joue le rôle du « double de quelque chose » pour $a+b$ ?
4. Pourquoi le raisonnement fonctionne-t-il aussi si $a$ ou $b$ est négatif ?

**Livrable :** trois lignes de calcul et une phrase de conclusion. Ne pas supposer que $k = \ell$ : les deux entiers pairs peuvent être différents.

<details><summary>Indice · Choisir un témoin</summary>

Un **témoin** est ici l'entier qui rend vraie l'écriture « $a+b = 2 \times$ un entier ». Utiliser la règle $2k + 2\ell = 2(k+\ell)$.

</details>

<details><summary>Correction · Une preuve pour tous les entiers</summary>

Comme $a$ et $b$ sont pairs, il existe $k,\ell \in \mathbb{Z}$ tels que $a=2k$ et $b=2\ell$. Alors :

$$
a+b = 2k + 2\ell = 2(k+\ell).
$$

La somme $k+\ell$ est un entier. Elle fournit donc le témoin qui prouve que $a+b$ est pair.

Le raisonnement ne suppose aucun signe : par exemple $-6 + 10 = 2(-3 + 5) = 4$.

</details>

---

# Traduire l'énoncé dans Lean

**Lean est un assistant de preuve :** il vérifie les étapes d'une démonstration formelle. Ici, on utilise Lean 4 avec la bibliothèque mathématique **Mathlib**.

| Écriture | Lecture |
| --- | --- |
| `a b : ℤ` | `a` et `b` sont des entiers relatifs. |
| `ha : Even a` | `ha` est l'hypothèse « `a` est pair ». |
| `hb : Even b` | `hb` est l'hypothèse « `b` est pair ». |
| `Even (a + b)` | C'est la conclusion à démontrer. |

Dans Mathlib, `Even a` signifie qu'il existe un entier `k` tel que **`a = k + k`**. C'est la même notion que $a = 2k$ ; la bibliothèque l'écrit sous forme d'addition.

On cherche donc un témoin pour écrire `a + b = (k + l) + (k + l)`.

[Définition officielle de `Even`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Even.html#Even).

---

# À faire · Formaliser la preuve en Lean

Dans un environnement **Lean 4 avec Mathlib**, retrouver les deux témoins, choisir leur somme, puis vérifier l'égalité obtenue.

**Livrable :** une preuve acceptée par Lean, sans `sorry` ni ajout d'axiome. `sorry` est un trou de preuve : un fichier accepté avec cet avertissement ne suffit pas à terminer la démonstration.

<details><summary>Correction · Le fichier Lean complet</summary>

```lean
import Mathlib

theorem somme_de_deux_pairs (a b : ℤ)
    (ha : Even a) (hb : Even b) : Even (a + b) := by
  rcases ha with ⟨k, hk⟩
  rcases hb with ⟨l, hl⟩
  refine ⟨k + l, ?_⟩
  rw [hk, hl]
  ring
```

Le témoin proposé est `k + l`. Après remplacement de `a` et `b`, il reste à vérifier l'identité `(k + k) + (l + l) = (k + l) + (k + l)`.

</details>

[Télécharger le fichier Lean](exemples/revision/somme_pairs.lean) · [Ouvrir un éditeur Lean en ligne](https://live.lean-lang.org/) ; utiliser un projet disposant de Mathlib.

---

# Lire la preuve Lean, ligne par ligne

| Ligne | Rôle dans la démonstration |
| --- | --- |
| `import Mathlib` | Charger les définitions et les outils utilisés. |
| `rcases ha with ⟨k, hk⟩` | Obtenir un entier `k` et l'égalité `hk : a = k + k`. |
| `rcases hb with ⟨l, hl⟩` | Obtenir un entier `l` et l'égalité `hl : b = l + l`. |
| `refine ⟨k + l, ?_⟩` | Proposer le témoin et laisser l'égalité comme but à prouver. |
| `rw [hk, hl]` | Remplacer `a` et `b` par leurs expressions. |
| `ring` | Justifier l'identité algébrique qui reste. |

`ring` produit une preuve de l'identité ; il ne se contente pas de tester quelques valeurs.

**À retenir :** un exemple illustre ; une preuve explique pourquoi le résultat vaut pour tous les cas de l'énoncé ; Lean contrôle la traduction formelle de ce raisonnement.

Références : [témoins et `rcases`](https://leanprover-community.github.io/mathematics_in_lean/C03_Logic.html), [réécriture et `ring`](https://leanprover-community.github.io/mathematics_in_lean/C02_Basics.html).

---

# 4. Fractions et simplifications

### Simplification par division par un même facteur :

$$
\frac{6x}{9} = \frac{6}{9}x = \frac{2}{3}x.
$$

### Fraction d'expressions :

$$
\frac{x^2 - 4}{x - 2}.
$$

---

Factorisons le numérateur :

$$
x^2 - 4 = (x-2)(x+2).
$$

Donc pour x !=2

$$
\frac{x^2 - 4}{x-2} = x+2.
$$

---

# 5. Manipulation de puissances

Règles fondamentales :

1.

$$
   a^m \cdot a^n = a^{m+n}
$$

3.

$$
   \frac{a^m}{a^n} = a^{m-n}
$$

---

5.

$$
   (a^m)^n = a^{mn}
$$

7.

$$
   (a b)^n = a^n b^n
$$

9.

$$
   \left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}
$$

Exemple :

$$
\frac{2^7}{2^3} = 2^{7-3} = 2^4 = 16.
$$

---

# 6. Racines

$$
\sqrt{a^2} = |a|
$$

$$
\sqrt{ab} = \sqrt{a}\sqrt{b} \quad (a,b \ge 0)
$$

$$
\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}
$$

Exemple :

$$
\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}.
$$

---

# Fractions et racines · Choisir une méthode

**Objectif :** simplifier des expressions exactes en utilisant les carrés, les racines et les identités remarquables.

Pour un dénominateur non nul :

$$
\left(\frac{u}{v}\right)^2=\frac{u^2}{v^2}.
$$

Pour $a,b\geq0$, les expressions $\sqrt a+\sqrt b$ et $\sqrt a-\sqrt b$ sont **conjuguées** :

$$
(\sqrt a+\sqrt b)(\sqrt a-\sqrt b)=a-b.
$$

Si $a\ne b$, multiplier le numérateur et le dénominateur par l'expression conjuguée permet de supprimer les racines du dénominateur. Cette transformation s'appelle **rationaliser le dénominateur**.

**Avant de développer :** chercher si les racines se simplifient déjà. Attention : $(u+v)^2\ne u^2+v^2$ en général ; le terme $2uv$ ne doit pas disparaître.

---

# Racines · Exercice A — Le carré d'un quotient

Sans calculatrice, simplifier :

$$
A=\left(\frac{\sqrt6}{\sqrt3+\sqrt2}\right)^2.
$$

1. Vérifier que le dénominateur est non nul.
2. Élever le numérateur et le dénominateur au carré, puis supprimer les racines du dénominateur.
3. Donner une valeur exacte et justifier chaque égalité.

**Livrable :** une chaîne de calcul sans racine au dénominateur. Une approximation décimale pourra servir de contrôle après le calcul exact.

<details><summary>Indice</summary>

Le carré du dénominateur vaut $5+2\sqrt6$. Quelle expression lui est conjuguée ?

</details>

<details><summary>Afficher la correction</summary>

Le dénominateur est strictement positif. En développant son carré :

$$
(\sqrt3+\sqrt2)^2=3+2\sqrt6+2=5+2\sqrt6.
$$

Ainsi :

$$
A=\frac6{5+2\sqrt6}
=\frac{6(5-2\sqrt6)}{(5+2\sqrt6)(5-2\sqrt6)}
=\frac{6(5-2\sqrt6)}{25-24}.
$$

Le produit des conjugués vaut 1, donc le facteur utilisé n'est pas nul. On obtient :

$$
\boxed{A=30-12\sqrt6}.
$$

Pour contrôler : $A\approx0{,}6061$. Le résultat est positif, comme le carré de départ.

</details>

---

# Racines · Exercice B — Simplifier avant de rationaliser

Sans calculatrice, simplifier :

$$
B=\left(\frac{\sqrt2}{\sqrt3+1}\right)^2.
$$

Vérifier que l'expression est définie, développer le carré du dénominateur, puis donner une valeur exacte sans racine au dénominateur.

<details><summary>Indice</summary>

Après avoir élevé au carré, simplifier la fraction par 2. Utiliser ensuite le conjugué de $2+\sqrt3$.

</details>

<details><summary>Afficher la correction</summary>

Comme $\sqrt3+1>0$, le quotient est défini. On calcule :

$$
B=\frac2{(\sqrt3+1)^2}
=\frac2{4+2\sqrt3}
=\frac1{2+\sqrt3}.
$$

Puis :

$$
B=\frac{2-\sqrt3}{(2+\sqrt3)(2-\sqrt3)}
=\frac{2-\sqrt3}{4-3}
=\boxed{2-\sqrt3}.
$$

Le produit au dénominateur vaut 1. Pour contrôler : $B\approx0{,}2679$.

</details>

---

# Racines · Exercice C — Réduire les racines d'abord

Sans calculatrice, simplifier :

$$
C=\left(\frac{\sqrt{12}}{\sqrt8-\sqrt2}\right)^2.
$$

Commencer par simplifier chaque racine. Vérifier que le dénominateur ne s'annule pas, puis chercher le chemin de calcul le plus court.

<details><summary>Indice</summary>

Écrire $12=4\times3$ et $8=4\times2$. Les deux termes du dénominateur deviennent des multiples de $\sqrt2$.

</details>

<details><summary>Afficher la correction</summary>

On a $\sqrt{12}=2\sqrt3$ et $\sqrt8=2\sqrt2$. Le dénominateur vaut donc :

$$
\sqrt8-\sqrt2=2\sqrt2-\sqrt2=\sqrt2>0.
$$

Il suffit alors d'élever le quotient au carré :

$$
C=\left(\frac{2\sqrt3}{\sqrt2}\right)^2
=\frac{(2\sqrt3)^2}{(\sqrt2)^2}
=\frac{12}{2}
=\boxed6.
$$

Ici, réduire les racines avant de calculer évite une rationalisation inutile. On n'a pas utilisé la fausse règle $\sqrt8-\sqrt2=\sqrt{8-2}$.

</details>

---

# Racines · Exercice D — Un dénominateur avec une différence

Sans calculatrice, simplifier :

$$
D=\left(\frac{\sqrt3}{\sqrt5-\sqrt2}\right)^2.
$$

Justifier que le quotient est défini. Développer le carré d'une différence, puis utiliser l'expression conjuguée pour donner une valeur exacte sans racine au dénominateur.

<details><summary>Indice</summary>

Le carré du dénominateur vaut $7-2\sqrt{10}$. Le produit avec son conjugué fait apparaître $49-40$.

</details>

<details><summary>Afficher la correction</summary>

Comme $\sqrt5>\sqrt2$, le dénominateur est strictement positif. Le carré d'une différence donne :

$$
(\sqrt5-\sqrt2)^2=5-2\sqrt{10}+2=7-2\sqrt{10}.
$$

Ainsi :

$$
D=\frac3{7-2\sqrt{10}}
=\frac{3(7+2\sqrt{10})}{(7-2\sqrt{10})(7+2\sqrt{10})}
=\frac{3(7+2\sqrt{10})}{49-40}.
$$

Le produit des conjugués vaut 9. Il reste à simplifier le facteur 3 :

$$
\boxed{D=\frac{7+2\sqrt{10}}3}.
$$

Pour contrôler : $D\approx4{,}4415$. Attention au signe du terme croisé : dans $(u-v)^2$, il vaut $-2uv$.

</details>

---

# 7. Logarithmes (règles essentielles)

$$
   \ln(ab)=\ln a + \ln b
$$

$$
   \ln\left(\frac{a}{b}\right)=\ln a - \ln b
$$

$$
   \ln(a^n) = n\ln a
$$

$$
   e^{\ln(a)} = a \quad (a>0)
$$

---

Exemples :

$$
\ln(12)=\ln(3)+\ln(4)
$$

$$
\ln(2^5)=5\ln 2
$$

---

# 8. Résolution d’équations simples

### 1. Premier degré

$$
3x - 5 = 13
\Rightarrow 3x = 18 \Rightarrow x = 6.
$$

### 2. Quadratiques

$$
ax^2 + bx + c = 0.
$$

Formule :

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.
$$

---

Exemple :

$$
x^2 - 3x + 2 = 0
$$

$$
\Delta = 9 - 8 = 1
$$

$$
x = \frac{3 \pm 1}{2} \Rightarrow x=1 \text{ ou } x=2.
$$

---

# Exercice 1 : Développer

a) 

$$
(2x-3)(x+4)
$$

b) 

$$
(x+5)^2
$$

---

# Exercice 2 : Factoriser

a) 

$$
4x^2 - 9
$$

b) 

$$
x^2 - 6x + 9
$$

---

# Exercice 3 : Simplifier

$$
\frac{3x^2 - 12x}{3x}
$$

---

# Exercice 4 : Puissances

Simplifier :

$$
\frac{5^7}{5^4}, \quad (3x^2)^3
$$

---

# Exercice 5 : Logarithmes

Simplifier :

a) 

$$
\ln(8x)
$$

b) 

$$
\ln(x^3)
$$

---

# Exercice 6 : Équation

Résoudre :

$$
x^2 - 5x + 6 = 0.
$$

---

# Rappel · Écrire une somme finie

Le symbole sigma abrège l'addition de plusieurs termes :

$$
\sum_{k=1}^{n} u_k = u_1+u_2+\cdots+u_n.
$$

L'indice $k$ prend ici toutes les valeurs entières de 1 à $n$. Il sert à parcourir les termes.

Exemple :

$$
\sum_{k=1}^{4}(2k+1)=3+5+7+9=24.
$$

Quand le même nombre $c$ est répété $n$ fois, on obtient $\sum_{k=1}^{n}c=nc$.

---

# Rappel · Repérer une somme télescopique

Une somme est dite **télescopique** lorsque des termes se compensent entre eux.

On commence par transformer chaque terme :

$$
\frac{1}{k(k+1)}=\frac1k-\frac1{k+1}.
$$

Alors les termes intermédiaires s'annulent :

$$
\sum_{k=1}^{n}\frac{1}{k(k+1)}
=\left(1-\frac12\right)+\left(\frac12-\frac13\right)+\cdots+
\left(\frac1n-\frac1{n+1}\right)
=1-\frac1{n+1}=\frac{n}{n+1}.
$$

---

# À vous · Quatre calculs de sommes finies

Pour $n\geq1$, simplifier les sommes 1 et 2. Calculer les sommes 3 et 4.

1. $\displaystyle S_n=\sum_{k=1}^{n}\frac{1}{k(k+1)}$
2. $\displaystyle U_n=\sum_{k=1}^{n}k\,k!$
3. $\displaystyle V_n=\sum_{k=1}^{n}\big((k+1)-k\big)$
4. $\displaystyle W=\sum_{k=1}^{4}\big((k+1)^2-k^2\big)$

Chercher dans chaque terme ce qui s'annule entre deux lignes successives.

---

# Correction · Les quatre sommes

<details><summary>Afficher une correction possible</summary>

1. $\displaystyle \frac1{k(k+1)}=\frac1k-\frac1{k+1}$, donc $\displaystyle S_n=1-\frac1{n+1}=\frac{n}{n+1}$.
2. $k\,k!=(k+1)!-k!$, donc $\displaystyle U_n=(n+1)!-1$.
3. Les termes se réduisent à $1$ : $\displaystyle V_n=\sum_{k=1}^{n}1=n$.
4. $\displaystyle W=(2^2-1^2)+(3^2-2^2)+(4^2-3^2)+(5^2-4^2)=5^2-1^2=24$.

</details>

---

# Facultatif guidé · Une somme avec deux décalages

On reprend la somme plus technique :

$$
T_n=\sum_{k=1}^{n}\frac{1}{k(k+2)}.
$$

1. Vérifier que $\displaystyle \frac{1}{k(k+2)}=\frac12\left(\frac1k-\frac1{k+2}\right)$.
2. Écrire les premiers termes et repérer ceux qui se compensent.
3. Donner les quelques termes qui restent, puis simplifier.

<details><summary>Correction guidée</summary>

La décomposition donne :

$$
T_n=\frac12\sum_{k=1}^{n}\left(\frac1k-\frac1{k+2}\right).
$$

Les termes intermédiaires s'annulent deux à deux. Il reste les deux premiers et les deux derniers :

$$
T_n=\frac12\left(1+\frac12-\frac1{n+1}-\frac1{n+2}\right).
$$

</details>

---

# Rappel · Écrire un produit fini

Comme $\sum$ abrège une addition, $\prod$ abrège une multiplication :

$$
\prod_{k=1}^{n}u_k=u_1\times u_2\times\cdots\times u_n.
$$

Par exemple :

$$
\prod_{k=1}^{4}k=1\times2\times3\times4=4!=24.
$$

En data, on multiplie aussi des probabilités indépendantes. Si trois mesures ont des probabilités de fiabilité $0{,}9$, $0{,}8$ et $0{,}95$, la probabilité qu'elles soient toutes fiables est leur produit : $0{,}9\times0{,}8\times0{,}95=0{,}684$.

En NumPy, `np.prod([0.9, 0.8, 0.95])` calcule ce produit.

---

# À vous · Deux calculs de produits

1. Développer puis calculer $\displaystyle P=\prod_{k=1}^{4}(k+1)$. Écrire le résultat avec une factorielle.
2. Trois mesures indépendantes ont les probabilités de fiabilité $0{,}9$, $0{,}8$ et $0{,}95$. Calculer la probabilité qu'elles soient toutes fiables, puis vérifier le calcul avec `np.prod`.

<details><summary>Afficher une correction possible</summary>

1. $\displaystyle P=2\times3\times4\times5=5!=120$.
2. $\displaystyle 0{,}9\times0{,}8\times0{,}95=0{,}684$. En NumPy, `np.prod([0.9, 0.8, 0.95])` renvoie `0.684`.

</details>

---

## Problème — Compter les occasions

La moitié des années d'un horizon reste-t-elle la moitié des rencontres ?

Appliquer les produits et pourcentages à une situation fictive, puis construire une grille de points dont chaque unité est explicite.

[Problème 1 : la moitié des années, combien de rencontres ?](../Tps/Tail_End/01_rencontres.md)

Dans le problème, on pourra écrire les journées de rencontre passées et futures comme des sommes finies, puis utiliser les fréquences constantes pour les calculer rapidement.

---

## [Retour au plan](https://antoine07.github.io/maths/)
