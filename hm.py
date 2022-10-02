# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import p
# d =  int(input("Введите число для заданной точности числа Пи:\n"))
# print(f'число Пи с заданной точностью {d} равно {round(p, d)}')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# number = int(input("Введите число: "))
# x = 2
# sp = []
# n = number
# while x <= number:
#     if number % x == 0:
#         sp.append(x)
#         number //= x
#         x = 2
#     else:
#         x += 1
# print(f"Простые множители числа {n}: {sp}")

# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# sp = list(map(int, input("Введите числа через пробел: ").split()))
# new_list = []
# for i in sp:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# k = int(input('Введите коэффициент: '))
# a = int(random.randint(0,100))
# b = int(random.randint(0,100))
# c = int(random.randint(0,100))

# if a != 0:
#     a1 = (str(a) + "x^" + str(k) + " + ")
# else:
#     a1 = (str())

# if b != 0:
#     b2 = (str(b) + "x" + " + ")
# else:
#     b2 = (str())

# if c != 0:
#     c3 = (str(c) + " = 0")
# else:
#     c3 = (str())

# with open('lessons4/file.txt', 'w', encoding='utf-8') as file:
#     file.write(f'{a1}{b2}{c3}')
# print(f'{a1}{b2}{c3}')

# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

with open('lessons4/file1.txt','r') as file:
    file1 = file.readline()
    list_of_file1 = file1.split()


with open('lessons4/file2.txt','r') as file:
    file2 = file.readline()
    list_of_file2 = file2.split()

print(f'{list_of_file1} + {list_of_file2}')
file3 = list_of_file1 + list_of_file2

with open('lessons4/file3.txt', 'w', encoding='utf-8') as file:
    file.write(f'{list_of_file1} + {list_of_file2}')