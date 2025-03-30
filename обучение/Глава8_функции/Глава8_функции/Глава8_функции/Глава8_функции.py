#8.1 создание и вывод функции
print('\n#8.1')

def display_message(message):
    print(message)

message = '8.1 is about functions!'
display_message(message)

#8.2 передача параметра функции
print('\n#8.2')

def favorite_book(title):
    print(f'One of my favorite book is {title.title()}')

title = input('What is you favorite book? ')
favorite_book(title)