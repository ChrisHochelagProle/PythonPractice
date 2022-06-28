class Perroquet:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        self.altitude = 0

    def repeter(self, phrase):
        print(self.nom + " dit: " + phrase * 3)

    def set_nom(self, new_name):
        self.nom = new_name

    def envoleToi(self, altitude):
        self.altitude = altitude

perroquet1=Perroquet("Terreur", 3)
perroquet1.repeter("Bonjour les pirates! ")

perroquet2=Perroquet("Soleil", 2)
perroquet2.repeter("Va te coucher! ")
perroquet2.set_nom("toto")
perroquet2.repeter("Va te coucher! ")