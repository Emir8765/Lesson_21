import datetime

import random

import math

tickets = {}

while True:
    print("Выберите действие\n 1.Выдача талона \n2.Сдача талона")
    main_choice = input('Ваш выбор: ')
    if main_choice == '1':
        car_num = input('Введите номер машины: ')
        tickets_id = str(random.randint(100000, 999999))
        tickets[tickets_id] = {
            'car number' : car_num,
            'entry time' : datetime.datetime.now()
        }
        print('Талон выдан')
        print('Номер талона: ', tickets_id)
        print('Номер машины: ', car_num)
    elif main_choice == '2':
        search_id = input('Введите номер талона: ')
        if search_id not in tickets:
            print('Ошибка: Талон с таким номером не найден')
            continue
        car_num = tickets[search_id]
        print('Счет к оплате: ')
        print('Номер талона: ', search_id)
        print('Номер машины: ', car_num)
    else:
        print('Error')

# almost finished