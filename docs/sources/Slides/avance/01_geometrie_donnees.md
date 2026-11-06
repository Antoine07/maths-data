---
marp: true
html: true
---

# Géométrie des données

## Normes, distances, projections et similarité

Après [Matrices et vecteurs propres](../matrice.md), nous savons multiplier une matrice par un vecteur. Nous allons maintenant comparer les observations représentées par ces vecteurs.

---

## Objectif

Choisir une notion de proximité adaptée à une question métier et calculer une projection.

À la fin : expliquer la différence entre **proximité en valeur** et **ressemblance de direction**, sans confondre leurs usages.

Prérequis : vecteurs, transposée, produit matrice-vecteur et racine carrée. Durée indicative : 3 h, exercices compris.

---

## Résumé général

Une journée devient un point dont les coordonnées décrivent température, occupation et équipements.

Une distance compare deux points. Un produit scalaire compare leurs directions et intervient aussi dans une prédiction linéaire.

Une projection conserve la partie d'un vecteur située dans une direction choisie. Elle préparera les moindres carrés et l'ACP.

---

## Concepts essentiels — Les dimensions

On note $X\in\mathbb{R}^{n\times p}$ la table de données : $n$ journées et $p$ variables.

Une ligne $x_i$ contient les $p$ caractéristiques d'une journée. Pour les formules, nous la représentons par un vecteur colonne de taille $p$.

Exemple : $x=(12,3,4)^T$ signifie 12 °C, 3 occupants et un indice d'équipement de 4. Cet indice est une variable simulée du projet.

L'ordre des colonnes doit rester identique lors de toutes les comparaisons.

---

## Concepts essentiels — Produit scalaire

$$
x^Tz=\sum_{j=1}^{p}x_jz_j.
$$

Chaque coordonnée de $x$ est multipliée par la coordonnée correspondante de $z$, puis les produits sont additionnés. Le résultat est un nombre.

Avec $x=(3,4)^T$ et $z=(4,3)^T$ : $x^Tz=3\times4+4\times3=24$.

Dans un modèle linéaire, $x^Tw$ combine les caractéristiques $x_j$ avec les poids $w_j$.

---

## Concepts essentiels — Normes L1 et L2

Une norme mesure la taille d'un vecteur.

$$
\|x\|_1=\sum_j|x_j|,\qquad \|x\|_2=\sqrt{\sum_jx_j^2}.
$$

Pour $x=(3,4)^T$, la norme L1 vaut $3+4=7$ et la norme L2 vaut $\sqrt{9+16}=5$.

L2 correspond à la longueur géométrique usuelle. L1 additionne les amplitudes. Ces deux notions réapparaîtront dans la régularisation.

---

## Concepts essentiels — Distance euclidienne

$$
d(x,z)=\|x-z\|_2.
$$

On soustrait les coordonnées, puis on mesure la longueur du vecteur obtenu.

Pour $x=(3,4)^T$ et $z=(4,3)^T$ : $d=\sqrt{(-1)^2+1^2}=\sqrt{2}\approx1{,}414$.

Une distance nulle signifie que les deux vecteurs sont identiques. Elle ne signifie pas seulement qu'ils ont la même direction.

---

## Explication détaillée — L'échelle change le voisin

Comparer directement une surface en m², une température en °C et un nombre de personnes donne une géométrie dominée par les grandes amplitudes numériques.

On peut d'abord choisir des échelles métier fixes : diviser les températures par 10 et le nombre d'occupants par 1, par exemple. Le choix doit être justifié.

Après le chapitre de centrage-réduction, nous comparerons ce choix avec une standardisation ajustée sur les seules données d'apprentissage.

Changer l'échelle modifie la question posée à la distance.

---

## Concepts essentiels — Similarité cosinus

Pour deux vecteurs non nuls :

$$
\operatorname{cos}(x,z)=\frac{x^Tz}{\|x\|_2\|z\|_2}.
$$

