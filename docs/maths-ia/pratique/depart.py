"""Faire évoluer ce même fichier pendant les huit séances."""
from parcours import charger, PARTITIONS

X, consommation, jours = charger()
print(X.shape, consommation.shape)

# S1-A : décrire les colonnes et écrire une prédiction X @ w + b.
# S1-B : décrire les données et dériver une perte à un paramètre.
# S1-Michel : écrire la propagation avant d'un réseau ; aucun entraînement ici.
# S2-A : ajuster moyenne et échelle sur train uniquement.
# S2-B : calculer puis contrôler un gradient par différences finies.
# S2-C : expérimenter la descente et la pénalité, sans consulter test.
# S2-Michel-2 : entraîner avec PyTorch et choisir les réglages sur validation.
# S2-Michel-3 : figer les modèles puis rédiger le bilan de généralisation.
