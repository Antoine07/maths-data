# Fondements mathématiques du machine learning – Plan de cours (4 jours)

Nov 10, 2026 · @Michel Cadennes

Module de 4 jours (4 × 7h) pour des étudiants de 1re année de mastère Data/IA aux profils hétérogènes. Chaque journée alterne cours, TD papier et TP Python ; le module se termine par un examen écrit.

| Jour | Thème | TP Python | Lien avec le fil rouge |
| --- | --- | --- | --- |
| 1 | Algèbre linéaire | Équations normales, ACP from scratch, compression SVD | Régression linéaire comme projection |
| 2 | Probabilités et statistiques | Biais-variance, Ridge, Naive Bayes | Moindres carrés et log-loss comme MLE |
| 3 | Optimisation | Régression logistique par GD, SGD, momentum | Conditionnement (SVD) et vitesse de convergence |
| 4 | Théorie de l'information et réseaux de neurones | Réseau de neurones from scratch sur MNIST | Cross-entropy (MLE) et rétropropagation (règle de la chaîne) |

## Principes directeurs

- **Un fil rouge pour relier les quatre jours.** On part de la régression linéaire et on va jusqu'au réseau de neurones. Chaque jour réutilise les outils de la veille : la SVD explique le conditionnement de la descente de gradient, le maximum de vraisemblance justifie la cross-entropy, la règle de la chaîne donne la rétropropagation.
- **Gérer l'hétérogénéité :**
  - un quiz diagnostic en ligne d'environ 20 minutes, à faire avant le jour 1 ;
  - une fiche de rappels distribuée à l'avance ;
  - des exercices de TD sur deux niveaux, « socle » et « approfondissement » ;
  - des binômes mixtes en TP.
- **Les TP en NumPy « from scratch ».** scikit-learn ne sert qu'à vérifier les résultats.
- **Rythme type :** 9h00–12h30 et 13h30–17h00, avec environ 1h30 de cours puis 1h30 à 2h de TD ou TP par demi-journée.

## Jour 1 – Algèbre linéaire : les données comme des matrices

### Matin – Espaces vectoriels et moindres carrés

- Correction rapide du diagnostic, pour savoir sur quoi insister.
- Vecteurs, normes (L1, L2, L∞), produit scalaire, similarité cosinus.
- La matrice de données X (n × d). Une matrice vue comme une application linéaire. Rang, noyau, inverse.
- Projection orthogonale. La régression linéaire comme projection de y sur l'image de X, puis les équations normales.
- *TD* : calculs de projections, démonstration des équations normales.

### Après-midi – Décompositions spectrales

- Valeurs et vecteurs propres, théorème spectral pour les matrices symétriques.
- SVD : interprétation géométrique, approximation de rang faible.
- ACP : maximiser la variance revient à chercher les vecteurs propres de la covariance.
- Conditionnement d'une matrice, avec un teaser pour le jour 3.
- *TP* : régression par les équations normales comparée à `lstsq`, ACP from scratch sur le jeu *digits*, compression d'image par SVD.

## Jour 2 – Probabilités et statistiques : apprendre, c'est estimer

### Matin – Modèles probabilistes et vraisemblance

- Rappels : variables aléatoires, espérance, variance, covariance, loi normale multivariée, formule de Bayes.
- Le maximum de vraisemblance (MLE).
  - Un bruit gaussien conduit aux moindres carrés, ce qui fait le lien avec le jour 1.
  - Un modèle de Bernoulli conduit à la régression logistique et à la log-loss.
- *TD* : calculer des MLE (gaussienne, Bernoulli, Poisson).

### Après-midi – Approche bayésienne et généralisation

- Le maximum a posteriori (MAP) comme régularisation :
  - un prior gaussien donne la régression Ridge ;
  - un prior de Laplace donne le Lasso.
- Le classifieur bayésien naïf.
- Décomposition biais-variance, sur-apprentissage, validation croisée.
- *TP* : simulation du compromis biais-variance avec des régressions polynomiales, effet de la régularisation Ridge, Naive Bayes sur des données textuelles.

## Jour 3 – Optimisation : comment on trouve les paramètres

### Matin – Calcul différentiel et convexité

- Gradient, jacobienne, hessienne, règle de la chaîne en dimension n.
- Calcul matriciel utile, par exemple le gradient de ‖Xw − y‖².
- Convexité : définitions, caractérisation par la hessienne, minimum global.
- La descente de gradient : rôle du pas, convergence, influence du conditionnement (lien avec la SVD du jour 1).
- *TD* : calculer des gradients de fonctions de coût classiques, prouver ou réfuter la convexité de fonctions.

### Après-midi – Optimisation stochastique et sous contraintes

- SGD et mini-batch, momentum, intuition d'Adam.
- Lagrangien et conditions KKT, présentés de façon intuitive.
- Le SVM à marge maximale : formulation primale, formulation duale, astuce du noyau.
- *TP* : régression logistique from scratch, en comparant GD, SGD et momentum. Visualisation des trajectoires selon le pas et le conditionnement.

## Jour 4 – Théorie de l'information et réseaux de neurones, puis examen

### Matin – Information et réseaux de neurones

- Entropie, entropie croisée, divergence de Kullback-Leibler.
- Minimiser la cross-entropy revient à maximiser la vraisemblance (lien avec le jour 2). La fonction softmax.
- Gain d'information et arbres de décision.
- Le perceptron multicouche comme composition de fonctions. Énoncé du théorème d'approximation universelle.
- La rétropropagation comme règle de la chaîne sur un graphe de calcul (lien avec le jour 3).

### Début d'après-midi (13h30–15h00)

- *TP* : un réseau de neurones from scratch en NumPy sur MNIST, avec vérification des gradients (*gradient checking*).

### Synthèse (15h00–15h15)

- Une carte qui relie chaque algorithme aux outils mathématiques utilisés.

### Examen écrit (15h15–17h00, 1h45)

- Un exercice par bloc, chacun mêlant calcul et interprétation. Par exemple :
  1. ACP sur une petite matrice.
  2. Calcul d'un MLE ou d'un MAP.
  3. Gradient et convexité d'une fonction de coût.
  4. Entropie et rétropropagation sur un petit réseau.
- Une fiche manuscrite recto autorisée. C'est rassurant pour les profils les plus fragiles.

**Variante :** si vous préférez ne pas faire passer l'examen en fin de journée, il peut avoir lieu la semaine suivante. Cela libère 1h45 pour approfondir le TP de réseau de neurones ou faire un TD de révision.
