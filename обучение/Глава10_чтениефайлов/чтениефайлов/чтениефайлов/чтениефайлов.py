#10.1 чтение файлов и вывод содержимого из них
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

#10.2 замена значение в каждой строке файла
print('\n#10.2')

with open(file) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

#10.3 запись информации в файл
print('\n#10.3')

filename  = 'guest.txt'

name  = input('What is your name: ')
with open(filename, 'a') as file_object:
    file_object.write(name.title() + '\n')