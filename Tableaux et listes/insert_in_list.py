def add_in_order(number, ordered_liste):
    for i in range(0, len(ordered_liste)):
        if number <= ordered_liste[i]:
            ordered_liste.insert(i, number)
            break
        else:
            ordered_liste.append(number)
            break
    return ordered_liste


ordered_list = [14, 50, 100, 125, 500]

print(add_in_order(510, ordered_list))
