from sommet import Sommet
class ArbreB:
    
    # Constructeur de la classe ArbreB
    def __init__(self, fg=None, fd=None, sommet=None):
        self.content = (fg, fd)
        self.sommet = sommet

    # Surcharge de la methode __iadd__ qui ajoute un sommet ou un arbre à l'arbreB
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

    # Surcharge de la methode __isub__ qui supprime un sommet de l'arbreB
    def __isub__(self, som: Sommet):

        fg = self.get_fg()
        fd = self.get_fd()
        
        if type(fg) == Sommet:
            print("tst fg")
            if fg.get_tag() == som.get_tag():
                self.set_fg(None)
                return self

        elif type(fg) == ArbreB:
            self.set_fg(self.get_fg().__isub__(som))
            return self
        
        if type(fd) == Sommet:
            print("tst fd")
            if fd.get_tag() == som.get_tag():
                self.set_fd(None)
                return self

        elif type(fd) == ArbreB:
            self.set_fg(self.get_fd().__isub__(som))
            return self

    # Surcharge de la méthode __str__ pour afficher l'arbre
    def __str__(self):
        fg, fd = None, None

        if self.content[0] != None:
            fg = self.content[0].get_tag()

        if self.content[1] != None:
            fd = self.content[1].get_tag()

        if (tag := self.get_tag()) != None:
            return f"fg: {fg}, fd: {fd}, tag: {tag}"
        
        else:
            return f"fg: {fg}, fd: {fd}"
        
    # Methode de copie de l'arbreB et ses déscendants
    def copie(self):
        cop_fg, cop_fd = None, None

        if (fg := self.get_fg()) != None:
            cop_fg = fg.copie()

        if (fd := self.get_fd()) != None:
            cop_fd = fd.copie()

        return ArbreB(cop_fg, cop_fd, self.get_sommet().copie())
    
    # Getter de l'attribut 'occur'
    def get_occur(self):
        return self.sommet.get_occur()
    
    # Getter de l'attribut 'sommet'
    def get_sommet(self) -> Sommet:
        return self.sommet

    # Getter de l'attribut 'fils gauche'
    def get_fg(self):
        return self.content[0]

    # Getter de l'attribut 'fils droit'
    def get_fd(self):
        return self.content[1]

    # Getter de l'attribut 'tag' du sommet associé à la racine de l'arbreB
    def get_tag(self):
        if self.sommet != None:
            return self.sommet.get_tag()
        else:
            print("Sommet = None")

    # Getter de l'attribut 'content'
    def get_content(self) -> tuple:
        return self.content
    
    # Setter de l'attribut 'occur' du sommet associé à la racine de l'arbreB
    def set_occur(self, occur) -> None:
        self.sommet.set_occur(occur)

    # Setter de l'attribut 'sommet' associé à la racine de l'arbreB
    def set_sommet(self, sommet: Sommet) -> None:
        self.sommet = sommet

    # Setter de l'attribut 'fils gauche' 
    def set_fg(self, fg) -> None:
        self.set_content(fg, self.content[1])

    # Setter de l'attribut 'fils droit' 
    def set_fd(self, fd) -> None:
        self.set_content(self.content[0], fd)

    # Setter de l'attribut 'tag' du sommet associé à la racine de l'arbreB
    def set_tag(self, tag) -> None:
        self.sommet.retag(tag)

    # Setter de l'attribut 'content'
    def set_content(self, fg, fd) -> None:
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
    