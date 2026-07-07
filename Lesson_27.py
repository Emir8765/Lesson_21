users_dict = {
    'Бектур':'1',
    'Эмир':'2',
    'Актан':'3'
}
while True:
    print('Добавить контакт: 1')
    print('Просмотр всех контактов: 2')
    print('Поиск контакта: 3')
    print('Изменение контакта: 4')
    print('Удаление контакта: 5')
    print('Выход: 6')
    users_ans = int(input('Введите номер команды:'))
    if users_ans == 1:
        ask_name = input('Напишите имя контакта:')
        ask_num = input('Напишите номер контакта:')
        if ask_num.isdigit():
            users_dict[ask_name] = ask_num
            print(f'Контакт {ask_name} успешно добавлен')
        else:
            print('Номер должен состоять только из цифр')
    elif users_ans == 2:
        if len(users_dict) > 0:
            print('Список контактов:')
            for name, numbers in users_dict.items():
                print(f'{name}: {numbers}')
        else:
            print('Для добавления новых контактов нажмите: 1 \nСписок пустой')
    elif users_ans == 3:
        search_name = input('Введите имя контакта:')
        if search_name in users_dict:
            print(f'Контакт {search_name}: {users_dict[search_name]}')
        else:
            print(f'Контакт {search_name} не найден')
    elif users_ans == 4:
        change_name = input('Введите имя контакта:')
        if change_name in users_dict:
            new_number = input('Введите новый номер контакта:')
            if new_number.isdigit():
                users_dict[change_name] = new_number
                print(f'Контакт {change_name} изменён на {new_number}')
            else:
                print('Номер должен состоять только из цифр')
        else:
            print('Контакт не найден')
    elif users_ans == 5:
        delete_contact = input('Введите имя контакта:')
        if delete_contact in users_dict:
            del users_dict[delete_contact]
            print(f'Контакт {delete_contact} успешно удалён')
        else:
            print(f'Контакт {delete_contact} не найден')
    elif users_ans == 6:
        break
