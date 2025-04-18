from restaurant import Restaurant as R
from user import User
from admin import Admin
from random import randint
from random import choice

#9.1 �������� ������ � ������������� �������
print('#9.1')

# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.name = restaurant_name
#         self.type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):
#         print(f'{self.name.title()} has {self.type} cuisine')

#     def open_restaurant(self):
#         print('The restaurant is open!')
    
#     def set_number_served(self,served):
#         self.number_served = served
#         print(f'Served clients: {self.number_served}')
    
#     def increment_number_served(self,plus_to_number_served):
#         self.number_served += plus_to_number_served
#         print(f'Served clients are grown now: {self.number_served}')

# restaurant = Restaurant('euroasia','asian')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

#9.2 �������� ������ � ������������� �������
print('\n#9.2')

# restaurant_0 = Restaurant('euroasia','asian')
# restaurant_0.describe_restaurant()

# restaurant_1 = Restaurant('tokio city','asian')
# restaurant_1.describe_restaurant()

# restaurant_2 = Restaurant('vostok','russian')
# restaurant_2.describe_restaurant

#9.3 �������� ������ � ������������� �������
print('\n#9.3')

# class User:
#     def __init__(self,first_name,last_name,location,nickname):
#         self.first = first_name
#         self.last = last_name
#         self.location = location
#         self.nickname = nickname
#         self.login_attempts = 0

#     def describe_user(self):
#         print(f"\n{self.first.title()} {self.last.title()}'s nickname is {self.nickname}")
#         print(f"His location is {self.location.title()}")

#     def greet_user(self):
#         print(f"Hello, {self.nickname}!")

#     def increment_login_attempts(self):
#         self.login_attempts += 1
#         return self.login_attempts

#     def reset_login_attempts(self):
#         self.login_attempts = 0
#         print(f'Login attempts reset: {self.login_attempts}')


# user_0 = User('alex','gafarov','spb','kodiword')
# user_0.describe_user()
# user_0.greet_user()

# user_1 = User('zlata','gafarova','spb','zlatik228')
# user_1.describe_user()
# user_1.greet_user()

# user_2 = User('kirill','zooravlev','ufa','sprint')
# user_2.describe_user()
# user_2.greet_user()

#9.4 ��������� ������  Restaurant � ���������� ����� ������� � ���������� ���������
print('\n#9.4')

# my_restaurant = Restaurant('euroasia','asian')
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()
# my_restaurant.number_served = 100
# print(my_restaurant.number_served)

# my_restaurant.set_number_served(500)

# my_restaurant.increment_number_served(30)

#9.5 ��������� ������ User � ���������� ����� ������� � ���������� ���������
print('\n#9.5')

# user_0 = User('alex','gafarov','spb','kodiword')
# user_0.describe_user()
# user_0.greet_user()
# attempts = user_0.increment_login_attempts()
# attempts = user_0.increment_login_attempts()
# attempts = user_0.increment_login_attempts()
# print(f'Login attempts now: {attempts}')
# user_0.reset_login_attempts()

#9.6 ������������ ������
print('\n#9.6')

# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavors = ['vanila', 'stawberry','wildberry']

#     def describe_flavors(self):
#         print(f'We have this flavors: ')
#         for flavor in self.flavors:
#             print(f'\t{flavor.title()}')


# my_ice_cream = IceCreamStand('ice cream for everyone','russian')
# my_ice_cream.describe_flavors()

#9.7 ������������ ������
print('\n#9.7')

# class Privileges:
#     def __init__(self):
#         self.list_privileges = ['allow to add message', 'allow to del users', 'allow to ban users']

#     def show_privileges(self):
#         print(f"There are some admin's privileges: ")
#         for privilege in self.list_privileges:
#             print(f'\t{privilege.title()}')


# class Admin(User):
#     def __init__(self,first_name,last_name,location,nickname):
#         super().__init__(first_name,last_name,location,nickname)
#         self.privileges = Privileges()


# admin = Admin('radmir', 'razyapov', 'moscow', 'chempik')

# admin.describe_user()
# admin.greet_user()
# admin.show_privileges()

#9.8 ��������� ��� �����
print('\n#9.8')

# admin_1 = Admin('nikita', 'kird', 'sterlitamak', 'lil kird')
# admin_1.describe_user()
# admin_1.greet_user()
# admin_1.privileges.show_privileges()

#9.10 создание и импортирование модуля restaurant 
print('\n#9.10')

my_restaurant = R("sasha's relax", "russian")
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(5)

#9.11 и 9.12 создание и импортирование модуля user и admin
print('\n#9.11')

admin = Admin('nikita', 'kird', 'sterlitamak', 'lil kird')
admin.privileges.show_privileges()
admin.describe_user()

#9.13 импортирование модуля random с методом randint, который создает рандомное число
print('\n#9.13')

class Die:
    '''создает кубик со стороной sides для броска'''
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        '''бросает кубик'''
        print(f'Came up: {randint(1,self.sides)}')

dice_6 = Die() #create dice with 6 sides
count = 1
print(f'\nDice = 6')
while count <= 10:
    dice_6.roll_die()
    count += 1

dice_10 = Die(10) #create dice with 10 sides
count = 1
print(f'\nDice = 10')
while count <= 10:
    dice_10.roll_die()
    count += 1

dice_20 = Die(20) #create dice with 20 sides
count = 1
print(f'\nDice = 20')
while count <= 10:
    dice_20.roll_die()
    count += 1

#9.14 импортирование модуля random с методом choice, который выбрает рандомный аргумент в списке
print('\n#9.14')

lotery = [1, 5, 12, 46, 234, 20, 123,2435, 1, 3, 'f', 'q', 't', 'p', 'z']
win_position = []

for a in range(4):  #choise a random arg from lotery and add to win_position
    position = choice(lotery)
    win_position.append(position)

print(f'Here is win position of lotery {win_position}')

#9.15 импортирование модуля random с методом choice, который выбрает рандомный аргумент в списке
print('\n#9.14')

my_ticket = [1, 'q', 234, 'p', 123, 2435, 1, 3, 12, 't', 20, 'z']
win_position = []

i = 0
time = 0
while i < 12: # choise a random arg from lotery and check with my_ticket
    time += 1
    position = choice(lotery)
    if position == my_ticket[i]:
        win_position.append(position)
        i += 1
    else:
        continue

print(win_position)
print(f'Time: {time}')