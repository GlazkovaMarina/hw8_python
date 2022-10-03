import inp
def start():
    while True:
        mode = int(input("Выберите действие:\nдля импорта нажмите 1,\nдля экспорта нажмите 2,\nдля завершения работы программы нажмите 0: "))
        if 1<= mode <= 2 :
            inp.input_mode(mode)
        elif mode == 0:
            print("Завершение работы!")
            break
        else:
            print("Некорректный ввод!")