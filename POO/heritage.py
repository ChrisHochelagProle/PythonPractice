class Personne:
    def __init__(self, nom, prenom, age):
        # les __ rende une variable privee on doit faire un getter pour lutiliser en dehors de la classe
        self.__nom = nom
        self.prenom = prenom
        self.age = age

    def ajouter_age(self):
        self.age += 1

    def __str__(self):
        return f'{self.nom} , {self.prenom}: {self.age} ans'


class Etudiant(Personne):
    def __init__(self, nom, prenom, age, matricule):
        Personne.__init__(self, nom, prenom, age)
        self.matricule = matricule

    def __str__(self):
        return f'{super.__str__()} Matricule: {self.matricule}'