def longueur(str):
    longueur_resultat = 0
    for char in str:
        longueur_resultat += 1
    return longueur_resultat


def separateur(str, separateur):
    list_separe = []
    swap_word = ""
    longueur_str = longueur(str)
    for i in range(longueur_str):
        if str[i] == separateur:
            list_separe.append(swap_word)
            swap_word = ""
        else:
            swap_word += str[i]
        if i == longueur_str - 1:
            list_separe.append(swap_word)

    return list_separe


def remplacer(str, original, remplacement):
    swap_word = ""
    liste_mot = str.split()
    longueur_original = longueur(original)
    for mot in liste_mot:
        longueur_chaine = longueur(mot)

        for i in range(longueur_original):



    return


print(longueur("Welcome"))
print(separateur("Welcome-to-world", "-"))
print(separateur("Mon nom est Bond, James Bond.", " "))
