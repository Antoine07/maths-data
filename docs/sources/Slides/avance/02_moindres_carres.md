---
marp: true
html: true
---

# Régression multivariée et stabilité

## Des projections à un modèle de consommation

Prérequis : [modélisation de la consommation](../02_modelisation.md), [matrices](../matrice.md) et [géométrie des données](01_geometrie_donnees.md).

---

## Objectif

Prédire une consommation avec plusieurs variables, résoudre les moindres carrés et diagnostiquer un problème de rang ou de conditionnement.

Nous allons expliquer ce que calcule un solveur, pourquoi une inversion explicite est fragile et pourquoi une bonne prédiction ne rend pas tous les coefficients interprétables.

Durée indicative : 4 h avec les exercices et le jalon 2.

---

## Résumé général

Le modèle du TP utilisait le jour comme unique variable. Nous ajoutons température, occupation et équipements.

Les moindres carrés choisissent les paramètres qui minimisent la somme des erreurs au carré. Géométriquement, les prédictions sont la projection de la cible sur l'espace engendré par les colonnes du modèle.

Le rang renseigne sur les dépendances exactes ; le conditionnement, sur la sensibilité aux perturbations.

---

## Concepts essentiels — La matrice de conception

Pour $n$ observations et $p$ variables : $X\in\mathbb{R}^{n\times p}$, $y\in\mathbb{R}^{n}$.

On ajoute une colonne de 1 : $A\in\mathbb{R}^{n\times(p+1)}$. Les paramètres $\theta=(b,w_1,\ldots,w_p)^T$ contiennent la constante $b$ et les poids.

$$
\widehat{y}=A\theta.
$$

Exemple : avec une ligne $(1,12,3)$ et $\theta=(5,-0{,}2,1)^T$, la prédiction est $5-2{,}4+3=5{,}6$ kWh. Les coefficients sont ici purement illustratifs.

---

## Concepts essentiels — Résidu et objectif

$$
r=y-A\theta,\qquad S(\theta)=\|r\|_2^2=\sum_{i=1}^{n}(y_i-\widehat{y}_i)^2.
$$

$r_i$ mesure l'écart observé moins prédit. Le carré évite que les erreurs positives et négatives s'annulent.

Si $y=(1,2,2)^T$ et les prédictions valent $(1,1,1)^T$, alors $r=(0,1,1)^T$ et $S=2$.

Minimiser la somme ou sa moyenne donne les mêmes paramètres, mais change les valeurs numériques de l'objectif.

---

## Explication détaillée — Une projection

Les prédictions possibles forment l'espace des combinaisons des colonnes de $A$.

Au meilleur ajustement, le résidu est orthogonal à chaque colonne :

$$
A^T(y-A\theta)=0.
$$

Par exemple, si $A$ ne contient qu'une colonne de 1 et $y=(1,2,3)^T$, la meilleure constante vaut 2. Les résidus $(-1,0,1)^T$ ont une somme nulle : leur produit scalaire avec la colonne de 1 est nul.

---

## Lecture des formules — Les équations normales

La condition précédente s'écrit :

$$
A^TA\theta=A^Ty.
$$

$A^TA$ a la taille $(p+1)\times(p+1)$. Cette équation relie les paramètres aux données.

Si $A$ a des colonnes indépendantes, la solution est unique. L'expression théorique $(A^TA)^{-1}A^Ty$ explique la solution, mais n'est pas notre méthode de calcul.

Exemple : $A=(1,1)^T$, $y=(2,4)^T$ donnent $2\theta=6$, donc $\theta=3$.

---

## Concepts essentiels — Rang et identifiabilité

Le rang de $A$ est le nombre de directions indépendantes portées par ses colonnes.

Si une colonne est exactement le double d'une autre, leurs effets ne peuvent pas être séparés de manière unique.

Pour $\widehat y=b+w_1x+w_2(2x)$, seules les valeurs de $b$ et de $w_1+2w_2$ sont identifiables. Les couples $(1,0)$ et $(-1,1)$ donnent la même contribution.

Les prédictions de moindres carrés sur l'apprentissage restent uniques ; les paramètres peuvent ne pas l'être.

---

## Concepts essentiels — Conditionnement

Pour une matrice de plein rang en colonnes, son conditionnement spectral est :

$$
\kappa_2(A)=\frac{\sigma_{\max}}{\sigma_{\min}}.
$$

