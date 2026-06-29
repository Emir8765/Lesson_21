# class Robot:
#     def __init__(self, name):
#         self.name = name
#     def __str__(self):
#         return f"{self.name}"
#
# r = Robot('Max')
# print(r)

# x = 'Hello'
#
# print(str(x))
# print(repr(x))



# 1
# class Animal:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#     # def __str__(self):
#     #     return f"{self.name}, {self.age} года"
#
# cat = Animal("Кот Барсик", 3)
# print(cat)

# 2
# class BankAccount:
#     def __init__(self,amount):
#         self.amount = amount
#     def __add__(self, other):
#         return BankAccount(self.amount + other.amount)
#     def __str__(self):
#         return f'Balance:{self.amount}'
#
# a = BankAccount(1000)
# b = BankAccount(500)
# print(a + b)

# 3
# class Fighter:
#     def __init__(self, level, fight_class):
#         self.level = level
#         self.fight_class = fight_class
#
#     def __eq__(self, other):
#         return {self.level} == {other.level} and {self.fight_class} == {other.fight_class}
#
# Fighter1 = Fighter(10, "Mage")
# Fighter2 = Fighter(10, "Mage")
# print(Fighter2 == Fighter1)

# 4
# class Teams:
#     def __init__(self, players):
#         self.players = players
#
#     def __getitem__(self, index):
#         return self.players[index]
#
#     def __len__(self):
#         return len(self.players)
#
# team = Teams(['Viper', 'Sage', 'Jett'])
#
# print(team[0])
# print(len(team))