# 3 Задайте последовательность чисел.
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# *Пример*
# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

n = list(input('Задайте последовательность чисел: '))
# n2 = list(set(n))
n2 = list(dict.fromkeys(n))
print(n2)


