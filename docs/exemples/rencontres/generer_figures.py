"""Régénérer les trois graphiques en exécutant le corrigé, sans fenêtre graphique.

python docs/exemples/rencontres/generer_figures.py
Les SVG vont dans docs/assets/images et, si présent, Slides/images.
Les PNG d'aperçu vont dans /tmp/rencontres-numpy.
"""
from pathlib import Path
import contextlib
import io
import os
import runpy
import shutil
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[2]
SORTIE = ROOT/'docs/assets/images'
APERCUS = Path(os.environ.get('MATHS_RENCONTRES_PREVIEWS', '/tmp/rencontres-numpy'))
SORTIE.mkdir(parents=True, exist_ok=True)
APERCUS.mkdir(parents=True, exist_ok=True)
noms = iter(['rencontres-annuelles', 'rencontres-passe-futur', 'rencontres-frequences'])
plt.rcParams['svg.hashsalt'] = 'coda-rencontres-numpy'


def enregistrer():
    nom = next(noms)
    fig = plt.gcf()
    cible = SORTIE/(nom+'.svg')
    fig.savefig(cible, metadata={'Date':None})
    cible.write_text('\n'.join(l.rstrip() for l in cible.read_text().splitlines())+'\n')
    fig.savefig(APERCUS/(nom+'.png'), dpi=120)
    if (ROOT/'Slides/images').exists():
        shutil.copyfile(cible, ROOT/'Slides/images'/cible.name)
    plt.close(fig)


plt.show = enregistrer
with contextlib.redirect_stdout(io.StringIO()):
    resultats = runpy.run_path(str(BASE/'rencontres_numpy.py'))
print('Trois graphiques générés dans', SORTIE)
