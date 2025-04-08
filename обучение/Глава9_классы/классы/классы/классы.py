#9.1 создание класса и использование методов
from pydoc import describe


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
restaurant_2.describe_restaurant

#9.3 создание класса и использование методов
print('\n#9.3')

class User:
    def __init__(self,first_name,last_name,location,nickname):
        self.first = first_name
        self.last = last_name
        self.location = location
        self.nickname = nickname

    def describe_user(self):
        print(f"\n{self.first.title()} {self.last.title()}'s nickname is {self.nickname}")
        print(f"His location is {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.nickname}!")


user_0 = User('alex','gafarov','spb','kodiword')
user_0.describe_user()
user_0.greet_user()

user_1 = User('zlata','gafarova','spb','zlatik228')
user_1.describe_user()
user_1.greet_user()

user_2 = User('kirill','zooravlev','ufa','sprint')
user_2.describe_user()
user_2.greet_user()