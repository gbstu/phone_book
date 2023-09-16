# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import os
import pathlib

def get_fool_file_name():
    f = os.path.abspath(__file__)
    p = os.path.dirname(os.path.abspath(__file__))
    fool_file_name = pathlib.Path(p,phone_book_file_name)
    return fool_file_name

def load_from_file(phone_list_name_file):
    if os.path.isfile(phone_list_name_file):
        with open(phone_list_name_file, 'r', encoding='UTF-8') as phone_list_file:
            phone_lines = phone_list_file.read()
         # print(phone_lines)
            phone_book_list = phone_lines.splitlines()
            for i in phone_book_list:
                if len(i.strip())==0:
                    phone_book_list.remove(i)
                    global flag_of_change
                    flag_of_change = True
    else:
        with open(phone_list_name_file, 'w', encoding='UTF-8') as phone_list_file:
            phone_list_file.write('')
    return phone_book_list

def save_to_file(phone_list_name_file):
    if flag_of_change:
        with open(phone_list_name_file, 'w', encoding='UTF-8') as phone_list_file:
            phone_lines =  '\n'.join(phone_book_list)
            phone_list_file.write(phone_lines)

def interface_contact():
    print()
    text_masseges = ('Введите 1 для поиска контакта,',
        '\t2 для добавления контакта,',
        '\t3 для вывода всех контактов,',
        '\t4 найти и изменить контакт,',
        '\t5 изменить контакт по индексу строки,',
        '\t6 найти и удалить контакт,',
        '\t7 удалить контакт по индексу строки,',
        '\t8 отсортировать список,',
        '\t0 для выхода: ')
    text_massege = '\n'.join(text_masseges)
    interfeis_act = input(text_massege)
    print("-"*60)
    while interfeis_act != '0':
        match interfeis_act:
            case '1':
                find_in_phone_book()
            case '2':
                add_contact()
            case '3':
                print_contacts(True)
            case '4':
                edit_find_contact()
            case '5':
                edit_contact_by_index()
            case '6':    
                del_find_contact()
            case '7':
                del_contact_by_index()
            case '8':
                sort_list()
            case _:
                print_contacts()

        print("-"*60)
        interfeis_act = input(text_massege)
    else:
        save_to_file(phone_list_file)

def sort_list():
    phone_book_list.sort()
    global flag_of_change
    flag_of_change = True

def yes_no(message_y_n = "Да/Нет (д/н | y/n): ") -> bool:
    ansver = input(message_y_n)
    if ansver.upper() in ('Y','YES','Д','ДА','1'):
        return True
    return False

def input_contact():
            last_name  = input("Введите фамилию: ")        
            first_name = input("Введите имя: ")
            patronim = input("Введите отчество: ")
            telefon = input("Введите телефон: ")
            while not telefon[1:].isdigit():
                print('Вы ввели неправильный телефон (только цифры) ')
                telefon = input("Введите телефон: ")
            return last_name, first_name, patronim, telefon

def add_contact():
    last_name, first_name, patronim, telefon = input_contact()
    print(f"Добавить контакт {contact_for_print(last_name.title() + ', ' +  first_name.title() + ', ' +patronim.title()+ ', '+  telefon)}? ")
    if yes_no():
        phone_book_list.append(last_name.title() + ', ' +  first_name.title() + ', ' +patronim.title()+ ', '+  telefon)
        global flag_of_change
        flag_of_change = True

def find_contact(str_find, position = 0):
    str_find = str_find.upper()
    if position < len(phone_book_list):
        for i in range(position, len(phone_book_list)):
            if str_find in phone_book_list[i].upper():
                # print('проверка поиска : ', i, str_find, phone_book_list[i].upper())
                return i
    return None

def find_in_phone_book():
    find_str = input('Введите строку для поиск по всем полям без учета регистра: ')
    none_contact = True
    p = find_contact(find_str, 0)
    while p != None:
        print('Контакт найден:', p, contact_for_print(phone_book_list[p]))
        none_contact = False
        p = find_contact(find_str, p+1)
    if none_contact:
        print('Контакт не найден')

