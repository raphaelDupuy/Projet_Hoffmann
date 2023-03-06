from arbreB import ArbreB
from sommet import Sommet


c = Sommet(2, "c")
e = Sommet(4, "e")
f = Sommet(1, "f")
sp = Sommet(1, " ")
i = Sommet(3, "i")
o = Sommet(3, "o")
t = Sommet(5, "t")

data = [c, e, f, sp, i, o, t]

arbre = 1

def build_tree(list_sommet):
    global arbre
    if len(list_sommet) > 1:
        small = list_sommet[1]
        small_occur = small.get_occur()

        smaller = list_sommet[0]
        smaller_occur = smaller.get_occur()

        for sommet in list_sommet[2:]:
            occur = sommet.get_occur()

            if occur < smaller_occur:
                smaller = sommet

            elif occur < small_occur:
                small = sommet

        sous_arbre = ArbreB(list_sommet.pop(list_sommet.index(small)), list_sommet.pop(list_sommet.index(smaller)), Sommet(small_occur + smaller_occur))
        list_sommet.append(sous_arbre)
        build_tree(list_sommet)

    else:
        arbre = list_sommet[0]
        pass


def call_tree(list_sommet):
    build_tree(list_sommet)
    return arbre
    
print(call_tree(data))