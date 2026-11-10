"""Figures calculées du parcours ; à exécuter dans la sandbox avec PyTorch."""
from pathlib import Path
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE/'pratique'))
from parcours import preparer, entrainer

OUT = BASE/'assets'
PREVIEWS = Path(os.environ.get('MATHS_IA_PREVIEWS', '/tmp/maths-ia-figures'))
PREVIEWS.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'figure.facecolor':'#f7f8f2','axes.facecolor':'white',
                     'text.color':'#203b36','axes.labelcolor':'#203b36',
                     'font.family':'DejaVu Sans','font.size':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'svg.fonttype':'path','svg.hashsalt':'coda-maths-ia'})


def sauver(nom, fig, titre, legende):
    fig.suptitle(titre, x=.06, y=.97, ha='left', fontsize=18, weight='bold')
    fig.text(.06, .025, legende, fontsize=9, color='#63716a')
    fig.tight_layout(rect=(.025,.075,.98,.89))
    svg = OUT/(nom+'.svg')
    fig.savefig(svg, metadata={'Title':titre,'Description':legende,'Date':None})
    svg.write_text('\n'.join(ligne.rstrip() for ligne in svg.read_text().splitlines())+'\n')
    fig.savefig(PREVIEWS/(nom+'.png'), dpi=130)
    plt.close(fig)


fig, axes = plt.subplots(1,2,figsize=(11.6,5.4))
x = np.linspace(-1,7,200)
axes[0].plot(x,(x-3)**2,color='#275c47',lw=2)
w = np.array([0.,1.5,2.25,2.625])
axes[0].scatter(w,(w-3)**2,c=['#b46a43','#80659b','#537b92','#275c47'],s=60,zorder=4)
axes[0].set(xlabel='Poids w',ylabel='L(w)',title='L(w) = (w − 3)² ; pas de 0,25')
for pas, couleur in [(.25,'#275c47'),(1.,'#b46a43')]:
    poids, pertes = 0., []
    for _ in range(7):
        pertes.append((poids-3)**2)
        poids -= pas*2*(poids-3)
    axes[1].plot(range(7),pertes,marker='o',color=couleur,label=f'Pas {pas:g}')
axes[1].set(xlabel='Itération',ylabel='Perte',title='Un pas peut converger ou osciller')
axes[1].legend()
for ax in axes: ax.grid(color='#dce2d9',alpha=.6)
sauver('descente',fig,'Observer une mise à jour plutôt que supposer son effet',
       'Exemple analytique ; le pas 1 oscille entre 0 et 6 et conserve une perte de 9.')

d = preparer()
fig, axes = plt.subplots(1,2,figsize=(11.6,5.4))
for ax, nom in zip(axes,['logistique','reseau']):
    resultat = entrainer(d['Z'],d['classes'],architecture=nom,pas=.1,
                        penalite=.001 if nom=='reseau' else 0.)
    trace = resultat['trace']
    ax.plot(trace[:,0],trace[:,1],color='#275c47',label='Apprentissage')
    ax.plot(trace[:,0],trace[:,2],color='#80659b',label='Validation')
    ax.axvline(resultat['iteration'],color='#b46a43',ls='--',lw=1,label='Meilleur état')
    ax.set(xlabel='Itération',ylabel='Perte binaire moyenne',title='Logistique' if nom=='logistique' else 'Réseau 3 → 4 → 1')
    ax.grid(color='#dce2d9',alpha=.6)
    ax.legend(fontsize=9)
sauver('apprentissage-validation',fig,'Suivre deux partitions aux rôles différents',
       '240 journées simulées ; graine 7 ; pas 0,1. Ces courbes ne consultent pas le test et ne prouvent pas une supériorité générale.')
print('Deux figures calculées ; aperçus :', PREVIEWS)
