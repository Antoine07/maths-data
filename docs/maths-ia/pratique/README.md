# Projet fil rouge — Consommation simulée

Les 240 journées sont simulées et reprennent le fil rouge du cours. Les colonnes d'entrée sont température, occupation et équipements. La consommation n'est jamais une entrée du classificateur.

Partitions : jours 1–144 pour apprendre, 145–192 pour choisir les réglages, 193–240 pour le bilan final. Le seuil de forte consommation est la médiane de la seule consommation d'apprentissage. Les échelles sont apprises sur les seules entrées d'apprentissage. La saisonnalité simulée change les distributions entre partitions : le rapport doit le commenter.

Faire évoluer `depart.py` et le même notebook. `parcours.py` fournit les utilitaires et une réalisation de référence à étudier après les exercices. La correction d'examen n'est pas dans ce dossier.

## Exécuter

Dans un environnement Python : `python -m pip install -r requirements.txt`, puis `python parcours.py --entrainer`. Aucun GPU n'est nécessaire.

Dans la sandbox existante, installer PyTorch pour le noyau Python avec `python -m pip install --user torch==2.7.1`. Les bibliothèques NumPy et Matplotlib y sont déjà disponibles. Après une installation dans une session Jupyter déjà ouverte, redémarrer le noyau Python. Une installation faite dans le conteneur sera à refaire après sa recréation ; pour la conserver dans l'image, ajouter PyTorch aux dépendances de construction.

L'installation PyTorch CPU peut également se faire avec l'index officiel : `python -m pip install --user torch==2.7.1 --index-url https://download.pytorch.org/whl/cpu`.

## Livrables

- Un notebook progressivement enrichi, relançable du début à la fin.
- Dimensions, unités, partitions et transformations explicites.
- Calculs manuels et contrôle d'au moins un gradient.
- Courbes d'apprentissage et de validation ; réglages choisis avant le test.
- Référence majoritaire, logistique et petit réseau comparés avec des métriques définies.
- Une conclusion sur les erreurs, les limites et l'absence de garantie de supériorité du réseau.
