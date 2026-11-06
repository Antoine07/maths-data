---
marp: true
html: true
---

# Du modèle linéaire au réseau de neurones

## Classification et rétropropagation

![Un petit réseau relie trois entrées à une couche cachée et une sortie ; les gradients parcourent ensuite le calcul en sens inverse.](../images/couverture-reseau.svg)

Prérequis : [produits matriciels](../matrice.md), [calcul différentiel](04_calcul_differentiel.md) et [optimisation](05_optimisation.md).

---

## Objectif

Comprendre le trajet d'une observation dans un petit réseau, puis celui des gradients en sens inverse.

Nous commencerons par une classification logistique et ajouterons une seule couche cachée. Les calculs NumPy seront vérifiés numériquement ; une comparaison avec PyTorch est proposée en extension.

Durée indicative : 5 h avec le TP et son interprétation.

---

## Résumé général

Une régression prédit une quantité ; une classification estime ici la probabilité d'une journée à forte consommation.

Un réseau compose des transformations affines et des activations. La rétropropagation calcule les gradients de cette composition ; un optimiseur les utilise ensuite pour mettre à jour les paramètres.

La complexité supplémentaire doit être évaluée face à un modèle de référence, sur les mêmes partitions.

---

## Concepts essentiels — Définir la cible binaire

Fixons un seuil $s$ à partir de l'apprentissage uniquement. La cible vaut $t_i=1$ si la consommation $y_i>s$, et 0 sinon.

Exemple : avec $s=12$ kWh, les consommations 10 et 15 deviennent les classes 0 et 1.

Dans le projet, $s$ est la médiane des consommations d'apprentissage. Il reste identique en validation et en test.

La consommation observée sert à construire l'étiquette après la journée ; elle n'est pas une variable d'entrée disponible avant la prévision.

---

## Concepts essentiels — Logit et sigmoïde

$$
z_i=a_i^T\theta,\qquad p_i=\sigma(z_i)=\frac{1}{1+e^{-z_i}}.
$$

$a_i$ est la ligne des caractéristiques avec la constante ; $z_i$ est le score brut, appelé logit ; $p_i$ est une probabilité modélisée entre 0 et 1.

Pour $z=0$, $p=0{,}5$. Pour $z=\ln3$, $p=3/4$.

La décision par défaut vaut 1 si $p\ge0{,}5$. Ce seuil de décision est différent du seuil de consommation $s$ utilisé pour définir la cible.

---

## Concepts essentiels — Perte binaire

$$
L=-\frac1n\sum_i[t_i\log p_i+(1-t_i)\log(1-p_i)].
$$

La perte pénalise une forte confiance dans la mauvaise classe. Elle travaille sur les probabilités, avant le seuil de décision.

Pour une observation de classe 1, une probabilité 0,8 donne $-\log(0{,}8)\approx0{,}223$ ; une probabilité 0,2 donne environ 1,609.

Les logarithmes sont naturels. On ne calcule pas cette expression naïvement lorsque les probabilités sont très proches de 0 ou 1.

---

## Lecture des formules — Une perte stable avec les logits

La même perte s'écrit :

$$
L=\frac1n\sum_i[\log(1+e^{z_i})-t_i z_i].
$$

`np.logaddexp(0, z)` calcule le premier terme de façon stable. La dérivée par rapport au logit est $(p_i-t_i)/n$.

Exemple : pour $z=0$ et $t=1$, la perte vaut $\log2\approx0{,}693$ et la dérivée vaut -0,5 pour une seule observation.

Un calcul de `np.exp(1000)` déborderait ; la formule stable conserve une valeur finie pour cette entrée.

---

## Lecture du code — Classification logistique

```python
import numpy as np
def perte_gradient(A, t, theta):
    z = A @ theta
    p = np.exp(-np.logaddexp(0, -z))
    perte = np.mean(np.logaddexp(0, z) - t*z)
    gradient = A.T @ (p - t) / len(t)
    return perte, gradient

A, t, theta = np.array([[1., 2.]]), np.array([1.]), np.zeros(2)
print(perte_gradient(A, t, theta))
```

