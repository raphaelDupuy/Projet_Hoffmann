from sommet import Sommet
from arbreB import ArbreB


data = {}

def analyse(file):
    fichier = open(file, 'r+')
    for ligne in fichier:
        print(ligne)

joli_arbre = ArbreB

analyse("texte.txt")











