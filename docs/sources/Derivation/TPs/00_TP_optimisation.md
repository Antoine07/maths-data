## Problème de data — Modéliser la croissance d'une audience sur un réseau social

Une influenceuse observe le nombre d'abonnés à son compte chaque mois.
Les données montrent une croissance rapide au début, puis un ralentissement.

Un modèle simple utilisé en data est :

$$
A(t) = 1000\ln(t+1),
\qquad t \ge 0
$$

où :
	•	t = temps en mois,
	•	A(t) = nombre d'abonnés prédits par le modèle.

Cette fonction représente une croissance qui ralentit progressivement, phénomène très courant en data.

---

1. Questions mathématiques

a) Étudier le signe de la dérivée de A(t)

$$
A(t)=1000\ln(t+1)
$$

---

b) Étudier A''(t) pour comprendre la dynamique

Interprétez

---

2. Question data : À quel moment la croissance devient-elle “lentement significative” ?

On considère qu'un mois est "faiblement intéressant" si le compte gagne moins de 50 abonnés.

---
