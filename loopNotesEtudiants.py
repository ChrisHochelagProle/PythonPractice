"""

Test d'implémentation pour une programme répétitif pour trouver la moyenne des notes.

"""

nb_eleves_classe = int(input("Entrez le nombre d'élèves dans votre classe: "))
somme_note = 0

for iterateur in range(nb_eleves_classe):
    texte = "Entrez la note de l'étudiant " + "(" + str(iterateur + 1) + ") : "
    note_etudiant = float(input(texte))
    somme_note += note_etudiant
moyenne = somme_note/nb_eleves_classe
print("La moyenne est :", moyenne)
