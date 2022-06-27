nom_de_famille = lambda chaine : chaine.split(" ")[1]
liste_de_nom_complets = ["John Postel", "Linus Torvald", "Vint Cerf", "Radia Perlman"]

print(list(sorted(liste_de_nom_complets, key=nom_de_famille)))