# Task 1.
from time import sleep


class TrafficLight:
    __color = ['Красный', 'Жёлтый', 'Зелёный']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается: '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(5)
            elif i == 2:
                sleep(3)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()


# Task 2.
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def intake_road(self):
        self.weigth = 35
        self.tickness = 0.07
        intake = self._length * self._width * self.weigth * self.tickness / 1000
        print(f'Необходимо {intake} тонн для строительства дороги')


road_1 = Road(9000, 6)
road_1.intake_road()


# Task 3.
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Position('Robert', 'Downey Jr', 'Actor', 1000000, 500000)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_total_income())


# Task 4.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула " + direction)

    def show_speed(self):
        print(f"Скорость {self.name} {self.speed} км/ч")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} выше разрешённой. Соблюдайте скоростной режим!')
        else:
            print(f'Машина {self.name} двигается с разрешённой скоростью.')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} выше разрешённой. Соблюдайте скоростной режим!')
        else:
            print(f'Машина {self.name} двигается с разрешённой скоростью.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'{self.name} это полицейская машина')


opel = TownCar(55, 'Бирюзовый', 'Opel', False)
ferrari = SportCar(150, 'Жёлтый', 'Ferrari', False)
truck = WorkCar(70, 'Серый', 'КамАЗ', False)
skoda = PoliceCar(110, 'Белый с синими полосами', 'Skoda', True)


print(ferrari.name, ferrari.color)
ferrari.show_speed()
opel.go()
opel.turn('Налево')
opel.stop()
truck.show_speed()
print(skoda.name, skoda.color, skoda.speed)
skoda.police()


# Task 5.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}.')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером.')


pen = Pen('Ручка Pilot')
pencil = Pencil('Карандаш STABILO Trio')
handle = Handle('Маркер ProMarkers')
pen.draw()
pencil.draw()
handle.draw()