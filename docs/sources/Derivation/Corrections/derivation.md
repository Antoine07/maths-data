# Correction des exercices

# Exercice 1

Calculer les dérivées partielles :

a) $$f(x,y)=x^3+y^2$$

$$
f_x = 3x^2,\qquad f_y = 2y.
$$

b) $$g(x,y)=xy + 3x$$

$$
g_x = y + 3,\qquad g_y = x.
$$

c) $$h(x,y)=\sqrt{x^2+y^2}$$

$$
h_x = \frac{x}{\sqrt{x^2+y^2}},\qquad
h_y = \frac{y}{\sqrt{x^2+y^2}}.
$$

---

# Exercice 2

Calculer le gradient :

a) $$f(x,y)=x^2 - y$$

$$
\nabla f = (2x,,-1).
$$

b) $$g(x,y)=xy^2 - 3y$$

$$
g_x = y^2,\qquad g_y = 2xy - 3.
$$

$$
\nabla g = (y^2,;2xy-3).
$$

---

# Exercice 3

Trouver les points critiques.

## a) $$f(x,y)=x^2 + y^2 - 4x$$

Gradient :

$$
f_x = 2x - 4,\quad f_y = 2y.
$$

Point critique :

$$
2x-4=0 \Rightarrow x=2,\qquad 2y=0 \Rightarrow y=0.
$$

Point critique : ((2,0)).

Classification : déjà montrée précédemment → **minimum local**.

---

## b) $$g(x,y)=x^2 - y^2$$

$$
g_x=2x,\qquad g_y=-2y.
$$

Point critique :

$$
2x=0 \Rightarrow x=0,\qquad -2y=0 \Rightarrow y=0.
$$

Point critique : ((0,0)).

Hessienne :

$$
H=
\begin{pmatrix}
2 & 0\
0 & -2
\end{pmatrix}.
$$

$$
D = 2\cdot(-2) = -4 < 0.
$$

Conclusion : **point selle**.

---

# Exercice 4

Interpréter les dérivées partielles de :

$$
f(x,y)=3x + 2y.
$$

$$
f_x=3,\qquad f_y=2.
$$

Interprétation :

* augmenter (x) fait croître la fonction trois fois plus fortement qu’une variation de même amplitude sur (y),
* (x) a donc un impact **plus important** que (y) sur la valeur de (f).

---

# Correction des exercices du chapitre Hessienne

---

# Exercice 1

$$
f(x,y)=x^2 + xy + y^2.
$$

### 1) Gradient

$$
f_x = 2x + y,\qquad f_y = x + 2y.
$$

Point critique :

$$
2x+y=0,\quad x+2y=0.
$$

Résolution :

De (2x+y=0), on a (y = -2x).
Remplacer dans (x+2y=0) :

$$
x + 2(-2x)=0 \Rightarrow x - 4x = 0 \Rightarrow -3x = 0 \Rightarrow x=0.
$$

Donc (y=-2x=0).

Point critique : ((0,0)).

### 2) Hessienne

$$
f_{xx}=2,\quad f_{yy}=2,\quad f_{xy}=1.
$$

$$
H=
\begin{pmatrix}
2 & 1\
1 & 2
\end{pmatrix}.
$$

Déterminant :

$$
D = 2\cdot 2 - 1^2 = 4 - 1 = 3 > 0.
$$

Comme $$f_{xx} = 2 > 0$$, conclusion :

**Minimum local**.

---

# Exercice 2

$$
g(x,y)=x^3 - 3xy + y^3.
$$

### Gradient

$$
g_x=3x^2 - 3y,\qquad g_y=-3x + 3y^2.
$$

Point critique : résoudre

$$
3x^2 - 3y = 0,\qquad -3x + 3y^2 = 0.
$$

Simplification :

$$
x^2 = y,\qquad y^2 = x.
$$

On remplace :

(x^2 = y) dans (y^2 = x) :

$$
(x^2)^2 = x \Rightarrow x^4 = x \Rightarrow x(x^3 - 1)=0.
$$

Solutions :

1. (x=0 \Rightarrow y=0).
2. (x^3 = 1 \Rightarrow x=1) et donc (y=1).

Points critiques : ((0,0)) et ((1,1)).

Hessienne :

$$
g_{xx}=6x,\quad g_{yy}=6y,\quad g_{xy}=-3.
$$

### Au point (0,0)

$$
H=
\begin{pmatrix}
0 & -3\
-3 & 0
\end{pmatrix}.
$$

$$
D = 0\cdot 0 - (-3)^2 = -9 < 0.
$$

Donc : **point selle**.

---

### Au point (1,1)

$$
H=
\begin{pmatrix}
6 & -3\
-3 & 6
\end{pmatrix}.
$$

$$
D = 6\cdot 6 - (-3)^2 = 36 - 9 = 27 > 0.
$$

Comme (f_{xx}=6>0), on conclut :

**Minimum local**.

---

# Exercice 3

$$
h(x,y)=x^2 - 2x + y^4.
$$

### 1) Gradient

$$
h_x = 2x - 2,\qquad h_y = 4y^3.
$$

Point critique :

$$
2x-2=0 \Rightarrow x=1,
\qquad 4y^3=0 \Rightarrow y=0.
$$

Point critique : ((1,0)).

### 2) Hessienne

$$
h_{xx}=2,\quad h_{yy}=12y^2,\quad h_{xy}=0.
$$

Au point ((1,0)) :

$$
H=
\begin{pmatrix}
2 & 0\
0 & 0
\end{pmatrix}.
$$

$$
D = 2\cdot 0 - 0 = 0.
$$

Conclusion :
Le test est **inconclusif**.

(On peut montrer par ailleurs que c’est un minimum au sens partiel sur (x), mais plat dans la direction (y).)

---

# Exercice 4

$$
k(x,y)=x^2 - y^2 + 2x - 4y.
$$

### Gradient

$$
k_x = 2x + 2,\qquad k_y = -2y - 4.
$$

Point critique :

$$
2x+2=0 \Rightarrow x=-1, \qquad -2y-4=0 \Rightarrow y=-2.
$$

Point critique : ((-1,-2)).

### Hessienne

$$
k_{xx}=2,\quad k_{yy}=-2,\quad k_{xy}=0.
$$

$$
H=
\begin{pmatrix}
2 & 0\
0 & -2
\end{pmatrix}.
$$

Déterminant :

$$
D = 2\cdot(-2) = -4 < 0.
$$

Conclusion :

**point selle**.

---

Souhaites-tu maintenant :

* le même type d’exercices mais plus difficiles,
* un exercice d’application (économie, physique, data),
* ou la suite du chapitre (jacobienne, approximation linéaire, optimisation) ?
