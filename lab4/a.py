def p1():
    number = int(input("Введите число:"))
    b = number % 3
    if b == 0 and number != 0:
        print("Число делиться на 3")
    else:
        print("Число не делиться на 3")

def p2():
    try:
        number = int(input("Введите число:"))
        b = 100 / number
    except ValueError:
        print("Пользователь ввёл не число")
    except ZeroDivisionError:
        print("Введено число 0")
    else:
        print("Деление числа 100 на введённное число", b)

def p3():
    y = input("Введите дату: ")
    y = y.split('.')
    if int(y[0]) * int(y[1]) == int(y[2][2:4]):
        print("Магическая дата")
    else:
        print("Не магическая дата")

def p4():
    a = input("Введите число: ")
    b = 0
    d = 0
    if len(a) % 2 == 0:
        for j in a[0:int(len(a) / 2)]:
            b = b + int(j)
        for j in a[int(len(a) / 2):int(len(a))+1]:
            d = d + int(j)
        if d == b:
            print("Это счастливый билет")
        else:
            print("Это не счастливый билет")
    else:
        print("Введено нечётное кол-во цифр")

p1(),p2(),p3(),p4()
