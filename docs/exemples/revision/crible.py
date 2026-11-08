"""Crible d'Ératosthène : nombres premiers jusqu'à une borne incluse.

Lancer : python3 crible.py
La fonction attend un entier naturel.
"""


def crible(n):
    if n < 2:
        return []
    premier = [True] * (n + 1)
    premier[0] = premier[1] = False
    p = 2
    while p * p <= n:
        if premier[p]:
            for multiple in range(p * p, n + 1, p):
                premier[multiple] = False
        p += 1
    return [i for i in range(2, n + 1) if premier[i]]


if __name__ == "__main__":
    print(crible(30))
