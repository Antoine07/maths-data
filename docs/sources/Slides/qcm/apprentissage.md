---
marp: true
theme: default
paginate: true
class: lead
---

# QCM de réactivation
## Analyse et apprentissage

**8 questions pour réactiver les notions du bloc.** Répondez ensemble, puis cliquez sur une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.

---

## QCM de réactivation · Analyse et apprentissage (1/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>1. Pour une fonction de plusieurs paramètres, que contient le gradient ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 1">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le gradient rassemble les sensibilités de la fonction à chacun de ses paramètres.">A. Les dérivées partielles par rapport à chaque paramètre.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Chaque composante décrit la variation selon un paramètre.">B. Les prédictions du modèle seulement.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Chaque composante décrit la variation selon un paramètre.">C. Les étiquettes de classe.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>2. Dans une étape de descente de gradient, dans quelle direction déplace-t-on les paramètres ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 2">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le gradient indique la montée locale ; son opposé vise une baisse de l’objectif.">A. Dans la direction opposée au gradient.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le gradient pointe vers l’augmentation locale de la fonction.">B. Toujours vers des paramètres plus grands.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Le gradient pointe vers l’augmentation locale de la fonction.">C. Dans une direction tirée au hasard.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Analyse et apprentissage (2/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>3. Un gradient nul prouve-t-il que l’on a trouvé un minimum ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 3">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Une pente nulle seule ne précise pas la forme autour du point.">A. Oui, toujours.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Un point stationnaire peut avoir plusieurs natures ; il faut étudier la courbure ou le voisinage.">B. Non ; cela peut aussi être un maximum ou un point selle.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Une pente nulle seule ne précise pas la forme autour du point.">C. Non ; un gradient ne peut jamais être nul.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>4. Que fait la rétropropagation dans un réseau ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 4">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Elle propage les dérivées de la sortie vers les paramètres des couches.">A. Elle calcule les gradients en appliquant la règle de chaîne.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="La rétropropagation calcule les gradients ; l’optimiseur met ensuite les paramètres à jour.">B. Elle choisit les données de test.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="La rétropropagation calcule les gradients ; l’optimiseur met ensuite les paramètres à jour.">C. Elle remplace la fonction de perte.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Analyse et apprentissage (3/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>5. Quelle est la valeur de la sigmoïde pour un logit nul ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 5">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Remplace z par zéro dans 1/(1+e^(−z)).">A. 0.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="σ(0)=1/(1+e⁰)=1/2.">B. 0,5.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Remplace z par zéro dans 1/(1+e^(−z)).">C. 1.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>6. Pourquoi ajouter une activation non linéaire entre deux couches affines ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 6">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Sans activation, plusieurs transformations affines se composent encore en une transformation affine.">A. Pour permettre au réseau de représenter des relations non linéaires.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Deux couches linéaires sans activation restent équivalentes à une seule couche linéaire.">B. Pour garantir une exactitude de 100 %.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Deux couches linéaires sans activation restent équivalentes à une seule couche linéaire.">C. Pour supprimer le besoin de données.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---

## QCM de réactivation · Analyse et apprentissage (4/4)

<div class="qcm-review">
<p class="qcm-intro">Répondez à deux questions, puis choisissez une proposition pour afficher le feedback. En cas d’erreur, vous pouvez réessayer.</p>
<div class="qcm-question" data-qcm-question>
<h3>7. Un réseau réussit très bien sur l’entraînement mais mal sur des données nouvelles. Quel problème observe-t-on ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 7">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le modèle a appris trop précisément les exemples d’entraînement et se généralise mal.">A. Le surapprentissage.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Compare les performances sur apprentissage et sur données tenues à l’écart.">B. Une meilleure généralisation.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Compare les performances sur apprentissage et sur données tenues à l’écart.">C. Une covariance nulle.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
<div class="qcm-question" data-qcm-question>
<h3>8. Pourquoi garder un jeu de test à l’écart pendant le choix du modèle ?</h3>
<div class="qcm-options" role="group" aria-label="Réponses à la question 8">
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="true" data-qcm-feedback="Le test final donne une évaluation moins biaisée par les décisions de réglage.">A. Pour estimer la performance sur des données qui n’ont pas servi aux choix.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Si le test guide les choix, il n’est plus indépendant de l’apprentissage du modèle.">B. Pour augmenter artificiellement la taille de l’entraînement.</button>
<button type="button" class="qcm-option" data-qcm-option data-qcm-correct="false" data-qcm-feedback="Si le test guide les choix, il n’est plus indépendant de l’apprentissage du modèle.">C. Pour calculer les gradients plus vite.</button>
</div>
<p class="qcm-feedback" data-qcm-feedback role="status" aria-live="polite" hidden></p>
</div>
</div>

---
