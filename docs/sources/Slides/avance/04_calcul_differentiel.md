---
marp: true
html: true
---

# Calcul différentiel matriciel

## Dériver un modèle et son erreur

Après [gradient et Hessienne](../gradient.md), nous passons de fonctions de deux variables à un modèle possédant plusieurs paramètres.

---

## Objectif

Calculer un gradient vectorisé, lire une Jacobienne et propager une dérivée à travers des fonctions composées.

Nous vérifierons les formules par différences finies avant de les utiliser pour entraîner un modèle.

Prérequis : dérivées partielles, gradient, transposée, moindres carrés et produits matriciels. Durée indicative : 4 h.

---

## Résumé général

Une prédiction dépend de paramètres ; une perte dépend de cette prédiction. La règle des fonctions composées relie les deux.

Le gradient rassemble les dérivées d'une sortie scalaire. La Jacobienne décrit les dérivées d'une sortie vectorielle.

La forme matricielle permet de calculer toutes les contributions sans écrire une boucle par observation. Elle prépare directement la rétropropagation.

---

## Concepts essentiels — Fixer les dimensions

$A\in\mathbb{R}^{n\times d}$ contient la constante et les variables ; $\theta\in\mathbb{R}^{d}$ contient les paramètres ; $y\in\mathbb{R}^{n}$ contient les consommations.

La prédiction $A\theta$ et le résidu $r=A\theta-y$ sont de taille $n$.

Nous prenons désormais **prédit moins observé** pour le résidu. Le signe est fixé dans toutes les dérivées qui suivent.

Avec deux observations et deux paramètres, $A$ est $2\times2$ et le gradient attendu possède deux composantes.

---

## Concepts essentiels — Gradient de la perte quadratique

$$
J(\theta)=\frac{1}{2n}\|A\theta-y\|_2^2,
\qquad \nabla_\theta J=\frac1nA^T(A\theta-y).
$$

$n$ est le nombre d'observations ; le facteur $1/2$ compense le 2 produit par la dérivation du carré.

Intuition : chaque erreur contribue aux poids en proportion des caractéristiques qui ont produit cette erreur.

Exemple : avec un seul point, $A=(1\;2)$, $y=3$ et $\theta=0$, le résidu vaut -3 et le gradient vaut $(-3,-6)^T$.

---

## Explication détaillée — Une composante du gradient

Pour le paramètre $\theta_j$ :

$$
\frac{\partial J}{\partial\theta_j}=\frac1n\sum_i r_iA_{ij}.
$$

La colonne $j$ de $A$ pondère les erreurs. Le produit $A^Tr$ effectue ces sommes pour tous les paramètres.

Avec $r=(-1,-3)^T$ et la colonne $A_j=(0,1)^T$, la somme vaut -3 ; divisée par $n=2$, la dérivée vaut -1,5.

Le produit inverse `A @ r` n'a pas cette signification, même si des dimensions carrées peuvent parfois masquer l'erreur.

---

## Exemple concret — Deux observations

$$
A=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
y=\begin{pmatrix}1\\3\end{pmatrix},\quad\theta=\begin{pmatrix}0\\0\end{pmatrix}.
$$

Les résidus valent $(-1,-3)^T$. La perte vaut $(1+9)/4=2{,}5$.

Le gradient vaut $(-2,-1{,}5)^T$. Les deux composantes sont négatives : les augmenter légèrement diminue localement la perte.

Un gradient donne une information locale ; il ne fournit pas directement la meilleure amplitude du déplacement.

---

## Lecture du code — Perte et gradient

```python
import numpy as np
A = np.array([[1., 0.], [1., 1.]])
y = np.array([1., 3.])
theta = np.zeros(2)
r = A @ theta - y
perte = (r @ r) / (2 * len(y))
gradient = A.T @ r / len(y)
print(perte, gradient)
```

**Fonctionnement :** les entrées sont les observations, la cible et les paramètres. Le code calcule le résidu, sa longueur au carré, puis les contributions aux paramètres.

**Exécution et résultat attendu :** `2.5 [-2. -1.5]`.

**Erreurs fréquentes :** oublier la moyenne, changer le signe du résidu ou mélanger `(n,)` et `(n, 1)`.

