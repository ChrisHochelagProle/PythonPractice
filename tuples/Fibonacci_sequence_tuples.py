# def fibonacci(terme):
#     sequence = (0, 1)
#     result = 0
#     # ici si je voulais ne pas afficher le terme dans les resultats il faudrait revoir la condition.
#     # fonctionne seulement si le terme est dans la sequence
#     while result != terme:
#         result = sequence[-2] + sequence[-1]
#         sequence += (result,)
#     return sequence
#
#
# print(fibonacci(34))

# Version qui donne les x premiers nombre de la sequence
# def fibonacci(jusqua):
#     sequence = ()
#     active = 0
#     while active < jusqua:
#         if active == 0 or active == 1 and sequence[-1] != 1:
#             sequence += (active,)
#             active += 1
#         else:
#             sequence += (sequence[-2] + sequence[-1],)
#             active += 1
#     return sequence
#
#
# print(fibonacci(8))
