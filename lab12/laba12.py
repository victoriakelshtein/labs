def p121():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')


    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors

        def ice_flavors(self):
            print('Вкусы мороженого:')
            print(*self.flavors, sep='\n')


    a = IceCreamStand('Мороженое', 'Кафе', ['Кокос', 'Киви', 'Банан', 'Клубника'])
    a.ice_flavors()

def p122():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

    class IceCreamStand(Restaurant):
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time):
            super().__init__(restaurant_name, cuisine_type)
            self.flavors = flavors
            self.place = loc
            self.time = time

        def ice_flavors(self):
            print('Виды мороженного: ')
            print(*self.flavors, sep='\n')

        def newflavor(self):
            self.flavors.append(input('Введите новый сорт мороженного:'))

        def delflavor(self):
            self.flavors.remove(input('Введите сорт, который хотите удалить:'))

        def poisk(self):
            if input('Введите какой вкус хотите найти:') in self.flavors:
                print('В наличии')
            else:
                print('Нет в наличии')

    class napalochke(IceCreamStand):
        def __init__(self, restaurant_name, cuisine_type, flavors, loc, time, material):
            super().__init__(restaurant_name, cuisine_type, flavors, loc, time)
            self.material = material

        def palka(self):
            print('Материал палочки:', self.material)

    a = IceCreamStand('Мороженное', 'Кафе', ['Кокос', 'Киви', 'Банан', 'Клубника'], 'ул. Шоссе в лаврики', '9:00-20:00')
    a.describe_restaurant()
    a.newflavor()
    a.ice_flavors()
    a.delflavor()
    a.ice_flavors()
    a.poisk()

    b = napalochke('Мороженное', 'Кафе', ['Кокос', 'Киви', 'Банан', 'Клубника'], 'ул. Белоостровская', '8:00-18:00', 'дерево')
    b.palka()

import tkinter as tk
def p123():
    class IceCreamStand:
        def __init__(self):
            self.names = ['Инмарко', '48 копеек', 'Ленинградское', 'Волшебный фонарь', 'Арбузная долька', 'Румба']
            self.types = ['Эскимо', 'Стаканчик', 'Эскимо', 'Брикет', 'Пломбир', 'Лёд']

        def get_names(self):
            return self.names

        def get_types(self):
            return self.types

    class IceCreamStandGUI:
        def __init__(self, master):
            self.master = master
            master.title('IceCream')

            self.ice_cream_stand = IceCreamStand()
            self.names_label = tk.Label(master, text='Название', font='Calibri 12 italic bold')
            self.names_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_names()))

            for name in self.ice_cream_stand.get_names():
                self.names_listbox.insert(tk.END, name)

            self.types_label = tk.Label(master, text='Вид', font='Calibri 12 italic bold')
            self.types_listbox = tk.Listbox(master, font='Calibri 12', height=len(self.ice_cream_stand.get_types()))

            for type in self.ice_cream_stand.get_types():
                self.types_listbox.insert(tk.END, type)

            self.names_label.grid(row=0, column=0)
            self.names_listbox.grid(row=1, column=0)
            self.types_label.grid(row=0, column=1)
            self.types_listbox.grid(row=1, column=1)

    root = tk.Tk()
    a = IceCreamStandGUI(root)
    root.mainloop()

p123()