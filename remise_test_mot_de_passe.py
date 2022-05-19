mot_de_passe = input("Entrez un mot de passe: ")
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