---
marp: true
theme: default
paginate: true
class: lead
---

# QCM de réactivation
## Analyse et apprentissage

**8 questions pour réactiver les notions du bloc.** Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ». Le feedback explique la réponse ; après une erreur, vous pouvez modifier votre choix et réessayer.

---

## QCM de réactivation · Analyse et apprentissage (1/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-1-label">1. Pour une fonction de plusieurs paramètres, que contient le gradient ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-1-label">
<label class="qcm-choice" for="qcm-apprentissage-1-a"><input id="qcm-apprentissage-1-a" type="radio" name="qcm-apprentissage-1" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Le gradient rassemble les sensibilités de la fonction à chacun de ses paramètres."><span>A. Les dérivées partielles par rapport à chaque paramètre.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-1-b"><input id="qcm-apprentissage-1-b" type="radio" name="qcm-apprentissage-1" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Chaque composante décrit la variation selon un paramètre."><span>B. Les prédictions du modèle seulement.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-1-c"><input id="qcm-apprentissage-1-c" type="radio" name="qcm-apprentissage-1" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Chaque composante décrit la variation selon un paramètre."><span>C. Les étiquettes de classe.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-1-d"><input id="qcm-apprentissage-1-d" type="radio" name="qcm-apprentissage-1" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le gradient rassemble une dérivée partielle par paramètre."><span>D. La dérivée par rapport au premier paramètre seulement.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-2-label">2. Dans une étape de descente de gradient, dans quelle direction déplace-t-on les paramètres ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-2-label">
<label class="qcm-choice" for="qcm-apprentissage-2-a"><input id="qcm-apprentissage-2-a" type="radio" name="qcm-apprentissage-2" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Le gradient indique la montée locale ; son opposé vise une baisse de l’objectif."><span>A. Dans la direction opposée au gradient.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-2-b"><input id="qcm-apprentissage-2-b" type="radio" name="qcm-apprentissage-2" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le gradient pointe vers l’augmentation locale de la fonction."><span>B. Toujours vers des paramètres plus grands.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-2-c"><input id="qcm-apprentissage-2-c" type="radio" name="qcm-apprentissage-2" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Le gradient pointe vers l’augmentation locale de la fonction."><span>C. Dans une direction tirée au hasard.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-2-d"><input id="qcm-apprentissage-2-d" type="radio" name="qcm-apprentissage-2" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Pour faire décroître localement l’objectif, on se déplace dans la direction opposée."><span>D. Dans la direction du gradient.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Analyse et apprentissage (2/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-3-label">3. Un gradient nul prouve-t-il que l’on a trouvé un minimum ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-3-label">
<label class="qcm-choice" for="qcm-apprentissage-3-a"><input id="qcm-apprentissage-3-a" type="radio" name="qcm-apprentissage-3" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Une pente nulle seule ne précise pas la forme autour du point."><span>A. Oui, toujours.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-3-b"><input id="qcm-apprentissage-3-b" type="radio" name="qcm-apprentissage-3" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Un point stationnaire peut avoir plusieurs natures ; il faut étudier la courbure ou le voisinage."><span>B. Non ; cela peut aussi être un maximum ou un point selle.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-3-c"><input id="qcm-apprentissage-3-c" type="radio" name="qcm-apprentissage-3" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Une pente nulle seule ne précise pas la forme autour du point."><span>C. Non ; un gradient ne peut jamais être nul.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-3-d"><input id="qcm-apprentissage-3-d" type="radio" name="qcm-apprentissage-3" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Un gradient nul peut aussi correspondre à un maximum ou à un point selle."><span>D. Oui, un gradient nul correspond toujours au minimum global.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-4-label">4. Que fait la rétropropagation dans un réseau ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-4-label">
<label class="qcm-choice" for="qcm-apprentissage-4-a"><input id="qcm-apprentissage-4-a" type="radio" name="qcm-apprentissage-4" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Elle propage les dérivées de la sortie vers les paramètres des couches."><span>A. Elle calcule les gradients en appliquant la règle de chaîne.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-4-b"><input id="qcm-apprentissage-4-b" type="radio" name="qcm-apprentissage-4" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La rétropropagation calcule les gradients ; l’optimiseur met ensuite les paramètres à jour."><span>B. Elle choisit les données de test.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-4-c"><input id="qcm-apprentissage-4-c" type="radio" name="qcm-apprentissage-4" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La rétropropagation calcule les gradients ; l’optimiseur met ensuite les paramètres à jour."><span>C. Elle remplace la fonction de perte.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-4-d"><input id="qcm-apprentissage-4-d" type="radio" name="qcm-apprentissage-4" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="La rétropropagation calcule les gradients ; l’optimiseur effectue les mises à jour."><span>D. Elle met directement à jour les poids du modèle.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Analyse et apprentissage (3/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-5-label">5. Quelle est la valeur de la sigmoïde pour un logit nul ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-5-label">
<label class="qcm-choice" for="qcm-apprentissage-5-a"><input id="qcm-apprentissage-5-a" type="radio" name="qcm-apprentissage-5" value="A" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Remplace z par zéro dans 1/(1+e^(−z))."><span>A. 0.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-5-b"><input id="qcm-apprentissage-5-b" type="radio" name="qcm-apprentissage-5" value="B" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="σ(0)=1/(1+e⁰)=1/2."><span>B. 0,5.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-5-c"><input id="qcm-apprentissage-5-c" type="radio" name="qcm-apprentissage-5" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Remplace z par zéro dans 1/(1+e^(−z))."><span>C. 1.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-5-d"><input id="qcm-apprentissage-5-d" type="radio" name="qcm-apprentissage-5" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Pour z=0, la sigmoïde vaut 1/(1+1)=0,5."><span>D. 1.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-6-label">6. Pourquoi ajouter une activation non linéaire entre deux couches affines ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-6-label">
<label class="qcm-choice" for="qcm-apprentissage-6-a"><input id="qcm-apprentissage-6-a" type="radio" name="qcm-apprentissage-6" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Sans activation, plusieurs transformations affines se composent encore en une transformation affine."><span>A. Pour permettre au réseau de représenter des relations non linéaires.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-6-b"><input id="qcm-apprentissage-6-b" type="radio" name="qcm-apprentissage-6" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Deux couches linéaires sans activation restent équivalentes à une seule couche linéaire."><span>B. Pour garantir une exactitude de 100 %.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-6-c"><input id="qcm-apprentissage-6-c" type="radio" name="qcm-apprentissage-6" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Deux couches linéaires sans activation restent équivalentes à une seule couche linéaire."><span>C. Pour supprimer le besoin de données.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-6-d"><input id="qcm-apprentissage-6-d" type="radio" name="qcm-apprentissage-6" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Une activation non linéaire permet de représenter des relations non linéaires ; toutes les activations ne bornent pas la sortie."><span>D. Pour garantir une sortie entre 0 et 1.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Analyse et apprentissage (4/4)

<div class="qcm-review">
<p class="qcm-intro">Choisissez une seule réponse parmi A, B, C et D, puis cliquez sur « Valider ».</p>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-7-label">7. Un réseau réussit très bien sur l’entraînement mais mal sur des données nouvelles. Quel problème observe-t-on ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-7-label">
<label class="qcm-choice" for="qcm-apprentissage-7-a"><input id="qcm-apprentissage-7-a" type="radio" name="qcm-apprentissage-7" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Le modèle a appris trop précisément les exemples d’entraînement et se généralise mal."><span>A. Le surapprentissage.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-7-b"><input id="qcm-apprentissage-7-b" type="radio" name="qcm-apprentissage-7" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Compare les performances sur apprentissage et sur données tenues à l’écart."><span>B. Une meilleure généralisation.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-7-c"><input id="qcm-apprentissage-7-c" type="radio" name="qcm-apprentissage-7" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Compare les performances sur apprentissage et sur données tenues à l’écart."><span>C. Une covariance nulle.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-7-d"><input id="qcm-apprentissage-7-d" type="radio" name="qcm-apprentissage-7" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Une bonne performance à l’entraînement et mauvaise sur de nouvelles données indiquent un surapprentissage."><span>D. Le sous-apprentissage.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3 id="qcm-apprentissage-8-label">8. Pourquoi garder un jeu de test à l’écart pendant le choix du modèle ?</h3>
<div class="qcm-options" role="radiogroup" aria-labelledby="qcm-apprentissage-8-label">
<label class="qcm-choice" for="qcm-apprentissage-8-a"><input id="qcm-apprentissage-8-a" type="radio" name="qcm-apprentissage-8" value="A" data-qcm-answer data-qcm-correct="true" data-qcm-feedback="Le test final donne une évaluation moins biaisée par les décisions de réglage."><span>A. Pour estimer la performance sur des données qui n’ont pas servi aux choix.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-8-b"><input id="qcm-apprentissage-8-b" type="radio" name="qcm-apprentissage-8" value="B" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Si le test guide les choix, il n’est plus indépendant de l’apprentissage du modèle."><span>B. Pour augmenter artificiellement la taille de l’entraînement.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-8-c"><input id="qcm-apprentissage-8-c" type="radio" name="qcm-apprentissage-8" value="C" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Si le test guide les choix, il n’est plus indépendant de l’apprentissage du modèle."><span>C. Pour calculer les gradients plus vite.</span></label>
<label class="qcm-choice" for="qcm-apprentissage-8-d"><input id="qcm-apprentissage-8-d" type="radio" name="qcm-apprentissage-8" value="D" data-qcm-answer data-qcm-correct="false" data-qcm-feedback="Les paramètres se règlent sur l’entraînement ou la validation ; le test reste réservé à l’évaluation finale."><span>D. Pour choisir les meilleurs paramètres du modèle.</span></label>
</div>
<button type="button" class="qcm-submit" data-qcm-submit>Valider</button>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---
