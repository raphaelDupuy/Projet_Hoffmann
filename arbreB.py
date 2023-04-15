from sommet import Sommet
class ArbreB:
    
    def __init__(self, fg=None, fd=None, sommet=None):
        self.content = (fg, fd)
        self.sommet = sommet

    def __iadd__(self, arb):
        if (t_arb := type(arb)) == ArbreB or t_arb == Sommet:

            fg = self.get_fg()
            père = self
            while type(fg) == ArbreB:
                père = fg
                fg = fg.get_fg()

            if t_arb == ArbreB:
                return arb.__iadd__(fg)

            elif t_arb == Sommet:

                if type(fg) == None:
                    fg_occ = 0
                elif type(fg) == Sommet:
                    fg_occ = fg.get_occur()

                noeud = ArbreB(arb, fg, Sommet(arb.get_occur() + fg_occ, f"{arb.get_tag()} {fg.get_tag()}"))
                père.set_content(noeud, père.get_fd())
                return self
        else:
            raise TypeError("Impossible d'ajouter autre chose qu'un arbre ou un sommet")

    # Supprime le sommet de l'arbreB
    def __isub__(self, som: Sommet):

        fg = self.get_fg()
        fd = self.get_fd()
        
        if type(fg) == Sommet:
            print("tst fg")
            if fg.get_tag() == som.get_tag():
                self.set_content(None, self.content[1])
                return self

        elif type(fg) == ArbreB:
            self.set_content(self.get_fg().__isub__(som), self.get_fd())
            return self
        
        if type(fd) == Sommet:
            print("tst fd")
            if fd.get_tag() == som.get_tag():
                self.set_content(self.content[0], None)
                return self

        elif type(fd) == ArbreB:
            self.set_content(self.get_fg(), self.get_fd().__isub__(som))
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
    