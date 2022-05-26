"""

Pseudo code
Nom de lalgorithme: verificateur de palindrome

Entrees: mot_a_evaluer (string)
Sortie: is_palindrome (booleen)

afficher "Entrer un palindrome: "
lire mot_a_evaluer

mot_renverser <-- ""
is_palindrome <-- Faux

pour compteur dans 1 a longueur de mot_a_evaluer + 1
    mot_renverser += mot_a_evaluer[len de mot_a_evaluer - compteur]

si mot_renverser == mot_a_evaluer
    is_palindrome <-- Vrai

afficher "Votre mot est un palindrome: ", is_palindrome, "."

"""

# Imports
import os.path

# Fonctions


def inverser(mot):
    mot_renverser = ""
    for compteur in range(1, len(mot) + 1):
        mot_renverser += mot[len(mot) - compteur]
    return mot_renverser


def isPalindrome(mot):
    if mot == inverser(mot):
        return True
    else:
        return False

# Informations generales pour mise en page

cours = "Concepts de programmation 1"
nom = "Desrosiers Mondor"
prenom = "Christopher"

# Variables pour le pseudo code


# Contantes
nom_de_algorithme = os.path.basename(__file__)
message_ouverture = 30 * "*" + f" Voici le resultat du programme: {nom_de_algorithme} " + 30 * "*"
message_fermeture = 30 * "*" + f" Codé par {prenom} {nom} dans le cadre du cours {cours} " + 30 * "*"

# Entrees

# Sorties

# Mise en page

print(message_ouverture)

# Mettre le code sous ce commentaire
mot_entrer = input("Entrer un palindrome: ")
# on gere si lutilisateur met un majuscule quelque part en mettant tout lowercase
mot_a_evaluer = mot_entrer.lower()

"""
mot_renverser = ""
for compteur in range(1, len(mot_a_evaluer) + 1):
    mot_renverser += mot_a_evaluer[len(mot_a_evaluer) - compteur]
"""

print("Votre mot est un palindrome?: ", isPalindrome(mot_a_evaluer))


# Message footer
print(message_fermeture)

