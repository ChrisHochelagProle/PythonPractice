def nb_de_minuscules(chaine):
    result = 0
    for char in chaine:
        if char.islower():
            result += 1
        else:
            pass
    return result


chaine = input("Entrez un chaine: ")
print("Il y a ", nb_de_minuscules(chaine), "minuscule dans '", chaine,  "'")
