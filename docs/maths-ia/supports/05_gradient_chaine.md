---
marp: true
html: true
---

# Gradient et règle de chaîne

Gradient et chaîne

Dérivées partielles, propagation du gradient et vérification numérique.

---

## Objectif

Calculer des dérivées partielles, assembler un gradient et suivre la règle de chaîne sur un petit réseau. Contrôler le résultat par différences finies.

**Prérequis :** Dérivée d'une fonction à un paramètre, perte quadratique, propagation avant et vecteurs.

---

## Résumé général

Un modèle contient plusieurs paramètres. Le gradient rassemble les variations de la perte selon chacun d'eux. La règle de chaîne transmet une variation à travers les étapes du calcul ; la rétropropagation organise cette transmission en réutilisant les résultats intermédiaires.

---

## Concepts essentiels — Dérivées partielles et gradient

Pour une perte qui dépend de w et b, une dérivée partielle fait varier un seul paramètre en gardant l'autre fixé.

Le gradient rassemble ces dérivées dans un ordre annoncé : $\nabla L=(\partial L/\partial w,\partial L/\partial b)$.

Chaque composante a le sens d'une pente locale. Dans la géométrie euclidienne choisie, le gradient indique la direction de plus forte augmentation locale ; la descente utilise son opposé.

---

## Lecture des formules — Une observation, deux paramètres

$$
\widehat y=wx+b,\quad r=\widehat y-y,\quad L=\frac12r^2.
$$

x et y sont ici fixés. w et b sont les paramètres ; r est le résidu. Le facteur 1/2 simplifie les dérivées : c'est une convention différente de la MSE sans ce facteur.

$$
\frac{\partial L}{\partial w}=rx,\qquad
\frac{\partial L}{\partial b}=r.
$$

Pour x=2, y=5, w=1, b=0 : la prédiction vaut 2, r=-3, L=4,5 et le gradient vaut (-6,-3).

---

## Explication détaillée — La règle de chaîne

Si w influence un intermédiaire z, qui influence une sortie h, qui influence L, on multiplie les variations locales le long du chemin.

Pour $L=\frac12(wx+b-y)^2$, la dérivée de L selon le résidu vaut r ; celle du résidu selon la prédiction vaut 1 ; celle de la prédiction selon w vaut x. Leur produit donne rx.

Si un paramètre intervient par plusieurs chemins, leurs contributions s'additionnent. C'est notamment le cas lorsque le même poids sert pour plusieurs observations.

---

## Exemple concret — Un premier gradient appliqué

Avec le gradient (-6,-3) et un pas de 0,1 :

$$
w_{nouveau}=1-0{,}1(-6)=1{,}6,\quad
b_{nouveau}=0-0{,}1(-3)=0{,}3.
$$

La nouvelle prédiction vaut $1{,}6\times2+0{,}3=3{,}5$. Le résidu devient -1,5 et la perte vaut 1,125.

Les deux paramètres ont changé. Le nouveau gradient doit être recalculé à ce nouveau point avant le pas suivant.

---

## Lecture des formules — Une couche cachée scalaire

Considérons $z=wx+b$, $h=\operatorname{ReLU}(z)$, $\widehat y=vh+c$ et $L=\frac12(\widehat y-y)^2$.

Avec r égal au résidu : $\partial L/\partial v=rh$ et $\partial L/\partial c=r$. Pour z>0, $\partial L/\partial w=rvx$ et $\partial L/\partial b=rv$ ; pour z<0, ces deux dernières contributions sont nulles.

En z=0, ReLU n'a pas de dérivée usuelle ; notre convention et celle de PyTorch utilisent 0 pour ce passage.

Exemple : x=2, w=1, b=0, v=3, c=0, y=5. Alors h=2, la prédiction vaut 6, r=1 ; les dérivées selon v, c, w et b valent respectivement 2, 1, 6 et 3.

---

## Lecture du code — Contrôler une dérivée

```python
import numpy as np
theta = np.array([1., 0.])
def perte(t):
    return .5 * (2*t[0] + t[1] - 5)**2
epsilon = 1e-6
numerique = []
for j in range(2):
    delta = np.zeros(2)
    delta[j] = epsilon
    numerique.append((perte(theta+delta)-perte(theta-delta))/(2*epsilon))
print(numerique)
```

**Fonctionnement :** la boucle modifie une coordonnée à la fois et compare deux pertes proches. Les autres paramètres restent fixés.

**Résultat attendu :** environ `[-6, -3]`, proche du gradient analytique.