def del_find_contact():
    print('ПОИСК И УДАЛЕНИЕ КОНТАКТА')
    find_str = input('Введите строку для поиск по всем полям без учета регистра: ')
    none_contact = True
    p = find_contact(find_str, 0)
    while p != None:
        none_contact = False
        found_contact = contact_for_print(phone_book_list[p])
        print('Контакт найден:', p, found_contact)
        print('Удалить контакт?')
        if yes_no():
            phone_book_list.remove(phone_book_list[p])
            print(f"Контакт {found_contact} удален.")
            global flag_of_change
            flag_of_change = True
        print(f"Продолжить поиск строки {find_str} ?")
        if yes_no():
            none_contact = True
            p = find_contact(find_str, p+1)
        else:
            p = None
    if none_contact:
        print('Контакты не найдены')

def del_contact_by_index():
    find_index = int(input('Введите индекс строки контакта для удаления: '))
    if find_index < len(phone_book_list):
        print('Удалить контакт?', find_index, contact_for_print(phone_book_list[find_index]))
        if yes_no():
            phone_book_list.remove(phone_book_list[find_index])
            global flag_of_change
            flag_of_change = True
    else:
        print('Контакт не найден')

def edit_find_contact():
    print('ПОИСК И ИЗМЕНЕНИЕ КОНТАКТА')
    find_str = input('Введите строку для поиск по всем полям без учета регистра: ')
    none_contact = True
    p = find_contact(find_str, 0)
    while p != None:
        none_contact = False
        found_contact = contact_for_print(phone_book_list[p])
        print('Контакт найден:', p, found_contact)
        print('Изменить?')
        if yes_no():
            last_name, first_name, patronim, telefon = input_contact()
            print("контакт", found_contact)
            phone_book_list[p] = last_name.title() + ', ' +  first_name.title() + ', ' +patronim.title()+ ', '+  telefon
            print(f"заменен на: {contact_for_print(last_name.title() + ', ' +  first_name.title() + ', ' +patronim.title()+ ', '+  telefon)}")
            global flag_of_change
            flag_of_change = True
        print(f"Продолжить поиск строки {find_str} ?")
        if yes_no():
            none_contact = True
            p = find_contact(find_str, p+1)
        else:
            p = None
    if none_contact:
        print('Контакт не найден')    

def edit_contact_by_index():
    find_index = int(input('Введите индекс строки контакта для измененияния: '))
    if find_index < len(phone_book_list):
        old_contact = contact_for_print(phone_book_list[find_index])
        print('Изменить контакт?', find_index, old_contact)
        if yes_no():
            last_name, first_name, patronim, telefon = input_contact()
            print("контакт", old_contact)
            phone_book_list[find_index] = last_name.upper() + ', ' +  first_name.upper() + ', ' +patronim.upper()+ ', '+  telefon
            print(f"заменен на: {contact_for_print(last_name.title() + ', ' +  first_name.title() + ', ' +patronim.title()+ ', '+  telefon)}")
             
            global flag_of_change 
            flag_of_change = True
    else:
        print('Контакт не найден')

def create_phone_number(n):
    m = ''.join(map(str, n))
    if len(n)==5:
        return f" {m[0]}-{m[1:3]}-{m[3:]}"
    elif len(n)==6:
        return f"  {m[:3]}-{m[3:]}"
    elif len(n)==10:
        return f"  ({m[:3]}) {m[3:6]}-{m[6:]}"
    elif (len(n)==11 and m[0]=='8'):
        return f" {m[0]}({m[1:4]}) {m[4:7]}-{m[7:]}"
    elif (len(n)==12 and m[0]=='+'):
        return f"{m[:2]}({m[2:5]}) {m[5:8]}-{m[8:]}"
    else:
        return n

def contact_for_print(string_contact):
    fio_n = []
    fio_n = list(string_contact.split(','))
    fio_n = list(map(lambda s: s.strip().title(), fio_n))
    # fio_n = list(map(lambda s: s.title(), fio_n))
    if len(fio_n)==4:
        fio_n[3] = create_phone_number(fio_n[3])
    return ' '.join(fio_n)

def print_contacts(show_index = False):
    print("="*60)
    if len(phone_book_list)>0:
        if show_index:
            j = 0
            for i in phone_book_list:
                print(str(j)+" ",contact_for_print(i))
                j += 1
        else:
            for i in phone_book_list:
                print(i)
    else:
        print("НЕТ ДАННЫХ")    
    print("="*60)
    


phone_book_file_name = "phone_book.txt"
phone_book_list = []

flag_of_change = False 

phone_list_file = get_fool_file_name()
phone_book_list = load_from_file(phone_list_file)

interface_contact()
