"""Un même jeu de données simulées, du modèle linéaire au réseau PyTorch.

NumPy suffit pour les premières séances. PyTorch n'est importé que pour
l'entraînement. Lancer : python parcours.py --entrainer
"""
from pathlib import Path
import argparse
import copy
import json
import numpy as np

COLONNES = ('temperature', 'occupation', 'equipements')
PARTITIONS = {'train': slice(0, 144), 'validation': slice(144, 192), 'test': slice(192, 240)}


def charger():
    data = np.genfromtxt(Path(__file__).parent / 'data/consommation.csv', delimiter=',', names=True)
    X = np.column_stack([data[c] for c in COLONNES])
    return X, data['consommation'], data['jour'].astype(int)


def ajuster_echelle(X):
    moyenne, ecart = X.mean(axis=0), X.std(axis=0)
    return moyenne, np.where(ecart > 0, ecart, 1.)


def preparer():
    X, y, jours = charger()
    moyenne, echelle = ajuster_echelle(X[PARTITIONS['train']])
    seuil = float(np.median(y[PARTITIONS['train']]))
    Z = (X - moyenne) / echelle
    classes = (y >= seuil).astype(float)
    return dict(X=X, y=y, jours=jours, Z=Z, classes=classes,
                moyenne=moyenne, echelle=echelle, seuil=seuil)


def predire_lineaire(X, poids, biais):
    return np.asarray(X) @ np.asarray(poids) + biais


def mse(predictions, cibles):
    predictions, cibles = np.asarray(predictions), np.asarray(cibles)
    if predictions.shape != cibles.shape:
        raise ValueError('Prédictions et cibles doivent avoir la même forme')
    return float(np.mean((predictions - cibles)**2))


def sigmoide(logits):
    return np.exp(-np.logaddexp(0., -np.asarray(logits)))


def passage_numpy(Z, W1, b1, W2, b2):
    cache = Z @ W1 + b1
    H = np.maximum(cache, 0.)
    logits = (H @ W2 + b2).reshape(-1)
    return H, logits, sigmoide(logits)


def metriques(classes, predictions):
    classes, predictions = np.asarray(classes, dtype=int), np.asarray(predictions, dtype=int)
    if classes.shape != predictions.shape:
        raise ValueError('Une décision est nécessaire pour chaque observation')
    matrice = np.zeros((2, 2), dtype=int)
    for vrai, predit in zip(classes, predictions):
        matrice[vrai, predit] += 1
    tn, fp, fn, tp = matrice.ravel()
    return {'matrice_confusion': matrice.tolist(),
            'exactitude': float(np.mean(classes == predictions)),
            'precision': float(tp/(tp+fp)) if tp+fp else None,
            'rappel': float(tp/(tp+fn)) if tp+fn else None}


def entrainer(Z, classes, architecture='reseau', pas=.1, penalite=0., graine=7,
              iterations=600, patience=80):
    """Sélection des itérations par validation ; aucun accès aux données de test."""
    import torch
    from torch import nn
    torch.set_num_threads(1)
    torch.manual_seed(graine)
    if architecture not in ('logistique', 'reseau'):
        raise ValueError('Architecture inconnue')
    modele = nn.Linear(3, 1) if architecture == 'logistique' else nn.Sequential(
        nn.Linear(3, 4), nn.ReLU(), nn.Linear(4, 1))
    train, validation = PARTITIONS['train'], PARTITIONS['validation']
    x_train = torch.tensor(Z[train], dtype=torch.float32)
    x_val = torch.tensor(Z[validation], dtype=torch.float32)
    y_train = torch.tensor(classes[train, None], dtype=torch.float32)
    y_val = torch.tensor(classes[validation, None], dtype=torch.float32)
    perte = nn.BCEWithLogitsLoss()
    groupes = [{'params': [p for p in modele.parameters() if p.ndim > 1], 'weight_decay': penalite},
               {'params': [p for p in modele.parameters() if p.ndim == 1], 'weight_decay': 0.}]
    optimiseur = torch.optim.SGD(groupes, lr=pas)
    meilleur, etat, meilleure_iteration, trace = float('inf'), None, 0, []
    for iteration in range(1, iterations+1):
        modele.train()
        optimiseur.zero_grad()
        cout = perte(modele(x_train), y_train)
        cout.backward()
        optimiseur.step()
        modele.eval()
        with torch.no_grad():
            cout_train = float(perte(modele(x_train), y_train))
            cout_val = float(perte(modele(x_val), y_val))
        trace.append((iteration, cout_train, cout_val))
        if cout_val < meilleur - 1e-7:
            meilleur, meilleure_iteration = cout_val, iteration
            etat = copy.deepcopy(modele.state_dict())
        if iteration - meilleure_iteration >= patience:
            break
    modele.load_state_dict(etat)
    modele.eval()
    return dict(modele=modele, perte_validation=meilleur, iteration=meilleure_iteration,
                trace=np.asarray(trace), architecture=architecture, pas=pas,
                penalite=penalite, graine=graine)


def probabilites(modele, Z):
    import torch
    modele.eval()
    with torch.no_grad():
        return torch.sigmoid(modele(torch.tensor(Z, dtype=torch.float32))).numpy().reshape(-1)


def experience():
    """Grille annoncée à l'avance ; deux modèles figés comparés au bilan final."""
    data = preparer()
    candidats = [entrainer(data['Z'], data['classes'], architecture='logistique', pas=.1)]
    candidats += [entrainer(data['Z'], data['classes'], pas=pas, penalite=.001)
                  for pas in (.01, .05, .1)]
    meilleurs = {nom: min((c for c in candidats if c['architecture'] == nom),
                         key=lambda c: c['perte_validation'])
                 for nom in ('logistique', 'reseau')}
    # Le test intervient seulement après ces choix. Il ne choisit ni modèle ni seuil.
    test = PARTITIONS['test']
    majoritaire = int(data['classes'][PARTITIONS['train']].mean() >= .5)
    bilan = {'seuil_consommation_train': data['seuil'],
             'reference_majoritaire': metriques(data['classes'][test],
                                                np.full(48, majoritaire))}
    for nom, resultat in meilleurs.items():
        p = probabilites(resultat['modele'], data['Z'][test])
        bilan[nom] = {k: resultat[k] for k in ('iteration', 'pas', 'penalite', 'perte_validation')}
        bilan[nom].update(metriques(data['classes'][test], p >= .5))
    return bilan, meilleurs


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--entrainer', action='store_true')
    options = parser.parse_args()
    donnees = preparer()
    print('X :', donnees['X'].shape, '; seuil appris :', round(donnees['seuil'], 3))
    if options.entrainer:
        bilan, _ = experience()
        print(json.dumps(bilan, ensure_ascii=False, indent=2))
