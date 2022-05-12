"""

Entrées: nombreDeviné (entier)

"""
import random

nombre_a_deviner = random.randint(1, 10)
nombre_deviner = 0
guess = False

while not guess:
    if nombre_deviner == 0:
        nombre_deviner = int(input("Deviner quel nombre j'ai choisi entre 1 et 10: "))
    elif nombre_deviner == nombre_a_deviner:
        print("Bravo!", "\n Le nombre etait bien: ", nombre_a_deviner)
        break
    else:
        nombre_deviner = int(input("Essayer de nouveau : "))
