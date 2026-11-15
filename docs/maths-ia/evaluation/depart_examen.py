"""Fichier étudiant : compléter les trois fonctions sans modifier les données.

Les vérifications fournies contrôlent les formes ; elles ne remplacent pas
les calculs et interprétations demandés sur la copie.
"""
from pathlib import Path
import numpy as np


def charger():
    data = np.genfromtxt(Path(__file__).parent / 'donnees_examen.csv', delimiter=',', names=True)
    X = np.column_stack([data['temperature'], data['occupation']])
    return X, data['consommation']


def predire(X, w, b):
    raise NotImplementedError('À compléter : une prédiction par ligne')


def mse(predictions, y):
    raise NotImplementedError('À compléter : erreur quadratique moyenne')


def decider(probabilites):
    raise NotImplementedError('À compléter : seuil de probabilité inclus à 0,5')


def verifier_contrats():
    X, y = charger()
    w, b = np.array([2., 1.]), 3.
    predictions = predire(X, w, b)
    assert predictions.shape == y.shape
    assert np.ndim(mse(predictions, y)) == 0
    p = np.array([.2, .7, .4, .9])
    decisions = decider(p)
    assert decisions.shape == p.shape
    assert np.isin(decisions, [0, 1]).all()
    print('Contrats de formes vérifiés ; justifier aussi les valeurs et les interprétations.')


if __name__ == '__main__':
    verifier_contrats()
