langues = ()
data = ((1, "Francais"), (2, "Francais", "Anglais"), (3, "Espagnol", "Arabe"))

for tuple in data:
    for langue in tuple[1:]:
        if langue in langues:
            continue
        else:
            langues += (langue,)

print("Langues: ", langues)
