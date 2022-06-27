# Pour creer et utiliser les matrices, les listes doivent avoir un nombre delements egaux

# Initialiser des matrices
mat = [[],[],[]]

mat = []
for i in range(3):
    mat.append([])

# Avec la comprehension des listes
mat = [[] for i in range(3)]

# Pour representer par exemple cette matrice
# 1  2  3  4
# 11 12 13 14
# 21 22 23 24

l1 = [1, 2, 3, 4]
l2 = [11, 12, 13, 14]
l3 = [21, 22, 23, 24]

mat1 = [l1, l2, l3]
# mat[ligne][colonne] commence a 0
assert mat1[0][0] == 1  # True

# on peut changer des valeurs
mat1[0][0] = 100
assert mat1[0][0] == 100  # True

# La longueur dune matrice est le nombre de listes
assert len(mat1) == 3  # True

# Somme de la matrice


def somme_matrice(matrice):
    somme = 0
    for uneListe in matrice:
        for unElement in uneListe:
            somme += unElement
    return somme


### Fonctions sur les matrices
### Filter et Map
# Filter
# Filtrer les elements selon un critere donne tant quon peut lexprimer par une fonction en python
def critere_pair(nombre):
    if nombre % 2 == 0:
        return True


liste1 = [78,23,44,35,12,87,56,90,28]
liste2 = list(filter(critere_pair, liste1))
assert liste2 == [78,44,12,56,90,28]  # True


def critere_inf_a_5(mot):
    if len(mot) < 6:
        return True

liste1 = ["pluie", "tempete", "ouragan", "neige", "verglas", "vent"]
liste2 = list(filter(critere_inf_a_5, liste1))
assert liste2 == ['pluie', 'neige', 'vent']  # True

# Map
# fonction qui permet dappliquer un traitement simple sur tous les elements dune liste et retourne une nouvelle liste
# avec les resultats
# Exemple mettre tous les premiers caracteres en majuscules.
def capitaliser(chaine):
    initiale = chaine[0]
    reste = chaine[1:]
    return initiale.upper() + reste.lower()


liste1 = ["eVOR", "cHRIS", "eXAmple"]
liste2 = list(map(capitaliser, liste1))
assert liste2 == ["Evor", "Chris", "Example"]  # True


### Fonctions lambda
# Au lieu de faire ce type de fonction et de l'appeler ensuite
def carre(x):
    return x**2


# On peut utiliser une fonciton lambda en suivant cette syntaxe
# son nom = lambda input : output
carre1 = lambda x : x**2
assert carre1(2) == 4  # True

# Exemple
f_longueur = lambda chaine : len(chaine)
liste1 = ["mot", "autre"]
liste2 = list(map(f_longueur, liste1))
assert liste2 == [3, 5]  # True

# Sorted
# Fonction de tri pouvant utiliser lambda si le tri nest pas alphanumerique ou numerique
f_sous_chaine = lambda chaine : chaine[4:]
# Ici on veut mettre en ordre selon la fin des chaines
liste1 = ["420-2C3", "345-1F3"]
# sorted prend dabord la liste a trier, ensuite une cle qui est une fonction, ici une fonction lambda et retourne
# une liste trier selon la fonction donnee
liste2 = list(sorted(liste1, key=f_sous_chaine))
assert liste2 == ['345-1F3', '420-2C3']  # True

# Un autre exemple en voulant trier pa rla longueur des mots
f_longueur_mots = lambda chaine : len(chaine)
liste1 = ["dos", "automobile", "chat", "vélo", "brachiosaure"]
liste2 = list(sorted(liste1, key=f_longueur_mots))
assert liste2 == ['dos', 'chat', 'vélo', 'automobile', 'brachiosaure']  # True
