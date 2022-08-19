class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):

    def draw(self):
        return f"Запуск отрисовки - {self.title}"


class Pencil(Stationery):

    def draw(self):
        return f"Запуск отрисовки - {self.title}"


class Handle(Stationery):

    def draw(self):
        return f"Запуск отрисовки - {self.title}"


pen = Pen('Рисую ручкой линии')
print(pen.draw())

pensil = Pencil("Штрихую карандашом")
print(pensil.draw())

handle = Handle("Обвожу маркером")
print(handle.draw())
