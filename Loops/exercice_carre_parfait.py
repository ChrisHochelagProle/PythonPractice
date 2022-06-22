def carres_parfaits(nombre):
    carres = []
    for un_nombre in range(1, nombre):
        if un_nombre*un_nombre < nombre:
            carres.append(un_nombre*un_nombre)
    return carres


print(carres_parfaits(100))