**Erreur fréquente :** comparer des dérivées calculées à des paramètres différents ou choisir un epsilon si petit que l'arrondi domine.

---

## Algorithme expliqué — La rétropropagation

**Objectif :** calculer les gradients d'une composition. **Entrées :** données, paramètres et calcul de perte.

**Traitement :** effectuer la propagation avant et conserver les intermédiaires ; démarrer à la perte ; multiplier par les dérivées locales en remontant les dépendances ; sommer les chemins et les observations.

**Sortie :** un gradient de même forme que chaque paramètre. Sur le réseau scalaire précédent, on retrouve les quatre dérivées 6, 3, 2 et 1 dans l'ordre w, b, v, c.

La rétropropagation calcule les gradients. L'optimiseur réalisera ensuite la mise à jour ; ce sont deux rôles distincts.

---

## Erreurs fréquentes

- Confondre dérivée, gradient et valeur de perte.
- Oublier une dépendance dans la règle de chaîne.
- Oublier de moyenner les contributions lorsque la perte est une moyenne.
- Calculer des différences finies à un autre point que le gradient analytique.
- Affirmer que ReLU est dérivable en zéro sans préciser la convention.

---

## Exercice 1 — Calculer deux dérivées partielles

**Objectif pédagogique :** Tenir les autres paramètres fixes. **Prérequis :** Perte quadratique et règle de chaîne.

**Énoncé :** Pour x=3, y=4, w=1, b=0 et L=(wx+b−y)²/2, calculer prédiction, perte et gradient selon w puis b.

**Contraintes :** Annoncer l'ordre des composantes.

**Livrable attendu :** Quatre résultats et les étapes.

**Critères de réussite :** Résidu -1, perte 0,5 et gradient (-3,-1).

<details><summary>Indices gradués</summary>

1. Calculer le résidu avant les dérivées.
2. La dérivée de la prédiction selon w vaut x.

</details>

---

## Correction — Calculer deux dérivées partielles

<details><summary>Afficher la correction</summary>

La prédiction vaut 3, le résidu -1 et la perte 0,5. La dérivée selon w est r×x=-3 ; celle selon b est r=-1. Le gradient dans l'ordre (w,b) est donc (-3,-1).

</details>


---

## Exercice 2 — Vérifier le gradient numérique

**Objectif pédagogique :** Valider une formule analytique. **Prérequis :** Différences finies et NumPy.

**Énoncé :** Pour la même perte, comparer le gradient analytique et les différences finies centrales avec epsilon=1e-6.

**Contraintes :** Faire varier une seule coordonnée à la fois et comparer avec une tolérance.

**Livrable attendu :** Deux gradients et l'écart maximal.

**Critères de réussite :** Accord à 1e-5 près sur ce petit exemple.

<details><summary>Indices gradués</summary>

1. Écrire une fonction qui reçoit les deux paramètres.
2. Utiliser un vecteur delta nul sauf à la coordonnée testée.

</details>

---

## Correction — Vérifier le gradient numérique

<details><summary>Afficher la correction</summary>

On contrôle la cohérence locale, pas la qualité du modèle.

```python
import numpy as np
t, eps = np.array([1., 0.]), 1e-6
def L(v):
    return .5*(3*v[0]+v[1]-4)**2
g = np.array([(L(t+eps*np.eye(2)[j])-L(t-eps*np.eye(2)[j]))/(2*eps) for j in range(2)])
assert np.allclose(g, [-3., -1.], atol=1e-5)
print(g)
```

La sortie est proche de [-3,-1]. Une tolérance convient aux arrondis flottants.

</details>


---

## Exercice 3 — Réparer le passage dans ReLU

**Objectif pédagogique :** Transmettre le gradient au bon endroit. **Prérequis :** Dérivée de ReLU hors zéro et masques.

**Énoncé :** Pour z=(-2,3) et un gradient venant de la suite égal à (5,5), un programme transmet (5,5) sans tenir compte de ReLU. Corriger.

**Contraintes :** Expliquer séparément chaque coordonnée ; ne pas utiliser le cas z=0.

**Livrable attendu :** Gradient transmis et code.

**Critères de réussite :** Résultat (0,5) et masque correct.

<details><summary>Indices gradués</summary>

1. La sortie ReLU ne varie pas autour d'un z strictement négatif.
2. Multiplier le gradient reçu par la dérivée locale.

</details>

---

## Correction — Réparer le passage dans ReLU

<details><summary>Afficher la correction</summary>

La dérivée locale vaut 0 en -2 et 1 en 3.

