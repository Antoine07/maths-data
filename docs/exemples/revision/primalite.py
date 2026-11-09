"""Tester la primalité d'un entier et compter les tests de divisibilité.

Lancer : python3 primalite.py
Complexité : O(racine(n)) tests au pire, un nombre constant de variables.
Les temps affichés sont des mesures d'exécution, pas des durées de travail.
"""
from math import isqrt
from time import perf_counter


def analyser_primalite(n):
    """Renvoyer (est_premier, nombre_de_tests) pour un entier n."""
    if n < 2:
        return False, 0
    d, tests = 2, 0
    while d * d <= n:
        tests += 1
        if n % d == 0:
            return False, tests
        d += 1
    return True, tests


def est_premier(n):
    """Tester les diviseurs de 2 à la racine incluse ; refuser n < 2."""
    return analyser_primalite(n)[0]


if __name__ == '__main__':
    print('N | premier ? | tests | borne des tests | temps mesuré (µs)')
    for n in (1, 2, 7, 49, 101, 121, 1009, 10007):
        debut = perf_counter()
        premier, tests = analyser_primalite(n)
        temps = perf_counter() - debut
        borne = max(0, isqrt(n) - 1)
        print(f'{n} | {premier} | {tests} | {borne} | {temps * 1e6:.3f}')
    print('Le nombre de tests décrit le travail ; les temps dépendent de la machine.')
