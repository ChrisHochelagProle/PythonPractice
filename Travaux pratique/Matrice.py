##################################### Mes fonctions pour aider ##############################################
def list_of_sorted_values_in_matrice(uneMatrice):
    liste_valeurs = []
    for liste in uneMatrice:
        for value in liste:
            liste_valeurs.append(value)
    liste_valeurs.sort()
    return liste_valeurs

################################# Developpement de Matrice ####################################################
class Matrice:
    def __init__(self, taille: int):
        self.taille = taille
        self.matrice = [[float(0) for x in range(taille)] for y in range(taille)]

    def transposer(self):
        matrice_transposer = []
        list_swap = []
        for y in range(self.taille):
            for x in range(self.taille):
                list_swap.append(self.matrice[x][y])
            matrice_transposer.append(list_swap)
            list_swap = []
        self.matrice = matrice_transposer

    def normaliser(self):
        valeur_minimal = list_of_sorted_values_in_matrice(self.matrice)[0]
        nouveau_nombre = lambda nombre_in_list: nombre_in_list - valeur_minimal

        nouvelle_matrice = []
        for liste in self.matrice:
            nouvelle_matrice.append(list(map(nouveau_nombre, liste)))

        valeur_maximum = list_of_sorted_values_in_matrice(nouvelle_matrice)[-1]
        nouveau_nombre = lambda nombre_in_list: nombre_in_list / valeur_maximum

        normaliser = []
        for liste in nouvelle_matrice:
            normaliser.append(list(map(nouveau_nombre, liste)))
        self.matrice = normaliser

    def polariser(self):
        for x in range(self.taille):
            for y in range(self.taille):
                if self.matrice[x][y] > 0:
                    self.matrice[x][y] = 1
                elif self.matrice[x][y] < 0:
                    self.matrice[x][y] = -1
                else:
                    self.matrice[x][y] = 0

    def additionner(self, uneMatrice):
        if self.taille != len(uneMatrice.matrice[0]):
            return f"Les deux matrices n'ont pas la meme taille."
        else:
            for x in range(self.taille):
                for y in range(self.taille):
                    self.matrice[x][y] += uneMatrice.matrice[x][y]

    def multiplier(self, nombre: float):
        nouveau_nombre = lambda nombre_in_list : nombre_in_list * nombre
        nouvelle_matrice = []
        for liste in self.matrice:
            nouvelle_matrice.append(list(map(nouveau_nombre, liste)))
        self.matrice = nouvelle_matrice

    def min(self):
        return list_of_sorted_values_in_matrice(self.matrice)[0]

    def max(self):
        return list_of_sorted_values_in_matrice(self.matrice)[-1]

    def afficher(self):
        affichage = ""
        for liste in self.matrice:
            affichage += "["
            liste_valeurs = []
            for value in liste:
                liste_valeurs.append("{:.3f}".format(value))
            adding_this = ", ".join(liste_valeurs)
            affichage += adding_this + "]\n"
        print(affichage)

    def getVal(self, x: int, y: int):
        return self.matrice[x][y]

    def setVal(self, x: int, y: int, value: float):
        self.matrice[x][y] = value

    def __str__(self):
        return f'{self.__class__}'