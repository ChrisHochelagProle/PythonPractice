# Exercices serie 10

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
liste_de_tailles_des_mots_2 = list(map(len, liste_de_chaines))
assert liste_de_tailles_des_mots == [5, 4, 6, 6, 9, 5]  # True
assert liste_de_tailles_des_mots_2 == [5, 4, 6, 6, 9, 5]  # True

# Retourner une liste de racines carree des nombres
liste_racines = list(map(racines_carree, liste_de_nombre))
assert liste_racines == [3.1622776601683795, 1.7320508075688772, 2.0, 'Cant square root of negative',
                         'Cant square root of negative']  # True

# Retourner lettre de lalphabet correspondante dune liste acceptant des entier de 0 a 25
# 0 = a et ainsi de suite
liste_lettre_au_lieu_de_chiffre = list(map(lettre_au_lieu_de_chiffre, liste_nombre_0_a_25))
assert liste_lettre_au_lieu_de_chiffre == ['a', 'c', 'e']  # True

# Code par Maddie
import math

add_or_substract_100 = lambda x : x-100 if x < 0 else x+100
word_len = lambda s : len(s)
# Malade son idee pour renvoyer une lettre selon un nombre dans la longueur de l'alphabet
alphabet = lambda n : "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")[n]

num_list = [-10, 20, -2, -65, 12, 26]
num_list_2 = [2, 10, 55, 24, 66, 70, 32, 23, 51]
word_list = ["maison", "bague", "livre", "un", "terminaison"]
int_char_list = [0, 21, 13, 5, 8, 12, 25]

print(list(map(add_or_substract_100, num_list)))
print(list(map(math.sqrt, num_list_2)))
print(list(map(word_len, word_list)))
print(list(map(alphabet, int_char_list)))

#output:
# [-110, 120, -102, -165, 112, 126]
# [1.4142135623730951, 3.1622776601683795, 7.416198487095663, 4.898979485566356, 8.12403840463596,
# 8.366600265340756, 5.656854249492381, 4.795831523312719, 7.14142842854285]
# [6, 5, 5, 2, 11]
# ['a', 'v', 'n', 'f', 'i', 'm', 'z']