Le numérateur mesure l'alignement ; les normes retirent l'effet des longueurs. La valeur appartient à $[-1,1]$.

Avec $(3,4)^T$ et $(4,3)^T$, on obtient $24/(5\times5)=0{,}96$.

Le cosinus mesure une ressemblance de direction. Il n'est pas défini pour un vecteur nul.

---

## Exemple concret — Même direction, autre intensité

Prenons $x=(1,2)^T$ et $z=(2,4)^T$.

Le produit scalaire vaut $10$ et les normes valent $\sqrt5$ et $2\sqrt5$. Leur cosinus vaut donc $1$.

Pourtant, la distance est $\sqrt5$ : les valeurs de $z$ sont deux fois plus grandes.

Pour chercher un profil de répartition, le cosinus peut convenir. Pour comparer des niveaux de consommation, il peut masquer une différence essentielle.

---

## Concepts essentiels — Orthogonalité et projection

Deux vecteurs sont orthogonaux lorsque leur produit scalaire est nul.

Pour un vecteur unitaire $u$, de norme 1, la projection de $x$ sur sa direction est :

$$
\widehat{x}=(u^Tx)u.
$$

Avec $u=(1,0)^T$ et $x=(3,4)^T$, le coefficient $u^Tx=3$ ; la projection est $(3,0)^T$.

Le résidu $r=x-\widehat{x}=(0,4)^T$ est orthogonal à $u$ : $u^Tr=0$.

---

## Voir la projection et la similarité

![À gauche, le vecteur (3,4), sa projection horizontale et son résidu vertical ; à droite, les vecteurs (1,2) et (2,4) ont la même direction mais des longueurs différentes.](../figures/geometrie-projection.svg)

---

## Lecture des formules — Projeter sur plusieurs axes

Si les colonnes de $Q\in\mathbb{R}^{p\times k}$ sont orthonormées, alors $Q^TQ=I_k$ et :

$$
\widehat{x}=QQ^Tx.
$$

$Q^Tx$ donne les $k$ coordonnées de $x$ sur les axes conservés. $Q$ les reconstruit dans l'espace de départ.

Avec $Q=(1,0)^T$ et $x=(3,4)^T$, on retrouve $(3,0)^T$.

Cette formule ne s'applique pas directement à une matrice de colonnes quelconques. La condition d'orthonormalité est essentielle.

---

## Lecture du code — Comparer des profils

```python
import numpy as np

def cosinus(x, z):
    nx, nz = np.linalg.norm(x), np.linalg.norm(z)
    if nx < 1e-12 or nz < 1e-12:
        raise ValueError("Cosinus indéfini pour un vecteur nul")
    return float(x @ z / (nx * nz))

print(cosinus(np.array([3., 4.]), np.array([4., 3.])))
```

**Fonctionnement :** `x` et `z` sont deux vecteurs de même taille. `@` produit leur produit scalaire ; la fonction renvoie un nombre.

**Exécution et résultat attendu :** calcul des normes, contrôle, division ; affichage `0.96`.

**Erreur fréquente :** remplacer `@` par `*`, qui produit ici deux multiplications séparées.

---

## Algorithme expliqué — Retrouver une journée proche

**Objectif :** trouver un profil connu ressemblant à une nouvelle journée.

**Entrées :** une matrice de journées d'apprentissage et une requête, avec les mêmes colonnes et les mêmes échelles.

**Traitement :** calculer un score pour chaque ligne, exclure les vecteurs nuls, puis classer les scores.

**Sortie :** l'identifiant du meilleur profil et son score. Pour les directions $(1,0)$, $(0,1)$ et la requête $(1,0)$, les scores sont 1 et 0 : le premier profil est choisi.

Cette recherche ne constitue pas encore un modèle de prévision.

---

## Erreurs fréquentes

- Mélanger les unités ou changer l'ordre des variables.
- Prendre la valeur maximale d'une distance pour trouver le voisin le plus proche.
- Confondre cosinus élevé et niveaux identiques.
- Diviser par la norme d'un vecteur nul.
- Interpréter une proximité comme une relation causale.

