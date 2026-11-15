---
marp: true
theme: default
paginate: true
class: lead
---

# QCM de réactivation
## Statistiques avec NumPy

**8 questions pour réactiver les notions du bloc.** Répondez ensemble, puis cliquez sur une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.

---

## QCM de réactivation · Statistiques avec NumPy (1/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>1. Une valeur centrée-réduite se calcule comment ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 1">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="On retire la moyenne puis on divise par l’écart-type ; la valeur indique un écart en unités d’écart-type.">A. (x−moyenne)/écart-type.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le score z compare d’abord l’écart à la moyenne à la dispersion de la série.">B. x−écart-type.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le score z compare d’abord l’écart à la moyenne à la dispersion de la série.">C. moyenne/x.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>2. Un score z vaut 2. Comment l’interpréter ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 2">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le score z est une distance standardisée, pas une probabilité.">A. La valeur est deux unités au-dessus de zéro.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le score z compte les écarts-types signés depuis la moyenne.">B. La valeur est deux écarts-types au-dessus de la moyenne.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le score z est une distance standardisée, pas une probabilité.">C. La probabilité de l’observation vaut 2.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Statistiques avec NumPy (2/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>3. Que signifie fixer le seuil d’un test à 5 % ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 3">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le seuil contrôle le risque de première espèce de la procédure, sous H0.">A. Sous H0, le test vise au plus 5 % de rejets à tort à long terme.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le 5 % porte sur la fréquence de fausses alertes de la procédure, pas sur la probabilité de H0.">B. H0 a 5 % de chances d’être vraie.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le 5 % porte sur la fréquence de fausses alertes de la procédure, pas sur la probabilité de H0.">C. La conclusion a exactement 5 % de chances d’être fausse.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>4. On observe 25 six sur 100 lancers et on teste un excès. Quelle probabilité correspond à la p-value simulée ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 4">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="La p-value additionne les résultats au moins aussi extrêmes selon la direction choisie.">A. P(X=25).</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le test unilatéral compte 25 six ou plus, dans les simulations où H0 est vraie.">B. P(X≥25) sous H0.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="La p-value additionne les résultats au moins aussi extrêmes selon la direction choisie.">C. La probabilité que le dé soit équilibré.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Statistiques avec NumPy (3/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>5. Pour le test bilatéral de 25 six, quelles zones sont aussi éloignées de la moyenne 100/6 ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 5">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="25 est à environ 8,33 au-dessus de 16,67 ; le miroir est 8,33 ou moins, donc X≤8.">A. X≤8 ou X≥25.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Reporte l’écart observé de l’autre côté de la moyenne, puis tiens compte du fait que X est entier.">B. X≤16 ou X≥25.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Reporte l’écart observé de l’autre côté de la moyenne, puis tiens compte du fait que X est entier.">C. Uniquement X≥25.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>6. Dans l’exemple des dés, qu’approche la courbe de Gauss quand le nombre de dés augmente ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 6">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le théorème central limite concerne ici les moyennes répétées ; un dé reste uniforme.">A. La distribution des moyennes de plusieurs dés.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Distingue un lancer individuel de la moyenne de plusieurs lancers.">B. La distribution des faces d’un seul dé.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Distingue un lancer individuel de la moyenne de plusieurs lancers.">C. La probabilité de chaque face, qui devient inégale.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Statistiques avec NumPy (4/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>7. Une covariance positive indique surtout que, dans les données, les deux variables…</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 7">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="La covariance décrit une variation conjointe, sans établir une causalité.">A. ont tendance à varier dans le même sens.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Une association statistique ne prouve pas à elle seule une cause.">B. ont une relation causale certaine.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Une association statistique ne prouve pas à elle seule une cause.">C. ont toujours la même moyenne.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>8. Dans k-means, comment met-on à jour le centre d’un groupe non vide ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 8">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le centroïde est la moyenne colonne par colonne des observations du groupe.">A. En prenant la moyenne des observations affectées.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le centre de k-means est un point moyen, qui n’est pas forcément une observation.">B. En choisissant l’observation la plus éloignée.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le centre de k-means est un point moyen, qui n’est pas forcément une observation.">C. En prenant la classe la plus fréquente.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---
