# [вырaжение for переменная in коллекция if условие]

squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(squares)

list1 = [x for x in range(1, 11)]
# print(list1)

text = 'hello'
# let = {ch for ch in text}
# print(let)

codes = {ch: ord(ch) for ch in 'abc'}
# print(codes)

numbers =[1,2,3,4,5,6]
sq = [x**2 for x in numbers]
# print(sq)

sqrs = [x for x in range(10) if x % 2 == 0]
# print(sqrs)

with open ('history.txt') as f:
    positives = [int(line) for line in f if int(line) > 0]
# print(positives)

# names = ['Аня', 'Боря', 'Катя', 'Аня']
# unique_names = {name for name in names}
# print(unique_names)



#1
# sqr = [x**2 for x in range(1,11) if x % 2 == 0]/
# print(sqr)

#2
# txt = input('Write any text: ')
# let = [l for l in txt]
# print(let)

#3
# list = ['hello', 'python']
# listlen = [(word, len(word)) for word in list]
#
# for word, length in listlen:
#     print(f'{word} : {length}')

#4
# l = [[1,2], [3,4], [5]]
# res = [num for sub in l for num in sub]
# print(res)

#5
# n = ['ivan', 'katya']
# cn = [nm +'@school.com' for nm in n]
# print(cn)