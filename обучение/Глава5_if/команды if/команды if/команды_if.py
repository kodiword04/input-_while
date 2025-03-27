
#5.3 проверка if 
from hmac import new


print('#5.3')
alien_color = 'green'

if alien_color == 'yellow':
    print('You take 5 points!')
if alien_color == 'green':
    print('You took all points!')

#5.4 проверка if-else
print('\n#5.4')
alien_color1 = 'red'

if alien_color1 == 'green':
    print('You take 5 points!')
else:
    print('You take 10 points!')

if alien_color1 == 'red':
    print('You take 5 points!')
else:
    print('You take 10 points!')

#5.5 проверка if-elif-else
print('\n#5.5')
alien_color = 'green'
if alien_color == 'red':
    print('You take 5 points!')
elif alien_color == 'yellow':
    print('You take 10 points!')
else:
    print('You take 15 points!')

#5.6 проверка if-elif-else
print('\n#5.6')
age = 18

if age <2:
    print('baby1')
elif age < 4:
    print('baby2')
elif age < 13:
    print('child')
elif age < 20:
    print('teenager')
elif age < 65:
    print('adult')
else:
    print('pensioner')

#5.8 проверка if in for
print('\n#5.8')

users = ['polina','zlata','kirill','admin','nikita']

for user in users:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {user.title()}, thank you for logging in again')

#5.9 проверка пустой список for in if
print('\n#5.9')

users = []
if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again')
else:
    print('We need to ind some users!')

#5.10 проверка if-elif-else in for
print('\n#5.10')

current_users = ['POLINA','zlata','kirill','admin','nikita']
new_users = ['polina','kira','kirill','radmir','senya']
upper_current_users = ['POLINA','ZLATA','KIRILL','ADMIN','NIKITA']

for user in new_users:
    if user in current_users:
        print(f'You must choose another nickname, {user.title()}')
    elif user in upper_current_users:
        print(f'You must choose another nickname, {user.title()}')
    else:
        print(f"You are welcome, {user.title()}!")

#5.11 проверка пустой список if in for
print('\n#5.10')

numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    if number <= 3:
        print(f'{number}th')
    else:
        print(f'{number}st')