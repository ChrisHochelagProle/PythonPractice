"""
Question 3
Level 1

Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is
an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
Consider use dict()

    # The dict() constructor builds dictionaries directly from sequences of key-value pairs.
    dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
"""


def dict_power(nombre):
    liste_paires = []
    for i in range (1, nombre + 1):
        liste_paires.append((i, i*i))
    return dict(liste_paires)


nombre = int(input("Entrez un nombre: "))
print(dict_power(nombre))
