# Petit programme qui extrait les mots avec au moins 2 majuscule adjacentes d'un string
def extraction_MAJ(chaine_char):
    liste_de_mots = chaine_char.split(" ")
    liste_maj = []
    for mot in liste_de_mots:
        maj = False
        for char in mot:
            if char.isupper() and maj:
                liste_maj.append(mot)
                break
            elif char.isupper() and not maj:
                maj = True
    return liste_maj


ch_de_char = "SQLite et MongoDB sont plus simple que les bases de donnees PostgraveSQL et Oracle"
print(extraction_MAJ(ch_de_char))
