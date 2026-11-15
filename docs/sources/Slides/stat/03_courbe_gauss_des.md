---
marp: true
theme: default
paginate: true
class: lead
---

# Comment la courbe de Gauss apparaît à partir des dés

**Une expérience à construire :** un dé n'a pas une forme en cloche. Pourtant, les moyennes de plusieurs dés s'en rapprochent.

---

## TP guidé · Construire les graphiques dans un notebook

Ouvrez le [notebook à compléter](https://antoine07.github.io/maths-data/stat/notebooks/gauss_des_depart.ipynb). Il vous guide du lancer simple à la courbe normale.

Les cellules de code sont à compléter. Des indications donnent les fonctions Matplotlib utiles ; la correction complète se trouve dans un volet replié à la fin du notebook.

| Pour représenter… | Fonctions à chercher dans le notebook |
|---|---|
| les probabilités des faces | `plt.bar`, `plt.xticks` |
| la distribution des moyennes | `plt.hist` |
| la moyenne théorique | `plt.axvline` |
| une courbe normale | `plt.plot`, `np.exp`, `np.linspace` |
| titres et axes | `plt.title`, `plt.xlabel`, `plt.ylabel`, `plt.legend`, `plt.show` |

---

## Un dé : six résultats équiprobables

Un dé équilibré donne les résultats $1,2,3,4,5,6$, chacun avec une probabilité de $1/6$.

La moyenne théorique vaut

$$
\mu=\frac{1+2+3+4+5+6}{6}=3{,}5.
$$

La moyenne est au milieu des faces, même si aucun lancer ne donne 3,5. La distribution d'un lancer est **uniforme**, pas en forme de cloche.

```python
import numpy as np
import matplotlib.pyplot as plt

de = np.arange(1, 7)
proba = np.full(6, 1 / 6)
moyenne_theorique = de.mean()

plt.bar(de, proba, color="steelblue")
plt.axvline(moyenne_theorique, color="tomato", linestyle="--", label="Moyenne : 3,5")
plt.xticks(de)
plt.xlabel("Résultat du lancer")
plt.ylabel("Probabilité")
plt.title("Un lancer : six issues équiprobables")
plt.legend()
plt.show()
```

---

## Deux dés : les résultats du milieu ont plus de façons d'arriver

On lance deux dés et on calcule leur moyenne. Il y a $6\times6=36$ couples possibles.

La moyenne 3,5 correspond à une somme de 7. Six couples la produisent : $(1,6),(2,5),\ldots,(6,1)$. La moyenne 6 ne vient que du couple $(6,6)$.

```python
moyennes_2 = []
for de1 in range(1, 7):
    for de2 in range(1, 7):
        moyennes_2.append((de1 + de2) / 2)

bornes = np.arange(0.75, 6.76, 0.5)
plt.hist(moyennes_2, bins=bornes, color="steelblue", edgecolor="white")
plt.axvline(3.5, color="tomato", linestyle="--", label="Moyenne théorique : 3,5")
plt.xlabel("Moyenne des deux dés")
plt.ylabel("Nombre de couples sur 36")
plt.title("Deux dés : les moyennes centrales sont plus fréquentes")
plt.legend()
plt.show()
```

La distribution devient triangulaire : les résultats proches du centre ont davantage de combinaisons.

---

## Pratique · Répéter l'expérience

Une expérience consiste à lancer $n$ dés et à calculer leur moyenne. On la répète 10 000 fois.

```python
rng = np.random.default_rng(2026)

def simuler_moyennes(n, repetitions=10_000):
    moyennes = []
    for _ in range(repetitions):
        des = rng.integers(1, 7, size=n)
        moyennes.append(sum(des) / n)
    return moyennes

for n in [1, 2, 5, 10, 30]:
    moyennes = simuler_moyennes(n)
    plt.figure(figsize=(7, 3))
    plt.hist(moyennes, bins=35, range=(1, 6), color="steelblue", edgecolor="white")
    plt.axvline(3.5, color="tomato", linestyle="--", label="Moyenne théorique : 3,5")
    plt.title(f"Moyennes de {n} dé(s), sur 10 000 expériences")
    plt.xlabel("Moyenne obtenue")
    plt.ylabel("Nombre d'expériences")
    plt.legend()
    plt.show()
```

`rng.integers(1, 7, size=n)` simule les dés d'une expérience. La boucle extérieure recommence cette expérience ; `sum(des) / n` calcule la moyenne observée.

---

## Observer la transformation

| Dés par expérience | Forme observée pour les moyennes |
|---:|---|
| 1 | uniforme, comme les faces du dé |
| 2 | triangulaire, avec un centre fréquent |
| 5 | une forme en cloche commence à apparaître |
| 10 | une cloche plus régulière |
| 30 | une cloche resserrée autour de 3,5 |

Les simulations varient légèrement. La tendance est le point important : **les moyennes se rapprochent d'une distribution normale**, même si les dés individuels ne suivent pas une loi normale.

La courbe de Gauss est la représentation graphique de la densité d'une loi normale.

---

## Superposer une courbe de Gauss

Pour 30 dés, on peut comparer l'histogramme des moyennes à une courbe normale ayant la même moyenne théorique et le même écart-type théorique.

```python
n = 30
sigma_de = (35 / 12) ** 0.5
sigma_moyennes = sigma_de / (n ** 0.5)
x = np.linspace(2.5, 4.5, 300)

densite = (1 / (sigma_moyennes * (2 * np.pi) ** 0.5)) * np.exp(
    -0.5 * ((x - 3.5) / sigma_moyennes) ** 2
)

moyennes_30 = simuler_moyennes(n)
plt.hist(moyennes_30, bins=30, density=True, alpha=0.65, label="Moyennes simulées")
plt.plot(x, densite, color="tomato", linewidth=2, label="Courbe normale théorique")
plt.xlabel("Moyenne des 30 dés")
plt.ylabel("Densité (aire totale = 1)")
plt.title("La loi normale approche la distribution des moyennes")
plt.legend()
plt.show()
```

La courbe rouge est une approximation normale. L'histogramme dépend du hasard ; les moyennes possibles restent discrètes, même si elles sont nombreuses.

---

## Pourquoi les moyennes se resserrent-elles ?

Les moyennes restent proches de 3,5, mais leur dispersion diminue quand on augmente le nombre de dés.

Pour un dé équilibré, l'écart-type théorique d'un lancer vaut

$$
\sigma=\sqrt{\frac{35}{12}}\approx1{,}708.
$$

Pour la moyenne de $n$ lancers indépendants :

$$
\sigma_{\overline X}=\frac{\sigma}{\sqrt n}.
$$

| Nombre de dés $n$ | Écart-type des moyennes, environ |
|---:|---:|
| 1 | 1,708 |
| 2 | 1,208 |
| 5 | 0,764 |
| 10 | 0,540 |
| 30 | 0,312 |

Plus $n$ grandit, plus les moyennes sont concentrées autour de 3,5. Le nombre 30 n'est pas une frontière magique.

---

## Calculer la dispersion sans fonction statistique

Pour une liste de moyennes $x_1,\ldots,x_m$, on calcule d'abord leur moyenne, puis la moyenne des carrés des écarts à cette moyenne.

$$
\text{variance}=\frac{1}{m}\sum_{i=1}^{m}(x_i-\overline{x})^2
\qquad\text{et}\qquad
\text{écart-type}=\sqrt{\text{variance}}.
$$

```python
for n in [1, 2, 5, 10, 30]:
    moyennes = simuler_moyennes(n)
    moyenne = sum(moyennes) / len(moyennes)
    variance = sum((x - moyenne) ** 2 for x in moyennes) / len(moyennes)
    ecart_type = variance ** 0.5
    print(f"{n:2d} dés : moyenne={moyenne:.3f}, écart-type={ecart_type:.3f}")
```

Les valeurs simulées sont proches des valeurs théoriques, sans être identiques. Elles dépendent du hasard et du nombre d'expériences simulées.

---

## Le théorème central limite, en mots

Quand on calcule la moyenne d'un grand nombre de variables indépendantes, de même loi et de variance finie, la distribution de ces moyennes, une fois centrées et réduites, se rapproche d'une loi normale.

Dans notre expérience :

- la loi d'un dé est uniforme ;
- chaque expérience produit une moyenne de plusieurs dés ;
- les moyennes simulées prennent progressivement une forme en cloche.

Cette observation illustre le **théorème central limite**. La loi normale n'est pas la loi des faces : elle décrit ici la distribution des moyennes répétées.

---

## À vous · Lire les simulations

1. Pourquoi la moyenne théorique de deux dés vaut-elle 3,5 sans que chaque lancer de dé puisse donner 3,5 ?
2. Combien de couples donnent une moyenne de 3,5 ? Et une moyenne de 6 ?
3. Comparez les graphiques pour 5, 10 et 30 dés. Qu'est-ce qui change dans la forme ? Dans la dispersion ?
4. Avant d'exécuter le calcul, estimez l'écart-type des moyennes pour 10 dés à l'aide de $1{,}708/\sqrt{10}$.
5. Pourquoi ne peut-on pas dire que les résultats d'un lancer suivent une loi normale ?

<details><summary>Afficher une correction possible</summary>

1. 3,5 est la moyenne des six faces, pas un résultat possible d'un lancer.
2. Six couples donnent 3,5, contre un seul pour 6 : $(6,6)$.
3. La forme devient plus proche d'une cloche et se resserre autour de 3,5.
4. $1{,}708/\sqrt{10}\approx0{,}540$.
5. Un lancer ne prend que six valeurs équiprobables ; sa distribution est uniforme et discrète.

</details>

---

## De la moyenne connue à une moyenne inconnue

Jusqu'ici, nous connaissions la moyenne théorique du dé : 3,5. Imaginons maintenant que cette moyenne soit inconnue.

On lance le dé 30 fois et on observe une moyenne de 3,8. On voudrait estimer un intervalle de valeurs plausibles pour la moyenne réelle.

Cette nouvelle question mène aux **intervalles de confiance**. Elle demande d'étudier la variabilité des moyennes d'échantillons et les conditions du calcul ; elle ne consiste pas à affirmer que la moyenne inconnue a 95 % de chances de se trouver dans un intervalle déjà calculé.

---

## Cas d'usage · Mesurer pour décider

En contrôle qualité, on peut prélever plusieurs pièces dans une production et calculer la moyenne d'une mesure : diamètre, durée de vie ou consommation.

La distribution des moyennes aide à distinguer une variation due à l'échantillonnage d'un écart qui mérite une investigation. En data science, ce raisonnement sert aussi à comprendre l'incertitude d'une moyenne calculée sur un échantillon.

**À retenir :** des données individuelles quelconques peuvent produire des moyennes dont la distribution ressemble à une loi normale, sous certaines conditions.
