---
marp: true
html: true
---

# Préparer et séparer les données

Préparation des données

Partitions, standardisation, cible binaire et prévention des fuites.

---

## Objectif

Construire un protocole d'évaluation, ajuster les transformations sur l'apprentissage et définir une cible binaire sans fuite de données.

**Prérequis :** Moyenne, écart-type, matrice d'observations, seuil de décision et distinction entre prédiction et apprentissage.

---

## Résumé général

La qualité d'un calcul dépend aussi des observations qui ont servi à le préparer. Les échelles et le seuil de consommation sont appris sur l'apprentissage. La validation sert aux choix ; le test sert au bilan après ces choix. Une chronologie fixée prépare l'affectation de journées futures.

---

## Concepts essentiels — Trois rôles différents

L'**apprentissage** sert à ajuster les transformations et les paramètres du modèle. La **validation** aide à choisir des réglages annoncés : pas, pénalité, architecture ou itérations.

Le **test** mesure ensuite les performances des modèles figés. Le consulter pour choisir le meilleur réglage le transforme en outil de sélection et rend le bilan trop optimiste.

Une séparation ne supprime pas tous les biais. Si les saisons diffèrent entre périodes, les distributions changent : cela doit être commenté.

---

## Exemple concret — Les mêmes journées dans toutes les séances

Les jours 1–144 forment l'apprentissage, 145–192 la validation et 193–240 le test. Les partitions sont fixées avant les transformations.

Les caractéristiques sont température, occupation et équipements. Le numéro de jour sert à identifier et séparer les lignes ; il n'est pas une caractéristique de notre modèle avancé.

La consommation est connue pour construire des étiquettes et évaluer les résultats historiques. La fournir comme entrée du classificateur ferait entrer la réponse dans la question.

---

## Voir les calculs

![Les 144 jours d’apprentissage, les 48 de validation et les 48 de test ont des rôles distincts.](../assets/partitions.svg)

---

## Lecture des formules — Standardiser sans changer de repère

$$
z_j=\frac{x_j-\mu_j}{s_j}.
$$

$x_j$ est une valeur de la caractéristique j ; $\mu_j$ et $s_j$ sont sa moyenne et son écart-type calculés sur l'apprentissage.

Avec une température de 20 °C, une moyenne d'apprentissage de 12 et un écart-type de 2, on obtient z=4. Dépasser 1 après standardisation est normal : cette transformation ne borne pas les valeurs entre 0 et 1.

La validation et le test utilisent les **mêmes** moyennes et échelles. Réapprendre une moyenne sur la validation changerait le repère utilisé par les poids.

---

## Concepts essentiels — Colonnes constantes

Si une caractéristique ne varie pas dans l'apprentissage, son écart-type est nul. Diviser par cet écart est impossible.

Notre convention remplace alors l'échelle par 1. Les valeurs d'apprentissage centrées de cette colonne deviennent 0. Cette convention doit être enregistrée avec le modèle.

Une caractéristique constante peut aussi être retirée si le même retrait est appliqué partout. Dans le parcours, nous gardons trois colonnes pour conserver le même contrat de dimensions.

---

## Lecture des formules — Définir la forte consommation

On fixe $t=\operatorname{mediane}(y_{train})$, puis la classe d'une journée vaut 1 si sa consommation est supérieure ou égale à t, et 0 sinon.

Pour des consommations d'apprentissage 10, 12, 16 et 18, la médiane vaut $(12+16)/2=14$. Les classes sont donc 0, 0, 1 et 1.

Le seuil t est en kWh. Il diffère du seuil de probabilité 0,5 utilisé pour convertir la sortie du modèle en décision.

Une classe définie par ce seuil décrit notre exercice. Elle ne constitue pas un seuil réglementaire ou une détection de panne validée.

---

## Lecture du code — Ajuster puis appliquer

```python
import numpy as np
from parcours import ajuster_echelle
train = np.array([[10., 1., 2.], [14., 3., 2.]])
validation = np.array([[20., 2., 2.]])
moyenne, echelle = ajuster_echelle(train)
print(moyenne, echelle)
print((validation - moyenne) / echelle)
```

**Fonctionnement :** `ajuster_echelle` calcule un paramètre par colonne et traite l'écart-type nul. La validation reçoit ensuite la transformation déjà fixée.

**Exécution et résultat :** moyenne `[12,2,2]`, échelle `[2,1,1]` et validation transformée `[[4,0,0]]`.

**Erreur fréquente :** calculer la moyenne sur le tableau complet avant de découper les partitions.

