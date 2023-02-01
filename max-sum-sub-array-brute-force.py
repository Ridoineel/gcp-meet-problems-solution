"""
	On vous donne un tableau d’entiers
	relatifs.
	Trouver le sous-tableau avec la
	plus grande somme et afficher
	cette somme.

	Par brute force: O(n**3)
"""

import sys

# redirection des flux d'entrées
# vers le fichier inputs/input2.txt
sys.stdin = open("inputs/input2.txt", "r")

def main():
	L = [int(i) for i in input().split()]
	n = len(L)
	maxSum = float("-inf")

	# on génère tous les sous
	# tableaux tout en calculant 
	# leur somme et en mettant à jour
	# la somme maximale
	for i in range(n):
		for j in range(i, n):
			sub_array_sum = sum(L[k] for k in range(i, j + 1))

			maxSum = max(maxSum, sub_array_sum)

	print(maxSum)

if __name__ == '__main__':
	main()