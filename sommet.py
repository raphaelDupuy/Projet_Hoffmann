class Sommet:

    def __init__(self, occur, tag=None):
        """Constructeur de la classe Sommet"""
        self.tag = tag
        self.occur = occur

    def get_occur(self):
        """Getter de l'attribut 'occur'"""
        return self.occur

    def get_tag(self) -> str:
        """Getter de l'attribut 'tag'"""
        return self.tag
    
    def set_occur(self, occur) -> None:
        """Setter de l'attribut 'occur'"""
        self.occur = occur

    def retag(self, new: str) -> None:
        """Permet de changer le tag d'un sommet"""
        self.tag = new
    
    def __str__(self) -> str:
        """Surcharge de la fonction __str__ pour afficher le sommet"""
        return f"occur: {self.get_occur()}, tag: {self.get_tag()}"

    def copie(self):
        """Méthode de copie du sommet"""
        return Sommet(self.get_occur(), self.get_tag())
