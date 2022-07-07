# Soit une classe représentant un point de l'espace 2D. Chaque instance de cette classe :
#
# · comporte deux attributs réels : un x et un y;
#
# · X et Y sont des attributs privés
#
# · comporte un constructeur paramétrique qui s'assure que l'instance en création est dans un état valide;
#
# · la classe point doit de finir la fonction DistanceDe(point )
#
# La méthode DistanceDe(point) implémente la bien connue équation
from math import sqrt


class Point:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def distanceDe(self, point):
        x0 = self.__x
        x1 = point.getX()
        y0 = self.__y
        y1 = point.getY()
        return sqrt((x0-x1)**2+(y0-y1)**2)

# Partie II
#
# Soit une classe cercle représentant un cercle. Chaque instance de cette classe comporte :
#
# · Une instance de la classe point « centre » définie dans la partie I et un rayon.
#
# · Comporte un constructeur paramétrique qui s'assure que l'instance en création est dans un état valide;
#
# · Définit une méthode intersecte(cercle) qui teste est-ce que deux cercles sont intersectés


class Cercle:
    def __init__(self, point, rayon: float):
        self.__centre = point
        self.__rayon = rayon

    def getRayon(self):
        return self.__rayon

    def intersecte(self, cercle):
        if self.__centre.distanceDe(cercle.__centre) <= self.__rayon + cercle.getRayon():
            return True
        else:
            return False

point1 = Point(5.0, 6.0)
cercle1 = Cercle(point1, 3.0)
point2 = Point(6.0, 6.0)
cercle2 = Cercle(point2, 3.0)

print(cercle1.intersecte(cercle2))