#  **TP : Analyse de données de température + mini API NumPy / FastAPI**

##  Objectifs du TP

Dans cet exercice, vous allez :

1. **simuler des données de température** sur 48 heures avec un cycle sinusoïdal idéal et un bruit gaussien. La loi normale est ici une hypothèse de simulation ; elle ne décrit pas à elle seule toute la variabilité météo réelle.
2. **nettoyer** ces données ;
3. **construire une matrice NumPy** représentant les mesures ;
4. **calculer la dérivée numérique** de la température ;
5. **analyser les zones où la température monte / descend** ;
6. **produire des graphiques** ;
7. **exposer vos résultats dans une mini API FastAPI**.

---

# **Fonctions NumPy autorisées pour ce TP**

Pour guider votre travail, vous êtes autorisés à utiliser **uniquement** les fonctions suivantes :

### Création de vecteurs et matrices

* `np.array`
* `np.arange`
* `np.linspace`
* `np.zeros`, `np.ones`
* `np.column_stack`
* `np.vstack`

### Calculs numériques

* Opérations vectorisées `+`, `-`, `*`, `/`, `**`
* `np.sin`, `np.cos`
* `np.abs`
* `np.diff`
* `np.mean`, `np.std`, `np.var`
* `np.random.seed`, `np.random.normal`
* Constante `np.pi`

###  Extraction / filtrage

* Masques booléens :
  `mask = (T < seuil)`
  `T[mask] = valeur`
* `np.where`
* `np.argmax`, `np.argmin` (indices des extrema)

### Affichage / informations

* `.shape`, `.size`
* `T[:10]` (slicing)
* `print`

### (pour le graphique) Matplotlib :

* `plt.plot`
* `plt.scatter`
* `plt.figure`
* `plt.subplot`
* `plt.grid`
* `plt.xlabel`, `plt.ylabel`, `plt.title`, `plt.legend`
* `plt.show`

Ces fonctions suffisent pour réaliser tout le TP.

---

#  **Génération des données**

Vous devez :

1. Créer un vecteur `t` contenant les heures de 0 à 47.

2. Exécuter le modèle simplifié suivant (temps en heures, températures en °C) :

```python
import numpy as np

t = np.arange(48, dtype=float)
np.random.seed(7)
noise = np.random.normal(loc=0.0, scale=0.5, size=t.size)
T_raw = 10 + 5 * np.sin((2*np.pi/24)*t) + noise
```

3. Afficher les 10 premières valeurs, puis tracer séparément le signal idéal, le bruit et `T_raw`.
4. Expliquer pourquoi $2\pi/24$ donne une période de 24 h. Remplacer 24 par 12 en gardant **le même tableau `noise`**, puis comparer les cycles, les amplitudes et les niveaux centraux.
5. Donner l'écart-type et la variance **théoriques** du bruit, avec leurs unités, puis comparer à `np.std(noise)` et `np.var(noise)` sur cet échantillon. Justifier les éventuelles différences.

**Réserve scientifique :** le sinus représente un cycle quotidien idéal, et le bruit simule des fluctuations aléatoires. Le cycle réel n'est pas parfaitement sinusoïdal. Dans cette formule, le maximum sans bruit est à 6 h ; pour le placer à 14 h, on pourrait utiliser $t-8$ dans le sinus. La phase, la période et l'amplitude jouent des rôles différents.

[Reprendre les questions et la correction de l'exercice 5](../../Slides/01_derivation.md).

> But : obtenir et comprendre une série temporelle simulée, sans la confondre avec des mesures météo réelles.

---

# **Nettoyage des données**

1. Identifier les valeurs aberrantes :

température < −5
température > 35
2. Créer un masque booléen.
3. Remplacer toute valeur aberrante par la moyenne de ses deux voisins immédiats.

> Le modèle peut ne produire aucune valeur hors de ces seuils : c'est un résultat valide. Pour tester le nettoyage, injecter volontairement une anomalie dans une copie de la série. Préciser le traitement des extrémités et des anomalies voisines avant de remplacer des valeurs.

---

# 🧭 **Étape 3 — Construction d'une matrice NumPy**

Créer une matrice ( M ) de taille 48 × 2 :

$$
M =
\begin{pmatrix}
t_0 & T_0 \
t_1 & T_1 \
\vdots & \vdots \
t_{47} & T_{47}
\end{pmatrix}
$$

Pour cela, utilisez **uniquement** :

* `np.column_stack((t, T))`

Puis afficher :

1. la forme `M.shape`,
1. les 5 premières lignes.

> *But : représenter proprement les données sous forme tabulaire.*

---

# **Dérivée numérique**

On approche la dérivée par un taux de variation entre deux mesures :

$$
T'(t_i) \approx \frac{T(t_{i+1}) - T(t_i)}{t_{i+1}-t_i}
$$

L'écart de temps vaut ici 1 h : la différence de températures donne numériquement un taux en °C/h. Sur un autre pas, il faut diviser par `np.diff(t)`. Les 48 mesures produisent 47 taux, associés aux intervalles entre mesures.

Vous devez :

1. Utiliser `np.diff(T) / np.diff(t)` pour obtenir ces taux ;
2. Créer un vecteur des heures correspondantes ;
3. Visualiser les 10 premières valeurs de la dérivée.

> *But : mesurer l'évolution locale de la température.*

---

# **Analyse**

À partir du vecteur `dT` :

1. Trouvez l'heure où la température monte **le plus vite**.
2. Trouvez l'heure où elle baisse **le plus vite**.
3. Déterminez les heures où la température est **quasi stable**, c'est-à-dire :

$$
|T'(t)| < 0.1
$$

> *But : interpréter les résultats physiques.*

---

#  **Graphiques**

Créer deux graphiques :

1. **Température nettoyée** vs temps
2. **Dérivée numérique** vs temps

Chaque graphique doit contenir :

1. un titre,
1. des axes nommés,
1. une grille,
1. une ou deux séries (selon le cas).

🎯 *But : visualiser proprement vos résultats.*

---

# **Mini API FastAPI**

Créer un fichier `main.py` avec trois endpoints :

---

###  **Endpoint 1 – `/temperature`**

Entrées : `t` (heure)

Retourner en JSON :

1. heure demandée,
1. température correspondante,
1. dérivée correspondante (approx).

---

### **Endpoint 2 – `/interval`**

Entrées : `t1`, `t2`

Retourner :

1. liste des températures entre t1 et t2,
1. moyenne,
1. minimum,
1. maximum.

---

### **Endpoint 3 – `/plot`**

Retourner un **PNG** généré avec Matplotlib :

1. soit la courbe des températures,
1. soit la courbe de dérivée,
1. soit les deux superposées (au choix).

> *But : relier l'analyse mathématique à un service REST simple.*

---

# **Questions de réflexion**

Ajouter dans votre rapport :

1. Pourquoi la dérivée numérique est-elle une **approximation** de la dérivée réelle ?
2. Pourquoi le bruit rend-il la dérivée plus irrégulière ?
3. Quelles limites a le nettoyage par moyenne locale ?
4. Comment améliorer l'analyse (ex : moyenne glissante) ?
5. Comment généraliser ce TP à des données météo réelles ?
6. Quel lien unit période, fréquence et pulsation ? Pourquoi une période de 12 h double-t-elle la fréquence du signal de 24 h ?
7. Pourquoi `scale=0.5` correspond-il à une variance de 0,25 °C² ? Pourquoi ce n'est pas une borne du bruit ?
8. Pourquoi simuler une série n'est-il pas déjà prédire ses valeurs futures ? Comment préserver l'ordre chronologique lors d'une future évaluation ?
