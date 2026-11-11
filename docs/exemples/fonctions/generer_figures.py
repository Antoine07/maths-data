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

fig, (ax,) = canvas(1)
x = np.linspace(0,4*np.pi,1001)
ax.plot(x,np.sin(x),color=GREEN,lw=2.5,label='sin(x)')
ax.plot(x,np.cos(x),color=PURPLE,lw=2.5,label='cos(x)')
ax.axhline(0,color=INK,lw=.8)
ax.annotate('',xy=(0,1.25),xytext=(2*np.pi,1.25),
            arrowprops=dict(arrowstyle='<->',color=ORANGE,lw=1.5))
ax.text(np.pi,1.33,'Une période de 2π radians',ha='center',color=ORANGE,fontsize=11)
ax.set(xlabel='Angle x (radians)',ylabel='Valeur de la fonction',xlim=(0,4*np.pi),ylim=(-1.3,1.65))
ax.set_xticks(np.arange(9)*np.pi/2,labels=['0','π/2','π','3π/2','2π','5π/2','3π','7π/2','4π'])
ax.legend(loc='upper right',fontsize=10)
save('fonctions-sinus-cosinus',fig,'Sinus et cosinus se répètent tous les 2π radians',
     'Les deux courbes ont la même période fondamentale. Le décalage entre sinus et cosinus vaut un quart de période.')

fig, axes = plt.subplots(2,2,figsize=(11.6,7.1),sharex=True,sharey=True)
for ax, fonction, coefficient, titre, couleur in zip(
    axes.flat,[np.sin,np.sin,np.sin,np.cos],[1,2,4,.5],
    ['sin(x) · période 2π','sin(2x) · période π','sin(4x) · période π/2','cos(x/2) · période 4π'],
    [GREEN,PURPLE,ORANGE,GREEN]
):
    periode = 2*np.pi/abs(coefficient)
    ax.axvspan(0,periode,color=couleur,alpha=.12)
    ax.plot(x,fonction(coefficient*x),color=couleur,lw=2)
    ax.axhline(0,color=INK,lw=.7)
    ax.set(title=titre,xlim=(0,4*np.pi),ylim=(-1.2,1.2),ylabel='Valeur')
    ax.set_xticks(np.arange(5)*np.pi,labels=['0','π','2π','3π','4π'])
    ax.grid(color='#dce2d9',alpha=.65)
    ax.set_axisbelow(True)
for ax in axes[-1]:
    ax.set_xlabel('Angle x (radians)')
save('fonctions-periodes',fig,'Comparer les périodes sur une fenêtre commune',
     'Chaque zone colorée couvre un cycle complet. Entre 0 et 4π, on compte respectivement 2, 4, 8 et 1 cycles.')

fig, (signal_ax, circle_ax) = plt.subplots(
    1, 2, figsize=(11.6, 5.0), gridspec_kw={'width_ratios': [1.3, 1]}
)
heures = np.linspace(0, 48, 700)
charge = 1 + .28*np.cos(2*np.pi*(heures-18)/24) + .08*np.cos(2*np.pi*(heures-7)/12)
signal_ax.fill_between(heures, 0, charge, color=GREEN, alpha=.12)
signal_ax.plot(heures, charge, color=GREEN, lw=2.7, label='Profil simulé')
signal_ax.axhline(1, color=ORANGE, ls='--', lw=1.5, label='Niveau moyen')
signal_ax.axvline(24, color='#dce2d9', ls=':', lw=1.5)
signal_ax.set(
    xlabel='Temps (heures)', ylabel='Consommation (unités simulées)',
    title='Un profil quotidien se répète', xlim=(0, 48), xticks=[0, 12, 24, 36, 48]
)
signal_ax.legend(fontsize=9)

