#10.1 ������ ������ � ����� ����������� �� ���
print('#10.1')

file = 'learning_python.txt'
with open(file) as file_object:
    string = file_object.read()

print(string.rstrip())

print('')

with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())

print('')

with open(file) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())

#10.2 ������ �������� � ������ ������ �����
print('\n#10.2')

with open(file) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

#10.3 ������ ���������� � ����
print('\n#10.3')

# filename  = 'guest.txt'

# name  = input('What is your name: ')
# with open(filename, 'a') as file_object:
#     file_object.write(name.title() + '\n')

#10.4 ������ ���������� � ���� � ������� �����
print('\n#10.4')

# filename  = 'guest_book.txt'

# active = True
# while active:
#     name  = input("Enter 'stop' if you want leave\nWhat is your name: ")
#     if name != 'stop':
#         with open(filename, 'a') as file_object:
#             file_object.write(name.title() + '\n')
#         print(f'Hello, {name.title()}')
#     else:
#         active = False

#10.5 ������ ���������� � ���� � ������� �����
print('\n#10.5')
# filename  = 'survey.txt'

# active = True
# while active:
#     answer  = input("Enter 'stop' if you want leave\nWhy are you like to code: ")
#     if answer != 'stop':
#         with open(filename, 'a') as file_object:
#             file_object.write(answer + '\n')
#     else:
#         active = False