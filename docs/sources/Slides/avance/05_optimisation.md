---
marp: true
html: true
---

# Optimisation et régularisation

## Apprendre des paramètres de façon contrôlée

Prérequis : [gradient et Hessienne](../gradient.md), [moindres carrés](02_moindres_carres.md) et [calcul différentiel matriciel](04_calcul_differentiel.md).

---

## Objectif

Implémenter une descente de gradient, expliquer son comportement et choisir une pénalisation à l'aide de la validation.

Nous distinguerons trois questions : le programme minimise-t-il l'objectif choisi ? Cet objectif est-il bien conditionné ? Le modèle prévoit-il correctement de nouvelles observations ?

Durée indicative : 4 h avec les exercices et le jalon 5.

---

## Résumé général

Une descente de gradient met à jour les paramètres dans la direction opposée au gradient. Son pas contrôle la taille du déplacement.

La courbure et l'échelle des variables influencent la convergence. Une pénalisation L2 limite l'amplitude des poids et modifie l'objectif.

La validation sert à choisir les réglages ; le test évalue le modèle une fois ces choix figés.

---

## Concepts essentiels — La mise à jour

$$
\theta_{t+1}=\theta_t-\eta\nabla J(\theta_t).
$$

$t$ est le numéro d'itération ; $\eta>0$ est le pas d'apprentissage. Le gradient indique la direction locale de plus forte augmentation ; on se déplace dans le sens opposé.

Exemple : $J(\theta)=(\theta-3)^2/2$, $\theta_0=0$, $\eta=0{,}5$. Le gradient initial vaut -3 et le nouveau paramètre vaut 1,5.

Un grand déplacement peut quitter la zone où l'approximation locale est fiable.

---

## Algorithme expliqué — Descente complète

**Entrées :** objectif différentiable, gradient, paramètres initiaux, pas, nombre maximal d'itérations et tolérance.

**Traitement :** calculer perte et gradient, vérifier que les valeurs sont finies, mettre à jour, conserver un historique ; arrêter selon le critère choisi.

**Sorties :** paramètres et historique permettant de diagnostiquer la convergence.

**Exemple pas à pas :** pour la fonction précédente, les trois premières valeurs sont 1,5 ; 2,25 ; 2,625. Le minimum est 3 et l'écart est divisé par deux à chaque étape.

---

## Lecture du code — Une première descente

```python
theta = 0.0
pas = 0.5
for _ in range(3):
    gradient = theta - 3.0
    theta -= pas * gradient
    print(theta)
```

**Fonctionnement :** `theta` est le paramètre scalaire ; la boucle applique trois mises à jour avec le même pas.

**Exécution et résultat attendu :** `1.5`, `2.25`, `2.625`.

**Erreur fréquente :** utiliser `+=` au lieu de `-=` ferait monter l'objectif sur cet exemple.

---

## Concepts essentiels — Convexité et stationnarité

Sur un domaine convexe, une fonction convexe vérifie qu'aucun segment entre deux points de son graphe ne passe sous son graphe. Pour une fonction deux fois continûment différentiable sur un ouvert convexe, une Hessienne positive semi-définie en tout point caractérise la convexité.

Pour un objectif convexe différentiable sans contrainte, un gradient nul suffit pour un minimum global.

Exemple : $f(x)=x^2$ a une dérivée seconde 2 partout et un minimum global en 0. Pour $f(x)=x^3$, la dérivée est nulle en 0 mais ce point n'est pas un minimum.

Les pertes des réseaux de neurones sont généralement non convexes.

---

## Concepts essentiels — Courbure et pas

Pour une perte quadratique convexe de Hessienne constante $H$, notons $L$ sa plus grande valeur propre. Si $L>0$, le choix :

$$
0<\eta<\frac{2}{L}
$$

fait décroître les composantes d'erreur dans les directions de courbure positive. Avec une Hessienne définie positive, la descente converge vers l'unique minimum.

