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

# Démo 1 · Le crible d’Ératosthène

**Objectif :** trouver tous les nombres premiers jusqu'à une borne, puis justifier la méthode.

Un entier naturel est **premier** s'il est supérieur ou égal à 2 et possède exactement deux diviseurs positifs : 1 et lui-même.

- 7 est premier ; 12 ne l'est pas, car $12 = 3 \times 4$.
- **1 n'est pas premier** : il n'a qu'un seul diviseur positif.
- Un **multiple** de $p$ s'écrit $kp$, où $k$ est un entier.

Le crible garde un nombre premier et élimine ses multiples plus grands que lui. On recommence avec le prochain nombre non éliminé.

---

# Diviseurs premiers et diviseurs premiers stricts

Un **diviseur premier** de $N$ est un nombre premier qui divise $N$. Il est **strict** s'il est strictement inférieur à $N$.

Pour **7** :

- Les diviseurs positifs sont $\{1,7\}$.
- Les diviseurs premiers sont $\{7\}$.
- Les diviseurs premiers stricts forment l'ensemble vide : $\varnothing$.

Le mot **premiers** est essentiel : 1 est un diviseur strict de 7, mais il n'est pas premier.

**Notation :** $\varnothing$ et $\{\}$ désignent l'ensemble vide. L'ensemble $\{\varnothing\}$ contient un élément, qui est lui-même l'ensemble vide.

---

# À faire · Passer les entiers de 1 à 30 au crible

**Prérequis :** multiplication et divisibilité.

Écrire les nombres de 1 à 30, puis barrer 1.

1. Entourer 2 et barrer ses multiples à partir de $2^2 = 4$.
2. Entourer le prochain nombre non barré : 3. Barrer ses multiples à partir de $3^2 = 9$.
3. Recommencer avec 5, à partir de $5^2 = 25$.
4. Lister les nombres restants. Pourquoi peut-on arrêter avant de traiter 7 ?

**Livrable :** une grille annotée, la liste obtenue et une phrase justifiant l'arrêt. Ne pas barrer le nombre premier lui-même.

<details><summary>Indice · Chercher un petit facteur</summary>

Si un nombre s'écrit $ab$ et que ses deux facteurs sont strictement supérieurs à $\sqrt{30}$, leur produit dépasse 30. Un nombre non premier entre 2 et 30 possède donc un facteur premier parmi 2, 3 et 5.

</details>

<details><summary>Correction · Les nombres conservés et la preuve de l'arrêt</summary>

On obtient **2, 3, 5, 7, 11, 13, 17, 19, 23 et 29**.

