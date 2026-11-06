---
marp: true
theme: default
paginate: true
class: lead
---

# Révision d’algèbre : calculs essentiels

![Un rectangle découpé en quatre aires illustre le passage entre (x + 2)(x + 3) et x² + 5x + 6, en développant ou en factorisant.](images/revision-algebre.svg)

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

## Problème — Compter les occasions

La moitié des années d'un horizon reste-t-elle la moitié des rencontres ?

Appliquer les produits et pourcentages à une situation fictive, puis construire une grille de points dont chaque unité est explicite.

[Problème 1 : la moitié des années, combien de rencontres ?](../Tps/Tail_End/01_rencontres.md)

En complément court : [où sont passées mes dix minutes ?](../Tps/Paradoxes/01_dix_minutes.md), pour travailler les conversions et distinguer temps cumulé et temps disponible d'un seul bloc.

---

## [Retour au plan](https://antoine07.github.io/maths/)
