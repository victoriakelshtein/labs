a = input()
b = input()
if a == b:
    print("пароль совпадает")
else:
    print("пароль не совпадает")
    
n = int(input("введите номер вашего места"))
print()
if n > 36:
    print("ваше место боковое")
elif n % 2:
    print("ваше место в купе снизу")
else:
    print("ваше место в купе сверху")

a, b = input(), input()
if a != 'красный' and a != 'жёлтный' and a != 'синий':
    print("ошибка цвета")
elif b != 'красный' and b != 'жёлтный' and b != 'синий':
    print("ошибка цвета")
elif a == 'красный' and b == 'синий' or a == 'синий' and b == 'красный':
    print("фиолетовый")
elif a == 'красный' and b == 'жёлтый' or a == 'жёлтый' and b == 'красный':
    print("оранжевый")
elif a == 'синий' and b == 'жёлтый' or a == 'синий' and b == 'красный':
    print("зелёный")
elif a == 'красный' and b == 'красный':
    print("красный")
elif a == 'синий' and b == 'синий':
    print("синий")
elif a == 'жёлтый'and b == 'жёлтый':
    print("жёлтый")
    
year = int(input("введите год"))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, "да это високосный год")
else:
    print("нет это невисокосный год")
