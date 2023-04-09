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
    
    def __str__(self):
        fg, fd = None, None

        if self.content[0] != None:
            fg = self.content[0].get_tag()

        
        if self.content[1] != None:
            fd = self.content[1].get_tag()

        return f"fg: {fg}, fd: {fd}"

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
    
    def get_sommet(self):
        return self.sommet
    
    def set_content(self, fg, fd):
        self.content = (fg, fd)


    # Supprime le sommet de l'arbreB
    def suppr(self):

        fg = self.get_fg()
        fd = self.get_fd()
        
        if type(fg) == Sommet:
            self.sommet = fg
            self.content = (None, self.content[1])
            del fg

        elif type(fd) == Sommet:
            self.sommet = fd
            self.content = (self.content[0], None)
            del fd

        elif type(fg) == ArbreB:
            self.sommet = fg.get_sommet()
            fg.suppr()

        elif type(fd) == ArbreB:
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
            essai = fg.find(char, chemin + "0")
            if essai != None:
                return essai
        
        if type(fd) == ArbreB:
            essai = fd.find(char, chemin + "1")
            if essai != None:
                return essai
    