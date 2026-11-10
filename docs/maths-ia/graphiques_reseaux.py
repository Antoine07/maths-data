"""Graphiques calculés pour observer un neurone et interpréter l'apprentissage.

Exécuter : python docs/maths-ia/graphiques_reseaux.py
NumPy et Matplotlib suffisent ; aucune donnée de test du fil rouge n'est utilisée.
"""
from pathlib import Path
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.lines import Line2D

BASE = Path(__file__).resolve().parent
VERT, VIOLET, ORANGE, BLEU = '#275c47', '#80659b', '#b46a43', '#537b92'


def sigmoide(z):
    return 1 / (1 + np.exp(-np.asarray(z)))


def logits_xor(X):
    """Réseau 2→2→1 avec paramètres fournis : deux ReLU, puis une sortie affine."""
    X = np.asarray(X)
    W1 = np.array([[1., 1.], [1., 1.]])
    b1 = np.array([0., -1.])
    W2 = np.array([8., -16.])
    return np.maximum(0., X @ W1 + b1) @ W2 - 4.


def trace_validation():
    """Descente réelle pour un neurone linéaire y_chapeau=w*x, avec x=1.

    Les cibles d'apprentissage sont [3,3] et celles de validation [1,3].
    Leur petite taille est volontaire : ce sont des données illustratives,
    pas les journées du projet. Aucun choix ne consulte un jeu de test.
    """
    poids = [0.]
    for _ in range(30):
        gradient = 2 * (poids[-1] - 3)
        poids.append(poids[-1] - .1 * gradient)
    poids = np.array(poids)
    train = np.mean((poids[:, None] - np.array([3., 3.]))**2, axis=1)
    validation = np.mean((poids[:, None] - np.array([1., 3.]))**2, axis=1)
    return np.arange(poids.size), poids, train, validation


