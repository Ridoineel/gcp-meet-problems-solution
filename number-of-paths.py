"""
	On vous donne un tableau d’entiers
	Etant donné deux point A et B dans une grille de taille
	NxN,
	trouver le nombre de chemins possible entre A et B.
	A partir d’un point, les seuls déplacements possibles sont
	soit vers le bas, soit vers la droite.
	(0, 0) sont les coordonnées du coin supérieur gauche.
"""

import sys

# redirection des flux d'entrées
# vers le fichier inputs/input3.txt
sys.stdin = open("inputs/input3.txt", "r")

def main():
	n = int(input())
	ai, aj = map(int, input().split())
	bi, bj = map(int, input().split())

if __name__ == '__main__':
	main()