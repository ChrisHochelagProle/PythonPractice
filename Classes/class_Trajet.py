class Trajet:

    def __init__(self, villeDepart: str, villeArriver: str,
                 nbPassagers: int):
        self.villeDepart = villeDepart
        self.villeArriver = villeArriver
        self.nbPassagers = nbPassagers
        self.kmParcourus = 0
        
    def avance(self, kilometresAdditionnels: int):
        self.kmParcourus += kilometresAdditionnels

    def embarque(self, nbPassagersAdditionnels):
        self.nbPassagers += nbPassagersAdditionnels

    def debarque(self, nbPassagerDeMoins: int):
        self.nbPassagers -= nbPassagerDeMoins

    def info(self):
        return f'Ville de depart: {self.villeDepart}\n' \
               f"Ville d'arriver: {self.villeArriver}\n" \
               f"Nombre de passagers: {self.nbPassagers}\n" \
               f"Kms parcourus: {self.kmParcourus}"

    def __str__(self):
        return f'{self.__class__}'


