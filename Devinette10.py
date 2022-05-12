"""

Entrées: nombreDeviné (entier)

"""
import random

nombre_a_deviner = random.randint(1, 10)
nombre_deviner = 0
guess = False

"""
while not guess:
    if nombre_deviner == 0:
        nombre_deviner = int(input("Deviner quel nombre j'ai choisi entre 1 et 10: "))
    elif nombre_deviner == nombre_a_deviner:
        print("Bravo!", "\n Le nombre etait bien: ", nombre_a_deviner)
        guess = True
    elif nombre_deviner > 10 or nombre_deviner < 1:
        nombre_deviner = int(input("Truc: le chiffre est entre 1 et 10. Reessayer: "))
    else:
        nombre_deviner = int(input("Essayer de nouveau : "))
"""

for compteur_essais in range(1, 7):
    if compteur_essais == 6:
        print("C'est assez! Vous avez essayer trop de fois.")
        break
    else:
        if nombre_deviner == 0:
            nombre_deviner = int(input("Deviner quel nombre j'ai choisi entre 1 et 10: "))
        elif nombre_deviner == nombre_a_deviner:
            print("Bravo!", "\n Le nombre etait bien: ", nombre_a_deviner)
            break
        elif nombre_deviner > 10 or nombre_deviner < 1:
            nombre_deviner = int(input("Truc: le chiffre est entre 1 et 10. Reessayer: "))
        else:
            nombre_deviner = int(input("Essayer de nouveau : "))
