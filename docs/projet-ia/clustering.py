"""Atelier après le jalon 3 : k-means en NumPy sur les mêmes journées simulées.

Exécution : python3 clustering.py. Aucun accès à la consommation ni au test.
"""
from pathlib import Path
import numpy as np


def distances_carrees(X, centres):
    """Une ligne par observation, une colonne par centre."""
    return np.sum((X[:, None, :] - centres[None, :, :]) ** 2, axis=2)


def affecter(X, centres):
    """À égalité, choisir le premier centre (convention explicite)."""
    return np.argmin(distances_carrees(X, centres), axis=1)


def lloyd(X, centres, max_iter=100):
    """Alterner affectation et moyenne ; garder le centre d'un cluster vide.

    À la limite d'itérations, les étiquettes correspondent aux centres retournés,
    mais ces centres ne sont pas nécessairement les moyennes de ces étiquettes.
    Le champ converge permet de distinguer ce cas d'un point fixe.
    """
    X, centres = np.asarray(X, dtype=float), np.array(centres, dtype=float, copy=True)
    if (X.ndim != 2 or centres.ndim != 2 or len(X) == 0 or len(centres) == 0
            or X.shape[1] == 0 or X.shape[1] != centres.shape[1]
            or not np.isfinite(X).all() or not np.isfinite(centres).all()):
        raise ValueError("Matrices finies, non vides et de même nombre de colonnes requises")
    if not isinstance(max_iter, (int, np.integer)) or max_iter < 1:
        raise ValueError("max_iter doit être un entier positif")
    labels = affecter(X, centres)
    historique = [float(np.sum((X - centres[labels]) ** 2))]
    converge = False
    for iteration in range(1, max_iter + 1):
        nouveaux = centres.copy()
        for j in range(len(centres)):
            membres = X[labels == j]
            if len(membres):
                nouveaux[j] = membres.mean(axis=0)
        nouveaux_labels = affecter(X, nouveaux)
        historique.append(float(np.sum((X - nouveaux[nouveaux_labels]) ** 2)))
        converge = np.array_equal(labels, nouveaux_labels)
        centres, labels = nouveaux, nouveaux_labels
        if converge:
            break
    return dict(centres=centres, labels=labels, inertie=historique[-1],
                historique=np.array(historique), iterations=iteration, converge=converge)


def kmeans(X, k, graine=0, n_init=10, max_iter=100):
    """Garder la plus faible inertie parmi n_init départs reproductibles."""
    X = np.asarray(X, dtype=float)
    if X.ndim != 2 or not len(X) or not X.shape[1] or not np.isfinite(X).all():
        raise ValueError("X doit être une matrice finie non vide")
    uniques = np.unique(X, axis=0)
    if not isinstance(k, (int, np.integer)) or not 1 <= k <= len(uniques):
        raise ValueError("k doit être compris entre 1 et le nombre de points distincts")
    if not isinstance(n_init, (int, np.integer)) or n_init < 1:
        raise ValueError("n_init doit être un entier positif")
    rng = np.random.default_rng(graine)
    candidats = [lloyd(X, uniques[rng.choice(len(uniques), k, replace=False)], max_iter)
                 for _ in range(n_init)]
    return min(candidats, key=lambda resultat: resultat['inertie'])


def atelier():
    data = np.genfromtxt(Path(__file__).parent / 'data/consommation.csv',
                         delimiter=',', names=True)
    # Même ordre de colonnes et mêmes partitions que depart.py.
    X = np.column_stack([data[nom] for nom in ('temperature', 'occupation', 'equipements')])
    apprentissage, validation = X[:144], X[144:192]
    moyenne, ecart = apprentissage.mean(0), apprentissage.std(0)
    echelle = np.where(ecart > 0, ecart, 1.)
    Z, V = (apprentissage - moyenne) / echelle, (validation - moyenne) / echelle
    bilans = []
    for k in (2, 3, 4):
        modele = kmeans(Z, k, graine=7)
        labels_validation = affecter(V, modele['centres'])
        erreur_validation = np.mean(np.min(distances_carrees(V, modele['centres']), axis=1))
        centres_unites = modele['centres'] * echelle + moyenne
        print(f"k={k} ; inertie train={modele['inertie']:.3f} ; "
              f"distance carrée moyenne validation={erreur_validation:.3f}")
        print('Effectifs train / validation :', np.bincount(modele['labels'], minlength=k),
              np.bincount(labels_validation, minlength=k))
        print('Centres : température (°C), occupation, équipements')
        print(np.round(centres_unites, 2))
        bilans.append(dict(k=k, modele=modele, labels_validation=labels_validation,
                           centres_unites=centres_unites, erreur_validation=erreur_validation))
    print("Comparer les profils et les graines ; une faible inertie ne prouve pas des catégories naturelles.")
    return bilans


if __name__ == '__main__':
    atelier()
