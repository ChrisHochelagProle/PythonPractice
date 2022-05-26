"""
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
sentence_to_sort = input("Entrez des mots separes par des virgules. On va les trier par ordre alphabetique.")
list_unsorted = sentence_to_sort.split(',')
list_unsorted.sort()
sentence = ""
for word in list_unsorted:
    if list_unsorted[len(list_unsorted)-1] != word:
        sentence += word + ","
    else:
        sentence += word

print(sentence)
