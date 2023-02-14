class ArbreB:
    
    def __init__(self, content):
        self.content = content

    def instert(self, sommet):
        self.content.append(sommet)

    def suppr(self, sommet):
        try:
            self.content.remove(sommet)
        except ValueError:
            pass

