"""Génère le graphique d'introduction sur la fréquence et le cumul."""

from pathlib import Path
import os
import shutil

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
FIGURE_NAME = "tail-02-cumul-intro.svg"
SOURCE_FIGURES = ROOT / "Slides" / "figures"
PUBLIC_FIGURES = ROOT / "docs" / "sources" / "Slides" / "figures"
PUBLIC_IMAGES = ROOT / "docs" / "assets" / "images"

GREEN = "#275c47"
BLUE = "#6375a8"
INK = "#203b36"
MUTED = "#63716a"
GRID = "#dce2d9"
BACKGROUND = "#f7f8f2"

plt.rcParams.update(
    {
        "figure.facecolor": BACKGROUND,
        "axes.facecolor": "#ffffff",
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
    }
)

fig = plt.figure(figsize=(12.2, 6.5), facecolor=BACKGROUND)
grid = fig.add_gridspec(2, 2, height_ratios=[1, 1.15], hspace=0.45, wspace=0.22)
step_ax = fig.add_subplot(grid[0, 0])
linear_ax = fig.add_subplot(grid[0, 1], sharey=step_ax)
cumulative_ax = fig.add_subplot(grid[1, :])

fig.suptitle(
    "Même durée, rythmes différents : que cumule-t-on ?",
    x=0.055,
    y=0.99,
    ha="left",
    fontsize=17,
    fontweight="bold",
)
fig.text(
    0.056,
    0.92,
    "Aires sous les rythmes en haut ; cumuls exacts et estimations au rythme moyen en bas.",
    color=MUTED,
    fontsize=9,
)

# Scénario A : 2 visiteurs/h pendant une heure, puis 4 visiteurs/h.
step_ax.stairs(
    [2, 4], [0, 1, 2], baseline=0, fill=True, color=GREEN, alpha=0.17
)
step_ax.stairs([2, 4], [0, 1, 2], color=GREEN, linewidth=2.8)
step_ax.text(0.5, 0.65, "2 × 1", color=GREEN, ha="center", fontweight="bold")
step_ax.text(1.5, 1.65, "4 × 1", color=GREEN, ha="center", fontweight="bold")
step_ax.text(1.02, 4.48, "Aire totale = 6", color=GREEN, ha="center", fontweight="bold")
step_ax.set(
    title="A · Fréquence constante par paliers",
    xlabel="Temps t (heures)",
    ylabel="Rythme (visiteurs par heure)",
    xlim=(0, 2),
    ylim=(0, 5),
    xticks=[0, 1, 2],
    yticks=[0, 1, 2, 3, 4, 5],
)
step_ax.grid(True, linewidth=0.7)

# Scénario B : fréquence qui augmente linéairement, f(t) = 2t.
t = np.linspace(0, 2, 300)
rate = 2 * t
linear_ax.fill_between(t, 0, rate, color=BLUE, alpha=0.17)
linear_ax.plot(t, rate, color=BLUE, linewidth=2.8, label="f(t) = 2t")
linear_ax.scatter([0, 2], [0, 4], color=BLUE, s=28, zorder=3)
linear_ax.text(1.02, 1.05, "Aire du triangle = 4", color=BLUE, ha="center", fontweight="bold")
linear_ax.set(
    title="B · Fréquence qui augmente continûment",
    xlabel="Temps t (heures)",
    xlim=(0, 2),
    xticks=[0, 1, 2],
)
linear_ax.grid(True, linewidth=0.7)

# Cumuls : aire exacte sous chaque rythme, comparée à une droite de pente égale
# au rythme moyen sur les deux heures.
curve_t = np.linspace(0, 2, 401)
cumulative_step = np.where(curve_t <= 1, 2 * curve_t, 2 + 4 * (curve_t - 1))
cumulative_linear = curve_t**2
cumulative_ax.plot(
    curve_t,
    cumulative_step,
    color=GREEN,
    linewidth=2.8,
    label=r"Scénario A : cumul par paliers",
)
cumulative_ax.plot(
    curve_t,
    3 * curve_t,
    color=GREEN,
    linewidth=1.8,
    linestyle="--",
    label=r"A au rythme moyen : $3t$",
)
cumulative_ax.plot(
    curve_t,
    cumulative_linear,
    color=BLUE,
    linewidth=2.8,
    label=r"Scénario B : cumul exact $t^2$",
)
cumulative_ax.plot(
    curve_t,
    2 * curve_t,
    color=BLUE,
    linewidth=1.8,
    linestyle="--",
    label=r"B au rythme moyen : $2t$",
)
cumulative_ax.axvline(1, color=GRID, linewidth=1, linestyle=":")
cumulative_ax.scatter([2, 2], [6, 4], color=[GREEN, BLUE], s=34, zorder=4)
cumulative_ax.annotate("6", (2, 6), xytext=(-12, 7), textcoords="offset points", color=GREEN, ha="right", fontweight="bold")
cumulative_ax.annotate("4", (2, 4), xytext=(-12, 7), textcoords="offset points", color=BLUE, ha="right", fontweight="bold")
cumulative_ax.set(
    title="Cumuls exacts et estimations avec le rythme moyen",
    xlabel="Temps t (heures)",
    ylabel="Visiteurs cumulés",
    xlim=(0, 2),
    ylim=(0, 7),
    xticks=[0, 0.5, 1, 1.5, 2],
    yticks=range(0, 8),
)
cumulative_ax.grid(True, linewidth=0.7)
cumulative_ax.legend(loc="upper left", ncol=2, fontsize=9)

fig.subplots_adjust(left=0.09, right=0.97, top=0.87, bottom=0.12)

SOURCE_FIGURES.mkdir(parents=True, exist_ok=True)
PUBLIC_FIGURES.mkdir(parents=True, exist_ok=True)
PUBLIC_IMAGES.mkdir(parents=True, exist_ok=True)
generated = SOURCE_FIGURES / FIGURE_NAME
fig.savefig(
    generated,
    metadata={
        "Title": "Deux rythmes, leurs cumuls et le rythme moyen",
        "Description": (
            "Le premier scénario a une fréquence par paliers et un cumul final de 6. "
            "Le second a une fréquence f(t)=2t et un cumul t², final 4. "
            "Les droites au rythme moyen ont le même total final mais diffèrent "
            "des cumuls exacts entre 0 et 2 heures."
        ),
        "Date": None,
    },
)
generated.write_text(
    "\n".join(line.rstrip() for line in generated.read_text(encoding="utf-8").splitlines()) + "\n",
    encoding="utf-8",
)
preview = os.environ.get("MATHS_CUMUL_PREVIEW")
if preview:
    preview_path = Path(preview)
    preview_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(preview_path, dpi=140)
plt.close(fig)

shutil.copyfile(generated, PUBLIC_FIGURES / FIGURE_NAME)
shutil.copyfile(generated, PUBLIC_IMAGES / FIGURE_NAME)
print(f"Figure générée : {generated}")
