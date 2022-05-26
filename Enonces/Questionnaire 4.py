def sommeChiffre(nb):
    chiffres_entier = list(str(nb))
    result = 0
    for chiffres in chiffres_entier:
        result += int(chiffres)
    return result

def enversNombre(nb):
    return int(str(nb)[::-1])


# Entier doit etre > 0
entier = int(input("Entrer un entier superieur a zero: "))

print("La somme des chiffres du nombre", entier, "est", sommeChiffre(entier))
print("L'envers du nombre", entier, "est", enversNombre(entier))
