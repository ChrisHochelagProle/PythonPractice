class Compte:
    def __init__(self, solde: float = 0):
        self.solde = solde

    def __str__(self):
        return f'Objet de type {self.__class__} contenant Solde: {self.solde}'

    def depot(self, montant: float):
        if montant > 0:
            self.solde += montant
        else:
            print("Montant invalide")

    def retrait(self, montant: float):
        if montant > 0:
            self.solde -= montant
        else:
            print("Montant invalide")

    def affichage_etat_de_compte(self):
        print(f'[{self.solde}$]')