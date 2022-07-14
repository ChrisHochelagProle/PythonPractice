class Media:
    pass

class Livre(Media):
    pass

class Dictionnaire(Livre):
    pass

d = Dictionnaire()
print(isinstance(d, Media))

