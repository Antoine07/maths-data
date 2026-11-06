"""Fil rouge exécutable : six jalons sur les mêmes données et partitions.

Lancer : python3 correction.py --verifier
NumPy suffit. Les résultats JSON sont écrits à côté de ce fichier.
"""
import argparse
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent


def charger():
    data = np.genfromtxt(BASE / "data/consommation.csv", delimiter=",", names=True)
    # Les trois variables sont disponibles au moment où l'on veut prédire.
    x = np.column_stack([data[k] for k in ("temperature", "occupation", "equipements")])
    y = data["consommation"]
    # Ordre chronologique : apprentissage, validation, test final réservé.
    return x, y, (slice(0, 144), slice(144, 192), slice(192, 240))


def ajuster_echelle(x):
    moyenne, ecart = x.mean(axis=0), x.std(axis=0)
    return moyenne, np.where(ecart < 1e-12, 1.0, ecart)


def ajouter_biais(x):
    return np.column_stack([np.ones(len(x)), x])


def rmse(prediction, cible):
    return float(np.sqrt(np.mean((prediction - cible) ** 2)))


def bilan_classification(prediction, cible):
    confusion = np.zeros((2, 2), dtype=int)
    np.add.at(confusion, (cible.astype(int), prediction.astype(int)), 1)
    rappels = [float(confusion[c, c] / confusion[c].sum()) if confusion[c].sum() else None for c in (0, 1)]
    return {"confusion_lignes_reelles_colonnes_predites": confusion.tolist(),
            "rappel_par_classe": rappels,
            "exactitude": float(np.mean(prediction == cible))}


def cout_gradient(a, y, theta, penalite=0.0):
    """J = ||A theta-y||²/(2n) + penalite ||theta[1:]||²/2."""
    residu = a @ theta - y
    reg = theta.copy()
    reg[0] = 0.0  # La constante n'est pas pénalisée.
    cout = np.mean(residu ** 2) / 2 + penalite * np.dot(reg, reg) / 2
    gradient = a.T @ residu / len(y) + penalite * reg
    return float(cout), gradient


def differences_finies(fonction, point, epsilon=1e-5):
    gradient = np.empty_like(point, dtype=float)
    for j in range(len(point)):
        delta = np.zeros_like(point, dtype=float)
        delta[j] = epsilon
        gradient[j] = (fonction(point + delta) - fonction(point - delta)) / (2 * epsilon)
    return gradient


def descente(a, y, penalite=0.0, iterations=2500, lot=None):
    theta = np.zeros(a.shape[1])
    masque = np.diag([0.0] + [1.0] * (a.shape[1] - 1))
    h = a.T @ a / len(y) + penalite * masque
    pas = 0.8 / np.linalg.eigvalsh(h)[-1]
    rng = np.random.default_rng(17)
    historique = []
    for _ in range(iterations):
        indices = rng.permutation(len(y)) if lot else np.arange(len(y))
        taille = lot or len(y)
        for debut in range(0, len(y), taille):
            ix = indices[debut:debut + taille]
            _, gradient = cout_gradient(a[ix], y[ix], theta, penalite)
            theta -= pas * gradient
        historique.append(cout_gradient(a, y, theta, penalite)[0])
    return theta, np.array(historique), float(pas)


def ridge(a, y, penalite):
    # Forme augmentée résolue par lstsq : aucune inversion explicite.
    d = np.diag([0.0] + [1.0] * (a.shape[1] - 1))
    augmente = np.vstack([a, np.sqrt(len(y) * penalite) * d])
    cible = np.concatenate([y, np.zeros(a.shape[1])])
    return np.linalg.lstsq(augmente, cible, rcond=None)[0]


def sigmoide(z):
    return np.exp(-np.logaddexp(0, -z))


def logistique_cout_gradient(a, y, theta):
    logits = a @ theta
    cout = np.mean(np.logaddexp(0, logits) - y * logits)
    gradient = a.T @ (sigmoide(logits) - y) / len(y)
    return float(cout), gradient


def reseau_cout_gradients(x, y, parametres):
    w1, b1, w2, b2 = parametres
    cache = np.tanh(x @ w1 + b1)
    logits = (cache @ w2 + b2).ravel()
    cout = np.mean(np.logaddexp(0, logits) - y * logits)
    dz2 = (sigmoide(logits) - y)[:, None] / len(y)
    dw2 = cache.T @ dz2
    db2 = dz2.sum(axis=0)
    dz1 = (dz2 @ w2.T) * (1 - cache ** 2)
    dw1 = x.T @ dz1
    db1 = dz1.sum(axis=0)
    return float(cout), (dw1, db1, dw2, db2)


