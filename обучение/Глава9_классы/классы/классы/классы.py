#9.1 создание класса и использование методов
print('#9.1')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.name.title()} has {self.type} cuisine')

    def open_restaurant(self):
        print('The restaurant is open!')

restaurant = Restaurant('euroasia','asian')
restaurant.describe_restaurant()
restaurant.open_restaurant()