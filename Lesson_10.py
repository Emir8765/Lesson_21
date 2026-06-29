# import math

# Пример импорта своей библиотеки
# import area
# from area import *

# floor: 15.99 -> 15

# Импорт одной функции
# from math import  pi, ceil as maximize
#
# import area
#
#
# def circumference(radius):
#     return maximize(2*radius*pi)
#
# print('линна окружности с радиусом 4 см: ',circumference(4),  'cm' )
# print('Площадь окружности с радиусом 4 cm: ',area.areaofcircle(4), 'cm^2')




# number1 = int(input('Write your first number: '))
# number2 = int(input('Write your second number: '))
# com = input('Which command (*, -, +, /) you want to use: ')
# if com == '*':
#     print('answer is: ', number1*number2)
# elif com == '-':
#     print('answer is: ',number1-number2)
# elif com == '+':
#     print('answer is: ',number1 + number2)
# elif com == '/':
#     print('answer is: ',number1/number2)
# else:
#     print('Error')


# num1 = int(input('Write your first number: '))
# num2 = int(input('Write your second number: '))
# com = input('Which command (*, -, +, /) you want to use: ')
# def plus(a,b):
#     if com == '+':
#         print('answer is: ', a + b)
#
# def minus(a,b):
#     if com == '-':
#         print('answer is: ', a - b)
#
# def divide(a,b):
#     if com == '/':
#         print('answer is: ', a / b)
#
# def multiple(a,b):
#     if com == '*':
#         print('answer is: ', a * b)
#
# if com == '+':
#     plus(num1, num2)
# elif com == '-':
#     minus(num1, num2)
# elif com == '/':
#     divide(num1, num2)
# elif com == '*':
#     multiple(num1, num2)

# help("modules")
# help("random")
# import random
# lst = ['Камень', 'Ножницы', 'Бумага']
# guest = input('Your choice is: ')
# if guest == 'Камень':
#     print(random.choice(lst))
#     if guest == 'Камень' and random.choice(lst) == 'Бумага':
#         print('you loose')
#     else:
#         print('you win')
#
# if guest == 'Ножницы':
#     print(random.choice(lst))
#     if guest == 'Ножницы' and random.choice(lst) == 'Камень':
#         print('you loose')
#     else:
#         print('you win')
#
# if guest == 'Бумага':
#     print(random.choice(lst))
#     if guest == 'Бумага' and random.choice(lst) == 'Ножницы':
#         print('you loose')
#     else:
#         print('you win')

# import random
# lst = ['Камень', 'Ножницы', 'Бумага']
# guest = input('Your choice is: ')
# # a=input()
# # b=lstr
#
# def game(a, b):
#     if a[0]:
#         print(random.choice(lst))
#         if a[0] and b[2]:
#             print('You lose')
#         elif a[0] and b[0]:
#             print('draw')
#         else:
#             print('you win')
#
#     if a[1]:
#         print(random.choice(lst))
#         if a[1] and b[0]:
#             print('You lose')
#         elif a[1] and b[1]:
#             print('draw')
#         else:
#             print('you win')
#
#     if a[2]:
#         print(random.choice(lst))
#         if a[2] and b[1]:
#             print('You lose')
#         elif a[2] and b[2]:
#             print('draw')
#         else:
#             print('you win')
#
# game(guest, lst)

