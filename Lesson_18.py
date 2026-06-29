#HАСЛЕДОВАНИЕ И КАПСУЛЯЦИЯ

# Наследование
# class Hello:
#     def hello(self):
#         print('Hello')
#
# class Say(Hello):
#     def say_it(self):
#         print('I am the Biggest Bird')
#
# say = Say()
# say.hello()
# say.say_it()


# class Transport:
#     def move(self):
#         print('Friends')
#
# class Auto(Transport):
#     def honk(self):
#         print('makes us weak')
#
# auto = Auto()
# auto.move()
# auto.honk()


# Инкапсуляция
# одно нижнее подчёркивание - защищенные данные
# два нижних подчеркивания - приватные данные

# class Words:
#     def __init__(self):
#         self._recipe = 'Sorry'
#
# class Secret(Words):
#     def reveal(self):
#         print(self._recipe)
#
# s1 = Secret()
# s1.reveal()


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#
#     def get_balance(self):
#         return self.__balance
#
#
# acc = BankAccount('Айгуль', 1000)
# # print(acc.__balance) - error
# print(acc.get_balance())


# class Animal:
#     def __init__(self):
#         print('Я животное')
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         print('Я собака')
#
# Dog()

# class Phone:
#     def __init__(self, price, brand):
#         self.price = price
#         self.brand = brand
#
#
# class Iphone(Phone):
#     def __init__(self, brand, price, colour):
#         super().__init__(brand, price)
        # self.colour = colour



#1
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
# class Cat(Animal):
#     def info(self):
#         print(f'Это кот по кличке {self.name}')
#
#     def meow(self):
#         print(f'{self.name} говорит: Мяу!')
#
# class Dog(Animal):
#     def info(self):
#         print(f'Это пёс по кличке {self.name}')
#
#     def bark(self):
#         print(f'{self.name} говорит: Гав!')
#
# cat = Cat('Tom')
# cat.info()
# cat.meow()
#
# dog = Dog('Бобик')
# dog.info()
# dog.bark()

#2
# class Transport:
#     def __init__(self):
#         self.__mileage = 0
#
#     def increase_mil(self, km):
#         if km > 0:
#             self.__mileage += km
#
#     def get_mil(self):
#         return self.__mileage
#
# class Car(Transport):
#     def drive(self,distance):
#         self.increase_mil(distance)
#         print(f'Машина проехала {distance} км. Текущий пробег: {self.get_mil()}')
#
# class Bike(Transport):
#     def ride(self, distance):
#         self.increase_mil(distance)
#         print(f'Мотоцикл проехал {distance} км.Текущий пробег: {self.get_mil()}')
#
# my_car = Car()
# my_car.drive(100)
#
# my_bike = Bike()
# my_bike.ride(100)

#3
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
#
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f'Пополнение баланса на {amount}. Новый баланс {self.__balance}')
#
#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print('Недостаточно средств')
#
#     def get_Balance(self):
#         return self.__balance
#
# acc = BankAccount(2000)
# acc.deposit(2000)

#4
# class Product:
#     def __init__(self, item, price):
#         self.item = item
#         self.price = price
#
# class DiscountProduct(Product):
#     def __init__(self, item, price, discount):
#         super().__init__(item, price)
#         self.discount = discount
#
#     def show__discount(self):
#         print(f'Товар: {self.item} Цена: {self.price} Скидка: {self.discount}%')
#
# product = DiscountProduct('Наушники', 4000, 20)
# product.show__discount()

