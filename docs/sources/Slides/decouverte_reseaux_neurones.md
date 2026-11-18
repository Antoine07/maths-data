---
marp: true
theme: default
paginate: true
class: lead
---

# Découverte des réseaux de neurones

Des calculs simples pour comprendre comment un modèle classe des données.

---

# Ce que nous allons construire

Un neurone reçoit quelques nombres, calcule un score et choisit une classe. Nous allons voir comment corriger ses poids lorsqu'il se trompe, puis comment plusieurs neurones peuvent travailler ensemble.

**À la fin du chapitre, tu sauras :**

- calculer le score d'un neurone à partir de ses entrées, ses poids et son biais ;
- appliquer une règle simple de correction ;
- reconnaître une limite d'un modèle linéaire ;
- lire une petite multiplication matricielle qui calcule plusieurs scores à la fois.

Nous utiliserons des additions, des multiplications, des tableaux NumPy et des dérivées simples. La dérivation en chaîne et la rétropropagation ne sont pas des prérequis ici.

---

# Un neurone calcule un score

On donne au neurone deux caractéristiques numériques, $x_1$ et $x_2$. Il leur associe des poids $w_1$ et $w_2$, puis ajoute un biais $b$ :

$$
z=w_1x_1+w_2x_2+b.
$$

Le score $z$ résume les entrées selon les poids choisis par le modèle. Une règle de décision transforme ensuite ce score en classe :

$$
\widehat y=\begin{cases}1 & \text{si } z\geq 0,\\ 0 & \text{si } z<0.\end{cases}
$$

Les poids disent quelles caractéristiques font monter ou baisser le score. Le biais déplace le seuil de décision.

---

# Exercice 1 · Calculer un score et prédire une classe

Un neurone reçoit $x_1=2$ et $x_2=1$. Ses poids valent $w_1=1$ et $w_2=-2$, et son biais vaut $b=1$.

1. Calculer le score $z$.
2. En déduire la classe prédite $\widehat y$.
3. Que devient le score si le biais passe de 1 à 0 ? La classe change-t-elle ?

**À faire à deux :** l'un effectue le calcul, l'autre vérifie chaque produit et le signe final.

---

# Une frontière sépare les deux classes

La décision change lorsque le score vaut zéro. Avec deux caractéristiques, l'équation

$$
w_1x_1+w_2x_2+b=0
$$

décrit une droite. Le neurone classe les points situés de part et d'autre de cette frontière.

<svg class="interactive-demo-svg discovery-boundary-svg" viewBox="0 0 520 350" role="img" aria-label="Deux groupes de points sont séparés par la droite x2 égale x1.">
  <text x="260" y="26" text-anchor="middle" class="demo-title">Deux caractéristiques, une droite de décision</text>
  <path d="M75 290H455M75 290V55" class="demo-axis"/>
  <path d="M75 230H455M75 170H455M75 110H455M150 55V290M225 55V290M300 55V290M375 55V290" class="demo-grid"/>
  <path d="M105 270L405 70" stroke="#d8894a" stroke-width="4" stroke-dasharray="8 6"/>
  <g fill="#457b9d"><circle cx="225" cy="270" r="9"/><circle cx="300" cy="210" r="9"/></g>
  <g fill="#e66f51"><rect x="137" y="137" width="18" height="18" rx="3"/><rect x="212" y="77" width="18" height="18" rx="3"/></g>
  <text x="260" y="324" text-anchor="middle" class="demo-caption">Caractéristique x₁</text>
  <text x="43" y="172" text-anchor="middle" class="demo-caption" transform="rotate(-90 43 172)">Caractéristique x₂</text>
  <text x="325" y="95" class="demo-caption">Frontière : x₂ = x₁</text>
</svg>

Sur ce dessin, une droite suffit à séparer les deux groupes. Un neurone seul ne peut produire qu'une frontière de ce type.

---

# Comment le perceptron apprend-il ?

On compare la classe prédite $\widehat y$ à la classe attendue $y$. Si le neurone se trompe, on modifie légèrement les poids dans le sens de l'exemple :

$$
\mathbf w\leftarrow\mathbf w+\eta(y-\widehat y)\mathbf x,
\qquad b\leftarrow b+\eta(y-\widehat y).
$$

Ici, $\eta$ est un petit nombre positif appelé **pas d'apprentissage**. La formule ne demande que des additions et des multiplications.

**Exemple guidé.** On prend $\mathbf x=(1,0)$, $y=0$, $\widehat y=1$, $\eta=0{,}2$, $\mathbf w=(0{,}2,0{,}1)$ et $b=-0{,}1$. Le facteur $(y-\widehat y)$ vaut $-1$ : le poids associé à la première caractéristique et le biais diminuent.

---

# Exercice 2 · Corriger une prédiction

Reprends l'exemple du neurone qui prédit 1 alors que la classe attendue est 0.

1. Calcule les nouveaux poids et le nouveau biais après une correction.
2. Recalcule le score du même exemple avec ces nouveaux paramètres.
3. La prédiction a-t-elle changé ? Explique le rôle du pas $\eta$.

