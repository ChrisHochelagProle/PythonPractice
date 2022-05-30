jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi', [34, 10]]
print(len(jour))
del(jour[4])
jour.append('samedi')
taille = len(jour)
for i in range(taille):
    print(jour[i])

for item in jour:
    print(item)

