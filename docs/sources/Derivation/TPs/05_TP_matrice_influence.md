#  **Exercice — Analyse de données : recommandations et matrice d'influence**

Une plateforme de streaming analyse le comportement de ses utilisateurs pour améliorer ses recommandations.
Chaque utilisateur est représenté par deux caractéristiques :

(x) : intérêt pour les **films d'action**,
(y) : intérêt pour les **films dramatiques**.

La plateforme observe que d'une semaine à l'autre, les préférences évoluent selon le modèle linéaire suivant :

$$
\begin{pmatrix}
x_{n+1} \\
y_{n+1}
\end{pmatrix}
$$

$$
\begin{pmatrix}
x_n \\
y_n
\end{pmatrix}
$$



### **Calculez les valeurs propres de (A).**

### **Trouvez les vecteurs propres associés.**

### **Construisez les matrices (P) et (D) telles que :**

$$
A = PDP^{-1}.
$$

### **Interprétez les valeurs propres dans un contexte de recommandation :**

* que se passe-t-il à long terme pour les préférences des utilisateurs ?
* pourquoi la direction propre dominante joue-t-elle un rôle clé dans les systèmes de recommandation ?

### **Interprétez les vecteurs propres :**

* quel vecteur décrit une **préférence stable** entre action et drame ?
* quel vecteur représente un **déséquilibre** entre les deux genres ?

### **Projection d'un utilisateur**

Un utilisateur a les préférences initiales :

$$
(x_0, y_0) = (4, 1).
$$

Projeter ce vecteur sur la base des vecteurs propres et déterminer qualitativement :

* vers quelle direction l'utilisateur converge,
* quel type de recommandations la plateforme lui fera à long terme.
