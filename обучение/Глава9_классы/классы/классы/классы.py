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

#9.2 создание класса и использование методов
print('\n#9.2')

restaurant_0 = Restaurant('euroasia','asian')
restaurant_0.describe_restaurant()

restaurant_1 = Restaurant('tokio city','asian')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('vostok','russian')
restaurant_2.describe_restaurant()