class Methode:
    def __init__(self, security, name):
        self.private = security
        self.nom = name
        self.retour = ""

    def set_retour(self, type_retour: str):
        self.retour = type_retour

    def isPrivate(self):
        return self.private

    def afficher(self):
        return (self.nom, self.private, self.retour)