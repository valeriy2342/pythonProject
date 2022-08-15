def numbers():
    try:
        with open('text_5.txt', 'w+', encoding="utf-8") as f:
            my_numbers = input('Введите цифры через пробел \n')
            f.writelines(my_numbers)
            number = my_numbers.split()

            print(sum(map(int, number)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Ошибка ввода, попробуйте снова и введите число')


numbers()
