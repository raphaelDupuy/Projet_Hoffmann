from arbreB import ArbreB
from sommet import Sommet
from int_graph import *


# c = Sommet(2, "c")
# e = Sommet(4, "e")
# f = Sommet(1, "f")
# sp = Sommet(1, " ")
# i = Sommet(3, "i")
# o = Sommet(3, "o")
# t = Sommet(5, "t")

# data = [c, e, f, sp, i, o, t]

def suppr(arbreB, noeud):
    if arbreB == noeud:
        arbreB.suppr()
        print(f"done, {arbreB.get_tag()}")
    elif type(arbreB) == ArbreB:
        suppr(arbreB.get_fg(), noeud)
        suppr(arbreB.get_fd(), noeud)


feuille1 = Sommet(1, '1')
feuille2 = Sommet(2, '2')
feuille3 = Sommet(3, '3')
noeud1 = ArbreB(feuille1, feuille2, Sommet(10, "noeud1"))
root = ArbreB(noeud1, feuille3, Sommet(0, "root"))


suppr(root, feuille1)

print(noeud1.content)
