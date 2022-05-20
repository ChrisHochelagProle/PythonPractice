prix_du_litre = float(input("Entrez le prix du litre d'essence: "))
distance_a_parcourir = float(input("Entrez la distanc à parcourir (en km): "))
consommation_vehicule = float(input("Entrez la consommation en L/100km du véhicule: "))

prix_voyage = round((consommation_vehicule * distance_a_parcourir / 100 * prix_du_litre), 2)

print("Votre déplacement vous coutera environ: " + str(prix_voyage) + "$. Bonne route.")