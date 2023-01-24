db_list = []

def read_db(path):
    global db_list
    with open(path, 'r', encoding = 'UTF-8') as file:
        my_list = file.readlines()
        for line in range(len(my_list)):
            line_list = my_list[line].split(';')
            db_list.append(line_list)
    return db_list

def write_db(path):
    with open(path, 'w', encoding='UTF-8') as file:
        for i in range(len(db_list)):
            line = ''
            for j in range(len(db_list[i])):
                line +=  db_list[i][j] + '; '
            line = line.replace(';\n','').replace('\n;','') + '\n'
            file.writelines(line)

def del_conact(db,find):
    for i in range(len(db)):
        if i == find:
            db[i].clear()
    db = [el for el in db if el]
    return db

def export_csv(path):
    with open(path, 'w') as file:
        file.write(f'Фамилия; Имя; Телефон; Комментарий\n')
        for i in range(len(db_list)):
            file.writelines(f'{db_list[i][0]};{db_list[i][1]};{db_list[i][2]};{db_list[i][3]}')
            