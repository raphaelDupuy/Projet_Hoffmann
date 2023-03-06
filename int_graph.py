import tkinter as tk
import arbreB
import sommet

def creation_arbre(arbre, x = 250,y = 10):
    if arbre.get_père() == None:
        screnn.create_oval((250,10), (270,30), outline="black", width= 2)

    fg = arbre.get_fg()
    fg_tag = fg.get_tag()
    fd = arbre.get_fd()
    fd_tag = fd.get_tag()

    
    if fg_tag == None :
        screnn.create_oval((x-30,y+30), (x+20-30,y+20+ 30), outline="black", width= 2)
        creation_arbre(fg,x-30,y+30)

    
        


# ef unravell(arbre,n,chemin = ""):
#     fg = arbre.get_fg()
#     fg_tag = fg.get_tag()
#     fd = arbre.get_fd()
#     fd_tag = fd.get_tag()

#     if fg_tag == None:
#         chemin += "0"
#         print(n*" ",(fg.get_sommet().get_occur(),fg_tag))
#         unravell(fg,n+5,chemin)
#     else:
#         print(n*" " ,(fg_tag,fg.get_occur()),chemin + "0")
    
#     if fd_tag == None:
#         chemin += "1"
#         print(n*" ",(fd.get_sommet().get_occur(),fd_tag))
#         unravell(fd,n+5,chemin)
#     else:
#         print(n*" " , (fd_tag,fd.get_occur()), chemin +"1")




racine = tk.Tk()

menu = tk.Button(racine, text=" creation arbre")
menu.grid(column = 0, row = 0 )
screnn = tk.Canvas(racine , width= 500, height= 500 , bg= "white")
screnn.grid(column = 1, row = 0, rowspan = 20)
creation_arbre("s")


racine.mainloop()
