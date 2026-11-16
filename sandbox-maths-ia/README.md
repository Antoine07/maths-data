# Sandbox Maths & IA

Environnement JupyterLab minimal avec Python, NumPy, pandas et Matplotlib.

Depuis ce dossier :

```sh
docker compose up --build
```

Ouvrir <http://localhost:8889/lab>. Aucun mot de passe ni jeton n'est demandé ; le port est lié à `127.0.0.1` et n'est donc accessible que depuis la machine locale.

Pour arrêter le conteneur :

```sh
docker compose down
```
