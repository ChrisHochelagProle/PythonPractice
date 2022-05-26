"""
Fonction qui cree un login avec un nom un prenom et deux entier. on utilier lentier un pour isoler les X premiers
caracteres de nom et le deuxieme pour isoler les Y premier caracteres de prenom.

Le resultat est une concatenation de ces deux chaines.
"""


def create_login(nom, prenom, taille1, taille2):
    return nom[:taille1]+prenom[:taille2]


print("Le login recommande est:", create_login("Christo", "Mondor", 4, 2))
