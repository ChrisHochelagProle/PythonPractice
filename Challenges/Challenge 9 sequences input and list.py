"""
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters
in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
raw_input() let you input anything without showing text in the command.
if variable: will let you check if a variable is not null i think
"""
lines = []

while True:
    ligne = input("")
    if ligne:
        lines.append(ligne.upper())
    else:
        break

for lignes in lines:
    print(lignes)

