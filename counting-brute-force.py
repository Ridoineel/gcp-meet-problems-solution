
"""
	On vous donne un texte.
	vous devez écrire un programme qui affiche le
	nombre d'occurrence de chaque lettre dans le
	texte.
"""

import sys

# redirection des flux d'entrées
# vers le fichier ...
sys.stdin = open("inputs/input1.txt", "r")

def main():
	text = input()
	# text = "ridoine"

	# ensemble 
	# des carcactères de text
	# sans doublons
	text2 = set(text) # n

	# O(n**2)

	for c in text2: # n
		occur = text.count(c) # n

		print(c, occur)

if __name__ == '__main__':
	main()