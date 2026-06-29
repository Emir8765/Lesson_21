# Множества

# Set - оставляет только уникальные значения убирая любые дубликаты (изменяемый)
# frozenset - похож на set но делает список неизменяемым по сути замораживая его
numbers = [1, 2, 2, 3, 4, 4, 5]
uni_numbers = set(numbers)
# print(uni_numbers)

# .add - добавляет элемент, .remove - удаляет элемент и выводит ошибку если такого элемента нет
fruits = {'apple', 'Banan'}
fruits.add('pear')
fruits.remove('Banan')
# print(fruits)

# .discard - Удаляет элемент но не выводит ошибку если такого элемента нет
fruits = {'apple', 'Banan'}
fruits.discard('pineapple')
# print(fruits)

# ищет элемент в списке и возвращает true/false
fruits = {'apple', 'Banan'}
# print('sdin' in fruits)

# убирая одинаковые выводит все уникальные элементы
set1 = {'1', '2', '3'}
set2 = {'1', '4', '3'}
# print(set1 | set2)

# выводит одинаковые элементы списка
# set1 = {'1', '2', '3'}
# set2 = {'1', '4', '3'}
# set3 = set1 & set2
# print(set3)

# выводит уникальные элементы первого или второго списка
# set1 = {'1', '2', '3'}
# set2 = {'1', '4', '3'}
# print(set2 - set1)

# Убирает общие элементы
# set1 = {'1', '2', '3'}
# set2 = {'1', '4', '3'}
# print(set2 ^ set1)


#1
# nums = input('Write your numbers: ').split()
# number = set(nums)
# print(f'Unicue numbers: {number}')

#2
# names = input('Write your names: ').split()
# searchName = input('Кого ищем? ')
# if searchName in names:
#     print(f'Да {searchName} есть в списке')
# else:
#     print(f'Нет {searchName} нет в списке')

#3
# subs = {'Math', 'Physics', 'English'}
# print('Favourite: Math', 'Physics', 'English')
# insch = {'History', 'Physics', 'Math'}
# print('In School: History', 'Physics', 'Math')
# same = subs & insch
# print(f'Same:  {same}')

#4
# students = {'Аня', 'Боря', 'Катя'}
# print('Who Comes: Аня, Боря, Катя')
# whoComes = {'Аня', 'Катя'}
# print('Who come: Аня, Катя')
# didntCome = students - whoComes
# print(f'Who didnt come: {didntCome}')

#5
# words = input('Write some words: ').split()
# uni_words = set(words)
# print(f'Unicue words: {uni_words}')
