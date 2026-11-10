---
marp: true
html: true
---

# Entraîner le réseau avec PyTorch

S2 · Michel 2 · Michel

Tenseurs, logits, autograd et boucle d'entraînement reproductible.

---

## Objectif

Traduire le réseau NumPy en PyTorch, expliquer autograd et exécuter une boucle d'entraînement correcte. Choisir les itérations et réglages sur validation.

**Prérequis :** Propagation avant, logits, règle de chaîne, descente de gradient, pénalité et préparation des partitions. PyTorch CPU est installé dans l'environnement.

---

## Résumé général

PyTorch représente les tableaux par des tenseurs et peut calculer automatiquement les gradients d'un calcul suivi. Un module contient les paramètres ; une perte mesure les erreurs ; l'optimiseur utilise les gradients. Le même réseau et les mêmes partitions sont conservés.

---

## Concepts essentiels — Tenseurs et paramètres

Un tenseur représente un tableau de nombres, avec une forme et un type. Pour nos calculs, les entrées et étiquettes deviennent des tenseurs flottants `float32`.

Un `nn.Module` rassemble des opérations et des paramètres. `nn.Linear(3,4)` transforme trois entrées en quatre sorties et contient un biais par sortie.

Les paramètres d'une couche PyTorch sont déjà suivis pour le calcul des gradients. Les entrées n'ont pas besoin de demander un gradient pour entraîner les poids.

---

## Lecture des formules — Retrouver les dimensions

Dans les supports NumPy, une couche s'écrit $XW+b$ avec W de forme (entrées, sorties). `nn.Linear` stocke au contraire ses poids dans la forme (sorties, entrées) et calcule l'équivalent de $XW^T+b$.

Pour deux observations et trois entrées, X est de forme (2,3). Une couche 3→4 possède des poids (4,3), un biais (4,) et produit (2,4).

Ces conventions représentent le même calcul. Il faut les connaître pour comparer les poids d'une réalisation NumPy et ceux d'une réalisation PyTorch.

---

## Concepts essentiels — Logits et perte binaire

Notre dernière couche retourne un logit par observation, de forme (n,1). Les cibles binaires doivent avoir la même forme et un type flottant.

`BCEWithLogitsLoss` combine une perte binaire et le traitement du logit de manière numérique stable. On lui fournit le logit directement, sans appliquer une sigmoïde avant.

Pour lire les probabilités lors de l'évaluation, on applique ensuite `torch.sigmoid` aux logits. Pour un logit nul et une classe 1, la perte vaut $-\log(0{,}5)\approx0{,}693$.

---

## Explication détaillée — Ce que fait autograd

Pendant le calcul suivi, PyTorch construit les dépendances nécessaires à la différentiation. `loss.backward()` calcule les gradients des paramètres ayant contribué à la perte.

Les gradients sont accumulés dans `.grad`. `zero_grad()` remet ces accumulations à zéro avant le calcul suivant. `step()` utilise ensuite les gradients pour modifier les paramètres.

Le trio ne remplit donc pas trois fois le même rôle : effacer l'ancien gradient, calculer le nouveau, puis mettre à jour.

---

## Lecture du code — Une boucle minimale

```python
import torch
from torch import nn
torch.manual_seed(7)
X = torch.tensor([[0., 0.], [0., 1.], [1., 0.], [1., 1.]])
y = torch.tensor([[0.], [0.], [1.], [1.]])
modele, perte = nn.Linear(2, 1), nn.BCEWithLogitsLoss()
optimiseur = torch.optim.SGD(modele.parameters(), lr=.1)
avant = float(perte(modele(X), y).detach())
for _ in range(50):
    optimiseur.zero_grad()
    cout = perte(modele(X), y)
    cout.backward()
    optimiseur.step()
apres = float(perte(modele(X), y).detach())
print(apres < avant)
```

**Fonctionnement :** ce petit exemple illustre les opérations sur quatre points, avant de revenir au même jeu de consommation.

**Résultat attendu :** `True`. La perte diminue sur les quatre observations utilisées ; ce constat n'évalue pas une généralisation.

**Erreur fréquente :** oublier `zero_grad()`, inverser `backward()` et `step()`, ou transformer les logits en probabilités avant cette perte.

---

## Exemple concret — Le réseau du fil rouge

L'architecture est 3→4→1 : trois caractéristiques standardisées, une couche ReLU et une sortie logit. Une régression logistique 3→1 constitue une référence plus simple.

La réalisation `entrainer` du fichier `parcours.py` apprend sur train et suit la validation. Elle garde une copie du meilleur état et le restaure après l'arrêt.

