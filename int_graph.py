import tkinter as tk
from sommet import Sommet
from arbreB import ArbreB
from math import log2




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
    screen = tk.Canvas(frame, width= 1000 , height=  800 , bg= "white",
                        scrollregion=(-WIDTH*4,0,WIDTH*6,HEIGHT))
    screen.grid(column = 1, row = 0, )
    hbar=tk.Scrollbar(frame,orient="horizontal", command= screen.xview, width= 25)
    hbar.grid(row= 1, column=1, sticky="we")

    vbar=tk.Scrollbar(frame,orient="vertical", command= screen.yview , width= 25)
    vbar.grid(row= 0, column=2, sticky="ns")
    screen.config( yscrollcommand= vbar.set, xscrollcommand= hbar.set)  
    draw_tree(arbre, WIDTH, 100, et )
    
def spawn_tree(arbre : ArbreB):  
    racine = tk.Tk()

    frame = tk.Frame(racine)
    frame.pack(fill="both", expand= True)
    frame.columnconfigure(1, weight= 1)
    frame.rowconfigure(1, weight= 1)
    menu = tk.Button(frame, text=" creation arbre")
    menu.grid(column = 0,  row = 0 )
    creation_arbre(arbre)
    frame.mainloop()



