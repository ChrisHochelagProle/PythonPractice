# On considère les données stockées dans les tuples suivants:
# Les tuples e1, e2 et e3 contiennent les noms d'employés d'une succursale de banque (1e élément) suivi par
# les langues maitrisées par cet employé
# En utilisant un dictionnaire:
# 1) affichez toutes langues avec lesquelles on peut servir la clientèle de la succursale
# 2)  affichez le langage maitrisé par un maximum d'employé

e1 = ("marco", "français", "anglais", "espagnol")
e2 = ("Li", "français", "anglais", "mandarin")
e3 = ("luca", "français", "italien")
employes = e1, e2, e3


def create_dict_of_speaking_language(employees):
    dict_langues = {}
    for workers in employees:
        for langue in workers[1:]:
            if langue not in dict_langues:
                dict_langues[langue] = 1
            else:
                dict_langues[langue] += 1
    return dict_langues


dict_langue = create_dict_of_speaking_language(employes)
print("Nous pouvons vous servir dans les langues suivantes: ")
for langue in dict_langue.keys():
    print(langue, end=" ")
print("\nLa langue la plus parler par les employes: ", max(dict_langue, key=dict_langue.get))