Les $\sigma$ sont les valeurs singulières ; nous les étudierons dans le chapitre SVD. Une petite valeur singulière signale une direction peu contrainte par les données.

Si elles valent 10 et 0,001, le rapport vaut 10 000. Cela indique une sensibilité potentielle, pas une erreur forcément multipliée par 10 000 dans chaque expérience.

---

## Pourquoi éviter l'inversion explicite ?

Former $A^TA$ peut aggraver les difficultés : pour une matrice de plein rang, $\kappa_2(A^TA)=\kappa_2(A)^2$.

Si $\kappa_2(A)=10^4$, on passe à $10^8$ pour les équations normales.

Les factorisations QR ou SVD résolvent directement le problème de moindres carrés. `np.linalg.lstsq` est l'outil utilisé ici ; `np.linalg.solve` convient à un système carré inversible.

La mise à l'échelle peut aider, mais ne supprime pas une dépendance exacte entre colonnes.

---

## Concepts essentiels — Pseudo-inverse

La pseudo-inverse $A^+$ généralise l'idée d'inverse : $\theta=A^+y$ est la solution de moindres carrés de norme minimale.

Elle reste définie pour les matrices rectangulaires ou de rang déficient.

Exemple : pour $A=(1\;1)$ et $y=2$, toutes les solutions vérifient $\theta_1+\theta_2=2$. La solution de norme minimale est $(1,1)^T$.

`lstsq` évite de construire explicitement la pseudo-inverse lorsqu'on veut seulement résoudre le problème.

---

## Exemple concret — Ajuster une droite

Pour les points $(0,1)$, $(1,2)$ et $(2,2)$, on cherche $\widehat y=b+wx$.

La solution est $b=7/6$ et $w=1/2$. Les prédictions sont $7/6$, $5/3$ et $13/6$.

Les résidus sont $(-1/6,1/3,-1/6)$ ; leur somme vaut 0 et leur produit scalaire avec $(0,1,2)$ vaut 0.

La somme des carrés vaut $1/36+1/9+1/36=1/6$. Nous avons vérifié la projection sans supposer que les points sont parfaitement alignés.

---

## Voir les résidus de l'ajustement

![Les trois observations (0,1), (1,2) et (2,2), leurs prédictions sur la droite et les résidus verticaux de signes opposés.](../figures/moindres-carres.svg)

La droite minimise la somme des carrés des écarts ; elle n'annule pas chaque écart.

---

## Lecture du code — Résoudre et vérifier

```python
import numpy as np
x = np.array([0., 1., 2.])
y = np.array([1., 2., 2.])
A = np.column_stack([np.ones(len(x)), x])
theta, _, rang, s = np.linalg.lstsq(A, y, rcond=None)
r = y - A @ theta
print(theta, rang)
print(A.T @ r)
```

**Fonctionnement :** `A` a trois lignes et deux colonnes. Le solveur renvoie les deux coefficients, le rang et les valeurs singulières `s`.

**Exécution et résultat attendu :** paramètres proches de `[1.166667, 0.5]`, rang 2, puis deux valeurs proches de zéro.

**Erreur fréquente :** lire le tableau `residuals` comme un vecteur d'erreurs par observation. Calculer explicitement `r` ; le tableau renvoyé peut aussi être vide.

---

## Mesurer la qualité d'une prévision

$$
\operatorname{RMSE}=\sqrt{\frac1n\sum_i(\widehat y_i-y_i)^2}.
$$

La racine de l'erreur quadratique moyenne s'exprime dans l'unité de la cible. Pour deux erreurs de 1 et -1 kWh, la RMSE vaut 1 kWh.

Sur les données de validation, comparer cette erreur à une référence : prédire toujours la moyenne des consommations **d'apprentissage**.

Une faible erreur d'entraînement ne suffit pas. Les données de test restent réservées à l'évaluation finale, après le choix des modèles.

---

## Algorithme expliqué — Du tableau au modèle

**Entrées :** variables connues et consommations des journées d'apprentissage ; variables des journées de validation.

**Traitement :** ajouter la constante, résoudre par `lstsq`, contrôler rang et résidus, puis prédire sur la validation.

**Sorties :** paramètres, diagnostic et RMSE comparée à une référence.

