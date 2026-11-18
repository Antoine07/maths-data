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

Le chapitre s'appuie sur des additions, des multiplications et des tableaux NumPy. Aucune méthode de dérivation n'est nécessaire pour les activités.

---

# Un parcours en trois étapes

**1 · Décider.** Comprendre le score d'un neurone et la droite qui sépare deux classes.

**2 · Apprendre.** Modifier les poids quand le neurone se trompe, puis observer ce qu'il peut et ne peut pas apprendre.

**3 · Regrouper les calculs.** Représenter plusieurs observations dans un tableau et utiliser de petites matrices avec NumPy.

Chaque étape part d'un calcul à la main, puis le vérifie dans un notebook. Nous utiliserons un petit jeu de données artificiel pour que les calculs restent lisibles.

---

# Étape 1 · Le neurone comme classifieur

Nous commençons par deux caractéristiques et deux classes. Le but est de comprendre chaque décision avant de demander au programme de la répéter sur beaucoup d'observations.

À la fin de cette étape, vous saurez calculer un score, lire son signe et représenter la frontière entre les deux classes.

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

# Lire le rôle des poids

Reprenons le score :

$$
z=w_1x_1+w_2x_2+b.
$$

- Si un poids est positif, augmenter la caractéristique correspondante augmente le score.
- Si un poids est négatif, l'augmenter diminue le score.
- Le biais $b$ déplace la frontière sans changer son orientation.

Ces effets dépendent de l'échelle des caractéristiques. Pour l'instant, nous choisissons de petits nombres faciles à comparer.

---

# Exercice · Prévoir avant de coder

Un neurone utilise $z=-x_1+x_2$ et prédit 1 lorsque $z\geq0$.

1. Calculer le score et la classe pour $(1,0)$, $(0,2)$ et $(3,3)$.
2. Placer ces points dans un repère et tracer la frontière $z=0$.
3. Indiquer de quel côté se trouvent les points prédits dans la classe 1.
4. Vérifier les trois prédictions avec une courte fonction Python.

L'objectif est de relier les calculs, la droite et les décisions du code.

---

# Étape 2 · Le perceptron apprend par corrections

Le neurone commence avec des poids choisis. Il lit les exemples un par un. Quand sa prédiction est fausse, la règle de Rosenblatt déplace ses poids dans le sens qui corrige cette erreur.

Nous suivons les changements des poids et le nombre d'erreurs. Nous ne cherchons pas encore à dériver une fonction d'erreur.

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

# Une correction, pas à pas

Dans l'exemple précédent, le facteur de correction vaut :

$$
\eta(y-\widehat y)=0{,}2(0-1)=-0{,}2.
$$

On applique ce facteur à chaque composante de $\mathbf x=(1,0)$ :

$$
\mathbf w_{nouveau}=(0{,}2,0{,}1)-0{,}2(1,0)=(0,0{,}1),
\qquad b_{nouveau}=-0{,}1-0{,}2=-0{,}3.
$$

Pour cette observation, le nouveau score est $-0{,}3$. La classe prédite devient 0. On vient de corriger cet exemple ; il faudra vérifier les autres exemples avant de conclure que le modèle est prêt.

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

# La boucle d'apprentissage

Voici les étapes à traduire en Python :

1. Initialiser les poids et le biais.
2. Parcourir les observations.
3. Calculer un score et une prédiction.
4. Si la prédiction est incorrecte, corriger les poids et le biais.
5. À la fin d'un passage complet, compter les erreurs.
6. Recommencer quelques passages et observer ce qui change.

Un passage complet sur les exemples s'appelle une **époque**. Le nombre d'époques est un réglage choisi avant l'exécution.

---

# TP · Compléter et observer l'apprentissage

Dans le notebook, complétez d'abord la fonction de prédiction, puis la boucle d'apprentissage.

```python
def predict_one(x, w, b):
    score = x @ w + b
    return int(score >= 0)

# À compléter : initialiser w et b, parcourir X et y,
# corriger les paramètres en cas d'erreur,
# puis mémoriser le nombre d'erreurs de chaque époque.
```

Comparez les erreurs avant et après chaque époque. Tracez ensuite la frontière avec les poids finaux. Les fonctions de tracé sont fournies ; concentrez-vous sur la logique d'apprentissage.

