# importing sys
import sys

# adding Folder_2 to the system path
sys.path.insert(0, 'C:\\Users\\e2295874\\PycharmProjects\\PythonPractice\\modules')

from utilities import is_prime

def dix_nombre():
    x = 0
    liste_nombres = []
    while x < 10:
        input_user = int(input("Entrez un nombre: "))
        liste_nombres.append(input_user)
        x += 1
    return liste_nombres


def dict_premiers_non_premiers(liste_nombre):
    dict_premiers = {}
    for nombre in liste_nombre:
        if is_prime(nombre):
            dict_premiers[nombre] = "Premier"
        else:
            dict_premiers[nombre] = "Non premier"
    return dict_premiers


print(dict_premiers_non_premiers(dix_nombre()))
