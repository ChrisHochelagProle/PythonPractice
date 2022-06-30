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

list_comptes = []
for i in range(4):
    compte = Compte()
    depot = float(input("Combien voulez-vous mettre dans le compte: "))
    compte.depot(depot)
    list_comptes.append(compte)

moyenne = 0
list_soldes = []
for compte in list_comptes:
    moyenne += compte.solde
    list_soldes.append(compte.solde)
moyenne = moyenne/len(list_comptes)

greater_30k = lambda solde : solde > 30000
lesser_20k = lambda solde : solde < 20000

nombre_30k = len(list(filter(greater_30k, list_soldes)))
nombre_20k = len(list(filter(lesser_20k, list_soldes)))

print("La moyenne des soldes des comptes dans notre banque", moyenne, "$")
print("Compte de plus de 30k:", nombre_30k)
print("Compte de moins de 20k:", nombre_20k)

print(list_comptes[0])
list_comptes[0].affichage_etat_de_compte()