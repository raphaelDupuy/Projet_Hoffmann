import tkinter as tk
from sommet import Sommet
from arbreB import ArbreB
from math import log2
import codecs
from bibliothèque import *
from tkinter.filedialog import askopenfilename 
from tkinter.messagebox import askquestion
from tkinter.messagebox import showinfo
from os import remove

screen = None
dictionnaire = {}

def draw_tree(arbre : ArbreB,x,y, ext):
    """ prend en entrée un arbre binaire et dessine l'arbre binaire"""
    screen.create_text(x, y, text= str(arbre.get_occur()))
    
    fg = arbre.get_fg()
    fg_tag = fg.get_tag()
    fd = arbre.get_fd()
    fd_tag = fd.get_tag()
    deplacement = 50*ext

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

def nbr_feuille(arbre: ArbreB):
    """prend en entrée un arbre binaire et renvoie son nombre de feuille"""
    if isinstance(arbre, Sommet):
        return 1
    else:
        return nbr_feuille(arbre.get_fd()) + nbr_feuille(arbre.get_fg())

def creation_screen(arbre : ArbreB ):
    """prend en entrée un arbre binaire et prépare l'écran pour l'affichage de l'arbre"""
    global screen, screen_width, screen_height
    for child in  frame.winfo_children():
       child.destroy()
    et  = nbr_feuille(arbre)  
    WIDTH, HEIGHT = 100*et, 100*et
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
    """prend en entrée un texte et affiche son resultat codé ou décodé"""

    # codecs.open(fichier +".txt","r", encoding="utf-8").read(), codecs.open(fichier +"c.txt","r", encoding="utf-8").read())
    global screen, screen_width, screen_height
    for child in  frame.winfo_children():
       child.destroy()

    print(frame.winfo_children())
    entree = askopenfilename(initialdir=".", title="Select file", 
                             filetypes=(("text files", "*.txt"),
                                         ("all files", "*.*")))[:-4]
    while not entree:
        showinfo("erreur", "veuillez selectionner un fichier")
        entree = askopenfilename(initialdir=".", title="Select file", 
                                 filetypes=(("text files", "*.txt"),
                                            ("all files", "*.*")))[:-4]
    

    if askquestion("Question", "le texte selectionné est-il codé ?") == "no":
        result = codage(arbre, entree)
        texteentre = codecs.open(entree +".txt","r", encoding= "utf-8").read()
      
    else:
        result = decodage(arbre, entree)
        texteentre = codecs.open(entree + ".txt","r", encoding= "utf-8").read()

    entre = tk.Text(frame, wrap="word", width= 100,font = ("Arial", 12))
    entre.grid(column = 0, row = 0)
    sortie = tk.Text(frame, wrap="word", width= 100, font= ("Arial", 12))
    sortie.grid(column = 2, row = 0)
    entre.insert(tk.END, texteentre)
    sortie.insert(tk.END, result)


def spawn_tree():  
    """créé une fenêtre graphique pour manipuler 
    l'arbre binaire ainsi créé"""
    global frame, screen_width, screen_height
    
    racine = tk.Tk()
    racine.title("traitement arbre binaire")
    screen_width = int(racine.winfo_screenwidth()*0.9)
    screen_height = int(racine.winfo_screenheight()*0.8)
    creation_arbre = tk.Button(racine, text=" afficher arbre")
    creation_arbre.grid(column = 0,  row = 0 )
    affiche_text = tk.Button(racine, text=" afficher texte")
    affiche_text.grid(column = 1,  row = 0) 

    fichier = askopenfilename(initialdir=".", title="Select file", 
                              filetypes=(("text files", "*.txt"),
                                         ("all files", "*.*")))[:-4]
    while not fichier:
        showinfo("erreur", "veuillez selectionner un fichier")
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
   

    frame.mainloop()
    remove(fichier+"c.txt")