La pénalité utilise la convention lambda/2 fois la somme des carrés des poids ; les biais sont placés dans un groupe non pénalisé. Cette convention correspond à l'ajout lambda×poids au gradient par SGD.

---

## Concepts essentiels — Évaluer pendant l'apprentissage

`modele.train()` et `modele.eval()` fixent le comportement de modules qui dépendent du mode, comme dropout. Notre petit réseau linéaire/ReLU ne change pas de calcul entre ces modes, mais le protocole est déjà explicite.

`torch.no_grad()` désactive le suivi des gradients pour un calcul d'évaluation. Il ne remplace pas `eval()` : ces deux outils ont des rôles différents.

Une graine fixée rend l'expérience plus facile à reproduire dans cet environnement CPU. Elle ne garantit pas des résultats identiques entre toutes les versions et toutes les machines.

---

## Algorithme expliqué — Entraîner le réseau du projet

**Objectif :** apprendre des paramètres et sélectionner une itération sans accès au test. **Entrées :** données préparées, architecture et grille annoncée.

**Traitement :** initialiser ; prédire sur train ; calculer la perte ; remettre les gradients à zéro ; rétropropager ; mettre à jour ; évaluer la validation sans gradient ; sauvegarder le meilleur état ; appliquer la règle d'arrêt.

**Sortie :** paramètres restaurés, pertes et réglages. Exemple : si la meilleure validation est à l'itération 120 et que l'arrêt survient à 200, le modèle rendu est celui de 120.