def initialiser_reseau(p, h=4):
    rng = np.random.default_rng(7)
    return [rng.normal(0, .2, (p, h)), np.zeros(h),
            rng.normal(0, .2, (h, 1)), np.zeros(1)]


def entrainer_classification(x, y, xv, yv):
    # Même nombre maximal d'itérations, sélection sur la perte de validation.
    a, av = ajouter_biais(x), ajouter_biais(xv)
    theta = np.zeros(a.shape[1])
    params = initialiser_reseau(x.shape[1])
    meilleur_lineaire = (float("inf"), None, 0)
    meilleur_reseau = (float("inf"), None, 0)
    for etape in range(2000):
        _, g = logistique_cout_gradient(a, y, theta)
        theta -= .08 * g
        _, gs = reseau_cout_gradients(x, y, params)
        params = [v - .08 * g for v, g in zip(params, gs)]
        perte_l = logistique_cout_gradient(av, yv, theta)[0]
        perte_r = reseau_cout_gradients(xv, yv, params)[0]
        if perte_l < meilleur_lineaire[0]:
            meilleur_lineaire = (perte_l, theta.copy(), etape + 1)
        if perte_r < meilleur_reseau[0]:
            meilleur_reseau = (perte_r, [v.copy() for v in params], etape + 1)
    return meilleur_lineaire, meilleur_reseau


def verifier_mathematiques():
    a = np.array([[1., 0.], [1., 1.], [1., 2.]])
    y = np.array([1., 2., 2.])
    theta = np.array([.3, -.2])
    analytique = cout_gradient(a, y, theta, .1)[1]
    numerique = differences_finies(lambda t: cout_gradient(a, y, t, .1)[0], theta)
    np.testing.assert_allclose(analytique, numerique, atol=1e-8)
    optimum = ridge(a, y, .1)
    solution, historique, _ = descente(a, y, .1)
    np.testing.assert_allclose(solution, optimum, atol=1e-7)
    assert np.all(np.diff(historique) <= 1e-10)
    binaire = np.array([0., 1., 1.])
    np.testing.assert_allclose(
        logistique_cout_gradient(a, binaire, theta)[1],
        differences_finies(lambda t: logistique_cout_gradient(a, binaire, t)[0], theta),
        atol=1e-8)
    params = initialiser_reseau(2)
    x = np.array([[.1, .3], [-.4, .2], [.2, -.1]])
    _, gradients = reseau_cout_gradients(x, binaire, params)
    # Toutes les coordonnées des quatre tenseurs sont vérifiées.
    for index, (parametre, gradient) in enumerate(zip(params, gradients)):
        def perte(v):
            copie = [p.copy() for p in params]
            copie[index] = v.reshape(parametre.shape)
            return reseau_cout_gradients(x, binaire, copie)[0]
        estime = differences_finies(perte, parametre.ravel()).reshape(parametre.shape)
        np.testing.assert_allclose(gradient, estime, atol=1e-8)
    # Rappel : un vecteur nul n'a pas de similarité cosinus définie.
    v = np.array([3., 4.])
    assert np.isclose(np.linalg.norm(v), 5)
    m = np.array([[3., 0.], [0., 1.]])
    u, s, vt = np.linalg.svd(m, full_matrices=False)
    approximation = (u[:, :1] * s[:1]) @ vt[:1]
    assert np.isclose(np.linalg.norm(m - approximation, "fro") ** 2, s[1] ** 2)
    print("Vérifications : gradients, rétropropagation, convergence et SVD OK.")


