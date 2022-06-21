def recette_mult(ingredients, multi):
    liste_ingredients = list()
    for ingredient in ingredients:
        active = list(ingredient)
        active[1] = active[1] * 2
        liste_ingredients.append(tuple(active))
    return tuple(liste_ingredients)


ingredients = (("Farine", 450), ("Oeuf", 4), ("Sucre", 420), ("Lait", 310))
print(recette_mult(ingredients, 2))