Exemple : pour $J(\theta)=(\theta-3)^2/2$, $L=1$. Le pas 0,5 converge ; le pas 2 produit une oscillation ; le pas 3 diverge depuis 0.

Cette borne concerne ici la quadratique et son gradient complet. Elle ne se transpose pas automatiquement à un réseau non linéaire ou à des mini-lots.

---

## Voir l'effet du pas sur la même fonction

![Trois descentes sur la même quadratique : le pas 0,5 converge, 1,8 converge en oscillant et 2,1 diverge. Le second panneau représente la perte en échelle logarithmique.](../figures/descente-pas.svg)

Les trois expériences ont le même point de départ. Seul le pas change.

---

## Explication détaillée — Pourquoi standardiser ?

Des directions de courbures très différentes produisent une vallée étroite : un pas acceptable sur un axe peut être trop grand sur l'autre.

La standardisation peut rendre les amplitudes plus comparables et accélérer la descente. Elle ne garantit pas un conditionnement parfait : des variables presque redondantes restent problématiques.

Les paramètres de standardisation sont appris sur l'apprentissage, puis réutilisés en validation et en test.

Exemple : convertir arbitrairement une variable de mètres en millimètres multiplie sa colonne par 1 000 ; les termes correspondants de la Hessienne peuvent alors changer d'un facteur $10^6$.

---

## Exemple concret — Une vallée étroite

Considérons $J(\theta_1,\theta_2)=(\theta_1^2+100\theta_2^2)/2$. Les deux paramètres sont sans unité dans cet exemple et le minimum est $(0,0)$.

La Hessienne vaut $\operatorname{diag}(1,100)$ : $L=100$. Depuis $(1,1)$, le gradient vaut $(1,100)$.

Avec un pas de 0,01, la première mise à jour donne $(0{,}99,0)$ ; avec un pas de 0,5, elle donne $(0{,}5,-49)$ et la perte augmente fortement.

Le pas doit respecter la direction la plus courbée, même si cela ralentit les autres directions.

---

## Concepts essentiels — Régularisation L2

Nous choisissons la convention :

$$
J_\lambda(\theta)=\frac{\|A\theta-y\|_2^2}{2n}
+\frac{\lambda}{2}\sum_{j=1}^{p}\theta_j^2.
$$

$\theta_0$ est la constante, non pénalisée ; $\lambda\ge0$ règle l'importance de la pénalité. Les variables sont standardisées avant la comparaison des poids.

Exemple : deux poids 2 et -1 donnent une pénalité $\lambda(4+1)/2$. Avec $\lambda=0{,}1$, elle vaut 0,25.

La pénalité introduit un compromis : mieux ajuster les observations ou garder des poids plus petits.

---

## Lecture des formules — Gradient régularisé

Avec $D=\operatorname{diag}(0,1,\ldots,1)$ :

$$
\nabla J_\lambda=\frac{A^T(A\theta-y)}{n}+\lambda D\theta.
$$

La première contribution réduit les résidus. La seconde ramène les poids, mais pas la constante, vers zéro.

Pour $\theta=(5,2,-1)^T$ et $\lambda=0{,}1$, le supplément de gradient vaut $(0,0{,}2,-0{,}1)^T$.

Ridge ne rend pas une variable causale et ne remplace pas une information manquante. Il impose un choix de préférence entre solutions possibles.

---

## Résoudre Ridge sans inverse explicite

La solution vérifie :

$$
(A^TA+n\lambda D)\theta=A^Ty.
$$

Une autre méthode consiste à appliquer `lstsq` à la matrice augmentée obtenue en empilant $A$ et $\sqrt{n\lambda}D$, et à la cible obtenue en ajoutant des zéros à $y$.

Pour $n=100$ et $\lambda=0{,}1$, le facteur ajouté vaut $\sqrt{10}$. Le carré reproduit le coefficient $n\lambda$ de l'équation.

Attention aux conventions : pour l'objectif `||Aθ-y||² + alpha*||w||²`, le paramètre correspondant vaut `alpha = n * lambda`.

---

