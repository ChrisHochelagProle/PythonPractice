class Attribut:
    def __init__(self, security, name, typeOf):
        self.private = security
        self.nom = name
        self.type = typeOf

    def isPrivate(self):
        return self.private

    def afficher(self):
        return (self.nom, self.private, self.type)