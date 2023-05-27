def p111():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

    newrestaurant = restaurant('Название: Кавказ', 'Тип кухни: Кавказская кухня')
    print(newrestaurant.restaurant_name)
    print(newrestaurant.cuisine_type)
    newrestaurant.describe_restaurant()
    newrestaurant.open_restaurant()

def p112():
    class rest:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

    restaurant1 = rest('Италия', 'Итальянская кухня')
    restaurant1.describe_restaurant()
    restaurant2 = rest('Карл и Фридрих', 'Немецкая кухня')
    restaurant2.describe_restaurant()
    restaurant3 = rest('Евразия', 'Европейская кухня')
    restaurant3.describe_restaurant()

def p113():
    class rest:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print(f'{self.restaurant_name} - {self.cuisine_type}')
            print(f'Рейтинг ресторана: {self.rating}')

        def open_restaurant(self):
            print(f'{self.restaurant_name}, Ресторан открыт!')

        def rating_set(self, new_rating):
            self.rating = new_rating

        def raiting(self):
            print(f'Новый рейтинг:{self.rating}')

    newrest = rest('Евразия', 'Европейская кухня', 4)
    newrest.describe_restaurant()
    newrest.rating_set(input('Введите новый рейтинг:'))
    newrest.raiting()

p113()