from shutil import get_unpack_formats

#3.1 создание списка
names = ['Andrey','Alex','Zlata']

print(names[0])
print(names[1])
print(names[2]) 

#3.2 вывод списка с сообщением
message = 'my friend is'

print(f'\n{message.title()} {names[0]}')
print(f'{message.title()} {names[1]}')
print(f'{message.title()} {names[2]}') 

#3.3 вывод списка с сообщением
cars = ['gelly','porshe','bmw']
message = 'I would like to buy'

print(f'\n{message} {cars[0].title()}')
print(f'{message} {cars[1].title()}')
print(f'{message} {cars[2].upper()}') 

#3.4 создание списка
guests = ['zlata','radmir','kirill'] 
invitation_message = 'I would like to invite you on lunch'

print(f'\n{invitation_message}, {guests[0].title()}')
print(f'{invitation_message}, {guests[1].title()}')
print(f'{invitation_message}, {guests[2].title()}')  

#3.5 замена значения из списка
print(guests[0]) 

guests[0] = 'nikita'

print(f'\n{invitation_message}, {guests[0].title()}')
print(f'{invitation_message}, {guests[1].title()}')
print(f'{invitation_message}, {guests[2].title()}') 

#3.6 расширение списка .insert и .append
print('Guest list expanded')

guests.insert(0,'darina')
guests.insert(2,'pasha')
guests.append('senya')

print(f'\n{invitation_message}, {guests[0].title()}')
print(f'{invitation_message}, {guests[1].title()}')
print(f'{invitation_message}, {guests[2].title()}') 
print(f'{invitation_message}, {guests[3].title()}')
print(f'{invitation_message}, {guests[4].title()}')
print(f'{invitation_message}, {guests[5].title()}') 

#3.7 удаление элементов списка del .pop
print('\nSorry, I can invite only 2 people')

guest1 = guests.pop(0)
print(f"Sorry, I can invite only 2 people,{guest1.title()}")

guest1 = guests.pop(0)
print(f"Sorry, I can invite only 2 people,{guest1.title()}")

guest1 = guests.pop(0)
print(f"Sorry, I can invite only 2 people,{guest1.title()}")

guest1 = guests.pop()
print(f"Sorry, I can invite only 2 people,{guest1.title()}")

print(f'My offer still stands, {guests[0].title()}')
print(f'My offer still stands, {guests[1].title()}')

del guests[0]
del guests[0]
print(guests)

#3.8 сортировка списка sorted()(.sort(reverse = True) - постоянный) .reverse (.reverse и .sort не работают в f-строках)
countries = ['Egypt','Belarus','UK','USA','Russia']
print(f'\n{countries}')

print(sorted(countries))
print(countries)
print(sorted(countries,reverse = True))
print(countries)
countries.reverse()
print(f'Change the orger: {countries}')
countries.reverse()
print(f'Again change:{countries}')
countries.sort()
print(f'Change the orger forever:{countries}')
countries.sort(reverse = True)
print(f'Change the order back forever:{countries}')

#3.9 длина списка 
print(f'The lengt of guests: {len(guests)}')