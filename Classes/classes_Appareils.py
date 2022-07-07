class Appareil:
    def __init__(self, fabricant, modele, noSerie, cpu, stockage):
        self.fabricant = fabricant
        self.modele = modele
        self.noSerie = noSerie
        self.cpu = cpu
        self.stockage = stockage

    def afficher(self):
        s = "Fabricant: " + self.fabricant + "\n" + \
            "Modèle: " + self.modele + "\n" + \
            "Numéro de série: " + self.noSerie + "\n" + \
            "CPU: " + self.cpu + "\n" + \
            "Stockage: " + self.stockage
        return s

class OrdinateurPortable(Appareil):
    def __init__(self, fabricant, modele, noSerie, cpu, stockage, dimEcran, ram):
        Appareil.__init__(self, fabricant, modele, noSerie, cpu, stockage)
        self.__dimEcran = dimEcran
        self.__ram = ram

    def ajouterRam(self, ram):
        self.__ram += ram

    def afficher(self):
        s = "Fabricant: " + self.fabricant + "\n" + \
            "Modèle: " + self.modele + "\n" + \
            "Ecran: " + self.__dimEcran + "\n" + \
            "Numéro de série: " + self.noSerie + "\n" + \
            "RAM: " + self.__ram + "\n" + \
            "CPU: " + self.cpu + "\n" + \
            "Stockage: " + self.stockage
        return s

class Telephone(Appareil):
    def __init__(self, fabricant, modele, noSerie, cpu, stockage, dimEcran, imei):
        Appareil.__init__(self, fabricant, modele, noSerie, cpu, stockage)
        self.dimEcran = dimEcran
        self.imei = imei


    def afficher(self):
        s = "Fabricant: " + self.fabricant + "\n" + \
            "Modèle: " + self.modele + "\n" + \
            "Ecran: " + self.dimEcran + "\n" + \
            "Numéro de série: " + self.noSerie + "\n" + \
            "IMEI: " + self.imei + "\n" + \
            "CPU: " + self.cpu + "\n" + \
            "Stockage: " + self.stockage
        return s

class Serveur(Appareil):
    def __init__(self, fabricant, modele, noSerie, cpu, stockage, ram):
        Appareil.__init__(self, fabricant, modele, noSerie, cpu, stockage)
        self.ram = ram

    def ajouterRam(self, ram):
        self.ram += ram

    def ajouterStockage(self, stockage):
        self.stockage += stockage

    def afficher(self):
        s = "Fabricant: " + self.fabricant + "\n" + \
            "Modèle: " + self.modele + "\n" + \
            "Numéro de série: " + self.noSerie + "\n" + \
            "RAM: " + self.ram + "\n" + \
            "CPU: " + self.cpu + "\n" + \
            "Stockage: " + self.stockage
        return s