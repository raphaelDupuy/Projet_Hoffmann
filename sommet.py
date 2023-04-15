class Sommet:

    # Constructeur de la classe Sommet
    def __init__(self, occur, tag=None):
        self.tag = tag
        self.occur = occur

    # Getter de l'attribut 'occur'
    def get_occur(self):
        return self.occur

    # Getter de l'attribut 'tag'
    def get_tag(self) -> str:
        return self.tag
    
    # Setter de l'attribut 'occur'
    def set_occur(self, occur) -> None:
        self.occur = occur

    # Permet de changer le tag d'un sommet
    def retag(self, new: str) -> None:
        self.tag = new
    
    # Surcharge de la fonction __str__ pour afficher le sommet
    def __str__(self) -> str:
        return f"occur: {self.get_occur()}, tag: {self.get_tag()}"
    
    # Méthode de copie du sommet
    def copie(self):
        return Sommet(self.get_occur(), self.get_tag())
