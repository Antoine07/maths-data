---
marp: true
html: true
---

# Examen — Des mathématiques aux premiers réseaux

**Épreuve individuelle · 3 h · Note sur 20**

| Partie | Travail | Temps | Points |
|---|---|---|---|
| A | Mathématiques | 1 h 30 | 10 |
| B | Comprendre un réseau | 30 min | 4 |
| C | Pratique Python et interprétation | 1 h | 6 |

Nom : ........................................  Prénom : ........................................

L'épreuve porte sur les trois premières séances : représentation, statistiques et dérivée simple, puis propagation avant. Aucun entraînement PyTorch ni calcul détaillé de rétropropagation n'est demandé.

---

## Consignes et livrables

Les parties A et B se rédigent sur copie. Une calculatrice simple et la fiche de formules ci-dessous sont autorisées. Les calculs doivent être justifiés ; une valeur seule ne suffit pas lorsque la question demande une explication.

La partie C utilise la sandbox Python/NumPy préparée. Le surveillant indique le passage à cette partie après les deux premières heures. Internet, les messageries et les outils d'assistance générative ne sont pas autorisés pendant l'épreuve. Aucun accès à un corrigé n'est autorisé.

Rendre la copie et un fichier Python ou notebook nommé `NOM_Prenom_maths_ia`. Le code doit se relancer avec les fichiers fournis. Les questions sont aussi indépendantes que possible : poursuivre avec une valeur annoncée si un calcul précédent bloque, en indiquant clairement cette hypothèse.

Les données sont une petite situation **simulée pour l'examen**, distincte des 240 journées des TP. Aucun résultat ne constitue une conclusion opérationnelle sur un bâtiment réel.

---

## Fiche de formules autorisée

$$
\widehat y=Xw+b,\qquad
MSE=\frac1n\sum_i(\widehat y_i-y_i)^2.
$$

$$
\bar x=\frac1n\sum_i x_i,\qquad
v=\frac1n\sum_i(x_i-\bar x)^2,\qquad s=\sqrt v.
$$

$$
\frac{d}{dw}(w-c)^2=2(w-c),\qquad
w_{nouveau}=w-\eta L'(w).
$$

$$
\operatorname{ReLU}(z)=\max(0,z),\qquad
\sigma(z)=\frac1{1+e^{-z}},\qquad \sigma(0)=0{,}5.
$$

Une couche est une transformation affine suivie, si prévu, d'une activation. Dans les parties B et C, la décision vaut 1 si la probabilité est supérieure ou égale à 0,5.

---

## Partie A — Mathématiques · 10 points

### A1 — Représenter et prédire · 3 points

Une journée est décrite par sa température et son occupation :

| Journée | Température (°C) | Occupation | Consommation observée (kWh) |
|---|---|---|---|
| 1 | 12 | 1 | 30 |
| 2 | 14 | 2 | 32 |
| 3 | 16 | 3 | 40 |
| 4 | 18 | 4 | 42 |

On utilise des poids **fournis pour l'exercice**, $w=(2,1)^T$, et un biais $b=3$.

1. Écrire X et préciser ses dimensions, celles de w et le nombre de prédictions. **0,75 point**
2. Calculer les quatre prédictions $Xw+b$. Montrer le calcul d'au moins une ligne. **1,25 point**
3. Interpréter le poids 2 de la température et le biais 3 dans ce modèle. Expliquer pourquoi le coefficient ne démontre pas à lui seul une causalité physique. **1 point**

---

### A2 — Décrire une variable · 2 points

Utiliser les quatre températures 12, 14, 16 et 18.

1. Calculer la moyenne. **0,5 point**
2. Donner les quatre écarts centrés et calculer la variance descriptive avec le diviseur n. **0,75 point**
3. Donner l'écart-type, sous forme exacte ou approchée. **0,25 point**
4. Préciser les unités de la moyenne, de la variance et de l'écart-type. **0,5 point**

---

### A3 — Dériver une erreur et effectuer un pas · 5 points

On considère maintenant un petit problème indépendant : entrées x=(1,2), cibles y=(2,4), modèle $\widehat y=wx$ sans biais.

