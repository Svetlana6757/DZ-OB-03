class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

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
        print(f"Животное {animal} добавлен в зоопарк")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member} добавлен в зоопарк")

class ZooKeeper:
    def feed_animal(self, animal):
        print(f"{animal.name} уже накормлен сотрудником.")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"{animal.name} уже вылечен ветеринаром.")

bird1 = Bird("Орел",5)
mammal1 = Mammal("Тигр", 6)
reptile1 = Reptile("Питон", 20)

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = Veterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)
zoo.add_staff(keeper)
zoo.add_staff(veterinarian)

animal_sound(zoo.animals)

keeper.feed_animal(mammal1)
veterinarian.heal_animal(reptile1)

import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as file:
        pickle.dump(zoo, file)

def load_zoo(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
