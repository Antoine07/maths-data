
# Correction des exercices


# Exercice 1

Âges : 12, 15, 14, 13, 16, 15.

### 1. Moyenne

$$
\bar{x}=\frac{12 + 15 + 14 + 13 + 16 + 15}{6}
= \frac{85}{6} \approx 14.17.
$$

### 2. Médiane

On range les valeurs :

12, 13, 14, 15, 15, 16

Il y a 6 valeurs → médiane = moyenne des deux centrales :

$$
\text{Médiane}=\frac{14 + 15}{2} = 14.5.
$$

### 3. Écart-type

Moyenne $$\bar{x}\approx 14.17$$.

On calcule les écarts au carré :

$$(12 - 14.17)^2 = 4.71$$
$$(13 - 14.17)^2 = 1.37$$
$$(14 - 14.17)^2 = 0.03$$
$$(15 - 14.17)^2 = 0.69$$
$$(15 - 14.17)^2 = 0.69$$
$$(16 - 14.17)^2 = 3.36$$

Somme : (4.71+1.37+0.03+0.69+0.69+3.36 = 10.85)

Variance :

$$
\text{Var}=\frac{10.85}{6} \approx 1.81.
$$

Écart-type :

$$
\sigma = \sqrt{1.81} \approx 1.35.
$$

---


# Exercice 2

Table :

| X | 1 | 2 | 3 |
| - | - | - | - |
| Y | 2 | 4 | 5 |

Moyennes :

$$
\bar{x}= \frac{1+2+3}{3} = 2,
\qquad
\bar{y}= \frac{2+4+5}{3} = \frac{11}{3}.
$$

### 1. Covariance

$$
\mathrm{Cov}(X,Y)=\frac{1}{3}\sum (x_i - \bar{x})(y_i - \bar{y}).
$$

Calcul :

* Pour (x=1) et (y=2) :

((1-2)(2 - 11/3)=(-1)(-5/3)=5/3)

* Pour (x=2), (y=4) :

((2-2)(4 - 11/3)=0)

* Pour (x=3), (y=5) :

((3-2)(5 - 11/3)=(1)(4/3)=4/3)

Total :

$$
\frac{1}{3}\left(\frac{5}{3} + 0 + \frac{4}{3}\right)
= \frac{1}{3}\cdot \frac{9}{3}
= \frac{1}{3}\cdot 3 = 1.
$$

Covariance = **1**.

### 2. Corrélation

Écart-type de X :
$$
\sigma_X = \sqrt{\frac{(1-2)^2 + (2-2)^2 + (3-2)^2}{3}}
= \sqrt{\frac{1 + 0 + 1}{3}}
= \sqrt{\frac{2}{3}}.
$$

Écart-type de Y :
$$
\sigma_Y = \sqrt{\frac{(2-11/3)^2 + (4-11/3)^2 + (5-11/3)^2}{3}}
= \sqrt{\frac{25/9 + 1/9 + 16/9}{3}}
= \sqrt{\frac{42/9}{3}}
= \sqrt{\frac{42}{27}}
= \sqrt{\frac{14}{9}}
= \frac{\sqrt{14}}{3}.
$$

Corrélation :

$$
\rho = \frac{\mathrm{Cov}}{\sigma_X \sigma_Y}
= \frac{1}{\sqrt{2/3}\cdot (\sqrt{14}/3)}
= \frac{3}{\sqrt{28/3}}
= \frac{3}{\sqrt{\frac{28}{3}}}
= \frac{3\sqrt{3}}{\sqrt{28}}
\approx 0.98.
$$

Très forte corrélation positive.

---


# Exercice 3

Tailles : 160, 170, 175, 150, 165.

### 1. Effectifs

| Taille   | 150 | 160 | 165 | 170 | 175 |
| -------- | --- | --- | --- | --- | --- |
| Effectif | 1   | 1   | 1   | 1   | 1   |

Toutes les valeurs sont uniques.

---

### 2. Moyenne

Somme = (150 + 160 + 165 + 170 + 175 = 820).

$$
\bar{x} = \frac{820}{5} = 164.
$$

Écart-type :

Écarts au carré :

$$(150 – 164)^2 = 196$$
$$(160 – 164)^2 = 16$$
$$(165 – 164)^2 = 1$$
$$(170 – 164)^2 = 36$$
$$(175 – 164)^2 = 121$$

Somme = (196 + 16 + 1 + 36 + 121 = 370).

Variance :

$$
\text{Var}=\frac{370}{5}=74.
$$

Écart-type :

$$
\sigma = \sqrt{74}\approx 8.60.
$$

---

### 3. Quartile (Q_1)

Données rangées :
150, 160, 165, 170, 175.

Il y a 5 valeurs → (Q_1) = 2ᵉ valeur = **160**.

---

# Exercice 4

Interprétation de la corrélation :

### a) $$\rho = 0.92$$

Relation linéaire **très forte et positive** : les deux variables augmentent ensemble presque parfaitement.

### b) $$\rho = -0.45$$

Relation linéaire **modérément négative** : quand l'une augmente, l'autre tend à diminuer mais ce n’est pas strict.

### c) $$\rho = 0$$

**Aucune relation linéaire détectable** : les variables varient de manière indépendante (ou relation non linéaire).


## Remarque sur la recherche des quartiles

# 1. Méthode "lycée" (quartile = valeur de rang 25 %)

On prend le rang :

$$
r = \frac{n+1}{4} = \frac{5+1}{4} = \frac{6}{4} = 1.5.
$$

Donc (Q_1) est **entre la 1ʳᵉ et la 2ᵉ valeur** :

Données rangées :
150, 160, 165, 170, 175

1ʳᵉ valeur = 150
2ᵉ valeur = 160

Interpolation linéaire :

$$
Q_1 = 150 + 0.5(160-150) = 155.
$$

Donc **Q1 = 155**.

---

# 2. Méthode "partition" (très utilisée en lycée)

On coupe :

* partie basse : 150, 160
* partie haute : 170, 175
* médiane : 165 (point du milieu)

Dans ce cas, (Q_1) = médiane de la partie basse :

$$
Q_1 = \frac{150+160}{2} = 155.
$$

---

# Conclusion

**Le quartile Q1 = 155**, pas 160.
Merci d’avoir pointé cela — la correction doit utiliser **155**, quelle que soit la méthode standard.