**Exemple pas à pas :** trois observations deviennent une matrice $3\times2$, le solveur fournit $(7/6,1/2)$, puis la multiplication par une nouvelle ligne $(1,3)$ donne $8/3$.

L'extrapolation au-delà des observations demande une justification métier.

---

## Erreurs fréquentes

- Oublier la colonne de 1 lorsque l'on veut une constante.
- Utiliser `A * theta` au lieu de `A @ theta`.
- Inverser une matrice rectangulaire ou former inutilement une inverse.
- Interpréter des coefficients instables comme des effets causaux.
- Choisir les variables après avoir comparé leurs résultats sur le test.

---

## Exercice 1 — Prédire la sortie du code

**Objectif pédagogique :** lire les dimensions. **Prérequis :** matrice de conception.

**Énoncé :** `X` contient 8 journées et 3 variables ; on lui ajoute une colonne de 1. Donner les dimensions de `A`, `theta`, `A @ theta` et du résidu.

**Contraintes :** écrire chaque dimension avant d'exécuter un programme. **Livrable attendu :** quatre tailles et une justification.

**Critères de réussite :** une prédiction par observation, sans tableau $8\times8$ involontaire.

<details><summary>Indices gradués</summary>

1. La constante ajoute une colonne, pas une ligne.
2. Le produit contracte la dimension des paramètres.
</details>

---

## Correction — Prédire la sortie du code

<details><summary>Afficher la correction</summary>

`A.shape == (8, 4)`, `theta.shape == (4,)`, `prediction.shape == (8,)` et `residu.shape == (8,)`.

Avec un `y` de taille `(8, 1)` et une prédiction de taille `(8,)`, la soustraction peut créer un tableau `(8, 8)` par diffusion automatique. Adopter une convention explicite : ici, la cible et la prédiction sont des vecteurs à une dimension.
</details>

---

## Exercice 2 — Ajuster et contrôler

**Objectif pédagogique :** appliquer les moindres carrés. **Prérequis :** `lstsq` et orthogonalité.

**Énoncé :** ajuster les points $(0,1)$, $(1,2)$, $(2,2)$ ; retrouver les coefficients et la somme des carrés.

**Contraintes :** aucune inverse explicite. **Livrable attendu :** coefficients, résidus et contrôle de `A.T @ r`.

**Critères de réussite :** coefficients proches de $(7/6,1/2)$ et somme des carrés $1/6$.

<details><summary>Indices gradués</summary>

1. Réutiliser le code de résolution.
2. La somme recherchée est `r @ r` ; vérifier les valeurs proches de zéro avec une tolérance.
</details>

---

## Correction — Ajuster et contrôler

<details><summary>Afficher la correction</summary>

```python
import numpy as np
A = np.array([[1., 0.], [1., 1.], [1., 2.]])
y = np.array([1., 2., 2.])
theta = np.linalg.lstsq(A, y, rcond=None)[0]
r = y - A @ theta
print(theta, r @ r, np.allclose(A.T @ r, 0))
```

**Lecture :** les entrées définissent trois observations ; `theta` contient deux paramètres. Après résolution, le programme affiche environ `[1.166667, 0.5]`, `0.166667`, puis `True`. Une comparaison exacte `== 0` serait fragile en calcul flottant.
</details>

---

## Exercice 3 — Une colonne en double

**Objectif pédagogique :** déboguer un modèle non identifiable. **Prérequis :** rang et pseudo-inverse.

**Énoncé :** remplacer `A` par les colonnes $(1,x,2x)$, avec $x=(0,1,2)^T$. Pourquoi l'inversion de `A.T @ A` échoue-t-elle ou devient-elle numériquement fragile ? Proposer une résolution.

**Contraintes :** préserver les prédictions et expliquer les coefficients. **Livrable attendu :** rang, solution et conclusion.

**Critères de réussite :** annoncer un rang 2 pour 3 colonnes et reconnaître plusieurs jeux de poids équivalents.

<details><summary>Indices gradués</summary>

1. La troisième colonne n'apporte pas une direction nouvelle.
2. `lstsq` sélectionne une solution de norme minimale ; retirer une colonne serait aussi possible.
</details>

---

## Correction — Une colonne en double

<details><summary>Afficher la correction</summary>

```python
import numpy as np
x = np.array([0., 1., 2.])
A = np.column_stack([np.ones(3), x, 2*x])
y = np.array([1., 2., 2.])
theta, _, rang, _ = np.linalg.lstsq(A, y, rcond=None)
print(rang, theta, A @ theta)
```

