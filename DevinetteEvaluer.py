"""

Entrées: nombreDeviné (entier)

Constante: nombreADeviner (entier)

Nom de l'algorithme: Jeu de devinette

nbADeviner <-- random de 1 à 10
nbDevine = 0
pour essais dans 1 à 6
    si essais = 6
        afficher "Vous avez depasser le nombres d'essais alloués"
        break
    sinon
        si nbDevine = 0
            afficher "Deviner quel nombre j'ai choisi entre 1 et 10: "
            lire nbDevine
        sinon si nbDevine = nbADeviner
            afficher "Bravo le nombre était bien: ", nbADeviner
        sinon
            afficher "Essayer de nouveau"
            lire nbDevine
        fin si

"""
import random

nombre_a_deviner = random.randint(1, 10)
nombre_deviner = 0

for compteur_essais in range(1, 7):
    if compteur_essais == 6: # on veut donner 5 essais, en arrivant la 6e fois dans la loop c'est le cas.
        print("C'est assez! Vous avez essayer trop de fois.")
        break
    else:
        if nombre_deviner == 0:
            nombre_deviner = int(input("Deviner quel nombre j'ai choisi entre 1 et 10: "))
        elif nombre_deviner == nombre_a_deviner:
            print("Bravo!", "\n Le nombre etait bien: ", nombre_a_deviner)
            break
        else:
            nombre_deviner = int(input("Essayer de nouveau : "))
