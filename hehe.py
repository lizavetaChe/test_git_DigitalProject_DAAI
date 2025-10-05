from datetime import datetime

def format(date):
    if date[2] in '0123456789':
        date = '.'.join(date.split(date[4])[::-1])
    else:
        date = '.'.join(date.split(date[2]))
    return date

def helloworld(w):
    if w == 'print':
        print('Hello World!')
    elif w == 'hello':
        name = input('Введите ваше имя: ')
        print(f'Привет, {name}!')
    elif w == 'y/o':
        data = input('Введите дату вашего рождения:')
        d1 = datetime.strptime(format(data), "%d.%m.%Y")
        d2 = datetime.now()
        yo = d2.year - d1.year
        if (d2.month, d2.day) < (d1.month, d1.day):
            yo -= 1
        if yo < 0:
            print('Скорее всего вы живете в другой вселенной')
        else:
            print(f'Вам {yo} лет(года)')
    elif w == 'time':
        print('Сейчас:', datetime.now())
    else:
        print('Error')
        
helloworld('print')
helloworld('time')
helloworld(123)
helloworld('hello')
helloworld('y/o')