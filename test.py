from arbreB import *
from sommet import *
from bibliothèque import *

a = Sommet(1, "a")
b = Sommet(2, "b")
c = Sommet(1, "c")
d = Sommet(2, "d")
arbre1 = ArbreB(a, b, sommet=Sommet(a.get_occur() + b.get_occur(), "[a/b]"))
arbre2 = ArbreB(c, d, sommet=Sommet(c.get_occur() + d.get_occur(), "[c/d]"))


print(a.get_tag(), a.get_occur())
A = a.copie()
A.retag("A")
A.set_occur("2")
print(f"sommet original: ({a}), copie modifiée: ({A})\n")

print(arbre1)
arbre1 -= a
print(arbre1)
arbre1 += c
print(arbre1)
arbre1 += a
print(arbre1, "\n")

fus = fusion(arbre1, arbre2)

def presente(arb):
    print(f"content: {arb.get_content()}")
    print(f"fg: ({arb.get_fg()})")
    print(f"fd: ({arb.get_fd()})")
    print(f"occurence: {arb.get_occur()}")
    print(f"sommet: ({arb.get_sommet()})")
    print(f"tag: {arb.get_tag()}\n")

presente(fus)
print(fus.find("a"))
print(fus.find("b"))

fus_bis = fus.copie()

fus_bis.set_fg(a)
fus_bis.set_fd(b)
fus_bis.set_tag("[a/b]")
fus_bis.set_sommet(Sommet(0, f"[{a.get_tag()}/{b.get_tag()}]"))
fus_bis.set_occur(a.get_occur() + b.get_occur())

presente(fus_bis)


