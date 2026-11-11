# Graphiques de modélisation

Quatre figures accompagnent le chapitre « Modéliser la consommation » : ajustement linéaire et prévision, comparaison linéaire/quadratique, différences d'ordre quatre et ajustement logarithmique.

Le script `generer_figures.py` produit les SVG publiés dans `docs/assets/images/`, des aperçus PNG et le manifeste `figures.json`. Il utilise NumPy et Matplotlib. Depuis la sandbox du dépôt :

```sh
docker compose -f sandbox_jupyter/docker-compose.yml exec jupyterlab python /workspace/docs/exemples/modelisation/generer_figures.py
```

Les jeux de données sont des exemples pédagogiques. Le graphique de prévision distingue les 30 valeurs utilisées pour l'ajustement du prolongement jusqu'au jour 40.
