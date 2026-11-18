---
marp: true
theme: default
paginate: true
class: lead
---

# Coder un perceptron

Préparer des données, coder un classifieur binaire et observer ses corrections.

[Voir les repères historiques de l’intelligence artificielle](#2)

---

# Repères historiques de l’intelligence artificielle

Suivez la frise chronologique de gauche à droite. Faites-la défiler horizontalement pour parcourir tous les repères.

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

---

# Le perceptron en un coup d’œil

Un perceptron transforme des entrées en une décision : il pondère les caractéristiques, additionne leurs contributions avec un biais, puis compare le score à un seuil. Il résume les opérations que nous allons coder, une observation à la fois.

<svg class="perceptron-intro-svg" viewBox="0 0 960 300" style="display:block;width:100%;max-width:900px;height:auto;margin:12px auto" role="img" aria-label="Schéma d'un perceptron à deux entrées : x1 vaut 2 et x2 vaut 1 ; les poids valent 1 et moins 2 ; le biais vaut 1 ; le score vaut 1 ; le seuil prédit la classe 1.">
  <defs>
    <marker id="perceptron-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#66776f"/></marker>
  </defs>
  <rect x="8" y="8" width="944" height="284" rx="18" fill="#f7faf7" stroke="#d8e3dc"/>
  <g font-family="system-ui, sans-serif" fill="#263b35">
    <text x="112" y="48" text-anchor="middle" font-size="15" font-weight="700">Entrées</text>
    <circle cx="112" cy="103" r="29" fill="#e5f1f5" stroke="#7ea6b5" stroke-width="2"/><text x="112" y="109" text-anchor="middle" font-size="17" font-weight="700">x₁=2</text>
    <circle cx="112" cy="190" r="29" fill="#e5f1f5" stroke="#7ea6b5" stroke-width="2"/><text x="112" y="196" text-anchor="middle" font-size="17" font-weight="700">x₂=1</text>
    <text x="286" y="48" text-anchor="middle" font-size="15" font-weight="700">Poids et produits</text>
    <rect x="224" y="78" width="124" height="50" rx="12" fill="#fff" stroke="#b8c9bf"/><text x="286" y="99" text-anchor="middle" font-size="14">w₁=1</text><text x="286" y="118" text-anchor="middle" font-size="13" fill="#5c6d64">1 × 2 = 2</text>
    <rect x="224" y="165" width="124" height="50" rx="12" fill="#fff" stroke="#b8c9bf"/><text x="286" y="186" text-anchor="middle" font-size="14">w₂=−2</text><text x="286" y="205" text-anchor="middle" font-size="13" fill="#5c6d64">−2 × 1 = −2</text>
    <text x="475" y="48" text-anchor="middle" font-size="15" font-weight="700">Somme + biais</text>
    <rect x="408" y="90" width="134" height="105" rx="18" fill="#fff1e8" stroke="#d9956a" stroke-width="2"/><text x="475" y="128" text-anchor="middle" font-size="24" font-weight="700">Σ + b</text><text x="475" y="160" text-anchor="middle" font-size="14">2 − 2 + 1</text>
    <text x="638" y="48" text-anchor="middle" font-size="15" font-weight="700">Score</text>
    <rect x="590" y="111" width="96" height="62" rx="15" fill="#eaf3ed" stroke="#81a28e" stroke-width="2"/><text x="638" y="150" text-anchor="middle" font-size="22" font-weight="700">z=1</text>
    <text x="790" y="48" text-anchor="middle" font-size="15" font-weight="700">Seuil</text>
    <rect x="733" y="111" width="114" height="62" rx="15" fill="#fff" stroke="#b8c9bf" stroke-width="2"/><text x="790" y="150" text-anchor="middle" font-size="18" font-weight="700">z ≥ 0 ?</text>
    <circle cx="900" cy="142" r="31" fill="#e5f1f5" stroke="#7ea6b5" stroke-width="2"/><text x="900" y="148" text-anchor="middle" font-size="16" font-weight="700">classe 1</text>
    <text x="480" y="260" text-anchor="middle" font-size="14" fill="#52645b">Même calcul qu’un produit scalaire, puis une règle de décision.</text>
  </g>
  <g fill="none" stroke="#66776f" stroke-width="2.2" marker-end="url(#perceptron-arrow)">
    <path d="M141 103 H213"/><path d="M141 190 H213"/>
    <path d="M348 103 C380 103 382 120 401 130"/><path d="M348 190 C380 190 382 166 401 155"/>
    <path d="M542 142 H582"/><path d="M686 142 H725"/><path d="M847 142 H861"/>
  </g>
</svg>

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


Le neurone utilise le même type de calcul avec ses entrées et ses poids, puis ajoute un biais.

---

# Objectif · Coder un perceptron

À partir d’un jeu de données sur les manchots, vous allez préparer les caractéristiques et la cible, coder le calcul d’un score, puis écrire la boucle qui ajuste les poids lorsqu’une prédiction est fausse.

Le fil de travail est simple : **données → score → classe prédite → comparaison à la classe réelle → correction des poids**.

À la fin, vous pourrez expliquer ce que fait le programme pour chaque manchot et représenter l’évolution des poids pendant l’apprentissage.

---

# Un neurone calcule un score

On donne au neurone deux caractéristiques numériques, $x_1$ et $x_2$. Il leur associe des poids $w_1$ et $w_2$, puis ajoute un biais $b$ :

$$
z=w_1x_1+w_2x_2+b.
$$

Le score $z$ résume les entrées selon les poids choisis par le modèle. Une règle de décision transforme ensuite ce score en classe.

En NumPy, l'opérateur `@` calcule un produit matriciel. Quand ses deux côtés sont des vecteurs de même longueur, il calcule leur produit scalaire : il multiplie les coordonnées correspondantes, puis additionne les produits.

```python
import numpy as np

x = np.array([2, 1])
poids = np.array([1, -2])
produit = x @ poids  # 2 × 1 + 1 × (-2) = 0
score = produit + 1  # le biais vaut 1, donc le score vaut 1
```

Dans notre perceptron, le score s'écrit donc `x @ poids + biais`. Pour une matrice `X` contenant plusieurs observations, `X @ poids` calcule en une fois un score par ligne.

On note $\widehat y$, prononcé **« y chapeau »**, la classe que le modèle prédit. Le chapeau indique ici une valeur estimée par le modèle. La lettre $y$ sans chapeau désigne la classe attendue, connue dans les données. La prédiction peut être correcte ($\widehat y=y$) ou erronée ($\widehat y\ne y$).

La règle de décision est :

$$
\widehat y=\begin{cases}1 & \text{si } z\geq 0,\\ 0 & \text{si } z<0.\end{cases}
$$

Cette règle porte le nom de **fonction escalier** : elle transforme un score en classe 0 ou 1.

```python
def fonction_escalier(score):
    return int(score >= 0)
```

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

Dans un repère, une droite s'écrit souvent $y=ax+b$. Ici, les deux axes représentent les caractéristiques $x_1$ et $x_2$ : on écrit donc plutôt $x_2=ax_1+c$. Cette droite partage le plan en deux demi-plans. Le signe du score indique de quel côté se trouve un point et donc quelle classe le perceptron prédit.

Avec deux caractéristiques, la frontière vérifie $w_1x_1+w_2x_2+b=0$ (si $w_2\neq0$, on peut isoler $x_2$). Elle contient les points dont le score vaut zéro.

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

# Préparer les données avant la classification

Avant de demander au perceptron de classer des observations, il faut transformer le tableau en données numériques bien définies. [Téléchargez le fichier `penguins.csv`](data/penguins.csv) et placez-le dans le dossier du notebook.

```python
import pandas as pd

df = pd.read_csv("penguins.csv")
df.head()
```

On conserve les mesures numériques (`bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`), la colonne `sex` et la colonne `species`. `species` servira à reconnaître la classe : elle ne doit donc pas être utilisée comme une caractéristique d'entrée.

Le fichier contient trois espèces. Pour ce premier perceptron, choisissez-en deux seulement : sa sortie est une décision binaire, codée 0 ou 1.

**À vous de préparer le tableau :**

1. Avec `df.dtypes` et `df.isna().sum()`, repérer les types de colonnes et les valeurs manquantes.
2. Garder deux espèces et décider comment traiter les lignes où une mesure ou `sex` manque.
3. Choisir un encodage cohérent en 0/1 pour les deux espèces. Cette colonne formera la cible `y`.
4. Choisir également un encodage 0/1 pour `sex`, qui sera une caractéristique d'entrée.
5. Construire `X` avec les mesures numériques et `sex`, puis vérifier que `X` ne contient que des nombres et que `y` ne contient que 0 et 1.

Vous pouvez choisir quelle espèce reçoit 0 ou 1 : l'essentiel est de garder la même convention dans tout le jeu de données. Les caractéristiques et la cible doivent rester séparées.

```python
mesures = [
    "bill_length_mm", "bill_depth_mm",
    "flipper_length_mm", "body_mass_g"
]

# À compléter : choisir deux espèces, traiter les valeurs manquantes,
# encoder species et sex, puis construire X et y.
```

**Question de vérification :** pourquoi la colonne `species` ne doit-elle pas rester dans `X` une fois que vous l'avez transformée en cible `y` ?

---

# Comment le perceptron apprend-il ?

Dans les données, $y$ est la classe attendue. $\widehat y$, prononcé « y chapeau », est la classe prédite par le perceptron. On compare les deux ; si elles diffèrent, on modifie légèrement les poids dans le sens de l'exemple :

$$
\mathbf w\leftarrow\mathbf w+\eta(y-\widehat y)\mathbf x,
\qquad b\leftarrow b+\eta(y-\widehat y).
$$

Ici, $\eta$ est un petit nombre positif appelé **pas d'apprentissage**. La formule ne demande que des additions et des multiplications.

La différence $y-\widehat y$ indique le sens de la correction. Par exemple, si la classe attendue est $y=0$ mais que le modèle prédit $\widehat y=1$, alors $y-\widehat y=0-1=-1$.

- Si la prédiction est juste, $y=\widehat y$ et la différence vaut $0$ : les paramètres ne changent pas.
- Si la vraie classe vaut $1$ mais que le modèle prédit $0$, la différence vaut $+1$ : le score de cet exemple est poussé vers le haut.
- Si la vraie classe vaut $0$ mais que le modèle prédit $1$, la différence vaut $-1$ : le score est poussé vers le bas.

Le vecteur $\mathbf{x}$ répartit cette correction entre les poids, tandis que le biais reçoit la correction directement. C'est une règle de mise à jour simple du perceptron, pas un calcul de dérivée.

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

# Entraîner le perceptron, manchot par manchot

Vous avez maintenant les caractéristiques `X` et la classe attendue `y`. Le perceptron va parcourir les lignes une par une. Pour chaque manchot, il calcule un score, prédit une espèce, compare sa prédiction à la cible, puis corrige ses paramètres en cas d'erreur.

Le traitement d'un manchot correspond à **une itération** : le modèle calcule, compare et, si nécessaire, met à jour ses poids. Une **époque** est un passage complet sur toutes les lignes. Avec 10 époques, chaque manchot est donc traité 10 fois.

## Mettre les mesures sur des échelles comparables

Les longueurs sont exprimées en millimètres, la masse en grammes et `sex` vaut 0 ou 1. Sans précaution, les valeurs de masse pèseraient beaucoup plus dans les calculs. Centrez-réduisez les quatre mesures numériques ; gardez `sex` encodé en 0/1.

```python
# X contient les quatre mesures numériques puis sex.
# Indice : mean(axis=0), std(axis=0), puis (valeur - moyenne) / écart-type.
moyennes = ...
ecarts_types = ...
X[:, :4] = ...
```

Pour cette activité, le pas d'apprentissage est fixé à **$\eta=0{,}1$**. C'est un hyperparamètre : on le choisit avant l'entraînement et on le garde identique pour tous les manchots et toutes les époques. Il n'est pas appris par le perceptron.

## Écrire l'algorithme dans `res.py`

Téléchargez le [squelette de `res.py`](data/res.py), placez-le à côté du notebook, puis complétez la mise à jour des poids et du biais. Le fichier contient la fonction escalier et le parcours des données.

Pour chaque ligne `i`, l'algorithme suit toujours le même ordre : calculer le score, appliquer la fonction escalier, comparer la classe prédite à `y[i]`, puis corriger les paramètres si elles diffèrent.

```python
from res import entrainer, predire

# Le pas reste fixé à 0.1 ; faire 10 passages sur les données.
poids, biais, historique, erreurs_par_epoque = entrainer(
    X, y, eta=0.1, nb_epoques=10
)
```

**À observer et expliquer :**

1. Pour les cinq premiers manchots, repérer le score, la classe attendue, la classe prédite et les poids après le passage.
2. Quand les poids changent-ils ? Que se passe-t-il quand la prédiction est correcte ?
3. Comparer le nombre d'erreurs d'une époque à l'autre. Les poids restent-ils fixes ou évoluent-ils encore ?
4. Expliquer le rôle de $\eta$ : que changerait un pas plus grand ou plus petit ? Pour cette expérience, ne modifiez pas sa valeur pendant l'entraînement.

La boucle de `res.py` applique bien ces étapes à **chaque** manchot. Pour comprendre le mécanisme, affichez le score, la cible, la prédiction et les poids après correction pour les cinq premiers exemples de la première époque. Le perceptron apprend à partir de `X` et `y` : la colonne `species` ne doit jamais être ajoutée aux caractéristiques `X`.

Pour voir l'évolution des paramètres, représentez chaque colonne de `historique` avec `plt.plot`. L'axe horizontal correspond au numéro d'itération (une observation traitée) ; chaque courbe représente un poids. Utilisez `plt.legend()` pour distinguer les poids. Observez aussi le biais, qui est suivi séparément. Comparez enfin le nombre d'erreurs après chaque époque.
