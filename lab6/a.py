def p1():
    strana = {
        "russia": "moscow",
        "germany": "berlin",
        "norway": "oslo",
        "finland": "helsinki"
    }
    l = input("Введите страну: ")
    print("a", strana)
    print("b", strana[l])
    print("c", sorted(strana))

def p2():
    ochki = {}
    ochki['А'] = ochki['В'] = ochki['Е'] = ochki['И'] = ochki['Н'] = ochki['О'] = ochki['Р'] = ochki['С'] = ochki['Т'] = 1
    ochki['Д'] = ochki['К'] = ochki['Л'] = ochki['М'] = ochki['П'] = ochki['У'] = 2
    ochki['Б'] = ochki['Г'] = ochki['Ё'] = ochki['Ь'] = ochki['Я'] = 3
    ochki['Й'] = ochki['Ы'] = 4
    ochki['Ж'] = ochki['З'] = ochki['Ч'] = ochki['Ц'] = ochki['Х'] = 5
    ochki['Ш'] = ochki['Э'] = ochki['Ю'] = 8
    ochki['Ф'] = ochki['Щ'] = ochki['Ъ'] = 10
    a = input("Введите слово: ")
    b = 0
    for i in a:
        i = i.upper()
        b += ochki[i]
    print(b)

def p3():
    student={}
    student["Максим"] = ["Китайский", "Русский"]
    student["Дима"] = ["Английский"]
    a = set()
    b = set()
    for key, value in student.items():
        for j in value:
            a.add(j)
            if j == 'Китайский':
                b.add(key)
    print(*a)
    print(*b)

p1(), p2(), p3()
