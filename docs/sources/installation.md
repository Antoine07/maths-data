# Stacks

*Lisez bien tout pour choisir une méthode d'installation*

1. **Télécharger Python**
2. **Environnement virtuel**
3. **Jupyter & JupyterLab**
4. **Alternative : Google Colab**

---


# Télécharger Python

Téléchargez la dernière version :  
[python.org/downloads](https://www.python.org/downloads/)

![w:600](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

---

# Créer un environnement virtuel

```bash
python -m venv env_dataops
````

Activez-le selon votre système :

**Windows**

```bash
env_dataops\Scripts\activate
```

**Mac / Linux**

```bash
source env_dataops/bin/activate
```

---

# Installer Jupyter et JupyterLab

![w:100](https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg)

```bash
pip install --upgrade pip
pip install notebook jupyterlab
```

Lancez JupyterLab :

```bash
jupyter lab
```

Pour sortir :

```bash
deactivate
```

# Organisation de travail avec la virtualisation

```txt
project_data/
│
├── env_dataops/          ←  environnement virtuel
│
├── requirements.txt      ← liste des dépendances du projet
├── main.py               ← point d'entrée principal du programme
│
├── mon_projet/           ← dossier du code source (ton “package”)
│   ├── models/           ← tes classes ou structures de données
│   │   └── user.py
│   └── utils/            ← fonctions utilitaires
│       └── helpers.py
│
└── tests/                ← tes fichiers de test
    └── test_user.py
```

---

# En cas de problème d'installation

Alternative en ligne sans installation : [Google Colab](https://colab.research.google.com)

---

# Alternative Docker

Vous pouvez sinon utiliser le docker-compose suivant 

```yaml
services:

  jupyter:
    image: jupyter/base-notebook:latest
    environment:
      JUPYTER_ENABLE_LAB: "yes"
      GRANT_SUDO: "yes"
      PYTHONPATH: "/home/jovyan/work/src"
    user: root
    ports:
      - "8880:8888"
      - "8000:8000"
    volumes:
      - ./project:/home/jovyan/work
    working_dir: /home/jovyan/work
    command: >
      bash -c "
      pip install -r /home/jovyan/work/config/requirements.txt &&
      start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''
      "
    restart: always

  fastapi:
    image: jupyter/base-notebook:latest
    user: root
    ports:
      - "8001:8000"
    volumes:
      - ./project:/home/jovyan/work
    working_dir: /home/jovyan/work/src
    command: >
      bash -c "
      pip install -r /home/jovyan/work/config/requirements.txt &&
      uvicorn main:app --host 0.0.0.0 --port 8000 --reload
      "
    restart: always
```

Fichier `requirements.txt`

```txt
numpy
sympy
matplotlib
scipy
pandas
fastapi
uvicorn
python-multipart
```

