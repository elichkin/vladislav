class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Скорость бега: {self.speed} км/ч')
class Dog(Animal):
    def __init__(self, name, weight, speed):
        super().__init__(name, weight, speed)
    def wof(self):
        print('Woof')

my_dog = Dog('Diper', 28, 12)
print(my_dog.name)
print(my_dog.weight)
my_dog.wof()