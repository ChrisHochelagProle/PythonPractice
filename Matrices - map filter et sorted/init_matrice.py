# 1 ligne en utilisant initialisation a la main
matrice = [[10, 10, 10, 10, 10], [20, 30, 40, 50, 60]]
assert matrice == [[10, 10, 10, 10, 10], [20, 30, 40, 50, 60]]

# 1 ligne using list comprehension
matrice = [[10 for i in range(5)], [i * 10 for i in range(2, 7)]]
assert matrice == [[10, 10, 10, 10, 10], [20, 30, 40, 50, 60]]
print(matrice)