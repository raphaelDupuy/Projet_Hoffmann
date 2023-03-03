class Sommet:

    def __init__(self, occur, tag=None):
        self.tag = tag
        self.occur = occur

    # Permet de changer le tag d'un sommet
    def retag(self, new):
        self.tag = new
    
    def get_chemin(self):
        raise NotImplementedError

    # Getter de l'attribut 'occur'
    def get_occur(self):
        return self.occur

    # Getter de l'attribut 'tag'
    def get_tag(self):
        return self.tag

