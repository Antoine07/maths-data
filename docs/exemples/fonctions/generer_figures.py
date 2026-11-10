"""Figures des exemples de fonctions, réutilisées dans les deux variantes du cours.

Exécuter dans la sandbox : python docs/exemples/fonctions/generer_figures.py
"""
from pathlib import Path
import json
import os
import shutil
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from temperature_simulee import simuler

DOCS = Path(__file__).resolve().parents[2]
OUT = DOCS/'assets/images'
PREVIEWS = Path(os.environ.get('MATHS_FONCTIONS_PREVIEWS', '/tmp/maths-fonctions'))
OUT.mkdir(parents=True, exist_ok=True)
PREVIEWS.mkdir(parents=True, exist_ok=True)
BG, INK, GREEN, PURPLE, ORANGE = '#f7f8f2', '#203b36', '#275c47', '#80659b', '#b46a43'
plt.rcParams.update({'figure.facecolor':BG, 'axes.facecolor':'white', 'text.color':INK,
                     'axes.labelcolor':INK, 'font.family':'DejaVu Sans', 'font.size':11,
                     'axes.spines.top':False, 'axes.spines.right':False,
                     'svg.fonttype':'path', 'svg.hashsalt':'coda-fonctions'})
manifest = []


def canvas(cols=2):
    fig, axes = plt.subplots(1, cols, figsize=(11.6, 5.5))
    for ax in np.atleast_1d(axes):
        ax.grid(color='#dce2d9', alpha=.65)
        ax.set_axisbelow(True)
    return fig, np.atleast_1d(axes)


def save(nom, fig, titre, description):
    fig.suptitle(titre, x=.055, y=.975, ha='left', fontsize=18, weight='bold')
    fig.text(.055, .025, description, fontsize=9, color='#63716a')
    fig.tight_layout(rect=(.025,.08,.985,.89))
    fichier = OUT/(nom+'.svg')
    fig.savefig(fichier, metadata={'Title':titre, 'Description':description, 'Date':None})
    fichier.write_text('\n'.join(l.rstrip() for l in fichier.read_text().splitlines())+'\n')
    fig.savefig(PREVIEWS/(nom+'.png'), dpi=130)
    plt.close(fig)
    source = DOCS.parent/'Slides/images'
    if source.is_dir():
        shutil.copyfile(fichier, source/fichier.name)
    manifest.append(dict(file=fichier.name, title=titre, description=description))


fig, (ax, deriv) = canvas()
x = np.linspace(-2.3, 2.3, 500)
ax.plot(x,x**3-3*x,color=GREEN,lw=2.5)
ax.scatter([-1,1],[2,-2],color=[ORANGE,PURPLE],s=65,zorder=5)
ax.annotate('Maximum local (−1 ; 2)',xy=(-1,2),xytext=(-2.15,3.1),fontsize=10,
            arrowprops=dict(arrowstyle='->',color=ORANGE),color=ORANGE)
ax.annotate('Minimum local (1 ; −2)',xy=(1,-2),xytext=(-.25,-4.5),fontsize=10,
            arrowprops=dict(arrowstyle='->',color=PURPLE),color=PURPLE)
ax.set(xlabel='x',ylabel='f(x)',title='f(x) = x³ − 3x',ylim=(-6,6))
deriv.plot(x,3*x*x-3,color=GREEN,lw=2.5)
deriv.axhline(0,color=INK,lw=1)
deriv.axvspan(-1,1,color=PURPLE,alpha=.12,label="f′ < 0 : décroissance")
deriv.scatter([-1,1],[0,0],color=[ORANGE,PURPLE],s=55,zorder=4)
deriv.set(xlabel='x',ylabel="f′(x)",title="Le changement de signe classe les extrema")
deriv.legend(fontsize=9)
save('fonctions-extrema',fig,'Relier les variations aux extrema locaux',
     'Aux points −1 et 1, la dérivée change de signe. La cubique est non bornée : ces extrema ne sont pas globaux sur ℝ.')

fig, (ax, deriv) = canvas()
for x in [np.linspace(-4,-.14,250),np.linspace(.14,4,250)]:
    ax.plot(x,x-1/x,color=GREEN,lw=2.5)
    deriv.plot(x,1+1/x**2,color=PURPLE,lw=2.5)
ax.axvline(0,color=ORANGE,ls='--',label='x = 0 exclu')
ax.plot([-4,4],[-4,4],color='#8d998d',ls=':',label='Asymptote y = x')
ax.set(xlabel='x',ylabel='f(x)',title='f(x) = x − 1/x',ylim=(-8,8))
ax.legend(fontsize=9)
deriv.axhline(0,color=INK,lw=1)
deriv.set(xlabel='x',ylabel="f′(x)",title="1 + 1/x² > 0 pour x ≠ 0",ylim=(-.5,12))
save('fonctions-quotient',fig,'Une branche croissante de chaque côté du point interdit',
     'Les tracés ne relient jamais les deux branches à travers 0. La croissance est établie séparément sur ]−∞,0[ et ]0,+∞[.')

