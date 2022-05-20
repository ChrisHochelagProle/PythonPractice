nb_etudiant_classe = 5
iteration = 1
somme_notes = 0

while iteration <= nb_etudiant_classe:
    somme_notes += float(input("Entrez la note d'un élève: "))
    iteration += 1

print("Voici la moyenne de votre classe: ", round(somme_notes/nb_etudiant_classe, 2))