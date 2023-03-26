from sommet import Sommet
from arbreB import ArbreB
import codecs
total = 0
dictionnaire = {}


def suppr(arbreB, noeud):

    if arbreB.get_tag() == noeud:
        if type(arbreB) == ArbreB:
            return arbreB.suppr()
        else:
            return None

    else:
        fg = arbreB.get_fg()
        fd = arbreB.get_fd()

        if type(fg) == Sommet:
            print(f"fg est sommet {fg.get_tag()}")
            if fg.get_tag() == noeud:
                arbreB.set_content(fg=None, fd=fd)
                print("done")

        if type(fd) == Sommet:
            print(f"fd est sommet {fd.get_tag()}")
            if fd.get_tag() == noeud:
                arbreB.set_content(fg=fg, fd=None)
                print("done")
        
        if type(fg) == ArbreB:
            print("continue sur fg")
            suppr(fg, noeud)

        if type(fd) == ArbreB:
            print("continue sur fd")
            suppr(fd, noeud)


# Prend en entrée un fichier texte et retourne une liste de sommets correspondant 
# aux charactères dans le fichier
def extract(file):
    global total, arbre, dictionnaire
    data = {}
    with codecs.open(file+".txt", "r", encoding= "utf-8") as fichier:
        for line in fichier:
            for letter in line:
                low_letter = letter.lower()
                if low_letter not in data.keys():
                    data[low_letter] = 1
                else:
                    data[low_letter] += 1
                dictionnaire[low_letter] = ""
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
        sorted(list_sommet, key=getKey)
        small = list_sommet[1]
        smaller = list_sommet[0]
        sous_arbre = ArbreB(list_sommet.pop(list_sommet.index(small)), list_sommet.pop(list_sommet.index(smaller)), Sommet(small.get_occur() + smaller.get_occur()))
        list_sommet.append(sous_arbre)
        return build_tree(list_sommet)

    else:
        return list_sommet[0]
    


def creation_dictionnaire(arbre: ArbreB):
    for key in dictionnaire.keys():
        dictionnaire[key] = arbre.find(key)


def codage(arbre,file):
    with codecs.open(file+".txt","r", encoding="utf-8") as fichier:
        with open(file+"c.txt","w") as fichier2:
            for line in fichier:
                for letter in line:
                    fichier2.write(dictionnaire[letter.lower()])
   


def decodage(arbre,file):
    with open("file.txt","r") as fichier:
        with codecs.open("test3.txt","w", encoding= "utf-8") as fichier2:
            racine = arbre
            for char in fichier.read():
                if char == "0":
                    arbre = arbre.get_fg()
                elif char == "1":
                    arbre = arbre.get_fd()
                if arbre.get_tag() != None:
                    fichier2.write(arbre.get_tag())
                    arbre = racine
                    
                

