"""
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

"""


class StrOp:
    # Variables de classe
    string = ""

    # Fonctions
    def __init__(self):
        self = self

    def get_string(self):
        return input("Entrez quelque chose: ")

    def print_string(self, string):
        return print(string.upper())


operations = StrOp()
chaine = operations.get_string()
operations.print_string(chaine)
