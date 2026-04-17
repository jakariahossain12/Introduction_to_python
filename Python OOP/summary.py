class Book:
    def __init__(self,name):
        self.name = name
    def read(self):
        raise NotImplementedError

class Physics(Book):
    def __init__(self, name,lab):
        self.lab = lab
        super().__init__(name)


topon = Physics("topon",True)

print(issubclass(Physics,Book))
print(isinstance(topon,Physics))
print(isinstance(topon,Book))

topon.read()