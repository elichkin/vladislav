class Animal:
    def __init__(self, name, weight, speed):
        self.name = name
        self.weight = weight
        self.speed = speed
    def run(self):
        print(f'Скорость бега: {self.speed} км/ч')

my_animal = Animal('Diper', 28, 12)

print(my_animal.name)
print(my_animal.weight)
my_animal.run()