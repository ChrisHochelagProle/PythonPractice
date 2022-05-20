nb = int(input("Nombre: "))

if nb < 0:
    print("Nombre inséré est négatif :" + str(nb))
elif nb > 0:
    print("Nombre inséré est positif :" + str(nb))
else:
    print("Nombre inséré est égal a 0 : " + str(nb))

nb = int(input("Nombre (test de division): "))

if nb % 5 == 0 & nb % 3 == 0:
    print("Votre nombre: " + str(nb) + " C'est divisible par 3 et 5.")
elif nb % 5 == 0:
    print("Votre nombre: " + str(nb) + " C'est divisible par 5.")
elif nb % 3 == 0:
    print("Votre nombre: " + str(nb) + " C'est divisible par 3.")
else:
    print("Nombre inséré est égal a 0")