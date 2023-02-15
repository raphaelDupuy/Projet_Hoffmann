from sommet import Sommet
from arbreB import ArbreB

total = 0
arbre = []

# Prend en entrée un fichier texte et retourne une liste de sommets correspondant 
# aux charactères dans le fichier
def extract(file):
    global total,arbre
    data = {}
    with open(file, "r") as fichier:
        for line in fichier:
            for letter in line:
                low_letter = letter.lower()
                if low_letter not in data.keys():
                    data[letter] = 1
                else:
                    data[letter] += 1
                total += 1

    classes = []
    for key, value in data.items():
        classes.append(Sommet(value, tag=key))
        arbre.append(Sommet(value, tag=key))
    return classes


# Prend en entrée une liste d'objets sommets et le nombre total de charactères dans le fichier
# à analyser et retourne un dictionnaire avec le char en clé et son pourcentage en value
def percentage(data):
    global total
    percentages = {}
    for sommet in data:
        tag, nb = sommet.get_tag(), sommet.get_occur()
        percent = (nb / total) * 100
        percentages[tag] = (round(percent, 2),sommet)
        sommet.occur = round(percent,2)
    return list(percentages.items())


def tree(data):
    pass

# Fonction principale du programme
def analyse(file):
    data = extract(file)
    return percentage(data)


def getKey(element):
    return element[1][0]


def buil_tree(list_sommet):
    global joli_arbre
    list_sommet = sorted(list_sommet, key=getKey)
    fg = (list_sommet[0][1][1])
    fd = (list_sommet[1][1][1])
    joli_arbre = ArbreB(fd,fg,Sommet(fg.get_occur() + fd.get_occur() ))
    list_sommet.append((joli_arbre.get_tag(),(joli_arbre.get_sommet().get_occur(),joli_arbre.get_sommet())))
    del(list_sommet[:2])
    if len(list_sommet) != 1:
        buil_tree(list_sommet)


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



# six = ArbreB(f, c, Sommet(f.get_occur() + c.get_occur()))

joli_arbre = ArbreB
l = analyse("texte.txt")
buil_tree(l)
print(joli_arbre.get_fd())
#unravell(joli_arbre)











