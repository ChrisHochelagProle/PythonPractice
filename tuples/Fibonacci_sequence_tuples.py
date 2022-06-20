def fibonacci(terme):
    sequence = (0, 1)
    result = 0
    # ici si je voulais ne pas afficher le terme dans les resultats il faudrait revoir la condition.
    while result != terme:
        result = sequence[-2] + sequence[-1]
        sequence += (result,)
    return sequence


print(fibonacci(34))
