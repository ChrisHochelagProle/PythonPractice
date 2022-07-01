from Matrice import *

m = Matrice(3)
m.afficher()

# Tester la méthode setVal()
compteur = 1
i = 0
while i < 3:
    j = 0
    while j < 3:
        m.setVal(i,j,compteur)
        compteur +=1
        j+=1
    i+=1

m.afficher()

# Tester les méthodes de transformation
m.transposer()
m.afficher()

m.normaliser()
m.afficher()

m.polariser()
m.afficher()

# Tester l'addition de deux matrices
m2 = Matrice(3)
i = 0
while i < 3:
    j = 0
    while j < 3:
        m2.setVal(i,j,10)
        j+=1
    i+=1

m.additionner(m2)
m.afficher()

# Tester la multiplication
m.multiplier(2)
m.afficher()

# Tester les min et max
print(m.min())
print(m.max())

# Tester l'affichage des valeurs individuelles
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(m.getVal(i,j))
        j+=1
    i+=1

print("Terminé.")
