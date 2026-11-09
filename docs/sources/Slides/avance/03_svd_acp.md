---
marp: true
html: true
---

# SVD et réduction de dimension

## Comprendre, compresser et reconstruire

Ce chapitre approfondit [l'introduction à l'ACP](../stat/04_acp_intro.md). Prérequis : produits matriciels, projection orthogonale, covariance et centrage-réduction.

---

## Objectif

Décomposer une matrice, relier ses valeurs singulières à la variance et choisir combien de directions conserver.

Nous voulons distinguer **expliquer la variance**, **reconstruire les données** et **améliorer une prédiction** : ces objectifs ne sont pas équivalents.

---

## Résumé général

La SVD décrit une matrice par deux familles de directions et des amplitudes positives ou nulles.

En conservant les amplitudes les plus grandes, on obtient une approximation de rang faible. Sur des données centrées, les directions de droite correspondent aux axes de l'ACP.

La SVD s'applique aussi aux matrices rectangulaires. Elle permet d'étudier rang, reconstruction et stabilité dans un même langage.

---

## Concepts essentiels — Décomposition réduite

Pour $X\in\mathbb{R}^{n\times p}$, posons $m=\min(n,p)$ :

$$
X=U\Sigma V^T.
$$

Dimensions : $U$ est $n\times m$, $\Sigma$ est $m\times m$ diagonale et $V^T$ est $m\times p$.

Les colonnes de $U$ et de $V$ sont orthonormées. Les valeurs singulières $\sigma_1\ge\cdots\ge\sigma_m\ge0$ sont les éléments diagonaux de $\Sigma$.

Exemple : pour $X=\operatorname{diag}(3,1)$, on peut choisir $U=V=I_2$ et $\Sigma=\operatorname{diag}(3,1)$.

---

## Lire les dimensions d'une SVD

![Une matrice n par p se décompose en U de taille n par m, Sigma de taille m par m et V transposée de taille m par p.](images/svd-facteurs.svg)

Vérifier chaque dimension avant d'écrire la reconstruction.

---

## Explication détaillée — Une somme de contributions

$$
X=\sum_{j=1}^{m}\sigma_j u_jv_j^T.
$$

$u_j$ est une colonne de $U$, $v_j$ une colonne de $V$. Leur produit extérieur est une matrice de rang au plus 1 ; $\sigma_j$ règle son amplitude.

Pour la matrice diagonale précédente, la première contribution conserve le 3 et la seconde conserve le 1.

Les signes de $u_j$ et $v_j$ peuvent être changés simultanément sans modifier leur contribution. Ne pas comparer deux SVD uniquement par le signe de leurs vecteurs.

---

## Concepts essentiels — Approximation de rang k

$$
X_k=U_k\Sigma_kV_k^T.
$$

L'indice $k$ signifie que l'on conserve les $k$ premières directions. Cette matrice est de rang au plus $k$.

Elle minimise l'erreur de reconstruction en norme de Frobenius parmi les matrices de rang au plus $k$. Si des valeurs singulières sont égales, plusieurs meilleures approximations peuvent exister.

Exemple : pour $X=\operatorname{diag}(3,1)$, $X_1=\operatorname{diag}(3,0)$.

---

## Lecture des formules — Mesurer la perte

La norme de Frobenius additionne les carrés de toutes les entrées, puis prend la racine :

$$
\|X-X_k\|_F^2=\sum_{j>k}\sigma_j^2.
$$

À droite : l'énergie des directions abandonnées. Avec les valeurs singulières 3 et 1, la reconstruction de rang 1 perd $1^2=1$.

L'énergie totale vaut $3^2+1^2=10$ ; conserver la première direction garde 90 % de l'énergie. Ce pourcentage se calcule avec les **carrés**, pas avec les valeurs singulières seules.

---

## Relier la SVD à l'ACP

Pour une matrice centrée $X_c$ de $n>1$ observations :

$$
C=\frac{X_c^TX_c}{n-1},\qquad
\lambda_j=\frac{\sigma_j^2}{n-1}.
$$

$C$ est la covariance d'échantillon. Ses vecteurs propres sont les directions $v_j$ ; ses valeurs propres $\lambda_j$ mesurent les variances sur ces directions.

Exemple : si $n=5$ et les valeurs singulières sont 4 et 2, les variances valent 4 et 1. Les parts expliquées sont 80 % et 20 %.

La SVD évite de former explicitement la covariance pour calculer ces directions.

---

