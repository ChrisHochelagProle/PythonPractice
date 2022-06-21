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
# Voir le contenu et comprendre key/value pairs
print(dict_langue)
print("Nous pouvons vous servir dans les langues suivantes: ")
for langue in dict_langue.keys():
    print(langue, end=" ")
# Ci-dessous la fonction max nous offre la possibilite de lui donner un objet iterable comme une liste ou un dictionnaire
# et de recevoir la plus grande valeur. Rappelez vous que dans dict on a des key\value pair et donc max cherche
# seulement dans les values. Ici c'est parfait car les valeurs ont ete augmentees a chaque fois qu'une personne
# parlait la langue et on cherche la langue la plus parler.
print("\nLa langue la plus parler par les employes: ", max(dict_langue, key=dict_langue.get))
