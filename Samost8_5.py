class Animal:
    def make_noise(self):
        pass
class Dog(Animal):
    def make_noise(self):
        print('Woof... Woof... Woof')
class Cat(Animal):
    def make_noise(self):
        print('Meow... Meow... Meow')

my_dog = Dog()
my_cat = Cat()

my_dog.make_noise()
my_cat.make_noise()