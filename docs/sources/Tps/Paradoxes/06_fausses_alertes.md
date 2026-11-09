# Excellent détecteur, mauvaises alertes ?

## Objectif et prérequis

**Après :** [classification et rétropropagation](../../Slides/avance/06_retropropagation.md) et [probabilités essentielles](../../Slides/stat/probabilites.md).

**Objectif :** relier fréquence de base, précision, rappel et exactitude. Le problème introduit la formule de Bayes à partir d'un tableau d'effectifs.

## La situation

Une usine fictive évalue un détecteur sur 100 000 objets, dont 0,1 % sont défectueux. Le détecteur signale 99 % des objets défectueux et déclenche une fausse alerte sur 1 % des objets normaux.

Le responsable entend « 99 % » et pense que 99 % des alertes correspondent à un défaut. Est-ce la même probabilité ?

---

## Énoncé

1. Compter les objets défectueux et normaux. Construire la matrice de confusion complète, lignes réelles et colonnes prédites.
2. Calculer le rappel : parmi les objets défectueux, quelle part est détectée ? Calculer la précision : parmi les alertes, quelle part correspond à un défaut ?
3. Calculer l'exactitude globale. La comparer à celle d'une règle qui déclare tous les objets normaux. Pourquoi l'exactitude seule ne suffit-elle pas ?
4. Refaire le calcul de précision avec 1 % de défauts, en conservant par hypothèse le rappel et le taux de fausses alertes.
5. Écrire une formule donnant la précision en fonction de la fréquence des défauts $\pi$. Quelle information manque si l'on annonce seulement « exactitude de 99 % » ?

## Contraintes, livrables et critères de réussite

**Contraintes :** nommer le dénominateur de chaque indicateur ; appliquer 1 % aux objets normaux, pas à tous les objets ; ne pas supposer les performances conditionnelles invariantes dans un vrai changement de contexte.

**Livrables :** matrice, indicateurs, graphique et reformulation claire des deux probabilités.

**Critères :** précision très différente du rappel ; comparaison avec une référence ; distinction entre $P(\text{alerte}\mid\text{défaut})$ et $P(\text{défaut}\mid\text{alerte})$.

<details><summary>Indices gradués</summary>

1. Il y a 100 objets défectueux et 99 900 objets normaux.
2. Les fausses alertes peuvent être nombreuses car elles concernent une population beaucoup plus grande.
3. La précision divise les vraies alertes par **toutes** les alertes.
</details>

---

## Correction — Compter avant d'interpréter

<details><summary>Afficher la correction</summary>

| Réalité | Alerte | Pas d'alerte |
|---|---:|---:|
| Défaut | 99 | 1 |
| Normal | 999 | 98 901 |

Le rappel vaut $99/100=99\%$. La précision vaut $99/(99+999)\approx9{,}02\%$ : environ neuf alertes sur dix sont fausses dans ce scénario.

L'exactitude vaut $(99+98\,901)/100\,000=99\%$. La règle « toujours normal » atteint même 99,9 %, mais manque les 100 défauts. L'indicateur pertinent dépend du coût des erreurs.

![Le détecteur produit 99 vraies alertes et 999 fausses alertes ; la précision augmente avec la fréquence des défauts si les taux conditionnels restent fixes.](../../Slides/figures/paradoxe-alertes.svg)
</details>

---

## Correction — Retrouver Bayes avec les effectifs

<details><summary>Afficher la correction</summary>

Notons $s$ la sensibilité, $f$ le taux de fausses alertes parmi les normaux et $\pi$ la fréquence des défauts. Alors :

$$
P(\text{défaut}\mid\text{alerte})=
\frac{s\pi}{s\pi+f(1-\pi)}.
$$

Le numérateur compte la proportion de vraies alertes ; le dénominateur ajoute les fausses alertes. C'est une application de la formule de Bayes.

Avec $\pi=1\%$, $s=99\%$ et $f=1\%$, on obtient 990 vraies et 990 fausses alertes sur 100 000 objets : la précision vaut 50 %.

Une exactitude globale ne donne ni la fréquence de base, ni la répartition des erreurs. Elle ne permet pas, seule, de répondre à la question « mon alerte correspond-elle à un défaut ? ».
</details>

---

## Correction — Contrôle Python

<details><summary>Afficher la correction</summary>

```python
population = 100000
for prevalence in (0.001, 0.01):
    defauts = population * prevalence
    vp = 0.99 * defauts
    fp = 0.01 * (population - defauts)
    print(round(vp), round(fp), round(100*vp/(vp+fp), 2))
```

**Lecture :** la boucle change uniquement la fréquence de base du scénario. Les sorties sont `99 999 9.02` et `990 990 50.0`.

**Erreur fréquente :** identifier la précision au rappel, ou appliquer le taux de fausses alertes aux seuls objets défectueux.
</details>

## Discussion — Une alerte n'est pas un diagnostic certain

Une réduction du taux de fausses alertes peut améliorer la précision, mais changer le seuil peut aussi diminuer le rappel. Les coûts des défauts manqués et des inspections inutiles doivent être discutés avant de choisir le seuil sur la validation.

**Lien IA :** évaluer sur une population représentative de l'usage prévu et publier les effectifs de confusion avec les pourcentages.

Référence : [MIT — probabilités conditionnelles et fréquence de base](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/mit18_05_s22_probability.pdf). Les objets et effectifs sont fictifs.

[Tous les problèmes du parcours](../../docs/problemes.html).
