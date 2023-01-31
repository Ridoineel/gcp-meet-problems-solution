
"""
	On vous donne un texte.
	vous devez écrire un programme qui affiche le
	nombre d'occurrence de chaque lettre dans le
	texte.
"""

import sys

# redirection des flux d'entrées
# vers le fichier inputs/input1.txt
sys.stdin = open("inputs/input1.txt", "r")

def main():
	text = input()

if __name__ == '__main__':
	main()