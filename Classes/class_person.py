class Person:
    # avec les : suivant les parametres dinitialisation on offre un reference qui saffichera comme aide memoire
    # lors de la creation des instances de lobjet comme ca on pourra savoir quoi donner comme parametre sans voir
    # la classe et l'utilisation quelle fait des parametres.
    def __init__(self, nom: str, age: int, taille: float, adresse: str):
        self.name = nom
        self.age = age
        self.height = taille
        self.adress = adresse

    def info(self):
        print(f'{self.name} a {self.age} ans et mesure {self.height}m. Cette personne vit a {self.adress}.')

    def vieillir(self):
        self.age += 1


christo = Person("Christopher Desrosiers Mondor", 26, 1.92, "Hochelaga")
christo.info()
christo.vieillir()
christo.info()