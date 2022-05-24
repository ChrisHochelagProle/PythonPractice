# pi*rayon ** 2 =  aire
import math


def surfcercle(rayon):
    """Fonction qui renvoi l'aire dun cercle selon un rayon donnee"""
    return math.pi*(rayon**2)


print(surfcercle(2.5))
print(surfcercle.__doc__)

