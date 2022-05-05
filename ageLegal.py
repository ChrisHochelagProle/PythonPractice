name = input("Entrez votre nom: ")
age = int(input("Entrez votre âge: "))


if age >= 21:
    print("Hello " + name + ". Vous êtes majeur(e) à l'internationale")

elif age < 21 & age >= 18:
    print("Hello " + name + ". Vous êtes majeur(e) au Canada")

else:
    print("Hello " + name + " malheureusement pas d'alcool pour toi!")

