class Personnage:
    def __init__(self, nom, classe, race, force, intel, dex, char):
        self.__nom = nom
        self.__classe = classe
        self.__race = race
        self.__vie = 100
        self.__force = force
        self.__intelligence = intel
        self.__agilete = dex
        self.__charisme = char
    def attaquer(self, cible):
        cible.vie -= self.__force
        print('Vous avez fait ', self.__force, ' dégâts.')
    def proteger(self):
        self.__agilete += 5
        self.__force += 5
        print("Vous vous mettez en garde et gagnez 5 agileté et 5 force pour vous défendre")
    def invoquer(self, cible):
        cible.vie -= self.__intelligence
        print('Vous invoquez un sort etvous avez fait ',
              self.__intelligence, ' dégâts magique')
    def afficher(self):
        print(f'Nom: {self.__nom}\n'
              f'Classe: {self.__classe}\n'
              f'Race: {self.__race}\n'
              f'Vie: {self.__vie}\n'
              f'Force: {self.__force}\n'
              f'Intelligence: {self.__intelligence}\n'
              f'Agilete: {self.__agilete}\n'
              f'Charisme: {self.__charisme}\n')

class Arme:
    def __init__(self, nom, enchantement):
        self.__nom = ''
        self.__durabilite = 0
        self.__dommage = 0
        self.__poids = 0
        self.__portee = 0
        self.__enchantement = ''
    def nommer(self):
        self.__nom = input('Entrez le nom de votre arme: ')
    def reparer(self):
        self.__durabilite += input('Points de durabilité à réparer')
    def afficher(self):
        print(f'Nom: {self.__nom}\n'
              f'Durabilite: {self.__durabilite}\n'
              f'Dommage: {self.__dommage}\n'
              f'Poids: {self.__poids}\n'
              f'Portee: {self.__portee}\n'
              f'Enchantement: {self.__enchantement}\n')

pers1 = Personnage("Chris", "Rogue", "Human", 10, 10, 16, 12)
pers2 = Personnage("JP", "Engineer", "Dwarf", 16, 10, 16, 12)
arme1 = Arme("Sting", "Fire")
arme2 = Arme("Needle", "Ice")

pers1.afficher()
pers2.afficher()
arme2.afficher()
arme1.afficher()