def longueur(str):
    longueur_resultat = 0
    for char in str:
        longueur_resultat += 1
    return longueur_resultat


def separateur(str, separateur):
    list_separe = []
    swap_word = ""
    longueur_str = longueur(str)
    for index in range(longueur_str):
        if str[index] == separateur:
            list_separe.append(swap_word)
            swap_word = ""
        else:
            swap_word += str[index]
        if index == longueur_str - 1:
            list_separe.append(swap_word)

    return list_separe


def remplacer(str, original, remplacement):
    len_original = longueur(original)
    str_copy = str
    new_str = ""
    while str_copy != "":
        len_str = longueur(str_copy)
        if original not in str_copy:
            new_str += str_copy
            str_copy = ""
            break
        for index in range(len_str):
            if str_copy[index:index+len_original] == original:
                new_str += str_copy[0:index] + remplacement
                str_copy = str_copy[index+len_original:longueur(str_copy)]
                break
    return new_str

# Execution de la fonction longueur()
str_welcome = "Welcome"
print(longueur(str_welcome))

# Execution de la fonction separateur()
str_separateur = "Welcome:tout:le:monde"
print(separateur(str_separateur, ":"))

# Execution de la fonction remplacer.
str_test = "juliette et sa soeur juliette sont soeur depuis que Bond a rencontrer tuche."
print(remplacer(str_test, "soeur", "amies"))
