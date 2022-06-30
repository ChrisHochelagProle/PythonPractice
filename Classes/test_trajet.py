from class_Trajet import Trajet

trajet_mtl_qc = Trajet("Montreal", "Quebec", 2)

print(trajet_mtl_qc)
print(trajet_mtl_qc.info())

trajet_mtl_qc.avance(150)
print(trajet_mtl_qc)
print(trajet_mtl_qc.info())

trajet_mtl_qc.embarque(2)
print(trajet_mtl_qc)
print(trajet_mtl_qc.info())

trajet_mtl_qc.avance(150)
trajet_mtl_qc.debarque(4)
print(trajet_mtl_qc)
print(trajet_mtl_qc.info())

# Output
# <class 'class_Trajet.Trajet'>
# Ville de depart: Montreal
# Ville d'arriver: Quebec
# Nombre de passagers: 2
# Kms parcourus: 0
# <class 'class_Trajet.Trajet'>
# Ville de depart: Montreal
# Ville d'arriver: Quebec
# Nombre de passagers: 2
# Kms parcourus: 150
# <class 'class_Trajet.Trajet'>
# Ville de depart: Montreal
# Ville d'arriver: Quebec
# Nombre de passagers: 4
# Kms parcourus: 150
# <class 'class_Trajet.Trajet'>
# Ville de depart: Montreal
# Ville d'arriver: Quebec
# Nombre de passagers: 0
# Kms parcourus: 300
#
# Process finished with exit code 0

