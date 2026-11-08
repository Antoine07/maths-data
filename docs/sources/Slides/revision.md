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

# Démo 1 · Le crible d’Ératosthène

**Objectif :** trouver tous les nombres premiers jusqu'à une borne, puis justifier la méthode.

Un entier naturel est **premier** s'il est supérieur ou égal à 2 et possède exactement deux diviseurs positifs : 1 et lui-même.

- 7 est premier ; 12 ne l'est pas, car $12 = 3 \times 4$.
- **1 n'est pas premier** : il n'a qu'un seul diviseur positif.
- Un **multiple** de $p$ s'écrit $kp$, où $k$ est un entier.

Le crible garde un nombre premier et élimine ses multiples plus grands que lui. On recommence avec le prochain nombre non éliminé.

---

# À faire · Passer les entiers de 1 à 30 au crible

**Prérequis :** multiplication et divisibilité. **Durée :** 10 à 15 minutes.

Écrire les nombres de 1 à 30, puis barrer 1.

1. Entourer 2 et barrer ses multiples à partir de $2^2 = 4$.
2. Entourer le prochain nombre non barré : 3. Barrer ses multiples à partir de $3^2 = 9$.
3. Recommencer avec 5, à partir de $5^2 = 25$.
4. Lister les nombres restants. Pourquoi peut-on arrêter avant de traiter 7 ?

**Livrable :** une grille annotée, la liste obtenue et une phrase justifiant l'arrêt. Ne pas barrer le nombre premier lui-même.

<details><summary>Indice · Chercher un petit facteur</summary>

Si un nombre s'écrit $ab$ et que ses deux facteurs sont strictement supérieurs à $\sqrt{30}$, leur produit dépasse 30. Un nombre non premier entre 2 et 30 possède donc un facteur premier parmi 2, 3 et 5.

</details>

<details><summary>Correction · Les nombres conservés</summary>

On obtient **2, 3, 5, 7, 11, 13, 17, 19, 23 et 29**.

![Grille du crible jusqu'à 30 : 1 est exclu ; les dix nombres premiers sont entourés en vert ; les autres nombres sont barrés.](images/crible-eratosthene.svg)

Après 5, le prochain nombre non barré est 7 et $7^2 = 49 > 30$. Tous les nombres composés jusqu'à 30 ont déjà été éliminés.

</details>

---

# Pourquoi le crible fonctionne-t-il ?

Un entier **composé** est un entier supérieur ou égal à 2 qui n'est pas premier. Il s'écrit $n = ab$ avec $a,b \geq 2$.

**Un petit facteur suffit.** Si $a > \sqrt{n}$ et $b > \sqrt{n}$, alors $ab > n$ : impossible. Un facteur est donc inférieur ou égal à $\sqrt{n}$ ; il possède lui-même un diviseur premier inférieur ou égal à $\sqrt{n}$.

**Aucun premier n'est barré.** Les nombres éliminés sont des multiples $kp$ avec $k \geq 2$ : ils sont composés.

**Aucun composé ne reste.** Tout composé $n \leq N$ possède un facteur premier inférieur ou égal à $\sqrt{N}$. Traiter ces facteurs suffit à l'éliminer.

**Pourquoi commencer à $p^2$ ?** Les multiples $2p, 3p, \ldots, (p-1)p$ ont déjà été barrés par un facteur premier plus petit que $p$.

---

# Le crible · Du raisonnement au code

**Entrée :** un entier naturel `n`. **Sortie :** la liste des nombres premiers inférieurs ou égaux à `n`.

```python
def crible(n):
    if n < 2:
        return []
    premier = [True] * (n + 1)
    premier[0] = premier[1] = False
    p = 2
    while p * p <= n:
        if premier[p]:
            for multiple in range(p * p, n + 1, p):
                premier[multiple] = False
        p += 1
    return [i for i in range(2, n + 1) if premier[i]]

print(crible(30))
```

`premier[i]` indique si `i` est encore candidat ; `p` parcourt les facteurs possibles. Le pas `p` du `range` parcourt les multiples ; `n + 1` permet d'inclure la borne `n`.

**Avant d'exécuter :** prédire les résultats pour 1, 2 et 30. Quel nombre serait oublié avec `range(..., n, p)` lorsque `n` est un carré de premier ?

<details><summary>Correction · Résultats et piège de la borne</summary>

`crible(1)` donne `[]`, `crible(2)` donne `[2]` et `crible(30)` donne `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`.

Avec une borne de fin `n` au lieu de `n + 1`, le multiple `n` n'est pas traité. Par exemple, 25 resterait candidat au passage de 5 : le programme le déclarerait premier à tort.

</details>

[Télécharger le programme Python](exemples/revision/crible.py).

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

**Prérequis :** mise en facteur commun et sens du mot « entier ». **Durée :** 15 à 20 minutes, dont une découverte de Lean.

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
