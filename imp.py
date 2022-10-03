import csv
import log
def write():
    while True:
        with open('data.csv', 'a') as f:
            writer = csv.writer(f)
            mode = int(input("Выберите режим записи данных: \nнажмите 1 для ввода данных вручную,\nнажмите 2 для записи данных из файла .csv: "))
            if mode == 1:
                fio = input("Введите фамилию и инициалы через точку (Н-р: Петров И.И.):")
                number = input("Введите номер телефона данного сотрудника: ")
                position = input("Введите должность: ") 
                salary = input("Введите зарплату (Н-р: 50 тыс. руб.): ")
                writer.writerow([fio, number, position, salary])
                log.log("импорт", fio + ' ' + number + ' ' + position + ' ' + salary)
                break 
            elif mode == 2:
                file_name = input("Введите название файла, из которого необходимо считать данные: ")
                with open(file_name) as f:
                    reader = csv.reader(f)
                    i = 0
                    for row in reader:
                        if i != 0:
                            row_copy = row
                            writer.writerow(row_copy)
                            line = ""
                            for elem in row_copy:
                                line += elem + " "
                            log.log("импорт", line)
                        i = 2
                break
            else:
                print("Некорректный ввод!")