def generer():
    sortie = BASE/'assets'
    apercus = Path(os.environ.get('MATHS_IA_PREVIEWS', '/tmp/maths-ia-figures'))
    apercus.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'figure.facecolor':'#f7f8f2', 'axes.facecolor':'white',
                         'text.color':'#203b36', 'axes.labelcolor':'#203b36',
                         'font.family':'DejaVu Sans', 'font.size':11,
                         'axes.spines.top':False, 'axes.spines.right':False,
                         'svg.fonttype':'path', 'svg.hashsalt':'coda-reseaux-observer'})

    def canevas(n=2):
        fig, axes = plt.subplots(1, n, figsize=(11.6, 5.4), squeeze=False)
        for ax in axes[0]:
            ax.grid(color='#dce2d9', alpha=.6)
            ax.set_axisbelow(True)
        return fig, axes[0]

    def sauver(nom, fig, titre, legende):
        fig.suptitle(titre, x=.06, y=.97, ha='left', fontsize=18, weight='bold')
        fig.text(.06, .025, legende, fontsize=9, color='#63716a')
        fig.tight_layout(rect=(.025,.105,.98,.89))
        svg = sortie/(nom+'.svg')
        fig.savefig(svg, metadata={'Title':titre, 'Description':legende, 'Date':None})
        svg.write_text('\n'.join(l.rstrip() for l in svg.read_text().splitlines())+'\n')
        fig.savefig(apercus/(nom+'.png'), dpi=130)
        plt.close(fig)

    fig, (gauche, droite) = canevas()
    z = np.linspace(-4,4,401)
    gauche.plot(z, sigmoide(z), color=VERT, lw=2.5)
    gauche.scatter([0],[.5], color=ORANGE, zorder=4)
    gauche.axhline(.5, color='#8b968a', ls=':', lw=1)
    gauche.set(xlabel='Score z', ylabel='σ(z)', title='Sigmoïde : une sortie entre 0 et 1', ylim=(-.05,1.05))
    droite.plot(z,np.maximum(0,z),color=VIOLET,lw=2.5)
    droite.scatter([0],[0],color=ORANGE,zorder=4)
    droite.set(xlabel='Score z',ylabel='ReLU(z)',title='ReLU : les scores négatifs deviennent 0',ylim=(-.2,4.2))
    sauver('reseau-activations',fig,'Deux activations, deux comportements',
           'Fonctions exactes. Les axes verticaux ont des échelles différentes : une sortie ReLU n’est pas une probabilité.')

    fig, (poids_ax, biais_ax) = canevas()
    x = np.linspace(-4,4,401)
    for w, couleur in [(-2,BLEU),(.5,ORANGE),(1,VERT),(2,VIOLET)]:
        poids_ax.plot(x,sigmoide(w*x),color=couleur,lw=2,label=f'w = {w:g}, b = 0')
    poids_ax.set(title='Changer le poids, biais fixé à 0')
    for b, couleur in [(-2,ORANGE),(0,VERT),(2,VIOLET)]:
        biais_ax.plot(x,sigmoide(x+b),color=couleur,lw=2,label=f'w = 1, b = {b:g}')
        biais_ax.scatter([-b],[.5],color=couleur,s=30,zorder=4)
    biais_ax.set(title='Changer le biais, poids fixé à 1')
    for ax in [poids_ax,biais_ax]:
        ax.axhline(.5,color='#8b968a',ls=':',lw=1)
        ax.set(xlabel='Entrée x',ylabel='p = σ(wx + b)',ylim=(-.05,1.05))
        ax.legend(fontsize=9,loc='upper left')
    sauver('reseau-poids-biais',fig,'Observer séparément le poids et le biais',
           'Paramètres fournis, sans apprentissage. Le seuil p = 0,5 correspond au score wx + b = 0.')

    fig, axes = canevas()
    valeurs = np.linspace(-.35,1.35,301)
    xx, yy = np.meshgrid(valeurs,valeurs)
    grille = np.column_stack([xx.ravel(),yy.ravel()])
    points = np.array([[0.,0.],[0.,1.],[1.,0.],[1.,1.]])
    classes = np.array([0,1,1,0])
    affine = 4*(grille.sum(axis=1)-.5)
    reseau = logits_xor(grille)
    for ax, logits, titre in zip(axes,[affine,reseau],['Score affine : 3 points sur 4 corrects','Réseau ReLU : 4 points sur 4 corrects']):
        predictions = (logits >= 0).reshape(xx.shape)
        ax.contourf(xx,yy,predictions,levels=[-.5,.5,1.5],cmap=ListedColormap(['#e5eee6','#e9e2f0']))
        ax.contour(xx,yy,logits.reshape(xx.shape),levels=[0],colors=['#203b36'],linewidths=1.5)
        for classe, couleur, marqueur in [(0,VERT,'o'),(1,VIOLET,'^')]:
            p = points[classes==classe]
            ax.scatter(p[:,0],p[:,1],c=couleur,marker=marqueur,s=100,edgecolors='white',linewidths=1,zorder=5)
        ax.set(xlabel='Entrée x₁',ylabel='Entrée x₂',title=titre,xlim=(-.35,1.35),ylim=(-.35,1.35))
        ax.set_aspect('equal')
        ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
    axes[0].scatter([1],[1],facecolors='none',edgecolors=ORANGE,s=250,lw=2,zorder=6)
    legende=[Line2D([0],[0],marker='o',color='none',markerfacecolor=VERT,label='Classe réelle 0',markersize=8),
             Line2D([0],[0],marker='^',color='none',markerfacecolor=VIOLET,label='Classe réelle 1',markersize=8)]
    fig.legend(handles=legende,loc='lower center',bbox_to_anchor=(.5,.058),ncol=2,frameon=False,fontsize=9)
    sauver('reseau-frontieres-xor',fig,'XOR : comparer les régions de décision',
           'Fond = classe prédite ; trait = p = 0,5. Paramètres choisis à la main : aucun entraînement ni bilan de généralisation.')

    fig, (ax,) = canevas(1)
    iterations, poids, train, validation = trace_validation()
    ax.plot(iterations,train,color=VERT,lw=2.5,label='Apprentissage : cibles (3 ; 3)')
    ax.plot(iterations,validation,color=VIOLET,lw=2.5,label='Validation : cibles (1 ; 3)')
    ax.scatter(iterations[::2],validation[::2],color=VIOLET,s=15)
    ax.set(xlabel='Nombre de mises à jour',ylabel='Erreur quadratique moyenne',title='Neurone linéaire : prédiction = w ; départ w = 0 ; pas = 0,1',xticks=range(0,31,5))
    ax.legend(fontsize=10)
    sauver('reseau-arret-validation',fig,'La dernière itération n’est pas toujours celle à retenir',
           'Calcul exact sur quatre cibles illustratives, distinctes du projet. La validation choisit l’état ; aucun test n’est utilisé.')
    print('Quatre graphiques calculés ; aperçus :', apercus)


if __name__ == '__main__':
    generer()
