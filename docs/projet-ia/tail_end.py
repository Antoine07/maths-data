"""Quatre problèmes originaux autour des occasions restantes. NumPy suffit.

Scénarios fictifs à horizon fixé ; aucune estimation individuelle de durée de vie.
Exécuter : python3 tail_end.py
"""
import json
import numpy as np


def rencontres(frequence_future=12):
    enfance = 18 * 300
    adulte = (30 - 18) * 12
    passe = enfance + adulte
    futur = (60 - 30) * frequence_future
    return {"passe": passe, "futur": futur, "total": passe + futur,
            "part_future": futur / (passe + futur)}


def frequence(t):
    return 24 * np.exp(-.05 * np.asarray(t))


def cumul(t):
    # Une primitive fixée par C(0)=0. Unités : occasions attendues.
    return 480 * (1 - np.exp(-.05 * np.asarray(t)))


def demi_horizon(horizon=30.):
    return float(-np.log((1 + np.exp(-.05 * horizon)) / 2) / .05)


def tableau_activites():
    # Six semaines fictives : sessions vidéo et rencontres avec un proche.
    return np.column_stack([np.arange(10., 22., 2.), [0., 0., 0., 0., 0., 1.]])


def acp_rare():
    x = tableau_activites()
    moyenne = x.mean(axis=0)
    centre = x - moyenne
    _, s, vt = np.linalg.svd(centre, full_matrices=False)
    reconstruit = (centre @ vt[:1].T) @ vt[:1] + moyenne
    ratio = s**2 / np.sum(s**2)
    return x, reconstruit, ratio


def score(x, y, poids_visites=3., poids_amis=2.):
    # Préférences posées pour l'exercice, pas mesure du bonheur.
    return poids_visites * np.log1p(x) + poids_amis * np.log1p(y)


def planning():
    x_continu = 7.1
    y_continu = 24 - 2*x_continu
    x = np.arange(13)
    y = 24 - 2*x
    valeurs = score(x, y)
    i = int(np.argmax(valeurs))
    return {"continu": [x_continu, y_continu], "entier": [int(x[i]), int(y[i])],
            "score_entier": float(valeurs[i])}


def verifier():
    base, double = rencontres(), rencontres(24)
    assert base['passe'] == 5544 and base['futur'] == 360
    assert double['passe'] == base['passe'] and double['futur'] == 720
    t = np.array([0., 5., 15., 30.])
    eps = 1e-5
    np.testing.assert_allclose((cumul(t + eps) - cumul(t - eps))/(2*eps), frequence(t), rtol=1e-8)
    np.testing.assert_allclose(cumul(demi_horizon()), cumul(30)/2, atol=1e-10)
    x, reconstruction, parts = acp_rare()
    assert parts[0] > .99
    assert reconstruction[-1, 1] < .75 and x[-1, 1] == 1
    assert planning()['entier'] == [7, 10]
    return {"probleme_1": {"base": base, "frequence_doublee": double},
            "probleme_2": {"cumul_30": float(cumul(30)), "demi_horizon": demi_horizon(),
                           "reference_constante": 24*30},
            "probleme_3": {"parts_variance": parts.tolist(),
                           "reconstruction_rencontre_semaine_6": float(reconstruction[-1, 1])},
            "probleme_4": planning()}


if __name__ == '__main__':
    print(json.dumps(verifier(), ensure_ascii=False, indent=2))
