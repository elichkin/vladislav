class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Скорость бега: {self.speed} км/ч')

class Dog(Animal):
    def __init__(self, name, weight, speed, tail_length):
        super().__init__(name, weight, speed)
        self.__tail_length = tail_length
    def wof(self):
        print('Woof')
    def wag_tail(self):
        print(f'Дипер виляет хвостом размером {self.__tail_length} см')

my_dog = Dog('Diper', 28, 12, 8)
# print(my_dog.__tail_length) защищённый атрибут
my_dog.wag_tail()