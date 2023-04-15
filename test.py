from arbreB import *
from sommet import *
from bibliothèque import *

a = Sommet(1, "a")
b =  Sommet(2, "b")
arbre = ArbreB(a, b, sommet=Sommet(2+1))
arbre2 = ArbreB(Sommet(1, "c"), Sommet(2, "d"), sommet=Sommet(2+1))

arbre += arbre2
print(arbre)
arbre -= a
print(arbre.get_fg())