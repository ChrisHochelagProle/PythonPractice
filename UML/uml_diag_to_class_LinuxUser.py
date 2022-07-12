# diagramme
# | ********************** |
# | UtilisateurLinux       |
# | ********************** |
# | + UID: str             |
# | + identifiant: str     |
# | + membreDe: str[]      |
# | + repertoirePerso: str |
# | ********************** |
# | + ajouterGroupe(str)   |
# | + connecter()          |
# | + deconnecter()        |
# | + getUID(): str        |
# | + supprimerGroupe(str) |
# | ********************** |

class UtilisateurLinux:
    def __init__(self, id: str, uid: str, home_dir: str, list_groups: list):
        self.identifiant = id
        self.uid = uid
        self.repertoirePerso = home_dir
        self.membreDe = list_groups

    def connecter(self):
        pass

    def deconnecter(self):
        pass

    def getUID(self):
        return self.uid

    def ajouterGroupe(self, nom_groupe: str):
        self.membreDe.append(nom_groupe)

    def supprimerGroupe(self, nom_groupe: str):
        self.membreDe.remove(nom_groupe)
