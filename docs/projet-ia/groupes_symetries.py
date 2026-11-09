"""Atelier transversal : rotations et permutation des lignes du même projet.

Exécution : python3 groupes_symetries.py. NumPy uniquement.
"""
from pathlib import Path
import numpy as np


def verifier():
    R = np.array([[0, -1], [1, 0]])
    I = np.eye(2, dtype=int)
    rotations = [np.linalg.matrix_power(R, k) for k in range(4)]
    assert np.array_equal(np.linalg.matrix_power(R, 4), I)
    for a in range(4):
        for b in range(4):
            assert np.array_equal(rotations[a] @ rotations[b], rotations[(a + b) % 4])
        assert np.array_equal(rotations[a] @ rotations[(-a) % 4], I)
    x, z = np.array([3., 4.]), np.array([1., 0.])
    assert np.isclose(np.linalg.norm(R @ x - R @ z), np.linalg.norm(x - z))
    # Le projecteur horizontal n'est pas équivariant à ces rotations.
    P = np.diag([1., 0.])
    assert not np.allclose(P @ R @ x, R @ P @ x)

    data = np.genfromtxt(Path(__file__).parent / 'data/consommation.csv',
                         delimiter=',', names=True)
    X = np.column_stack([data[nom] for nom in ('temperature', 'occupation', 'equipements')])[:144]
    y = data['consommation'][:144]
    # Poids de démonstration figés : ce n'est pas un modèle ajusté.
    poids = np.array([-2., 3., 4.])
    predire = lambda valeurs: valeurs @ poids + 10.
    permutation = np.random.default_rng(7).permutation(len(X))
    retour = np.argsort(permutation)
    predictions = predire(X)
    permutees = predire(X[permutation])
    assert np.allclose(permutees, predictions[permutation])
    assert np.allclose(permutees[retour], predictions)
    erreur = np.mean((predictions - y) ** 2)
    erreur_alignee = np.mean((permutees - y[permutation]) ** 2)
    assert np.isclose(erreur, erreur_alignee)
    erreur_desalignee = np.mean((permutees - y) ** 2)
    assert not np.isclose(erreur, erreur_desalignee)
    print('C4 : composition et inverses vérifiés ; distances conservées.')
    print('Prédictions équivariantes ; erreur moyenne invariante si les cibles suivent.')
    print(f'Erreur alignée={erreur:.3f} ; cibles désalignées={erreur_desalignee:.3f}')
    return dict(erreur=erreur, erreur_alignee=erreur_alignee, erreur_desalignee=erreur_desalignee)


if __name__ == '__main__':
    verifier()
