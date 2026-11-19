from pathlib import Path

import numpy as np
import pandas as pd


# Télécharger le jeu de données Penguins.
url = "https://raw.githubusercontent.com/Antoine07/maths-data/main/docs/data/penguins.csv"
df = pd.read_csv(url)

# Garder deux espèces et les deux mesures utilisées par le modèle.
caracteristiques = ["bill_length_mm", "flipper_length_mm"]
codes_especes = {"Adelie": 1, "Gentoo": 0}
colonnes_utiles = caracteristiques + ["species"]

donnees = df.loc[
    df["species"].isin(codes_especes), colonnes_utiles
].dropna().copy()

# Transformer les noms d'espèce en classes numériques.
donnees["species"] = donnees["species"].map(codes_especes).astype(int)
donnees = donnees.rename(columns={"species": "target"})

# Séparer les caractéristiques X de la cible y.
X = donnees[caracteristiques].to_numpy(dtype=float)
y = donnees["target"].to_numpy(dtype=int)

# Enregistrer le tableau nettoyé à côté de ce script.
fichier_sortie = Path(__file__).with_name("penguins_nettoye.csv")
donnees.to_csv(fichier_sortie, index=False)

print("Lignes conservées :", len(donnees))
print("Dimensions de X :", X.shape)
print("Dimensions de y :", y.shape)
print("Effectifs des classes :")
print(donnees["target"].value_counts().sort_index())
print("Fichier enregistré :", fichier_sortie)
