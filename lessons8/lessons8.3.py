class Err:
    def __init__(self, *args):
        self.my_list = []

    def input_unit(self):

        while True:
            try:
                list_unit = int(input('Введите значение для добовления в список и нажимайте Enter - '))
                self.my_list.append(list_unit)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Неверный ввод - строка или булево")
                exit_unit = input(f'Ввести еще раз? Y/N ')

                if exit_unit == 'Y' or exit_unit == 'y':
                    print(my_except.input_unit())
                elif exit_unit == 'N' or exit_unit == 'n':
                    return f'ВЫХОД'
                else:
                    return f'ВЫХОД'


my_except = Err(1)
print(my_except.input_unit())
