def p101():
    import json
    with open('json', 'r', encoding='utf-8') as fl:
        a = json.load(fl)
    for i in a['products']:
        print('Название:', i['name'])
        print('Цена:', i['price'])
        print('Вес: ', i['weight'])
        if i['available']:
            print('В наличии')
        else:
            print('Нет в наличии')

def p102():
    import json
    with open('json', 'r', encoding='utf-8') as fl:
        a = json.load(fl)
    for i in a['products']:
        print('Название:', i['name'])
        print('Цена:', i['price'])
        print('Вес: ', i['weight'])
        if i['available']:
            print('В наличии')
        else:
            print('Нет в наличии')
    name = input('Введите название:')
    price = input('Введите цену:')
    weight = input('Введите вес:')
    available = input(str('В наличии, введите да или нет:'))
    print('Название:', name)
    print('Цена:', price)
    print('Вес: ', weight)
    print('В наличие или нет: ', available)

def p103():
    a = {}
    with open('en.txt', encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            fdata = line.split('-')
            fdata[0] = fdata[0].lstrip().rstrip()
            for j in fdata[1].split(','):
                j = j.lstrip().rstrip()
                if j not in a:
                    a[j] = [fdata[0]]
                else:
                    a[j].append(fdata[0])
    sd = dict(sorted(a.items()))
    with open('ru-en.txt', 'w', encoding='utf-8') as f:
        for key, value in sd.items():
            f.write(key + ' - ' + ', '.join(value) + '\n')
            print(key +'-'+','.join(value))
