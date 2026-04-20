class User:
    def __init__(self,name,age,money):
        self.__name = name
        self.__age = age 
        self.__money = money
    
    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self.__age
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter  # setter any value setter is set
    def salary(self,value):
        self.__money += value


s = User('kopa',34,12000)

# print(s.__money)

print(s.age)
print(s.salary)
s.salary = 99999
print(s.salary)

