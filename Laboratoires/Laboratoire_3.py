class Chaine:
    def __init__(self, mot: str):
        self.__mot = mot

    def longueur(self):
        longueur_resultat = 0
        for char in self.__mot:
            longueur_resultat += 1
        return longueur_resultat

    def separateur(self, separateur: str):
        list_separe = []
        swap_word = ""
        longueur_str = self.longueur()
        for index in range(longueur_str):
            if self.__mot[index] == separateur:
                list_separe.append(swap_word)
                swap_word = ""
            else:
                swap_word += self.__mot[index]
            if index == longueur_str - 1:
                list_separe.append(swap_word)
        return list_separe

    def remplacer(self, original: str, remplacement: str):
        len_original = Chaine(original).longueur()
        str_copy = Chaine(self.__mot)
        new_str = ""
        while str_copy != "":
            len_str = str_copy.longueur()
            if original not in str_copy.__mot:
                new_str += str_copy.__mot
                str_copy.__mot = ""
                break
            for index in range(len_str):
                if str_copy.__mot[index:index + len_original] == original:
                    new_str += str_copy.__mot[0:index] + remplacement
                    str_copy.__mot = str_copy.__mot[index + len_original:str_copy.longueur()]
                    break
        return new_str

string = Chaine("Welcome in this class")
print(string.longueur())
string = Chaine("Welcome:420")
print(string.separateur(":"))
string=Chaine("juliette et sa, soeur juliette sont soeur depuis que soeur est un mot utiliser sur .sa tombe.")
print(string.remplacer("sa", "son"))