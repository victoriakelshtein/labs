def p81():
    from PIL import Image
    img=Image.open("cat.jpeg")
    box = (40, 50, 400, 400)
    new_img = img.crop(box)
    new_img.save("cat_2.jpeg")
    new_img.show()

def p82():
    from PIL import Image
    slovar= {
        "новый год" : "newyear.jpg",
        "8 марта" : "8marta-6(1).jpg"
    }
    days = input("Введите название праздника -")
    if days in slovar:
        file = slovar[days]
        img = Image.open(file)
        img.show()
    else:
        print("По вашему запросу нет открыток")

def p83():
    from PIL import Image,ImageDraw,ImageFont
    img=Image.open("cat.jpeg")
    draw=ImageDraw.Draw(img)
    k=input("введите имя поздравляемого - ")
    font=ImageFont.truetype("arial.ttf", size=100)
    text_width,text_height=draw.textsize("Hellow world!",font=font)
    x=(img.width-text_width) //2
    y=(img.height-text_height)//5
    draw.text((x,y), k, font=font,fill=(150,255,255))
    img.save("holidays.jpg")
    img.show()
p83()
