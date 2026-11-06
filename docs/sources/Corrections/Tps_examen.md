# **Correction – Normalisation et comparaison de deux séries statistiques**

## 1. Étude descriptive des séries

### Série A

* Minimum : **12**
* Maximum : **103**
* Moyenne ( \mu_A \approx 63 )
* Écart-type ( \sigma_A \approx 26 )

### Série B

* Minimum : **95**
* Maximum : **250**
* Moyenne ( \mu_B \approx 168 )
* Écart-type ( \sigma_B \approx 45 )

### Interprétation

Les deux séries :

* n’ont **pas la même unité**,
* n’ont **pas le même niveau moyen**,
* n’ont **pas la même dispersion**.

➡️ Une comparaison directe n’est donc **pas possible** sans normalisation.

---

## 2. Normalisation par centrage–réduction

On applique la formule :
[
z = \frac{x - \mu}{\sigma}
]

### Résultats et observations

#### a) Moyennes

Après centrage-réduction :

* moyenne de la série A = **0**
* moyenne de la série B = **0**

➡️ Les deux séries sont recentrées autour de la même valeur.

#### b) Écarts-types

Après réduction :

* écart-type de A = **1**
* écart-type de B = **1**

➡️ Les dispersions deviennent comparables.

#### c) Comparabilité des distributions

Les séries deviennent comparables :

* en termes de **dispersion relative**,
* de **symétrie**,
* et de **présence de valeurs extrêmes**.

⚠️ En revanche, les **niveaux absolus** et les unités sont perdus.

### Conclusion

Le centrage-réduction permet de comparer les **formes des distributions**, indépendamment des unités.

---

## 3. Normalisation min–max

On applique la formule :
[
x_{\min\max} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}
]

### Résultats et observations

#### a) Échelle

Après normalisation :

* toutes les valeurs sont comprises entre **0 et 1** pour A et B.

➡️ Les deux séries sont sur la **même échelle**.

#### b) Information conservée

La normalisation min–max conserve :

* l’ordre des valeurs,
* les écarts relatifs,
* la dynamique de variation.

⚠️ Elle ne conserve pas :

* la moyenne,
* l’écart-type,
* l’interprétation statistique des valeurs.

### Conclusion

La normalisation min–max est adaptée pour comparer des **évolutions** ou des **profils**.

---

## 4. Représentations graphiques

### a) Séries centrées-réduites

**Représentation pertinente : diagramme à moustaches**

* médiane proche de 0 pour les deux séries,
* dispersions comparables,
* outliers éventuellement visibles.

➡️ Le boxplot permet de comparer la **distribution**.

---

### b) Séries normalisées min–max

**Représentation pertinente : courbes**

* valeurs entre 0 et 1,
* comparaison directe des évolutions,
* visualisation des pics et variations.

➡️ La courbe permet de comparer la **dynamique temporelle**.

---

## 5. Interprétation des résultats

### 1. Comparaison des médianes

* Après centrage-réduction : médianes proches de 0 (effet de la méthode).
* Après min–max : médianes parfois différentes.

➡️ Des médianes proches **ne signifient pas** que les séries ont des niveaux comparables, mais qu’elles sont comparables **relativement**.

---

## Partie facultative

### 2. Série la plus dispersée

* La série **B** est plus dispersée (moustaches plus longues en min–max).

### 3. Valeurs atypiques

* Peu de véritables outliers.
* Quelques valeurs élevées plus visibles dans la série B après centrage-réduction.

### 4. Dynamique temporelle

* Série A : évolution plutôt **régulière**.
* Série B : évolution **plus irrégulière**, avec des pics.

➡️ La normalisation **n’altère pas l’ordre des données**, mais modifie la perception des écarts.

---

## Conclusion générale

* Le **centrage–réduction** sert à comparer des **distributions**.
* La **normalisation min–max** sert à comparer des **évolutions**.
* Les données sont les mêmes, **seul l’objectif d’analyse change**.

C’est exactement ce que ce TP cherche à mettre en évidence.