**Pratique NumPy :** représente les poids par un tableau et réalise cette mise à jour sans boucle.

```python
import numpy as np

x = np.array([1.0, 0.0])
y = 0
prediction = 1
eta = 0.2
w = np.array([0.2, 0.1])
b = -0.1

# À compléter : mettre à jour w et b
```

---

# Exercice 3 · Entraîner un petit perceptron

On veut distinguer deux groupes à partir de deux caractéristiques. Les lignes de `X` sont les observations ; `y` contient leur classe attendue.

```python
import numpy as np

X = np.array([
    [1.0, 0.0],
    [2.0, 1.0],
    [0.0, 2.0],
    [1.0, 3.0]
])
y = np.array([0, 0, 1, 1])
```

1. Avec $\mathbf w=(-1,1)$ et $b=0$, calcule les quatre scores et les classes prédites.
2. Complète une fonction `predict(X, w, b)` qui renvoie toutes les prédictions en une opération NumPy.
3. En partant de poids nuls, applique la règle de correction pendant plusieurs passages sur les observations. Compte les erreurs à chaque passage.
4. Trace ou affiche les prédictions avant et après l'apprentissage. Que remarque-t-on ?

**Indice de code :** `X @ w` calcule les produits scalaires de toutes les lignes de `X` avec le vecteur `w`.

---

# Une limite : le problème XOR

Voici quatre exemples et leur classe :

| $x_1$ | $x_2$ | Classe XOR |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

1. Place ces quatre points dans un repère et colore-les selon leur classe.
2. Peut-on tracer une seule droite qui sépare les deux classes ?
3. Qu'est-ce que cela nous apprend sur les possibilités d'un neurone seul ?

Une couche de neurones supplémentaire peut d'abord fabriquer de nouvelles caractéristiques, puis une autre unité peut prendre une décision à partir de celles-ci.

---

# Une couche cachée · Un exemple à calculer

On définit la fonction seuil $s(z)$ : elle vaut 1 si $z\geq0$, et 0 sinon. Deux petits neurones produisent de nouvelles valeurs :

$$
h_1=s(x_1+x_2-0{,}5),\qquad h_2=s(x_1+x_2-1{,}5).
$$

Un neurone de sortie calcule ensuite :

$$
\widehat y=s(h_1-2h_2-0{,}5).
$$

**À vous :** compléter le tableau pour les quatre lignes XOR. Pour chaque ligne, calculer d'abord $h_1$ et $h_2$, puis $\widehat y$. Aucun calcul de dérivée n'est nécessaire.

La couche cachée crée une représentation intermédiaire. Le réseau combine ces valeurs pour résoudre une tâche qu'une seule droite ne pouvait pas séparer.

---

# Des scores à la matrice

Avec plusieurs observations et plusieurs neurones, répéter le calcul une ligne à la fois devient répétitif. Les matrices regroupent ces calculs.

On range les observations dans $X$ : une ligne par observation, une colonne par caractéristique. On range les poids dans $W$ : une ligne par neurone, une colonne par caractéristique. Les scores de tous les neurones se calculent alors ainsi :

$$
Z=XW^\top+\mathbf b.
$$

Le biais $\mathbf b$ contient un nombre par neurone ; NumPy le réutilise pour chaque ligne. La multiplication matricielle n'est qu'une façon compacte de faire plusieurs produits scalaires.

---

# Exercice 4 · Calculer avec de petites matrices

On donne :

$$
X=\begin{bmatrix}1&2\\3&1\end{bmatrix},\qquad
W=\begin{bmatrix}2&-1\\1&1\end{bmatrix},\qquad
\mathbf b=(-1,-3).
$$

1. Combien y a-t-il d'observations et de caractéristiques dans $X$ ? Combien y a-t-il de neurones dans $W$ ?
2. Calculer à la main $XW^\top+\mathbf b$. Commencer par les produits scalaires de chaque ligne de $X$ avec chaque ligne de $W$.
3. Vérifier avec NumPy :

```python
import numpy as np

X = np.array([[1, 2], [3, 1]])
W = np.array([[2, -1], [1, 1]])
b = np.array([-1, -3])
Z = X @ W.T + b
print(Z)
```

4. Avec la même règle de seuil, transformer les scores en sorties 0 ou 1.

---

# Ce que nous savons faire, et la suite

Nous savons calculer les scores d'un neurone, corriger une prédiction, constater la limite d'une frontière linéaire et regrouper plusieurs calculs avec des matrices.

La règle du perceptron apprend sans dériver une fonction de perte. Les méthodes plus avancées ajustent les poids à l'aide de dérivées et de gradients. Pour les comprendre et coder la rétropropagation, il faudra d'abord travailler la dérivation en chaîne et les dérivées de plusieurs variables.

**À retenir :** un réseau de neurones reste une suite de calculs simples. Les poids déterminent ces calculs ; les données et une règle d'apprentissage les font évoluer.
