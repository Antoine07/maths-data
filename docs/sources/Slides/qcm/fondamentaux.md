---
marp: true
theme: default
paginate: true
class: lead
---

# QCM de réactivation
## Des bases à la modélisation

**8 questions pour réactiver les notions du bloc.** Répondez ensemble, puis cliquez sur une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.

---

## QCM de réactivation · Des bases à la modélisation (1/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>1. Dans l’encodage cyclique d’une heure, pourquoi utiliser sinus et cosinus ensemble ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 1">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Les deux coordonnées conservent la position sur le cycle ; les heures proches de minuit restent voisines.">A. Le couple place l’heure sur un cercle et rapproche 23 h de 0 h.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Pense au passage de 23 h à 0 h : ces heures sont proches dans la journée même si leurs nombres sont éloignés.">B. Cela transforme toujours la consommation en sinus pur.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Pense au passage de 23 h à 0 h : ces heures sont proches dans la journée même si leurs nombres sont éloignés.">C. Une seule valeur de cosinus suffit à distinguer toutes les heures.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>2. Dans T(t) = a t + b, que représente a ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 2">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Dans une fonction affine, la pente décrit le changement de la sortie quand l’entrée augmente d’une unité.">A. La température au jour zéro uniquement.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="La pente a mesure la variation de T quand t augmente d’une unité, ici un jour.">B. La variation estimée de température par jour.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Dans une fonction affine, la pente décrit le changement de la sortie quand l’entrée augmente d’une unité.">C. L’erreur moyenne du modèle.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Des bases à la modélisation (2/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>3. Que renvoie np.polyfit(t, T, 1) ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 3">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le degré 1 correspond au modèle a t + b ; les coefficients sont renvoyés dans l’ordre du degré décroissant.">A. Les paramètres d’un ajustement affine de degré 1.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le dernier argument est le degré du polynôme demandé.">B. Les paramètres d’un polynôme de degré 2.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le dernier argument est le degré du polynôme demandé.">C. Les températures triées.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>4. Que décrit la dérivée f&#x27;(t) ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 4">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Distingue la hauteur de la fonction du rythme auquel elle évolue.">A. Le cumul total depuis le début.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="La dérivée décrit la variation locale de la fonction au point t.">B. La pente ou le rythme de variation instantané de f.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Distingue la hauteur de la fonction du rythme auquel elle évolue.">C. La valeur moyenne de f.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Des bases à la modélisation (3/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>5. Un rythme constant vaut 2 visiteurs par heure pendant 3 heures. Quel est le cumul ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 5">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Pour un rythme constant, multiplie le rythme par la durée.">A. 2 visiteurs.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Pour un rythme constant, multiplie le rythme par la durée.">B. 5 visiteurs.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="À rythme constant, le cumul vaut 2 × 3 = 6 visiteurs.">C. 6 visiteurs.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>6. Le rythme vaut f(t)=2t visiteurs par heure. Quel est le cumul entre 0 h et 2 h ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 6">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le rythme au bout de 2 h n’est pas resté égal à 4 pendant toute la durée.">A. 2 visiteurs, car le rythme final vaut 4.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="L’aire du triangle vaut base × hauteur / 2 = 2 × 4 / 2 = 4 visiteurs.">B. 4 visiteurs, aire du triangle sous la droite.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le rythme au bout de 2 h n’est pas resté égal à 4 pendant toute la durée.">C. 8 visiteurs, car 4 × 2 = 8.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Des bases à la modélisation (4/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>7. Dans le modèle de refroidissement T(t)=T_amb+(T0−T_amb)e^(−kt), vers quelle valeur T(t) se rapproche-t-elle ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 7">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Quand t grandit, e^(−kt) diminue et tend vers zéro.">A. La température initiale T0.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le terme exponentiel tend vers zéro ; il reste T_amb.">B. La température ambiante T_amb.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Quand t grandit, e^(−kt) diminue et tend vers zéro.">C. Zéro dans tous les cas.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>8. Après la transformation logarithmique du refroidissement, que représente la pente de la droite ajustée ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 8">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Repère le signe devant kt dans l’expression transformée.">A. k.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="ln(T−T_amb)=ln(T0−T_amb)−kt : la pente est −k.">B. −k.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Repère le signe devant kt dans l’expression transformée.">C. T_amb.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>