![Grille du crible jusqu'à 30 : 1 est exclu ; les dix nombres premiers sont entourés en vert ; les autres nombres sont barrés.](images/crible-eratosthene.svg)

**Démonstration par contradiction.** Supposons qu'un nombre composé $n \leq 30$ soit encore non barré après le passage de 2, 3 et 5.

Il possède un facteur premier $p$ inférieur ou égal à $\sqrt{n}$. On a donc :

$$
p \leq \sqrt{n} \leq \sqrt{30} \approx 5{,}477 < 6.
$$

Comme $p$ est un entier premier, il vaut nécessairement **2, 3 ou 5**.

Mais $n$ est alors un multiple de l'un de ces trois nombres. Puisque $n$ est composé, il est strictement supérieur à ce facteur premier : **il aurait donc déjà été barré**.

C'est une contradiction avec notre supposition. **Aucun nombre composé ne peut rester : tous les nombres conservés sont premiers.**

Le prochain nombre non barré est 7 et $7^2 = 49 > 30$ : on peut donc arrêter le crible après le passage de 5.

</details>

---

# Pourquoi le crible fonctionne-t-il ?

Un entier **composé** est un entier supérieur ou égal à 2 qui n'est pas premier. Il s'écrit $n = ab$ avec $a,b \geq 2$.

**Un petit facteur suffit.** On appelle $a$ le plus petit des deux facteurs, donc $2 \leq a \leq b$. Alors $a^2 \leq ab = n$, d'où $a \leq \sqrt{n}$. Ce facteur $a$ possède lui-même un diviseur premier $p \leq a \leq \sqrt{n}$.

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

# Reconnaître un nombre premier

Pour un entier $N \geq 2$, notons :

$$
P_N=\{p\mid p\text{ est premier},\ p\mid N,\ p<N\}.
$$

$p\mid N$ signifie que $p$ divise $N$, sans reste. $P_N$ est donc l'ensemble des **diviseurs premiers stricts** de $N$.

$$
N\text{ est premier}\quad\Longleftrightarrow\quad P_N=\varnothing.
$$

**Exemples :** $P_7=\varnothing$, tandis que $P_{12}=\{2,3\}$. La condition $N\geq2$ exclut 1, qui n'est pas premier malgré l'absence de diviseur premier strict.

<details><summary>Correction · Pourquoi ce critère fonctionne-t-il ?</summary>

Si $N$ est premier, ses seuls diviseurs positifs sont 1 et $N$. Aucun n'est un diviseur premier strict : $P_N=\varnothing$.

Réciproquement, supposons $P_N=\varnothing$. Si $N$ était composé, il s'écrirait $N=ab$ avec $2\leq a\leq b<N$. L'entier $a$ posséderait un facteur premier $p\leq a<N$. Ce nombre $p$ diviserait aussi $N$, donc appartiendrait à $P_N$ : contradiction. Ainsi, $N$ est premier.

</details>

---

# Réduire la recherche à la racine carrée

Tout nombre composé $N$ possède un diviseur premier $p\leq\sqrt N$, comme nous l'avons démontré pour justifier le crible.

**Il suffit donc de vérifier qu'aucun diviseur premier inférieur ou égal à $\sqrt N$ ne divise $N$.**

<details><summary>Correction · La contradiction sous la borne</summary>

Supposons qu'aucun tel diviseur n'existe, mais que $N$ soit composé. Écrivons $N=ab$ avec $2\leq a\leq b$.

Alors $a^2\leq ab=N$, donc $a\leq\sqrt N$. Comme $a\geq2$, il possède un facteur premier $p\leq a$. Ce facteur divise aussi $N$, avec $p\leq\sqrt N$ : contradiction.

</details>

Pour programmer ce contrôle simplement, nous testerons **tous les entiers de 2 à $\lfloor\sqrt N\rfloor$**, sans construire une liste préalable de nombres premiers. Le symbole $\lfloor\sqrt N\rfloor$ désigne la partie entière de la racine.

La borne est **incluse** : pour 49, il faut tester 7.

---

# Tester la primalité en Python

```python
def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print(est_premier(7), est_premier(49), est_premier(101))
```

**Lecture et exécution :** pour un entier `n`, `d` parcourt les diviseurs candidats ; `%` calcule le reste. Un reste nul suffit à conclure que `n` est composé. Sans diviseur sous la borne, la fonction renvoie `True`. Résultat : `True False True`.

**Erreur fréquente :** écrire `d * d < n` au lieu de `<=` ferait manquer le facteur 7 de 49. La comparaison de carrés utilise uniquement des entiers.

---

# Mesurer le travail : combien de tests ?

Nous comptons les opérations `n % d`, c'est-à-dire les **tests de divisibilité**.

| Entier $N$ | Résultat | Nombre de tests |
|---|---|---|
| 7 | Premier | 1 : tester 2 |
| 49 | Composé | 6 : tester 2 à 7 |
| 101 | Premier | 9 : tester 2 à 10 |
| 1009 | Premier | 30 : tester 2 à 31 |

Pour $N\geq2$, on effectue au plus $\lfloor\sqrt N\rfloor-1$ tests. Cette borne est atteinte lorsque $N$ est premier ; un diviseur peut permettre de s'arrêter plus tôt.

**Complexité : $O(\sqrt N)$ tests dans le pire cas.** La mémoire auxiliaire utilise un nombre constant de variables, soit $O(1)$ dans ce modèle.

Pour des nombres premiers de taille comparable, multiplier $N$ par environ 100 multiplie le nombre de tests par environ 10. Cette estimation compte les tests ; elle ne donne pas une durée d'exécution garantie.

---

# À faire · Vérifier l'algorithme et sa complexité

**Objectif :** relier la preuve, les cas limites et le nombre d'opérations.

1. Prédire les réponses pour 1, 2, 7, 49 et 121.
2. Ajouter un compteur incrémenté juste avant chaque calcul de `n % d`.
3. Vérifier les nombres de tests du tableau et expliquer pourquoi tester tous les entiers n'impose pas de chercher d'abord les nombres premiers.

**Livrable :** réponses, compteur et justification de la borne. **Réussite :** 1 est refusé, 2 est accepté sans test, et les carrés 49 et 121 sont refusés.

<details><summary>Correction · Résultats et compteur</summary>

Les réponses sont `False`, `True`, `True`, `False`, `False`. Les nombres de tests sont respectivement **0, 0, 1, 6 et 10**.

Le compteur doit augmenter à chaque test, y compris celui qui trouve un diviseur. Pour 121, le dernier candidat est 11 : le test de la racine est indispensable.

Tester tous les entiers jusqu'à la racine inclut tous les nombres premiers de cet intervalle. Si aucun de ces entiers ne divise $N$, aucun nombre premier de cet intervalle ne le divise non plus : le critère démontré s'applique.

Le [programme téléchargeable](exemples/revision/primalite.py) fournit `est_premier` et `analyser_primalite`, qui renvoie la réponse et le compteur. Il affiche aussi une mesure de temps indicative pour comparer les exécutions ; le nombre de tests justifie la complexité, les chronométrages dépendent de la machine.

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