---

## Concepts essentiels — Jacobienne

Pour $F:\mathbb{R}^{d}\to\mathbb{R}^{m}$, sa Jacobienne est une matrice $m\times d$ : une ligne par sortie, une colonne par entrée.

Exemple : $F(x_1,x_2)=(x_1^2+x_2,x_1x_2)^T$.

$$
J_F(x)=\begin{pmatrix}2x_1&1\\x_2&x_1\end{pmatrix}.
$$

Au point $(2,3)$, elle vaut $\begin{pmatrix}4&1\\3&2\end{pmatrix}$.

Intuition : chaque coefficient mesure la sensibilité locale d'une sortie à une entrée.

---

## Concepts essentiels — Règle des fonctions composées

Si la perte scalaire $L$ dépend du vecteur $F(x)$ :

$$
\nabla_x L=J_F(x)^T\nabla_F L.
$$

$\nabla_F L$ est la sensibilité de la perte aux sorties intermédiaires. La Jacobienne transposée la ramène vers les entrées.

Avec la Jacobienne précédente et $\nabla_F L=(1,-1)^T$, on obtient $(1,-1)^T$ : $(4-3,1-2)$.

Les bibliothèques peuvent calculer ce produit sans construire la Jacobienne complète.

---

## Lecture des formules — Une chaîne scalaire

Posons $z=2w+1$ et $L=z^2$. La chaîne donne :

$$
\frac{dL}{dw}=\frac{dL}{dz}\frac{dz}{dw}=2z\times2.
$$

Pour $w=1$, $z=3$, $L=9$ et la dérivée vaut 12.

Le calcul suit deux sens : les valeurs vont de $w$ vers $L$ ; les sensibilités reviennent de $L$ vers $w$.

C'est le principe que nous réutiliserons sur un réseau de neurones.

---

## Suivre une chaîne dans les deux sens

![Pour w égal à 1, z vaut 3 et L vaut 9. Les dérivées locales 6 et 2 se multiplient pour donner 12.](images/chaine-derivees.svg)

---

## Concepts essentiels — Approximation de Taylor

Pour une petite perturbation $h$ :

$$
J(\theta+h)\approx J(\theta)+\nabla J(\theta)^Th.
$$

$h$ est le déplacement proposé. Le produit scalaire indique la variation prédite au premier ordre.

Pour $f(x)=x^2$, $x=2$ et $h=0{,}1$, l'approximation donne $4+4\times0{,}1=4{,}4$, contre la valeur exacte 4,41.

L'erreur dépend de la courbure et de la taille du déplacement. Un petit modèle local ne justifie pas un grand saut arbitraire.

---

## Lire une approximation locale

![La courbe x carré et son approximation affine au point 2 ; en 2,1, les valeurs exacte et approchée valent respectivement 4,41 et 4,40. L'écart augmente quand on s'éloigne.](../figures/taylor-local.svg)

---

## Concepts essentiels — Hessienne du modèle linéaire

$$
H=\nabla^2J=\frac1nA^TA.
$$

La Hessienne est ici constante et positive semi-définie : pour tout vecteur $v$, $v^THv=\|Av\|^2/n\ge0$. La perte est donc convexe sur tout l'espace.

Pour les deux observations de l'exemple, $H=\begin{pmatrix}1&0{,}5\\0{,}5&0{,}5\end{pmatrix}$.

Si $A$ a un plein rang en colonnes, la Hessienne est définie positive et le minimum est unique. Une Hessienne définie positive en un seul point critique ne prouve pas la convexité globale d'une fonction quelconque.

---

## Algorithme expliqué — Vérifier un gradient

Pour la coordonnée $j$, avec $e_j$ le vecteur unité correspondant :

$$
g_j^{num}=\frac{J(\theta+\varepsilon e_j)-J(\theta-\varepsilon e_j)}{2\varepsilon}.
$$

**Entrées :** fonction de perte, paramètres et petit pas $\varepsilon$, par exemple $10^{-5}$ en précision double.

**Traitement :** perturber une coordonnée à la fois dans les deux sens, calculer la pente, comparer avec la formule.

**Sortie :** écart entre les deux gradients. Pour $f(w)=w^2$ en $w=2$, la formule donne environ 4.

