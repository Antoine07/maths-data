---
marp: true
theme: default
paginate: true
class: lead
---



# **Étude complète d'une fonction – Limites, Continuité, Tableau de Variation et Tangente**

Ce chapitre complète l'étude de fonction commencée dans la partie sur la dérivation.
Il fournit toutes les notions nécessaires pour analyser correctement une fonction en mathématiques et en data science.

---

# Vue d'ensemble — relier la courbe et ses variations

![Deux représentations de la fonction x³−3x et de sa dérivée. Le signe de la dérivée indique les intervalles de croissance et les changements de signe repèrent les extrema locaux.](images/fonctions-extrema.svg)

Sur la courbe de $f$, on voit les montées, les descentes et les extrema. La courbe de $f'$ aide à les justifier : $f'>0$ là où $f$ croît ; $f'<0$ là où $f$ décroît. Nous allons aussi étudier les limites, les asymptotes, la continuité et les tangentes.

---

# Limites d'une fonction

La limite décrit **le comportement d'une fonction lorsqu'on s'approche d'un point**, ou lorsqu'on part vers l'infini.

![La fonction x+1, définie pour x différent de 1, s'approche de 2 des deux côtés du point non défini.](images/limite-point.svg)

Exemple illustré : $f(x)=x+1$ pour $x\neq1$. Même sans valeur en 1, sa limite en ce point vaut 2.

---

## Limites aux bornes infinies

Pour une fonction polynomiale :

**Le terme de plus haut degré domine.**

Exemples :

1.

$$
f(x)=3x^3 - 2x \quad\Rightarrow\quad f(x)\to +\infty\text{ lorsque }x\to+\infty.
$$

2.

$$
g(x)= -5x^4 + x \quad\Rightarrow\quad g(x)\to -\infty\text{ lorsque }x\to+\infty.
$$

---

## Limites en un point

Elles permettent de repérer :

1. les **asymptotes verticales**,
1. les **discontinuités**.

Exemple :

$$
\frac{1}{x} \quad\Rightarrow\quad \lim_{x\to 0^+}=+\infty,\quad \lim_{x\to 0^-}=-\infty.
$$

→ On dit que (x=0) est une **asymptote verticale**.

---

# Asymptotes

## Asymptote verticale

Si :

$$
\lim_{x\to a^\pm} f(x)=\pm\infty
$$

alors (x=a) est une **asymptote verticale**.

---

## Asymptote horizontale

Si :

$$
\lim_{x\to\pm\infty} f(x)=L
$$

alors (y=L) est une **asymptote horizontale**.

Exemple :

$$
f(x)=2 + \frac{1}{x}
\Rightarrow y=2.
$$

---

## Lire les limites sur une courbe

![Deux branches de la fonction 1+1/(x-1), séparées par l'asymptote verticale x=1 et se rapprochant de l'asymptote horizontale y=1.](figures/limites-asymptotes.svg)

Comparer les deux limites latérales au point interdit et les limites à l'infini.

---

## Asymptote oblique

Si :

$$
\lim_{x\to\infty} \big(f(x) - (ax+b)\big)=0
$$

alors (ax+b) est une asymptote oblique.

Exemple :

$$
f(x)=x + \frac{2}{x} \quad\Rightarrow\quad \text{asymptote } y=x.
$$

---

Pour une fonction `f(x)`, on recherche une asymptote oblique de la forme :

$$
y = ax + b.
$$

---

## **Calculer la pente (a)**

$$
a = \lim_{x\to+\infty} \frac{f(x)}{x}
$$

1. Si cette limite existe et est **finie**, il y a potentiellement une asymptote oblique.
1. Si (a = 0) → asymptote horizontale.
1. Si la limite diverge → **pas d'asymptote**.

---

## **Calculer l'ordonnée à l'origine (b)**

$$
b = \lim_{x\to+\infty} \big(f(x) - ax\big)
$$

Si (b) existe et est finite:
  $$
  y = ax + b \text{ est une asymptote oblique}
  $$

---

## **Exemple rapide**

Considérons :
$$
f(x)=\frac{x^2 + 3x - 1}{x}
= x + 3 - \frac{1}{x}
$$

Alors :

1.

$$
a=\lim_{x\to+\infty} \frac{f(x)}{x} = 1
$$

---

2.

$$
b=\lim_{x\to+\infty} (f(x) - x) = 3
$$

**Asymptote oblique :**

$$
y = x + 3
$$

![La courbe de f(x)=x+3-1/x se rapproche de la droite pointillée y=x+3 lorsque x tend vers plus ou moins l’infini. La droite verticale x=0 est aussi une asymptote.](figures/fonctions-asymptote-oblique.svg)

La différence vaut $f(x)-(x+3)=-\frac1x$ : elle tend vers $0$ aux deux infinis. Pour $x<0$, elle est positive : la courbe est au-dessus de son asymptote. Pour $x>0$, elle est négative : la courbe est en dessous.

---

# Continuité d'une fonction

Une fonction est continue en un point (a) si :

$$
\lim_{x\to a} f(x) = f(a).
$$

Cas typiques de non-continuité :

* saut (fonction par morceaux mal raccordée),
* point isolé,
* asymptote verticale.

---

# Fonctions définies par morceaux

Très important en data science (ReLU, Huber, fonctions coûts).

## Exemple :

$$
f(x)=
\begin{cases}
x + 2 & x < 0 \\
x^2  & x \ge 0
\end{cases}
$$

![Dans un repère orthonormé, la branche x+2 arrive au point ouvert (0,2) et la branche x² passe par le point plein (0,0), placé à l’origine.](figures/fonction-par-morceaux.svg)

Le dessin rend visible le rôle des conditions : à $x=0$, la valeur $2$ est exclue de la première branche et la valeur $0$ est incluse dans la seconde. On peut ainsi vérifier la continuité avant d'étudier la dérivabilité.

---

Questions classiques :

1. La fonction est-elle continue ?
2. Est-elle dérivable ?
3. Étudier ses variations.

Ce type de fonction aide à comprendre :

1. les "kinks" d'une fonction,
1. les dérivées nulles ou non-existantes,
1. les comportements mixtes.

---

#  Tangente à une courbe

Lorsqu'on connaît la dérivée `f'(a)`, l'équation de la tangente à la courbe en (x=a) est :

$$
y = f(a) + f'(a)(x-a).
$$

Exemple :

Pour 

$$
f(x)=x^2
$$

tangente en (x=1) :

$$
f(1)=1,\quad f'(1)=2
$$

$$
y = 1 + 2(x-1).
$$

Cette formule sera utilisée plus tard pour l'**approximation linéaire**.

![À gauche, la courbe de x² et sa tangente au point d'abscisse 1. À droite, la dérivée 2x donne la pente de la tangente en chaque point.](figures/derivee-tangente.svg)

À $x=1$, la courbe passe par $(1,1)$ et la pente vaut $f'(1)=2$. La tangente est donc $y=1+2(x-1)$.

---


# **Étude de fonction avec NumPy et Matplotlib**

Même si l'étude de fonction est théorique, les outils numériques sont très utiles pour :

1. visualiser les variations,
1. comprendre la convexité,
1. identifier maxima et minima,
1. comparer dérivée analytique et dérivée numérique.

Pour cela, on utilise :

---

### **Fonctions NumPy utiles**

| Fonction                          | Rôle                                          |
| --------------------------------- | --------------------------------------------- |
| `np.linspace(a, b, n)`            | Crée un vecteur de n points entre a et b      |
| `np.diff(y) / np.diff(x)`         | Taux de variation entre deux points voisins  |
| `np.gradient(y, x)`               | Approximation de la dérivée en chaque point  |
| `np.sin(x), np.exp(x), np.log(x)` | Fonctions usuelles                            |
| `x**2, x**3`                      | Puissances rapides                            |
| `np.where(condition)`             | Sélection d'indices                           |

----

### **Fonctions Matplotlib utiles**

| Fonction                    | Rôle                                 |
| --------------------------- | ------------------------------------ |
| `plt.plot(x, y)`            | Tracer une courbe                    |
| `plt.axhline(0)`            | Ligne horizontale (repère pour f'=0) |
| `plt.grid()`                | Grille                               |
| `plt.legend()`              | Légende                              |
| `plt.figure(figsize=(...))` | Taille du graphique                  |

---

# **Méthode générale (numérique) d'étude de fonction**

Pour une fonction ( f(x) ) sur un intervalle ([a,b]), on peut :

### **1. Créer un échantillon de points :**

```python
x = np.linspace(a, b, 400)
```

### **2. Calculer la fonction :**

```python
f = x**3 - 3*x  # exemple
```

---

### **3. Calculer la dérivée numérique :**

```python
f1 = np.gradient(f, x)
```

### **4. Calculer la dérivée seconde :**

```python
f2 = np.gradient(f1, x)
```

Voir un exemple complet à tester dans un Notebook
[code Numpy](https://github.com/Antoine07/maths/blob/main/Examples/mes_tests.ipynb)

---

# **Méthode de dichotomie**

La **méthode de dichotomie** permet de trouver numériquement une solution de :

$$
f(x) = 0
$$

Elle s'applique lorsque $f$ est continue sur $[a,b]$ et que ses valeurs aux bornes sont de signes opposés :

$$
f(a)\cdot f(b) < 0.
$$

La continuité et le changement de signe garantissent au moins une racine dans l'intervalle. Si la fonction est aussi strictement monotone, cette racine est unique.

---

# 🔎 **Principe**

1. Choisir un intervalle ([a,b]) où le signe change.
2. Calculer le milieu :
   $$
   m = \frac{a+b}{2}
   $$
3. Si $f(m)=0$, on a trouvé une racine. Sinon, si $f(a)$ et $f(m)$ sont de signes contraires, conserver $[a,m]$.
4. Dans l'autre cas, conserver $[m,b]$ : $f(m)$ et $f(b)$ sont alors de signes contraires.
5. Répéter jusqu'à obtenir la précision voulue.

L'intervalle se **réduit de moitié** à chaque étape. Après $n$ étapes, sa longueur vaut $(b-a)/2^n$. On peut ainsi encadrer une racine à la précision voulue. Si plusieurs racines se trouvent dans l'intervalle, la méthode en approche une, sans garantir laquelle.

---

#  **Exemple**

On cherche la solution de :

$$
f(x)=x^2 - 2 = 0
$$

Les solutions exactes sont 

$$
\pm \sqrt{2}
$$

La méthode dichotomique permet d'approcher la solution avec une erreur epsilon.

---

## Exercice 

Trouvez, à l'aide de la méthode par dicothomie, une valeur approchée de :

$$
\sqrt{2}
$$

---

# TP Saturation numérique

[Saturation numérique](https://antoine07.github.io/maths-data/pratique/Derivation/TPs/01_TP_saturation_numerique.html)

---

# Exercice facultatif — Étude numérique avec NumPy

Étudier numériquement la fonction :

$$
f(x) = x^4 - 2x^2 + 3
$$

Travail demandé :

1. Générer un vecteur `x` entre –3 et 3.
2. Calculer `f(x)`, puis sa dérivée `f'(x)` avec `np.gradient`.
3. Tracer les deux courbes.
4. Repérer graphiquement :

1. les extremums,
1. les intervalles où f croît / décroît.

---

## [Retour au plan](https://antoine07.github.io/maths/)
