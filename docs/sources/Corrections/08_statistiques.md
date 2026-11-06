
```python
import numpy as np

# Raw temperature data
temps = np.array([
    15.2, 15.5, 15.1, 15.3, 15.4,
    25.8, 26.1, 25.9,
    15.2, 15.3, 15.1
])

# 1) Center the data
mean_temp = np.mean(temps)
temps_centered = temps - mean_temp

print("Mean temperature:", mean_temp)
print("Centered temperatures:", temps_centered)

threshold = 2

cold_idx = np.where(temps_centered < -threshold)[0]
hot_idx  = np.where(temps_centered >  threshold)[0]

print("Cold days (indices):", cold_idx)
print("Hot days (indices):", hot_idx)

print("Cold temperatures:", temps[cold_idx])
print("Hot temperatures:", temps[hot_idx])

```

## Centrer réduire 

```python
import numpy as np

# -----------------------------
# Données initiales
# -----------------------------
temperature = np.array([36.8, 37.1, 36.9, 37.5, 38.2, 36.7, 37.0])
heart_rate  = np.array([62, 70, 65, 74, 90, 60, 68])

print("Données brutes :")
print("Températures :", temperature)
print("Fréquences cardiaques :", heart_rate)
print("-" * 40)

# -----------------------------
# 1) Centrage
# -----------------------------
temp_centered = temperature - np.mean(temperature)
heart_centered = heart_rate - np.mean(heart_rate)

print("Températures centrées :", np.round(temp_centered, 3))
print("Cardiaques centrées   :", np.round(heart_centered, 3))
print("-" * 40)

# Interprétation automatique
def interpret_centered(arr, label):
    print(f"Interprétation pour {label}:")
    for i, val in enumerate(arr):
        if val > 0:
            print(f" - Individu {i}: au-dessus de la moyenne ({val:.2f})")
        elif val < 0:
            print(f" - Individu {i}: en-dessous de la moyenne ({val:.2f})")
        else:
            print(f" - Individu {i}: exactement la moyenne")
    print()

interpret_centered(temp_centered, "Température")
interpret_centered(heart_centered, "Fréquence cardiaque")

# -----------------------------
# 2) Réduction (centrage + division par l'écart-type)
# -----------------------------
temp_scaled = temp_centered / np.std(temp_centered)
heart_scaled = heart_centered / np.std(heart_centered)

print("-" * 40)
print("Températures centrées-réduites :", np.round(temp_scaled, 3))
print("Cardiaques centrées-réduites   :", np.round(heart_scaled, 3))
print("-" * 40)

# Interprétation automatique
def interpret_scaled(arr, label):
    print(f"Interprétation (centrées-réduites) pour {label}:")
    for i, val in enumerate(arr):
        if val > 1:
            print(f" - Individu {i}: valeur très élevée (+{val:.2f} écarts-types)")
        elif val < -1:
            print(f" - Individu {i}: valeur très faible ({val:.2f} écarts-types)")
        elif abs(val) < 0.5:
            print(f" - Individu {i}: proche de la moyenne ({val:.2f})")
        else:
            print(f" - Individu {i}: légèrement atypique ({val:.2f})")
    print()

interpret_scaled(temp_scaled, "Température")
interpret_scaled(heart_scaled, "Fréquence cardiaque")

# -----------------------------
# Conclusion automatique
# -----------------------------
print("=" * 60)
print("Conclusion :")
print("Les données centrées-réduites ont une moyenne de 0 et un écart-type de 1.")
print("Elles permettent de comparer température et fréquence cardiaque sur la")
print("même échelle (les écarts-types).")
print("On peut maintenant identifier les individus vraiment atypiques.")
print("=" * 60)
```