def p1():
    print(' '.join([input("Введите слово:") for i in range(int(input("Введите колличество слов:")))]))


def p2():
    print("Введите слова, чтобы закончить ввод напишите 'stop'")
    while True:
        a = input("Введите слово:")
        if a == 'stop':
            print("Вы остановили процесс")
            break
        print(' '.join(a))


def p3():
    b = ("Введите слово:")
    while (b2 := str(input())) != "stop":
        if "ф" in b2 or "Ф" in b2:
            print("Ого! Это редкое слово")
        else:
            print("Эх, это не очень редкое слово")


def p4():
    from random import randint
    print("Для завершения игры введите: stop")
    while True:
        a = randint(1,100)
        b = randint(1,100)
        print(f"{a} + {b} = ", end= '')
        otvet = input()
        while not otvet.isdigit() and otvet != 'stop':
            print("Ошибка, повторите ввод", end= '')
            otvet = input()
            if otvet == 'stop':
                break
            otvet = int(otvet)
            if a+b == otvet:
                print("Верно")
            else:
                print("Ответ неверный")

p1(),p2(),p3(),p4()
