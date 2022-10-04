import logging
import time


class Elevator:
    def __init__(self, floor_count, elevator_massa):
        self.elevator_massa = elevator_massa
        self.floor_count = floor_count
        self.units = []
        self.units_kg = 0
        self.count_units = 0
        self.weight_units = 0
        self.floor_location = 1
        self.weight = 0

    vov = input("Вызов лифта:")
    faf = input("Сколько людей поедет:")

    def move(self, floor_number):
        if floor_number <= self.floor_count:
            if self.units_kg <= self.elevator_massa:
                self.floor_location = floor_number
                print("Лифт запускается")
                print("Лифт начинает движение")
                print(f'Лифт находится на {floor_number} этаже\n')
                time.sleep(1.5)
                print("Через 1 секунду.")
            else:
                logging.warning("A WARNING")
                raise

    def add_unit(self, unit: list):
        floor = unit[0]
        weigth = unit[1]
        self.units.append(unit)
        self.units_kg += weigth
        self.count_units += 1
        print(f"Дверь открывается \n Зашел человек!\n\nЭтаж на котором  выйдет: :этаж: {floor} \nВес: {weigth}кг\n")

    def deleted_unit(self, i = 0):
        while i < self.count_units:
            if self.floor_location == self.units[i][0]:
                self.units_kg -= self.units[i][1]
                self.count_units -= 1
                self.units.pop(i)
                print("Человек вышел\n Дверь закрвыется")
            i += 1

class Human:

    def call_elevator(self, unit_location):
        elevator.move(unit_location)

    def massa(self, weight):
        self.weight = weight
        print(f"Вес человека:{weight}")

weight = 60

elevator = Elevator( 5 ,300)
human = Human()
elevator.move(1)
elevator.move(2)
human.call_elevator(3)
elevator.add_unit([5,weight])
elevator.move(4)
elevator.move(5)
elevator.deleted_unit()