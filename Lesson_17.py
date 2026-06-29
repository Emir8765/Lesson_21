# class C1:
#     def __init__(self, name, battery, hp):
#         self.name = name
#         self.battery = battery
#         self.hp = hp

    # def say_hi(self):
    #     print(f'Привет, я {self.name}')
    #
    # def charge(self, amount):
    #     self.battery += amount
    #     print(f'{self.name} подзарядился на {amount}%. Теперь заряд: {self.battery}')
    #
    # def move(self, distance):
    #     print(f'{self.name} проехал {distance} метров')

    # def attack(self, target):
    #     target.hp -= 10
    #     print(f'{self.name} attacked {target.name}! {target.name} have {target.hp} HP.')

# r1 = C1('Maкс', 80)
# r1.say_hi()
#
# r2 = C1('Макс', 20)
# r2.charge(80)
#
# r3 = C1('Макс', 20)
# r3.move(100)

# r4 = C1('Мax', 20, 90)
# r5 = C1('Billy', 20, 80)
# r4.attack(r5)

# Объект.метод()


# s#1
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print(f'Hello! My name is {self.name} i am {self.age} years old')
#
# call = Pet('Max', 4)
# call.greet()
#
# #2
# class Player:
#     def __init__(self, name, jump):
#         self.name = name
#         self.jump = jump
#
#     def jumping(self):
#         print(f'Player {self.name} is {self.jump}')
#
# callb = Player('DragonX', 'jumping')
# callb.jumping()
#
# #3
# class Fighter:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#
#     def attack(self, target):
#         target.hp -= 10
#         print(f'{self.name} attacking {target.name}! {target.name} have {target.hp}' )
#
# call1 = Fighter('Max', 100)
# call2 = Fighter('Billy', 90)
# call1.attack(call2)
#
# #4
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#
#     def deposit(self,amount):
#         self.balance += amount
#         print(f'Пополнение на {amount}. New balance: {self.balance}')
#
# callback = BankAccount(5000)
# callback.deposit(2000)
#
# #5
# class Phone:
#     def __init__(self, battery):
#         self.battery = battery
#
#     def check_battery(self):
#         if self.battery < 20:
#             print(f'Внимание! Hизкий заряд батареи: {self.battery}%')
#         else:
#             print('Its ok')
#
# callback = Phone(15)
# callback.check_battery()