**Exécution :** `A` possède une dépendance exacte ; le rang vaut 2. Les coefficients valent environ `[7/6, 0.1, 0.2]` et la pente effective est $0{,}1+2\times0{,}2=0{,}5$.

La solution est calculable mais les effets séparés des deux colonnes ne sont pas identifiables. Une pénalisation, étudiée plus tard, constitue un choix supplémentaire ; elle ne crée pas d'information absente des observations.
</details>

---

## Projet fil rouge — Jalon 2

Dans le [projet consommation](../../Projet_IA/README.md), conserver les partitions créées au jalon 1. Utiliser température, occupation et équipements, avec une constante.

**Notions mobilisées :** moindres carrés, rang, résidu et validation. **Fonctionnalité à produire :** prévoir la consommation de validation et comparer avec la moyenne d'apprentissage.

**Résultat vérifiable :** matrice d'apprentissage de taille `(144, 4)`, rang 4 et un tableau des RMSE. Ajouter temporairement une copie d'une variable et expliquer la perte de rang.

**Livrables :** modèle sauvegardé et commentaire sur l'identifiabilité. **À observer :** confusion entre bonne prévision et interprétation causale.

---

## Cas d'usage réels

**Entreprise :** équipe de gestion énergétique, scénario pédagogique.

**Problème :** prévoir un ordre de grandeur de la consommation avant la journée.

**Solution :** ajuster un modèle multivarié sur des variables disponibles au moment de la prévision.

**Bénéfice attendu :** un modèle de référence rapide à vérifier et à comparer. Une valeur future de température n'est utilisable que si une prévision était effectivement disponible à cet instant.

---

## Fiche de révision

- Le modèle s'écrit $\widehat y=A\theta$.
- Les moindres carrés minimisent une somme de carrés.
- À l'optimum, le résidu est orthogonal aux colonnes de $A$.
- Le rang concerne l'identifiabilité ; le conditionnement concerne la sensibilité.
- Utiliser `lstsq`, vérifier les dimensions et évaluer hors apprentissage.

---

## Questions de révision

1. Pourquoi ajoute-t-on une colonne de 1 ?
2. Que représente l'espace des colonnes de $A$ ?
3. Peut-on avoir de bonnes prédictions avec des paramètres non uniques ?
4. Pourquoi former $A^TA$ peut-il amplifier les difficultés numériques ?
5. À quoi sert la référence qui prédit la moyenne d'apprentissage ?

---

## QCM — Questions 1 et 2

**1. Avec 3 variables et une constante, le nombre de paramètres vaut :** A. 3 ; B. 4 ; C. le nombre de lignes ; D. 1.

**2. Deux colonnes exactement proportionnelles indiquent :** A. un gain de rang ; B. une dépendance ; C. un meilleur test ; D. une causalité.

<details><summary>Afficher la correction</summary>

1. **B** : trois poids et une constante.
2. **B** : une colonne est une combinaison de l'autre.
</details>

---

## QCM — Questions 3 à 5

**3. Pour résoudre un système rectangulaire de moindres carrés :** A. `inv(A)` ; B. `A * y` ; C. `lstsq(A, y)` ; D. `det(A)`.

**4. Une RMSE de 2 sur une cible en kWh s'exprime en :** A. kWh ; B. kWh² ; C. pourcentage ; D. aucune unité.

**5. Si les paramètres sont non uniques, `lstsq` choisit :** A. le vecteur nul ; B. le plus grand vecteur ; C. une solution au hasard ; D. une solution de norme L2 minimale parmi les solutions de moindres carrés.

<details><summary>Afficher la correction</summary>

3. **C** : le solveur traite le problème directement.
4. **A** : la racine rétablit l'unité de la cible.
5. **D** : c'est la convention de solution de norme minimale.
</details>

---

## Résumé final

Nous avons transformé une projection en modèle multivarié.
La stabilité des calculs et la qualité des prévisions sont deux questions distinctes.
Avant d'approfondir la SVD, reprendre [covariance et corrélation](../stat/02_covariance_correlation.md), [centrage-réduction](../stat/03_centrage_reduction.md) et [introduction à l'ACP](../stat/04_acp_intro.md).

Références : [NumPy — moindres carrés](https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html), [NumPy — conditionnement](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cond.html).
