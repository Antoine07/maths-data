# Rencontres — Correction NumPy et Matplotlib

`rencontres_numpy.py` contient le corrigé complet du problème « La moitié des années, combien de rencontres ? ». Il construit les tableaux, calcule les deux scénarios et les six fréquences, puis affiche une figure à deux panneaux.

Exécuter dans l'environnement Python du cours, avec NumPy et Matplotlib :

```sh
python rencontres_numpy.py
```

La correction utilise 30 ans comme âge actuel et 60 ans comme horizon fixé. Les fréquences sont des hypothèses de scénario. Les longueurs des blocs suivent les paramètres d'âge ; leur adaptation suppose `18 <= age_actuel < age_fin`.

`generer_figures.py` exécute le même corrigé sans ouvrir de fenêtre et enregistre le SVG publié dans `docs/assets/images/`. Depuis la racine du projet :

```sh
python docs/exemples/rencontres/generer_figures.py
```

L'aperçu PNG va dans `/tmp/rencontres-numpy/` ; `MATHS_RENCONTRES_PREVIEWS` permet de choisir un autre dossier.
