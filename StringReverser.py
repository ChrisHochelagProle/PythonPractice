mot = input("Entrez un mot a renverser: ")
mot_renverser = ""

for compteur in range(1, len(mot)+1):
    mot_renverser += mot[len(mot)-compteur]

print(mot_renverser)