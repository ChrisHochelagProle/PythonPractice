def isPair(nombre):
    return nombre % 2 == 0


list = [32, 5, 12, 8, 3, 75, 2, 15]
list_pair = []
list_impair = []

for nombre in list:
    if isPair(nombre):
        list_pair.append(nombre)
    else:
        list_impair.append(nombre)

print("Pair: ", list_pair)
print("Impair: ", list_impair)
