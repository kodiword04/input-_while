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