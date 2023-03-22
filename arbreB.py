from sommet import Sommet
class ArbreB:
    
    def __init__(self, fg, fd, sommet=None):
        self.content = (fg, fd)
        self.sommet = sommet

    def __add__(self, arb):
        fg = self.get_fg()
        while type(fg) == ArbreB:
            fg = fg.get_fg()
        noeud = ArbreB(arb, fg, Sommet(arb.get_occur() + fg.get_occur()))
        fg = noeud
        return self

    def get_occur(self):
        return self.sommet.get_occur()
    
    # Getter de l'attribut 'sommet'
    def get_sommet(self):
        return self.sommet

    # Getter de l'attribut 'fils droit'
    def get_fg(self):
        return self.content[0]

    # Getter de l'attribut 'fils droit'
    def get_fd(self):
        return self.content[1]

    # Modif de get tag :
    #   passe de 
        # def get_tag(self):
        #     return self.tag
    # qui ne permet pas de recup le tag du sommet
    # mais celui à l'initialisation du noeud
    # donc modif au cas ou le sommet change (suppr)
    # à:
    def get_tag(self):
        if self.sommet != None:
            return self.sommet.get_tag()
        else:
            print("Sommet = None")
    
    def get_père(self):
        return self.père
    
    def get_sommet(self):
        return self.sommet

    # Insère un sommet avec un tag dans l'arbreB
    def instert(self, sommet):
        pass

    # Supprime le sommet de l'arbreB
    def suppr(self):

        fg = self.get_fg()
        fd = self.get_fd()
        
        if fg == Sommet:
            self.sommet = fg
            self.content[0] = None
            del fg

        elif fd == Sommet:
            self.sommet = fd
            self.content[1] = None
            del fd

        elif fg == ArbreB:
            self.sommet = fg.get_sommet()
            fg.suppr()

        elif fd == ArbreB:
            self.sommet = fd.get_sommet()
            fd.suppr()

        

    # Trouve un charractère dans l'arbreB
    def find(self, char, chemin=''):

        fg = self.get_fg()
        fg_tag = fg.get_tag()

        fd = self.get_fd()
        fd_tag = fd.get_tag()

        if fg_tag == char:
            return chemin + "0"
        elif fd_tag == char:
            return chemin + "1"
        
        if type(fg) == ArbreB:
            return fg.find(char, chemin + "0")
        
        if type(fd) == ArbreB:
            return fd.find(char, chemin + "1")
    