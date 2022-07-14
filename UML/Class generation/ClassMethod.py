class Methode:
    def __init__(self, security, name, retourOf):
        self.private = security
        self.nom = name
        self.retour = retourOf

    def afficher(self):
        return (self.nom, self.private, self.retour)