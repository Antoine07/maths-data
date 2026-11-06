# **ACP** - Facultatif

On conserve les séries `A` et `B` du TP précédent.

Nous travaillerons exclusivement avec les séries **centrées-réduites**, car c'est le prétraitement indispensable avant une ACP.

On note :

$$
A_i^{*} = \frac{A_i - \mu_A}{\sigma_A}, \qquad
B_i^{*} = \frac{B_i - \mu_B}{\sigma_B}.
$$

---

## **1. Calcul des séries centrées-réduites**

1. À partir des résultats précédents, rappeler les valeurs de :

$$
\mu_A,\ \sigma_A
$$

$$
\mu_B,\ \sigma_B
$$

2. Calculer explicitement les trois premières valeurs centrées-réduites des deux séries :

Par exemple :

$$
A^{*}_1 = \frac{12 - \mu_A}{\sigma_A},\qquad
A^{*}_2 = \frac{18 - \mu_A}{\sigma_A},\qquad
A^{*}_3 = \frac{25 - \mu_A}{\sigma_A}.
$$

Faire de même pour :

$$
B^{*}_1,\ B^{*}_2,\ B^{*}_3.
$$

3. Vérifier par un calcul direct que :

$$
\frac{1}{n}\sum_{i=1}^n A_i^{*} = 0,
\qquad
\frac{1}{n}\sum_{i=1}^n B_i^{*} = 0,
$$

et que les variances valent bien 1.

On pourra calculer une moyenne approchée avec seulement les 5 premières valeurs pour tester.

---

## **2. Calcul du coefficient de corrélation**

Le coefficient de corrélation entre les séries centrées-réduites se calcule par :

$$
r = \frac{1}{n} \sum_{i=1}^n A_i^{*} B_i^{*}.
$$

1. Calculer les produits (A_i^{*} B_i^{*}) pour les cinq premières valeurs.
2. En déduire une approximation du coefficient de corrélation (sur cinq valeurs).
3. Donner ensuite le coefficient exact avec Python ou une calculatrice.

Questions :

* Le coefficient est-il positif, négatif, proche de 1 ou 0 ?
* Les variations des deux séries sont-elles liées ?
* Peut-on dire qu'une partie de la variabilité de B est expliquée par A ?

---

## **3. Construction du nuage de points dans**

$$
(A^{*}, B^{*})
$$

Représenter chaque observation sous forme de point :

$$
P_i = (A_i^{*},\ B_i^{*}).
$$

Consignes :

1. Tracer le nuage de points en utilisant les valeurs normalisées.
2. Identifier visuellement :

   * s'il existe une direction dominante (un alignement approximatif),
   * si les points sont plutôt étalés ou regroupés.

Guidage :

Calculer :

$$
P_1 = (A^{*}_1, B^{*}_1),\quad
P_2 = (A^{*}_2, B^{*}_2),\quad
P_3 = (A^{*}_3, B^{*}_3).
$$

Questions :

* Le nuage semble-t-il pencher dans une direction particulière ?
* Cette direction correspond-elle à une relation linéaire entre A et B ?

---

## **4. Identification d'un axe principal (idée essentielle de l'ACP)**

À partir du nuage de points centrés-réduits :

1. Dessiner une droite qui semble suivre la tendance générale du nuage.
2. Projeter quelques points sur cette droite (en traçant les perpendiculaires).

Guidage de calcul :

Pour un axe donné par une direction vectorielle normalisée `u = (u1, u2)`, la projection de (P_i) est :

$$
c_i = A_i^{*} u_1 + B_i^{*} u_2.
$$

1. Choisir une direction simple, par exemple
   $$
   u = \left(\frac{1}{\sqrt{2}},\ \frac{1}{\sqrt{2}}\right)
   $$
   si A et B sont corrélées positivement.
2. Calculer les projections `c1, c2, c3`.
3. Commenter ce que représentent ces valeurs projetées.

Questions :

* La projection condense-t-elle l'information de manière cohérente ?
* Les projections ordonnent-elles les observations de façon similaire aux séries initiales ?
* Pourquoi ce procédé constitue-t-il une réduction de dimension ?

---

## **5. Transition finale vers l'ACP formelle**

Rédiger une conclusion guidée :

1. Pourquoi devait-on d'abord centrer-réduire les données ?
2. Pourquoi le coefficient de corrélation est-il crucial pour comprendre la structure du nuage ?
3. Pourquoi l'axe que l'on a dessiné s'apparente-t-il à la première composante principale ?
4. Comment l'ACP formalise-t-elle :

   * la recherche de l'axe maximisant la variance,
   * le calcul automatique des projections,
   * la réduction de dimension à un seul axe ?
