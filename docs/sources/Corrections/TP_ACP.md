```python

import numpy as np

# -----------------------------
# 1. Données
# -----------------------------
X = np.array([
    [160, 55],
    [170, 65],
    [172, 68],
    [180, 80],
    [175, 75],
    [158, 50]
], dtype=float)

print("Données initiales :\n", X)
print("-" * 50)

# -----------------------------
# 2. Centrage des données
# -----------------------------
mean = np.mean(X, axis=0)
X_centered = X - mean

print("Moyennes :", mean)
print("Données centrées :\n", np.round(X_centered, 2))
print("-" * 50)

# -----------------------------
# 3. Matrice de covariance
# -----------------------------
C = np.cov(X_centered, rowvar=False)

print("Matrice de covariance :\n", np.round(C, 2))
print("-" * 50)

# -----------------------------
# 4. Valeurs propres / vecteurs propres
# -----------------------------
eigenvalues, eigenvectors = np.linalg.eig(C)

# Trier par importance décroissante
idx = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

print("Valeurs propres (variance expliquée) :\n", eigenvalues)
print("Vecteurs propres (directions principales) :\n", eigenvectors)
print("-" * 50)

# Pourcentage de variance expliquée
variance_ratio = eigenvalues / np.sum(eigenvalues)
print("Proportion de variance expliquée :", variance_ratio)
print("-" * 50)


# -----------------------------
# 5. Projection des données
# -----------------------------
X_projected = X_centered @ eigenvectors

print("Données projetées sur les nouvelles composantes :\n", np.round(X_projected, 2))
print("-" * 50)


print("=== Interprétation ===")

print("\nPC1 (1ère composante) explique {:.1f}% de la variance."
      .format(variance_ratio[0] * 100))

print("C’est la direction :", np.round(eigenvectors[:, 0], 3))

if variance_ratio[0] > 0.85:
    print("→ Les données sont presque entièrement alignées sur une seule direction.")
    print("→ On peut résumer la taille + poids par une seule composante.")
else:
    print("→ Il faut au moins 2 composantes pour bien représenter les données.")

# Exemple d'analyse simple
print("\nProjection sur PC1 :")
print(np.round(X_projected[:, 0], 2))
print("→ Ce score indique la « corpulence globale » de chaque individu.")
```

✔ Les données sont centrées (moyenne = 0).

✔ La covariance taille-poids est positive (elles montent ensemble).

✔ PC1 explique la majorité de la variance (souvent >90%).

✔ PC1 ≈ combinaison linéaire taille+poids → “gabarit général”.

✔ PC2 ≈ différence taille/poids → “silhouette plus ou moins élancée”.

✔ La projection simplifie l’analyse sur une seule dimension.