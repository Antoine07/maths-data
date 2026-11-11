"""Graphiques reproductibles du chapitre « Modéliser la consommation »."""

from pathlib import Path
import json
import os
import shutil

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "docs" / "assets" / "images"
PREVIEWS = Path(os.environ.get("MATHS_MODELISATION_PREVIEWS", "/tmp/modelisation-apercus"))
SLIDES_IMAGES = ROOT / "Slides" / "images"
OUT.mkdir(parents=True, exist_ok=True)
PREVIEWS.mkdir(parents=True, exist_ok=True)

GREEN = "#275c47"
PURPLE = "#80659b"
ORANGE = "#b46a43"
INK = "#203b36"
MUTED = "#63716a"
GRID = "#dce2d9"
BG = "#f7f8f2"

plt.rcParams.update(
    {
        "figure.facecolor": BG,
        "axes.facecolor": "white",
        "axes.edgecolor": GRID,
        "axes.labelcolor": INK,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "grid.color": GRID,
        "grid.alpha": 0.7,
        "axes.axisbelow": True,
        "legend.frameon": False,
        "legend.fontsize": 9,
        "svg.fonttype": "path",
        "svg.hashsalt": "coda-modelisation-consommation",
    }
)

FIGURES = []


def save(name, fig, title, description):
    fig.suptitle(title, x=0.055, y=0.98, ha="left", fontsize=17, fontweight="bold")
    fig.text(0.056, 0.925, description, color=MUTED, fontsize=9)
    fig.tight_layout(rect=(0.035, 0.07, 0.98, 0.88), pad=1.4)
    target = OUT / f"{name}.svg"
    fig.savefig(
        target,
        metadata={"Title": title, "Description": description, "Date": None},
    )
    target.write_text(
        "\n".join(line.rstrip() for line in target.read_text(encoding="utf-8").splitlines()) + "\n",
        encoding="utf-8",
    )
    fig.savefig(PREVIEWS / f"{name}.png", dpi=130)
    plt.close(fig)
    if SLIDES_IMAGES.is_dir():
        shutil.copyfile(target, SLIDES_IMAGES / target.name)
    FIGURES.append({"file": target.name, "title": title, "description": description})


# Exercice 1 : données observées, droite ajustée et extrapolation au jour 40.
C = np.array(
    [
        9.5, 9.7, 9.8, 10.0, 10.3, 10.4, 10.6, 10.8, 11.0, 11.3,
        11.4, 11.5, 11.7, 12.0, 12.1, 12.4, 12.6, 12.7, 12.9, 13.0,
        13.2, 13.4, 13.5, 13.7, 13.9, 14.0, 14.1, 14.3, 14.5, 14.6,
    ]
)
t = np.arange(1, len(C) + 1)
a, b = np.polyfit(t, C, 1)
prediction = a * 40 + b
fig, ax = plt.subplots(figsize=(11.8, 5.8))
ax.scatter(t, C, color=GREEN, s=38, label="Mesures simulées, jours 1 à 30", zorder=3)
ax.plot(t, a * t + b, color=PURPLE, linewidth=2.7, label="Droite ajustée sur les 30 jours")
future = np.linspace(30, 40, 100)
ax.plot(future, a * future + b, color=ORANGE, linewidth=2.2, linestyle="--", label="Prolongement du modèle")
ax.axvline(30, color=GRID, linewidth=1.2, linestyle=":")
ax.scatter([40], [prediction], color=ORANGE, s=70, zorder=4)
ax.annotate(
    f"Jour 40 : {prediction:.1f} kWh/jour",
    (40, prediction),
    xytext=(-12, 16),
    textcoords="offset points",
    ha="right",
    color=ORANGE,
    fontweight="bold",
)
ax.set(
    xlabel="Jour t",
    ylabel="Consommation quotidienne (kWh)",
    xlim=(0, 42),
    ylim=(8.5, 17.4),
    title="La droite décrit les données ; son prolongement est une prévision",
    xticks=[1, 10, 20, 30, 40],
)
ax.grid(True, linewidth=0.7)
ax.legend(loc="upper left", ncol=2)
save(
    "modelisation-consommation-lineaire",
    fig,
    "Une tendance linéaire et sa limite",
    "Exemple simulé : les jours 1 à 30 servent à ajuster le modèle. Le point au jour 40 est une extrapolation, pas une mesure.",
)

# Modèle quadratique : comparaison des ajustements et lecture des différences.
T = np.array([9.5, 9.7, 10.0, 10.4, 10.9, 11.3, 12.0, 12.8, 13.7, 14.8, 16.0, 17.3, 18.7, 20.2, 21.8])
days = np.arange(1, len(T) + 1)
linear = np.poly1d(np.polyfit(days, T, 1))
quadratic = np.poly1d(np.polyfit(days, T, 2))
dense = np.linspace(1, len(T), 300)
second_diff = np.diff(T, n=2)
fig, (fit_ax, diff_ax) = plt.subplots(1, 2, figsize=(12.2, 5.8), gridspec_kw={"width_ratios": [1.45, 1]})
fit_ax.scatter(days, T, color=GREEN, s=34, label="Données", zorder=3)
fit_ax.plot(dense, linear(dense), color=ORANGE, linestyle="--", linewidth=2, label="Ajustement linéaire")
fit_ax.plot(dense, quadratic(dense), color=PURPLE, linewidth=2.7, label="Ajustement quadratique")
fit_ax.set(xlabel="Indice du jour", ylabel="Valeur observée", title="Une courbure apparaît")
fit_ax.grid(True, linewidth=0.7)
fit_ax.legend()
diff_indices = np.arange(2, len(T))
diff_ax.axhline(second_diff.mean(), color=ORANGE, linestyle="--", linewidth=1.8,
                label=f"Moyenne : {second_diff.mean():.2f}")
