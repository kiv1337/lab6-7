# На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось;

start_numbers = set()

text = input("Введите строку с числами: ")

numbers = text.split()
for el in numbers:
    el = int(el)
    if el in start_numbers:
        print("YES")
    else:
        print("NO")
        start_numbers.add(el)
print(type(start_numbers))


