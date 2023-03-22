from arbreB import ArbreB
from sommet import Sommet


# c = Sommet(2, "c")
# e = Sommet(4, "e")
# f = Sommet(1, "f")
# sp = Sommet(1, " ")
# i = Sommet(3, "i")
# o = Sommet(3, "o")
# t = Sommet(5, "t")

# data = [c, e, f, sp, i, o, t]

feuille1 = Sommet(1, '1')
feuille2 = Sommet(2, '2')
feuille3 = Sommet(3, '3')
noeud1 = ArbreB(feuille1, feuille2, Sommet(10, "noeud1"))
root = ArbreB(noeud1, feuille3, Sommet(0, "root"))

print(root.find('root'))

