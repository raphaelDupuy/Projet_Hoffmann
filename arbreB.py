class ArbreB:
    
    def __init__(self, fg, fd, père):
        self.content = ([fg, fd], père)

    def __add__(self, arb):
        pass

    # Getter fils gauche, retourne le fils gauche d'un arbreB
    def get_fg(self):
        return self.content[0][0]

    # Getter fils droit, retourne le fils droit d'un arbreB
    def get_fd(self):
        return self.content[0][1]

    # Insère un sommet avec un tag dans un arbreB
    def instert(self, sommet):
        pass

    # Supprime un sommet dans un arbreB
    def suppr(self, sommet):
        try:
            self.content.remove(sommet)
        except ValueError:
            pass

    # Trouve un charractère dans un arbreB
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

        
    