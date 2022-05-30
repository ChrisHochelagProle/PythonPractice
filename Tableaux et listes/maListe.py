ma_liste = [15, "Bonjour", [0, "bonsoir"], 15, 100]
copy = ma_liste.copy()
assert copy[3] * 100 == 1500
assert copy == [15, "Bonjour", [0, "bonsoir"], 15, 100]
a = copy.pop(3)
assert copy == [15, "Bonjour", [0, "bonsoir"], 100]
copy = ma_liste.copy()
copy.insert(2, 25)
assert copy == [15, "Bonjour", 25, [0, "bonsoir"], 15, 100]
