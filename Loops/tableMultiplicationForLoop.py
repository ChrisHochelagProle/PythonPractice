"""
Pseudo code
Générateur de table de multiplication de 7
sorties : resultat (entier)

pour multiple <-- 1 à 10
    resultat <-- 7 * multiple
    afficher "7 * ", multiple, " = ", resultat
fin pour

"""

print("******Tableau de multiplication de 7 par 1 a 10*******")
print("******************************************************")
# range2 = [1,2,3,4,5,6,7,8,9,10]
# Je pourrais utiliser un array au lien de la fonction range()
for multiple in range(1, 11):
    resultat = 7*multiple
    print("7 *", multiple, "=", resultat)
print("******************************************************")
