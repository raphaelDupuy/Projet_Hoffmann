class Sommet:

    def __init__(self, occur, tag=None):
        self.tag = tag
        self.occur = occur

    # Permet de changer le tag d'un sommet
    def retag(self, new):
        self.tag = new

    # Getter de l'attribut 'occur'
    def get_occur(self):
        return self.occur

    # Getter de l'attribut 'tag'
    def get_tag(self):
        return self.tag
    
    def __str__(self) -> str:
        return f"occur: {self.get_occur()}, tag: {self.get_tag()}"
