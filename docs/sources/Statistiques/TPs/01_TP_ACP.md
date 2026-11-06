# **Exercice – Analyse de performance sportive par ACP**

On étudie un groupe d’athlètes évalués selon quatre critères :

1. **Vitesse** (km/h)
2. **Force** (kg soulevés)
3. **Endurance** (score sur 100)
4. **Agilité** (score sur 100)

Les données suivantes décrivent 10 athlètes :

```python
import numpy as np

X = np.array([
    [29, 118, 45, 72],
    [27, 110, 40, 65],
    [31, 125, 48, 78],
    [26, 105, 37, 63],
    [30, 120, 46, 74],
    [28, 115, 44, 70],
    [32, 130, 50, 80],
    [25, 100, 35, 60],
    [27, 108, 39, 66],
    [29, 117, 42, 68]
], dtype=float)
```

---

# **Travail demandé**

## **1. Préparation des données**

1. Centrez et réduisez la matrice `X`.
2. Expliquez en une phrase pourquoi cette étape est indispensable en ACP.

---

## **2. ACP : extraction des axes principaux**

1. Calculez la matrice de covariance des données standardisées.
2. Calculez les **valeurs propres** et **vecteurs propres**.
3. Classez les axes principaux par importance décroissante.

**Questions :**

* Que représente la valeur propre associée à PC1 ?
* Que peut-on dire si PC1 explique plus de 80 % de la variance totale ?

---

## **3. Projection des individus**

1. Projetez `X` sur PC1 et PC2.
2. Tracez le nuage des individus dans le plan PC1–PC2.

**Questions :**

* Quelles sont les deux performances les plus corrélées entre elles ?
* Les athlètes semblent-ils former des groupes ?

---

## **4. Cercle de corrélation**

1. Calculez les coordonnées des 4 variables dans le cercle de corrélation.
2. Tracez le cercle complet (unit circle + flèches).

**Questions d’interprétation :**

* Quelles variables sont **fortement corrélées** ?
* Quelles variables contribuent le plus à PC1 ?
* Une variable s’écarte-t-elle des autres dans sa direction ? Que signifie cela ?

---

## **5. Analyse finale (2–3 phrases)**

Rédigez une conclusion décrivant :

* l'information principale révélée par l’ACP,
* le type d’athlètes mis en évidence (par exemple : explosifs, endurants…),
* comment le cercle de corrélation aide à interpréter les axes.
