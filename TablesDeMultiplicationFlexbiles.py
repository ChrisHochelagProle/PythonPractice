"""
Pseudo code
Générateur de table de multiplication avec for
entrees : table_de
sorties : resultat (entier)

afficher "Pour quelle nombre voulez voir la table de multiplication de 1 a 10? : "
lire table_de
pour multiple <-- 1 à 10
    resultat <-- table_de * multiple
    afficher table de, "*", multiple, " = ", resultat
fin pour

Générateur de table de multiplication avec while
entrees : table_de
sorties : resultat (entier)

afficher "Pour quelle nombre voulez voir la table de multiplication de 1 a 10? : "
lire table_de
iterateur <-- 1
tant que iterateur <=10 faire
    resultat <-- table_de * multiple
    afficher table de, "*", multiple, " = ", resultat
    iterateur = iterateur + 1

"""

# Version avec for
print("******Tableau de multiplication de 7 par 1 a 10 (for)*******")
print("******************************************************")
table_de = int(input("Pour quelle nombre voulez voir la table de multiplication de 1 a 10? : "))
for multiple in range(1, 11):
    resultat = table_de * multiple
    print(table_de, "*", multiple, "=", resultat)
print("******************************************************")


""" Version avec while
print("******Tableau de multiplication de 7 par 1 a 10 (while)*******")
print("******************************************************")
table_de = int(input("Pour quelle nombre voulez voir la table de multiplication de 1 a 10? : "))
iterateur = 1
while iterateur <= 10:
    resultat = table_de * iterateur
    print(table_de, "*", iterateur, "=", resultat)
    iterateur += 1
print("******************************************************")
"""