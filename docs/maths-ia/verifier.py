"""Contrôles publics du cours et des distributions étudiantes, sans corrigé d'examen.

Exécuter dans la sandbox équipée de PyTorch. Aucun notebook source n'est réécrit.
"""
from pathlib import Path
import ast
import contextlib
import io
import json
import re
import sys
import tempfile
import zipfile
import xml.etree.ElementTree as ET

import numpy as np
import torch
import nbformat
from nbclient import NotebookClient

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE/'pratique'))
from parcours import preparer, PARTITIONS, entrainer, probabilites, passage_numpy, metriques, mse

config = json.loads((BASE/'parcours.json').read_text())
modules = config['modules']
assert len(modules) == 8
examen = config['examen']
assert examen['minutes'] == examen['maths']+examen['ia']+examen['pratique'] == 180
assert examen['maths'] == 90 and examen['ia'] == 30 and examen['points'] == 20
required = ['Objectif','Résumé général','Concepts essentiels','Lecture des formules',
            'Lecture du code','Algorithme expliqué','Erreurs fréquentes','Projet fil rouge',
            "Cas d'usage réels",'Fiche de révision','Questions de révision','QCM','Résumé final']
snippets = 0
for module in modules:
    source = BASE/'supports'/(module['id']+'.md')
    text = source.read_text()
    for section in required:
        assert '## '+section in text, (source.name, section)
    assert len(re.findall(r'^## Exercice [123] — ', text, re.M)) == 3
    assert len(re.findall(r'\*\*[1-5]\. ',text)) == 5
    assert 'Indices gradués' in text and 'Afficher la correction' in text
    assert 'Durée indicative' not in text
    for block in re.findall(r'```python\n(.*?)```', text, re.S):
        ast.parse(block)
        namespace = {'np':np}
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(block,str(source),'exec'),namespace)
        if 'avant' in namespace and 'apres' in namespace:
            assert namespace['apres'] < namespace['avant']
        snippets += 1

d = preparer()
assert d['X'].shape == (240,3) and d['Z'].shape == (240,3)
assert np.allclose(d['moyenne'],d['X'][PARTITIONS['train']].mean(0))
assert np.isclose(d['seuil'],np.median(d['y'][PARTITIONS['train']]))
assert np.allclose(d['Z'][PARTITIONS['train']].mean(0),0,atol=1e-12)
assert np.allclose(d['Z'][PARTITIONS['train']].std(0),1)
# L'entraînement ne dépend pas du contenu des lignes réservées au test.
Z2, classes2 = d['Z'].copy(), d['classes'].copy()
Z2[PARTITIONS['test']] += 10000
classes2[PARTITIONS['test']] = 1-classes2[PARTITIONS['test']]
r1 = entrainer(d['Z'],d['classes'],iterations=40)
r2 = entrainer(Z2,classes2,iterations=40)
for a,b in zip(r1['modele'].parameters(),r2['modele'].parameters()):
    assert torch.equal(a,b)
assert np.isclose(r1['perte_validation'],r1['trace'][:,2].min(),atol=1e-6)
assert np.isfinite(probabilites(r1['modele'],d['Z'])).all()
assert metriques([0,0],[0,0])['precision'] is None
try:
    mse(np.zeros((4,1)),np.zeros(4))
except ValueError:
    pass
else:
    raise AssertionError('Diffusion silencieuse acceptée')

for path in (BASE/'assets').glob('*.svg'):
    assert ET.parse(path).getroot().tag.endswith('svg')
for folder in ['pratique','evaluation']:
    for path in (BASE/folder).glob('*.ipynb'):
        notebook = nbformat.read(path,as_version=4)
        nbformat.validate(notebook)
        for cell in notebook.cells:
            if cell.cell_type=='code': ast.parse(cell.source)
    archive = BASE/('pratique.zip' if folder=='pratique' else 'examen-etudiant.zip')
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert all(not any(mot in name.lower() for mot in ['correction','corrige','__pycache__']) for name in z.namelist())
        assert any(name.endswith('.ipynb') for name in z.namelist())
        assert any(name.endswith('.csv') for name in z.namelist())
        with tempfile.TemporaryDirectory() as dossier:
            z.extractall(dossier)
            if folder=='pratique':
                import subprocess
                process = subprocess.run([sys.executable,str(Path(dossier)/'pratique/parcours.py')],capture_output=True,text=True)
                assert process.returncode == 0, process.stderr

notebook = nbformat.read(BASE/'pratique/depart.ipynb',as_version=4)
NotebookClient(notebook,timeout=120,kernel_name='python3',
               resources={'metadata':{'path':str(BASE/'pratique')}}).execute()
home = (BASE.parent/'index.html').read_text()
assert home.index('id="algebre"') < home.index('id="decouvrir-reseaux"') < home.index('id="statistiques"')
assert home.count('id="decouvrir-reseaux"') == 1
bloc = home.split('<!-- maths-ia intro start -->')[1].split('<!-- maths-ia intro end -->')[0]
precedent = -1
for module in modules:
    marqueur = 'data-course="maths-ia/'+module['id']+'"'
    assert home.count(marqueur) == 1
    position = bloc.index(marqueur)
    assert position > precedent
    precedent = position
assert bloc.index('examen.html') > bloc.index('03_comprendre_reseau.html')
assert bloc.index('examen.html') < bloc.index('04_preparer_donnees.html')
assert '07_entrainer_pytorch.html' in home and '08_evaluer.html' in home
assert home.index('Fil rouge · 6 jalons') > home.rfind('</section>')
assert 'Correction enseignant' not in (BASE/'examen.html').read_text()
print(f'OK : 8 séances, 24 exercices, 40 QCM, {snippets} extraits Python exécutés ; données, gradients, PyTorch et archives vérifiés.')
print('Ordre des prérequis, examen de 180 minutes, notebook fil rouge et absence de corrigé dans les distributions étudiantes vérifiés.')
