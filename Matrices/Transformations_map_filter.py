positif = lambda nombre : nombre > 0
pair_positif = lambda nombre : nombre > 0 and nombre % 2 == 0
pas_multiple_dix = lambda nombre : not nombre % 10 == 0
commence_par_a = lambda chaine : chaine[0] in "Aa"
contient_pas_x = lambda chaine : not "x" in chaine

liste_de_nombre = [10, 3, 4, -6, -50]
liste_de_chaines = ["Annee", "Gras", "Cheval", "Xavier", "xylophone", "avion"]

# Conserver les nombre positifs dune liste de nombre
nombres_positifs = list(filter(positif, liste_de_nombre))
assert nombres_positifs == [10, 3, 4]  # True

# Conserver les nombres pairs positifs dans une liste de nombre
nombres_pairs_positifs = list(filter(pair_positif, liste_de_nombre))
assert nombres_pairs_positifs == [10, 4]  # True

# Eliminer les multiples de 10 dans une liste de nombres
liste_sans_les_multiple_10 = list(filter(pas_multiple_dix, liste_de_nombre))
assert liste_sans_les_multiple_10 == [3, 4, -6]  # True

# Conserver les mots qui commencent par A majuscule ou ninuscule dans une liste de chaines
mots_commencent_par_a_min_ou_maj = list(filter(commence_par_a, liste_de_chaines))
assert mots_commencent_par_a_min_ou_maj == ['Annee', 'avion']  # True

# Eliminer dune liste de mot ceux qui contiennent x en minuscule
liste_sans_mots_qui_contiennent_x = list(filter(contient_pas_x, liste_de_chaines))
assert liste_sans_mots_qui_contiennent_x == ['Annee', 'Gras', 'Cheval', 'Xavier', 'avion']  # True