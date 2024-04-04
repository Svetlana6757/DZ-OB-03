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
        print(f"{self.name} поет чирик-чирик")