## Concepts essentiels — L1, en prolongement

Une pénalité L1 utilise la somme des valeurs absolues des poids. Elle peut produire des coefficients exactement nuls et servir à sélectionner des variables.

Pour les poids $(2,-1)$, la norme L1 vaut 3, contre une norme L2 au carré égale à 5.

La valeur absolue n'est pas différentiable en 0 : la descente lisse présentée ici ne s'applique pas telle quelle. Des méthodes adaptées, comme la descente par coordonnées ou les méthodes proximales, constituent un approfondissement facultatif.

Le TP obligatoire utilise L2, dont le gradient a été dérivé.

---

## Concepts essentiels — Mini-lots

Pour un lot de $b$ observations, on estime la contribution des données avec leur moyenne de gradient, puis on ajoute la pénalité une fois.

Un lot complet utilise toutes les observations ; un mini-lot utilise un sous-ensemble ; une époque correspond à un passage sur l'ensemble de l'apprentissage.

Exemple : 144 journées avec des lots de 32 donnent cinq mises à jour par époque, dont une sur les 16 dernières journées.

La perte complète peut remonter d'une époque à l'autre. Un pas constant avec des mini-lots ne garantit pas d'atteindre exactement la solution de Ridge.

---

## Lecture du code — Réutiliser le projet

Depuis le dossier `Projet_IA`, après les jalons précédents :

```python
from correction import charger, ajuster_echelle, ajouter_biais, descente, ridge
x, y, (train, validation, test) = charger()
mu, sigma = ajuster_echelle(x[train])
A = ajouter_biais((x - mu) / sigma)
theta, historique, pas = descente(A[train], y[train], penalite=0.1)
reference = ridge(A[train], y[train], penalite=0.1)
print(max(abs(theta - reference)) < 1e-6)
```

**Fonctionnement :** les fonctions reprennent les mêmes données et conventions. `descente` calcule un pas à partir de la quadratique ; `ridge` fournit une solution de comparaison.

**Résultat attendu :** `True` sur les données fournies. Ne pas attendre le même accord exact d'une descente à mini-lots avec pas constant.

---

## Validation, arrêt et test

Choisir $\lambda$ parmi une liste annoncée, en comparant les RMSE sur la validation. La perte d'apprentissage et la pénalité ne suffisent pas à sélectionner le meilleur modèle prédictif.

Sur un réseau, l'arrêt anticipé conserve les paramètres de l'itération ayant la meilleure perte de validation, avant une éventuelle remontée.

Le test est consulté une fois les transformations, réglages et règles de sélection figés. Une mauvaise performance de test ne doit pas déclencher une nouvelle optimisation sur ce même test.

Pour une série temporelle, les partitions respectent l'ordre des jours. Leur distribution peut changer : le commentaire des résultats doit le signaler.

---

## Erreurs fréquentes

- Ajouter le gradient au lieu de le soustraire.
- Déclarer une divergence impossible parce que la fonction est convexe.
- Pénaliser involontairement la constante.
- Comparer des paramètres `lambda` sans vérifier la normalisation des pertes.
- Confondre minimum de la perte d'apprentissage et meilleur modèle en validation.

---

## Exercice 1 — Lire la trajectoire

**Objectif pédagogique :** comprendre le pas. **Prérequis :** dérivation d'une quadratique.

**Énoncé :** pour $J(\theta)=(\theta-3)^2/2$, depuis 0, calculer deux mises à jour avec les pas 0,5 puis 3.

**Contraintes :** faire deux trajectoires distinctes. **Livrable attendu :** les valeurs et une conclusion.

**Critères de réussite :** distinguer réduction et amplification de l'écart au minimum.

<details><summary>Indices gradués</summary>

1. Le gradient vaut $\theta-3$.
2. Après une mise à jour, l'écart au minimum est multiplié par $1-\eta$.
</details>

---

## Correction — Lire la trajectoire

<details><summary>Afficher la correction</summary>

Avec 0,5 : $0\to1{,}5\to2{,}25$. L'écart au minimum diminue.

