def p1():
    import random
    b = int(input("Введите число: "))
    d = [random.randint(1,10)for i in range(5)]
    if b in d:
        print(("Поздравляю,вы угадали число!"))
    else:
        print("Нет такого числа!")

def p2():
    b = []
    a = [1, 2, 4, 6, 5, 4, 1, 7, 2,8]
    for i in a:
        if a.count(i) > 1:
            b.append(i)
    print(*b)

def p3():
    a = int(input("Введите сколько вы хотите выходных на неделе: "))
    d = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")
    for j in d:
        print("Ваши выходные дни: ", *d[-a:])
        print("Ваши рабочие дни: ", *d[:-a])
        break

def p4():
    import random
    md5 = ["Яриз", "Соболева", "Зимина", "Пархомец", "Кельштейн", "Кашицына", "Марченко", "Скрипилова", "Капустинский", "Заяц"]
    md8 = ["Степанова", "Иванов", "Сальников", "Данилов", "Мешков", "Маскалёв", "Запарожец", "Гридасова", "Иванов", "Семенченко"]
    a1 = []
    a2 = []
    a = []
    a1.append(random.sample(md5, 5))
    a2.append(random.sample(md8, 5))
    a.extend(*a1)
    a.extend(*a2)
    a = tuple(a)
    print("Исходный список: ", *md5)
    print("Исходный список: ", *md8)
    print('a', *a)
    print('b', len(a))
    print('d', *sorted(a))
    print('e', 'Иванов' in a)
    print('e', a.count('Иванов)'))

p1(), p2(), p3(), p4()
