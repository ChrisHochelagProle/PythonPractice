"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method
"""
liste_nombre = []

for nombre in range(2000, 3201):
    if nombre % 7 == 0 and nombre % 5 != 0:
        liste_nombre.append(nombre)

print(liste_nombre)
