def factorial(nombre):
    result = 1
    liste = []
    for i in range(1, nombre + 1):
        liste.append(i)
    for i in liste:
        result *= i
    return result


nombre = int(input("Entrez un nombre dont vous chercher le factoriel entre 1 et 30: "))
print(factorial(nombre))