$$
L(w)=\frac{(w-2)^2+(2w-4)^2}{2}.
$$

1. Simplifier la perte sous la forme $c(w-2)^2$, en déterminant c. **1 point**
2. Calculer $L'(w)$. **1 point**
3. Calculer la perte et la dérivée en $w_0=0$. **0,75 point**
4. Avec un pas $\eta=0{,}1$, calculer $w_1$ et $L(w_1)$. La perte a-t-elle diminué ? **1,25 point**
5. Repartir de $w_0=0$ avec un pas $\eta=0{,}5$. Calculer le nouveau poids et sa perte. Que montre cette comparaison sur le choix du pas ? **1 point**

---

## Partie B — Comprendre un réseau · 4 points

On fournit l'entrée x=(1,2), représentée en ligne, et les paramètres :

$$
W_1=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\quad b_1=(0,0),\quad
W_2=\begin{pmatrix}1\\-1\end{pmatrix},\quad b_2=0.
$$

Le réseau calcule $h=\operatorname{ReLU}(xW_1+b_1)$, puis $z=hW_2+b_2$ et $p=\sigma(z)$.

1. Expliquer le rôle d'un poids et d'un biais. **0,5 point**
2. Calculer les deux scores cachés, les deux activations h, le logit z, la probabilité p et la décision au seuil annoncé. **2 points**
3. Pourquoi introduit-on une activation non linéaire entre deux couches affines ? **0,75 point**
4. Compter les paramètres du réseau, biais compris. Le nombre d'observations change-t-il ce total ? **0,75 point**

---

## Partie C — Pratique Python et interprétation · 6 points

Utiliser `depart_examen.py` ou le notebook de départ. Le fichier `donnees_examen.csv` contient les quatre journées de la partie A. La fonction de chargement est fournie ; aucune installation n'est demandée.

### C1 — Écrire deux fonctions · 2 points

Compléter `predire(X, w, b)` pour renvoyer une prédiction par ligne et `mse(predictions, y)` pour renvoyer la moyenne des carrés des erreurs.

Contrôler les formes ; signaler une incompatibilité au lieu de laisser NumPy créer silencieusement un tableau de différences inattendu. Afficher les prédictions et la MSE sur les quatre journées. **1 point par fonction**

### C2 — Diagnostiquer un calcul trompeur · 2 points

Le code suivant s'exécute sans erreur :

```python
predictions = (X @ w + b).reshape(-1, 1)
erreurs = predictions - y
perte = np.mean(erreurs ** 2)
```

Pour X de forme (4,2), w de forme (2,) et y de forme (4,), donner la forme de `erreurs`, expliquer pourquoi elle est incorrecte pour cette tâche et corriger le calcul. Ajouter un contrôle qui empêche ce problème. **Diagnostic 1 point ; correction et contrôle 1 point**

---

### C3 — Passer des probabilités aux décisions · 2 points

Un réseau fournit les probabilités `[0.2, 0.7, 0.4, 0.9]`. Les classes réelles sont `[0, 1, 1, 1]`.

1. Compléter `decider(probabilites)` avec la règle « classe 1 si p ≥ 0,5 ». **0,75 point**
2. Calculer le nombre de décisions correctes et identifier les observations mal classées, avec des numéros de 1 à 4. **0,75 point**
3. Une probabilité de 0,9 signifie-t-elle que la décision est certaine ? Justifier brièvement. **0,5 point**

Une implémentation vectorisée ou une boucle correcte est acceptée. Les explications doivent distinguer probabilité estimée, décision et valeur réelle.

---

## Vérification avant remise

- Le fichier ou notebook porte votre nom.
- Les parties A et B contiennent les étapes des calculs.
- Le code de la partie C se relance dans l'ordre avec le CSV fourni.
- Les formes sont vérifiées et aucune réponse ne repose sur un accès au corrigé.
- Vous avez indiqué les hypothèses éventuellement utilisées pour poursuivre une question.

Fin du sujet. Le corrigé est remis séparément par l'enseignant.
