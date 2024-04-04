class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def make_sound(self):

    def eat(self):
        print(f"{self.name} сейчас ест.")

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} чирикают")


class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} лают, мяукают, мычат")


class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print(f"{self.name} шипят")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{animal.name} уже накормлен сотрудником.")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"{animal.name} уже вылечен ветеринаром.")


import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)

def load_zoo(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
