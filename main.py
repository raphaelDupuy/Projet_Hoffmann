from sommet import Sommet
from arbreB import ArbreB

total = 0

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
    return data


def analyse(file):
    data = extract(file)
    print(data)
    for key, value in data.items():
        pass


joli_arbre = ArbreB

analyse("texte.txt")











