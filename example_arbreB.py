from sommet import Sommet
from arbreB import ArbreB

c = Sommet(2, "c")
e = Sommet(4, "e")
f = Sommet(1, "f")
sp = Sommet(1, " ")
i = Sommet(3, "i")
o = Sommet(3, "o")
t = Sommet(5, "t")

six = ArbreB(f, c, Sommet(f.get_occur() + c.get_occur()))
cinq = ArbreB(o, e, Sommet(o.get_occur() + e.get_occur()))
quatre = ArbreB(six, i, Sommet(six.get_sommet().get_occur() + i.get_occur()))
trois = ArbreB(cinq, sp, Sommet(cinq.get_sommet().get_occur() + sp.get_occur()))
deux = ArbreB(quatre, t, Sommet(quatre.get_sommet().get_occur() + t.get_occur()))
un = ArbreB(deux, trois, deux.get_sommet().get_occur() + trois.get_sommet().get_occur())

def unravell(arbre):
    fg = arbre.get_fg()
    fg_tag = fg.get_tag()
    fd = arbre.get_fd()
    fd_tag = fd.get_tag()

    if fg_tag == None:
        unravell(fg)
    else:
        print(fg_tag)
    
    if fd_tag == None:
        unravell(fd)
    else:
        print(fd_tag)

unravell(un)
