from sommet import Sommet
from arbreB import ArbreB

total = 0


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
                    data[low_letter] = 1
                else:
                    data[low_letter] += 1
                total += 1

    classes = []
    for key, value in data.items():
        classes.append(Sommet(value, tag=key))
    return classes


# Prend en entrée une liste d'objets sommets et le nombre total de charactères dans le fichier
# à analyser et retourne un dictionnaire avec le char en clé et son pourcentage en value
def percentage(data):
    global total
    for sommet in data:
        sommet.occur = round((sommet.get_occur()/total)*100,2)
    return data

def tree(data):
    pass

# Fonction principale du programme
def analyse(file):
    data = extract(file)
    return percentage(data)


def getKey(element):
    """indique a la fonction sort() sur quel paramètres elle doit trier la liste"""
    return element.get_occur()


arbre = None
def build_tree(list_sommet):
    """version 1"""
    # """ prends en entré une liste de sommets et crèe un arbre avec,
    #   les  2 sommets dont l'occurence est la plus faible"""
    # global joli_arbre
    # list_sommet = sorted(list_sommet, key=getKey)
    # fg = (list_sommet[0][1][1])
    # fd = (list_sommet[1][1][1])
    # joli_arbre = ArbreB(fd,fg)
    # if isinstance(fg, ArbreB):
    #     fg = fg.get_sommet()
    # if isinstance(fd, ArbreB):
    #     fd = fd.get_sommet()
    # joli_arbre.sommet = Sommet((fg.get_occur() + fd.get_occur() ))
    # list_sommet.append((joli_arbre.get_tag(),(joli_arbre.get_sommet().get_occur(),joli_arbre)))
    # del(list_sommet[:2])

    # if len(list_sommet) != 1:
    #     build_tree(list_sommet)

    """version 2 recursif test"""
    """prend en entrée une liste non triée de sommets"""
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

        sous_arbre = ArbreB(list_sommet.pop(list_sommet.index(small)), list_sommet.pop(list_sommet.index(smaller)), Sommet(small.get_occur() + smaller.get_occur()))
        list_sommet.append(sous_arbre)
        return build_tree(list_sommet)

    else:
        return list_sommet[0]        



def unravell(arbre,n,chemin = ""):
    fg = arbre.get_fg()
    fg_tag = fg.get_tag()
    fd = arbre.get_fd()
    fd_tag = fd.get_tag()

    if fg_tag == None:
        print(n*" ",(fg.get_sommet().get_occur(),fg_tag))
        unravell(fg,n+5,chemin+ "0")
    else:
        print(n*" " ,(fg_tag,fg.get_occur()),chemin + "0")
    
    if fd_tag == None:
        print(n*" ",(fd.get_sommet().get_occur(),fd_tag))
        unravell(fd,n+5,chemin +"1")
    else:
        print(n*" " , (fd_tag,fd.get_occur()), chemin +"1")



# six = ArbreB(f, c, Sommet(f.get_occur() + c.get_occur()))

joli_arbre = analyse("texte.txt")
joli_arbre = build_tree(joli_arbre)
unravell(joli_arbre,3)

