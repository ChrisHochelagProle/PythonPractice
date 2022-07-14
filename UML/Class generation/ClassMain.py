from ClassMethod import *
from ClassAttribut import *


class aClass:
    def __init__(self, umlUnformatted: dict):
        self.name = umlUnformatted["nom"]
        self.methods = umlUnformatted["methodes"]
        self.attributs = umlUnformatted["attributs"]

    def setName(self, nom: str):
        self.name = nom

    def addAttribut(self, a_attribut: Attribut):
        self.attributs.append(a_attribut)

    def getAttibuts(self):
        return self.attributs

    def addMethod(self, a_method: Methode):
        self.methods.append(a_method)

    def getMethods(self):
        return self.methods