**Fonctionnement :** les entrées sont une matrice de caractéristiques, des classes 0/1 et des paramètres. La fonction renvoie une perte scalaire et un gradient de même taille que `theta`.

**Exécution et résultat attendu :** perte proche de 0,693 et gradient `[-0.5, -1.]`.

**Erreur fréquente :** dériver les prédictions déjà arrondies en classes ; le seuillage n'intervient pas dans la perte d'apprentissage.

---

## Lire la probabilité et la perte

![À gauche, la sigmoïde transforme les logits en probabilités ; à droite, la perte augmente lorsque le logit exprime une certitude contraire à la classe réelle.](../figures/sigmoide-perte.svg)

Le seuil de décision n'intervient pas dans le calcul de la perte différentiable.

---

## Concepts essentiels — Une couche cachée

Pour $X\in\mathbb{R}^{n\times p}$ et $h$ neurones :

$$
Z_1=XW_1+b_1,\quad H=\tanh(Z_1),\quad Z_2=HW_2+b_2.
$$

Dimensions : $W_1$ est $p\times h$, $b_1$ contient $h$ nombres, $H$ est $n\times h$, $W_2$ est $h\times1$ et $b_2$ contient un nombre.

Chaque biais est ajouté à toutes les lignes correspondantes. Les logits de sortie deviennent des probabilités avec la sigmoïde.

Exemple de taille : avec 3 variables et 4 neurones, il y a $3\times4+4+4\times1+1=21$ paramètres.

---

## Explication détaillée — Pourquoi une activation ?

Sans activation, deux transformations affines successives se regroupent en une seule transformation affine. Empiler des couches linéaires ne crée donc pas une relation non linéaire avec les entrées.

La tangente hyperbolique transforme un nombre en une valeur entre -1 et 1 ; $\tanh(0)=0$. Sa dérivée vaut $1-\tanh^2(z)$, donc 1 en 0.

Lorsque son entrée est très grande en valeur absolue, la sortie sature et la dérivée devient petite. La standardisation et une initialisation mesurée peuvent aider, sans garantir un apprentissage réussi.

---

## Exemple concret — Un neurone, à la main

Prenons une entrée $x=1$, un poids caché $w_1=0$, un biais caché nul, un poids de sortie $w_2=2$ et un biais de sortie nul.

La propagation donne $z_1=0$, $h=\tanh(0)=0$, $z_2=0$ et $p=0{,}5$.

Pour une cible 1, la perte vaut $\log2$. Le gradient du logit est -0,5 ; celui de $w_2$ vaut $h(-0{,}5)=0$.

En revanche, le gradient de $w_1$ vaut $x(1-h^2)w_2(-0{,}5)=-1$. Un poids de sortie nul aurait bloqué ce trajet de gradient sur cet exemple.

---

## Algorithme expliqué — Rétropropagation

**Entrées :** données, classes, paramètres et valeurs intermédiaires de la propagation.

**Traitement :** partir de la dérivée de la perte aux logits ; calculer les gradients de la sortie ; traverser l'activation ; calculer ceux de la couche cachée.

**Sorties :** un gradient pour chacun des quatre tableaux de paramètres.

**Exemple pas à pas :** dans l'exemple précédent, la sensibilité -0,5 devient -1 après multiplication par le poids de sortie 2, reste -1 à travers l'activation en 0, puis donne -1 pour le poids d'entrée puisque $x=1$.

La rétropropagation calcule les gradients. La descente de gradient est l'étape distincte qui modifie les paramètres.

---

## Un graphe de calcul vérifiable

![Les données traversent deux transformations affines séparées par tanh. La perte est calculée à partir des logits ; les gradients reviennent en sens inverse.](images/reseau-calcul.svg)

---

## Lecture des formules — Revenir vers la sortie

En conservant une sortie de taille $n\times1$, notons :

$$
G_2=\frac{P-T}{n},\qquad
\nabla_{W_2}L=H^TG_2,\quad
\nabla_{b_2}L=\sum_i(G_2)_i.
$$

$P$ contient les probabilités et $T$ les classes. La moyenne sur le lot est déjà dans $G_2$ : on ne la divise pas une seconde fois dans chaque gradient.

