class Ville:
    def __init__(self, nom: str, population: int):
        self.nom = nom
        self.population = population

    def infos(self):
        infos = f'Nom: {self.nom}\n' \
                f'Population: {self.population} habitant.e.s\n'
        return infos


class Pays:
    def __init__(self, codeISO2: str, nom: str, villes: list):
        self.codeISO2 = codeISO2
        self.nom = nom
        self.villes = villes

    def infos(self):
        villes = ""
        for ville in self.villes:
            villes += ville.infos()
        infos = f'Nom: {self.nom}\n' \
                f'Code iso 2: {self.codeISO2}\n' \
                f'Villes: \n{villes}'
        return infos

montreal = Ville("Montreal", 1800000)
joliette = Ville("Joliette", 100000)
list_villes_canada = [montreal, joliette]
canada = Pays("56784", "Canada", list_villes_canada)
print(canada.infos())