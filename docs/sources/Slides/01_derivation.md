---
marp: true
theme: default
paginate: true
class: lead
---

# Dérivation

## 1. Définition intuitive de la dérivée

La dérivée d'une fonction (f) en un point (x) mesure **la pente de la courbe** de (f) à ce point.
On l'interprète comme la vitesse de variation :

$$
f'(x) = \text{pente de la tangente au point } x.
$$

Si :

1. (f'(x) > 0) : la fonction **augmente** (pente positive).
1. (f'(x) < 0) : la fonction **diminue** (pente négative).
1. (f'(x) = 0) : la courbe a une **tangente horizontale** (candidats aux extremums).

---

## Lire une tangente et sa pente

![À gauche, f(x)=x carré et sa tangente en x=1 ; à droite, la dérivée 2x. La valeur en 1 vaut 1 et la pente vaut 2.](figures/derivee-tangente.svg)

La valeur de la fonction et la valeur de sa dérivée ne désignent pas la même quantité.

---

## 2. Fonction dérivable

Une fonction est dérivable sur un intervalle si sa pente existe en tout point.
Notation :

$$
f : I \to \mathbb{R}, \quad f'(x) \text{ existe pour tout } x \in I.
$$

---

# 3. Règles de dérivation

### 3.1. Dérivées usuelles

$$
(x^n)' = nx^{n-1}
$$

$$
(\sqrt{x})' = \frac{1}{2\sqrt{x}}
$$

$$
(e^x)' = e^x
$$

$$
(\ln(x))' = \frac{1}{x}
$$

### Fonctions trigonométriques

$$
(\sin x)' = \cos x
$$

$$
(\cos x)' = -\sin x
$$

---

### 3.2. Règles de calcul

1. **Somme**

$$
(f+g)' = f' + g'
$$

2. **Produit**

$$
(fg)' = f'g + fg'
$$

3. **Quotient**

$$
\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2} \qquad (g \neq 0)
$$

4. **Composition** (chaîne)

$$
f(g(x))' = f'(g(x)) \cdot g'(x)
$$

---

# 4. Dérivée et sens de variation

Pour étudier une fonction, on :

1. calcule sa dérivée (f'),
2. étudie le signe de (f'),
3. remplit un tableau de variation.

Règle fondamentale :

1. (f'(x) > 0) : (f) **croît**,
1. (f'(x) < 0) : (f) **décroît**,
1. (f'(x) = 0) : points critiques (minima, maxima possibles).

---

# 5. Dérivée seconde et courbure (rappel utile)

La dérivée seconde est la dérivée de la dérivée :

$$
f''(x) = (f'(x))'.
$$

Elle indique la **courbure** :

1. (f''(x) > 0) : la courbe est **convexe** (pente augmente),
1. (f''(x) < 0) : la courbe est **concave** (pente diminue).

---

# 6. Exemples corrigés

## Exemple 1 

1. Dérivée :

$$
f'(x) = 3x^2 - 3.
$$

2. Signe :

$$
f'(x)=0 \iff 3x^2-3=0 \iff x^2=1 \iff x=\pm 1.
$$

3. Variation :

1. $$(f'>0) pour (x<-1)$$
1. $$(f'<0) pour (-1<x<1)$$
1. $$(f'>0) pour (x>1)$$

La fonction décroît puis croît → minimum local en (x=1), maximum local en (x=-1).

---

## Exemple 2 : Fonction avec quotient

$$f(x)=\frac{x^2-1}{x} (sur \mathbb{R}\setminus{0})$$

$$
f'(x)=\frac{2x^2 - (x^2 - 1)}{x^2} = \frac{x^2 + 1}{x^2}.
$$

Comme $$x^2+1>0$$, on obtient :

$$
f'(x) > 0 \quad \text{pour tout } x\neq 0.
$$

La fonction est **strictement croissante** sur chaque intervalle de son domaine.

---

## Exemple 3 : Composition

$$f(x) = e^{3x}$$

$$
f'(x) = 3 e^{3x}.
$$

Toujours positif → fonction strictement croissante.

---

# 7. Exercices d'entraînement

## Exercice 1

Dériver :

a) 

$$
f(x)=x^4 - 2x^2 + 1
$$

b) 

$$
g(x)=\sqrt{x}(x^2+3)
$$

c) 

$$
h(x)=\frac{3x+1}{x-2}
$$

---

## Exercice 2

Étudier les variations de :

a) 

$$
f(x)=x^3+3x^2
$$

b) 

$$
g(x)=\ln(x) - x
$$

c) 

$$
h(x)=e^{-x}
$$

---

## Exercice 3

Trouver les maxima/minima de :

a) 

$$
f(x)=x^2 - 4x +1
$$

b) 

$$
g(x)=x + \frac{1}{x}
$$

Cette fonction n'est pas définie en 0.

c) 

$$
h(x)=\sin x + x
$$

---

## Exercice 4

Étudier la convexité de :

a) 

$$
f(x)=x^4
$$

b) 

$$
g(x)=x e^x
$$

c) 

$$
h(x)=\ln(x)
$$

---

## Exercice 5

Mettez en place un environnement de production pour faire les TP du cours avec FastAPI, Numpy et Pandas.

Voyez ce fichier pour l'installation : [installation](https://github.com/Antoine07/maths/blob/main/installation.md)

Testez ce code et expliquez ce qu'il fait exactement.

```python
noise = np.random.normal(loc=0.0, scale=0.5, size=t.size)
T_raw = 10 + 5 * np.sin((2*np.pi/24)*t) + noise
```

---

## Problème — Un rythme et son cumul

Un groupe se retrouve aujourd'hui deux fois par mois. Peut-on simplement multiplier cette fréquence par 30 ans ?

Comparer une fréquence constante à une fréquence décroissante et vérifier le cumul en le dérivant. Le problème introduit la relation entre une fréquence et son cumul.

[Problème 2 : et si les occasions devenaient moins fréquentes ?](../Tps/Tail_End/02_frequence.md)

---

## TP optimisation 

[TP Optimisation](https://github.com/Antoine07/maths/blob/main/Derivation/TPs/00_TP_optimisation.md)

---

## [Retour au plan](https://antoine07.github.io/maths/)
