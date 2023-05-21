def p71():
    from PIL import Image
    img = Image.open('uiu.jpeg')
    img.show()
    print(img.format, img.size, img.mode)

def p72():
    from PIL import Image
    img = Image.open('uiu.jpeg')
    new_img = (1642, 1088)
    new_img_u = img.resize(new_img)
    new_img_u.save('iui.jpg')
    new_img_second = img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img_second.save('iuii.jpg')
    new_img_tree = img.transpose(Image.FLIP_TOP_BOTTOM)
    new_img_tree.save('iii.jpg')

def p73():
    from PIL import Image, ImageFilter
    img1 = Image.open('sus1.jpg')
    img2 = Image.open('sus2.jpg')
    img3 = Image.open('sus3.jpg')
    img4 = Image.open('sus4.jpg')
    img5 = Image.open('sus5.jpg')
    e1 = img1.filter(ImageFilter.FIND_EDGES)
    e2 = img2.filter(ImageFilter.FIND_EDGES)
    e3 = img3.filter(ImageFilter.FIND_EDGES)
    e4 = img4.filter(ImageFilter.FIND_EDGES)
    e5 = img5.filter(ImageFilter.FIND_EDGES)
    e1.save('sus_1.jpg')
    e1.show()
    e2.save('sus_2.jpg')
    e2.show()
    e3.save('sus_3.jpg')
    e3.show()
    e4.save('sus_4.jpg')
    e4.show()
    e5.save('sus_5.jpg')
    e5.show()

def p74():
    from PIL import Image

    img_path = 'sus1.jpg'
    watermark_path = 'water2.png'
    img = Image.open(img_path).convert('RGB')
    watermark = Image.open(watermark_path).convert('RGBA')
    watermark = watermark.resize((1200, 900))
    img.paste(watermark, (1, 10), watermark)
    img.save('LABA_7.1.2.jpg')
    img.show()
p72()
