# # 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# # В качестве символа-разделителя используйте пробел.

# some_str = input() # '1 2 3 4 5'
# some_list = some_str.split() # ['1', '2', '3', '4', '5']
# some_int_list = list(map(int, some_list)) # [1, 2, 3, 4, 5]
# print(max(some_int_list), min(some_int_list))

# some_str = input() # '1 2 3 4 5'
# print(max(list(map(int, some_str.split()))), min(list(map(int, some_str.split()))))


# # 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# # 1) с помощью математических формул нахождения корней квадратного уравнения
# # 2) с помощью дополнительных библиотек Python

# import sympy as sm

# x = sm.Symbol('x')
# a = int(input())
# b = int(input())
# c = int(input())
# print(sm.solveset(a * x ** 2 + b * x + c, x))

# # 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


# import sympy as sm
# a = int(input())
# b = int(input())
# print(sm.lcm(a, b))