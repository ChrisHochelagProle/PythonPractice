from math import sqrt

liste_de_nombre = [10, 3, 4, -6, -50]
liste_de_chaines = ["Annee", "Gras", "Cheval", "Xavier", "xylophone", "avion"]
liste_nombre_0_a_25 = [0, 2, 4]

# Les lambdas pour effectuer certaines modifications avec map()
min_or_plus_100 = lambda nombre : nombre - 100 if nombre >= 0 else nombre + 100
taille_des_mots = lambda mot : len(mot)
racines_carree = lambda nombre : sqrt(nombre) if nombre >= 0 else "Cant square root of negative"
# ici je vais utiliser chr. chr(97) = 'a' donc si on ajoute 97 a nos nombre entre 0 et 25 on aura les entiers
# qui peuvent etre transformes en lettre par cette fonction de pyhton
lettre_au_lieu_de_chiffre = lambda chiffre : chr(chiffre + 97)

# Donc on peut voir que les deux facons donne le meme resultat si on veut ajouter ou enlever 100 selon notre condition
# En utilisant une fonction
def minus_or_plus_100(nombre):
    if nombre >= 0:
        return nombre - 100
    else:
        return nombre + 100


# En utilisant lambda avec une condition. On peut seulement utiliser lambda si on a une seule condition
min_or_plus_100 = lambda nombre : nombre - 100 if nombre >= 0 else nombre + 100
facon_sans_lambda_plus_ou_moins_100 = list(map(minus_or_plus_100, liste_de_nombre))
assert facon_sans_lambda_plus_ou_moins_100 == [-90, -97, -96, 94, 50]  # True


facon_avec_lambda_plus_ou_moins_100 = list(map(min_or_plus_100, liste_de_nombre))
assert facon_avec_lambda_plus_ou_moins_100 == [-90, -97, -96, 94, 50]  # True

# Retourner une liste avec la taille de chaque mot
liste_de_tailles_des_mots = list(map(taille_des_mots, liste_de_chaines))
assert liste_de_tailles_des_mots == [5, 4, 6, 6, 9, 5]  # True

# Retourner une liste de racines carree des nombres
liste_racines = list(map(racines_carree, liste_de_nombre))
assert liste_racines == [3.1622776601683795, 1.7320508075688772, 2.0, 'Cant square root of negative',
                         'Cant square root of negative']  # True

# Retourner lettre de lalphabet correspondante dune liste acceptant des entier de 0 a 25
# 0 = a et ainsi de suite
liste_lettre_au_lieu_de_chiffre = list(map(lettre_au_lieu_de_chiffre, liste_nombre_0_a_25))
assert liste_lettre_au_lieu_de_chiffre == ['a', 'c', 'e']  # True