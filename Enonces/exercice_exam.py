# Une médiathèque contient différents types de médias. Mais quel que soit le média,
# celui-ci possède un titre. Quand un média est créé, son titre est donné à la création
# et par la suite, il ne change plus.
#
# 1. Définissez la classe Media avec son constructeur public, un champ titre privé et son accesseur.
class Media:
    no_enregistrement = 0
    def __init__(self, titre: str):
        self.__titre = titre
        self.__noEnregistrement = Media.no_enregistrement
        Media.no_enregistrement += 1

    def getTitre(self):
        return self.__titre

    def getNumero(self):
        return Media.no_enregistrement

    def plusPetit(self):
        return self.__noEnregistrement < Media.no_enregistrement

    def __str__(self):
        infos = f'No enregistrement: {self.__noEnregistrement}\n' \
                f'Titre du media: {self.__titre}'
        return infos


class Livre(Media):
    def __init__(self, titre: str, auteur: str, nbPages: int):
        super().__init__(titre)
        self.auteur = auteur
        self.nbPages = nbPages

    def __str__(self):
        infos = f'{super().__str__()}\n' \
                f'Auteur: {self.auteur}\n' \
                f'Nombre de pages: {self.nbPages}'
        return infos

class Dictionnaire(Media):
    def __init__(self, titre: str, auteur: str, nbPages: int, langue: str, nbtomes: int):
        super().__init__(titre)
        self.auteur = auteur
        self.nbPages = nbPages
        self.langue = langue
        self.nbTomes = nbtomes

    def __str__(self):
        infos = f'{super().__str__()}\n' \
                f'Auteur: {self.auteur}\n' \
                f'Nombre de pages: {self.nbPages}\n' \
                f'Langue: {self.langue}\n' \
                f'Nombre de tomes: {self.nbTomes}'
        return infos

# test
hp = Livre("Harry Potter", "J.K. Rowling", 240)
ltdf = Livre("Le trone de fer", "R.R. Martin", 789)
print(hp)
print(ltdf)
print(Media.no_enregistrement)