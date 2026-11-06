## **Normalisation et comparaison graphique de deux séries de données**

On s'intéresse à deux séries de mesures provenant de deux capteurs différents.
Ces capteurs ne mesurent pas dans les mêmes unités, ce qui empêche toute comparaison directe.

On travaille avec les deux séries suivantes :

```python
A = [
    12, 18, 25, 30, 35, 40, 41, 42, 45, 50,
    53, 57, 60, 62, 65, 68, 70, 72, 75, 78,
    80, 83, 85, 88, 90, 92, 95, 97, 100, 103
]
B = [
    100, 110, 95, 120, 130, 140, 125, 135, 150, 160,
    155, 165, 170, 158, 175, 180, 168, 185, 190, 200,
    195, 205, 210, 198, 215, 220, 230, 225, 240, 250
]
```

Objectifs :

1. Normaliser les deux séries dans une échelle commune, d'abord par centrage-réduction puis par min–max.
2. Représenter graphiquement les séries normalisées.
3. Comparer les distributions à l'aide d'un boxplot ou d'une courbe.
4. Interpréter les différences observées.

---

## **Études**

1. Calculer, pour chaque série A et B :

   * le minimum et le maximum.
   * la moyenne `mu`.
   * l'écart-type `sigma`.

2. Normalisez (centré-réduire)

   Questions :

   * Qu'observe-t-on sur les moyennes des séries centrées-réduites ?
   * Que peut-on dire de leurs écarts-types ?
   * Les deux séries deviennent-elles comparables en termes de forme de distribution ?

3. Normalisation `min–max`

   Calculer pour chaque valeur
   $$
   x_{\min\max} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}.
   $$

   Questions :

   * Les deux séries sont-elles maintenant sur la même échelle `[0, 1]` ?
   * Quelle information conserve-t-on avec cette normalisation ?

---

## **Représentation graphique**

### Consigne

Représenter les deux séries normalisées sur un même graphique :

* soit en boxplots comparatifs (deux boxplots côte à côte) ;
* soit en courbes représentant les valeurs dans l'ordre des observations.

Représentations à produire :

1. Un graphique avec les deux séries centrées-réduites.
2. Un graphique avec les deux séries normalisées min–max.


## **Interprétation des résultats**

Répondez aux questions suivantes :

1. Les médianes sont-elles proches dans les différentes normalisations ?
   Cela signifie-t-il que les séries ont des niveaux comparables une fois standardisées ?

## Partie facultative

2. Quelle série est la plus dispersée ?
   Observer la longueur des moustaches dans les boxplots min–max.

3. Observe-t-on des valeurs atypiques (outliers) dans l'une ou l'autre normalisation ?

4. Les courbes présentent-elles la même dynamique dans le temps ?

   * Évolution régulière ou irrégulière ?
   * Présence de pics isolés ?
   * La normalisation modifie-t-elle l'interprétation visuelle ?
