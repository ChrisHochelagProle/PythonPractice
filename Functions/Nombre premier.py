# divisable par 1 et lui-meme
# Dautres etudiant.e.s ont utiliser le fait quil faut quil y ait un maximum de 2 diviseur
# implementer avec un compteur de diviseur
# break quand plus grand que 2 pour optimiser.
# crissement plus facile que mon code.
def nombre_premier(nombre_donner):
    is_premier = True
    # cette condition fonctionne pour tous les nombres --
    # if nombre_donner % 1 == 0 and nombre_donner % nombre_donner == 0:
    for i in range(2, nombre_donner):
        if nombre_donner % i == 0:
            is_premier = False
    return is_premier


while True:
    nombre = int(input("Entrez un nombre pour verifier sil est premier: "))
    print("Le nombre est premier?: ", nombre_premier(nombre))
    encore = input("Encore? ")
    if encore == "non":
        break
