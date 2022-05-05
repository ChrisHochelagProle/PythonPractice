# ********************************* PSEUDO CODE ************************************
# taxe HST <-- 1.13
# taxeTVQ <-- 0.09975
# taxeTPS <-- 0.05
#
# afficher "Dans quelle province vivez vous? (Ontario ou Quebec)"
# lire provinceLu
# si provinceLu = Ontario
#   afficher "Quel est le prix de l'article acheté?"
#   lire prixLu
#   prixTaxer <-- prixLu * taxeHST
#   afficher "Le prix de l'article dans votre province est de:", prixTaxer, "$"
# si provinceLu = Quebec
#   afficher "Quel est le prix de l'article acheté?"
#   lire prixLu
#   prixTaxer <-- (prixLu * taxeTPS) + (prixLu * taxe TVQ) + prixLu
#   afficher "Le prix de l'article dans votre province est de: ", prixTaxer, "$"
# sinon
#   afficher "Le programme n'implémente pas de fonction pour votre province
# finsi

taxeHST = 1.13
taxeTVQ = 0.09975
taxeTPS = 0.05

province = input("Dans quelle province vivez vous? (Ontario ou Quebec) ")

if province == "Ontario":
    prixArticle = input("Quel est le prix de l'article acheté? ")
    prixTaxer = float(prixArticle) * taxeHST
    print("Le prix de l'article dans votre province est de: " + str(prixTaxer) + "$")
elif province == "Quebec":
    prixArticle = input("Quel est le prix de l'article acheté? ")
    prixTaxer = (float(prixArticle) * taxeTPS) + (float(prixArticle) * taxeTVQ) + float(prixArticle)
    print("Le prix de l'article dans votre province est de: " + str(prixTaxer) + "$")
else:
    print("Le programme n'implémente pas de fonction pour votre province.")
