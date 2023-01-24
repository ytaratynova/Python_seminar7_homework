def main_menu():
    print()
    print('Главное меню:')
    menu_list = ['Показать все контакты',
                 'Поиск', 
                 'Создать контакт',
                 'Удалить контакт',
                 'Экспорт контактов',
                 'Завершение работы'
                ]
    for i in range(len(menu_list)):
        print(f'    | {i+1}. {menu_list[i]}')
    print()

    user_input = int(input('Введите команду: '))
    return user_input

def show_all(db):
    print('Ваша телефонная книга: ')
    if db_success(db):
        for i in range(len(db)):
            string = ''
            user_id = str(i + 1)
            string = string + '\n' + user_id + '. '
            for j in range(len(db[i])):
                string += db[i][j] + ' '
            print(string.replace('\n',''))
           

def db_success(db):
    if db:
        return True
    else:
        return False
    
def exit_program():
    print('Завершение программы')      
    exit()

def create_contact():
    print('Создание нового контакта')
    new_contact = []
    firstname = input('Введите фамилию: ')
    new_contact.append(firstname)
    lastname = input('Введите имя: ')
    new_contact.append(lastname)
    phone = input('Введите телефон: ')
    new_contact.append(phone)
    com = input('Введите комментарий: ')
    new_contact.append(com)
    print('Контакт записан')
    return new_contact

def search_info(db):
    in_contact = False
    search_for = input('Введите фамилию контакта: ')
    print('Осуществляем поиск контакта...')
    for i in range(len(db)):
        if search_for.lower() in db[i][0].lower():
            for j in range(len(db[i])):
                print(db[i][j].upper(), end = ' ')
                find = i
                in_contact = True
            print()
    if in_contact == False:
         print(f'Контакт с фамилией, похожей на  "{search_for}" не найден')
         find = ''
    return find

def del_confirm():
    yes_or_no = input('Вы уверены, что хотите удалить контакт? (Да/Нет): ')
    if yes_or_no == 'Да':
        return True
    else:
        return False




    