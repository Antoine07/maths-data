# Graphiques des fonctions et température simulée

Sept figures SVG accompagnent les chapitres « Fonctions périodiques » et « Comprendre la dérivée ». La variante maths-ia réutilise les figures des extrema et de la température.

- `temperature_simulee.py` : expérience reproductible, comparaison des périodes 24 et 12 h, statistiques du bruit. Avec NumPy et Matplotlib : `python temperature_simulee.py`.
- `generer_figures.py` : régénère les sept SVG dans `docs/assets/images/`, leurs aperçus PNG dans `/tmp/maths-fonctions/` et le manifeste `figures.json`. Si le dossier de travail `Slides/images/` existe, les SVG y sont aussi recopiés.
- `verifier.py` : contrôle avec NumPy les calculs présentés, les périodes, le paramétrage du bruit, les figures et le code de l'exercice publié. À lancer après la génération des pages : `python docs/exemples/fonctions/verifier.py` depuis la racine du dépôt.

Dans la sandbox du projet :

```sh
docker compose -f sandbox_jupyter/docker-compose.yml exec jupyterlab python /workspace/docs/exemples/fonctions/generer_figures.py
docker compose -f sandbox_jupyter/docker-compose.yml exec jupyterlab python /workspace/docs/exemples/fonctions/verifier.py
```

Les graphiques illustrent des calculs, sans remplacer leurs démonstrations. Les températures sont simulées ; le choix d'un cycle sinusoïdal et d'un bruit gaussien ne constitue pas un modèle météorologique validé.
