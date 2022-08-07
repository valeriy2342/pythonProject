def num(x, y):
    return x / y


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

try:
    print(num(x, y))

except ZeroDivisionError:
    print('На ноль делить нельзя, попробуйте другое число')
