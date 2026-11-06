

#  **Exercice — Analyse de données : recommandations et matrice d’influence**

Une plateforme de streaming analyse le comportement de ses utilisateurs pour améliorer ses recommandations.
Chaque utilisateur est représenté par deux caractéristiques :

* (x) : intérêt pour les **films d’action**,
* (y) : intérêt pour les **films dramatiques**.

La plateforme observe que d’une semaine à l’autre, les préférences évoluent selon le modèle linéaire suivant :

$$
\begin{pmatrix}
x_{n+1} \\
y_{n+1}
\end{pmatrix}
=============

A
\begin{pmatrix}
x_n  \\
y_n
\end{pmatrix},
\qquad
A=
\begin{pmatrix}
0.9 & 0.4  \\
0.1 & 0.7
\end{pmatrix}.
$$

La matrice (A) encode les influences :

* regarder des films d’action augmente légèrement l’intérêt pour les films dramatiques,
* regarder des drames augmente modérément l’intérêt pour l’action,
* chaque intérêt décroît naturellement avec le temps.

---

#  **Questions**

### **1. Calculez les valeurs propres de (A).**

### **2. Trouvez les vecteurs propres associés.**

### **3. Construisez les matrices (P) et (D) telles que :**

$$
A = PDP^{-1}.
$$

### **4. Interprétez les valeurs propres dans un contexte de recommandation :**

* que se passe-t-il à long terme pour les préférences des utilisateurs ?
* pourquoi la direction propre dominante joue-t-elle un rôle clé dans les systèmes de recommandation ?

### **5. Interprétez les vecteurs propres :**

* quel vecteur décrit une **préférence stable** entre action et drame ?
* quel vecteur représente un **déséquilibre** entre les deux genres ?

### **6. BONUS — Projection d’un utilisateur**

Un utilisateur a les préférences initiales :

$$
(x_0, y_0) = (4, 1).
$$

Projeter ce vecteur sur la base des vecteurs propres et déterminer qualitativement :

* vers quelle direction l’utilisateur converge,
* quel type de recommandations la plateforme lui fera à long terme.

---

# 🧪 **Version Python pour vérifier vos résultats**

*(À placer à la fin de l’exercice, comme dans votre cours.)*

```python
import numpy as np

A = np.array($$
    $$0.9, 0.4$$,
    $$0.1, 0.7$$
$$)

# Valeurs propres et vecteurs propres
valeurs_propres, vecteurs_propres = np.linalg.eig(A)

print("Valeurs propres :")
print(valeurs_propres)

print("\nVecteurs propres :")
print(vecteurs_propres)

# Projection d'un utilisateur
u = np.array($$4, 1$$)
coeffs = np.linalg.solve(vecteurs_propres, u)

print("\nCoordonnées dans la base propre :")
print(coeffs)
```
