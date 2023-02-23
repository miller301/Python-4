# Задача 22
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите количество чисел первого набора: '))
m = int(input('Введите количество чисел второго набора: '))
a = []
b = []

for item in range(n):
    number = (int(input('Введите число для 1 набора: ')))
    a.append(number)
for item in range(m):
    number = (int(input('Введите число для 2 набора: ')))
    b.append(number)

numbers_set_1 = set(a)
numbers_set_2 = set(b)
print(numbers_set_1)
print(numbers_set_2)
result_sets = numbers_set_1.intersection(numbers_set_2)
result_list = list(result_sets)
result_list.sort()
print(result_list)