def plusGrandInList(liste):
    liste.sort()
    return liste[-1]


liste = [32, 5, 12, 8, 3, 75, 2, 15]
print(plusGrandInList(liste))
