class Person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print("vat mangso poau korma")
    
    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight,team):
        self.team = team
        super().__init__(name, age, height, weight)
    # override
    def eat(self):
        print("vegetables")
    

    def exercise(self):
        print('gym e poisa')
    
    def __add__(self, other):
        return self.age + other.age
    
    def __mul__(self, other):
        return self.weight * other.weight



sakib = Cricketer('sakir',30,34,23,'bd')

mushi = Cricketer('mishi',34,42,23,'bd')




#? plus sign overload

print(4 +3)
print('sakib' + 'rakib')
print([34,53] + [34,2,35,2])
print(sakib + mushi)
print(sakib * mushi)