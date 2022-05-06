nb_lapin = 100
nb_semaine = 0

growth_index = 1.10

while nb_lapin < 200:
    nb_lapin = nb_lapin * growth_index
    nb_semaine += 1
    #print(nb_lapin) # pour afficher chaque ittération.

print("La votre cible de 200 lapins sera atteinte en: " + str(nb_semaine) + " semaines.")