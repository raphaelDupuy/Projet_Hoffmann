from sommet import Sommet
from arbreB import ArbreB
from int_graph import spawn_tree
from bibliothèque import *

dictionnaire = {}
joli_arbre = analyse("texte.txt")
joli_arbre = build_tree(joli_arbre)
creation_dictionnaire(joli_arbre)
codage(joli_arbre)
spawn_tree(joli_arbre)
decodage(joli_arbre)