Pour un neurone caché donnant $h=0{,}4$ et une erreur de probabilité -0,5 sur une seule ligne, le gradient de son poids de sortie vaut -0,2.

---

## Lecture des formules — Revenir vers l'entrée

$$
G_1=(G_2W_2^T)\odot(1-H^2),\qquad
\nabla_{W_1}L=X^TG_1,\quad
\nabla_{b_1}L=\sum_i(G_1)_i.
$$

$\odot$ désigne un produit élément par élément. $G_1$ a la même taille que la couche cachée, $n\times h$.

Le premier facteur ramène l'erreur à chaque neurone ; le second applique la dérivée de son activation.

Exemple scalaire : $G_2=-0{,}5$, $w_2=2$ et $h=0$ donnent $G_1=-1$. Avec $x=1$, le gradient de $w_1$ vaut -1.

---

## Lecture du code — Les quatre gradients

```python
# X, H, W2, probabilites et classes proviennent de la propagation.
# Ici, probabilites et classes sont des vecteurs de taille (n,).
G2 = (probabilites - classes)[:, None] / len(classes)
dW2 = H.T @ G2
db2 = G2.sum(axis=0)
G1 = (G2 @ W2.T) * (1 - H**2)
dW1 = X.T @ G1
db1 = G1.sum(axis=0)
```

**Fonctionnement :** `[:, None]` crée la colonne de sortie. `@` combine les directions ; `*` applique les dérivées de l'activation coordonnée par coordonnée.

**Exécution et résultat attendu :** les gradients ont les tailles respectives de `W1`, `b1`, `W2`, `b2`. Avec le neurone de l'exemple : gradients de poids -1 et 0, gradients de biais -1 et -0,5.

**Erreur fréquente :** remplacer `* (1-H**2)` par un produit matriciel.

---

## Vérifier avant d'entraîner

Utiliser les différences finies du chapitre précédent sur chaque coordonnée d'un tout petit réseau. La correction fournie contrôle les quatre tableaux de paramètres en précision double.

Une initialisation identique de tous les neurones peut les maintenir symétriques. Utiliser une petite initialisation aléatoire reproductible, avec une graine fixée.

Le module facultatif [verification_pytorch.py](../../Projet_IA/verification_pytorch.py) calcule ensuite la même perte avec `binary_cross_entropy_with_logits` et compare tous les gradients avec `autograd`.

`backward()` accumule les gradients dans PyTorch : une boucle d'entraînement doit les remettre à zéro à chaque itération, par exemple avec `optimizer.zero_grad()`.

---

## Évaluer sans promettre une victoire du réseau

Comparer la classe majoritaire d'apprentissage, la régression logistique et le petit réseau. Fixer les seuils avant le test et examiner aussi la matrice de confusion.

L'exactitude est le nombre de décisions correctes divisé par le nombre d'observations. Exemple : 8 bonnes décisions sur 10 donnent 80 %.

Elle peut masquer une classe rare. Le rappel d'une classe est la part de ses observations réellement retrouvées : 3 alertes détectées sur 5 donnent 60 % de rappel.

Dans le projet, les partitions chronologiques ont des fréquences de classes différentes. Le petit réseau n'est pas nécessairement meilleur que le modèle logistique.

---

## Erreurs fréquentes

- Utiliser la consommation observée comme variable pour prédire sa propre classe.
- Dériver une décision seuillée plutôt qu'une perte sur logits.
- Oublier la dérivée de l'activation ou diviser deux fois par le nombre de lignes.
- Déclarer un réseau supérieur parce que sa perte d'apprentissage est plus faible.
- Interpréter une probabilité produite par une sigmoïde comme automatiquement bien calibrée.

---

## Exercice 1 — Lire les dimensions d'un réseau

**Objectif pédagogique :** vérifier les produits et compter les paramètres. **Prérequis :** dimensions matricielles.

**Énoncé :** pour 10 observations, 3 variables et 4 neurones cachés, donner les dimensions de chaque tableau et le nombre de paramètres.

**Contraintes :** conserver une sortie colonne. **Livrable attendu :** un tableau de tailles et le total.