fig, (ax, deriv) = canvas()
x=np.linspace(-1,1,300)
ax.plot(x,np.exp(3*x),color=GREEN,lw=2.5,label='f(x) = exp(3x)')
ax.plot(x,1+3*x,color=ORANGE,ls='--',label='Tangente en 0 : 1 + 3x')
ax.scatter([0],[1],color=ORANGE,s=55,zorder=5)
ax.set(xlabel='x',ylabel='f(x)',title='La composition change la pente')
ax.legend(fontsize=9)
deriv.plot(x,3*np.exp(3*x),color=PURPLE,lw=2.5)
deriv.scatter([0],[3],color=ORANGE,s=55,zorder=5)
deriv.set(xlabel='x',ylabel="f′(x)",title="f′(x) = 3 exp(3x) > 0")
save('fonctions-composition',fig,'Ne pas oublier la dérivée de la fonction intérieure',
     'En x = 0, la valeur vaut 1 et la pente vaut 3. L’exponentielle et sa dérivée restent strictement positives.')

fig, (ax, quotient, sinus) = canvas(3)
x=np.linspace(-1,5,300)
ax.plot(x,x*x-4*x+1,color=GREEN,lw=2.5)
ax.scatter([2],[-3],color=PURPLE,s=55,zorder=4)
ax.annotate('Minimum global (2 ; −3)',xy=(2,-3),xytext=(.1,4.8),fontsize=9,
            arrowprops=dict(arrowstyle='->',color=PURPLE),color=PURPLE)
ax.set(xlabel='x',ylabel='f(x)',title='a) x² − 4x + 1')
for x in [np.linspace(-4,-.18,250),np.linspace(.18,4,250)]:
    quotient.plot(x,x+1/x,color=GREEN,lw=2.5)
quotient.axvline(0,color=ORANGE,ls='--',lw=1)
quotient.scatter([-1,1],[-2,2],color=[ORANGE,PURPLE],s=55,zorder=4)
quotient.annotate('Max. local',xy=(-1,-2),xytext=(-3.5,.5),fontsize=9,color=ORANGE,
                  arrowprops=dict(arrowstyle='->',color=ORANGE))
quotient.annotate('Min. local',xy=(1,2),xytext=(1.3,5),fontsize=9,color=PURPLE,
                  arrowprops=dict(arrowstyle='->',color=PURPLE))
quotient.set(xlabel='x',ylabel='g(x)',title='b) x + 1/x, x ≠ 0',ylim=(-7,7))
x=np.linspace(0,2*np.pi,400)
sinus.plot(x,np.sin(x)+x,color=GREEN,lw=2.5)
sinus.scatter([np.pi],[np.pi],color=ORANGE,s=55,zorder=4)
sinus.hlines(np.pi,np.pi-.7,np.pi+.7,color=ORANGE,ls='--')
sinus.annotate('Tangente horizontale,\nsans extremum',xy=(np.pi,np.pi),xytext=(.3,5.1),fontsize=9,
                arrowprops=dict(arrowstyle='->',color=ORANGE),color=ORANGE)
sinus.set(xlabel='x (radians)',ylabel='h(x)',title='c) sin(x) + x')
sinus.set_xticks([0,np.pi,2*np.pi],labels=['0','π','2π'])
save('fonctions-exercice-extremums',fig,'Une dérivée nulle ne garantit pas un minimum',
     'Les valeurs et les changements de signe se justifient par le calcul. Une courbe sur une fenêtre finie ne prouve pas un extremum global.')

fig, (ax, bruit_ax) = canvas()
t, T24, bruit, brut = simuler()
dense=np.linspace(0,48,600)
ax.plot(dense,10+5*np.sin(2*np.pi*dense/24),color=GREEN,lw=2,label='Période 24 h, sans bruit')
ax.plot(dense,10+5*np.sin(2*np.pi*dense/12),color=PURPLE,lw=1.5,ls='--',label='Période 12 h, sans bruit')
ax.scatter(t,brut,color=ORANGE,s=15,alpha=.8,label='24 h + bruit simulé')
ax.set(xlabel='Temps (h)',ylabel='Température simulée (°C)',title='Deux cycles ou quatre cycles en 48 h',xlim=(0,48))
ax.legend(fontsize=8)
bruit_ax.plot(t,bruit,color=ORANGE,lw=1,marker='.',label='48 tirages gaussiens')
bruit_ax.axhline(0,color=INK,lw=1)
bruit_ax.axhline(.5,color=PURPLE,ls='--',label='± sigma : repères, pas des bornes')
bruit_ax.axhline(-.5,color=PURPLE,ls='--')
bruit_ax.set(xlabel='Temps (h)',ylabel='Bruit ajouté (°C)',title='Sigma = 0,5 °C ; variance = 0,25 °C²')
bruit_ax.legend(fontsize=8)
save('fonctions-temperature',fig,'Séparer le cycle idéal et les fluctuations simulées',
     'Exemple reproductible, graine 7. Le cycle réel n’est pas parfaitement sinusoïdal ; le choix gaussien est une hypothèse de simulation.')

(Path(__file__).parent/'figures.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Cinq figures générées ; aperçus :', PREVIEWS)