Références : [PyTorch — autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html), [boucle d'optimisation](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html).

---

## Erreurs fréquentes

- Passer des probabilités à BCEWithLogitsLoss.
- Fournir des cibles de forme (n,) face à une sortie (n,1).
- Accumuler les gradients par oubli de zero_grad.
- Croire que backward modifie automatiquement les poids.
- Garder les derniers poids sans appliquer la règle de sélection.

---

## Exercice 1 — Lire les formes d'un réseau

**Objectif pédagogique :** Relier NumPy et PyTorch. **Prérequis :** Matrices et nn.Linear.

**Énoncé :** Pour X de forme (5,3), donner les formes des poids, biais et sorties d'une couche Linear(3,4), puis de Linear(4,1). Combien de paramètres ?

**Contraintes :** Préciser la convention de stockage PyTorch.

**Livrable attendu :** Tableau des formes et total.

**Critères de réussite :** Sortie finale (5,1) et 21 paramètres.

<details><summary>Indices gradués</summary>

1. Le poids PyTorch est stocké sorties×entrées.
2. Chaque sortie d'une couche possède un biais.

</details>

---

## Correction — Lire les formes d'un réseau

<details><summary>Afficher la correction</summary>

Première couche : poids (4,3), biais (4,), sortie (5,4). Seconde : poids (1,4), biais (1,), sortie (5,1). Total 12+4+4+1=21. Les cinq observations ne multiplient pas le nombre de paramètres.

</details>


---

## Exercice 2 — Observer l'accumulation des gradients

**Objectif pédagogique :** Expliquer zero_grad. **Prérequis :** Dérivée d'un carré et autograd.

**Énoncé :** Créer w=2 avec suivi de gradient. Calculer deux fois la dérivée de (w−3)² sans effacer .grad, puis recommencer après effacement. Prédire les valeurs.

**Contraintes :** Recalculer une nouvelle perte avant chaque backward.

**Livrable attendu :** Trois gradients et une explication.

**Critères de réussite :** Valeurs -2, -4 puis -2.

<details><summary>Indices gradués</summary>

1. La dérivée vaut -2 au point w=2.
2. Les appels à backward ajoutent leur contribution au gradient existant.

</details>

---

## Correction — Observer l'accumulation des gradients

<details><summary>Afficher la correction</summary>

La variable reste à 2 ; seuls ses gradients s'accumulent.

```python
import torch
w = torch.tensor(2., requires_grad=True)
((w-3)**2).backward()
print(float(w.grad))
((w-3)**2).backward()
print(float(w.grad))
w.grad = None
((w-3)**2).backward()
print(float(w.grad))
```

L'affichage est -2, -4, -2. Il n'y a aucune mise à jour des poids sans optimiseur ou opération explicite.

</details>


---

## Exercice 3 — Corriger et contrôler un entraînement

**Objectif pédagogique :** Déboguer une boucle et garder le bon état. **Prérequis :** Perte, backward, step et validation.

**Énoncé :** Une boucle appelle step avant backward, n'efface jamais les gradients et retourne systématiquement les derniers poids. Décrire les corrections puis entraîner la référence logistique du projet.

**Contraintes :** Ne pas consulter le test. Utiliser la validation pour choisir l'itération.

**Livrable attendu :** Boucle ordonnée, courbes et itération sélectionnée.

**Critères de réussite :** Gradient remis à zéro avant le backward ; meilleur état restauré.

<details><summary>Indices gradués</summary>

1. Repartir de l'ordre calcul avant → perte → gradients → mise à jour.
2. La meilleure validation peut précéder l'arrêt.

</details>

---

## Correction — Corriger et contrôler un entraînement

<details><summary>Afficher la correction</summary>

La fonction fournie applique la séquence et garde le meilleur état.

```python
from parcours import preparer, entrainer
d = preparer()
r = entrainer(d['Z'], d['classes'], architecture='logistique', iterations=80, patience=30)
assert 1 <= r['iteration'] <= len(r['trace'])
assert r['perte_validation'] <= r['trace'][0, 2] + 1e-7
print(r['architecture'], r['iteration'])
```

Le résultat contient les paramètres restaurés et une trace. Aucun score test n'est calculé dans cette fonction.

</details>


---

## Projet fil rouge

### Contexte et utilisateurs

Une équipe de gestion énergétique souhaite comprendre des profils de journées et préparer une prévision. Les 240 journées sont entièrement simulées ; les résultats ne constituent pas une étude de bâtiment réel.

### Problème à résoudre et fonctionnalités cibles

Reprendre les données et le réseau de la semaine 1. Entraîner une logistique et le réseau 3→4→1 ; comparer la petite grille de pas sur validation et conserver les courbes.

### Modèle de données et architecture attendue

Réutiliser `pratique/depart.py`, `pratique/parcours.py` et le même notebook. Les entrées sont température, occupation et équipements. La consommation est la cible, jamais une entrée du classificateur. Les jours 1–144 servent à apprendre, 145–192 à valider, 193–240 au bilan final.

---

## Projet fil rouge — Livrables et validation

### Jalon relié à la séance

Annoncer les réglages et la graine, sauvegarder les pertes et le meilleur état, puis expliquer une ligne de la boucle. À observer : double sigmoïde, cibles de mauvaise forme, accumulation et test utilisé pour choisir.

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

**Solution étudiée :** Tenseurs, logits, autograd et boucle d'entraînement reproductible.

**Bénéfice attendu :** comprendre les hypothèses et contrôler les résultats avant une utilisation sur des données réelles. Une amélioration numérique ne démontre pas une économie d'énergie ni une causalité.

---

## Fiche de révision

- PyTorch conserve les conventions de calcul mais automatise les gradients.
- Logits et cibles doivent avoir des formes compatibles.
- zero_grad, backward et step remplissent des rôles distincts.
- L'état retenu provient de la validation et doit être restauré.

---

## Questions de révision

1. Que stocke nn.Linear dans weight ?
2. Pourquoi ne faut-il pas appliquer la sigmoïde avant BCEWithLogitsLoss ?
3. Que fait backward et que fait step ?
4. Quelle différence existe entre eval et no_grad ?
5. Pourquoi sauvegarder une copie de l'état et non une référence mutable ?

---

## QCM — Questions 1 à 2

**1. Linear(3,4) stocke un poids de forme**

A. (3,4) ; B. (4,3) ; C. (3,3) ; D. (4,4).

**2. BCEWithLogitsLoss reçoit**

A. les logits ; B. les décisions arrondies ; C. la matrice de confusion ; D. une sigmoïde déjà appliquée.

<details><summary>Afficher la correction</summary>

1. **B** : les sorties sont la première dimension des poids PyTorch

2. **A** : la fonction intègre le traitement stable des logits

</details>

---

## QCM — Questions 3 à 5

**3. backward calcule**

A. le meilleur seuil ; B. la partition ; C. les gradients ; D. la sauvegarde finale.

**4. step réalise**

A. la création des étiquettes ; B. une nouvelle standardisation ; C. la sélection du test ; D. la mise à jour des paramètres.

**5. Le meilleur état du projet est choisi sur**

A. la dernière ligne du CSV ; B. la perte de validation ; C. l'exactitude test ; D. le nombre de paramètres seul.

<details><summary>Afficher la correction</summary>

3. **C** : il remonte les dépendances du calcul

4. **D** : l'optimiseur utilise les gradients disponibles

5. **B** : la règle d'arrêt et de choix ne consulte pas le test

</details>

---

## Résumé final

PyTorch conserve les conventions de calcul mais automatise les gradients.
Logits et cibles doivent avoir des formes compatibles.
zero_grad, backward et step remplissent des rôles distincts.
L'état retenu provient de la validation et doit être restauré.

[Continuer le parcours](08_evaluer.md) · [Programme et livrables](programme.md).
