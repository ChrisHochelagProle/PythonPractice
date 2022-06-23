def mots_avec_deux_voyelles(chaine):
    # list_voyelle = ("a", "e", "i", "o", "u", "y")
    voyelles = "AEIOUYaeiouy"
    # liste_mots = chaine.lower().split()
    liste_mots = chaine.split()
    liste_mots_voyelles = []
    for mot in liste_mots:
        second_vowel = False
        for lettre in mot:
            # if lettre in list_voyelle and second_vowel:
            if lettre in voyelles and second_vowel:
                liste_mots_voyelles.append(mot)
                break
            # elif lettre in list_voyelle:
            elif lettre in voyelles:
                second_vowel = True
    return liste_mots_voyelles


chaine_char = "Python est un language de programmation de haut niveau."
print(mots_avec_deux_voyelles(chaine_char))
