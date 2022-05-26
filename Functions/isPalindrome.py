def isPalinfrome(mot):
    mot_lower = mot.lower()
    if mot_lower == mot_lower[::-1]: # [::-1] utilise un step de 1 en partant de la fin pour retourner une nouvelle
                                     # liste de charactere a l'envers.
        return True
    else:
        return False


mot = input("Entrez un mot: ")
print("Le mot ", mot, "est-il un palindrome?", isPalinfrome(mot))
