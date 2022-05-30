from array import *
array_num = array('i', [1, 3, 5, 7, 9])  # i veut dire entier
print("Tableau d'origine:", str(array_num))
array_num.reverse()
print("L'inverse:", array_num)
array_2 = array('i', [-1, 12])
array_num.extend(array_2)
array_num.insert(2, 4)
array_num.pop(3)
array_num.append(54)
array_num.remove(3)
# retourner l'index d'une valeur. La posiiton de la premiere fois quon le trouve
array_num.index(54)
