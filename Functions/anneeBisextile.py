def bissextile(annee):
    if annee % 4 == 0 and not(annee % 100 == 0) or annee % 400 == 0:
        return True
    else:
        return False


annee = int(input("Donnez une annee: "))
biss = bissextile(annee)
if biss:
    print("Annee: ", annee, "est bissextile!")
else:
    print("Annee: ", annee, "n'est pas bissextile!")