Un pas trop petit amplifie les erreurs d'arrondi. Cette vérification est coûteuse : elle sert au débogage, pas à entraîner un grand réseau.

---

## Erreurs fréquentes

- Dériver la prédiction en oubliant la perte qui suit.
- Oublier un facteur introduit par une fonction intermédiaire.
- Utiliser une transposée pour « faire marcher » le code sans expliquer les dimensions.
- Assimiler gradient petit et bonne généralisation.
- Tester une dérivée classique exactement au point non différentiable d'une activation.

---

## Exercice 1 — Dérouler une composition

**Objectif pédagogique :** appliquer la règle de chaîne. **Prérequis :** dérivée d'un carré.

**Énoncé :** pour $L(w)=(2w+1)^2$, calculer $L(1)$ et sa dérivée en 1 en nommant la variable intermédiaire.

**Contraintes :** ne pas développer le polynôme avant le calcul. **Livrable attendu :** deux étapes de dérivation et le résultat.

**Critères de réussite :** obtenir une dérivée 12 et identifier l'origine des deux facteurs.

<details><summary>Indices gradués</summary>

1. Nommer $z=2w+1$.
2. Calculer séparément $dL/dz$ et $dz/dw$.
</details>

---

## Correction — Dérouler une composition

<details><summary>Afficher la correction</summary>

En $w=1$, $z=3$ et $L=9$. La dérivée de $z^2$ par rapport à $z$ vaut 6 ; celle de $2w+1$ par rapport à $w$ vaut 2. Leur produit donne 12.

Le nombre 6 seul ne serait pas la dérivée par rapport au paramètre initial.
</details>

---

## Exercice 2 — Dériver une perte multivariée

**Objectif pédagogique :** calculer une perte et son gradient. **Prérequis :** moindres carrés et dimensions.

**Énoncé :** pour $A=((1,0),(1,1))$, $y=(1,3)^T$ et $\theta=(0,0)^T$, retrouver la perte et le gradient. Vérifier par différences finies.

**Contraintes :** convention de résidu prédiction moins cible. **Livrable attendu :** calcul manuel et écart numérique.

**Critères de réussite :** perte 2,5, gradient $(-2,-1{,}5)^T$, écart inférieur à $10^{-7}$.

<details><summary>Indices gradués</summary>

1. Calculer `r = A @ theta - y`.
2. Utiliser deux valeurs de perte par coordonnée pour le contrôle numérique.
</details>

---

## Correction — Dériver une perte multivariée

<details><summary>Afficher la correction</summary>

```python
import numpy as np
A = np.array([[1., 0.], [1., 1.]])
y = np.array([1., 3.])
theta = np.zeros(2)
def perte(t):
    return np.mean((A @ t - y)**2) / 2
epsilon = 1e-5
numerique = np.array([
    (perte(theta + epsilon*e) - perte(theta - epsilon*e))
    / (2*epsilon) for e in np.eye(2)
])
print(numerique)
```

**Lecture :** `np.eye(2)` fournit les deux directions unitaires ; la compréhension calcule une pente dans chacune. La sortie est proche de `[-2., -1.5]`. Le contrôle numérique complète le calcul vectorisé, il ne le remplace pas pour l'entraînement.
</details>

---

## Exercice 3 — Un gradient qui monte

**Objectif pédagogique :** déboguer par les dimensions et un exemple. **Prérequis :** gradient et approximation locale.

**Énoncé :** un programme renvoie `A @ (y - A @ theta)` comme gradient. Identifier le problème de dimensions et le problème de signe. Corriger aussi l'absence de moyenne.

**Contraintes :** vérifier sur une matrice rectangulaire. **Livrable attendu :** formule et contre-exemple.

**Critères de réussite :** résultat de taille `d`, signe cohérent, accord avec différences finies.

<details><summary>Indices gradués</summary>

1. La sortie doit avoir autant de composantes que de paramètres.
2. Revenir à la définition de la perte, puis au résidu choisi.
</details>

---

## Correction — Un gradient qui monte

<details><summary>Afficher la correction</summary>

La correction est `A.T @ (A @ theta - y) / len(y)`.

