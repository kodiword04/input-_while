#8.1 �������� � ����� �������
print('\n#8.1')

def display_message(message):
    print(message)

message = '8.1 is about functions!'
display_message(message)

#8.2 �������� ��������� �������
print('\n#8.2')

def favorite_book(title):
    print(f'One of my favorite book is {title.title()}')

title ='harry potter'
favorite_book(title)

#8.3 позиционные аргументы и именованные 
print('\n#8.3')

def make_shirt1(size, text):
    print(f'Size:{size}\nText: {text}')

def make_shirt2(size, text):
    print(f'Size:{size}\nText: {text}')

make_shirt1('3','I love animmals')
make_shirt2(size = '4', text = 'I am Sasha')

#8.4 аргументы по умолчанию 
print('\n#8.4')

def make_shirt(size = 'L', text = 'I love Python'):
    print(f'Size:{size}\nText: {text}')

make_shirt()
make_shirt('4',text = 'I love C++')

#8.5 все типы вызовов аргументов
print('\n#8.5')

def describe_city(city, country = 'russia'):
    print(f'{city.title()} is {country.title()}')

describe_city('spb')
describe_city('new york', country = 'america')
describe_city('paris', 'france')

#8.6 возвращение значения в функции
print('\n#8.6')

def city_country(city,country):
    full_location = f'{city.title()},{country.title()}'
    return full_location

location = city_country('spb', 'russia')
print(location)
location = city_country('new york', 'america')
print(location)
location = city_country('paris', 'france')
print(location)

#8.7 создание словаря в функции
print('\n#8.7')

def musician_album(name_author, name_song, date_published = None):
    album = {'author': name_author, 'song': name_song}
    if date_published:
        album['published'] = date_published
    return album

album = musician_album('choy','star which name is sun')
print(album)
album = musician_album('poshlay_molly','non-stop')
print(album)
album = musician_album('mumi troll','vladivostok 2000')
print(album)
album = musician_album('instasamka','titanic', date_published = 2024)
print(album)

# #8.8 работа с while и функцией
# print('\n#8.8')
# name_author = ''

# while True:
#     print('\nTell me author and song, please.\nIf you want to stop enter: "q"')
#     name_author = input('Author: ')
#     if name_author != 'q':
#         name_song = input('Song: ')
#         print(musician_album(name_author, name_song))
#     else:
#         break

#8.9 список в функции 
print(f'\n#8.9')

def show_messages(messages):
    for message in messages:
        print('\t' + message)

messages = ['I am Sasha', 'I study in Politech', 'My wife is Zlata']

show_messages(messages)

# #8.10 изменение элементов списка через функцию
# print(f'\n#8.10')

# def send_messages(messages, sent_messages):
#     while messages:
#         sent_message = messages.pop(0)
#         print(f'Sent: {sent_message}')
#         sent_messages.append(sent_message)

# sent_messages = []

# send_messages(messages, sent_messages)

# print(messages)
# print(sent_messages)

#8.11 запрет на изменение элементов списка через функцию
print(f'\n#8.11')

def send_messages(messages, sent_messages):
    while messages:
        sent_message = messages.pop(0)
        print(f'Sent: {sent_message}')
        sent_messages.append(sent_message)

sent_messages = []

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)

#8.12 передача любого кол-ва информации в функцию(список)
print(f'\n#8.12')

def make_sandwiches(*components):
    print('Make sandwich with: ')
    for component in components:
        print('\t' + component)

make_sandwiches('cheese','bread','meat')
make_sandwiches('spicy')
make_sandwiches('ketchap','milk')

#8.12 передача любого кол-ва информации в функцию(словарь)
print(f'\n#8.12')

def build_profile(first, last, **facts):
    facts['first_name'] = first
    facts['last_name'] = last
    return facts

user_profile = build_profile('sasha','gafarov',location = 'spb', university = 'politech', wife = 'zlata')

print(user_profile)