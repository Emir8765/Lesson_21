class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__health = 100
        self.__satiety = 50
        self.__happiness = 50

    def info(self):
        print(f'{self.name} - здоровье {self.get_health()} - сытость {self.__satiety} - уровень счастья {self.__happiness}')

    def get_health(self):
        return self.__health

    def feed(self):
        self.__satiety += 25
        self.__happiness -= 10
        if self.__satiety > 100:
            self.__satiety = 100
        elif self.__satiety <= 0:
            self.__satiety = 0
            print(f'{self.name} хочет есть')
        if self.__happiness >= 100:
            self.__happiness = 100
        elif self.__happiness <= 0:
            self.__happiness = 0
            print(f'{self.name} хочет поиграть, поиграй с ним')
        print(f'{self.name} был накормлен сотрудниками. Сытость увеличилась на 15')

    def play(self):
        self.__happiness += 25
        self.__satiety -= 20
        if self.__happiness >= 100:
            self.__happiness = 100
        elif self.__happiness <= 0:
            self.__happiness = 0
            print(f'{self.name} хочет поиграть, поиграй с ним')
        if self.__satiety > 100:
            self.__satiety = 100
        elif self.__satiety <= 0:
            self.__satiety = 0
            print(f'{self.name} хочет есть')
        print(f'{self.name} играет с сотрудниками, ему очень нравиться')


class Lion(Animal):
    def roar(self):
        print(f'{self.name} рычит!!! Публика в восторге!')

class Rhino(Animal):
    def charge(self):
        print(f'{self.name} ломает каменные стены!!! Публика аплодирует!')

class Hippo(Animal):
    def swim(self):
        print(f'{self.name} плавает глубоко под водой!')


simba = Lion('Лев Симба',3)
pedro = Hippo('Бегемот Педро', 4)
rokki = Rhino('Носорог Рокки', 3)

#
simba.roar()
pedro.swim()
rokki.charge()
#
simba.info()
pedro.info()
rokki.info()
#
simba.feed()
pedro.feed()
#
simba.info()
pedro.info()
#
simba.play()
pedro.play()
#
simba.info()
pedro.info()
#


# 1 - Я выбрал тему зоопарка-игры.
# По коду она примерно похожa на простые игры тамагочи.
# Если выбирать из серьезных аналогов то моя программма чем-то похожа на Duolingo.

# 2 - есть класс Animal в котором лежит большинство параметров и логика ухода
# Классы наследники это Lion Rhino Hippo у них есть свои особые методы делающие программу интереснее

# 3 - поля satiety, health, happiness защищены
# я поставил перед ними вот такие знаки: __ .
# Так мы инкапсулируем важные данные и их не смогут поменять наши данные в других местах. Изменения этих параметров доступно строго через безопасные методы feed(), play().

# 4 - уникальные методы есть у каждого наследника
# встроенные методы feed и play

# 5 Примеры вывода
# Лев Симба рычит!!! Публика в восторге!
# Бегемот Педро плавает глубоко под водой!
# Носорог Рокки ломает каменные стены!!! Публика аплодирует!
# Лев Симба - здоровье 100 - сытость 50 - уровень счастья 50
# Бегемот Педро - здоровье 100 - сытость 50 - уровень счастья 50
# Носорог Рокки - здоровье 100 - сытость 50 - уровень счастья 50
# Лев Симба был накормлен сотрудниками. Сытость увеличилась на 15
# Бегемот Педро был накормлен сотрудниками. Сытость увеличилась на 15
# Лев Симба - здоровье 100 - сытость 75 - уровень счастья 40
# Бегемот Педро - здоровье 100 - сытость 75 - уровень счастья 40
# Лев Симба играет с сотрудниками, ему очень нравиться
# Бегемот Педро играет с сотрудниками, ему очень нравиться
# Лев Симба - здоровье 100 - сытость 55 - уровень счастья 65
# Бегемот Педро - здоровье 100 - сытость 55 - уровень счастья 65


# 6 трудно было когда я составлял именно общую логику и я немного использовал ИИ


# 7 после составления основной логики я понял как мне нужно дальше писать и большинство условий составлял сам чем горжусь