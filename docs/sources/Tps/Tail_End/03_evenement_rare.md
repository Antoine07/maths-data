# Problème 3 — Une rencontre peut-elle disparaître dans 99 % de variance ?

## Le point de départ

Noé résume ses six prochaines semaines dans un tableau. Il compte des sessions vidéo et les occasions de voir un proche qui habite loin.

Un outil lui propose de compresser son tableau : « Nous conservons plus de 99 % de la variance. » Noé se demande si cela suffit pour conserver ce qui compte dans sa question.

Le tableau est fictif et toutes les semaines sont connues pour cet exercice descriptif. Il ne s'agit pas d'une évaluation prédictive.

---

## Objectif et prérequis

**Objectif pédagogique :** distinguer une erreur globale de reconstruction et la préservation d'un événement rare.

**Prérequis :** [centrage-réduction](../../Slides/stat/03_centrage_reduction.md), [ACP](../../Slides/stat/04_acp_intro.md) et [SVD](../../Slides/avance/03_svd_acp.md).

Le sens des colonnes est choisi pour illustrer le problème ; il ne leur attribue pas de valeur universelle.

---

## Données et énoncé

| Semaine | Sessions vidéo | Rencontres avec le proche |
|---:|---:|---:|
| 1 | 10 | 0 |
| 2 | 12 | 0 |
| 3 | 14 | 0 |
| 4 | 16 | 0 |
| 5 | 18 | 0 |
| 6 | 20 | 1 |

1. Centrer les deux colonnes, sans standardiser. Réaliser la SVD et calculer les parts de variance.
2. Conserver un seul axe et reconstruire le tableau en réajoutant les moyennes.
3. Examiner la valeur reconstruite de la rencontre en semaine 6. Une règle descriptive signale une semaine si cette valeur atteint 0,75. Que devient le signal ?
4. Recommencer après standardisation des deux colonnes. Un axe suffit-il encore à conserver 95 % de variance ?
5. Proposer une représentation et un critère de contrôle qui préservent l'information nécessaire à Noé.

---

## Contraintes, livrables et critères de réussite

**Contraintes :** ne pas arrondir les reconstructions en cours de calcul ; appliquer la même règle de 0,75 avant et après compression ; ne pas confondre cette reconstruction descriptive avec un comptage réel.

**Livrables :** parts de variance, tableau reconstruit, graphique, réponse au seuil et choix argumenté d'une autre représentation.

**Critères de réussite :** annoncer la bonne part de variance, détecter l'atténuation de l'événement rare et distinguer variance de valeur d'usage.

<details><summary>Indices gradués</summary>

1. Les parts utilisent les carrés des valeurs singulières.
2. La reconstruction de rang 1 est `(Xc @ Vt[:1].T) @ Vt[:1] + moyenne`.
3. Une perte globale peut être petite alors que l'erreur sur une colonne ou une ligne particulière est importante.
</details>

---

## Correction — Une bonne compression, selon quelle métrique ?

<details><summary>Afficher la correction</summary>

Le premier axe conserve environ **99,331 %** de la variance du tableau centré non standardisé. Pourtant, la rencontre de la semaine 6 passe de 1 à environ **0,529** après reconstruction de rang 1.

La règle de 0,75 signale la semaine avant compression mais plus après. Elle était fixée avant le calcul : nous n'avons pas changé le seuil pour fabriquer cette comparaison.

![La reconstruction de rang 1 suit surtout les sessions vidéo et réduit la rencontre de la semaine 6 d'une valeur 1 à environ 0,529.](../../Slides/figures/tail-03-variance.svg)

La reconstruction peut produire des valeurs fractionnaires, voire négatives, car une projection linéaire n'impose pas des comptes entiers positifs. Ce n'est donc pas un calendrier directement exploitable.
</details>

---

## Correction — Changer l'échelle change le compromis

<details><summary>Afficher la correction</summary>

Après standardisation, les parts deviennent environ **82,73 %** et **17,27 %**. Le seuil de 95 % impose les deux axes : il n'y a plus de réduction de dimension à ce seuil.

La standardisation change les poids implicites de l'erreur : chaque colonne possède désormais la même variance. Elle ne garantit pas pour autant de préserver tous les événements importants dans tous les tableaux.

On peut conserver explicitement la colonne des rencontres, construire une vue séparée des événements rares et contrôler l'erreur par colonne ou le nombre d'événements effacés par la règle descriptive.

La métrique doit correspondre à la question. Il n'est pas nécessaire de compresser toutes les informations dans un seul indicateur.
</details>

---

## Correction — Contrôle avec Python

<details><summary>Afficher la correction</summary>

```python
import numpy as np
X = np.column_stack([np.arange(10., 22., 2.), [0, 0, 0, 0, 0, 1]])
mu = X.mean(axis=0)
Xc = X - mu
_, s, Vt = np.linalg.svd(Xc, full_matrices=False)
reconstruction = (Xc @ Vt[:1].T) @ Vt[:1] + mu
print(100*s[0]**2 / np.sum(s**2))
print(reconstruction[-1, 1])
_, ss, _ = np.linalg.svd(Xc / X.std(axis=0), full_matrices=False)
print(100*ss**2 / np.sum(ss**2))
```

**Lecture :** les entrées sont six semaines et deux variables. Le code centre, décompose, tronque et reconstruit, puis refait le diagnostic sur des colonnes standardisées. Les sorties sont environ `99.331`, `0.529` et `[82.733, 17.267]`.

**Erreur fréquente :** lire 99,331 % comme le pourcentage de rencontres correctement préservées. Il s'agit d'une fraction de variance globale dans la géométrie choisie.
</details>

---

## Discussion — La rareté n'est pas le bruit

Une rencontre rare peut être importante pour la question posée, même si elle contribue peu à la variance d'un tableau brut.

**Lien data / IA :** une bonne reconstruction globale ne garantit pas de préserver une anomalie, un défaut industriel rare ou une caractéristique utile à une cible. La représentation doit être évaluée selon l'usage prévu.

[Retour aux quatre problèmes](README.md). Inspiration du comptage des occasions : [*The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html) ; expérience SVD originale.
