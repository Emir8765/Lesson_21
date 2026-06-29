# try:
#     a = input('Выведите первое число')
#     b = input('Выведите второе число')
#     print( int(a) / int(b))
# except TypeError:
#     print('Введите число а не букву')
# except Exception as e:
#     print(f'Произошла неизвестная ошибка')
# finally:
#     print('')

#
# try:
#     f = open('myfile.txt')
#     data = f.read()
# except FileNotFoundError:
#     print('Файл не найден. Проверь имя')
# else:
#     print('Файл прочитан успешно')
# finally:
#     print('Работа с файлами завершена')

#
# age = int(input('How old are you?'))
# if age <= 0:
#     raise ValueError('Age cannot be Negative')


#1
# try:
#     a = input('Write number 1: ')
#     b = input('Write number 2: ')
#     print(int(a) / int(b))
# except ZeroDivisionError:
#     print('Cant divide on a zero')
# except ValueError:
#     print('Write only numbers')
# finally:
#     print('Program is actually over')

#2
# name = input('Write the file name: ')
# try:
#     with open(name, 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print('Write real name of file')

#3
