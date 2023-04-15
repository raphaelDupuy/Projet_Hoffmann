from arbreB import *
from sommet import *
from bibliothèque import *

arbre = ArbreB(Sommet(1, "a"), Sommet(2, "b"), sommet=Sommet(2+1))
arbre2 = ArbreB(Sommet(1, "c"), Sommet(2, "d"), sommet=Sommet(2+1))
print(arbre.get_fg())
print(arbre.get_fd())

arbre += arbre2
print(arbre)
print(arbre)