Avec 3 : $0\to9\to-9$. L'écart au minimum est multiplié par -2 à chaque étape ; son amplitude augmente. La convexité n'empêche donc pas un mauvais pas de faire diverger l'algorithme.
</details>

---

## Exercice 2 — Retrouver la solution directe

**Objectif pédagogique :** contrôler une descente. **Prérequis :** gradient vectorisé et moindres carrés.

**Énoncé :** sur $A=((1,0),(1,1),(1,2))$ et $y=(1,2,2)$, partir de deux poids nuls et effectuer 2 500 pas de 0,1 sans pénalité.

**Contraintes :** conserver la perte à chaque étape. **Livrable attendu :** paramètres et comparaison à `lstsq`.

**Critères de réussite :** accord à $10^{-6}$ et perte qui ne croît pas au-delà de la tolérance d'arrondi.

<details><summary>Indices gradués</summary>

1. Réutiliser le gradient du chapitre précédent.
2. Comparer les paramètres, puis les pertes ; les valeurs proches de zéro se testent avec une tolérance.
</details>

---

## Correction — Retrouver la solution directe

<details><summary>Afficher la correction</summary>

```python
import numpy as np
A = np.array([[1., 0.], [1., 1.], [1., 2.]])
y = np.array([1., 2., 2.])
theta = np.zeros(2)
pertes = []
for _ in range(2500):
    r = A @ theta - y
    pertes.append(np.mean(r*r)/2)
    theta -= 0.1 * (A.T @ r / len(y))
print(theta, np.all(np.diff(pertes) <= 1e-12))
```

**Lecture :** chaque itération recalcule l'erreur sur les trois lignes. L'historique contient 2 500 scalaires ; la sortie est proche de `[1.166667, 0.5] True`. Ici, les poids restent identifiables car les deux colonnes sont indépendantes.
</details>

---

## Exercice 3 — Réparer une régularisation

**Objectif pédagogique :** déboguer puis justifier un protocole. **Prérequis :** L2 et validation.

**Énoncé :** un programme ajoute `lambda * theta` au gradient et retient le `lambda` qui minimise l'erreur de test. Identifier deux problèmes et corriger.

**Contraintes :** conserver une constante non pénalisée. **Livrable attendu :** gradient et règle de sélection corrigés.

**Critères de réussite :** zéro pénalité sur la première coordonnée, choix sur la validation, test réservé.

<details><summary>Indices gradués</summary>

1. Quelle coordonnée contient la constante ?
2. Un jeu utilisé pour choisir un réglage reste-t-il un test final indépendant de ce choix ?
</details>

---

## Correction — Réparer une régularisation

<details><summary>Afficher la correction</summary>

Construire `reg = theta.copy()`, fixer `reg[0] = 0`, puis ajouter `lambda * reg` au gradient de la partie données.

Comparer les candidats sur la validation, figer le réglage et évaluer ensuite le test. Les erreurs calculées sur le test ne doivent pas choisir les paramètres.

Le choix de ne pas pénaliser la constante correspond à notre convention ; il faut l'annoncer pour rendre les comparaisons reproductibles.
</details>

---

## Projet fil rouge — Jalon 5

Dans le [projet consommation](../../Projet_IA/README.md), réutiliser le gradient du jalon 4, la standardisation du jalon 3 et les partitions initiales.

**Notions mobilisées :** pas, convergence et pénalité L2. **Fonctionnalité :** entraîner la régression par descente ; comparer les pénalités 0, 0,001, 0,01, 0,1 et 1 sur la validation.

**Résultat vérifiable :** mêmes paramètres à $10^{-6}$ près entre descente complète et résolution directe du même objectif. Sur le fichier fourni, la validation choisit $\lambda=0{,}1$.

**Livrables :** historique, tableau de validation et paramètres figés. **À observer :** recherche de réglages sur le test et changements de convention entre deux méthodes.

---

## Problème — Organiser les occasions restantes

