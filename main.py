from sommet import Sommet
from arbreB import ArbreB
from int_graph import spawn_tree, fichier
from bibliothèque import *

dictionnaire = {}
file = fichier
joli_arbre = analyse(file)
joli_arbre = build_tree(joli_arbre)
creation_dictionnaire(joli_arbre)
codage(joli_arbre,file)
spawn_tree(joli_arbre)

