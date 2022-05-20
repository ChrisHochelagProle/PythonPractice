"""

Exemple de programme avec une boucle imbriquée.
Calculer le revenu trimestriel de plusieurs magasins.

"""

nombre_epiceries = int(input("Combien y a-t-il d'épiceries? : "))

for iterateur_epicerie in range(nombre_epiceries):  # Parcourir les épiceries
    revenu = 0.0
    for iterateur_mois in range(3):  # Prcourir les mois (3 mois ici)
        message = "Donnez le revenu de l'épicerie (" + str(iterateur_epicerie + 1) + ") pour le mois : " + str(
            iterateur_mois + 1) + "\n"
        revenu += float(input(message))
    print("Le revenu total du magasin (", str(iterateur_epicerie + 1), ") pour le 1er trimestre de l'année:", revenu,
          "$")
    print("*" * 50)