## Projeter et reconstruire

$$
Z=X_cV_k,\qquad \widehat X=ZV_k^T+\mu.
$$

$Z\in\mathbb{R}^{n\times k}$ contient les nouvelles coordonnées. $\mu$ est la ligne des moyennes retirées avant la projection.

Exemple : $x=(3,4)$ et $V_1=(1,0)^T$ donnent la coordonnée 3, puis la reconstruction centrée $(3,0)$.

Pour des données standardisées, multiplier aussi chaque colonne reconstruite par son écart-type avant de réajouter sa moyenne.

---

## Lecture du code — ACP avec NumPy

```python
import numpy as np
X = np.array([[0., 0.], [1., 2.], [2., 4.]])
mu = X.mean(axis=0)
Xc = X - mu
U, s, Vt = np.linalg.svd(Xc, full_matrices=False)
k = 1
Z = Xc @ Vt[:k].T
reconstruction = Z @ Vt[:k] + mu
print(s, np.allclose(reconstruction, X))
```

**Fonctionnement :** `Vt` contient les directions en lignes ; `s` est un vecteur, pas une matrice diagonale.

**Exécution et résultat attendu :** les données sont parfaitement alignées ; valeurs singulières proches de `[3.162278, 0]`, reconstruction exacte à l'arrondi près, puis `True`.

**Erreur fréquente :** utiliser `Vt[:k]` au lieu de sa transposée pour la projection.

---

## Lire le spectre et l'erreur de reconstruction

![Sur les données du projet, deux axes conservent moins de 95 pour cent de variance ; l'erreur de reconstruction diminue jusqu'à zéro avec les trois axes.](../figures/svd-variance.svg)

Les axes sont appris sur l'apprentissage. L'erreur du second panneau est calculée sur la validation, avec ces mêmes axes.

---

## Choisir k sans forcer la compression

$$
q_k=\frac{\sum_{j=1}^{k}\sigma_j^2}{\sum_{j=1}^{m}\sigma_j^2}.
$$

$q_k$ est la part cumulée de variance pour une ACP centrée. Choisir le plus petit $k$ satisfaisant le seuil retenu.

Pour les énergies $(9,1)$, un seuil de 90 % autorise $k=1$ ; un seuil de 95 % impose $k=2$.

Si toutes les valeurs singulières sont nulles, les données centrées sont constantes : ce rapport est indéfini. Arrêter ce calcul et expliquer l'absence de variance.

Une direction de faible variance peut rester utile à une cible : l'ACP ne connaît pas cette cible.

---

## Algorithme expliqué — Appliquer l'ACP à de nouvelles données

**Entrées :** matrices d'apprentissage et de validation avec les mêmes colonnes.

**Traitement :** ajuster moyenne et éventuellement écart-type sur l'apprentissage ; transformer les deux tables avec ces mêmes paramètres ; calculer la SVD sur l'apprentissage ; choisir $k$ ; projeter la validation sur les axes conservés.

**Sorties :** axes, paramètres de transformation, nouvelles coordonnées et erreur de reconstruction.

**Exemple pas à pas :** retirer la moyenne $(1,2)$ des trois points précédents, retenir un axe, puis reconstruire les coordonnées de départ.

Calculer les axes sur toutes les données ferait entrer la validation et le test dans l'ajustement.

---

## Exemple concret — Compresser une image

Une image en niveaux de gris est une matrice $H\times W$. Sa SVD peut être tronquée sans effectuer de centrage : il s'agit alors de compression matricielle, pas nécessairement d'une ACP.

Les facteurs tronqués contiennent environ $k(H+W+1)$ nombres au lieu de $HW$.

Pour une image $100\times100$ et $k=5$, on stocke 1 005 nombres au lieu de 10 000. Cette comparaison compte les nombres, pas les octets d'un fichier JPEG.

Le rang choisi règle le compromis entre stockage et fidélité visuelle.

---

## Erreurs fréquentes

- Confondre valeurs propres et valeurs singulières.
- Oublier le centrage pour relier SVD et ACP.
- Conserver 95 % des valeurs singulières au lieu de 95 % de leurs carrés.
- Imposer un rang réduit même lorsque les données ne le permettent pas au seuil fixé.
- Ajuster la standardisation ou les axes sur les données de test.

---

## Exercice 1 — Calculer l'information conservée

**Objectif pédagogique :** lire un spectre. **Prérequis :** carrés et somme cumulée.

