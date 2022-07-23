plus = int(input('Ведите сумму выручки вашей компании в рублях: '))
minus = int(input('Введите сумму издержек компании в рублях: '))

resalt = plus // minus * 100
res_pius = plus - minus

if plus > minus:
    print(
        f'Ваша выручка больше издержек компании. Вы заработали {res_pius} рублей. Рентабильность компании составила {resalt} %')
elif plus == minus:
    print('Ваша компания отработала в ноль')
else:
    print(
        f'издержки компании больше выручки компании. Вы потратили {res_pius} рублей Рентабильность компании составила {resalt} %')

sotrudnik = int(input('Введите колличество сотрудников вашей компании: '))

plus_sotrudnik = plus // sotrudnik
print(f'Средняя выручка сотрудника составляет {plus_sotrudnik} руб')
