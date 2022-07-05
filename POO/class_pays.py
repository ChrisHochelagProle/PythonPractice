class Pays:
    def __init__(self, nb_habitants=0, superficie=0):
        self.__nb_habitants = nb_habitants
        self.__superficie = superficie

    def set_nb_habitants(self, nbHabitants):
        self.__nb_habitants = nbHabitants

    def get_nb_habitants(self):
        return self.__nb_habitants

    def set_superficie(self, superficie):
        self.__superficie = superficie

    def get_superficie(self):
        return self.__superficie

    def augmenteSuperficie(self, pays):
        pays.set_superficie(pays.get_superficie()+1)

    # En utilisant ALT+insert et override methods on peut inserer des methodes de la classe parent comme __str__
    def __str__(self) -> str:
        return super().__str__()


class Permutation:
    def permutervers1(self, p1, p2):
        temp = Pays(0, 0)
        p1 = p2
        p2 = temp

    def permuterver2(self, p1, p2):
        tmp = Pays(0, 0)
        tmp.set_nb_habitants(p1.get_nb_habitants())
        tmp.set_superficie(p1.get_superficie())
        p1.set_nb_habitants(p2.get_nb_habitants())
        p1.set_superficie(p2.get_superficie())
        p2.set_nb_habitants(tmp.get_nb_habitants())
        p2.set_superficie(tmp.get_superficie())


    def copier(p):
        r = Pays(0, 0)
        r.set_nb_habitants(p.get_nb_habitant)
        r.set_superficie(p.get_superficie())
        return r

# 2
pays_1 = Pays()
pays_1.augmenteSuperficie(pays_1)
print(pays_1.get_superficie())

# 3 Parce que nouveau ne renvoie rien et on n<affecte rien a p1 donc reste original
def nouveau(p) :
	P=Pays(0,0)

p1=Pays(10000,5000)
nouveau(p1)
print(p1.get_superficie())

# 4 Parce que permutervers1 renvoie rien il affecte les valeurs a des valeurs locales a la fonciton de la classe
p1=Pays(10000,2000)
p2=Pays(30000,5000)
permut=Permutation()
permut.permutervers1(p1,p2)
print(p1)
print(p2)

# 5
p1=Pays(10000,2000)
p2=Pays(30000,5000)
permut=Permutation()
permut.permuterver2(p1, p2)
print(p1)
print(p2)