def main(verifier=False):
    if verifier:
        verifier_mathematiques()
    x, y, (train, validation, test) = charger()
    moyenne, ecart = ajuster_echelle(x[train])
    z = (x - moyenne) / ecart
    a = ajouter_biais(z)
    # Jalon 1 : chercher une journée similaire dans l'apprentissage.
    normes = np.linalg.norm(z[train], axis=1)
    requete = z[validation][0]
    scores = z[train] @ requete / (np.maximum(normes, 1e-12) * np.linalg.norm(requete))
    # Jalon 2 : régression et diagnostic de rang.
    ols, _, rang, singulieres = np.linalg.lstsq(a[train], y[train], rcond=None)
    # Jalon 3 : ACP par SVD, ajustée seulement sur l'apprentissage.
    u, s, vt = np.linalg.svd(z[train], full_matrices=False)
    ratio = s ** 2 / np.sum(s ** 2)
    k = int(np.searchsorted(np.cumsum(ratio), .95) + 1)
    reconstruit = (z[validation] @ vt[:k].T) @ vt[:k]
    # Jalon 4 : vérifier le gradient de la perte du modèle précédent.
    point = np.zeros(a.shape[1])
    numerique = differences_finies(lambda t: cout_gradient(a[train], y[train], t)[0], point)
    ecart_gradient = float(np.max(np.abs(numerique - cout_gradient(a[train], y[train], point)[1])))
    # Jalon 5 : choisir lambda sur la validation, puis figer le modèle.
    candidats = [0., .001, .01, .1, 1.]
    evaluations = [(rmse(a[validation] @ ridge(a[train], y[train], l), y[validation]), l) for l in candidats]
    _, penalite = min(evaluations)
    choisi = ridge(a[train], y[train], penalite)
    gd, historique, pas = descente(a[train], y[train], penalite)
    # Jalon 6 : même problème, nouvelle cible : journée à forte consommation.
    seuil = float(np.median(y[train]))
    classes = (y > seuil).astype(float)
    lineaire, reseau = entrainer_classification(z[train], classes[train], z[validation], classes[validation])
    # Le test intervient ici, une fois les choix et paramètres figés.
    pred_l = sigmoide(a[test] @ lineaire[1]) >= .5
    w1, b1, w2, b2 = reseau[1]
    pred_r = sigmoide((np.tanh(z[test] @ w1 + b1) @ w2 + b2).ravel()) >= .5
    majoritaire = int(np.mean(classes[train]) > .5)
    rapport = {
        "donnees": "240 journées simulées ; aucune mesure réelle",
        "partitions": {"apprentissage": 144, "validation": 48, "test": 48},
        "jalon_1": {"jour_similaire": int(np.argmax(scores) + 1), "cosinus": float(scores.max())},
        "jalon_2": {"rang": int(rang), "conditionnement": float(singulieres[0] / singulieres[-1]), "rmse_validation": rmse(a[validation] @ ols, y[validation])},
        "jalon_3": {"variance_expliquee": ratio.tolist(), "k_95": k, "erreur_reconstruction_validation": float(np.mean((z[validation] - reconstruit) ** 2))},
        "jalon_4": {"ecart_gradient_max": ecart_gradient},
        "jalon_5": {"lambda": penalite, "pas": pas, "cout_initial": float(historique[0]), "cout_final": float(historique[-1]), "ecart_gd_ridge": float(np.linalg.norm(gd - choisi)), "rmse_test": rmse(a[test] @ choisi, y[test]), "rmse_reference_test": rmse(np.full(48, y[train].mean()), y[test])},
        "jalon_6": {"seuil_kwh": seuil, "effectifs_classes": {nom: np.bincount(classes[ix].astype(int), minlength=2).tolist() for nom, ix in [("apprentissage", train), ("validation", validation), ("test", test)]}, "reference": bilan_classification(np.full(len(pred_l), majoritaire), classes[test]), "logistique": bilan_classification(pred_l, classes[test]), "reseau": bilan_classification(pred_r, classes[test]), "iterations_logistique": lineaire[2], "iterations_reseau": reseau[2]}
    }
    if verifier:
        assert len(x) == 240 and a.shape == (240, 4)
        assert ecart_gradient < 1e-7
        np.testing.assert_allclose(gd, choisi, atol=1e-6)
        np.testing.assert_allclose(z[train].mean(axis=0), 0, atol=1e-12)
        assert not np.shares_memory(x[train], x[test])
    dossier = BASE / "resultats"
    dossier.mkdir(exist_ok=True)
    (dossier / "bilan.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2) + "\n")
    np.savez(dossier / "modeles.npz", moyenne=moyenne, ecart=ecart, theta=choisi, axes=vt[:k], w1=w1, b1=b1, w2=w2, b2=b2)
    print(json.dumps(rapport, ensure_ascii=False, indent=2))
    return rapport


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verifier", action="store_true")
    main(parser.parse_args().verifier)
