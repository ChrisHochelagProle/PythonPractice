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

mot_entrer = input("Entrer un palindrome: ")
# on gere si lutilisateur met un majuscule quelque part en mettant tout lowercase
mot_a_evaluer = mot_entrer.lower()
is_palindrome = False
mot_renverser = ""
for compteur in range(1, len(mot_a_evaluer) + 1):
    mot_renverser += mot_a_evaluer[len(mot_a_evaluer) - compteur]

if mot_a_evaluer == mot_renverser:
    is_palindrome = True

print("Votre mot est un palindrome?: ", is_palindrome)
