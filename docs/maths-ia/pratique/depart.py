"""Faire évoluer ce même fichier au fil des chapitres."""
from parcours import charger, PARTITIONS

X, consommation, jours = charger()
print(X.shape, consommation.shape)

# Chapitre 1 : décrire les colonnes et écrire une prédiction X @ w + b.
# Chapitre 2 : décrire les données et dériver une perte à un paramètre.
# Chapitre 3 : écrire la propagation avant d'un réseau ; aucun entraînement ici.
# Chapitre 4 : ajuster moyenne et échelle sur train uniquement.
# Chapitre 5 : calculer puis contrôler un gradient par différences finies.
# Chapitre 6 : expérimenter la descente et la pénalité, sans consulter test.
# Chapitre 7 : entraîner avec PyTorch et choisir les réglages sur validation.
# Chapitre 8 : figer les modèles puis rédiger le bilan de généralisation.
