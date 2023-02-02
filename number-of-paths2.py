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

cache = {}

def explore(i, j, targetI, targetJ):

	if (i, j) not in cache:
		if i < 0 or i > targetI or j < 0 or j > targetJ:
			return 0

		if i == targetI and j == targetJ:
			return 1

		cache[i, j] = explore(i + 1, j, targetI, targetJ) + explore(i, j + 1, targetI, targetJ) + 

	return cache[i, j]

def main():
	n = int(input())
	ai, aj = map(int, input().split())
	bi, bj = map(int, input().split())

	# si le point B se trouve au dessus
	# ou à gauche de A  on affiche "IMPOSSIBLE"

	if ai > bi or aj > bj:
		print("IMPOSSIBLE")
		exit()

	nbPaths = explore(ai, aj, bi, bj)

	print(nbPaths)

if __name__ == '__main__':
	main()