---

## Exercice 1 — Lire une projection

**Objectif pédagogique :** relier les calculs à la géométrie. **Prérequis :** produit scalaire et norme L2.

**Énoncé :** pour $x=(3,4)^T$ et $u=(1,0)^T$, calculer la norme de $x$, sa projection sur $u$ et le résidu.

**Contraintes :** faire d'abord les calculs à la main. **Livrable attendu :** trois résultats et une phrase d'interprétation.

**Critères de réussite :** la projection est parallèle à $u$ et le résidu est orthogonal à $u$.

<details><summary>Indices gradués</summary>

1. Vérifier que $u$ est unitaire.
2. Calculer $(u^Tx)u$, puis soustraire le résultat à $x$.
</details>

---

## Correction — Lire une projection

<details><summary>Afficher la correction</summary>

La norme est $\sqrt{3^2+4^2}=5$. La projection est $(3,0)^T$. Le résidu vaut $(0,4)^T$ et son produit scalaire avec $u$ est nul.

```python
import numpy as np
x, u = np.array([3., 4.]), np.array([1., 0.])
projection = (u @ x) * u
residu = x - projection
print(np.linalg.norm(x), projection, u @ residu)
```

**Lecture et exécution :** les entrées sont `x` et `u` ; la projection est calculée, puis le résidu. La sortie est `5.0 [3. 0.] 0.0`. Il ne faut pas appliquer cette formule à un `u` non unitaire sans le normaliser.
</details>

---

## Exercice 2 — Choisir une proximité

**Objectif pédagogique :** choisir une mesure selon le besoin. **Prérequis :** distance et cosinus.

**Énoncé :** une requête vaut $(1,2)^T$. Les profils A et B valent $(2,4)^T$ et $(1,3)^T$. Quel profil choisir pour retrouver une direction ? Pour retrouver des valeurs proches ?

**Contraintes :** calculer les deux mesures. **Livrable attendu :** un tableau et deux décisions justifiées.

**Critères de réussite :** distinguer le classement par cosinus et celui par distance.

<details><summary>Indices gradués</summary>

1. A est un multiple de la requête.
2. Comparer les distances $\sqrt5$ et 1.
</details>

---

## Correction — Choisir une proximité

<details><summary>Afficher la correction</summary>

A : cosinus $1$ et distance $\sqrt5\approx2{,}236$.

B : cosinus $7/\sqrt{50}\approx0{,}990$ et distance $1$.

A conserve exactement la direction. B conserve mieux les valeurs. Il n'existe pas de « meilleur voisin » indépendant de la question choisie.
</details>

---

## Exercice 3 — Corriger un classement

**Objectif pédagogique :** déboguer et justifier un choix. **Prérequis :** tableaux NumPy et cosinus.

**Énoncé :** un programme utilise `scores = X * q`, puis `np.argmax(scores)`. Corriger le calcul pour classer les lignes de `X` par cosinus avec `q`.

**Contraintes :** traiter les lignes nulles ; refuser une requête nulle. **Livrable attendu :** une fonction et un exemple.

**Critères de réussite :** un score par ligne, aucune division par zéro et premier résultat justifié.

<details><summary>Indices gradués</summary>

1. `X @ q` fournit un produit scalaire par ligne.
2. `np.linalg.norm(X, axis=1)` fournit une norme par ligne.
</details>

---

## Correction — Corriger un classement

<details><summary>Afficher la correction</summary>

```python
import numpy as np
X = np.array([[0., 0.], [1., 2.], [1., 0.]])
q = np.array([1., 2.])
nq = np.linalg.norm(q)
if nq < 1e-12:
    raise ValueError("Requête nulle")
normes = np.linalg.norm(X, axis=1)
scores = np.full(len(X), -np.inf)
valides = normes > 1e-12
scores[valides] = (X[valides] @ q) / (normes[valides] * nq)
print(np.argmax(scores))
```

