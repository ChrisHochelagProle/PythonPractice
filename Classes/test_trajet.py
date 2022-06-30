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
