from sommet import Sommet
from arbreB import ArbreB

total = 0

# Prend en entrée un fichier texte et retourne une liste de sommets correspondant 
# aux charactères dans le fichier
def extract(file):
    global total
    data = {}
    with open(file, "r") as fichier:
        for line in fichier:
            for letter in line:
                low_letter = letter.lower()
                if low_letter not in data.keys():
                    data[letter] = 1
                else:
                    data[letter] += 1
                total += 1

    classes = []
    for key, value in data.items():
        classes.append(Sommet(value, tag=key))
    return classes


# Prend en entrée une liste d'objets sommets et le nombre total de charactères dans le fichier
# à analyser et retourne un dictionnaire avec le char en clé et son pourcentage en value
def percentage(data):
    global total
    percentages = {}
    for sommet in data:
        tag, nb = sommet.get_tag(), sommet.get_occur()
        percent = (nb / total) * 100
        percentages[tag] = round(percent, 2)
    return percentages


def tree(data):
    pass

# Fonction principale du programme
def analyse(file):
    data = extract(file)
    print(percentage(data))


joli_arbre = ArbreB

analyse("texte.txt")











