name = input("Entrez votre nom: ")
age = int(input("Entrez votre âge: "))

if age < 20 or age > 60:
    print("Vous n'avez pas l'age requis")
elif (age < 30) & (age >= 20):
    print("Vous êtes dans la vingtaine.")
elif (age < 40) & (age >= 30):
    print("Vous êtes dans la trentaine.")
elif (age < 50) & (age >= 40):
    print("Vous êtes dans la quarantaine.")
elif (age < 60) & (age >= 50):
    print("Vous êtes dans la cinquantaine.")

print("Bonne journée à vous " + name)
