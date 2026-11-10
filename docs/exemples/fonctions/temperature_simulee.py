"""Reproduire l'exercice de température et comparer deux périodes.

Les tirages reproduisent np.random.seed(graine) puis np.random.normal,
avec un générateur local pour ne pas modifier les autres expériences.
Les températures sont simulées ; elles ne sont pas des mesures météo.
"""
import numpy as np


def simuler(heures=48, periode=24., ecart_type=.5, graine=7):
    if not isinstance(heures, (int, np.integer)) or heures < 2:
        raise ValueError('heures doit être un entier au moins égal à 2')
    if not np.isfinite(periode) or periode <= 0:
        raise ValueError('La période doit être positive et finie')
    if not np.isfinite(ecart_type) or ecart_type < 0:
        raise ValueError("L'écart-type doit être positif ou nul et fini")
    t = np.arange(heures, dtype=float)
    bruit = np.random.RandomState(graine).normal(loc=0., scale=ecart_type, size=t.size)
    signal = 10 + 5*np.sin((2*np.pi/periode)*t)
    return t, signal, bruit, signal+bruit


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    t, T24, bruit, brut = simuler()
    _, T12, bruit12, _ = simuler(periode=12.)
    assert np.array_equal(bruit, bruit12)
    fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)
    axes[0].plot(t, T24, label='Signal idéal : période 24 h')
    axes[0].plot(t, T12, '--', label='Signal idéal : période 12 h')
    axes[0].scatter(t, brut, s=16, label='24 h + bruit, sigma=0,5 °C')
    axes[0].set(ylabel='Température simulée (°C)')
    axes[0].legend()
    axes[1].plot(t, bruit, label='Bruit tiré')
    axes[1].axhline(.5, color='grey', ls='--', label='± sigma : repères, pas des bornes')
    axes[1].axhline(-.5, color='grey', ls='--')
    axes[1].set(xlabel='Temps (h)', ylabel='Bruit (°C)')
    axes[1].legend()
    for ax in axes:
        ax.grid(True, alpha=.3)
    fig.tight_layout()
    print('Théorie : moyenne 0 ; écart-type 0,5 °C ; variance 0,25 °C².')
    print('Sur ces 48 tirages :', bruit.mean(), bruit.std(), bruit.var())
    plt.show()
