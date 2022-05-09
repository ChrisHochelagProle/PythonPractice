"""
Pseudo code
Nom de l'algorithme : Validation d'un mot de passe.
Entrées : mdp_lu (string)

tant que vrai faire
    afficher "Entrer un mot de passe: "
    lire mdp_Lu
    si mdp_Lu = "wow"
        afficher "Bienvenue"
        break
    fin si
    afficher "Le mot de passe est invalide"


"""

while True:
    mdp_Lu = input("Entrer un mot de passe: ")
    if mdp_Lu == "wow":
        print("Bienvenue.")
        break
    print("Le mot de passe est invalide.")
