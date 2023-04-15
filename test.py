from arbreB import *
from sommet import *
from bibliothèque import *

a = Sommet(1, "a")
b =  Sommet(2, "b")
c =Sommet(1, "c")
d = Sommet(2, "d")
arbre = ArbreB(a, b, sommet=Sommet(a.get_occur() + b.get_occur(), "[a/b]"))
arbre2 = ArbreB(c, d, sommet=Sommet(c.get_occur() + d.get_occur(), "[c/d]"))


print(fusion(arbre, arbre2).get_fg())
