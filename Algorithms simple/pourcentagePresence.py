'''''
Nom de l'algorithme : pourcentagePresenceEtudiante
Constantes : 
Entrées : nb_etudiants_inscrits (entier), nb_etudiants_presents (entier)
Sortie : pourcentage_presence (réel)

afficher "Entrez le nombre de presence et d'inscriptions: "
lire nb_etudiants_presents, nb_etudiants_inscrits
pourcentage_presence <-- nb_etudiants_presents * 100 / nb_etudiants_inscrits
afficher "Le pourcentage de présence est de : ", pourcentage_presence, "%"


'''''

nb_etudiants_presents = int(input("Entrez le nombre de presence étudiante : "))
nb_etudiants_inscrits = int(input("Entrez le nombre d'inscription étudiante : "))
pourcentage_presence = nb_etudiants_presents * 100 / nb_etudiants_inscrits
print("Le pourcentage de présences est de : " + str(pourcentage_presence) + " %")