# ✅ **Correction Exercice 1**

### Fonction :

$$
f(x) = x^3 - 3x.
$$

---

## **1. Calcul de ( f'(x) )**

$$
f'(x) = 3x^2 - 3.
$$

---

## **2. Calcul de ( f''(x) )**

$$
f''(x) = 6x.
$$

---

## **3. Signe de ( f''(x) )**

* ( f''(x) > 0 ) si ( x > 0 ).
  → la pente **augmente**, courbure **vers le haut** (∪), ( f ) est **convexe**.

* ( f''(x) < 0 ) si ( x < 0 ).
  → la pente **diminue**, courbure **vers le bas** (∩), ( f ) est **concave**.

* ( f''(x) = 0 ) en ( x = 0 ).
  → point **d'inflexion** (la courbure change de signe).

---

## **4. Interprétation : évolution de la pente**

* Pour ( x<0 ) : la pente baisse → la courbe forme un **dôme**.
* Pour ( x>0 ) : la pente augmente → la courbe forme une **cuvette**.
* À ( x=0 ) : la pente passe progressivement d'un comportement concave à convexe.

👉 **Graphiquement, c'est une courbe en S classique.**

---


# **Correction Exercice 2**

### Fonction :

$$
g(x) = -x^2 + 4x.
$$

---

## **1. Calcul de ( g'(x) )**

$$
g'(x) = -2x + 4.
$$

---

## **2. Calcul de ( g''(x) )**

$$
g''(x) = -2.
$$

---

## **3. Étude de l'évolution de la pente**

Comme
$$
g''(x) = -2 < 0 \quad \text{pour tout } x,
$$
cela signifie :

* la pente **diminue en permanence** sur ℝ,
* le graphe est **toujours courbé vers le bas** (∩).

---

## **4. Forme du graphe**

$$
g'' < 0 \Rightarrow \text{fonction concave sur ℝ}.
$$

Le graphe est donc un **dôme** (parabole renversée).

---

## **5. Nature du sommet**

On trouve le point critique :
$$
g'(x) = -2x + 4 = 0 \Rightarrow x = 2.
$$

La valeur correspondante :
$$
g(2) = -(2)^2 + 4(2) = -4 + 8 = 4.
$$

Et comme
$$
g''(x) = -2 < 0,
$$
le point ((2,4)) est un **maximum**.

---

# 🎯 **Synthèse des deux exercices**

| Fonction     | (f'')            | Pente                               | Courbure  | Point notable    |
| ------------ | ---------------- | ----------------------------------- | --------- | ---------------- |
| ( x^3 - 3x ) | change de signe  | augmente à droite, diminue à gauche | S (∩ → ∪) | inflexion en 0   |
| (-x^2 + 4x)  | toujours négatif | diminue                             | ∩ dôme    | maximum en (2,4) |

---

# **Correction de l'exercice**

On étudie :
$$
f(x) = x^4 - 2x^2 + 3.
$$

---

## **1. Calcul de ( f'(x) )**

$$
f'(x) = 4x^3 - 4x.
$$

---

## **2. Calcul de ( f''(x) )**

$$
f''(x) = 12x^2 - 4.
$$

On peut factoriser :
$$
f''(x) = 4(3x^2 - 1).
$$

---

## **3. Signe de ( f''(x) )**

Résolvons :
$$
f''(x) = 0 \quad \Leftrightarrow \quad 3x^2 - 1 = 0.
$$

$$
3x^2 = 1 \quad\Rightarrow\quad x^2 = \frac{1}{3} \quad\Rightarrow\quad x = \pm \frac{1}{\sqrt{3}}.
$$

On étudie le signe de ( f'' ) par intervalles :

* Pour $$(|x| > \frac{1}{\sqrt{3}})$$ :
  $$(3x^2 - 1 > 0 \Rightarrow f''(x) > 0)$$.

* Pour $$(|x| < \frac{1}{\sqrt{3}})$$ :
  $$(3x^2 - 1 < 0 \Rightarrow f''(x) < 0)$$.

---

## **4. Conclusion : convexité / concavité**

* **Convexe** (∪) sur :
$$
  ]-\infty,\ -\tfrac{1}{\sqrt{3}}[ \quad \cup \quad ]\tfrac{1}{\sqrt{3}},\ +\infty[
$$

* **Concave** (∩) sur :
$$
  ] -\tfrac{1}{\sqrt{3}},\ \tfrac{1}{\sqrt{3}} [
$$

---

## **5. Points d'inflexion**

Il y a un changement de signe de ( f'' ) en
$$
x = -\tfrac{1}{\sqrt{3}} \quad \text{et} \quad x = \tfrac{1}{\sqrt{3}}.
$$

Donc ce sont des **points d'inflexion**.

Leurs ordonnées sont :
$$
f!\left(\pm \tfrac{1}{\sqrt{3}}\right)
= \left(\tfrac{1}{3^2}\right) - 2\left(\tfrac{1}{3}\right) + 3
= \tfrac{1}{9} - \tfrac{2}{3} + 3
= \tfrac{1}{9} - \tfrac{6}{9} + \tfrac{27}{9}
= \tfrac{22}{9}.
$$

Donc les points d'inflexion sont :
$$
\left(-\tfrac{1}{\sqrt{3}},\ \tfrac{22}{9}\right)
\quad\text{et}\quad
\left(\tfrac{1}{\sqrt{3}},\ \tfrac{22}{9}\right).
$$

---

# Résumé 

| Intervalle                     | Signe de ( f'' ) | Nature      |
| ------------------------------ | ---------------- | ----------- |
| $$]-\infty,\ -1/\sqrt{3}[$$    | ( >0 )           | Convexe (∪) |
| $$]-1/\sqrt{3},\ 1/\sqrt{3}[$$ | ( <0 )           | Concave (∩) |
| $$]1/\sqrt{3},\ +\infty[$$     | ( >0 )          | Convexe (∪) |

Points d'inflexion :  $$x = \pm 1/\sqrt{3}$$