---

# Interpréter le résultat

Quand le nombre d'erreurs atteint zéro sur ces exemples, le perceptron a appris à les séparer. Cela ne prouve pas qu'il saura classer toutes les observations possibles : il a seulement réussi sur les exemples étudiés.

Si les classes se chevauchent ou ne peuvent pas être séparées par une droite, les erreurs peuvent persister. Il faut alors comprendre la limite du modèle au lieu d'ajouter des corrections sans fin.

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

# Étape 3 · Calculer plusieurs scores avec des matrices

Jusqu'ici, nous avons calculé les scores observation par observation. Les tableaux NumPy permettent de regrouper les observations ; les matrices regroupent aussi les poids de plusieurs neurones.

Nous allons seulement lire et calculer de petits produits. Une ligne représente une observation, et une colonne représente une caractéristique ou un neurone selon le tableau.

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

# Lire les dimensions avant de calculer

Si $X$ contient $m$ observations et $d$ caractéristiques, sa forme est $(m,d)$. Si le modèle contient $r$ neurones, $W$ a la forme $(r,d)$.

$$
X:(m,d),\qquad W^\top:(d,r),\qquad XW^\top:(m,r).
$$

Le résultat contient donc $m$ lignes et $r$ colonnes : un score par observation et par neurone. Cette vérification des dimensions aide à repérer une transposition oubliée.

---

# Un calcul matriciel, ligne par ligne

Prenons $X=\begin{bmatrix}1&2\\3&1\end{bmatrix}$ et $W=\begin{bmatrix}2&-1\\1&1\end{bmatrix}$.

La première observation donne les scores $1\times2+2\times(-1)=0$ et $1\times1+2\times1=3$.

La seconde donne $3\times2+1\times(-1)=5$ et $3\times1+1\times1=4$.

Ainsi, $XW^\top=\begin{bmatrix}0&3\\5&4\end{bmatrix}$. La multiplication matricielle rassemble simplement ces quatre produits scalaires.

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

# Vérifier les formes dans NumPy

Avant de calculer, affichez les formes :

```python
print(X.shape)       # observations × caractéristiques
print(W.shape)       # neurones × caractéristiques
print(W.T.shape)     # caractéristiques × neurones
print((X @ W.T).shape)
```

Ajoutez ensuite le biais et vérifiez qu'il existe une valeur par neurone. Pour chaque ligne de `X`, la règle de seuil transforme les scores en sorties 0 ou 1.

---

# Mini-défi · Comparer deux façons de calculer

À partir des mêmes petits tableaux :

1. Calculer les scores avec une boucle sur les lignes de `X`.
2. Calculer les mêmes scores avec `X @ W.T`.
3. Afficher les deux résultats et vérifier qu'ils sont égaux.
4. Compter le nombre de multiplications et d'additions effectuées dans les deux écritures.

Le but n'est pas de mesurer des temps sur un exemple minuscule. Il s'agit de comprendre que la notation matricielle rassemble les calculs et se généralise à de nombreux exemples.

---

# Pour aller un peu plus loin · XOR avec des poids choisis

Les deux neurones cachés proposés plus tôt transforment les entrées en deux nouvelles valeurs $h_1$ et $h_2$. Le neurone de sortie combine ces valeurs pour retrouver la classe XOR.

Complétez la table à la main, puis vérifiez avec NumPy. Les poids sont fournis : il n'est pas demandé de les apprendre. Cet exemple montre ce qu'un petit réseau peut calculer, sans expliquer encore comment entraîner toutes ses couches.

---

# Ce que nous savons faire, et la suite

Nous savons calculer les scores d'un neurone, corriger une prédiction, constater la limite d'une frontière linéaire et regrouper plusieurs calculs avec des matrices.

La règle du perceptron apprend en corrigeant les erreurs observées. D'autres méthodes d'apprentissage utilisent des outils mathématiques supplémentaires ; elles feront l'objet d'un cours ultérieur.

**À retenir :** un réseau de neurones reste une suite de calculs simples. Les poids déterminent ces calculs ; les données et une règle d'apprentissage les font évoluer.
