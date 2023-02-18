class ArbreB:
    
    def __init__(self, fg, fd, sommet = None, tag=None, père=None):
        self.content = (fg, fd)
        self.père = père
        self.sommet = sommet
        self.tag = tag

    def __add__(self, arb):
        pass
    
    # Getter de l'attribut 'sommet'
    def get_sommet(self):
        return self.sommet

    # Getter de l'attribut 'fils droit'
    def get_fg(self):
        return self.content[0]

    # Getter de l'attribut 'fils droit'
    def get_fd(self):
        return self.content[1]

    def get_tag(self):
        return self.tag
    
    def get_père(self):
        return self.père
    
    def get_sommet(self):
        return self.sommet

    # Insère un sommet avec un tag dans l'arbreB
    def instert(self, sommet):
        pass

    # Supprime un sommet de l'arbreB
    def suppr(self, sommet):
        try:
            self.content.remove(sommet)
        except ValueError:
            pass

    # Trouve un charractère dans l'arbreB
    def find(self, char):

        fg = self.get_fg()
        fg_tag = fg.get_tag()

        fd = self.get_fd()
        fd_tag = fd.get_tag()

        if fg_tag != None:
            if fg_tag == char:
                return fg.get_chemin()
        else:
            fg.find(char)
        
        if fd_tag != None:
            if fd_tag == char:
                return fd.get_chemin()
        else:
            fd.find(char)

        
    