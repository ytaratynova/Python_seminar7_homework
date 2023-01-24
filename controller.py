import model
import view

def input_handler(inp: int):
    if view.db_success(model.db_list) == False:
                model.read_db('database.txt')
    match inp:
        case 1:
           view.show_all(model.db_list)
        case 2:
           view.search_info(model.db_list)
        case 3:
           model.db_list.append(view.create_contact())
           model.write_db('database.txt')
        case 4: 
            search_result = view.search_info(model.db_list)
            if view.del_confirm() == True:
                 model.db_list = model.del_conact(model.db_list, search_result)
                 print(model.db_list)
        case 5:
            model.export_csv('telephone_book.csv') 
        case 6:
            model.write_db('database.txt')
            view.exit_program()
              

def start():
    while True:
        user_input = view.main_menu()
        input_handler(user_input)