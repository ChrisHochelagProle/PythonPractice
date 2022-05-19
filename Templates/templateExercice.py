# Informations generales pour mise en page
import os.path

cours = "Concepts de programmation"
nom = "Desrosiers Mondor"
prenom = "Christopher"

# Variables pour le pseudo code
nom_de_algorithme = os.path.basename(__file__)

# Contantes
message_ouverture = 30 * "*" + f" Voici le resultat du programme: {nom_de_algorithme} " + 30 * "*"
message_fermeture = 30 * "*" + f" Codé par {prenom} {nom} dans le cadre du cours {cours} " + 30 * "*"

# Entrees

# Sorties

# Mise en page

print(message_ouverture)

# Mettre le code sous ce commentaire

# Message footer
print(message_fermeture)
