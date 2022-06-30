matrice = []
ligne = 0
while ligne < 5:
    liste = []
    colonne = 0
    while colonne < 5:
        liste.append(0)
        colonne += 1
    matrice.append(liste)
    ligne += 1

for liste in matrice:
    print(liste)
