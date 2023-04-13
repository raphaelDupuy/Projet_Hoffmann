from arbreB import *
from sommet import *
from bibliothèque import *

arbre = ArbreB(Sommet(1, "a"), Sommet(2, "b"))
arbre2 = ArbreB(Sommet(1, "c"), Sommet(2, "d"))
suppr(arbre, "a")
arbre = arbre + arbre2
print(arbre)