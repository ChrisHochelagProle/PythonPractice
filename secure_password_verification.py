
# Imports
import os.path

# Fonctions

# Informations generales pour mise en page

cours = "Concepts de programmation 1"
nom = "Desrosiers Mondor"
prenom = "Christopher"

# Variables pour le pseudo code


# Contantes
nom_de_algorithme = os.path.basename(__file__)
message_ouverture = 30 * "*" + f" Voici le resultat du programme: {nom_de_algorithme} " + 30 * "*"
message_fermeture = 30 * "*" + f" Codé par {prenom} {nom} dans le cadre du cours {cours} " + 30 * "*"

# Entrees
mot_de_passe = input("Entrez un mot de passe: ")

# Sorties

# Mise en page

print(message_ouverture)

# Mettre le code sous ce commentaire


majuscule = False
minuscule = False
chiffre = False
different_debut_fin = False

for lettre in mot_de_passe:
    if lettre == lettre.upper():
        majuscule = True
    if lettre == lettre.lower() and lettre.isnumeric() == False:
        minuscule = True
    if lettre.isnumeric():
        chiffre = True

if mot_de_passe[0] != mot_de_passe[len(mot_de_passe)-1]:
    different_debut_fin = True

if different_debut_fin and majuscule and minuscule and chiffre and 5 <= len(mot_de_passe) <=10:
    print("Mot de passe securitaire.")
else:
    print("Ce mot de passe nest pas securitaire.")

# Message footer
print(message_fermeture)
