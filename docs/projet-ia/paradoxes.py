"""Six problèmes pédagogiques et leurs contrôles numériques. NumPy suffit.

Exécuter : python3 paradoxes.py
Tous les nombres décrivent des scénarios fictifs ou des modèles explicités.
"""
import json
import numpy as np


def minutes_quotidiennes(minutes=10, annees=20, jours_par_an=365):
    heures = minutes * jours_par_an * annees / 60
    return {'heures': heures, 'journees_16h': heures/16}


def simpson():
    # Lignes : formations A et B ; colonnes : débutants et confirmés.
    reussites = np.array([[18, 9], [5, 24]])
    effectifs = np.array([[30, 10], [10, 30]])
    taux = reussites/effectifs
    globaux = reussites.sum(axis=1)/effectifs.sum(axis=1)
    communs = taux @ np.array([.5, .5])
    return taux, globaux, communs


def attente_bus(tailles=(2., 18.)):
    intervalles = np.asarray(tailles, dtype=float)
    if np.any(intervalles <= 0):
        raise ValueError('Les intervalles doivent être strictement positifs')
    # Observation uniforme dans le temps sur une suite périodique.
    poids = intervalles/intervalles.sum()
    return float(poids @ (intervalles/2))


def disponibilite(n=10, p=.8, dates=1):
    ensemble = p**n  # Hypothèse d'indépendance entre personnes.
    au_moins_une = 1 - (1-ensemble)**dates  # Aussi entre dates.
    return ensemble, au_moins_une


def braess():
    demande = 4000
    moitie = demande/2
    avant = moitie/100 + 45
    apres = demande/100 + demande/100
    deviation = demande/100 + 45
    return {'avant_minutes': avant, 'apres_minutes': apres,
            'deviation_individuelle_minutes': deviation,
            'augmentation_relative': (apres-avant)/avant}


def alertes(population=100000, prevalence=.001, sensibilite=.99, faux_positifs=.01):
    anomalies = population*prevalence
    normaux = population-anomalies
    vp = anomalies*sensibilite
    fn = anomalies-vp
    fp = normaux*faux_positifs
    vn = normaux-fp
    return {'vrais_positifs': vp, 'faux_negatifs': fn,
            'faux_positifs': fp, 'vrais_negatifs': vn,
            'precision': vp/(vp+fp), 'rappel': sensibilite,
            'exactitude': (vp+vn)/population,
            'reference_toujours_normal': 1-prevalence}


def verifier():
    minutes = minutes_quotidiennes()
    assert np.isclose(minutes['heures'], 1216+2/3)
    taux, globaux, communs = simpson()
    assert np.all(taux[0] > taux[1]) and globaux[0] < globaux[1]
    np.testing.assert_allclose(communs, [.75, .65])
    assert np.isclose(attente_bus(), 8.2)
    assert np.isclose(attente_bus([10, 10]), 5)
    groupe, quatre = disponibilite(dates=4)
    assert np.isclose(groupe, .1073741824)
    assert groupe < quatre < 4*groupe
    route = braess()
    assert route['avant_minutes'] == 65 and route['apres_minutes'] == 80
    assert route['deviation_individuelle_minutes'] > route['apres_minutes']
    detection = alertes()
    assert detection['vrais_positifs'] == 99 and detection['faux_positifs'] == 999
    assert np.isclose(detection['exactitude'], .99)
    assert .09 < detection['precision'] < .091
    rng = np.random.default_rng(42)
    instants = rng.uniform(0, 20, 200000)
    attentes = np.where(instants < 2, 2-instants, 20-instants)
    assert abs(attentes.mean()-8.2) < .04
    groupes = rng.random((100000, 10)) < .8
    assert abs(groupes.all(axis=1).mean()-groupe) < .004
    return {'minutes': minutes, 'simpson': {'par_groupe': taux.tolist(), 'global': globaux.tolist(), 'population_commune': communs.tolist()},
            'bus': {'theorie_minutes': attente_bus(), 'simulation_minutes': float(attentes.mean())},
            'diner': {'une_date': groupe, 'au_moins_une_sur_quatre': quatre},
            'braess': route, 'alertes': detection}


if __name__ == '__main__':
    print(json.dumps(verifier(), ensure_ascii=False, indent=2))
