#6.1 вывод всех значений словаря
person_o = {'first_name':'sasha','last_name':'gafarov','age':20,'city':'spb'}

print(person_o['first_name'])
print(person_o['last_name'])
print(person_o['age'])
print(person_o['city'])

#6.2 работа со словарем
numbers_o = {
    'zlata': 1441,
    'kirill': 523,
    'sasha': 20,
    'radmir': 31,
    'nikita': 5,
    }

print(f"\nZlata's favorite numer is {numbers_o['zlata']}")
print(f"Kirill's favorite numer is {numbers_o['kirill']}")
print(f"Radmir's favorite numer is {numbers_o['radmir']}")
print(f"Sasha's favorite numer is {numbers_o['sasha']}")
print(f"Nikita's favorite numer is {numbers_o['nikita']}")

#6.3 работа со словарем
glossary_o = {
    'list':'collect some piece',
    'dictionary':'collect two piece in one order',
    'piece':'int or str',
    'cycle': 'check every piece in some list',
    'comment':'explain something in programm',
    }
print(f'\nList can {glossary_o["list"]}')
print(f'Dictionary can {glossary_o["dictionary"]}')
print(f'Piece is {glossary_o["piece"]}')
print(f'Cycle can {glossary_o["cycle"]}')
print(f'Comment can {glossary_o["comment"]}\n')

#6.4 улучшенная 6.3 циклом for
for termin, meaning in glossary_o.items():
    if termin != 'piece':
        print(f'{termin.title()} can {meaning}')
    else:
        print(f'{termin.title()} is {meaning}')

#6.5 вывод каждого ключа и значения
rivers_o = {
    'nile':'egypt',
    'volga':'russia',
    'temza':'london'
    }
print('')
for river, country in rivers_o.items():
    print(f'The {river.title()} runs through {country.title()}')
print('')
for river in rivers_o.keys():
    print(f'River: {river.title()}')
print('')
for country in rivers_o.values():
    print(f'Country: {country.title()}')

#6.6 set() - создает множество, его можно сравнивать с значением\ключом, чтобы не было повторов
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

names_for_poll = ['phil','jen','kirill','valera','edward']
print('')
for name in names_for_poll:
    if name in set(favorite_languages.keys()):
        print(f'Thank you for taking the poll,{name.title()}')
    else:
        print(f'Do you want to take the poll, {name.title()}?')

#6.7 словари в списке
person_0 = {'first_name':'sasha','last_name':'gafarov','age':20,'city':'spb'}
person_1 = {'first_name':'zlata','last_name':'gafarova','age':20,'city':'spb'}
person_2 = {'first_name':'kirill','last_name':'zooravlev','age':21,'city':'ufa'}

persons = (person_0, person_1, person_2)
print('')
for person in persons:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()}:\n\t{person['age']}\n\t{person['city']}")

#6.8 словари в списке
berta = {'species':'dog','host':'mom'}
luna = {'species':'cat','host':'me'}
motia = {'species':'cat','host':'mom'}

pets = (berta, luna, motia)
print('')
for pet in pets:
    print(f"{pet['host'].title()} has a {pet['species']}")

#6.9 списки в словаре
favorite_places = {
    'sasha': ['university','cinema'],
    'zlata': ['university','gym','cinema'],
    'nikita': ['cinema','bar','gym'],
    }
print('')
for name, places in favorite_places.items():
    print(f"{name.title()} like to visit: ")
    for place in places:
        print(f"\t{place}")

#6.10 списки в словаре
numbers_0 = {
    'zlata': [1231,1441,12312,523],
    'kirill': [523,1241,54,2345,423],
    'sasha': [20,1234,623,235],
    'radmir': [31,1,57],
    'nikita': [5],
    }
print('')
for name, numbers in numbers_0.items():
    if len(numbers) > 1:
        print(f"{name.title()} most liked numbers are ")
    else:
        print(f"{name.title()} most liked number is ")
    for number in numbers:
        print(f"\t{number}")

#6.11 словарь в словаре
cities = {
    'spb': {
        'population': '6 million',
        'country': 'russia',
        'fact': 'founded by Peter the Great'
        },
    'london': {
        'population': '10 million',
        'country': 'uk',
        'fact': 'people there like to drink tea with milk'
        },
    'new york': {
        'population': '18 million',
        'country': 'america',
        'fact': 'very rich city'
        }
    }
print('')
for city,facts in cities.items():
    print(f'\nFacts about {city.title()}:')
    for fact, info in facts.items():
        print(f'\t{fact.title()}:')
        print(f'\t\t{info.title()}')