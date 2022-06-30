# Le dictionnaire ci-dessous associe à chaque lettre sa valeur en scrabble français:
scrabble={"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,
          "N":1,"O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":2,"V":4,"W":10,"X":10,"Y":10,"Z":10}

# Chaque joueur utilise ses jetons (un jeton contient une seule lettre) pour former un mot.
# Écrivez un programme qui lit un mot saisi par l'utilisateur et affiche la valeur de ce mot en scrabble.

mot = input("Entrez un mot que vous voulez jouer au scrabble: ")
score = 0
for lettre in mot:
    score += scrabble[lettre.upper()]

print(f'Votre score est {score} points!')
