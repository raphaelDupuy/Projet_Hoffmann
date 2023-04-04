import tkinter as tk
from sommet import Sommet
from arbreB import ArbreB
from math import log2
import codecs
from bibliothèque import *
from tkinter.filedialog import askopenfilename 
from tkinter.messagebox import askquestion
from os import remove


screen = None
dictionnaire = {}


def draw_tree(arbre : ArbreB,x,y, ext):
    screen.create_text(x, y, text= str(arbre.get_occur()))
    
    fg = arbre.get_fg()
    fg_tag = fg.get_tag()
    fd = arbre.get_fd()
    fd_tag = fd.get_tag()
    deplacement = 100 *ext

    screen.create_line((x,y+10),(x+ deplacement, y+90))
    screen.create_line((x,y+10),(x- deplacement, y+90))
    if isinstance(fd, ArbreB):
       draw_tree(fd, x + deplacement, y + 100, ext /2)
    else:
        screen.create_text(x + deplacement, y + 100, text= fd_tag, fill= "red")
    if isinstance(fg, ArbreB):
        draw_tree(fg,x - deplacement, y + 100, ext /2)
    else:
        screen.create_text(x - deplacement , y + 100, text= fg_tag, fill= "red")


def hauteur(arbre: ArbreB):
    if isinstance(arbre, Sommet):
        return 0
    else:
        return 1 + max(hauteur(arbre.get_fd()),hauteur(arbre.get_fg()))




def creation_screen(arbre : ArbreB ):
    global screen, screen_width, screen_height
    if screen:
        for widget in screen.find_all():
            screen.delete(widget)
    h  = hauteur(arbre) 
    et = h * log2(h)
    WIDTH, HEIGHT = 200*et, 200*et
    screen = tk.Canvas(frame,  width= screen_width , height=  screen_height, bg= "white",
                        scrollregion=(-WIDTH*4,0,WIDTH*6,HEIGHT))
    screen.grid(column = 1, row = 0 )
    hbar=tk.Scrollbar(frame,orient="horizontal", command= screen.xview, width= 25)
    hbar.grid(row= 5, column=1, sticky="we")

    vbar=tk.Scrollbar(frame,orient="vertical", command= screen.yview , width= 25)
    vbar.grid(row= 0, column=2, sticky="ns")
    screen.config( yscrollcommand= vbar.set, xscrollcommand= hbar.set)
    draw_tree(arbre, WIDTH, 100, et )
    

def afficher_texte(arbre : ArbreB):

    # codecs.open(fichier +".txt","r", encoding="utf-8").read(), codecs.open(fichier +"c.txt","r", encoding="utf-8").read())
    global screen, screen_width, screen_height
    if screen:
        for widget in screen.find_all():
            screen.delete(widget)
        screen.config(scrollregion=(0,0,4000,1600))
    else:
        screen = tk.Canvas(frame, width= screen_width , height=  screen_height ,
                            bg= "white",  scrollregion=(0,0,4000,1600))
        screen.grid(column = 1, row = 0)

    entree = askopenfilename(initialdir=".", title="Select file", 
                             filetypes=(("text files", "*.txt"),
                                         ("all files", "*.*")))[:-4]

    if askquestion("Question", "le texte selectioné est-il codé ?") =="no":
        result = codage(arbre, entree)
        texteentre = codecs.open(entree +".txt","r", encoding="utf-8").read()
        screen.create_text(screen_width // 4 ,screen_height // 2, text= texteentre,
                            width= 500, font= ("Arial", 12), anchor= "center")
        screen.create_text(3*screen_width//4 ,screen_height // 2, text= result,
                            width= 500, font= ("Arial", 12), anchor= "center")
    else:
        result = decodage(arbre, entree)
        texteentre = codecs.open(entree +".txt","r", encoding="utf-8").read()
        screen.create_text(screen_width // 4 ,screen_height // 2, text=texteentre,
                            width= 500, font= ("Arial", 12), anchor= "center")
        screen.create_text(3*screen_width//4 ,screen_height // 2, text= result,
                            width= 500, font= ("Arial", 12), anchor= "center")

    hbar=tk.Scrollbar(frame,orient="horizontal",
                       command= screen.xview, width= 25)
    hbar.grid(row= 5, column=1, sticky="we")

    vbar=tk.Scrollbar(frame,orient="vertical",
                       command= screen.yview , width= 25)
    vbar.grid(row= 0, column=2, sticky="ns")
    


def spawn_tree():  
    global frame, screen_width, screen_height
    

    racine = tk.Tk()
    screen_width = int(racine.winfo_screenwidth()*0.9)
    screen_height = int(racine.winfo_screenheight()*0.8)
    creation_arbre = tk.Button(racine, text=" creation arbre")
    creation_arbre.grid(column = 0,  row = 0, )
    affiche_text = tk.Button(racine, text=" afficher texte")
    affiche_text.grid(column = 1,  row = 0) 

    fichier = askopenfilename(initialdir=".", title="Select file", 
                              filetypes=(("text files", "*.txt"),
                                         ("all files", "*.*")))[:-4]
    
    liste_sommet = analyse(fichier)
    arbre = build_tree(liste_sommet)
    creation_dictionnaire(arbre)

    affiche_text.bind("<Button-1>", lambda event: afficher_texte(arbre))
    creation_arbre.bind("<Button-1>", lambda event: creation_screen(arbre))
    frame = tk.Frame(racine)
    frame.grid(column = 0, row = 2, columnspan = 2)
    frame.columnconfigure(1, weight= 1)
    frame.rowconfigure(1, weight= 1)

    frame.mainloop()
    remove(fichier+"c.txt")

