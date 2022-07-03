from math import sqrt

number_list = [1, 2, 3, 4]


def squaring(number):
    return number ** 2

'''Написати свій генератор який буде працювати як функція
 map тобто повертати результат виконання функці (перший параметр)  на кожен елемент зі списку (другий параметр)'''
def my_map(func, items):
    for i in items:
        yield func(i)


print(list(my_map(squaring, number_list)))
print(my_map(sqrt, number_list))

'''Написати свій генератор який буде приймати завжди три параметри start, end, step і повертaти посимвольно числа 
в даних межах. Значення кроку за замовчуванням має бути 1'''
def my_range(start, stop, step=1):
    if start < stop:
        while start < stop:
            yield start
            start += step

    elif start > stop and step < 0:
        while start > stop:
            yield start
            start += step


for i in my_range(1, 5):
    print(i)

for i in my_range(50, 1, -7):
    print(i)

for i in my_range(5, 1):
    print(i)
