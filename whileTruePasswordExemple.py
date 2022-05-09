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

# Solution 1
"""
while True:
    mdp_Lu = input("Entrer un mot de passe: ")
    if mdp_Lu == "wow":
        print("Bienvenue.")
        break
    print("Le mot de passe est invalide.")
"""

# Solution 2
"""
mdp_Lu = input("Entrez un mot de passe: ")
while mdp_Lu != "wow":
    print("Mot de passe invalide")
    mdp_Lu = input("Entrez un mot de passe: ")
    
print("Bienvenu")
"""

# Dans le cas ou l'utilisateur dépasse trois essais
for iterateur in range(1, 4):
    mdp_Lu = input("Entrer un mot de passe: ")
    if mdp_Lu == "wow":
        print("Bienvenue.")
        break
    elif iterateur == 3:
        print("Veuillez contacter votre superviseur")
