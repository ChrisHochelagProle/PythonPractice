# Code 1
# x = (1, 2, 3)
# x[2] = 3
# Console: TypeError: 'tuple' object does not support item assignment

# Code 2
# x = (1, 2, 3)
# print(x[2])
# Console: 3

# Code 3
# x = (1, 2, 3)
# y = (x[0], x[1], x[2])
# print(y)
# Console: (1, 2, 3)

# Code 4
# x = (1, 2, 3)
#
# for i in x:
#     x[i] += 1
#
# print(x)
# Aussi, x[i] ne fonctionne pas car i est un tuple?
# Console: TypeError: 'tuple' object does not support item assignment

# Code 5
# x = (1, 2, 3)
# y = x * 5+2
# Console: TypeError: can only concatenate tuple (not "int") to tuple
# y = x * 5
# print(y)
# Console: (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
