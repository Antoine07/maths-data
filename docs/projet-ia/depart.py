"""Point de départ : faire évoluer ce fichier au fil des six chapitres."""
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
data = np.genfromtxt(BASE / "data/consommation.csv", delimiter=",", names=True)
X = np.column_stack([data[k] for k in ("temperature", "occupation", "equipements")])
y = data["consommation"]
train, validation, test = slice(0, 144), slice(144, 192), slice(192, 240)
print("Données :", X.shape, y.shape)

# Jalon 1 : définir une distance et comparer des journées sans utiliser y.
# Jalon 2 : ajouter la constante et résoudre les moindres carrés sur train.
# Jalon 3 : après le cours de statistiques, standardiser et réaliser la SVD.
# Atelier clustering après le jalon 3 : comparer k=2,3,4 avec clustering.py.
# Jalon 4 : écrire la perte et son gradient, puis les vérifier numériquement.
# Jalon 5 : entraîner, choisir lambda sur validation et figer les paramètres.
# Jalon 6 : classifier les journées, comparer au modèle de référence sur test.
