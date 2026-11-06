#  **Correction complète**

La fonction de perte est :

[
L(x,y)=x^4 - 2x^2 + y^2 - 3xy.
]

---

# **1. Dérivées partielles**

### Par rapport à (x)

[
L_x = 4x^3 - 4x - 3y
]

### Par rapport à (y)

[
L_y = 2y - 3x
]

---

# **2. Points critiques**

On résout :

[
L_x = 0,\qquad L_y = 0.
]

### De (L_y = 0) :

[
2y - 3x = 0
\quad\Rightarrow\quad
y = \frac{3}{2}x
]

On substitue dans (L_x = 0) :

[
4x^3 - 4x - 3\left(\frac{3}{2}x\right)=0
]

[
4x^3 - 4x - \frac{9}{2}x = 0
]

[
4x^3 - \left(4 + \frac{9}{2}\right)x = 0
]

[
4x^3 - \frac{17}{2}x = 0
]

Factorisons :

[
x\left(4x^2 - \frac{17}{2}\right)=0
]

Donc :

1. (x = 0)
2. (4x^2 = \frac{17}{2})
   [
   x^2 = \frac{17}{8}
   \quad\Rightarrow\quad
   x = \pm \sqrt{\frac{17}{8}}
   ]

Correspondance des y :

[
y = \frac{3}{2}x
]

### ✔ Points critiques :

[
(0,0)
]

[
\left(\sqrt{\frac{17}{8}},; \frac{3}{2}\sqrt{\frac{17}{8}}\right)
]

[
\left(-\sqrt{\frac{17}{8}},; -\frac{3}{2}\sqrt{\frac{17}{8}}\right)
]

---

# **3. Hessienne**

Calculons les dérivées secondes.

[
L_{xx} = 12x^2 - 4, \qquad
L_{yy} = 2, \qquad
L_{xy} = L_{yx} = -3
]

Hessienne :

[
H(x,y)=
\begin{pmatrix}
12x^2 - 4 & -3 \
-3 & 2
\end{pmatrix}
]

---

# **4. Évaluation du Hessien aux points critiques**

---

## 🔹 **Cas 1 : ((0,0))**

[
H(0,0)=
\begin{pmatrix}
-4 & -3 \
-3 & 2
\end{pmatrix}
]

Déterminant :

[
\det(H)=(-4)(2) - (-3)^2 = -8 - 9 = -17 < 0
]

➡️ **Hessien indéfini**
➡️ **point-selle**

---

## 🔹 **Cas 2 et 3 : (x=\pm\sqrt{17/8}), (y=\frac{3}{2}x)**

Calculons d’abord (12x^2 - 4) :

[
x^2 = \frac{17}{8}
]

[
12x^2 - 4 = 12\left(\frac{17}{8}\right) - 4
= \frac{204}{8} - 4
= 25.5 - 4
= 21.5
]

Le Hessien vaut donc :

[
H=
\begin{pmatrix}
21.5 & -3 \
-3 & 2
\end{pmatrix}
]

Déterminant :

[
\det(H)=21.5\cdot 2 - 9 = 43 - 9 = 34 > 0
]

Et :

[
L_{xx}=21.5 > 0
]

➡️ Hessien **défini positif**
➡️ **minimum local strict**

Cela vaut pour les deux points symétriques (car la Hessienne dépend seulement de (x^2)).

---

# 🎯 **Conclusion sur la classification**

| Point critique                                                       | Nature             |
| -------------------------------------------------------------------- | ------------------ |
| ((0,0))                                                              | **Point-selle**    |
| (\left(\sqrt{\frac{17}{8}},;\frac{3}{2}\sqrt{\frac{17}{8}}\right))   | **Minimum strict** |
| (\left(-\sqrt{\frac{17}{8}},;-\frac{3}{2}\sqrt{\frac{17}{8}}\right)) | **Minimum strict** |

---

# 🚀 **6. Interprétation machine learning**

### **a) Pourquoi la descente de gradient ralentit-elle dans un point-selle ?**

Parce que :

* le gradient devient très petit,
* mais la fonction ne se comporte pas comme un minimum,
* certaines directions montent, d’autres descendent.

Le modèle peut **stagner longtemps** sans progresser.

---

### **b) Pourquoi les minima non stricts posent problème ?**

Car la surface est plate ou très mal conditionnée :

* le gradient est faible ou instable,
* les mises à jour deviennent petites ou oscillent,
* la convergence est lente.

---

### **c) Zones dangereuses pour un algorithme ML**

Ici :

* autour de ((0,0)), le Hessien est **indéfini** → **point-selle → danger**
* les régions où (x\approx 0) créent des vallées plates → ralentissement majeur
