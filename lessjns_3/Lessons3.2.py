def info(a, e, c, d, b, f):
    return f' Вас зовут {second_name} {name} , вы родились {date} в городе {town}. Ваш email {email}, телефон {number}'


name = input('Введите ваше имя: ')
second_name = input('Введите вашу фамилию: ')
date = input('Введите дату вашего рождения: ')
town = input('Введите место вашего рождения: ')
email = input('Введите ваш email: ')
number = input('Введите ваш телефон: ')

print(info(a=name, b=second_name, c=date, d=town, e=email, f=number))
