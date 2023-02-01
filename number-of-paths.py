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

paths = 0

def explore(i, j, targetI, targetJ, n):
	global paths

	# s'il le point ne fait pas partie de la grille.
	if i < 0 or i >= n or j < 0 or j >= n:
		return

	# si on a atteint l'arrivé
	# on incrémente le nombre de chemin
	if i == targetI and j == targetJ:
		paths += 1

	# le point en bas
	explore(i + 1, j, targetI, targetJ, n)
	# le point à droite
	explore(i, j + 1, targetI, targetJ, n)

def main():
	n = int(input())
	ai, aj = map(int, input().split())
	bi, bj = map(int, input().split())

	# si le point A se trouve au dessous
	# de B, on affiche "IMPOSSIBLE"

	if ai > bi:
		print("IMPOSSIBLE")
		exit()

	# on explore la grille
	# en commencant par A
	# avec pour arrivé B
	explore(ai, aj, bi, bj, n)

	print(paths)

if __name__ == '__main__':
	main()