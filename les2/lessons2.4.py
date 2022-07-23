str = (input('Введите несколько слов через пробел ')).split()

for i, v in enumerate(str, 1):
    print(f'{i}) {v}')
