
"""
	On vous donne un texte.
	vous devez écrire un programme qui affiche le
	nombre d'occurrence de chaque lettre dans le
	texte.

	En utilisant le hashage
"""

import sys

# redirection des flux d'entrées
# vers le fichier inputs/input1.txt
sys.stdin = open("inputs/input1.txt", "r")

def main():
	text = input()

	hash_table = dict()

	# n O(n)
	for c in text:
		if c not in hash_table:
			hash_table[c] = 1
		else:
			hash_table[c] += 1

	print(hash_table)
	
	for c, n in hash_table.items():
		print(c, n)


if __name__ == '__main__':
	main()