**Énoncé :** les valeurs singulières sont 4, 2 et 0. Calculer les parts d'énergie et le rang minimal pour garder 90 %.

**Contraintes :** calcul à la main. **Livrable attendu :** trois parts et une décision.

**Critères de réussite :** parts totalisant 1, distinction entre rang effectif et rang choisi.

<details><summary>Indices gradués</summary>

1. L'énergie totale vaut $16+4$.
2. Une seule direction conserve 80 %.
</details>

---

## Correction — Calculer l'information conservée

<details><summary>Afficher la correction</summary>

Les parts valent 80 %, 20 % et 0 %. Le rang de la matrice est 2 ; il faut retenir $k=2$ pour atteindre 90 %.

La direction de valeur singulière nulle n'apporte rien à la reconstruction. En calcul flottant, le rang numérique dépend d'une tolérance, pas d'une égalité exacte à zéro.
</details>

---

## Exercice 2 — Compresser une petite image

**Objectif pédagogique :** reconstruire et mesurer une erreur. **Prérequis :** SVD réduite et norme de Frobenius.

**Énoncé :** utiliser `image = np.diag([3., 1.])`. Reconstruire aux rangs 1 puis 2 et comparer les erreurs quadratiques.

**Contraintes :** passer par les facteurs SVD. **Livrable attendu :** deux matrices et deux erreurs.

**Critères de réussite :** erreur 1 au rang 1 et erreur proche de 0 au rang 2.

<details><summary>Indices gradués</summary>

1. Avec NumPy, `(U[:, :k] * s[:k])` multiplie chaque colonne par sa valeur singulière.
2. Multiplier ensuite par `Vt[:k]`.
</details>

---

## Correction — Compresser une petite image

<details><summary>Afficher la correction</summary>

```python
import numpy as np
image = np.diag([3., 1.])
U, s, Vt = np.linalg.svd(image, full_matrices=False)
for k in (1, 2):
    approx = (U[:, :k] * s[:k]) @ Vt[:k]
    print(k, np.linalg.norm(image - approx, "fro") ** 2)
```

**Lecture :** la boucle conserve successivement une puis deux directions. Les sorties sont `1 1.0` et `2 0.0`. Utiliser `s[:k]` comme une matrice dans un produit `@` donnerait des dimensions incorrectes.
</details>

---

## Exercice 3 — Déboguer une ACP

**Objectif pédagogique :** éviter la fuite de données et justifier les dimensions. **Prérequis :** centrage-réduction et projection.

**Énoncé :** un programme calcule `mu = X_total.mean(0)`, décompose `X_total - mu`, puis applique `X_validation @ Vt[:k]`. Identifier trois problèmes et proposer la transformation correcte.

**Contraintes :** ne pas consulter le test. **Livrable attendu :** ordre des opérations et formule corrigée.

**Critères de réussite :** paramètres appris sur `X_train`, centrage cohérent et sortie de taille `(n_validation, k)`.

<details><summary>Indices gradués</summary>

1. Sur quelles lignes les moyennes et les axes ont-ils été appris ?
2. Quelle dimension doit disparaître dans le produit matriciel ?
</details>

---

## Correction — Déboguer une ACP

<details><summary>Afficher la correction</summary>

Calculer `mu = X_train.mean(axis=0)`, puis la SVD de `X_train - mu`.

Transformer la validation par `(X_validation - mu) @ Vt[:k].T`. La moyenne vient de l'apprentissage ; le centrage est appliqué avant la projection ; la transposée donne les bonnes dimensions.

Si une standardisation est utilisée, son écart-type vient aussi de l'apprentissage. Ne pas réajuster les axes sur les nouvelles observations.
</details>

---

## Projet fil rouge — Jalon 3

Reprendre le [projet consommation](../../Projet_IA/README.md). Introduire maintenant la standardisation, ajustée seulement sur les 144 journées d'apprentissage, et réexaminer les voisins du jalon 1.

**Notions mobilisées :** covariance, SVD, projection et reconstruction. **Fonctionnalité :** proposer un nombre d'axes à 95 % de variance.

**Résultat vérifiable :** avec les trois variables du fichier fourni, les parts sont environ 40,24 %, 33,96 % et 25,80 % ; il faut donc garder les trois axes. Expliquer pourquoi il n'y a pas de compression au seuil demandé.

**Livrables :** paramètres de transformation, spectre, erreur de reconstruction et conclusion. **À observer :** suppression arbitraire d'un axe pour obtenir absolument deux dimensions.

