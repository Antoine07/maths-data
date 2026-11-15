# Problème 1 — La moitié des années, combien de rencontres ?

## Le point de départ

Léa a 30 ans. Elle pense : « Si je regarde jusqu'à mes 60 ans, il reste autant de temps qu'il en est passé. »

Ce raisonnement compte des années. Mais Léa veut maintenant compter les journées où elle voit un proche. Elle n'a pas toujours vécu au même endroit.

Le scénario est fictif ; l'horizon de 60 ans est fixé pour l'exercice et n'est pas une prévision de durée de vie.

---

## Objectif et prérequis

**Objectif pédagogique :** définir un indicateur, vérifier ses unités et comprendre le rôle du dénominateur.

**Prérequis :** [révisions d'algèbre](../../Slides/revision.md), multiplication et pourcentages. Aucune probabilité n'est nécessaire.

**Travail attendu :** calcul manuel avec des sommes finies, puis script Python utilisant NumPy et un seul graphique Matplotlib à deux panneaux.

---

## Données et unités

| Période | Durée | Journées de rencontre par an |
|---|---:|---:|
| De 0 à 18 ans | 18 ans | 300 |
| De 18 à 30 ans | 12 ans | 12 |
| De 30 à 60 ans, scénario de base | 30 ans | 12 |

Une journée où plusieurs rencontres ont lieu ne compte qu'une fois. Les journées ne sont pas des durées de 24 h passées ensemble : c'est notre unité de comptage.

Les fréquences sont supposées constantes à l'intérieur de chaque période. Le modèle ne pondère ni la durée ni la qualité des rencontres.

---

## Énoncé

1. En notant $a$ l'âge au début de l'année, écrire avec le symbole somme $\sum$ le total des journées de rencontre passées et celui des journées futures. Utiliser les bornes du tableau et le fait que la fréquence est constante sur chaque période pour calculer ces sommes.
2. Calculer deux pourcentages : **la part des années restantes** parmi les 60 années de l'horizon, puis **la part des journées de rencontre futures** parmi toutes les journées de rencontre prévues entre 0 et 60 ans (journées passées + journées futures). Comparer ces deux pourcentages.
3. Dessiner une grille où chaque point représente **12 journées de rencontre**, en distinguant passé et futur. Combien de points faut-il ?
4. Léa passe désormais à 24 journées de rencontre par an. Recalculer le futur, le total et la fraction future. Le passé change-t-il ? La fraction future est-elle exactement doublée ?
5. Formuler une conclusion conditionnelle : qu'affirme le calcul et qu'ignore-t-il ?

---

## À réaliser — Un script NumPy et un graphique

Écrire un script autonome à partir des paramètres suivants, **après les calculs manuels** :

```python
import numpy as np
import matplotlib.pyplot as plt

age_actuel = 30
age_fin = 60
rencontres_enfance = 300
rencontres_adulte = 12
rencontres_futures = 12
```

1. Construire `ages` avec `np.arange(age_fin)`, puis un tableau `rencontres` contenant une valeur par année : 18 valeurs pour l’enfance, `age_actuel - 18` pour la vie adulte passée et `age_fin - age_actuel` pour le futur. Utiliser `np.full` et `np.concatenate`. Vérifier que les deux tableaux ont la forme `(60,)`.
2. Séparer passé et futur par **slicing** à l’indice `age_actuel`. Calculer les trois totaux avec `np.sum`, puis les pourcentages d’années restantes et de journées futures.
3. Retrouver le nombre de points de la grille pour une unité de 12 journées. Vérifier que les totaux sont divisibles par 12 avant d’utiliser `//` : une division entière peut sinon masquer un reste.
4. Créer une **copie** du tableau, doubler uniquement les valeurs futures, puis recalculer le total et la part future. Vérifier que le tableau initial et le passé restent inchangés.
5. Comparer les fréquences `np.array([6, 12, 24, 36, 52, 100])`. Calculer les journées futures, les totaux et les proportions par **opérations vectorisées**, sans boucle de calcul. Une boucle est autorisée pour afficher le tableau des résultats.
6. Créer une seule figure Matplotlib avec deux panneaux : à gauche, les journées de rencontre par année et une ligne à `age_actuel - 0.5` pour séparer passé et futur ; à droite, la part future en fonction des fréquences testées, avec un repère horizontal à 50 %.
7. Afficher une conclusion qui distingue les années et les journées de rencontre, puis rappelle les hypothèses du modèle.

**Repères NumPy :** `np.full(n, valeur)` répète une valeur ; `np.concatenate` assemble les blocs. `tableau[:indice]` sélectionne ce qui précède l’indice, et `tableau[indice:]` ce qui le suit, indice compris. `np.sum` additionne un tableau ; `copy()` permet de modifier un scénario sans écraser l’original. Une opération entre un tableau et un scalaire s’applique à chaque élément.

**Lecture des âges :** la case d’indice 0 représente l’année de 0 à 1 an, et la case 59 celle de 59 à 60 ans. L’âge de fin n’est pas inclus dans `np.arange` ; on compte bien 60 années, sans ajouter une année supplémentaire.

---

## Contraintes, livrables et critères de réussite

**Contraintes :** annoncer toutes les unités ; conserver les jours passés lorsque le futur change ; ne pas transformer un horizon fixé en certitude.

**Livrables :** calculs manuels avec sommes, grille de points, script `.py` exécutable, tableau des six scénarios, figure à deux panneaux et conclusion de cinq lignes.

**Critères de réussite :** nombres cohérents avec les trois périodes, dénominateur recalculé dans chaque scénario, tableau initial conservé, calcul vectorisé des six fréquences et axes avec unités. La légende de la grille indique l’unité de chaque point.

<details><summary>Indices gradués</summary>

1. Pour chaque période : années × journées par an = journées.
2. La part future est `futur / (passé + futur)`.
3. En doublant la fréquence future, le numérateur **et** le dénominateur changent.
</details>

---

## Correction — Calculs et représentation

<details><summary>Afficher la correction</summary>

Enfance : $\sum_{a=0}^{17}300=18\times300=5\,400$ journées. Vie adulte passée : $\sum_{a=18}^{29}12=12\times12=144$ journées. Le passé total vaut donc $5\,544$ journées.

Le futur du scénario de base vaut $\sum_{a=30}^{59}12=30\times12=360$ journées. Le total de l'horizon vaut $5\,904$ journées.

La moitié des années de l'horizon restent, mais la part des journées futures vaut :

$$
\frac{360}{5\,544+360}\approx0{,}06098=6{,}10\%.
$$

![492 points, dont 462 pour le passé et 30 pour le futur ; chaque point représente 12 journées de rencontre.](../../Slides/figures/tail-01-rencontres.svg)

La grille contient $5\,904/12=492$ points : 462 pour le passé et 30 pour le futur. Les points représentent des journées de rencontre, pas des années de vie.
</details>

---

## Correction — Changer le futur sans réécrire le passé

<details><summary>Afficher la correction</summary>

Avec 24 journées par an, le futur vaut 720 journées et le total vaut $5\,544+720=6\,264$ journées.

$$
\text{Nouvelle part future}=\frac{720}{6\,264}\approx11{,}49\%.
$$

Le nombre futur double, mais le pourcentage ne double pas exactement : le total change aussi. Le passé reste à 5 544 journées.

Conclusion possible : **si** les fréquences et l'horizon fixés se réalisent, le modèle compte 360 journées futures dans le scénario de base. Il ne mesure ni la qualité des relations, ni la durée des visites, ni les événements qui pourraient modifier les fréquences.
</details>

---

## Correction — Script NumPy et Matplotlib

<details><summary>Afficher la correction</summary>

[Télécharger le script Python complet](../../Slides/exemples/rencontres/rencontres_numpy.py).

**Résultats attendus :** 5 544 journées passées, 360 futures et 5 904 au total ; 50 % des années restent, mais environ 6,10 % des journées de rencontre. La grille compte 462 points passés et 30 futurs, soit 492 points. Avec 24 journées par an dans le futur : 720 journées futures, un total de 6 264 et une part d’environ 11,49 %.

**Lecture du code :** `ages` et `rencontres` ont la forme `(60,)`. Les deux premières tranches forment le passé ; la dernière forme le futur. Les durées des blocs sont calculées à partir des âges pour rester cohérentes si l’on adapte le scénario, avec `18 <= age_actuel < age_fin`.

`rencontres.copy()` conserve les données initiales. L’affectation sur la tranche future ne change que le scénario copié. Dans la comparaison vectorisée, `frequences`, `jours_futurs_scenarios`, `totaux` et `proportions` ont la forme `(6,)`. La boucle finale sert uniquement à présenter les résultats déjà calculés.

```python
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# TP — La moitié des années, combien de rencontres ?
# NumPy + Matplotlib
# ============================================================

# 1. PARAMÈTRES DU MODÈLE

age_actuel = 30
age_fin = 60

# Nombre de journées de rencontre par an
rencontres_enfance = 300    # De 0 à 18 ans
rencontres_adulte = 12      # De 18 ans à l'âge actuel
rencontres_futures = 12     # De l'âge actuel à l'âge de fin

# 2. CONSTRUIRE LE TABLEAU NUMPY

ages = np.arange(age_fin)

rencontres = np.concatenate([
    np.full(18, rencontres_enfance),
    np.full(age_actuel - 18, rencontres_adulte),
    np.full(age_fin - age_actuel, rencontres_futures)
])

print("Tableau des rencontres :")
print(rencontres)
print("Nombre d'années :", len(rencontres))

# 3. CALCULER LE PASSÉ ET LE FUTUR

passe = rencontres[:age_actuel]
futur = rencontres[age_actuel:]

jours_passes = np.sum(passe)
jours_futurs = np.sum(futur)
jours_total = np.sum(rencontres)

part_annees = (age_fin - age_actuel) / age_fin * 100
part_future = jours_futurs / jours_total * 100

print("\n===== SITUATION INITIALE =====")
print(f"Journées passées : {jours_passes}")
print(f"Journées futures : {jours_futurs}")
print(f"Total : {jours_total}")
print(f"Années restantes : {part_annees:.2f} %")
print(f"Rencontres futures : {part_future:.2f} %")

# 4. REPRÉSENTATION EN POINTS
# 1 point = 12 journées de rencontre.
# Ici les deux totaux sont divisibles par 12 : // ne perd aucun reste.

unite = 12
points_passes = jours_passes // unite
points_futurs = jours_futurs // unite

print("\n===== REPRÉSENTATION EN POINTS =====")
print(f"Points passés : {points_passes}")
print(f"Points futurs : {points_futurs}")
print(f"Total : {points_passes + points_futurs}")

# 5. SCÉNARIO : DOUBLER LES RENCONTRES FUTURES

nouvelles_rencontres = rencontres.copy()
nouvelles_rencontres[age_actuel:] = 2 * rencontres_futures

nouveau_futur = np.sum(nouvelles_rencontres[age_actuel:])
nouveau_total = np.sum(nouvelles_rencontres)
nouvelle_part = nouveau_futur / nouveau_total * 100

print("\n===== SCÉNARIO DOUBLÉ =====")
print(f"Journées futures : {nouveau_futur}")
print(f"Total : {nouveau_total}")
print(f"Part future : {nouvelle_part:.2f} %")

# 6. SIMULER PLUSIEURS FRÉQUENCES
# Vectorisation NumPy : la boucle suivante sert seulement à l'affichage.

frequences = np.array([6, 12, 24, 36, 52, 100])
duree_future = age_fin - age_actuel
jours_futurs_scenarios = frequences * duree_future
totaux = jours_passes + jours_futurs_scenarios
proportions = jours_futurs_scenarios / totaux * 100

print("\n===== COMPARAISON DES SCÉNARIOS =====")
for frequence, jours, proportion in zip(
    frequences, jours_futurs_scenarios, proportions
):
    print(
        f"{frequence:3d} jours/an | "
        f"{jours:4d} jours futurs | "
        f"{proportion:6.2f} %"
    )

# 7. GRAPHIQUE — DEUX LECTURES DU MODÈLE

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

axes[0].bar(ages, rencontres, color="steelblue")
axes[0].axvline(age_actuel - 0.5, color="red", linestyle="--")
axes[0].set(xlabel="Âge au début de l'année", ylabel="Journées par an",
            title="Fréquence annuelle")
axes[0].grid(axis="y", alpha=0.3)

axes[1].plot(frequences, proportions, marker="o", color="darkgreen")
axes[1].axhline(50, color="red", linestyle="--", label="50 %")
axes[1].set(xlabel="Journées futures par an", ylabel="Part future (%)",
            title="Scénarios de fréquence")
axes[1].grid(alpha=0.3)
axes[1].legend()

fig.tight_layout()
plt.show()

# 8. CONCLUSION

print("\n===== CONCLUSION =====")
print(
    f"Il reste {part_annees:.0f} % des années, "
    f"mais seulement {part_future:.2f} % "
    "des journées de rencontre."
)
print(
    f"En doublant les rencontres futures, "
    f"cette proportion atteint {nouvelle_part:.2f} %."
)
print(
    "Les résultats dépendent des hypothèses "
    "de fréquence et de durée retenues."
)
```

**Lire la figure.** Le panneau gauche montre les journées de rencontre par année et sépare le passé du futur. Le panneau droit compare les scénarios de fréquence future avec le même passé ; les segments relient les scénarios calculés et ne représentent pas des observations réelles.

![Une figure en deux panneaux : fréquence annuelle des rencontres et part future selon six scénarios.](../../Slides/images/rencontres-analyse.svg)

À 100 journées par an pendant les 30 années futures, le modèle compte 3 000 journées futures sur 8 544, soit environ 35,11 %. Le repère à 50 % n’est donc atteint par aucun des six scénarios proposés.

**Erreur fréquente :** conserver le total 5 904 lorsque la fréquence future change. Le nombre futur et le dénominateur doivent être recalculés ensemble : doubler le nombre de journées futures ne double pas exactement leur proportion.

**Limites :** ces graphiques représentent un scénario fictif et des fréquences supposées. Ils ne mesurent ni la durée des visites ni la qualité des relations, et ne prédisent pas une trajectoire individuelle.

</details>

---

## Discussion — Ce que cet indicateur raconte

Les années et les rencontres ne sont pas réparties de la même façon. Pour rendre l'indicateur utile, il faut expliciter son unité, ses périodes et ses hypothèses.

Une grille peut rendre un ordre de grandeur visible tout en donnant une impression de certitude. La légende et la conclusion conditionnelle font partie de la réponse mathématique.

**Lien data :** avant de construire un tableau de bord, définir précisément ce que représente une ligne, un point et un pourcentage.

[Retour aux quatre problèmes](README.md). Idée de départ : [Tim Urban, *The Tail End*](https://waitbutwhy.com/2015/12/the-tail-end.html) ; scénario et calculs originaux.
