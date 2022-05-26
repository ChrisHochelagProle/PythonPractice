"""
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
tuple() method can convert list to tuple

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']
"""
sequence = input("Entrez des nombres separes par une virgule: ")
liste_nombre = sequence.split(',')
tuples_nombre = tuple(liste_nombre)
print(liste_nombre, "\n", tuples_nombre)