Un horizon contient 24 demi-journées disponibles. Une visite et une sortie n'ont pas le même coût en temps. Comment annoncer les contraintes, choisir un objectif et obtenir un calendrier réalisable ?

[Problème 4 : vingt-quatre demi-journées à répartir](../../Tps/Tail_End/04_planning.md)

Objectif : comprendre que l'optimisation répond à un objectif défini, dont il faut aussi discuter les limites.

---

## Approfondissement — Choix individuels et résultat collectif

Peut-on ajouter une route sans supprimer aucun trajet, et pourtant ralentir tous les conducteurs ?

[Explorer le paradoxe de Braess](../../Tps/Paradoxes/05_braess.md).

Ce problème facultatif introduit un petit graphe orienté et distingue un équilibre de décisions individuelles du meilleur plan collectif réalisable.

---

## Cas d'usage réels

**Entreprise :** équipe chargée d'une prévision énergétique, scénario pédagogique.

**Problème :** contrôler l'apprentissage lorsque les variables sont corrélées ou de tailles différentes.

**Solution :** diagnostiquer la courbure, mettre à l'échelle et comparer une pénalisation avec une référence sans pénalité.

**Bénéfice attendu :** rendre l'entraînement plus stable et mesurable. Une amélioration en validation doit être constatée ; elle n'est pas garantie par l'ajout d'une pénalité.

---

## Fiche de révision

- La descente soustrait le gradient multiplié par un pas positif.
- Une garantie de convergence dépend des hypothèses sur la fonction et le pas.
- Les mini-lots introduisent une variabilité dans les mises à jour.
- L2 pénalise ici les poids, pas la constante.
- La validation choisit ; le test évalue les choix figés.

---

## Questions de révision

1. Pourquoi une perte convexe peut-elle diverger sous une descente ?
2. Pourquoi standardiser ne supprime-t-il pas une redondance exacte ?
3. Comment convertir notre `lambda` vers une pénalité sans moyenne de perte ?
4. Pourquoi la perte complète peut-elle remonter avec des mini-lots ?
5. Quelle différence entre arrêt de convergence et arrêt anticipé sur validation ?

---

## QCM — Questions 1 et 2

**1. La mise à jour usuelle est :** A. $\theta+\eta\nabla J$ ; B. $\theta-\eta\nabla J$ ; C. $\theta/\nabla J$ ; D. $\nabla J-\eta$.

**2. Un pas trop grand peut :** A. faire diverger une quadratique convexe ; B. garantir le minimum ; C. supprimer la pénalité ; D. améliorer toujours le test.

<details><summary>Afficher la correction</summary>

1. **B** : le gradient pointe vers l'augmentation locale.
2. **A** : la courbure limite le pas utilisable.
</details>

---

## QCM — Questions 3 à 5

**3. Notre pénalité L2 exclut :** A. tous les poids ; B. la température uniquement ; C. la constante ; D. les erreurs.

**4. Le paramètre de régularisation est choisi avec :** A. le test final ; B. la validation ; C. les noms de colonnes ; D. le plus petit fichier.

**5. Une époque signifie :** A. une ligne ; B. une seule multiplication ; C. un appel au test ; D. un passage sur tout l'apprentissage.

<details><summary>Afficher la correction</summary>

3. **C** : la première entrée de $D$ est nulle.
4. **B** : le test évalue ensuite le modèle figé.
5. **D** : plusieurs mini-lots peuvent constituer cette époque.
</details>

---

## Résumé final

Nous savons comparer une solution directe et un apprentissage itératif.
La stabilité numérique, la convergence et la généralisation se vérifient séparément.
Les mêmes outils vont apprendre les paramètres d'un classifieur puis d'un petit réseau.

[Continuer : classification et rétropropagation](06_retropropagation.md).

Références : [scikit-learn — Ridge](https://scikit-learn.org/stable/modules/linear_model.html#ridge-regression-and-classification), [éviter les fuites de données](https://scikit-learn.org/stable/common_pitfalls.html).
