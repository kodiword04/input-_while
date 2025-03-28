# #7.1 input()
# print('#7.1\n')
# car = input('What car do you want to take: ')
# print(f'Let me see if I can find you a {car.title()}')

# #7.2 input() � int()
# print('\n#7.2')

# num_of_seats = input('How many seats do you need?\n')

# if int(num_of_seats) >= 8:
#     print('Sorry but you need to wait a few hours')
# else:
#     print('You are welcome!')

# #7.3 input() � int()
# print('\n#7.3')
# number = input('Tell me a number and I tell you is it multiply 10 or not\n')
# if int(number) % 10 == 0:
#     print(f'\t{number} is multiply 10: ')
# else:
#     print(f'\t{number} is not multiply 10')

# #7.4 while
# print('\n#7.4')
# message = '\nHello! Please enter topping for your pizza.\nIf you are done, enter "quit": '

# active = True
# while active:
#     topping = input(message)

#     if topping == 'quit':
#         active = False
#     else:
#         print(f'Added: {topping}')

# #7.5 while()
# print('\n#7.5')
# message = '\nTell your age and I tell you a ticket cost.\nIf you are done, enter "quit": '

# active = True
# while active:
#     age = input(message)
#     if age == 'quit':
#         active = False
#     else:
#         if int(age) < 3:
#             print('Ticket cost 0')
#         elif int(age) < 12:
#             print('Ticket cost is 10 dollars')
#         else:
#             print('Ticket cost is 15 dollars')

# #7.7 бесконечный цикл для проверки
# print('\n#7.7')
# x = 1
# while x<5:
#     print('ya lox')

# #7.8 добавление элементов списка в другой список с помощью while
# print('\n#7.8')
# sandwiches_orders = ['cheeseburger','vopper', 'grandcheese', 'angus burger']
# finished_sandwiches = []

# while sandwiches_orders:
#     sandwich = sandwiches_orders.pop()
#     print(f'{sandwich.title()} is done! ')
#     finished_sandwiches.append(sandwich)

# print(f'\nOrders are done: ')
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich.title())

#7.9 удаление повторяющихся элементов списка с помощью while
print('\n#7.9')
sandwiches_orders = ['cheeseburger','pastrami',
                     'vopper','pastrami',
                    'grandcheese','angus burger',
                    'pastrami']

for sandwich_orders in sandwiches_orders:
    print(sandwich_orders)

print('\nPastrami is over now!')

while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')

print('')
for sandwich_orders in sandwiches_orders:
    print(sandwich_orders)