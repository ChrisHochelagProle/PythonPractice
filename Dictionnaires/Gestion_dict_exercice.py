def remplissage(dict):
    while True:
        entree = input("Entrez le nom d'une personne et son age, separes par une virgule: ")
        if entree != "":
            keyvalue = entree.split(',')
            key = str(keyvalue[0])
            value = int(keyvalue[1])
            dict[key] = value
        else:
            break


def consultation(dict):
    while True:
        entree = input("Entrez le nom d'une personne que vous rechercher: ")
        if entree in dict:
            name = entree
            age = dict[entree]
            print("Nom:", name, "-", "age:", age, "ans.")
        else:
            print(dict.get(entree, "Valeur non trouvee"))
            break


dico = dict()
remplissage(dico)
consultation(dico)

#solutionnaire

# Écrire un programme qui crée un mini-système de stockage de données fonctionnant à
# l’aide d’un dictionnaire, dans lequel vous mémoriserez les noms d’une série de personnes, avec leur âge.
#
# · Votre programme devra comporter deux fonctions :
#
# o La première pour le remplissage du dictionnaire, et la seconde pour sa consultation.
#
# o Dans la fonction de remplissage, utilisez une boucle pour accepter les données entrées par l’utilisateur. Dans le
# dictionnaire, le nom de la personne servira de clé d’accès, et l’âge sera exprimé en années (donnée de type entier).
#
# o La fonction de consultation comportera elle aussi une boucle, dans laquelle l’utilisateur pourra fournir un nom
# quelconque pour obtenir en retour l’âge de la personne correspondant. Le résultat de la requête devra être une ligne
# de texte bien formatée, telle par exemple : « Nom : Jean Dhoute - âge : 15 ans ».
#
# o Créer ensuite un programme qui permet de remplir le dictionnaire avec 5 personnes et d’afficher les informations
# d’une personne en particulier


#Définition de la fonction de consultation
# def consultation(dictionnaire):
#
#     nom = input("Entrez le nom (ou <enter> pour terminer) : ")
#     if nom == "":
#         print("Attention il faut saisir une valeur")
#     elif nom in dictionnaire: # le nom est-il répertorié Dans le dictionnaite
#         item = dictionnaire[nom] # consultation proprement dite
#
#         print("Nom ",nom, "- âge :",item, "ans")
#     else:
#         print("*** nom inconnu ! ***")
#
# #Définition de la fonction de remplissage
# def remplissage(dictionnaire):
#
#     nom = input("Entrez le nom (ou <enter> pour terminer) : ")
#     if nom == "":
#         print("Attention il faut saisir une valeur")
#     else:
#         age = int(input("Entrez l'âge (nombre entier !) : "))
#         dictionnaire[nom] = age
#
# #Test des fonctions
# dico ={}
# i=1
# while i<=5:
#     remplissage(dico)
#     i = i + 1
#
#
# choix = input("Choisissez : (R)emplir - (C)onsulter  : ")
# if choix.upper() == 'R':
#     remplissage(dico)
# elif choix.upper() == 'C':
#     consultation(dico)