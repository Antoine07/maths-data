---
marp: true
html: true
paginate: true
---

# Problème — Peut-on certifier qu’un nombre est premier ?

On veut décider si un entier est premier sans tester tous les nombres jusqu’à lui. Le problème invite à construire un crible, justifier la borne de recherche, puis programmer et analyser une méthode.

---

# Démo 1 · Le crible d’Ératosthène

**Objectif :** trouver tous les nombres premiers jusqu'à une borne, puis justifier la méthode.

Un entier naturel est **premier** s'il est supérieur ou égal à 2 et possède exactement deux diviseurs positifs : 1 et lui-même.

- 7 est premier ; 12 ne l'est pas, car $12 = 3 \times 4$.
- **1 n'est pas premier** : il n'a qu'un seul diviseur positif.
- Un **multiple** de $p$ s'écrit $kp$, où $k$ est un entier.

Le crible garde un nombre premier et élimine ses multiples plus grands que lui. On recommence avec le prochain nombre non éliminé.

---

# Diviseurs premiers et diviseurs premiers stricts

Un **diviseur premier** de $N$ est un nombre premier qui divise $N$. Il est **strict** s'il est strictement inférieur à $N$.

Pour **7** :

- Les diviseurs positifs sont $\{1,7\}$.
- Les diviseurs premiers sont $\{7\}$.
- Les diviseurs premiers stricts forment l'ensemble vide : $\varnothing$.

Le mot **premiers** est essentiel : 1 est un diviseur strict de 7, mais il n'est pas premier.

**Notation :** $\varnothing$ et $\{\}$ désignent l'ensemble vide. L'ensemble $\{\varnothing\}$ contient un élément, qui est lui-même l'ensemble vide.

---

# À faire · Passer les entiers de 1 à 30 au crible

**Prérequis :** multiplication et divisibilité.

Écrire les nombres de 1 à 30, puis barrer 1.

1. Entourer 2 et barrer ses multiples à partir de $2^2 = 4$.
2. Entourer le prochain nombre non barré : 3. Barrer ses multiples à partir de $3^2 = 9$.
3. Recommencer avec 5, à partir de $5^2 = 25$.
4. Lister les nombres restants. Pourquoi peut-on arrêter avant de traiter 7 ?

**Livrable :** une grille annotée, la liste obtenue et une phrase justifiant l'arrêt. Ne pas barrer le nombre premier lui-même.

<details><summary>Indice · Chercher un petit facteur</summary>

Si un nombre s'écrit $ab$ et que ses deux facteurs sont strictement supérieurs à $\sqrt{30}$, leur produit dépasse 30. Un nombre non premier entre 2 et 30 possède donc un facteur premier parmi 2, 3 et 5.

</details>

<details><summary>Correction · Les nombres conservés et la preuve de l'arrêt</summary>

On obtient **2, 3, 5, 7, 11, 13, 17, 19, 23 et 29**.