Pour `A` de taille `(5, 3)`, le résidu a taille `(5,)` et le gradient a taille `(3,)`. Le produit proposé essaie de contracter une dimension 3 avec une dimension 5.

Pour un seul paramètre et $J(\theta)=(\theta-1)^2/2$, le vrai gradient en 0 vaut -1. Le signe opposé indiquerait la mauvaise direction pour une descente.
</details>

---

## Projet fil rouge — Jalon 4

Reprendre le modèle multivarié et les données transformées au jalon 3 du [projet consommation](../../Projet_IA/README.md).

**Notions mobilisées :** calcul matriciel et règle de chaîne. **Fonctionnalité à produire :** une fonction renvoyant à la fois la perte et son gradient.

**Résultat vérifiable :** gradient de taille `(4,)` et accord avec les différences finies à $10^{-7}$ près sur un point de contrôle en précision double.

**Livrables :** fonction, contrôle numérique et explication de chaque dimension. **À observer :** oubli de la constante, signe inversé et diffusion automatique involontaire.

Le même gradient servira à la descente du prochain chapitre.

---

## Cas d'usage réels

**Entreprise :** équipe data d'un service énergétique, scénario pédagogique.

**Problème :** vérifier un modèle doté d'une fonction de perte personnalisée.

**Solution :** calculer les gradients puis les comparer à une approximation numérique sur un petit cas.

**Bénéfice attendu :** détecter une erreur avant un entraînement coûteux. Un gradient correct valide le calcul local, pas la pertinence métier du modèle.

---

## Fiche de révision

- Une perte scalaire a un gradient ; une sortie vectorielle a une Jacobienne.
- Toujours fixer l'ordre des dimensions et le signe du résidu.
- La règle de chaîne multiplie les sensibilités intermédiaires.
- Taylor décrit une variation locale.
- Les différences finies servent à contrôler l'implémentation.

---

## Questions de révision

1. Pourquoi le gradient a-t-il autant de composantes que les paramètres ?
2. À quoi sert le facteur $1/2$ dans la perte quadratique ?
3. Quelle différence entre gradient et Jacobienne ?
4. Pourquoi ne pas choisir systématiquement un pas numérique de $10^{-20}$ ?
5. Pourquoi le gradient ne fixe-t-il pas à lui seul le pas d'apprentissage ?

---

## QCM — Questions 1 et 2

**1. Pour une fonction de $\mathbb R^3$ vers $\mathbb R^2$, la Jacobienne est :** A. $3\times2$ ; B. $2\times3$ ; C. $3\times3$ ; D. scalaire.

**2. Pour $J=\|A\theta-y\|^2/(2n)$, le gradient est :** A. $Ar$ ; B. $-A^Tr$ ; C. $A^Tr/n$ avec $r=A\theta-y$ ; D. $r^2$.

<details><summary>Afficher la correction</summary>

1. **B** : une ligne par sortie, une colonne par entrée.
2. **C** : transposée, signe et moyenne correspondent à la perte choisie.
</details>

---

## QCM — Questions 3 à 5

**3. La règle de chaîne sert à :** A. dériver une composition ; B. trier les données ; C. inverser une matrice ; D. choisir les variables.

**4. Les différences finies sont surtout utiles pour :** A. tous les entraînements ; B. supprimer les biais ; C. choisir le test ; D. vérifier un gradient sur un petit cas.

**5. Un gradient nul garantit-il une bonne performance de test ?** A. toujours ; B. seulement avec NumPy ; C. non ; D. si le fichier est grand.

<details><summary>Afficher la correction</summary>

3. **A** : la dérivée traverse les fonctions intermédiaires.
4. **D** : leur coût croît avec le nombre de paramètres.
5. **C** : stationnarité de la perte d'apprentissage et généralisation sont distinctes.
</details>

---

## Résumé final

Nous savons calculer et contrôler l'influence des paramètres sur une erreur.
Les dimensions rendent les formules vérifiables.
La prochaine étape utilise ces gradients pour apprendre les paramètres, avec un pas et un critère d'arrêt.

[Continuer : optimisation et régularisation](05_optimisation.md).

Référence : [PyTorch — règle de chaîne et différentiation automatique](https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html).
