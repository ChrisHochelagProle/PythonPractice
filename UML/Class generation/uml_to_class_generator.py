from ClassMain import *
from ClassMethod import *
from ClassAttribut import *
from ClassGenUtils import *
from uml_generator import *

class ClassGenerator:
    def __init__(self, uml: str):
        self.uml_diagram = uml

    def generateClass(self):
        # ici je cree un objet aClass ayant un nom, une liste de methodes et une liste d'attributs
        # Les attributs on un nom, une securite et un type
        # Les methodes on un nom, une securite et PEUVENT avoir un type de retour
        my_class = aClass(umlUnformat(self.uml_diagram))
        attributs_text = ""
        for atribu in my_class.getAttibuts():
            if atribu.isPrivate():
                attributs_text += f"    self.__{atribu.nom} = ''\n    "
            else:
                attributs_text += f"    self.{atribu.nom} = ''\n    "
        methode_text = ""
        for method in my_class.methods:
            if method.retour == "":
                methode_text += f"def {method.nom}(self):\n    " \
                                f"    pass\n\n    "
            else:
                methode_text += f"def {method.nom}(self):\n    " \
                                f"    {method.retour}_result = ''\n    " \
                                f"    return string\n\n    "
        class_body = f"class {my_class.name}:\n" \
                     f"    def __init__(self):\n" \
                     f"    {attributs_text}\n" \
                     f"\n" \
                     f"    {methode_text}"

        return class_body

# exemple
# | ********************* |
# | Senseur               |
# | ********************* |
# | + humidite: float     |
# | + pression: float     |
# | + temperature: int    |
# | + connecte: bool      |
# | ********************* |
# | + demarrer()          |
# | + lireValeurs(): dict |
# | ********************* |
uml = generateUML()

generator = ClassGenerator(uml)
print(generator.generateClass())
