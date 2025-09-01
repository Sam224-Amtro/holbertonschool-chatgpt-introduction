#!/usr/bin/python3

# "sys" permet de récupérer ce qu’on écrit après le nom du fichier quand on lance le programme
import sys

# On crée une fonction qui calcule la factorielle
def factorial(n):
    result = 1 # On commence avec 1
    while n > 1: # Tant que n est plus grand que 1
        result *= n # On multiplie le résultat par n
        n -= 1 # Décrément n pour éviter une boucle infinie
    return result # Quand c’est fini, on renvoie le résultat

# Ici on prend le nombre écrit après le nom du fichier (sys.argv[1]),
# on le transforme en entier (int), et on calcule sa factorielle
f = factorial(int(sys.argv[1]))
# On affiche le résultat
print(f)