**Lecture du code :** les entrées sont `X` et `q`. Le masque `valides` exclut la ligne nulle ; `-inf` l'empêche de gagner le classement. La sortie est l'indice `1`, la deuxième ligne. Ne pas aplatir les produits élément par élément avant `argmax`.
</details>

---

## Projet fil rouge — Jalon 1

Le [projet consommation](../../Projet_IA/README.md) prolonge le TP de modélisation avec 240 journées **simulées**. Faire évoluer le même fichier `depart.py` pendant les six jalons.

**Notions mobilisées :** vecteurs, échelles et proximité. **Fonctionnalité à produire :** retrouver trois journées d'apprentissage proches d'une journée de validation, sans utiliser sa consommation.

**Résultat vérifiable :** trois identifiants et leurs scores ; contrôle manuel du premier. **À observer :** confusion entre direction et niveau, utilisation de la cible dans la distance.

**Livrable :** fonction de recherche et choix argumenté d'échelles fixes. La standardisation sera introduite au jalon 3.

---

## Cas d'usage réels

**Entreprise :** service de maintenance de bâtiments, scénario pédagogique.

**Problème :** retrouver des situations de fonctionnement comparables avant d'examiner une anomalie.

**Solution :** représenter les journées par les mêmes variables et comparer des profils après mise à l'échelle justifiée.

**Bénéfice attendu :** rendre la comparaison explicable. Une journée proche reste un indice, pas une preuve de panne ni une explication causale.

---

## Fiche de révision

- Une ligne représente une observation ; une colonne, une variable.
- Une norme mesure une taille ; une distance mesure un écart.
- Le cosinus compare des directions et exclut les vecteurs nuls.
- Une projection conserve la composante portée par un axe.
- Les échelles participent à la définition de la proximité.

---

## Questions de révision

1. Pourquoi deux profils de cosinus 1 peuvent-ils être éloignés ?
2. Pourquoi le produit scalaire de deux vecteurs orthogonaux est-il nul ?
3. Que change la conversion des mètres en centimètres dans une distance brute ?
4. Que représente le résidu après une projection orthogonale ?
5. Pourquoi la consommation à prédire ne doit-elle pas servir à chercher les voisins ?

---

## QCM — Questions 1 et 2

**1. La norme L2 de $(3,4)^T$ vaut :** A. 7 ; B. 25 ; C. 5 ; D. 12.

**2. Pour deux vecteurs non nuls, un cosinus de 1 indique :** A. des coordonnées égales ; B. la même direction et le même sens ; C. l'orthogonalité ; D. une distance nulle.

<details><summary>Afficher la correction</summary>

1. **C** : $\sqrt{9+16}=5$.
2. **B** : les longueurs peuvent être différentes.
</details>

---

## QCM — Questions 3 à 5

**3. Quelle opération donne un produit scalaire par ligne ?** A. `X * q` ; B. `X + q` ; C. `X @ q` ; D. `X.T + q`.

**4. Avant de projeter par $(u^Tx)u$, il faut vérifier :** A. $\|u\|=1$ ; B. $\|x\|=1$ ; C. $x=u$ ; D. $u=0$.

**5. Quel choix influence les voisins trouvés ?** A. uniquement le nombre de lignes ; B. uniquement leur ordre ; C. le nom du fichier ; D. l'échelle des variables.

<details><summary>Afficher la correction</summary>

3. **C** : le produit matrice-vecteur combine chaque ligne.
4. **A** : la formule donnée suppose un axe unitaire.
5. **D** : la distance dépend de l'unité et de la pondération des coordonnées.
</details>

---

## Résumé final

Nous pouvons représenter, comparer et projeter les journées.
Une géométrie doit correspondre à la question métier.
La prochaine étape consiste à projeter une cible sur les colonnes d'une matrice : c'est l'idée des moindres carrés.

[Continuer : régression multivariée](02_moindres_carres.md).

Référence : [NumPy — normes](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html).
