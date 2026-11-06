# Où sont passées mes dix minutes ?

## Objectif et prérequis

**Après :** [révisions d'algèbre](../../Slides/revision.md), en prolongement du [problème des rencontres](../Tail_End/01_rencontres.md).

**Durée :** 20 min. **Objectif :** convertir un petit temps quotidien en un ordre de grandeur cumulé, sans changer d'unité au milieu du raisonnement.

## La situation

Mina consacre dix minutes par jour à un rituel. Elle dit : « Dix minutes, c'est presque rien. » Son ami lui propose d'examiner vingt ans de ce rituel.

Pour ce scénario fictif, une année compte 365 jours. Une « journée disponible » est fixée à 16 heures : il ne s'agit donc pas d'une journée civile de 24 heures. Le modèle additionne du temps ; il ne mesure pas la valeur du rituel.

---

## Énoncé

1. Calculer le temps cumulé en minutes, puis en heures, sur un an et sur vingt ans.
2. Convertir le résultat de vingt ans en journées civiles de 24 h, puis en journées de 16 h. Pourquoi les nombres diffèrent-ils ?
3. Dessiner vingt colonnes représentant chacune une année. Quelle unité utiliser pour leur hauteur ?
4. Mina remplace cinq minutes de ce rituel par cinq minutes d'une autre activité. A-t-elle gagné du temps dans son calendrier ? Quelle quantité a changé d'usage ?
5. Expliquer pourquoi 76 journées de 16 h réparties en petites séquences ne sont pas identiques à 76 journées libres d'affilée.

## Contraintes, livrables et critères de réussite

**Contraintes :** garder 365 jours par an et annoncer la définition d'une journée. **Livrables :** conversions, représentation et conclusion de trois lignes.

**Critères :** même quantité de temps dans toutes les conversions ; distinction entre temps cumulé, disponibilité continue et valeur d'une activité.

<details><summary>Indices gradués</summary>

1. Multiplier minutes/jour × jours/an × années.
2. Diviser par 60 pour passer aux heures, puis par la durée de journée choisie.
3. Une réaffectation de temps n'augmente pas la durée du calendrier.
</details>

---

## Correction — Un petit nombre répété

<details><summary>Afficher la correction</summary>

Sur un an : $10\times365=3\,650$ minutes, soit environ 60,83 heures.

Sur vingt ans : $73\,000$ minutes, soit $1\,216{,}67$ heures. Cela représente environ 50,69 journées civiles ou **76,04 journées de 16 h**.

![Un rituel de dix minutes par jour cumule environ 60,83 heures par an ; la courbe atteint 1216,67 heures après vingt ans.](../../Slides/figures/paradoxe-minutes.svg)

Réaffecter cinq minutes par jour déplace $608{,}33$ heures sur vingt ans, sans ajouter d'heures au calendrier. Ces heures fragmentées n'offrent pas nécessairement les possibilités d'un bloc continu.
</details>

---

## Correction — Contrôle Python

<details><summary>Afficher la correction</summary>

```python
minutes = 10 * 365 * 20
heures = minutes / 60
print(round(heures, 2))
print(round(heures / 24, 2), round(heures / 16, 2))
```

**Lecture :** la quantité initiale est en minutes ; chaque division convertit l'unité. Les sorties sont `1216.67`, puis `50.69 76.04`.

**Erreur fréquente :** annoncer 76 jours sans préciser qu'il s'agit de journées de 16 h, ou appeler ce cumul des vacances automatiquement disponibles.
</details>

## Discussion — Compter ne suffit pas à juger

Le rituel pourrait être reposant, utile ou simplement agréable. Le calcul rend un volume visible ; il ne décide pas de ce que Mina devrait faire de son temps.

**Lien data :** un indicateur gagne en clarté lorsque son unité, sa période et ce qu'il exclut sont annoncés.

[Tous les problèmes du parcours](../../docs/problemes.html).
