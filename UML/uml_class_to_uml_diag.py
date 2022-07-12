# class Pays:
#     def __init__(self,codeISO,nom):
#         self.__iso = codeISO
#         self.__nom = nom
#
#     def infos(self):
#         return self.__nom + " (" + self.__iso + ") "
#
# class Ville:
#     def __init__(self,nom,pop,pays):
#         self.__nom = nom
#         self.__pop = pop
#         self.__pays = pays
#
#     def infos(self):
#         infosPays = self.__pays.infos()
#         return self.__nom + ", " + self.__pop + ", " + infosPays
#
# p = Pays("CA","Canada")
# v = Ville("Montréal","1780000",p)
# | ************** |
# | Pays           |
# | ************** |
# | - iso: str     |
# | - nom: str     |
# | ************** |
# | + infos(): str |
# | ************** |
# 1..1 (ville contient 1 et un seul Pays)
# |
# |
# | (ville en relation avec pays)
# |
# | ************** |
# | Ville          |
# | ************** |
# | - nom: str     |
# | - pays: Pays   |
# | - pop: int     |
# | ************** |
# | + infos(): str |
# | ************** |