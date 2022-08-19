class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(self.position + ' ' + self.surname + ' ' + self.name)

    def get_total_income(self):
        print(f'Общий доход {self._income["wage"] + self._income["bonus"]} рублей')


x = Position('Валерий', 'Хуранов', 'Инженер', 100000, 150000)

x.get_full_name()
x.get_total_income()
