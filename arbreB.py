from sommet import Sommet
class ArbreB:
    
    def __init__(self, fg=None, fd=None, sommet=None):
        """Constructeur de la classe ArbreB"""
        self.content = (fg, fd)
        self.sommet = sommet

    def __iadd__(self, arb):
        """Surcharge de la methode __iadd__ qui ajoute un sommet ou un arbre à l'arbreB"""
        if (t_arb := type(arb)) == ArbreB or t_arb == Sommet:

            fg = self.get_fg()
            père = self
            fg_occ = 0
            fg_tag = None
            while type(fg) == ArbreB:
                père = fg
                fg = fg.get_fg()

            if t_arb == ArbreB:
                return arb.__iadd__(fg)

            elif t_arb == Sommet:

                if fg == None:
                    père.set_content(arb, père.get_fd())
                    père.set_tag(f"[{arb.get_tag()}/{père.get_fd().get_tag()}]")
                    
                elif type(fg) == Sommet:
                    fg_occ = fg.get_occur()
                    fg_tag = fg.get_tag()
                    noeud = ArbreB(arb, fg, Sommet(arb.get_occur() + fg_occ, f"[{arb.get_tag()}/{fg_tag}]"))
                    père.set_content(noeud, père.get_fd())
                    père.set_tag(f"[{noeud.get_tag()}/{père.get_fd().get_tag()}]")
                return self
        else:
            raise TypeError("Impossible d'ajouter autre chose qu'un arbre ou un sommet")

    def __isub__(self, som: Sommet):
        """Surcharge de la methode __isub__ qui supprime un sommet de l'arbreB"""
        fg = self.get_fg()
        fd = self.get_fd()
        
        if type(fg) == Sommet:
            if fg.get_tag() == som.get_tag():
                self.set_fg(None)
                self.set_tag(f"[None/{self.get_fd().get_tag()}]")
                return self

        elif type(fg) == ArbreB:
            self.set_fg(self.get_fg().__isub__(som))
            return self
        
        if type(fd) == Sommet:
            if fd.get_tag() == som.get_tag():
                self.set_fd(None)
                self.set_tag(f"[{self.get_fd().get_tag()}/None]")
                return self

        elif type(fd) == ArbreB:
            self.set_fg(self.get_fd().__isub__(som))
            return self

    def __str__(self):
        """Surcharge de la méthode __str__ pour afficher l'arbre"""
        fg, fd = None, None

        if self.content[0] != None:
            fg = self.content[0].get_tag()

        if self.content[1] != None:
            fd = self.content[1].get_tag()

        if (tag := self.get_tag()) != None:
            return f"fg: {fg}, fd: {fd}, tag: {tag}"
        
        else:
            return f"fg: {fg}, fd: {fd}"

    def copie(self):
        """Methode de copie de l'arbreB et ses déscendants"""
        cop_fg, cop_fd = None, None

        if (fg := self.get_fg()) != None:
            cop_fg = fg.copie()

        if (fd := self.get_fd()) != None:
            cop_fd = fd.copie()

        return ArbreB(cop_fg, cop_fd, self.get_sommet().copie())
    
    def get_occur(self):
        """Getter de l'attribut 'occur'"""
        return self.sommet.get_occur()
    
    def get_sommet(self) -> Sommet:
        """Getter de l'attribut 'sommet'"""
        return self.sommet

    def get_fg(self):
        """Getter de l'attribut 'fils gauche'"""
        return self.content[0]

    def get_fd(self):
        """Getter de l'attribut 'fils droit'"""
        return self.content[1]

    def get_tag(self):
        """Getter de l'attribut 'tag' du sommet associé à la racine de l'arbreB"""
        if self.sommet != None:
            return self.sommet.get_tag()
        else:
            return None

    def get_content(self) -> tuple:
        """Getter de l'attribut 'content'"""
        return self.content
    
    def set_occur(self, occur) -> None:
        """Setter de l'attribut 'occur' du sommet associé à la racine de l'arbreB"""
        self.sommet.set_occur(occur)

    def set_sommet(self, sommet: Sommet) -> None:
        """Setter de l'attribut 'sommet' associé à la racine de l'arbreB"""
        self.sommet = sommet

    def set_fg(self, fg) -> None:
        """Setter de l'attribut 'fils gauche'"""
        self.set_content(fg, self.content[1])

    def set_fd(self, fd) -> None:
        """Setter de l'attribut 'fils droit'"""
        self.set_content(self.content[0], fd)

    def set_tag(self, tag) -> None:
        """Setter de l'attribut 'tag' du sommet associé à la racine de l'arbreB"""
        self.sommet.retag(tag)

    def set_content(self, fg, fd) -> None:
        """Setter de l'attribut 'content'"""
        self.content = (fg, fd)

    def find(self, char, chemin=''):
        """Trouve un charractère dans l'arbreB"""
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
    