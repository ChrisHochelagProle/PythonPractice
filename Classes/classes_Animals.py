class Animal:
    def __init__(self, nom: str, couleur: str, poids: float):
        self.__nom = nom
        self.__couleur = couleur
        self.__poids = poids

    def manger(self, quantite: int):
        print(quantite * "nomm")

    def dormir(self, duree: int):
        print(duree * "Zzz")

class Chien(Animal):
    # def __init__(self, nom: str, couleur: str, poids: float):
    #     super().__init__(nom, couleur, poids)

    def aboyer(self):
        print("Wouf")

class Chat(Animal):
    # def __init__(self, nom: str, couleur: str, poids: float):
    #     super().__init__(nom, couleur, poids)

    def miauler(self):
        print("Miaou")

