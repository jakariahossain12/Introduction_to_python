from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("i need food")
    def move(self):
        pass


class Monkey(Animal):
    def __init__(self,name):
        self.category = 'mankey'
        self.name = name
        super().__init__()
    def eat(self):
        print("hey na nana i am eating banana")


k = Monkey("banor")
print(k.eat())