**Critères de réussite :** propagation compatible et 21 paramètres, indépendamment des 10 observations.

<details><summary>Indices gradués</summary>

1. Chaque neurone caché reçoit trois poids et un biais.
2. La sortie reçoit quatre poids et un biais.
</details>

---

## Correction — Lire les dimensions d'un réseau

<details><summary>Afficher la correction</summary>

`X` : `(10,3)` ; `W1` : `(3,4)` ; `b1` : `(4,)` ; `H` : `(10,4)` ; `W2` : `(4,1)` ; `b2` : `(1,)` ; logits : `(10,1)`.

Le total est $12+4+4+1=21$. Les gradients reprennent les dimensions des paramètres ; ils ne contiennent pas une nouvelle dimension de taille 10.
</details>

---

## Exercice 2 — Rétropropager à la main

**Objectif pédagogique :** vérifier chaque facteur de la chaîne. **Prérequis :** sigmoïde, tangente hyperbolique et perte binaire.

**Énoncé :** reprendre le neurone avec $x=1$, $w_1=b_1=b_2=0$, $w_2=2$ et cible 1. Calculer les quatre gradients et une mise à jour avec un pas de 0,1.

**Contraintes :** calculer tous les gradients avant de modifier un paramètre. **Livrable attendu :** propagation, gradients et nouveaux paramètres.

**Critères de réussite :** respecter le signe et la règle de chaîne.

<details><summary>Indices gradués</summary>

1. Le logit est nul, donc la probabilité vaut 0,5.
2. Le gradient du biais de sortie vaut -0,5 ; remonter ensuite vers la couche cachée.
</details>

---

## Correction — Rétropropager à la main

<details><summary>Afficher la correction</summary>

Gradients : $dw_1=-1$, $db_1=-1$, $dw_2=0$, $db_2=-0{,}5$.

Après soustraction de 0,1 fois chaque gradient : $w_1=0{,}1$, $b_1=0{,}1$, $w_2=2$, $b_2=0{,}05$.

La nouvelle entrée cachée vaut 0,2, puis le logit devient positif. La probabilité de la classe 1 augmente et la perte de cette observation diminue.

Modifier `w2` avant de calculer `G1` mélangerait des paramètres de deux étapes différentes.
</details>

---

## Exercice 3 — Déboguer et comparer

**Objectif pédagogique :** détecter un gradient incorrect et justifier un protocole. **Prérequis :** rétropropagation et validation.

**Énoncé :** un programme calcule `G1 = G2 @ W2.T`, sans dérivée d'activation, puis choisit le nombre d'itérations sur le test. Corriger les deux erreurs et vérifier le gradient numériquement.

**Contraintes :** même partition pour réseau et modèle logistique ; aucun réglage sur le test. **Livrable attendu :** code corrigé, écart de gradient et tableau comparatif.

**Critères de réussite :** accord numérique sur les quatre tableaux et choix des paramètres sur validation.

<details><summary>Indices gradués</summary>

1. La chaîne doit traverser la tangente hyperbolique.
2. Comparer deux modèles exige de garder une évaluation finale commune.
</details>

---

## Correction — Déboguer et comparer

<details><summary>Afficher la correction</summary>

Remplacer par `(G2 @ W2.T) * (1 - H**2)`. Utiliser le produit élément par élément pour la dérivée d'activation.

Conserver pour chaque modèle les paramètres donnant la meilleure perte de validation. Le script `correction.py --verifier` contrôle numériquement les quatre gradients sur un petit réseau ; il compare ensuite les modèles une fois les choix figés.

Une meilleure performance du modèle logistique constitue un résultat valable. La complexité d'un réseau demande une justification empirique.
</details>

---

## Projet fil rouge — Jalon 6

Dans le [projet consommation](../../Projet_IA/README.md), conserver le jeu de données, la standardisation et les partitions des cinq premiers jalons.

**Notions mobilisées :** logistique, réseau et rétropropagation. **Fonctionnalité :** estimer la probabilité d'une journée au-dessus du seuil défini sur l'apprentissage.

