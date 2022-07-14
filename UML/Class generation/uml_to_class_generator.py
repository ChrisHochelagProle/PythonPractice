def returnAlpha(string: str):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    return result

class Attribut:
    def __init__(self, security, name, typeOf):
        self.private = security
        self.nom = name
        self.type = typeOf

    def afficher(self):
        return (self.nom, self.private, self.type)
class Methode:
    def __init__(self, security, name, retourOf):
        self.private = security
        self.nom = name
        self.retour = retourOf

    def afficher(self):
        return (self.nom, self.private, self.retour)

class ClassGenerator:
    def __init__(self, uml: str):
        self.uml_diagram = uml

    def generateClass(self):
        nom_de_classe = ""
        lines_in_uml = self.uml_diagram.split("\n")
        lines_without_bars = []
        for line in lines_in_uml:
            lines_without_bars.append(line.strip("|"))
        compteur_separations = 0
        attributs = []
        methodes = []
        for line in lines_without_bars:
            private = False
            nom_attribut = ""
            type_attribut = ""
            nom_methode = ""
            type_retour = ""
            if "*" in line:
                compteur_separations += 1
                continue
            if compteur_separations == 1:
                pass
                nom_de_classe = line.strip(" ")
            elif compteur_separations == 2:
                if "-" in line:
                    private = True
                elif "+" in line:
                    private = False
                list_nom_et_type = line.split(":")
                nom_pre_edit = list_nom_et_type[0]
                type_pre_edit = list_nom_et_type[1]
                nom_attribut = returnAlpha(nom_pre_edit)
                type_attribut = returnAlpha(type_pre_edit)
                attribut = Attribut(private, nom_attribut, type_attribut)
                attributs.append(attribut)
            elif compteur_separations == 3:
                if "-" in line:
                    private = True
                elif "+" in line:
                    private = False
                list_nom_et_type = line.split(":")
                nom_pre_edit = list_nom_et_type[0]
                retour_pre_edit = list_nom_et_type[1]
                nom_methode = returnAlpha(nom_pre_edit)
                type_retour = returnAlpha(type_pre_edit)
                methode = Methode(private, nom_methode, type_retour)
                methodes.append(methode)
            else:
                break
        attributs_text = ""
        for atribu in attributs:
            if atribu.private:
                attributs_text += f"    self.__{atribu.nom} = ''\n    "
            else:
                attributs_text += f"    self.{atribu.nom} = ''\n    "
        methode_text = ""
        for method in methodes:
            methode_text += f"def {method.nom}(self):\n    " \
                            f"    pass"
        class_body = f"class {nom_de_classe}:\n" \
                f"    def __init__(self):\n" \
                f"    {attributs_text}\n" \
                f"\n" \
                f"    {methode_text}"

        return class_body


uml = f'| ************** |\n' \
      f'| Ville          |\n' \
      f'| ************** |\n' \
      f'| - nom: str     |\n' \
      f'| + pays: Pays   |\n' \
      f'| - pop: int     |\n' \
      f'| ************** |\n' \
      f'| + infos(): str |\n' \
      f'| ************** |\n'

generator = ClassGenerator(uml)
print(generator.generateClass())
