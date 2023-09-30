# Нечётные числа из исходного кортежа.


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
odd_numbers = []

for el in numbers:                 # odd_numbers = [el for el in numbers if el % 2 != 0]
    if el % 2 != 0:
        odd_numbers.append(el)

print(odd_numbers)