**Résultat vérifiable :** gradients validés numériquement ; comparaison de la référence, de la logistique et d'un réseau à quatre neurones. Sur les données fournies, la logistique obtient 48/48 décisions correctes et le réseau 47/48 ; ce petit test synthétique n'est pas une preuve de supériorité générale.

**Livrables :** paramètres sauvegardés, pertes de validation, confusion et commentaire des erreurs. **À observer :** fuite de cible et confiance excessive dans l'exactitude.

---

## Cas d'usage réels

**Entreprise :** service d'exploitation d'un bâtiment, scénario pédagogique.

**Problème :** anticiper une journée de forte demande pour planifier les équipements.

**Solution :** comparer un classifieur simple et un petit réseau sur les caractéristiques connues avant la journée.

**Bénéfice attendu :** une alerte assortie d'une évaluation explicite. Les faux négatifs et faux positifs ont des conséquences différentes ; leur coût doit guider un éventuel changement de seuil, choisi avant l'évaluation finale.

---

## Problème — Une bonne exactitude peut masquer de mauvaises alertes

Un détecteur atteint 99 % d'exactitude sur une population où les défauts sont rares. Quelle proportion de ses alertes correspond vraiment à un défaut ?

[Explorer les fausses alertes et la fréquence de base](../../Tps/Paradoxes/06_fausses_alertes.md).

Revenir aux effectifs de confusion, distinguer les dénominateurs et introduire Bayes à partir des comptes.

---

## Fiche de révision

- Une sigmoïde convertit un logit en probabilité modélisée.
- La perte est calculée avant le seuillage des décisions.
- L'activation rend le réseau non linéaire.
- La rétropropagation applique la règle de chaîne à chaque étage.
- Le réseau doit être comparé à des références, avec les mêmes données et un test réservé.

---

## Questions de révision

1. Quelle différence entre le seuil de consommation et le seuil de probabilité ?
2. Pourquoi deux couches affines sans activation ne suffisent-elles pas à créer une non-linéarité ?
3. Quelle différence entre rétropropagation et descente de gradient ?
4. Pourquoi vérifier les gradients sur un petit réseau avant l'entraînement ?
5. Que masque parfois une bonne exactitude sur une classe rare ?

---

## QCM — Questions 1 et 2

**1. Un logit nul donne une probabilité :** A. 0 ; B. 1 ; C. 0,5 ; D. indéfinie.

**2. La rétropropagation calcule principalement :** A. les gradients ; B. les partitions ; C. le seuil métier ; D. la variance expliquée.

<details><summary>Afficher la correction</summary>

1. **C** : $1/(1+e^0)=1/2$.
2. **A** : l'optimiseur utilise ensuite ces gradients pour les mises à jour.
</details>

---

## QCM — Questions 3 à 5

**3. La dérivée de `tanh(z)` vaut :** A. `tanh(z)` ; B. `1 - tanh(z)**2` ; C. `z**2` ; D. toujours 0.

**4. Un réseau plus complexe est-il nécessairement meilleur sur le test ?** A. toujours ; B. si sa perte d'apprentissage est faible ; C. si ses poids sont nombreux ; D. non.

**5. Pour une perte binaire stable, on préfère :** A. arrondir d'abord les probabilités ; B. calculer naïvement `exp(1000)` ; C. travailler à partir des logits avec une fonction adaptée ; D. supprimer les logarithmes.

<details><summary>Afficher la correction</summary>

3. **B** : la dérivée dépend de la sortie de l'activation.
4. **D** : la généralisation doit être mesurée.
5. **C** : `logaddexp` ou `binary_cross_entropy_with_logits` évitent les calculs naïfs fragiles.
</details>

---

## Résumé final

Le parcours relie désormais données, projections, gradients et apprentissage.
Un réseau est une composition dont on peut expliquer les valeurs et les dérivées.
La vérification numérique et les références simples restent indispensables.
L'évaluation finale porte sur des observations non utilisées pour choisir le modèle.

[Terminer le projet et consulter les livrables](../../Projet_IA/README.md).

Références : [PyTorch — Autograd](https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html), [perte binaire sur logits](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html).