---

## Projet fil rouge — Extension du même jalon

Ajouter temporairement une copie d'une colonne au tableau, sans modifier les partitions. Observer la valeur singulière nulle et la nouvelle possibilité de compression.

Puis retirer cette colonne redondante du modèle de référence. Le projet continue avec les mêmes variables d'origine.

TP complémentaire : remplacer la petite matrice de l'exercice 2 par une image en niveaux de gris ; comparer plusieurs rangs et l'erreur de reconstruction. L'affichage avec Matplotlib est facultatif.

---

## Problème — Ce qui est rare n'est pas forcément du bruit

Un tableau décrit de nombreuses sessions vidéo et une seule rencontre avec un proche. Que devient cette rencontre lorsque l'on conserve plus de 99 % de la variance ?

[Problème 3 : une rencontre peut-elle disparaître dans 99 % de variance ?](../../Tps/Tail_End/03_evenement_rare.md)

Objectif : distinguer la fidélité globale d'une reconstruction et la préservation de l'information utile.

---

## Cas d'usage réels

**Entreprise :** exploitant d'un réseau de capteurs, scénario pédagogique.

**Problème :** résumer plusieurs mesures redondantes sans stocker chaque série intégralement.

**Solution :** rechercher une représentation de rang faible puis mesurer l'erreur de reconstruction.

**Bénéfice attendu :** une représentation plus compacte lorsque les données possèdent effectivement des dépendances. Une bonne reconstruction ne garantit pas de conserver toutes les anomalies utiles.

---

## Fiche de révision

- La SVD réduit une matrice à des directions et des amplitudes.
- Les valeurs singulières sont positives ou nulles et rangées par ordre décroissant.
- En ACP centrée, les variances sont les carrés des valeurs singulières divisés par $n-1$.
- Les axes de projection sont les colonnes de $V$, donc les lignes de `Vt`.
- Le nombre d'axes doit être choisi selon un objectif explicite.

---

## Questions de révision

1. Pourquoi la SVD s'applique-t-elle à une matrice rectangulaire ?
2. Comment reconstruire les unités initiales après standardisation ?
3. Pourquoi deux logiciels peuvent-ils donner des signes opposés pour un axe ?
4. Que signifie une petite valeur singulière ?
5. Pourquoi une direction peu variable peut-elle rester utile à une classification ?

---

## QCM — Questions 1 et 2

**1. NumPy renvoie dans `s` :** A. une covariance ; B. un vecteur de valeurs singulières ; C. les moyennes ; D. une inverse.

**2. Sur des données centrées, les parts de variance utilisent :** A. $\sigma_j$ ; B. $1/\sigma_j$ ; C. $\sigma_j^2$ ; D. les signes des axes.

<details><summary>Afficher la correction</summary>

1. **B** : `s` est un vecteur de longueur `min(n, p)` en SVD réduite.
2. **C** : la variance est proportionnelle au carré de l'amplitude.
</details>

---

## QCM — Questions 3 à 5

**3. Pour projeter une matrice de taille `(n, p)` sur k axes :** A. `Xc @ Vt[:k].T` ; B. `Xc @ Vt[:k]` ; C. `Xc + U` ; D. `Xc * s`.

**4. Retenir 95 % de variance garantit :** A. 95 % d'exactitude ; B. aucune erreur ; C. un modèle causal ; D. ce seuil de variance sur l'apprentissage.

**5. Où ajuste-t-on les axes avant une évaluation ?** A. sur le test ; B. sur l'apprentissage ; C. sur toutes les données ; D. uniquement sur les cibles.

<details><summary>Afficher la correction</summary>

3. **A** : les dimensions donnent `(n, k)`.
4. **D** : ce seuil ne porte pas sur la performance prédictive.
5. **B** : la validation et le test n'ajustent pas les axes.
</details>

---

## Résumé final

La SVD relie rang, stabilité, ACP et reconstruction.
Réduire la dimension est un choix mesurable, pas une obligation.
Nous pouvons maintenant regrouper les observations et interpréter les profils obtenus, avant d'apprendre les paramètres des modèles prédictifs.

[Continuer : clustering et profils de consommation](08_clustering.md). Le parcours reprendra ensuite le [gradient et la Hessienne](../gradient.md).

Références : [NumPy — SVD](https://numpy.org/doc/stable/reference/generated/numpy.linalg.svd.html), [scikit-learn — ACP](https://scikit-learn.org/stable/modules/decomposition.html#pca).
