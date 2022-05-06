'''
multiplicateur = 1
print("Table de multiplication de 5")
print("****************************************")
while multiplicateur <= 10:
    print(str(multiplicateur) + " * " + "5 = " + str(multiplicateur*5))
    multiplicateur += 1
print("****************************************")
'''

#Version plus flexible
multiplicateur = 1
table_de = 5
nb_multiplications = 4
entete = "Table de multiplication de " + str(table_de)
ligne_separation = "***************************"

print(entete)
print(ligne_separation)
while multiplicateur <= nb_multiplications:
    print(str(multiplicateur) + " * " + str(table_de) + " = " + str(multiplicateur * table_de))
    multiplicateur += 1
print(ligne_separation)