"""
	On vous donne un tableau d’entiers
	relatifs.
	Trouver le sous-tableau avec la
	plus grande somme et afficher
	cette somme.

	En utilisant l'algorithme de Kadane
"""

import sys

# redirection des flux d'entrées
# vers le fichier inputs/input2.txt
sys.stdin = open("inputs/input2.txt", "r")

def kadane(seq):
	maxSum = local_sum = seq[0]

	for i in range(len(seq)):
		local_sum += seq[i]

		# mise à jour de la valeur max
		maxSum = max(local_sum, maxSum)

		local_sum = max(0, local_sum)

	return maxSum


def main():
	L = [int(i) for i in input().split()]
	maxSum = kadane(L)

	print(maxSum)

if __name__ == '__main__':
	main()