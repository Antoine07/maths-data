---
marp: true
html: true
---

# Mathématiques CODA — De la modélisation à l’IA

## Le parcours et ses prérequis

Les nouveaux chapitres prolongent les supports existants. Le même [projet de consommation électrique](../Projet_IA/README.md) évolue au fil des six jalons avancés.

---

## 1 — Fonctions et premiers modèles

1. [Révisions d’algèbre](revision.md).
2. [Dérivation](01_derivation.md), puis [étude des fonctions](02_derivation.md).
3. [Modéliser la température](01_modelisation.md), puis [la consommation](02_modelisation.md).

Objectif : comprendre une variation et ajuster une première relation entre une variable et une cible.

---

## 2 — Algèbre pour les données

4. [Matrices, transformations et valeurs propres](matrice.md).
5. **Nouveau :** [géométrie des données](avance/01_geometrie_donnees.md) — normes, distances et projections ; jalon 1.
6. **Nouveau :** [moindres carrés et stabilité](avance/02_moindres_carres.md) — régression multivariée, rang et conditionnement ; jalon 2.

Objectif : passer des vecteurs à un modèle multivarié dont on peut contrôler les calculs.

---

## 3 — Statistiques et représentation

7. [Statistiques descriptives](stat/01_stat_descriptive.md), [probabilités essentielles](stat/probabilites.md), [covariance et corrélation](stat/02_covariance_correlation.md), puis [centrage-réduction](stat/03_centrage_reduction.md).
8. [Introduction à l’ACP](stat/04_acp_intro.md).
9. **Nouveau :** [SVD et réduction de dimension](avance/03_svd_acp.md) — directions, reconstruction et compression ; jalon 3.

Objectif : comprendre ce qui est conservé ou perdu lorsqu’on change la représentation des données.

---

## 4 — Analyse pour apprendre les paramètres

10. [Dérivées partielles, gradient et Hessienne](gradient.md).
11. **Nouveau :** [calcul différentiel matriciel](avance/04_calcul_differentiel.md) — Jacobienne, chaîne de dérivation et vérification ; jalon 4.
12. **Nouveau :** [optimisation et régularisation](avance/05_optimisation.md) — descente, pas et L2 ; jalon 5.
13. **Nouveau :** [classification et rétropropagation](avance/06_retropropagation.md) — logistique et réseau ; jalon 6.

Objectif : comprendre et vérifier comment un modèle apprend.

---

## Mise en pratique

Chaque nouveau chapitre contient trois exercices progressifs, des corrections dépliables, des questions de révision et cinq QCM.

Le [projet fil rouge](../Projet_IA/README.md) fournit les données simulées, un point de départ, les six jalons, une correction exécutable et les critères de validation. Compter environ 24 à 30 h pour les nouveaux chapitres avec les TP, selon les prérequis.

Les approfondissements statistiques existants restent disponibles depuis l’accueil HTML.

---

## Quatre problèmes — Compter les occasions

Inspirés de l'idée de *The Tail End*, ces problèmes originaux sont placés après leurs prérequis :

1. [Rencontres et pourcentages](../Tps/Tail_End/01_rencontres.md), après les révisions.
2. [Fréquence et cumul](../Tps/Tail_End/02_frequence.md), après la dérivation.
3. [Événement rare et variance](../Tps/Tail_End/03_evenement_rare.md), après la SVD.
4. [Calendrier sous contrainte](../Tps/Tail_End/04_planning.md), après l'optimisation.

[Énoncés, objectifs et corrections](../Tps/Tail_End/README.md).

---

## Dix problèmes accessibles dans le parcours

Les cartes lavande apparaissent après le cours associé : rencontres et dix minutes après les révisions ; fréquence après dérivation ; Simpson après les statistiques ; bus et dîner après les probabilités ; événement rare après SVD ; planning et Braess après optimisation ; fausses alertes après classification.

Chaque carte précise la question, les notions, le prérequis et la durée. Le badge « Approfondissement » distingue le problème de Braess.

[Ouvrir le catalogue des dix problèmes](../docs/problemes.html).
