def stringToDictReversed(phrase):
    dict = {}
    list_mots = phrase.split(" ")
    for mot in list_mots:
        dict[mot] = mot[::-1]
    return dict


phrase = input("Entrez une phrase: ")
print(stringToDictReversed(phrase))
