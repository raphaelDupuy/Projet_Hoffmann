import tkinter as tk
from sommet import Sommet
from arbreB import ArbreB
from math import log2




def draw_tree(arbre : ArbreB,x,y, ext):
    screen.create_text(x, y, text= str(arbre.get_occur()))
    print(ext, hauteur(arbre))
    
    fg = arbre.get_fg()
    fg_tag = fg.get_tag()
    fd = arbre.get_fd()
    fd_tag = fd.get_tag()
    deplacement = 100 *ext

    screen.create_line((x,y),(x+ deplacement, y+100))
    screen.create_line((x,y),(x- deplacement, y+100))
    if isinstance(fd, ArbreB):
       draw_tree(fd, x + deplacement, y + 100, ext /2)
    else:
        screen.create_text(x + deplacement, y + 100, text= fd_tag)
    if isinstance(fg, ArbreB):
        draw_tree(fg,x - deplacement, y + 100, ext /2)
    else:
        screen.create_text(x - deplacement , y + 100, text= fg_tag)


def hauteur(arbre: ArbreB):
    if isinstance(arbre, Sommet):
        return 0
    else:
        return 1 + max(hauteur(arbre.get_fd()),hauteur(arbre.get_fg()))




def creation_arbre(arbre : ArbreB ):
    global screen
    h  = hauteur(arbre) 
    et = h * log2(h)
    WIDTH, HEIGHT = 200*et, 200*et
    screen = tk.Canvas(racine , width= 1000 , height=  800 , bg= "white",
                        scrollregion=(-WIDTH*4,0,WIDTH*6,HEIGHT))
    screen.grid(column = 1, row = 0, )
    hbar=tk.Scrollbar(racine,orient="horizontal", command= screen.xview, width= 25)
    hbar.grid(row= 1, column=1, sticky="we")

    vbar=tk.Scrollbar(racine,orient="vertical", command= screen.yview , width= 25)
    vbar.grid(row= 0, column=2, sticky="ns")
    screen.config( yscrollcommand= vbar.set, xscrollcommand= hbar.set)  
    draw_tree(arbre, WIDTH, 100, et )

    
        




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
    """version 2 recursif test"""
    """prend en entrée une liste non triée de sommets"""
    if len(list_sommet) > 1:
        list_sommet.sort( key = getKey)
        small = list_sommet[1]
        small_occur = small.get_occur()

        smaller = list_sommet[0]
        smaller_occur = smaller.get_occur()


        sous_arbre = ArbreB(list_sommet.pop(list_sommet.index(small)), list_sommet.pop(list_sommet.index(smaller)), Sommet(round(small.get_occur() + smaller.get_occur(),2)))
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
        print(n*" ",(fg.get_occur(),fg_tag))
        unravell(fg,n+5,chemin+ "0")
    else:
        print(n*" " ,(fg_tag,fg.get_occur()),chemin + "0")
    
    if fd_tag == None:
        print(n*" ",(fd.get_occur(),fd_tag))
        unravell(fd,n+5,chemin +"1")
    else:
        print(n*" " , (fd_tag,fd.get_occur()), chemin +"1")





joli_arbre = analyse("texte.txt")
joli_arbre = build_tree(joli_arbre)
unravell(joli_arbre, 4)
    


racine = tk.Tk()

menu = tk.Button(racine, text=" creation arbre")
menu.grid(column = 0,  row = 0 )
creation_arbre(joli_arbre)
racine.mainloop()

