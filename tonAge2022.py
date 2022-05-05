'''''
Nom de l'algorithme : tonAgeEn2022
Constantes : annee = 2022 = entier
Entrées : anneeLu = entier
Sortie : age = entier

afficher "Entrez votre annee de naissance"
lire anneeLu
age <-- 2022 - anneeLu
afficher "Vous avez: ", age, " ans!"


'''''

anneeCourante = 2022

anneeNaissance = input("Entrez votre annee de naissance: ")

# Pour arriver à l'âge de la personne on soustrait l'année courante à son année de naissance. Si vous êtes né en 2000
# Et qu'on est en 2022, vous avez donc 22 ans (2022 - 2000 donne bien 22)
age = 2022 - int(anneeNaissance)
print("Vous avez: " + str(age) + " ans!")