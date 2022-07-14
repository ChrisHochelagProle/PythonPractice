def plusGrandInList(liste):
    liste.sort()
    return liste[-1]

class DiagramUml:
    def __init__(self, nomClasse: str, listeAttributs: list, listeMethodes: list):
        self.nomClasse = nomClasse
        self.listeAttributs = listeAttributs
        self.listeMethodes = listeMethodes
        len_max_attribut = len(plusGrandInList(self.listeAttributs))
        len_max_methode = len(plusGrandInList(self.listeMethodes))
        self.plus_grand = lambda len1, len2: len1 if len1 >= len2 else len2
        self.len_max = self.plus_grand(len_max_attribut, len_max_methode)
        separateur = (self.len_max * "*")
        self.separateur = separateur

    def getUML(self):
        attributsStr = ""
        methodesStr = ""
        espace_ap_funct = lambda len1, len2: (len1 - len2) * " "
        for attribut in self.listeAttributs:
            espace_ap = espace_ap_funct(self.len_max, len(attribut))
            attributsStr += f'| {attribut} {espace_ap}|' + '\n'
        for methode in self.listeMethodes:
            espace_ap = espace_ap_funct(self.len_max, len(methode))
            methodesStr += f'| {methode} {espace_ap}|' + '\n'
        espace_ap_nom_classe = espace_ap_funct(self.len_max, len(self.nomClasse))
        string = (f'| {self.separateur} |\n'
                  f'| {self.nomClasse} {espace_ap_nom_classe}|\n'
                  f'| {self.separateur} |\n'
                  f'{attributsStr}'
                  f'| {self.separateur} |\n'
                  f'{methodesStr}'
                  f'| {self.separateur} |')
        return string