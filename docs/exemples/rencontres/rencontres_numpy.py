import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# TP — La moitié des années, combien de rencontres ?
# NumPy + Matplotlib
# ============================================================

# 1. PARAMÈTRES DU MODÈLE

age_actuel = 30
age_fin = 60

# Nombre de journées de rencontre par an
rencontres_enfance = 300    # De 0 à 18 ans
rencontres_adulte = 12      # De 18 ans à l'âge actuel
rencontres_futures = 12     # De l'âge actuel à l'âge de fin

# 2. CONSTRUIRE LE TABLEAU NUMPY

ages = np.arange(age_fin)

rencontres = np.concatenate([
    np.full(18, rencontres_enfance),
    np.full(age_actuel - 18, rencontres_adulte),
    np.full(age_fin - age_actuel, rencontres_futures)
])

print("Tableau des rencontres :")
print(rencontres)
print("Nombre d'années :", len(rencontres))

# 3. CALCULER LE PASSÉ ET LE FUTUR

passe = rencontres[:age_actuel]
futur = rencontres[age_actuel:]

jours_passes = np.sum(passe)
jours_futurs = np.sum(futur)
jours_total = np.sum(rencontres)

part_annees = (age_fin - age_actuel) / age_fin * 100
part_future = jours_futurs / jours_total * 100

print("\n===== SITUATION INITIALE =====")
print(f"Journées passées : {jours_passes}")
print(f"Journées futures : {jours_futurs}")
print(f"Total : {jours_total}")
print(f"Années restantes : {part_annees:.2f} %")
print(f"Rencontres futures : {part_future:.2f} %")

# 4. REPRÉSENTATION EN POINTS
# 1 point = 12 journées de rencontre.
# Ici les deux totaux sont divisibles par 12 : // ne perd aucun reste.

unite = 12
points_passes = jours_passes // unite
points_futurs = jours_futurs // unite

print("\n===== REPRÉSENTATION EN POINTS =====")
print(f"Points passés : {points_passes}")
print(f"Points futurs : {points_futurs}")
print(f"Total : {points_passes + points_futurs}")

# 5. SCÉNARIO : DOUBLER LES RENCONTRES FUTURES

nouvelles_rencontres = rencontres.copy()
nouvelles_rencontres[age_actuel:] = 2 * rencontres_futures

nouveau_futur = np.sum(nouvelles_rencontres[age_actuel:])
nouveau_total = np.sum(nouvelles_rencontres)
nouvelle_part = nouveau_futur / nouveau_total * 100

print("\n===== SCÉNARIO DOUBLÉ =====")
print(f"Journées futures : {nouveau_futur}")
print(f"Total : {nouveau_total}")
print(f"Part future : {nouvelle_part:.2f} %")

# 6. SIMULER PLUSIEURS FRÉQUENCES
# Vectorisation NumPy : la boucle suivante sert seulement à l'affichage.

frequences = np.array([6, 12, 24, 36, 52, 100])
duree_future = age_fin - age_actuel
jours_futurs_scenarios = frequences * duree_future
totaux = jours_passes + jours_futurs_scenarios
proportions = jours_futurs_scenarios / totaux * 100

print("\n===== COMPARAISON DES SCÉNARIOS =====")
for frequence, jours, proportion in zip(
    frequences, jours_futurs_scenarios, proportions
):
    print(
        f"{frequence:3d} jours/an | "
        f"{jours:4d} jours futurs | "
        f"{proportion:6.2f} %"
    )

# 7. GRAPHIQUE — DEUX LECTURES DU MODÈLE

fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

axes[0].bar(ages, rencontres, color="steelblue")
axes[0].axvline(age_actuel - 0.5, color="red", linestyle="--")
axes[0].set(xlabel="Âge au début de l'année", ylabel="Journées par an",
            title="Fréquence annuelle")
axes[0].grid(axis="y", alpha=0.3)

axes[1].plot(frequences, proportions, marker="o", color="darkgreen")
axes[1].axhline(50, color="red", linestyle="--", label="50 %")
axes[1].set(xlabel="Journées futures par an", ylabel="Part future (%)",
            title="Scénarios de fréquence")
axes[1].grid(alpha=0.3)
axes[1].legend()

fig.tight_layout()
plt.show()

# 8. CONCLUSION

print("\n===== CONCLUSION =====")
print(
    f"Il reste {part_annees:.0f} % des années, "
    f"mais seulement {part_future:.2f} % "
    "des journées de rencontre."
)
print(
    f"En doublant les rencontres futures, "
    f"cette proportion atteint {nouvelle_part:.2f} %."
)
print(
    "Les résultats dépendent des hypothèses "
    "de fréquence et de durée retenues."
)
