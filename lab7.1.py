# Найти среднее геометрическое всех чисел в кортеже.


numbers = (1, 2, 3, 4, 5)

multi = 1

for el in numbers:
    multi *= el

geometric_mean = multi ** (1 / len(numbers))


print("Среднее геометрическое:", geometric_mean)
