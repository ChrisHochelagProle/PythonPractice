from ClassMethod import *
from ClassAttribut import *

def returnAlpha(string: str):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
    return result

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
            # traitement si on est rendu au nom de la classe
            if compteur_separateurs_vus == 1:
                nom_classe = returnAlpha(line)
                dict_class_infos["nom"] = nom_classe
            # traitement si on est rendu aux attributs de la classe
            elif compteur_separateurs_vus == 2:
                # exemple :  - nom: str
                sans_les_espaces = lambda string: returnAlpha(string)
                list_nomEtsec_type = map(sans_les_espaces, line.split(":"))
