# class Robot:
    # pass
# class ключевое слово
# Robot название (с заглавной буквы)
# pass - временная заглушка
from pprint import PrettyPrinter


# class NewC:
#     def __init__(self, name, battery):
#         self.name = name
#         self.battery = battery
#
# r1 = NewC('Name', 80)
# print(r1.name)
# print(r1.battery)


# class F:
#     def __init__(self, age , time):
#         self.age = age
#         self.time = time
#
#
# callBack = F(13,'9:00')
# print(callBack.time)
# print(callBack.age)


#1
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# pPet = Pet('Барсик', 3)
# print(f'Pet Name: {pPet.name}')
# print(f'Age : {pPet.age}')

#2
# class Car:
#     def __init__(self, model,year):
#         self.model = model
#         self.year = year
#
# callCar = Car('BMW M5', 2022)
# print(f'Модель: {callCar.model}')
# print(f'Год выпуска: {callCar.year}')

# 3
# class Player:
#     def __init__(self, nickname, HP):
#         self.nickname = nickname
#         self.HP = HP
#
# callPlayer = Player('DragonX', 100)
# print(f'Player: {callPlayer.nickname}')
# print(f'HP: {callPlayer.HP}')

# 4
# class Phone:
#     def __init__(self, model, GB):
#         self.model = model
#         self.GB = GB
#
# callPhone = Phone('Samsung', '128 GB')
# print(f'Phone: {callPhone.model}, {callPhone.GB}')

# 5
# class Product:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#
# callProduct = Product('Наушники', 1500)
# print(f'Item: {callProduct.item}')
# print(f'Price: {callProduct.price} сом')




class Hero:
    def __init__(self, name, role, health, mana, gold):
        self.name = name
        self.role = role
        self.health = health
        self.mana = mana
        self.gold = gold


Hero1 = Hero('Jack', 'Mag', '100 HP', '450 MP', '75 gold')
Hero2 = Hero('Fill', 'Warrior', '200 HP', '80 MP', '100 gold')
Hero3 = Hero('Tom', 'Archer', '120 HP', '100 MP', '60 gold')
Hero4 = Hero('Phillip', 'Armour-bearer', '70 HP', '50 MP', '40 gold')
Hero5 = Hero('Zeno', 'Killer', '150 HP', '200 MP', '340 gold')

print(f'{Hero1.role} {Hero1.name} have {Hero1.health}, {Hero1.mana} mane and {Hero1.gold} gold')
print(f'{Hero2.role} {Hero2.name} have {Hero2.health}, {Hero2.mana} mane and {Hero2.gold} gold')
print(f'{Hero3.role} {Hero3.name} have {Hero3.health}, {Hero3.mana} mane and {Hero3.gold} gold')
print(f'{Hero4.role} {Hero4.name} have {Hero4.health}, {Hero4.mana} mane and {Hero4.gold} gold')
print(f'{Hero5.role} {Hero5.name} have {Hero5.health}, {Hero5.mana} mane and {Hero5.gold} gold')