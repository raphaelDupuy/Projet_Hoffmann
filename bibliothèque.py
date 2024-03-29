from sommet import Sommet
from arbreB import ArbreB
import codecs
total = 0
dictionnaire = {}

def fusion(arbreA, arbreB):
    """Fonction de fusion de deux arbres binaires
    (retourne un nouvel arbre avec une copie des 
    arbres à fusioner en fg et fd)"""
    copA, copB = arbreA.copie(), arbreB.copie()
    new = ArbreB(copA, copB, sommet=Sommet(arbreA.get_occur() + arbreB.get_occur(), f"[{arbreA.get_tag()} / {copB.get_tag()}]"))
    return new

def suppr(arbreB, noeud) -> None:
    """Supprime un noeud donné dans un arbreB donné"""

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

def extract(file):
    """Prend en entrée un fichier texte et retourne une liste de sommets correspondant 
        aux charactères dans le fichier"""
    global total, arbre1, dictionnaire
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

def percentage(data):
    """Prend en entrée une liste d'objets sommets et le nombre total de charactères dans le fichier
        à analyser et retourne un dictionnaire avec le char en clé et son pourcentage en value"""
    global total
    for sommet in data:
        sommet.occur = round((sommet.get_occur()/total)*100,2)
    return data

def analyse(file):
    """Prends un fichier et retourne une liste avec tous les sommets 
        qui correspondent aux charactères du fichier"""
    data = extract(file)
    return percentage(data)

arbre1 = None
def build_tree(list_sommet):
    """Retourne un arbreB correspondant aux sommets donnés dans la liste en entrée"""
    if len(list_sommet) > 1:
        list_sommet.sort(key= lambda x: x.get_occur())
        small = list_sommet[1]
        smaller = list_sommet[0]
        sous_arbre = ArbreB(list_sommet.pop(list_sommet.index(small)), list_sommet.pop(list_sommet.index(smaller)), Sommet(round(small.get_occur() + smaller.get_occur(),2)))
        list_sommet.append(sous_arbre)
        return build_tree(list_sommet)

    else:
        return list_sommet[0]

def creation_dictionnaire(arbre: ArbreB) -> None:
    """Ajoute dans le dictionnaire les chemins vers les charactères
        via l'arbre de hoffmann"""
    for key in dictionnaire.keys():
        dictionnaire[key] = arbre.find(key)

def codage(arbre,file):
    """Renvoie le texte contenu dans le fichier, encodé par l'arbre donné"""
    with codecs.open(file+".txt","r", encoding="utf-8") as fichier:
        with open(file+"c.txt","w") as fichier2:
            textecode = ""
            for line in fichier:
                for letter in line:
                    if  letter.lower() not in dictionnaire.keys():
                        return " erreur l'arbre n'est pas codé par ce texte"
                    fichier2.write(dictionnaire[letter.lower()])
                    textecode += dictionnaire[letter.lower()]
    return textecode

def decodage(arbre,file):
    """Décode le texte donné avec l'arbre donné"""
    with open(file+".txt","r") as fichier:
        racine = arbre
        textecode = fichier.read()
        texte = ""

        for char in textecode:
            textecode = textecode[1:]

            if char == "0":
                arbre = arbre.get_fg()

            elif char == "1":
                arbre = arbre.get_fd()

            if isinstance(arbre, Sommet):
                texte += arbre.get_tag()

                if len(textecode) > 0:
                    arbre = racine

        if isinstance(arbre, Sommet):
            return texte
        
        else:
            return "erreur ce texte n'est pas codé par cet arbre"
