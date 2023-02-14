class Sommet:

    def __init__(self, nb, chemin, tag=None):
        self.tag = tag
        self.nb = nb
        self.chemin = chemin

    def retag(self, new):
        self.tag = new

    def get_chemin(self):
        return self.chemin

    def get_tag(self):
        return self.tag