diff_ax.scatter(diff_indices, second_diff, color=PURPLE, s=38, label="Deuxièmes différences")
diff_ax.set(xlabel="Indice", ylabel="Δ²T", title="Valeurs proches, pas identiques")
diff_ax.grid(True, linewidth=0.7)
diff_ax.legend()
save(
    "modelisation-quadratique",
    fig,
    "Comparer une droite et une parabole",
    "Les deuxièmes différences sont globalement proches d’une constante. Les valeurs arrondies ne sont pas parfaitement régulières.",
)

# Exercice 2 : les différences d'ordre quatre sont presque constantes.
y_poly = np.array([5.00, 6.32, 9.28, 14.40, 22.30, 33.60, 48.92, 69.00, 94.60, 126.52, 165.60])
x_poly = np.arange(1, len(y_poly) + 1)
poly4 = np.poly1d(np.polyfit(x_poly, y_poly, 4))
fourth_diff = np.diff(y_poly, n=4)
fig, (poly_ax, diff_ax) = plt.subplots(1, 2, figsize=(12.2, 5.8), gridspec_kw={"width_ratios": [1.45, 1]})
poly_x = np.linspace(1, len(y_poly), 300)
poly_ax.scatter(x_poly, y_poly, color=GREEN, s=38, label="Données", zorder=3)
poly_ax.plot(poly_x, poly4(poly_x), color=PURPLE, linewidth=2.7, label="Ajustement de degré 4")
poly_ax.set(xlabel="Indice", ylabel="Valeur y", title="Un polynôme de degré 4 suit les points")
poly_ax.grid(True, linewidth=0.7)
poly_ax.legend()
diff_ax.axhline(fourth_diff.mean(), color=ORANGE, linestyle="--", linewidth=1.8,
                label=f"Moyenne : {fourth_diff.mean():.3f}")
diff_ax.scatter(np.arange(1, len(fourth_diff) + 1), fourth_diff, color=PURPLE, s=40,
                label="Quatrièmes différences")
diff_ax.set(xlabel="Indice", ylabel="Δ⁴y", title="Les écarts sont approximatifs")
diff_ax.grid(True, linewidth=0.7)
diff_ax.legend()
save(
    "modelisation-polynome",
    fig,
    "Les différences finies aident à choisir un degré",
    "Les valeurs y sont arrondies à deux décimales ; les quatrièmes différences sont proches d’une constante, sans être identiques.",
)

# Exercice 3 : ajustement logarithmique et transformation de l'abscisse.
t_log = np.arange(1, 10)
y_log = np.array([2.1, 2.9, 3.4, 3.8, 4.1, 4.3, 4.5, 4.6, 4.7])
coef_log = np.polyfit(np.log(t_log), y_log, 1)
log_model = lambda x: coef_log[0] * np.log(x) + coef_log[1]
smooth_t = np.linspace(1, 9, 300)
fig, (curve_ax, transformed_ax) = plt.subplots(1, 2, figsize=(12.2, 5.8), gridspec_kw={"width_ratios": [1.2, 1]})
curve_ax.scatter(t_log, y_log, color=GREEN, s=38, label="Données", zorder=3)
curve_ax.plot(smooth_t, log_model(smooth_t), color=PURPLE, linewidth=2.7, label="a ln(t) + b")
curve_ax.set(xlabel="Temps t", ylabel="Valeur y", title="La croissance ralentit")
curve_ax.grid(True, linewidth=0.7)
curve_ax.legend()
log_t = np.log(t_log)
transformed_ax.scatter(log_t, y_log, color=GREEN, s=38, label="Données transformées", zorder=3)
transformed_ax.plot(log_t, np.polyval(coef_log, log_t), color=PURPLE, linewidth=2.4, label="Ajustement linéaire")
transformed_ax.set(xlabel="ln(t)", ylabel="Valeur y", title="La transformation rend la relation linéaire")
transformed_ax.grid(True, linewidth=0.7)
transformed_ax.legend()
save(
    "modelisation-logarithmique",
    fig,
    "Passer d’une courbe logarithmique à une droite",
    "Le modèle y = a ln(t) + b s’ajuste en traçant y en fonction de ln(t). Le logarithme impose t > 0.",
)

(Path(__file__).parent / "figures.json").write_text(json.dumps(FIGURES, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"{len(FIGURES)} figures générées ; aperçus : {PREVIEWS}")
