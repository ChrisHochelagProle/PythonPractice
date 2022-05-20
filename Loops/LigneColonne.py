"""
for ligne in range(1, 6):  # On affichera 5 lignes
    barre = str(ligne)
    for colonne in range(1, ligne+1):  #Sur chaque ligne on ajoutera un nombre de # égal au nombre de lignes + 1
        barre += "#"
    print(barre)
"""

# ici je voulais juste tester voir comment coder lignes et colonne et les représenter par des chiffres.
lignes = 5
colonnes = 6

for ligne_iterateur in range(1, lignes+1):
    ligne = ""
    for colonne_iterateur in range(1, colonnes+1):
        ligne += str(colonne_iterateur)
    print(ligne)
