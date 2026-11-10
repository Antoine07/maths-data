"""Vérifier les calculs de l'exercice et les figures publiées, avec NumPy seul."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET
import numpy as np
from temperature_simulee import simuler

BASE = Path(__file__).resolve().parent
DOCS = BASE.parents[1]
t, signal, bruit, brut = simuler()
# Concordance avec l'extrait effectivement donné aux étudiants.
source = (DOCS/'sources/Slides/01_derivation.md').read_text()
blocs = re.findall(r'```python\n(.*?)```', source, re.S)
assert len(blocs) == 1
namespace = {}
exec(compile(blocs[0], 'exercice5', 'exec'), namespace)
for nom, valeur in [('t', t), ('noise', bruit), ('T_raw', brut)]:
    assert np.array_equal(namespace[nom], valeur), nom
assert signal.shape == bruit.shape == brut.shape == (48,)
assert np.allclose(signal[24:], signal[:24])
_, signal12, bruit12, _ = simuler(periode=12.)
assert np.allclose(signal12[12:], signal12[:-12])
assert np.array_equal(bruit12, bruit)
assert np.isclose(signal.max(), 15) and np.isclose(signal.min(), 5)
assert np.isclose(signal12.max(), 15) and np.isclose(signal12.min(), 5)
assert 1/12 == 2*(1/24)
assert np.any(np.abs(bruit) > .5)  # ± sigma ne sont pas des bornes.
assert not np.isclose(bruit.std(), .5)
assert np.isclose(bruit.var(), bruit.std()**2)
# Contrôle numérique du paramétrage sigma/variance sur une grande simulation fixe.
_, _, grand_bruit, _ = simuler(heures=200000)
assert abs(grand_bruit.std()-.5) < .005
assert abs(grand_bruit.var()-.25) < .005
# Coordonnées des extrema et changements de signe présentés.
f = lambda x: x**3-3*x
fp = lambda x: 3*x*x-3
assert f(-1) == 2 and f(1) == -2
assert fp(-2) > 0 and fp(0) < 0 and fp(2) > 0
assert (2-2)**2-3 == -3
assert -1+1/(-1) == -2 and 1+1/1 == 2
assert np.isclose(1+np.cos(np.pi),0)
assert 1+np.cos(np.pi-.1) > 0 and 1+np.cos(np.pi+.1) > 0
figures = json.loads((BASE/'figures.json').read_text())
assert len(figures) == 5
for figure in figures:
    path = DOCS/'assets/images'/figure['file']
    assert ET.parse(path).getroot().tag.endswith('svg')
    assert path.read_text().count('<path') > 10
    assert all(ligne == ligne.rstrip() for ligne in path.read_text().splitlines())
html = (DOCS/'01_derivation.html').read_text()
for figure in figures:
    assert 'assets/images/'+figure['file'] in html
assert html.count('<details>') == html.count('</details>') == 2
assert 'scale=0.5' in source and 'variance' in source and 'fréquence' in source
assert 'modèle simplifié' in source and 'pas parfaitement sinusoïdal' in source
# Les sources de travail locales, quand présentes, concordent avec la publication.
for relatif in ['Slides/01_derivation.md','Derivation/TPs/02_TP_temperature.md']:
    original = DOCS.parent/relatif
    if original.exists():
        assert original.read_bytes() == (DOCS/'sources'/relatif).read_bytes()
print('OK : 5 figures, extrema, périodes 24/12 h, écart-type/variance et extrait étudiant exécuté.')
