"""
Entrees : prenom (string), nom (string)
Sorties : initiales (String)

afficher "Entrer votre prenom et nom de famille: "
lire prenomLu, nomLu
initiales = prenomLu[0] + nomLu[0]

afficher "Vos initiales sont: ", intiales
"""

"""
prenom = input("Entrez votre prenom: ")
nom = input("Entres votre nom: ")
initiales = prenom[0] + nom[0]
print("Vos initiales: " + initiales)
"""

# Version qui prend en compte les noms composes - A finir plus tard.
# nom = input("Entrez votre nom: ")
nom = "Patrick Denver Troy Ground"
initiales = ""
""" Tests
print(nom.find(" "))
partie1 = nom[0:11]
reste = nom[12:]
print(reste)
nom = "Mondor"
print(nom.find(" "))
"""

# Code pour n<importe quel nom
# On va couper a chaque espace donc on trouve combien il y a d<espace dans le nom
nombre_espaces = nom.count(" ")
# print(nombre_espaces)
# on va isoler liniatiale de chaque mot en faisant laction x (nombre despaces) fois
for compteur in range(nombre_espaces+1):
    # tant quil y a des espaces
    if compteur != nombre_espaces:
        partie_analyse = nom[0:nom.find(" ")]
    else:
        partie_analyse = nom
    # print(partie_analyse)
    initiale = partie_analyse[0]
    indice_prochain_nom = int(nom.find(" ")) + 1
    nom = nom[indice_prochain_nom:]
    # print(nom)
    initiales += initiale

print(initiales)