---

## Explication détaillée — Réutiliser sans réapprendre

Une transformation ajustée fait partie du modèle : sauvegarder les poids sans la moyenne, l'échelle, l'ordre des colonnes et le seuil ne suffit pas à reproduire les décisions.

Une journée inconnue suit les étapes connues : sélectionner les mêmes caractéristiques, appliquer la transformation, calculer le logit puis la décision.

Cette règle concerne aussi une ACP ou une sélection de variables. Même sans utiliser les étiquettes, regarder la distribution du test pour ajuster une transformation apporte de l'information sur ce test.

---

## Algorithme expliqué — Préparer le projet

**Objectif :** produire des entrées comparables et une cible définie sans consulter le test pour les choix.

**Entrées :** table des 240 journées et partitions fixées. **Traitement :** sélectionner les trois colonnes ; ajuster moyenne et échelle sur train ; calculer la médiane de consommation sur train ; appliquer ces paramètres à toutes les lignes.

**Sorties :** entrées standardisées, classes et paramètres de transformation. Sur le petit exemple, la validation est transformée en (4,0,0) et le seuil de consommation de l'autre exemple vaut 14.

Référence : [scikit-learn — éviter les fuites de données](https://scikit-learn.org/stable/common_pitfalls.html#data-leakage).

---

## Erreurs fréquentes

- Ajuster avant de séparer les données.
- Inclure la cible dans les entrées.
- Confondre standardisation et normalisation entre 0 et 1.
- Réajuster la transformation pour chaque nouvelle journée.
- Utiliser le test pour choisir un seuil.

---

## Exercice 1 — Repérer une fuite de cible

**Objectif pédagogique :** Sélectionner des caractéristiques admissibles. **Prérequis :** Entrée, cible et chronologie.

**Énoncé :** Un classificateur reçoit temperature, occupation, equipements et consommation pour prédire forte_consommation. Identifier la fuite et expliquer le rôle de jour.

**Contraintes :** Distinguer les données disponibles avant la journée des données utilisées pour établir l'étiquette.

**Livrable attendu :** Liste des entrées retenues et justification.

**Critères de réussite :** La consommation est exclue des entrées ; le jour sert ici au partitionnement.

<details><summary>Indices gradués</summary>

1. Comment l'étiquette forte_consommation est-elle construite ?
2. Une variable peut être disponible pour évaluer sans être disponible pour prévoir.

</details>

---

## Correction — Repérer une fuite de cible

<details><summary>Afficher la correction</summary>

Les entrées sont température, occupation et équipements. La consommation détermine directement la classe : l'inclure donnerait la réponse au modèle. Le jour identifie les lignes et fixe les partitions chronologiques ; il n'entre pas dans les caractéristiques retenues pour cette expérience.

</details>


---

## Exercice 2 — Transformer une journée inconnue

**Objectif pédagogique :** Appliquer des paramètres appris. **Prérequis :** Moyenne, écart-type et traitement d'une constante.

**Énoncé :** Pour train=((10,1,2),(14,3,2)) et la nouvelle journée (20,2,2), calculer les paramètres et les coordonnées standardisées.

**Contraintes :** Ne pas ajuster la transformation sur la nouvelle journée.

**Livrable attendu :** Moyenne, échelle et nouvelle représentation.

**Critères de réussite :** Résultat (4,0,0) et aucune division par zéro.

<details><summary>Indices gradués</summary>

1. La troisième colonne est constante.
2. Utiliser les moyennes et écarts-types de train.

</details>

---

## Correction — Transformer une journée inconnue

<details><summary>Afficher la correction</summary>

La moyenne est (12,2,2), les écarts-types sont (2,1,0), donc les échelles retenues sont (2,1,1). La nouvelle journée devient (4,0,0).

```python
import numpy as np
from parcours import ajuster_echelle
X = np.array([[10., 1., 2.], [14., 3., 2.]])
mu, s = ajuster_echelle(X)
print((np.array([20., 2., 2.]) - mu) / s)
```

Le résultat conserve le même repère que l'apprentissage.

</details>


---

## Exercice 3 — Réparer une préparation globale

**Objectif pédagogique :** Déboguer un protocole. **Prérequis :** Partitions et indexation.

**Énoncé :** Le code calcule `mu = X.mean(0)` avant de séparer train et test. Corriger le calcul sur le jeu du projet et vérifier les dimensions.

**Contraintes :** Utiliser les partitions fixées et ne pas utiliser la consommation dans X.

**Livrable attendu :** Code corrigé et explication de la fuite.

**Critères de réussite :** Moyennes calculées sur 144 lignes uniquement ; entrées finales de forme (240,3).

<details><summary>Indices gradués</summary>

1. Sélectionner d'abord les indices d'apprentissage.
2. Appliquer ensuite les mêmes paramètres à toutes les lignes.

</details>

---

## Correction — Réparer une préparation globale

<details><summary>Afficher la correction</summary>

La préparation du projet expose les paramètres appris et permet de les contrôler.

```python
import numpy as np
from parcours import preparer, PARTITIONS
data = preparer()
assert np.allclose(data['moyenne'], data['X'][PARTITIONS['train']].mean(0))
assert data['Z'].shape == (240, 3)
print(data['Z'][PARTITIONS['train']].mean(0))
```

Les moyennes standardisées de train sont proches de zéro à l'arrondi près ; celles de validation ne sont pas imposées à zéro.

</details>


---

## Projet fil rouge

### Contexte et utilisateurs

Une équipe de gestion énergétique souhaite comprendre des profils de journées et préparer une prévision. Les 240 journées sont entièrement simulées ; les résultats ne constituent pas une étude de bâtiment réel.

### Problème à résoudre et fonctionnalités cibles

Préparer les représentations et les étiquettes qui seront réutilisées par les modèles logistique et réseau. Cette préparation précède tout entraînement.

### Modèle de données et architecture attendue

Réutiliser `pratique/depart.py`, `pratique/parcours.py` et le même notebook. Les entrées sont température, occupation et équipements. La consommation est la cible, jamais une entrée du classificateur. Les jours 1–144 servent à apprendre, 145–192 à valider, 193–240 au bilan final.

---

## Projet fil rouge — Livrables et validation

### Jalon relié à la séance

Enregistrer trois moyennes, trois échelles, la médiane de consommation train et les identifiants des partitions. Vérifier les moyennes de Z_train et traiter explicitement les colonnes constantes. À observer : paramètres recalculés sur validation ou test.

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

**Solution étudiée :** Partitions, standardisation, cible binaire et prévention des fuites.

**Bénéfice attendu :** comprendre les hypothèses et contrôler les résultats avant une utilisation sur des données réelles. Une amélioration numérique ne démontre pas une économie d'énergie ni une causalité.

---

## Fiche de révision

- Les partitions précèdent l'ajustement des transformations.
- La validation guide les choix ; le test mesure après ces choix.
- L'échelle, les colonnes et le seuil font partie du modèle.
- La saisonnalité simulée limite l'interprétation des résultats.

---

## Questions de révision

1. Quels paramètres de préparation doivent être sauvegardés ?
2. Pourquoi une valeur standardisée peut-elle dépasser 1 ?
3. Quel rôle joue la validation ?
4. Pourquoi la médiane du test ne doit-elle pas définir la cible ?
5. Quelle limite reste présente avec des partitions chronologiques ?

---

## QCM — Questions 1 à 2

**1. La moyenne de standardisation est apprise sur**

A. le test ; B. la validation seule ; C. l'apprentissage ; D. chaque requête.

**2. Une colonne constante exige**

A. une division par zéro ; B. une convention explicite ou un retrait cohérent ; C. une nouvelle cible ; D. un mélange des partitions.

<details><summary>Afficher la correction</summary>

1. **C** : les transformations sont ajustées sur l'apprentissage

2. **B** : son écart-type nul doit être traité

</details>

---

## QCM — Questions 3 à 5

**3. Le seuil de consommation est calculé à partir**

A. de y_train ; B. de X_test ; C. de y_test ; D. de toutes les probabilités.

**4. Une valeur standardisée de 4 est**

A. toujours un bug ; B. une probabilité ; C. nécessairement interdite ; D. possible.

**5. Le test sert à**

A. choisir le meilleur pas ; B. réajuster les centres ; C. établir le bilan après les choix ; D. définir les classes.

<details><summary>Afficher la correction</summary>

3. **A** : il est défini avant le bilan de test

4. **D** : la standardisation ne borne pas les valeurs

5. **C** : il n'est pas utilisé pour régler le modèle

</details>

---

## Résumé final

Les partitions précèdent l'ajustement des transformations.
La validation guide les choix ; le test mesure après ces choix.
L'échelle, les colonnes et le seuil font partie du modèle.
La saisonnalité simulée limite l'interprétation des résultats.

[Continuer le parcours](05_gradient_chaine.md) · [Tous les chapitres](../index.html).
