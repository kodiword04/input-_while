
#4.1 ���� for ��� �������
from ast import Num


pizzas = ['peperoni','4_cheeses','margaritta']
for pizza in pizzas:
    print(f'I like {pizza.title()} pizza')

print(f'I really like pizza!\n')

#4.2 ���� for ��� ������� 
animals = ['dog','cat','mouse','rabbit','panda']
for animal in animals:
    print(f'A {animal} would be a good friend')

print(f'Any of these animals would be a nice friend!')

#4.3 range()
numbers = list(range(1,21))
for number in numbers:
    print(number)

#4.4 for in range()
#numbers = list(range(1,1000001))
#for number in numbers:
    #print(number)

#4.5 max() min() sum()
numbers = list(range(1,1000001))
print(f'\n{min(numbers)}')
print(f'{max(numbers)}')
print(f'{sum(numbers)}\n')

#4.6 �������� �����
odd_numbers = list(range(1,21,2))
for odd in odd_numbers:
    print(odd)
print('\n')

#4.7 ����� ������� 3
numbers = list(range(0,31,3))
for number in numbers:
    print(number)
print('\n')

#4.8 ���� �� 1 �� 10
cubes = []
for cube in range(1,11):
    print(cube**3)

#4.9 ��������� �����
cubes = [cube**3 for cube in range(1,11)]
print(f'\n{cubes}')

#4.9 ����� ���������
print(f'\nThe irst three items in the list are:{animals[:3]}')
print(f'The irst three items in the list are:{animals[1:4]}')
print(f'The irst three items in the list are:{animals[-3:]}\n')

#4.10 ����������� ������
friend_pizzas = pizzas[:]
pizzas.append('with pineapple')
friend_pizzas.append('parmezano')

print(f'My favorite pizzas are:{pizzas}')
print(f"Friend's favorite pizzas are:{friend_pizzas}\n")

#4.11 ����� ������� ����� for
for pizza in pizzas:
    print(pizza)
for friend_pizza in friend_pizzas:
    print(friend_pizza)
print(f'My favorite pizzas are:{pizzas}')
print(f"Friend's favorite pizzas are:{friend_pizzas}\n")

#4.12 ������ � ��������� 
menu = ('bread','salad','pizza','soup','pasta')
for position in menu:
    print(position)
menu = ('salad1','salad2','salad3','pizza','bread')
for position in menu:
    print(position)