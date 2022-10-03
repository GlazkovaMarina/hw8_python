import csv
import log
def read():
    while True:
        mode = int(input("По какому полю осуществить поиск:\nнажмите 1, если по ФИО,\nнажмите 2, если по номеру телефона,\nнажмите 3, если по должности,\nнажмите 4, если по зарплате: "))
        if mode == 1:
            find_fio()
            break
        elif mode == 2:
            find_number()
            break
        elif mode == 3:
            find_position()
            break
        elif mode == 4:
            find_salary()
            break
        else:
            print("Некорректный ввод!")

def find_fio():
    fio = input("Введите фамилию и инициалы через точку (Н-р: Петров И.И.): ")
    log.log("экспорт", fio)
    with open('data.csv') as f:
        reader = csv.reader(f)
        i = 0
        flag = 0
        for row in reader:
            if i != 0:
                if row[0] == fio:
                   flag = 1
                   print(row)
            i = 2
        if flag == 0:
            print("Данные о таком сотруднике отсутствуют!")

def find_number():
    number = input("Введите номер телефона данного сотрудника: ")
    log.log("экспорт", number)
    with open('data.csv') as f:
        reader = csv.reader(f)
        i = 0
        flag = 0
        for row in reader:
            if i != 0:
                if row[1] == number:
                   print(row)
                   flag = 1
            i = 2
        if flag == 0:
            print("Данные о таком сотруднике отсутствуют!")

def find_position():
    position = input("Введите должность: ") 
    log.log("экспорт", position)
    with open('data.csv') as f:
        reader = csv.reader(f)
        i = 0
        flag = 0
        for row in reader:
            if i != 0:
                if row[2] == position:
                   print(row)
                   flag = 1
            i = 2
        if flag == 0:
            print("Данные о таком сотруднике отсутствуют!")

def find_salary():
    salary = input("Введите зарплату (Н-р: 50 тыс. руб.): ")
    log.log("экспорт", salary)
    with open('data.csv') as f:
        reader = csv.reader(f)
        i = 0
        flag = 0
        for row in reader:
            if i != 0:
                if row[3] == salary:
                   print(row)
                   flag = 1
            i = 2
        if flag == 0:
            print("Данные о таком сотруднике отсутствуют!")