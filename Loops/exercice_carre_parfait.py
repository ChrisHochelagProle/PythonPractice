def carres_parfaits(nombre):
    carres = []
    for un_nombre in range(1, nombre):
        if un_nombre**2 < nombre:
            carres.append(un_nombre**2)
    return carres


print(carres_parfaits(100))