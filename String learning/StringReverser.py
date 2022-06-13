"""

mot = input("Entrez un mot a renverser: ")
mot_renverser = ""

for compteur in range(1, len(mot)+1):
    mot_renverser += mot[len(mot)-compteur]

print(mot_renverser)

"""
# Methode plus rapide.
mot = input("Entrez un mot a renverser: ")
# Ici on passe sur l'ensemble des caracteres avec un iterateur de -1 en partant de la fin.
mot_renverser = mot[::-1]

print(mot_renverser)
