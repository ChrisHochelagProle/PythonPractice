from math import pi
####################  Partie 1  ######################
def afficheContenu(uneMatrice):
    affichage = ""
    for liste in uneMatrice:
        affichage += str(liste) + "\n"
    print(affichage)


def recherche(element, uneMatrice):
    for liste in uneMatrice:
        for item in liste:
            if item == element:
                return True
    return False


def occurence(element, uneMatrice):
    result = 0
    for liste in uneMatrice:
        for item in liste:
            if item == element:
                result += 1
    return result


def indices(element, uneMatrice):
    liste_indices = []
    x = 0
    y = 0
    for liste in uneMatrice:
        for item in liste:
            if item == element:
                liste_indices.append(x, y)
            y += 1
        x += 1
    return liste_indices


def minMatrice(uneMatrice):
    liste_elements = []
    for liste in uneMatrice:
        for item in liste:
            liste_elements.append(item)
    return min(liste_elements)

def maxMatrice(uneMatrice):
    liste_elements = []
    for liste in uneMatrice:
        for item in liste:
            liste_elements.append(item)
    return max(liste_elements)

def moyenneMatrice(uneMatrice):
    liste_elements = []
    somme = 0
    for liste in uneMatrice:
        for item in liste:
            liste_elements.append(item)
            somme += item
    return somme/len(liste_elements)

####################  Appel  ######################

mat = [[2, 3, 2, 3], [7, 8, 8, 9], [9, 6, 3, 3]]
afficheContenu(mat)
print(occurence(3, mat))
print(occurence(-99, mat))
print(minMatrice(mat))
print(maxMatrice(mat))
print(moyenneMatrice(mat))

####################  Partie 2  ######################

uneListe = [233.344, 21.903, 143.352, 78.109, 35.566]
entre_0_100 = lambda nombre : 0 < nombre < 101
liste_0_100 = list(filter(entre_0_100, uneListe))
print(liste_0_100)

uneListe = ['Une', 'fois', 'l', 'installation',
            'terminée,', 'vous', 'pouvez', 'vous',
            'connecter', 'à', 'OpenSSH', 'Server',
            'à', 'partir', 'd', 'un', 'appareil',
            'Windows', '10', 'ou', 'Windows',
            'Server', '2019']
plus_2_lettre = lambda mot : len(mot) > 2
liste_plus_2_lettre = list(filter(plus_2_lettre,
                                   uneListe))
print(liste_plus_2_lettre)

uneListe = [2.3, 12.8, 6.7, 31.2, 3.0]
circonference = lambda nombre : 2 * pi * nombre
liste_circonference = list(map(circonference, uneListe))
print(liste_circonference)

uneListe = ['vous', 'pouvez', 'vous', 'connecter']
inverser = lambda mot : mot[::-1]
liste_inverser = list(map(inverser, uneListe))
print(liste_inverser)

# J'ai ajouter une adresse MAC commencant par 08:00
# parce que vous demandez de les eliminer mais il
# n'y en avait aucune. Pour tester que ca fonctionne
# je devait l'ajouter.
s = "d2-7c-2F-8A-3E-19\n" \
    "bf:a0:de:8d:82:11\n" \
    "E2:10:71:A4:58:28\n" \
    "86-56-f2-5f-82-da\n" \
    "52-4a-c1-42-72-dd\n" \
    "8A:02:38:15:14:67\n" \
    "08:00-2e-45-67-87"
liste_adrs_before_cleanup = s.split("\n")
liste_adrs_clean = []
for item in liste_adrs_before_cleanup:
    item = item.lower()
    if "-" in item:
        liste = item.split("-")
        string = ":".join(liste)
        liste_adrs_clean.append(string)
    else:
        liste_adrs_clean.append(item)
commence_pas_08_00 = lambda mot : mot[0:5] != "08:00"
liste_finale = list(filter(commence_pas_08_00,
                           liste_adrs_clean))
print(liste_finale)