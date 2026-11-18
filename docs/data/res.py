"""Squelette étudiant : perceptron binaire pour les données des manchots.

Compléter la mise à jour des poids et du biais avant d'entraîner le modèle.
"""

import numpy as np


def fonction_escalier(score):
    """Renvoie 1 si le score est positif ou nul, 0 sinon."""
    return int(score >= 0)


def entrainer(X, y, eta=0.1, nb_epoques=10):
    """Entraîne un perceptron et garde une trace des poids et des erreurs."""
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=int)

    poids = np.zeros(X.shape[1])
    biais = 0.0
    historique = []
    erreurs_par_epoque = []

    for epoque in range(nb_epoques):
        erreurs = 0

        for i in range(len(X)):
            xi = X[i]
            score = xi @ poids + biais
            classe_reelle = y[i]
            classe_predite = fonction_escalier(score)
            erreur = classe_reelle - classe_predite

            if erreur != 0:
                # TODO : remplacer la ligne d'arrêt par la mise à jour des poids.
                # Indice : w_nouveau = w + eta * erreur * xi
                # TODO : mettre à jour le biais avec eta et erreur.
                # Indice : b_nouveau = b + eta * erreur
                raise NotImplementedError("Complète les deux mises à jour")
                erreurs += 1

            historique.append(poids.copy())

            # Afficher quelques exemples pour suivre les premières corrections.
            if epoque == 0 and i < 5:
                print(
                    f"manchot {i + 1} | score={score:.3f} | "
                    f"cible={classe_reelle} | prédiction={classe_predite} | "
                    f"poids={poids} | biais={biais:.3f}"
                )

        erreurs_par_epoque.append(erreurs)
        print(f"Époque {epoque + 1} : {erreurs} erreur(s)")

    return poids, biais, np.asarray(historique), erreurs_par_epoque


def predire(X, poids, biais):
    """Renvoie les classes prédites pour plusieurs observations."""
    X = np.asarray(X, dtype=float)
    scores = X @ poids + biais
    return np.array([fonction_escalier(score) for score in scores])
