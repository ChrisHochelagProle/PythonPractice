from ClassMethod import *
from ClassAttribut import *

def returnAlpha(string: str):
    result = ""
    for char in string:
        if char.isalpha() or char in "+-":
            result += char
    return result

def securityToBool(security: str):
    return security == "-"

def umlUnformat(uml: str):
    # Je veux retourner un dico qui contiendra {nom: "string", attributs: [a1, a2, etc], methodes: [m1, m2, etc]}
    dict_class_infos = {}
    nom_classe = ""
    list_attributs = []
    list_methodes = []
    # Les section d'un bloc UML sont separres par * dans mon generateur uml donc je dois savoir cette information
    # pour savoir quand la ligne represente le nom, les attributs et les methodes de la classe
    separateur_sections_uml = "*"
    # J'aurai egalement besoin d'un compteur pour savoir combien de separateur j'ai rencontrer dans le traitement
    # 1 == nom de class
    # 2 == liste attributs
    # 3 == liste de methodes
    compteur_separateurs_vus = 0
    # pour faire un traitement ligne par ligne dans l'uml, je transforme en liste
    list_lines_in_uml = uml.split("\n")



    for line in list_lines_in_uml:
        if separateur_sections_uml in line:
            compteur_separateurs_vus += 1
            continue
        else:
            # traitement si on est rendu au nom dans l'uml
            if compteur_separateurs_vus == 1:
                nom_classe = returnAlpha(line)
                dict_class_infos["nom"] = nom_classe
            # traitement si on est rendu aux attributs dans l'uml
            elif compteur_separateurs_vus == 2:
                # exemple :  - nom: str
                sans_les_espaces = lambda string: returnAlpha(string)
                list_nomEtsec_type = list(map(sans_les_espaces, line.split(":")))
                # Ici on a donc une liste du format ["-nom", "str"] nous donnant le nom et la securite en list[0]
                # et type d'attribut en list[1]
                securite_attribut = list_nomEtsec_type[0][0] # - etant le premier char de "-nom"
                nom_attribut = list_nomEtsec_type[0][1:] # nom etant le reste de la chaine en list[0]
                type_attribut = list_nomEtsec_type[1] # contenant str dans notre exemple
                attribut = Attribut(securityToBool(securite_attribut),nom_attribut, type_attribut)
                list_attributs.append(attribut)
            # traitement si on est rendu aux methodes dans l'uml
            elif compteur_separateurs_vus == 3:
                # Exemple: + infos(): str
                # Exemple sans retour: + afficher()
                if ":" in line:
                    sans_les_espaces = lambda string: returnAlpha(string)
                    list_nomEtsec_typeRetour = list(map(sans_les_espaces, line.split(":")))
                    # Ici on a une liste du format ["+infos()", "str"]
                    # list[0] = securite et nom
                    # list[1] = type de retour
                    securite_methode = list_nomEtsec_typeRetour[0][0]  # - etant le premier char de "+infos()"
                    nom_methode = list_nomEtsec_typeRetour[0][1:]  # nom etant le reste de la chaine en list[0]
                    type_retour_methode = list_nomEtsec_typeRetour[1]  # contenant str dans notre exemple
                    methode = Methode(securityToBool(securite_methode), nom_methode)
                    methode.set_retour(type_retour_methode)
                    list_methodes.append(methode)
                else:
                    sans_les_espaces = lambda string: returnAlpha(string)
                    nom_et_sec = sans_les_espaces(line)
                    # ici on a une chaine "+afficher()
                    securite_methode = nom_et_sec[0]
                    nom_methode = nom_et_sec[1:]
                    # on transforme + ou - en True ou False avec securityToBool
                    methode = Methode(securityToBool(securite_methode), nom_methode)
                    list_methodes.append(methode)
            else:
                break
    # ici on rempli le dictionnaire avec le nom et les deux listes
    dict_class_infos["nom"] = nom_classe
    dict_class_infos["attributs"] = list_attributs
    dict_class_infos["methodes"] = list_methodes

    # On fini par retourner le dictionnaire pour la prochaine etape
    return dict_class_infos

