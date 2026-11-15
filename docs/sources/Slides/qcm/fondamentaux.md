---
marp: true
theme: default
paginate: true
class: lead
---

# QCM de réactivation
## Des bases à la modélisation

**8 questions pour réactiver les notions du bloc.** Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ». Le feedback explique la réponse ; après une erreur, vous pouvez modifier votre choix et réessayer.

---

## QCM de réactivation · Des bases à la modélisation (1/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-1-label">1. Dans l’encodage cyclique d’une heure, pourquoi utiliser sinus et cosinus ensemble ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-1-label">
<label class="qcm-choice" for="qcm-fondamentaux-1-a"><input id="qcm-fondamentaux-1-a" type="radio" name="qcm-fondamentaux-1" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Les deux coordonnées conservent la position sur le cycle ; les heures proches de minuit restent voisines."><span>A. Le couple place l’heure sur un cercle et rapproche 23 h de 0 h.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-1-b"><input id="qcm-fondamentaux-1-b" type="radio" name="qcm-fondamentaux-1" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Pense au passage de 23 h à 0 h : ces heures sont proches dans la journée même si leurs nombres sont éloignés."><span>B. Cela transforme toujours la consommation en sinus pur.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-1-c"><input id="qcm-fondamentaux-1-c" type="radio" name="qcm-fondamentaux-1" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Pense au passage de 23 h à 0 h : ces heures sont proches dans la journée même si leurs nombres sont éloignés."><span>C. Une seule valeur de cosinus suffit à distinguer toutes les heures.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-1-d"><input id="qcm-fondamentaux-1-d" type="radio" name="qcm-fondamentaux-1" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La numérotation brute crée une grande distance artificielle entre 23 et 0."><span>D. Donner à chaque heure un nombre de 0 à 23 suffit à bien représenter la proximité entre 23 h et 0 h.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-2-label">2. Dans T(t) = a t + b, que représente a ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-2-label">
<label class="qcm-choice" for="qcm-fondamentaux-2-a"><input id="qcm-fondamentaux-2-a" type="radio" name="qcm-fondamentaux-2" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Dans une fonction affine, la pente décrit le changement de la sortie quand l’entrée augmente d’une unité."><span>A. La température au jour zéro uniquement.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-2-b"><input id="qcm-fondamentaux-2-b" type="radio" name="qcm-fondamentaux-2" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="La pente a mesure la variation de T quand t augmente d’une unité, ici un jour."><span>B. La variation estimée de température par jour.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-2-c"><input id="qcm-fondamentaux-2-c" type="radio" name="qcm-fondamentaux-2" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Dans une fonction affine, la pente décrit le changement de la sortie quand l’entrée augmente d’une unité."><span>C. L’erreur moyenne du modèle.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-2-d"><input id="qcm-fondamentaux-2-d" type="radio" name="qcm-fondamentaux-2" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La pente décrit une variation par unité de temps ; la valeur initiale est associée à l’ordonnée à l’origine."><span>D. La pente a est la valeur de T au premier jour mesuré.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Des bases à la modélisation (2/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-3-label">3. Que renvoie np.polyfit(t, T, 1) ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-3-label">
<label class="qcm-choice" for="qcm-fondamentaux-3-a"><input id="qcm-fondamentaux-3-a" type="radio" name="qcm-fondamentaux-3" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Le degré 1 correspond au modèle a t + b ; les coefficients sont renvoyés dans l’ordre du degré décroissant."><span>A. Les paramètres d’un ajustement affine de degré 1.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-3-b"><input id="qcm-fondamentaux-3-b" type="radio" name="qcm-fondamentaux-3" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le dernier argument est le degré du polynôme demandé."><span>B. Les paramètres d’un polynôme de degré 2.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-3-c"><input id="qcm-fondamentaux-3-c" type="radio" name="qcm-fondamentaux-3" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le dernier argument est le degré du polynôme demandé."><span>C. Les températures triées.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-3-d"><input id="qcm-fondamentaux-3-d" type="radio" name="qcm-fondamentaux-3" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le degré 1 correspond à une droite, pas à une constante."><span>D. Un ajustement constant de degré 0.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-4-label">4. Que décrit la dérivée f&#x27;(t) ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-4-label">
<label class="qcm-choice" for="qcm-fondamentaux-4-a"><input id="qcm-fondamentaux-4-a" type="radio" name="qcm-fondamentaux-4" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Distingue la hauteur de la fonction du rythme auquel elle évolue."><span>A. Le cumul total depuis le début.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-4-b"><input id="qcm-fondamentaux-4-b" type="radio" name="qcm-fondamentaux-4" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="La dérivée décrit la variation locale de la fonction au point t."><span>B. La pente ou le rythme de variation instantané de f.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-4-c"><input id="qcm-fondamentaux-4-c" type="radio" name="qcm-fondamentaux-4" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Distingue la hauteur de la fonction du rythme auquel elle évolue."><span>C. La valeur moyenne de f.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-4-d"><input id="qcm-fondamentaux-4-d" type="radio" name="qcm-fondamentaux-4" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La dérivée mesure un rythme instantané ; le cumul est relié à l’aire sous la courbe."><span>D. La dérivée donne toujours le cumul depuis l’origine.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Des bases à la modélisation (3/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-5-label">5. Un rythme constant vaut 2 visiteurs par heure pendant 3 heures. Quel est le cumul ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-5-label">
<label class="qcm-choice" for="qcm-fondamentaux-5-a"><input id="qcm-fondamentaux-5-a" type="radio" name="qcm-fondamentaux-5" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Pour un rythme constant, multiplie le rythme par la durée."><span>A. 2 visiteurs.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-5-b"><input id="qcm-fondamentaux-5-b" type="radio" name="qcm-fondamentaux-5" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Pour un rythme constant, multiplie le rythme par la durée."><span>B. 5 visiteurs.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-5-c"><input id="qcm-fondamentaux-5-c" type="radio" name="qcm-fondamentaux-5" value="C" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="À rythme constant, le cumul vaut 2 × 3 = 6 visiteurs."><span>C. 6 visiteurs.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-5-d"><input id="qcm-fondamentaux-5-d" type="radio" name="qcm-fondamentaux-5" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Un rythme par heure se multiplie par la durée pour obtenir un cumul."><span>D. 5 visiteurs, car 2 + 3 = 5.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-6-label">6. Le rythme vaut f(t)=2t visiteurs par heure. Quel est le cumul entre 0 h et 2 h ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-6-label">
<label class="qcm-choice" for="qcm-fondamentaux-6-a"><input id="qcm-fondamentaux-6-a" type="radio" name="qcm-fondamentaux-6" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le rythme au bout de 2 h n’est pas resté égal à 4 pendant toute la durée."><span>A. 2 visiteurs, car le rythme final vaut 4.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-6-b"><input id="qcm-fondamentaux-6-b" type="radio" name="qcm-fondamentaux-6" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="L’aire du triangle vaut base × hauteur / 2 = 2 × 4 / 2 = 4 visiteurs."><span>B. 4 visiteurs, aire du triangle sous la droite.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-6-c"><input id="qcm-fondamentaux-6-c" type="radio" name="qcm-fondamentaux-6" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le rythme au bout de 2 h n’est pas resté égal à 4 pendant toute la durée."><span>C. 8 visiteurs, car 4 × 2 = 8.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-6-d"><input id="qcm-fondamentaux-6-d" type="radio" name="qcm-fondamentaux-6" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le rythme augmente : il faut compter l’aire sous la droite, pas un rectangle à la hauteur finale."><span>D. 8 visiteurs, en prenant le rythme final 4 pendant les deux heures.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Des bases à la modélisation (4/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-7-label">7. Dans le modèle de refroidissement T(t)=T_amb+(T0−T_amb)e^(−kt), vers quelle valeur T(t) se rapproche-t-elle ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-7-label">
<label class="qcm-choice" for="qcm-fondamentaux-7-a"><input id="qcm-fondamentaux-7-a" type="radio" name="qcm-fondamentaux-7" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Quand t grandit, e^(−kt) diminue et tend vers zéro."><span>A. La température initiale T0.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-7-b"><input id="qcm-fondamentaux-7-b" type="radio" name="qcm-fondamentaux-7" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Le terme exponentiel tend vers zéro ; il reste T_amb."><span>B. La température ambiante T_amb.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-7-c"><input id="qcm-fondamentaux-7-c" type="radio" name="qcm-fondamentaux-7" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Quand t grandit, e^(−kt) diminue et tend vers zéro."><span>C. Zéro dans tous les cas.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-7-d"><input id="qcm-fondamentaux-7-d" type="radio" name="qcm-fondamentaux-7" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le modèle tend vers la température ambiante, pas vers la température de départ."><span>D. La température initiale T0.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-fondamentaux-8-label">8. Après la transformation logarithmique du refroidissement, que représente la pente de la droite ajustée ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-fondamentaux-8-label">
<label class="qcm-choice" for="qcm-fondamentaux-8-a"><input id="qcm-fondamentaux-8-a" type="radio" name="qcm-fondamentaux-8" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Repère le signe devant kt dans l’expression transformée."><span>A. k.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-8-b"><input id="qcm-fondamentaux-8-b" type="radio" name="qcm-fondamentaux-8" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="ln(T−T_amb)=ln(T0−T_amb)−kt : la pente est −k."><span>B. −k.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-8-c"><input id="qcm-fondamentaux-8-c" type="radio" name="qcm-fondamentaux-8" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Repère le signe devant kt dans l’expression transformée."><span>C. T_amb.</span></label>
<label class="qcm-choice" for="qcm-fondamentaux-8-d"><input id="qcm-fondamentaux-8-d" type="radio" name="qcm-fondamentaux-8" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La pente vaut −k ; l’ordonnée à l’origine sert à retrouver T0."><span>D. L’ordonnée à l’origine de la droite transformée vaut directement k.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>
