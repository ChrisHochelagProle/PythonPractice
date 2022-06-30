def infoMatrice(matrice):
    somme = 0
    nb_elements = 0
    for liste in matrice:
        for element in liste:
            somme += element
            nb_elements += 1
    information = "Nombre elements: " + str(nb_elements) + " Somme des elements: " + str(somme)
    return information


m1 = [[1, 1], [2, 2], [3, 3], [4, 4]]
print(infoMatrice(m1))