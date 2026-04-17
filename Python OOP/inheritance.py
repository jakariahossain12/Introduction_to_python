
# base class parent class common attribute + functionality class
# derived class child class uncommon attribute + functionality class

class Device:
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        return f'Running laptop : { self.brand}'
    


class Laptop:
    def __init__(self,memory,ssd):
        self.memory = memory
        self.ssd = ssd
    
    
    def coding(self):
        return f'learning python and practicing'


class Phone(Device):
    def __init__(self,dual_sim,brand,price,color):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color)
    
    
    def phone_call(self,number,text):
        return f'sending sms to : {number} with {text}'
    
    def __repr__(self):
        return f'phone : {self.dual_sim} {self.brand} {self.price} {self.color}'


my_phone = Phone(True,"samsun",20000,"black")

print(my_phone)