![Grille du crible jusqu'à 30 : 1 est exclu ; les dix nombres premiers sont entourés en vert ; les autres nombres sont barrés.](images/crible-eratosthene.svg)

**Démonstration par contradiction.** Supposons qu'un nombre composé $n \leq 30$ soit encore non barré après le passage de 2, 3 et 5.

Il possède un facteur premier $p$ inférieur ou égal à $\sqrt{n}$. On a donc :

$$
p \leq \sqrt{n} \leq \sqrt{30} \approx 5{,}477 < 6.
$$

Comme $p$ est un entier premier, il vaut nécessairement **2, 3 ou 5**.

Mais $n$ est alors un multiple de l'un de ces trois nombres. Puisque $n$ est composé, il est strictement supérieur à ce facteur premier : **il aurait donc déjà été barré**.

C'est une contradiction avec notre supposition. **Aucun nombre composé ne peut rester : tous les nombres conservés sont premiers.**

Le prochain nombre non barré est 7 et $7^2 = 49 > 30$ : on peut donc arrêter le crible après le passage de 5.

</details>

---

# Pourquoi le crible fonctionne-t-il ?

Un entier **composé** est un entier supérieur ou égal à 2 qui n'est pas premier. Il s'écrit $n = ab$ avec $a,b \geq 2$.

**Un petit facteur suffit.** On appelle $a$ le plus petit des deux facteurs, donc $2 \leq a \leq b$. Alors $a^2 \leq ab = n$, d'où $a \leq \sqrt{n}$. Ce facteur $a$ possède lui-même un diviseur premier $p \leq a \leq \sqrt{n}$.

**Aucun premier n'est barré.** Les nombres éliminés sont des multiples $kp$ avec $k \geq 2$ : ils sont composés.

**Aucun composé ne reste.** Tout composé $n \leq N$ possède un facteur premier inférieur ou égal à $\sqrt{N}$. Traiter ces facteurs suffit à l'éliminer.

**Pourquoi commencer à $p^2$ ?** Les multiples $2p, 3p, \ldots, (p-1)p$ ont déjà été barrés par un facteur premier plus petit que $p$.

![Au passage de 7, les multiples 14, 21, 28, 35 et 42 sont déjà barrés par 2, 3 ou 5. Le premier nouveau multiple à barrer est 49, égal à 7 au carré.](images/crible-depart-carre.svg)

**À lire sur le dessin :** $28=4\times7=2\times14$ et $42=6\times7=2\times21$ ont déjà été barrés au passage de 2. Le multiplicateur n'a pas besoin d'être premier.

Ici, on imagine un crible allant au moins jusqu'à 49. **Pour la grille limitée à 30, on s'arrête après 5**, puisque $7^2>30$.

---

# Le crible · Du raisonnement au code

**À vous de programmer le crible**, puis d'en analyser le coût en temps et en mémoire.

**Entrée :** un entier naturel `n`. **Sortie :** la liste des nombres premiers inférieurs ou égaux à `n`.

1. Écrire une fonction `crible(n)` à partir du raisonnement précédent, sans bibliothèque de génération de nombres premiers.
2. Prévoir les cas `n = 0`, `1` et `2`. Commencer les barrages à $p^2$ et justifier la condition d'arrêt.
3. Vérifier le résultat pour 30 et contrôler que 49 n'est pas déclaré premier.
4. Ajouter temporairement un compteur : compter chaque écriture qui barre un multiple, même si ce multiple était déjà barré. Quel total obtient-on pour 30 ?
5. Déterminer les complexités en temps et en mémoire lorsque `n` augmente. Distinguer l'initialisation, les barrages et la construction du résultat.

**Livrable :** code, résultats des vérifications, compteur pour 30 et analyse argumentée des complexités. **Réussite :** borne incluse, aucun nombre premier barré et prise en compte de toutes les boucles et des listes utilisées.

<details><summary>Indices gradués</summary>

1. Utiliser une table dont la case d'indice `i` indique si `i` est encore candidat ; exclure 0 et 1.
2. Ne barrer les multiples d'un candidat que si celui-ci n'a pas déjà été éliminé.
3. Pour un premier $p$, estimer le nombre de barrages à l'aide de $n/p$, puis additionner les coûts des passages. Le nombre de tours de la seule boucle extérieure ne donne pas le coût total.

</details>

<details><summary>Afficher la correction · Algorithme, vérifications et complexités</summary>

```python
def crible(n):
    if n < 2:
        return []
    premier = [True] * (n + 1)
    premier[0] = premier[1] = False
    p = 2
    while p * p <= n:
        if premier[p]:
            for multiple in range(p * p, n + 1, p):
                premier[multiple] = False
        p += 1
    return [i for i in range(2, n + 1) if premier[i]]

print(crible(30))
```

`premier[i]` indique si `i` est encore candidat ; `p` parcourt les facteurs possibles. Le pas `p` du `range` parcourt les multiples ; `n + 1` permet d'inclure la borne `n`.

**Résultats et piège de la borne.**

`crible(0)` et `crible(1)` donnent `[]`, `crible(2)` donne `[2]` et `crible(30)` donne `[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]`. Le nombre 49 est barré au passage de 7.

Avec une borne de fin `n` au lieu de `n + 1`, le multiple `n` n'est pas traité. Par exemple, 25 resterait candidat au passage de 5 : le programme le déclarerait premier à tort.

**Compteur pour 30.** Au passage de 2, on effectue 14 écritures, de 4 à 30. Au passage de 3, on en effectue 8, de 9 à 30. Au passage de 5, on en effectue 2 : 25 et 30. Le total est donc **24 barrages**, en comptant les écritures répétées sur un même nombre.

**Mémoire.** La table `premier` contient $n+1$ cases : la mémoire auxiliaire est **$O(n)$**. La liste renvoyée ne change pas cet ordre. Le crible stocke une table pour tout l'intervalle ; sa mémoire n'est donc pas constante.

**Temps.** Initialiser la table et parcourir les indices pour construire le résultat coûtent chacun $O(n)$. Pour un premier $p\leq\sqrt n$, les barrages coûtent au plus $n/p$ opérations. Leur coût total est donc majoré par :

$$
n\sum_{\substack{p\leq\sqrt n\\p\text{ premier}}}\frac1p.
$$

En majorant cette somme par celle de tous les entiers de 2 à $\lfloor\sqrt n\rfloor$, on obtient une **borne simple $O(n\log n)$**. Une analyse plus fine de la somme sur les seuls nombres premiers donne **$O(n\log\log n)$** pour ce crible ; ce résultat est admis ici.

La boucle extérieure s'arrête à la racine, mais chaque passage peut barrer de nombreux multiples : le crible complet n'est pas un algorithme en $O(\sqrt n)$.

Référence pour l'analyse affinée : [CP-Algorithms — analyse du crible d'Ératosthène](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html#asymptotic-analysis).

[Télécharger le programme Python](../../../exemples/revision/crible.py).

</details>

---

# Reconnaître un nombre premier

Pour un entier $N \geq 2$, notons :

$$
P_N=\{p\mid p\text{ est premier},\ p\mid N,\ p<N\}.
$$

$p\mid N$ signifie que $p$ divise $N$, sans reste. $P_N$ est donc l'ensemble des **diviseurs premiers stricts** de $N$.

$$
N\text{ est premier}\quad\Longleftrightarrow\quad P_N=\varnothing.
$$

**Exemples :** $P_7=\varnothing$, tandis que $P_{12}=\{2,3\}$. La condition $N\geq2$ exclut 1, qui n'est pas premier malgré l'absence de diviseur premier strict.

<details><summary>Correction · Pourquoi ce critère fonctionne-t-il ?</summary>

Si $N$ est premier, ses seuls diviseurs positifs sont 1 et $N$. Aucun n'est un diviseur premier strict : $P_N=\varnothing$.

Réciproquement, supposons $P_N=\varnothing$. Si $N$ était composé, il s'écrirait $N=ab$ avec $2\leq a\leq b<N$. L'entier $a$ posséderait un facteur premier $p\leq a<N$. Ce nombre $p$ diviserait aussi $N$, donc appartiendrait à $P_N$ : contradiction. Ainsi, $N$ est premier.

</details>

---

# Réduire la recherche à la racine carrée

Tout nombre composé $N$ possède un diviseur premier $p\leq\sqrt N$, comme nous l'avons démontré pour justifier le crible.

**Il suffit donc de vérifier qu'aucun diviseur premier inférieur ou égal à $\sqrt N$ ne divise $N$.**

<details><summary>Correction · La contradiction sous la borne</summary>

Supposons qu'aucun tel diviseur n'existe, mais que $N$ soit composé. Écrivons $N=ab$ avec $2\leq a\leq b$.

Alors $a^2\leq ab=N$, donc $a\leq\sqrt N$. Comme $a\geq2$, il possède un facteur premier $p\leq a$. Ce facteur divise aussi $N$, avec $p\leq\sqrt N$ : contradiction.

</details>

Pour programmer ce contrôle simplement, nous testerons **tous les entiers de 2 à $\lfloor\sqrt N\rfloor$**, sans construire une liste préalable de nombres premiers. Le symbole $\lfloor\sqrt N\rfloor$ désigne la partie entière de la racine.

La borne est **incluse** : pour 49, il faut tester 7.

---

# Tester la primalité en Python

```python
def est_premier(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

print(est_premier(7), est_premier(49), est_premier(101))
```

**Lecture et exécution :** pour un entier `n`, `d` parcourt les diviseurs candidats ; `%` calcule le reste. Un reste nul suffit à conclure que `n` est composé. Sans diviseur sous la borne, la fonction renvoie `True`. Résultat : `True False True`.

**Erreur fréquente :** écrire `d * d < n` au lieu de `<=` ferait manquer le facteur 7 de 49. La comparaison de carrés utilise uniquement des entiers.

---

# Mesurer le travail : combien de tests ?

Nous comptons les opérations `n % d`, c'est-à-dire les **tests de divisibilité**.

| Entier $N$ | Résultat | Nombre de tests |
|---|---|---|
| 7 | Premier | 1 : tester 2 |
| 49 | Composé | 6 : tester 2 à 7 |
| 101 | Premier | 9 : tester 2 à 10 |
| 1009 | Premier | 30 : tester 2 à 31 |

Pour $N\geq2$, on effectue au plus $\lfloor\sqrt N\rfloor-1$ tests. Cette borne est atteinte lorsque $N$ est premier ; un diviseur peut permettre de s'arrêter plus tôt.

**Complexité : $O(\sqrt N)$ tests dans le pire cas.** La mémoire auxiliaire utilise un nombre constant de variables, soit $O(1)$ dans ce modèle.

Pour des nombres premiers de taille comparable, multiplier $N$ par environ 100 multiplie le nombre de tests par environ 10. Cette estimation compte les tests ; elle ne donne pas une durée d'exécution garantie.

---

# À faire · Vérifier l'algorithme et sa complexité

**Objectif :** relier la preuve, les cas limites et le nombre d'opérations.

1. Prédire les réponses pour 1, 2, 7, 49 et 121.
2. Ajouter un compteur incrémenté juste avant chaque calcul de `n % d`.
3. Vérifier les nombres de tests du tableau et expliquer pourquoi tester tous les entiers n'impose pas de chercher d'abord les nombres premiers.

**Livrable :** réponses, compteur et justification de la borne. **Réussite :** 1 est refusé, 2 est accepté sans test, et les carrés 49 et 121 sont refusés.

<details><summary>Correction · Résultats et compteur</summary>

Les réponses sont `False`, `True`, `True`, `False`, `False`. Les nombres de tests sont respectivement **0, 0, 1, 6 et 10**.

Le compteur doit augmenter à chaque test, y compris celui qui trouve un diviseur. Pour 121, le dernier candidat est 11 : le test de la racine est indispensable.

Tester tous les entiers jusqu'à la racine inclut tous les nombres premiers de cet intervalle. Si aucun de ces entiers ne divise $N$, aucun nombre premier de cet intervalle ne le divise non plus : le critère démontré s'applique.

Le [programme téléchargeable](../../../exemples/revision/primalite.py) fournit `est_premier` et `analyser_primalite`, qui renvoie la réponse et le compteur. Il affiche aussi une mesure de temps indicative pour comparer les exécutions ; le nombre de tests justifie la complexité, les chronométrages dépendent de la machine.

</details>
