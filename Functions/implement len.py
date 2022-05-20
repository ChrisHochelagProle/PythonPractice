def longueur(une_string):
    lenght = 0
    for lettre in une_string:
        lenght += 1
    return lenght


mot = input("Entrez un mot: ")

print("Le mot contient", longueur(mot), "caracteres.")
