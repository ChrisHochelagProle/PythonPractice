"""

Entrées : montantInvestiLu (réel), nbAnneeInvestissement (int)
Sorties : montantCumulé (réel)
Constante : tauxInteretBanque (réel)

"""

taux_interet_banque = 0.12

while True:
    montant_cumule = float(input("Montant a investir: "))
    annees_placement = int(input("Pour combien d'annees? (entre 1 et 5) : "))
    if 1 <= annees_placement <= 5:
        for annees_iterateur in range(1, annees_placement + 1):
            montant_cumule += (montant_cumule * taux_interet_banque)
            # On pourra decommenter la prochaine ligne pour un affichage aprres chaque annee et vis versa
            # print("Montant cumule de l'année(", annees_iterateur, "):", "{:.2f}".format(montant_cumule), "$")
        print("Montant total accumulé après investissement: ", "{:.2f}".format(montant_cumule))
        continuer = input("Voulez vous refaire l'Exercice? (o/n) ")
        if continuer != "o":
            break
    else:
        print("Nous n'offrons pas de solutions de placement sur :", annees_placement, "années.")
        break
