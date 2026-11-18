---
marp: true
theme: default
paginate: true
class: lead
---

# Découverte des réseaux de neurones

Des calculs simples pour comprendre comment un modèle classe des données.

[Voir la frise historique de l’intelligence artificielle](#34)

---

# Échauffement · Le produit scalaire d’un panier

Le **produit scalaire** de deux vecteurs de même dimension est le nombre obtenu en multipliant leurs coordonnées de même rang, puis en additionnant les produits. Pour deux vecteurs $a$ et $b$ à trois coordonnées, on écrit

$$
a\cdot b=a_1b_1+a_2b_2+a_3b_3.
$$

Dans une liste de courses, on associe à chaque produit sa quantité et son prix unitaire.

| Produit | Prix (€) | Quantité |
|:---|---:|---:|
| Sachet de pommes | 2 | 2 |
| Bouteille de lait | 1 | 1 |
| Pain | 3 | 1 |

On garde le même ordre dans les deux vecteurs. Pour les quantités $q=(2,1,1)$ et les prix $p=(2,1,3)$, le total vaut

$$
\begin{aligned}
q\cdot p &= 2\times 2+1\times 1+1\times 3\\
         &= 8\ \text{euros}.
\end{aligned}
$$

**À toi de jouer.** Garde l’ordre pommes, lait, pain et calcule le total de chaque panier.

1. Panier $(1,2,1)$.
2. Panier $(0,3,2)$.
3. Panier $(3,0,2)$. Un budget de 10 € suffit-il ?

<details>
<summary>Vérifier les trois calculs</summary>

1. $1\times 2+2\times 1+1\times 3=7$ €.
2. $0\times 2+3\times 1+2\times 3=9$ €.
3. $3\times 2+0\times 1+2\times 3=12$ €. Il manque 2 €.

</details>

Le neurone utilise le même type de calcul avec ses entrées et ses poids, puis ajoute un biais.

---

# Un parcours en trois étapes

**1 · Décider.** Calculer le score d'un neurone, comparer le seuil, ReLU et la sigmoïde, puis lire la droite qui sépare deux classes.

**2 · Apprendre.** Modifier les poids quand le neurone se trompe, puis observer ce qu'il peut et ne peut pas apprendre.

**3 · Regrouper les calculs.** Représenter plusieurs observations dans un tableau et utiliser de petites matrices avec NumPy.

Chaque étape part d'un calcul à la main, puis le vérifie dans un notebook. Nous utiliserons un petit jeu de données artificiel pour que les calculs restent lisibles.

Le chapitre s'appuie sur des additions, des multiplications et des tableaux NumPy. Aucune méthode de dérivation n'est nécessaire pour les activités.

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

# Le score peut passer par une fonction d'activation

Le neurone calcule d'abord un score $z$. Une **fonction d'activation** transforme ensuite ce score avant de produire la sortie.

Dans le perceptron que nous venons de voir, la fonction seuil transforme le score en une décision 0 ou 1. D'autres activations donnent une sortie différente. Nous allons en comparer deux, sans étudier leur apprentissage.

---

# ReLU · garder la partie positive

La fonction ReLU est définie par :

$$
\operatorname{ReLU}(z)=\max(0,z).
$$

Elle renvoie 0 si le score est négatif, et garde le score s'il est positif.

| Score $z$ | $-2$ | $0$ | $3$ |
|---:|---:|---:|---:|
| ReLU$(z)$ | $0$ | $0$ | $3$ |

ReLU ne donne pas directement une classe : elle produit une nouvelle valeur que d'autres neurones peuvent utiliser.

---

# Sigmoïde · une sortie entre 0 et 1

La sigmoïde transforme le score ainsi :

$$
\sigma(z)=\frac{1}{1+e^{-z}}.
$$

Quelques valeurs approchées :

| Score $z$ | $-2$ | $0$ | $2$ |
|---:|---:|---:|---:|
| Sigmoïde $\sigma(z)$ | $0{,}12$ | $0{,}50$ | $0{,}88$ |

Sa sortie reste entre 0 et 1. Pour une classification binaire, on peut comparer cette sortie à un seuil, par exemple 0,5. Ici, nous nous limitons au calcul et à l'interprétation des sorties.

---

# Observer les deux fonctions

ReLU coupe les scores négatifs à 0 et augmente ensuite en ligne droite. La sigmoïde évolue progressivement entre 0 et 1.

<svg class="interactive-demo-svg" viewBox="0 0 680 270" role="img" aria-label="Graphiques de ReLU et de la sigmoïde : ReLU vaut zéro pour les scores négatifs, la sigmoïde évolue entre zéro et un.">
  <text x="185" y="28" text-anchor="middle" class="demo-title">ReLU(z)</text>
  <path d="M55 210H320M185 220V48" class="demo-axis"/>
  <path d="M55 170H320M55 130H320M55 90H320M120 48V210M250 48V210" class="demo-grid"/>
  <path d="M65 210H185L300 65" fill="none" stroke="#d8894a" stroke-width="4" stroke-linecap="round"/>
  <text x="185" y="252" text-anchor="middle" class="demo-caption">Score z</text>
  <text x="32" y="126" text-anchor="middle" class="demo-caption" transform="rotate(-90 32 126)">Sortie</text>
  <text x="495" y="28" text-anchor="middle" class="demo-title">Sigmoïde σ(z)</text>
  <path d="M365 210H640M502 220V48" class="demo-axis"/>
  <path d="M365 170H640M365 130H640M365 90H640M435 48V210M570 48V210" class="demo-grid"/>
  <path d="M375 202C415 198 440 178 465 155S495 132 502 130S525 108 545 88S590 65 630 59" fill="none" stroke="#457b9d" stroke-width="4" stroke-linecap="round"/>
  <path d="M365 130H640" stroke="#d8894a" stroke-width="2" stroke-dasharray="7 6"/>
  <text x="502" y="252" text-anchor="middle" class="demo-caption">Score z · la ligne pointillée indique 0,5</text>
</svg>

Les deux activations transforment le même score de façons différentes. Dans nos exercices d'apprentissage, nous garderons la règle seuil, dont les sorties restent faciles à vérifier à la main.

---

# Exercice · Comparer seuil, ReLU et sigmoïde

On considère les scores $z=-2$, $z=0$ et $z=2$.

1. Calculer les trois sorties ReLU.
2. À l'aide du tableau précédent, donner les sorties de la sigmoïde.
3. Appliquer la règle seuil du perceptron : sortie 1 si $z\geq0$, sinon 0.
4. Pour chaque fonction, décrire en une phrase ce que sa sortie représente.

**Repère :** ce sont trois transformations du score. Dans ce cours, vous n'avez pas à calculer leurs dérivées ni à entraîner un réseau avec la sigmoïde.

---

# Exercice 1 · Calculer un score et prédire une classe

Un neurone reçoit $x_1=2$ et $x_2=1$. Ses poids valent $w_1=1$ et $w_2=-2$, et son biais vaut $b=1$.

1. Calculer le score $z$.
2. En déduire la classe prédite $\widehat y$.
3. Que devient le score si le biais passe de 1 à 0 ? La classe change-t-elle ?

**À faire à deux :** l'un effectue le calcul, l'autre vérifie chaque produit et le signe final.

---

# Une frontière sépare les deux classes

Avec deux caractéristiques et au moins un poids non nul, la frontière est la droite d'équation $w_1x_1+w_2x_2+b=0$. Elle contient les points dont le score vaut zéro.

Reprenons l'exercice 1 avec le biais initial $b=1$. Le score est $z=x_1-2x_2+1$. En posant $z=0$ et en isolant $x_2$, on obtient

$$
x_2=\frac{x_1+1}{2}.
$$

<svg class="discovery-boundary-svg" viewBox="0 0 364 262" style="display:block;width:100%;max-width:432px;height:auto;margin:8px auto 16px" role="img" aria-label="Repère gradué. La droite x₂ = (x₁ + 1) / 2 passe par (1, 1) et (3, 2). Le point (2, 1) est sous la droite en classe 1. Le point (2, 2) est au-dessus en classe 0.">
  <polygon points="45,31 301,31 301,63 45,191" fill="#faeee7"/>
  <polygon points="45,191 301,63 301,223 45,223" fill="#e5f1f5"/>
  <path d="M45 159H301 M45 95H301 M45 31H301 M109 31V223 M173 31V223 M237 31V223 M301 31V223" class="demo-grid"/>
  <path d="M45 24V223H319" class="demo-axis" fill="none"/>
  <line x1="45" y1="191" x2="301" y2="63" stroke="#a85532" stroke-width="2.5" stroke-dasharray="6 4"/>
  <circle cx="109" cy="159" r="3.5" fill="#a85532"/>
  <circle cx="237" cy="95" r="3.5" fill="#a85532"/>
  <rect x="168" y="90" width="10" height="10" rx="1.5" fill="#a44432"/>
  <circle cx="173" cy="159" r="5.5" fill="#32647e"/>
  <g fill="#203f38" font-family="system-ui, sans-serif" font-size="16">
    <g text-anchor="middle">
      <text x="45" y="17">x₂</text>
      <text x="38" y="246">0</text>
      <text x="109" y="246">1</text>
      <text x="173" y="246">2</text>
      <text x="237" y="246">3</text>
      <text x="301" y="246">4</text>
    </g>
    <g text-anchor="end">
      <text x="34" y="164">1</text>
      <text x="34" y="100">2</text>
      <text x="34" y="36">3</text>
    </g>
    <text x="326" y="228">x₁</text>
    <text x="307" y="68" fill="#813d2c">z = 0</text>
    <text x="60" y="55" fill="#813d2c">Classe 0 · z &lt; 0</text>
    <text x="169" y="205" fill="#285770">Classe 1 · z ≥ 0</text>
    <text x="185" y="100">(2, 2)</text>
    <text x="185" y="164">(2, 1)</text>
  </g>
</svg>

Le point $(2,1)$ de l'exercice a un score de $1$. Il est sous la droite, dans la classe 1. La règle $z\geq 0$ inclut aussi les points de la droite dans cette classe.

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

---

# Repères historiques de l’intelligence artificielle

<ol class="ai-history" role="list" aria-label="Onze repères chronologiques de l’intelligence artificielle">
  <li><time datetime="1943">1943</time><div>
    <strong>Un modèle mathématique du neurone</strong>
    <p>McCulloch et Pitts décrivent des neurones à seuil qui, reliés entre eux, réalisent des opérations logiques. <a href="https://doi.org/10.1007/BF02478259">Article original</a></p>
  </div></li>
  <li><time datetime="1950">1950</time><div>
    <strong>Le jeu de l’imitation</strong>
    <p>Alan Turing propose un jeu de conversation écrite pour évaluer si une machine peut imiter les réponses d’une personne. <a href="https://academic.oup.com/mind/article/LIX/236/433/986238">Article de Turing</a></p>
  </div></li>
  <li><time datetime="1956">1956</time><div>
    <strong>L’atelier de Dartmouth</strong>
    <p>Des chercheurs se réunissent autour d’un programme de recherche appelé « intelligence artificielle » dans leur proposition de 1955. <a href="https://www-formal.stanford.edu/jmc/slides/dartmouth/dartmouth/node1.html">Récit de John McCarthy</a></p>
  </div></li>
  <li><time datetime="1958">1958</time><div>
    <strong>Le perceptron</strong>
    <p>Frank Rosenblatt publie son modèle de perceptron, qui apprend à classer des exemples en ajustant des poids. <a href="https://pubmed.ncbi.nlm.nih.gov/13602029/">Article de Rosenblatt</a></p>
  </div></li>
  <li><time datetime="1976">1976</time><div>
    <strong>MYCIN et les systèmes experts</strong>
    <p>Edward Shortliffe présente MYCIN, un programme qui applique des règles d’experts pour assister des décisions médicales. <a href="https://www.sciencedirect.com/book/monograph/9780444001795/computer-based-medical-consultations-mycin">Monographie</a></p>
  </div></li>
  <li><time datetime="1986">1986</time><div>
    <strong>La rétropropagation</strong>
    <p>Rumelhart, Hinton et Williams décrivent comment ajuster les poids des couches intermédiaires à partir de l’erreur en sortie. <a href="https://doi.org/10.1038/323533a0">Article dans Nature</a></p>
  </div></li>
  <li><time datetime="1997">1997</time><div>
    <strong>Deep Blue aux échecs</strong>
    <p>Le système d’IBM remporte un match en six parties contre le champion du monde Garry Kasparov. <a href="https://www.ibm.com/history/deep-blue">Archives IBM</a></p>
  </div></li>
  <li><time datetime="2012">2012</time><div>
    <strong>AlexNet et la reconnaissance d’images</strong>
    <p>Un réseau convolutif profond entraîné sur GPU remporte le défi de classification ImageNet. <a href="https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c-Abstract.html">Article NeurIPS</a></p>
  </div></li>
  <li><time datetime="2016">2016</time><div>
    <strong>AlphaGo au jeu de go</strong>
    <p>Le programme de Google DeepMind bat le joueur professionnel Lee Sedol par quatre parties à une. <a href="https://deepmind.google/research/alphago/">Compte rendu de DeepMind</a></p>
  </div></li>
  <li><time datetime="2017">2017</time><div>
    <strong>Le Transformer</strong>
    <p>Vaswani et ses coauteurs proposent une architecture fondée sur l’attention et la testent sur des tâches de traduction. <a href="https://arxiv.org/abs/1706.03762">Article original</a></p>
  </div></li>
  <li><time datetime="2022-11-30">2022</time><div>
    <strong>ChatGPT et l’IA générative grand public</strong>
    <p>OpenAI ouvre au public l’accès à un assistant qui génère des réponses en langage naturel. <a href="https://openai.com/index/chatgpt/">Annonce de lancement</a></p>
  </div></li>
</ol>