```python
import numpy as np
z, gradient_recu = np.array([-2., 3.]), np.array([5., 5.])
gradient_transmis = gradient_recu * (z > 0)
print(gradient_transmis)
```

La sortie est `[0. 5.]`. Le masque conserve la forme du gradient.

</details>


---

## Projet fil rouge

### Contexte et utilisateurs

Une équipe de gestion énergétique souhaite comprendre des profils de journées et préparer une prévision. Les 240 journées sont entièrement simulées ; les résultats ne constituent pas une étude de bâtiment réel.

### Problème à résoudre et fonctionnalités cibles

Ajouter une fonction de perte et un gradient explicites sur un petit modèle de consommation, puis vérifier un point numériquement avant d'utiliser l'entraînement automatique.

### Modèle de données et architecture attendue

Réutiliser `pratique/depart.py`, `pratique/parcours.py` et le même notebook. Les entrées sont température, occupation et équipements. La consommation est la cible, jamais une entrée du classificateur. Les jours 1–144 servent à apprendre, 145–192 à valider, 193–240 au bilan final.

---

## Projet fil rouge — Livrables et validation

### Jalon relié à la séance

Conserver les paramètres et les données utilisés pour le contrôle ; produire l'écart entre gradient analytique et numérique. À observer : convention de perte différente, signe inversé et oubli du facteur x.

### Livrables

Ajouter le code et son commentaire au notebook existant. Conserver les dimensions, les unités, la partition utilisée et les contrôles effectués.

### Critères de validation

Le notebook se relance dans l'ordre. Les calculs manuels concordent avec le code. Les transformations et réglages ne sont jamais appris sur le test. Expliquer les erreurs plutôt que supprimer les observations gênantes.

### Extensions facultatives

Reprendre les supports du [catalogue général](../../index.html) pour approfondir une notion. Les groupes, l'ACP, la SVD et le clustering sont des compléments ; leur étude complète n'est pas nécessaire pour ce parcours court.

---

## Cas d'usage réels

**Organisation :** service de gestion énergétique, scénario pédagogique.

**Problème :** transformer des mesures hétérogènes en une décision interprétable.

**Solution étudiée :** Dérivées partielles, propagation du gradient et vérification numérique.

**Bénéfice attendu :** comprendre les hypothèses et contrôler les résultats avant une utilisation sur des données réelles. Une amélioration numérique ne démontre pas une économie d'énergie ni une causalité.

---

## Fiche de révision

- Le gradient rassemble les dérivées partielles.
- La règle de chaîne suit les dépendances du calcul.
- La convention de perte détermine les facteurs du gradient.
- Un contrôle numérique valide un calcul local, pas la généralisation.

---

## Questions de révision

1. Que garde-t-on fixe dans une dérivée partielle ?
2. Pourquoi les contributions de plusieurs observations s'additionnent-elles ?
3. Quel effet a le facteur 1/2 dans la perte ?
4. Comment contrôle-t-on une composante du gradient ?
5. Quelle différence existe entre rétropropagation et optimisation ?

---

## QCM — Questions 1 à 2

**1. Un gradient contient**

A. une dérivée par paramètre ; B. uniquement la perte ; C. les partitions ; D. les étiquettes.

**2. Pour L=r²/2, la dérivée selon r est**

A. r² ; B. r ; C. 2 ; D. 0.

<details><summary>Afficher la correction</summary>

1. **A** : chaque composante correspond à une variation partielle

2. **B** : le facteur 1/2 simplifie la dérivée du carré

</details>

---

## QCM — Questions 3 à 5

**3. En z<0, la dérivée locale de ReLU est**

A. 1 ; B. -1 ; C. 0 ; D. toujours indéfinie.

**4. Un contrôle numérique doit**

A. utiliser le test ; B. changer tous les paramètres ensemble ; C. chercher une précision infinie ; D. comparer au même point.

**5. La rétropropagation**

A. choisit le meilleur seuil ; B. calcule les gradients ; C. sépare les données ; D. garantit un minimum global.

<details><summary>Afficher la correction</summary>

3. **C** : ReLU est localement constante dans cette région

4. **D** : la comparaison porte sur la même dérivée locale

5. **B** : la mise à jour revient ensuite à l'optimiseur

</details>

---

## Résumé final

Le gradient rassemble les dérivées partielles.
La règle de chaîne suit les dépendances du calcul.
La convention de perte détermine les facteurs du gradient.
Un contrôle numérique valide un calcul local, pas la généralisation.

[Continuer le parcours](06_optimiser.md) · [Tous les chapitres](../index.html).
