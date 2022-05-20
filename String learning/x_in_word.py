"""
Pseudo code
Nom de l'algorithme: Combien de caracteres dans ce mot?

Entrees: mot (string), caractere (string)
Sorties: nombre_de_car_dans_mot (int)

afficher "Entrer un mot: "
lire mot
afficher "Entrez un caractere: "
lire caractere
nombre_de_car_dans_mot <-- 0

pour lettre dans mot faire
    si lettre == caractere
        nombre_de_car_dans_mot += 1

afficher "Il y a donc ", nombre_de_car_dans_mot, " fois le caractere ", caractere, "dans le mot: ", mot
"""
mot = input("Entrez un mot: ")
caractere = input("Entrez un caractere du mot: ")
nombre_de_car_dans_mot = 0

for lettre in mot:
    if lettre == caractere:
        nombre_de_car_dans_mot += 1

print("Il y a donc ", nombre_de_car_dans_mot, " fois le caractere ", caractere, "dans le mot: ", mot)

