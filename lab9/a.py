def p91():
    import os
    from PIL import Image, ImageFilter
    spisok = ["butterfly1.jpg", "butterfly2.jpg", "butterfly3.jpg", "butterfly4.jpg", "butterfly5.jpg"]
    new_folder = "LABA_9"
    os.makedirs(new_folder, exist_ok=True)
    for i in spisok:
        img = Image.open(i)
        img = img.filter(ImageFilter.CONTOUR)
        saving = os.path.join(new_folder, "new" + i)
        img.save(saving)

def p92():
    import os
    from PIL import Image, ImageFilter
    spisok = ["butterfly1.jpg", "butterfly2.jpg", "butterfly3.jpg", "butterfly4.jpg", "butterfly5.jpg"]
    new_folder = "LABA_9"
    os.makedirs(new_folder, exist_ok=True)
    for i in spisok:
        if i.endswith('.jpg'):
            img = Image.open(i)
            img = img.filter(ImageFilter.CONTOUR)
            saving = os.path.join(new_folder, "new" + i)
            img.save(saving)

def p93():
    import csv
    a = 0
    print("Нужно купить: ")
    with open('laba9.csv', encoding= 'utf-8') as file:
        file = csv.reader(file)
        for i in file:
            name = i[0]
            kolichestvo = int(i[1])
            cena = int(i[2])
            a += kolichestvo*cena
            print(name, '-', kolichestvo, ' шт. за', cena, 'руб.')
    print("Итоговая сумма: ", a)

p93()
