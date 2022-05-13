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
nom = "Christopher Desrosiers Mondor"
print(nom.find(" "))
partie1 = nom[0:11]
reste = nom[12:]
print(reste)
nom = "Mondor"
print(nom.find(" "))