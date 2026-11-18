---
marp: true
theme: default
paginate: true
class: lead
---

# Découverte des réseaux de neurones

Des calculs simples pour comprendre comment un modèle classe des données.

[Voir la frise historique de l’intelligence artificielle](#2)


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

---

# Le perceptron en un coup d’œil

Un perceptron transforme des entrées en une décision : il pondère les caractéristiques, additionne leurs contributions avec un biais, puis compare le score à un seuil. Le schéma reprend les nombres de l’exercice de la slide suivante.

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

Le score $z$ résume les entrées selon les poids choisis par le modèle. Une règle de décision transforme ensuite ce score en classe.

On note $\widehat y$, prononcé **« y chapeau »**, la classe que le modèle prédit. Le chapeau indique ici une valeur estimée par le modèle. La lettre $y$ sans chapeau désigne la classe attendue, connue dans les données. La prédiction peut être correcte ($\widehat y=y$) ou erronée ($\widehat y\ne y$).

La règle de décision est :

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

# Entraîner le perceptron, manchot par manchot

Vous avez maintenant les caractéristiques `X` et la classe attendue `y`. Le perceptron va parcourir les lignes une par une. Pour chaque manchot, il calcule un score, prédit une espèce, compare sa prédiction à la cible, puis corrige ses paramètres en cas d'erreur.

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

## Compléter la boucle

On commence avec des poids nuls et un biais nul. À chaque ligne `i`, notez le score avant correction, calculez la prédiction avec le seuil $z\geq0$, puis comparez-la à `y[i]`. Reprenez la règle de correction vue plus haut pour compléter les deux lignes manquantes.

```python
import numpy as np

eta = 0.1
poids = np.zeros(X.shape[1])
biais = 0.0
nb_epoques = 10
historique = []

for epoque in range(nb_epoques):
    erreurs = 0

    for i in range(len(X)):
        xi = X[i]
        # Indice : produit scalaire des caractéristiques et des poids,
        # puis ajout du biais.
        score = ...
        # Indice : la classe prédite vaut 1 si le score est positif ou nul.
        classe_reelle = y[i]
        classe_predite = ...
        erreur = classe_reelle - classe_predite

        if erreur != 0:
            # Compléter : mettre à jour les poids et le biais
            ...
            ...
            erreurs += 1

        # Garder une trace des poids après le passage de ce manchot
        historique.append(poids.copy())

        # Afficher les cinq premiers passages de la première époque
        if epoque == 0 and i < 5:
            print(f"manchot {i + 1} | score avant correction={score:.3f} | "
                  f"classe réelle={classe_reelle} | prédiction={classe_predite} | "
                  f"poids après={poids} | biais après={biais:.3f}")

    print(f"Époque {epoque + 1} : {erreurs} erreur(s)")
```

**À observer et expliquer :**

1. Pour les cinq premiers manchots, repérer le score, la classe attendue, la classe prédite et les poids après le passage.
2. Quand les poids changent-ils ? Que se passe-t-il quand la prédiction est correcte ?
3. Comparer le nombre d'erreurs d'une époque à l'autre. Les poids restent-ils fixes ou évoluent-ils encore ?
4. Expliquer le rôle de $\eta$ : que changerait un pas plus grand ou plus petit ? Pour cette expérience, ne modifiez pas sa valeur pendant l'entraînement.

La boucle applique bien ces étapes à **chaque** manchot ; l'affichage des cinq premiers sert seulement à rendre le suivi lisible. Le perceptron apprend à partir de `X` et `y` : la colonne `species` ne doit jamais être ajoutée aux caractéristiques `X`.

Pour voir l'évolution des paramètres, représentez chaque colonne de `historique` avec `plt.plot`. L'axe horizontal correspond au nombre de manchots déjà traités ; chaque courbe représente un poids. Utilisez `plt.legend()` pour distinguer les poids. Observez aussi le biais, qui est suivi séparément.

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

Pour cet exemple précis, la frontière est $x_2=\frac{x_1+1}{2}$, et non $x_2=x_1$. L'égalité $x_2=x_1$ apparaîtra dans l'exercice suivant, qui utilise un autre score : $z=-x_1+x_2$.

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
