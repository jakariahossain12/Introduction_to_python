# poly --> many (multiple)
# morph --> shape

class Animal:
    def __init__(self,name):
        self.name = name
    
    def make_sound(self):
        print("animal making ome sound")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("meow meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def make_sound(self):
        print("gheu gheu")

don = Cat('rea')

fe = Dog("jjjj")

kh = Dog("dddd")

amilas = [ don,fe,kh]

for an in amilas:
    an.make_sound()