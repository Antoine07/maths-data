---
marp: true
theme: default
paginate: true
class: lead
---

# Calculer une valeur centrée-réduite

**Un calcul pas à pas avant l’ACP :** situer une observation par rapport à la moyenne, en nombre d’écarts-types.

---

## Une valeur de 9, est-ce beaucoup ?

Cela dépend de la série à laquelle elle appartient. Pour comparer une observation aux autres, on peut mesurer :

1. son écart à la moyenne ;
2. cet écart en unités d’écart-type.

Prenons huit valeurs :

$$
2,\;4,\;4,\;4,\;5,\;5,\;7,\;9.
$$

Nous allons calculer une valeur centrée-réduite sans commencer par Python.

---

## Étape 1 · Calculer la moyenne et les écarts

La somme des huit valeurs vaut 40. Leur moyenne est donc :

$$
\overline{x}=\frac{40}{8}=5.
$$

On soustrait 5 à chaque valeur :

| Valeur $x$ | 2 | 4 | 4 | 4 | 5 | 5 | 7 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Écart $x-5$ | −3 | −1 | −1 | −1 | 0 | 0 | 2 | 4 |

La somme des écarts vaut 0 : les écarts négatifs et positifs se compensent.

---

## Étape 2 · Calculer l’écart-type

Pour ne pas laisser les écarts positifs et négatifs s’annuler, on les élève au carré :

| Écart $x-5$ | −3 | −1 | −1 | −1 | 0 | 0 | 2 | 4 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Carré $(x-5)^2$ | 9 | 1 | 1 | 1 | 0 | 0 | 4 | 16 |

La somme des carrés vaut 32. Pour cette série, on divise par 8 :

$$
\text{variance}=\frac{32}{8}=4
\qquad\Longrightarrow\qquad
\text{écart-type}=\sqrt{4}=2.
$$

Ici, nous décrivons les huit valeurs observées : on utilise l’écart-type calculé avec `ddof=0`, le choix par défaut de `np.std`.

---

## Étape 3 · Calculer les valeurs centrées-réduites

On divise chaque écart à la moyenne par l’écart-type :

$$
z=\frac{x-\overline{x}}{\sigma}.
$$

Ici, $\overline{x}=5$ et $\sigma=2$ :

| Valeur $x$ | 2 | 4 | 4 | 4 | 5 | 5 | 7 | 9 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Valeur centrée-réduite $z$ | −1,5 | −0,5 | −0,5 | −0,5 | 0 | 0 | 1 | 2 |

Exemples : $z(2)=(2-5)/2=-1{,}5$ ; $z(9)=(9-5)/2=2$.

---

## Lire le résultat

- $z=0$ : la valeur est égale à la moyenne.
- $z=1$ : elle est un écart-type au-dessus de la moyenne.
- $z=-1{,}5$ : elle est un écart-type et demi en dessous.
- $z=2$ : elle est deux écarts-types au-dessus.

Après cette transformation, la série a une moyenne égale à 0 et un écart-type égal à 1. Les valeurs sont exprimées sur une même échelle, même si les mesures de départ ont des unités ou des amplitudes différentes.

---

## Vérifier le calcul avec NumPy

```python
import numpy as np

x = np.array([2, 4, 4, 4, 5, 5, 7, 9], dtype=float)
moyenne = np.mean(x)
ecart_type = np.std(x)  # ddof=0 : division par le nombre de valeurs
z = (x - moyenne) / ecart_type

print("Moyenne :", moyenne)          # 5.0
print("Écart-type :", ecart_type)    # 2.0
print("Valeurs z :", z)
print("Vérification :", z.mean(), z.std())  # 0.0, 1.0
```

`x - moyenne` centre toutes les valeurs. La division par `ecart_type` les réduit ensuite. Le tableau `z` contient les valeurs centrées-réduites.

---

## Pourquoi avant l’ACP ?

L’ACP cherche des directions qui résument les variations de plusieurs variables. Si une variable est mesurée en milliers et une autre en unités, la première peut dominer le calcul simplement à cause de son échelle.

Centrer-réduire chaque colonne permet de comparer les variables sur une échelle commune. L’ACP peut alors s’appuyer sur leurs variations relatives, plutôt que sur les seules unités de mesure.

La transformation n’est pas automatique pour toutes les analyses : le choix dépend de la question. Pour notre première ACP, nous allons examiner les données standardisées avant de chercher les axes principaux.

---

## À vous · Une valeur au-dessus de la moyenne

Une série de mesures a une moyenne de 12 et un écart-type de 3.

1. Calculez la valeur centrée-réduite correspondant à $x=18$.
2. Interprétez le résultat en une phrase.
3. Quel serait le score $z$ pour $x=9$ ?

<details><summary>Afficher la correction</summary>

Pour $x=18$ : $z=(18-12)/3=2$. La valeur est deux écarts-types au-dessus de la moyenne.

Pour $x=9$ : $z=(9-12)/3=-1$. Elle est un écart-type en dessous de la moyenne.

</details>
