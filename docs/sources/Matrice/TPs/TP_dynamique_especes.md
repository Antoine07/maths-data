# **Modèle de compétition entre deux espèces**

Deux espèces animales partagent le même territoire :

* `x_n` : population des **espèces A**
* `y_n` : population des **espèces B**

Chaque année, leurs interactions sont modélisées par :

$$
X_{n+1} = M X_n,
\qquad
X_n =
\begin{pmatrix}
x_n \\ 
y_n
\end{pmatrix},
\quad
M=
\begin{pmatrix}
1.2 & -0.3 \\
-0.2 & 1.1
\end{pmatrix}.
$$

Interprétez le modèle.


##  **Données initiales**

On suppose :

$$
X_0 =
\begin{pmatrix}
100 \\
80
\end{pmatrix}.
$$

### Calculez à la main :

1. `X_1 = M X_0`
2. `X_2 = M X_1`

**Questions d'analyse :**

* Quelle espèce augmente le plus rapidement ?
* Les interactions semblent-elles positives ou négatives ?
* La domination d'une espèce semble-t-elle se renforcer ?


### **Étude asymptotique par valeurs propres**

1. Calculez les **valeurs propres** de (M).
1. Trouvez les **vecteurs propres associés**.
1. Déterminez **la valeur propre dominante**.
1. Expliquez pourquoi cette valeur contrôle le **comportement à long terme**.


##  **Comportement au fil du temps**

À partir des valeurs propres :

1. Décrire qualitativement la tendance quand `n tend vers l'infini`.
2. Les populations deviennent-elles **proportionnelles** ?
3. Quel vecteur propre décrit cette proportion ?
4. Interpréter en biologie :

   * coexistence stable ?
   * domination d'une espèce ?
   * compétition destructrice ?


##  **Simulation numérique**

Vous pouvez vérifier vos calculs avec NumPy :

```python
# TODO
```


## Exprimez en une phrase claire 

> "Quelle sera la relation entre les deux espèces après un très grand nombre d'années ?"
