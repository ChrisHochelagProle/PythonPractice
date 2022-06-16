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
