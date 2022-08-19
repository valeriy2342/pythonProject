class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} цвет {self.color} поехала,'

    def stop(self):
        return f'\nМашина {self.name} остановилась \n'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nМашина {self.name} едет со скоростью {self.speed}'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f'Машина привысила скорость, скорость {self.speed}'
        else:
            return f"Скорость автомобиля {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f'Машина привысила скорость, скорость {self.speed}'
        else:
            return f"Скорость автомобиля {self.speed}"


class PoliceCar(Car):
    pass


t = TownCar(60, "Баклажан", "Лада", False)
print(t.go(), t.show_speed(), t.turn('направо'), t.turn('налево'), t.stop())

t = TownCar(80, "Баклажан", "Лада", False)
print(t.go(), t.show_speed(), t.stop())

s = SportCar(280, "Красный", "Ferari", False)
print(s.go(), s.show_speed(), s.turn('налево'), s.stop(), s.go(), s.turn('направо'), s.turn('налево'), s.stop())

w = WorkCar(40, "Черный", "Билаз", False)
print(w.go(), w.show_speed(), w.turn('налево'), w.stop())

w = WorkCar(50, "Черный", "Билаз", False)
print(w.go(), w.show_speed(), w.stop())

p = PoliceCar(140, "Белый", "Ford", False)
print(p.go(), p.show_speed(), p.stop())
