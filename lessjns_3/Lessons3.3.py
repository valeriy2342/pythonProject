def num(x, y, z):
    numbers = [x, y, z]
    numbers.remove(min(x, y, z))
    return sum(numbers)


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

print(num(x, y, z))
