import random
import gc
spec = list('1234567890@#–—$_&-+()/*":;!?,.~`|^={}\%[]<>')
bk = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
obe = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#–—$_&-+()/*":;!?,.~`|^={}\%[]<>'
oben = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' 
f = open('C:\est\slovar3.txt', 'r+')
slovar = [i[:-1] for i in f]
print('*' * 52)
for i in range(30):
    if i == 15:
        print('*              здравствуйте,                       *')
        print('*     это программа для генерации паролей.         *')
        print('*     Она поможет сгенерировать уникальный ключ    *')
    elif i == 5:
        print('*  BY o2o                                V 1.0     *')
    elif i == 25:
        print('*  базу данных паролей легко                       *')
        print('*  изменить, при помощи замены/ред. файла          *')
        print('*  slovar3.txt по пути C:\est\slovar3.txt          *')
    elif i == 28:
        print('*  для продолжения нажмите ENTER                   *')
        print('*  для выхода введите "exit" (без кавычек)         *')
    else:
        print('*', ' ' * 48, '*')
print('*' * 52)
if input() != 'exit':
    print('*' * 32)
    for i in range(10):
        if i == 2:
            print('*    Выберите режим            *')
            print('*    работы программы ниже     *')
        elif i == 6:
            print('*  1) по ключевым словам       *')
            print('*  2) по длинне пароля         *')
            print('*  3) проверка пароля в базе   *')
            print('*  4) генерация любого пароля  *')
            print('*    (в диапозоне от 5 до 30)  *')
            print('*  5) генерация пароля         *')
            print('*     без спец символов        *')
            print('*                              *')
            print('*  для выхода нажмите ENTER    *')
        else:
            print('*', ' ' * 28, '*')
    print('*' * 32)
    x = input()
else:
    exit()
if x == '1':
    print('введите ключевые слова через запятую с пробелом')
    sps = str(input()).split(', ')
    st = ''
    while sps:
        st += random.choice(bk) + sps.pop() + random.choice(spec)
    print()
    print('-' * 10)
    print()
    print(st)
    print()
    print('-' * 10)
    print()
    print('Работа программы завершена')
elif x == '2':
    print('Введите длинну пароля')
    st = ''
    for i in range(int(input())):
        st += random.choice(obe)
    print()
    print('-' * 10)
    print()
    print(st)
    print()
    print('-' * 10)
    print()
    print('Работа программы завершена')
elif x == '3':
    print('Введите пароль, который вы хотите проверить')
    x = str(input()).lower()
    flag = False
    for i in slovar:
        if i in x:
            flag = True
    if x in slovar:
        print('Пароль слишком простой, он есть в словаре')
    elif flag:
        print('Ваш пароль не найден в словаре, но его стоит изменить')
    else:
        print('Ваш пароль не найден в словере, возможно он уникальный')
elif x == '4':
    spch = [int(i) for i in range(5, 30)]
    st = ''
    for i in range(random.choice(spch)):
        st += random.choice(obe)
    print(st)
elif x == '5':
    print('Введите длинну пароля')
    st = ''
    for i in range(int(input())):
        st += random.choice(oben)
    print()
    print('-' * 10)
    print()
    print(st)
    print()
    print('-' * 10)
    print()
    print('Работа программы завершена')
print('для выхода нажмите любую клавишу')
input()
gc.collect()