theta = np.linspace(0, 2*np.pi, 500)
circle_ax.plot(np.cos(theta), np.sin(theta), color=PURPLE, lw=2.2)
circle_ax.axhline(0, color='#dce2d9', lw=.8)
circle_ax.axvline(0, color='#dce2d9', lw=.8)
circle_ax.plot([0, 1], [0, 0], color=ORANGE, lw=1.5, alpha=.8)
heure_23 = 2*np.pi*23/24
point_23 = (np.cos(heure_23), np.sin(heure_23))
circle_ax.plot([0, point_23[0]], [0, point_23[1]], color=GREEN, lw=1.5, alpha=.8)
circle_ax.scatter([1, point_23[0]], [0, point_23[1]], color=[ORANGE, GREEN], s=58, zorder=4)
circle_ax.annotate('0 h', (1, 0), xytext=(12, 10), textcoords='offset points', color=ORANGE, weight='bold')
circle_ax.annotate('23 h', point_23, xytext=(10, -20), textcoords='offset points', color=GREEN, weight='bold')
arc = np.linspace(heure_23, 2*np.pi, 30)
circle_ax.plot(1.12*np.cos(arc), 1.12*np.sin(arc), color=ORANGE, lw=2.5)
circle_ax.set(
    title='Coder l’heure sur un cercle', xlabel='cos(2πh/24)', ylabel='sin(2πh/24)',
    xlim=(-1.4, 1.55), ylim=(-1.4, 1.4), aspect='equal'
)
save('fonctions-ia-cyclique',fig,'Du cycle observé aux variables d’un modèle',
     'Profil électrique simulé sur deux jours. Une paire sinus/cosinus code l’heure sans rupture entre 23 h et 0 h.')

fig, (phase_ax, sine_ax) = plt.subplots(
    1, 2, figsize=(11.6, 4.8), gridspec_kw={'width_ratios': [1, 1.25]}
)
phi0 = np.pi/6
delta_phi = np.pi/2
phi1 = phi0 + delta_phi
angles = np.linspace(0, 2*np.pi, 500)
phase_ax.plot(np.cos(angles), np.sin(angles), color='#dce2d9', lw=2)
phase_ax.axhline(0, color='#dce2d9', lw=.8)
phase_ax.axvline(0, color='#dce2d9', lw=.8)
phase_ax.annotate('', xy=(np.cos(phi0), np.sin(phi0)), xytext=(0, 0),
                  arrowprops=dict(arrowstyle='->', color=ORANGE, lw=2, linestyle='--'))
phase_ax.annotate('', xy=(np.cos(phi1), np.sin(phi1)), xytext=(0, 0),
                  arrowprops=dict(arrowstyle='->', color=PURPLE, lw=2.8))
arc_angles = np.linspace(phi0, phi1, 80)
phase_ax.plot(.78*np.cos(arc_angles), .78*np.sin(arc_angles), color=GREEN, lw=2.5)
phase_ax.annotate('', xy=(.78*np.cos(phi1), .78*np.sin(phi1)),
                  xytext=(.78*np.cos(phi1-.08), .78*np.sin(phi1-.08)),
                  arrowprops=dict(arrowstyle='->', color=GREEN, lw=2))
phase_ax.text(-1.2, -.5, 'Δφ = ω Δt', color=GREEN, ha='left', weight='bold', fontsize=9)
phase_ax.annotate('t', (np.cos(phi0), np.sin(phi0)), xytext=(9, -5), textcoords='offset points',
                  color=ORANGE, fontsize=10, weight='bold')
phase_ax.annotate('t + Δt', (np.cos(phi1), np.sin(phi1)), xytext=(-28, 10), textcoords='offset points',
                  color=PURPLE, fontsize=10, weight='bold')
phase_ax.scatter([0], [0], color=INK, s=25, zorder=4)
phase_ax.set(title='La phase : l’angle de l’aiguille', xlabel='cos φ', ylabel='sin φ',
             xlim=(-1.3, 1.35), ylim=(-1.25, 1.3), aspect='equal')

wave_phase = np.linspace(0, 2*np.pi, 500)
sine_ax.plot(wave_phase, np.sin(wave_phase), color=GREEN, lw=2.7)
sine_ax.axhline(0, color='#dce2d9', lw=.8)
sine_ax.axvline(phi1, color=PURPLE, lw=1.4, ls='--')
sine_ax.scatter([phi1], [np.sin(phi1)], color=PURPLE, s=58, zorder=4)
sine_ax.annotate('sin φ', (phi1, np.sin(phi1)), xytext=(10, -22), textcoords='offset points',
                 color=PURPLE, weight='bold')
sine_ax.set(title='Le sinus suit la position de l’aiguille', xlabel='Phase φ (radians)',
            ylabel='sin φ', xlim=(0, 2*np.pi), ylim=(-1.25, 1.3),
            xticks=[0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
            xticklabels=['0', 'π/2', 'π', '3π/2', '2π'])
save('fonctions-phase-pulsation',fig,'Phase et pulsation : angle et vitesse de rotation',
     'La phase indique la position de l’aiguille. La pulsation ω mesure la vitesse de variation de la phase ; en Δt, Δφ=ωΔt. Le sinus est sa projection verticale.')

(Path(__file__).parent/'figures.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Neuf figures générées ; aperçus :', PREVIEWS)
