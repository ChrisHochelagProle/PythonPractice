dico = dict()
dico['computer'] = 'ordinateur'
dico['mouse'] = 'souris'
dico['keyboard'] = 'clavier'
print(dico)
print(dico['mouse'])
del dico['computer']
print(dico)
print(len(dico))
if 'mouse' in dico:
    print("Oui l'element est disponible")
else:
    print("Non l'element n'est pas disponible")

print(dico.keys())
for key in dico.keys():
    print("Cle:", key, " --- valeur :", dico[key])

print(list(dico.keys()))
print(dico.values())
print(dico.items())

# pour une vraie copie et pas une reference
dico_copie = dico.copy()
del dico['mouse']
print(dico)
print(dico_copie)

# si on for key in dict cest parce quon utilise juste les cles, pour les valeurs il faut dico[key]
print("Keys")
for key in dico_copie:
    print(key)

print("Keys with.keys")
for key in dico_copie.keys():
    print(key)

print("Values")
for key in dico_copie:
    print(dico_copie[key])

# utiliser tuple pour avoir les deux
print("Key Value pair")
for key, value in dico_copie.items():
    print(key, value)

# on peut utiliser plusieurs types de variables comme key
avion = dict()
avion[1235] = 'Paul Bertrantd'
avion[4526] = 'Laure Poupier'
avion[5897] = 'Charle Loupier'

for key, value in avion.items():
    print(key, value)

# il y aura une erreur si le siege n'existe pas
# print(avion[1111])

# on peut attraper l'erreur comme suit
print(avion.get(1111, 'Pas de valeur ici.'))

# Du fait qu’ils ne sont pas des séquences, les dictionnaires se révèlent donc particulièrement précieux pour gérer des
# ensembles de données où l’on est amené à effectuer fréquemment des ajouts ou des suppressions, dans n’importe quel
# ordre. Ils remplacent avantageusement les listes lorsqu’il s’agit de traiter des ensembles de données numérotées, dont
# les numéros ne se suivent pas.
